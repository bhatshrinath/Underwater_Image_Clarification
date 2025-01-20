import os
import numpy as np
import cv2
import natsort
import datetime
import streamlit as st
import time
import base64
import io

from PIL import Image
from GuidedFilter import GuidedFilter
from backgroundLight import BLEstimation
from depthMapEstimation import depthMap
from depthMin import minDepth
from getRGBTransmission import getRGBTransmissionESt
from global_Stretching import global_stretching
from refinedTransmissionMap import refinedtransmissionMap
from sceneRadiance import sceneRadianceRGB
from LabStretching import LABStretching
from color_equalisation import RGB_equalisation
from global_stretching_RGB import stretching
from relativeglobalhistogramstretching import RelativeGHstretching
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio

def calculate_psnr(img1, img2):
    # The two images must be the same size
    assert img1.shape == img2.shape, "Input images must have the same dimensions."
    
    # Calculate PSNR
    return peak_signal_noise_ratio(img1, img2, data_range=img2.max() - img2.min())


def calculate_ssim(img1, img2):
    # The two images must be the same size
    assert img1.shape == img2.shape, "Input images must have the same dimensions."
    
    # Convert the images to grayscale
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Calculate SSIM
    return ssim(img1_gray, img2_gray)

def get_image_download_link(img, filename, text):
    encoded = base64.b64encode(img).decode()
    href = f'<a href="data:image/jpeg;base64,{encoded}" download="{filename}" style="display: block; text-align: center; padding: 10px; color: white; background-color: #FF6347; border: none; border-radius: 4px; text-decoration: none;">{text}</a>'
    return href

np.seterr(over='ignore')

def main():
    st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
            color: #808080;
            font-weight: bold;
            text-shadow: 2px 2px #000000;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Underwater Image Clarification</p>', unsafe_allow_html=True)

    # Custom CSS
    st.markdown("""
    <style>
    body {
        background-color: #FFF8DC;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "jfif"])
    if uploaded_file is not None:
        img = np.array(Image.open(uploaded_file))
        st.image(img, caption='Uploaded Image', use_column_width=True)

        st.sidebar.markdown("## Image Processing Parameters")

        st.sidebar.markdown("### Block Size")
        blockSize = st.sidebar.slider('The block size for the guided filter. Larger values give more smoothing but slower speed.', min_value=1, max_value=20, value=9)

        st.sidebar.markdown("### GimfiltR")
        gimfiltR = st.sidebar.slider('The range radius for the guided filter. Larger values give more smoothing but slower speed.', min_value=1, max_value=100, value=50)

        st.sidebar.markdown("### Eps")
        eps = st.sidebar.slider('Epsilon for the guided filter. A small value gives more details.', min_value=1, max_value=100, value=10, step=1, format="%e")


        if st.button('Process Image'):
            with st.spinner('Processing...'):
                progress_bar = st.progress(0)
                status_text = st.empty()

                try:
                    #IMAGE ENHANCEMENT using RGHS
                    status_text.text('Enhancing image using RGHS...')
                    sceneRadiance = img
                    sceneRadiance = stretching(sceneRadiance)
                    progress_bar.progress(10)  # 10% progress

                    sceneRadiance = LABStretching(sceneRadiance)
                    progress_bar.progress(20)  # 20% progress

                    # Normalize the image data to the range [0, 1]
                    sceneRadiance_normalized = (sceneRadiance - np.min(sceneRadiance)) / (np.max(sceneRadiance) - np.min(sceneRadiance))

                    st.image(sceneRadiance_normalized, caption='IMAGE ENHANCEMENT using RGHS', use_column_width=True)

                    # Convert the normalized image to PIL Image
                    img_pil = Image.fromarray(np.uint8(sceneRadiance_normalized*255))

                    # Create BytesIO object
                    img_io = io.BytesIO()
                    img_pil.save(img_io, 'JPEG', quality=85)
                    img_io.seek(0)

                    # Get bytes data
                    img_bytes = img_io.getvalue()

                    # Create download link
                    st.markdown(get_image_download_link(img_bytes, 'image_enhanced_using_RGHS.jpg', 'Download image enhanced using RGHS'), unsafe_allow_html=True)

                    # Save the processed image
                    status_text.text('Saving RGHS processed image...')
                    cv2.imwrite('InputImagesULAP/' + 'rghs_processed_RGHS.jpg', sceneRadiance)
                    progress_bar.progress(30)  # 30% progress

                    #IMAGE COLOR RESTORATION using ULAP
                    status_text.text('Restoring image color using ULAP...')
                    img_new = cv2.imread('InputImagesULAP/' + 'rghs_processed_RGHS.jpg')
                    progress_bar.progress(40)  # 40% progress

                    DepthMap = depthMap(img_new)
                    DepthMap = global_stretching(DepthMap)
                    progress_bar.progress(50)  # 50% progress

                    guided_filter = GuidedFilter(img_new, gimfiltR, eps)
                    refineDR = guided_filter.filter(DepthMap)
                    refineDR = np.clip(refineDR, 0,1)
                    progress_bar.progress(60)  # 60% progress

                    AtomsphericLight = BLEstimation(img_new, DepthMap) * 255
                    progress_bar.progress(70)  # 70% progress

                    d_0 = minDepth(img_new, AtomsphericLight)
                    d_f = 8 * (DepthMap + d_0)
                    transmissionB, transmissionG, transmissionR = getRGBTransmissionESt(d_f)
                    progress_bar.progress(80)  # 80% progress

                    transmission = refinedtransmissionMap(transmissionB, transmissionG, transmissionR, img_new)
                    sceneRadiancenew = sceneRadianceRGB(img_new, transmission, AtomsphericLight)
                    progress_bar.progress(90)  # 90% progress

                    st.write('Processed Image:')

                    # Normalize the image data to the range [0, 1]
                    sceneRadiancenew_normalized = (sceneRadiancenew - np.min(sceneRadiancenew)) / (np.max(sceneRadiancenew) - np.min(sceneRadiancenew))

                    st.image(sceneRadiancenew_normalized, caption='IMAGE COLOR RESTORATION using ULAP', use_column_width=True)

                    # Convert image to .jpg format
                    status_text.text('Finalizing...')

                    # Convert color space from BGR to RGB
                    sceneRadiancenew_rgb = cv2.cvtColor(sceneRadiancenew, cv2.COLOR_BGR2RGB)

                    # Encode the image
                    _, img_encodednew = cv2.imencode('.jpg', sceneRadiancenew_rgb)

                    # Calculate SSIM
                    ssim_value = calculate_ssim(img, sceneRadiancenew)
                    ssim_value_rounded = round(ssim_value, 2)  # Round to 2 decimal places
                    st.info("To evaluate the performance of the image processing pipeline, the Structural Similarity Index (SSIM) is used which is a method for comparing similarities between two images. The SSIM value can range from -1 to 1, where 1 means the two images are identical.")
                    st.info(f"SSIM: {ssim_value_rounded}")

                    psnr_value = calculate_psnr(img, sceneRadiancenew)
                    psnr_value_rounded = round(psnr_value, 2)  # Round to 2 decimal places
                    st.info("The Peak Signal-to-Noise Ratio (PSNR) is a measure of quality of lossy compression codecs (e.g., for image compression). The signal in this case is the original data, and the noise is the error introduced by compression. A higher PSNR indicates that the reconstruction is of higher quality. PSNR of 10 dB and above is considered good image quality")
                    st.info(f"PSNR: {psnr_value_rounded}")

                    # Create download link
                    st.markdown(get_image_download_link(img_encodednew, 'processed_image.jpg', 'Download processed image'), unsafe_allow_html=True)

                    progress_bar.progress(100)  # 100% progress

                    status_text.text('Done!')

                except Exception as e:
                    st.error(f"Error processing image: {e}")

if __name__ == '__main__':
    main()