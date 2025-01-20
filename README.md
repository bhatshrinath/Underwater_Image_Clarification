# Underwater Image Clarification

This project is designed to enhance the quality of underwater images by applying a series of image processing techniques. The architecture of the project is set up such that the output of one step serves as the input for the next step, making the system modular and easy to maintain and update.

## Architecture
a. **Image Acquisition:** The system reads underwater images from a specified directory. These images serve as the input for the system.

b. **RGB Histogram Stretching (RGHS) Processing:**

    1. Pre-processing : The system applies RGB histogram stretching and LAB color space stretching to each image. RGB histogram stretching enhances the global contrast of the images by stretching the range of color values. LAB color space stretching balances the color distribution across the LAB color space, which is designed to approximate human vision. The output of this stage is a set of images that are ready for further processing.
    
    2. Depth Map Estimation: The system estimates the depth map of each pre-processed image. The depth map represents the distance of the objects in the scene from the camera, which is a crucial factor in underwater image enhancement.

    3. Global Stretching: This technique is used to enhance the contrast of the image. It operates by stretching the range of intensity values in the image to span a desired range, typically the full range of pixel values. This can help to improve the visibility of features in the image by maximizing the use of available dynamic range. It's particularly useful in underwater image enhancement where the contrast is often poor due to scattering and absorption of light.

c. **Underwater Light Absorption and Propagation (ULAP) Processing:** 

    1. Background Light Estimation: The system estimates the background light (Atmospheric Light) of each image using the depth map. The background light represents the light that is not reflected by any object in the scene and reaches the camera directly from the light source.

    2. Transmission Map Estimation: The system calculates the transmission map of each image, which represents the portion of the light that is not scattered and reaches the camera.

    3. Scene Radiance Calculation: The system calculates the scene radiance of each image using the transmission map and the background light. The scene radiance represents the light that is reflected by the objects in the scene and reaches the camera.

    4. Image Enhancement : The system applies a guided filter to refine the depth map, refines the transmission map, and recalculates the scene radiance. This step further enhances the quality of the images.

d. **Image Output:** The system saves the enhanced images to a specified directory.

## Evaluation
 - The performance of the image processing pipeline is evaluated using the Structural Similarity Index (SSIM). The SSIM is a method for comparing similarities between two images. The SSIM value can range from -1 to 1, where 1 means the two images are identical.
 - The Peak Signal-to-Noise Ratio (PSNR) is a measure of quality of lossy compression codecs (e.g., for image compression). The signal in this case is the original data, and the noise is the error introduced by compression. A higher PSNR indicates that the reconstruction is of higher quality. PSNR of 10 dB and above is considered good image quality.

## System Requirements

- Python 3.6 or higher
- OpenCV library
- Numpy library
- A machine with at least 4GB of RAM

*Note: This is a basic requirement. Depending on the size and quantity of the images you are processing, you might need a machine with higher specifications.*

## Installation

1. Install Python 3.6 or higher if you haven't already. You can download it from the official website: https://www.python.org/downloads/

2. Install the required Python libraries:
    ```
    pip install -r requirements.txt
    ```

3. To create a Python environment using the `requirements.txt` file, follow these steps:

    a. Open a terminal (Command Prompt, PowerShell, or Terminal in Linux/Mac).

    b. Navigate to the directory containing the `requirements.txt` file. You can use the `cd` command followed by the path to the directory. For example:

    ```bash
    cd path/to/directory
    ```

    c. Create a new virtual environment. If you're using `venv` (included in standard Python 3.3 and later), you can do this with the following command:

    ```bash
    python3 -m venv env
    ```

    This creates a new virtual environment named `env` in the current directory.

    d. Activate the virtual environment. The command to do this depends on your operating system:

    - On Windows:

    ```bash
    .\env\Scripts\activate
    ```

    - On Unix or MacOS:

    ```bash
    source env/bin/activate
    ```

    e. Once the virtual environment is activated, you can install the requirements using pip:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the Python packages listed in the `requirements.txt` file in your new virtual environment.

    f. Next steps:
    - Run your Python script in this environment.
    - Deactivate the environment when you're done using the `deactivate` command.

## Usage (Local Run)

1. Change the path in the main.py script
    - folder = "/path/to/your/images"

2. Place your input images in the `InputImages` directory.

3. Run the main script:
    ```
    python main.py
    ```

4. The enhanced images will be saved in the `OutputImages` directory.

## Usage (Streamlit Web App)

1. Run the Streamlit app:
    ```
    streamlit run streamlit_app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the file uploader in the Streamlit app to upload your input images.

4. The app will process the images and display the enhanced images.

## Directory Diagram

 - InputImages
 - OutputImages
 - main.py
 - streamlit_app.py
 - backgroundLight.py
 - color_equalisation.py
 - depthMapEstimation.py
 - depthMin.py
 - desiredRange.py
 - getRGBTransmission.py
 - global_stretching_ab.py
 - global_stretching_RGB.py
 - global_stretching.py
 - global_stretchingL.py
 - GuidedFilter.py
 - LabStretching.py
 - refinedTransmissionMap.py
 - relativeglobalhistogramstretching.py
 - S_model.py
 - sceneRadiance.py
 - stretchRange.py
 - README.md
 - requirements.txt
