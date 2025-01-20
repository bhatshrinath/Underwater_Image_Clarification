# encoding=utf-8
import os
import numpy as np
import cv2
import natsort
import datetime

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

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

starttime = datetime.datetime.now()

#RGHS Processing  
folder = "C:/Users/40102982/Downloads/Underwater_Image_Clarification"
path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        img = cv2.imread(folder +'/InputImages/' + file)
        height = len(img)
        width = len(img[0])

        sceneRadiance = img

        sceneRadiance = stretching(sceneRadiance)

        sceneRadiance = LABStretching(sceneRadiance)

        cv2.imwrite('InputImagesULAP/' + prefix + '_RGHS.jpg', sceneRadiance)
        
#ULAP Processing        
path = folder + "/InputImagesULAP"
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)        
        
        img_new = cv2.imread(folder +'/InputImagesULAP/' + file)

        blockSize = 9
        gimfiltR = 50
        eps = 10 ** -3

        DepthMap = depthMap(img_new)
        DepthMap = global_stretching(DepthMap)
        guided_filter = GuidedFilter(img_new, gimfiltR, eps)
        refineDR = guided_filter.filter(DepthMap)
        refineDR = np.clip(refineDR, 0,1)

        cv2.imwrite('OutputImages/' + prefix + '_ULAPDepthMap.jpg', np.uint8(refineDR * 255))

        AtomsphericLight = BLEstimation(img_new, DepthMap) * 255

        d_0 = minDepth(img_new, AtomsphericLight)
        d_f = 8 * (DepthMap + d_0)
        transmissionB, transmissionG, transmissionR = getRGBTransmissionESt(d_f)

        transmission = refinedtransmissionMap(transmissionB, transmissionG, transmissionR, img_new)
        sceneRadiance = sceneRadianceRGB(img_new, transmission, AtomsphericLight)

        cv2.imwrite('OutputImages/' + prefix + '_ULAP_TM.jpg', np.uint8(transmission[:, :, 2] * 255))
        cv2.imwrite('OutputImages/' + prefix + '_ULAP.jpg', sceneRadiance)

Endtime = datetime.datetime.now()
Time = Endtime - starttime
print('Time', Time)