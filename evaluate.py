import torch
import torch.nn.functional as F
import os
import cv2
from torchmetrics import PeakSignalNoiseRatio, TotalVariation

if os.path.isfile(r"evaluateFiles.txt"):
    pathfile = open(r"evaluateFiles.txt", 'rt').read().splitlines()

def calculate_l1_loss(image1, image2):
    tensor1 = torch.from_numpy(image1.transpose((2, 0, 1))).float() 
    tensor2 = torch.from_numpy(image2.transpose((2, 0, 1))).float() 
    return F.l1_loss(tensor1, tensor2)

def calculate_l2_loss(image1, image2):
    tensor1 = torch.from_numpy(image1.transpose((2, 0, 1))).float() 
    tensor2 = torch.from_numpy(image2.transpose((2, 0, 1))).float() 
    return F.mse_loss(tensor1, tensor2)

def calculate_psnr(image1, image2):
    tensor1 = torch.from_numpy(image1.transpose((2, 0, 1))).float() 
    tensor2 = torch.from_numpy(image2.transpose((2, 0, 1))).float() 
    mse = F.mse_loss(tensor1, tensor2)
    psnr = 10 * torch.log10(1 / mse)
    return psnr

def calculate_tv_loss(image):
    tensor = torch.from_numpy(image.transpose((2, 0, 1))).float() 
    h_tv = torch.sum(torch.abs(tensor[:, :, :-1] - tensor[:, :, 1:]))
    v_tv = torch.sum(torch.abs(tensor[:, :-1, :] - tensor[:, 1:, :]))
    tv_loss = h_tv + v_tv
    return tv_loss


l1 = 0.0
l2 = 0.0
psnr = 0.0
tv = 0.0

for i in range(15):
    images = cv2.imread(r"yesureresult/"+ pathfile[3*i])
    x2 = cv2.imread(r"yesureresult/"+ pathfile[3*i + 2])
    print(pathfile[3*i], pathfile[3*i + 2])

    l1 += calculate_l1_loss(x2, images)
    l2 += calculate_l2_loss(x2, images)
    psnr += calculate_psnr(x2, images)
    tv += calculate_tv_loss(x2)


print("L1", l1 / 15)
print("L2", l2 / 15)
print("PSNR", psnr / 15)
print("TV", tv / 15)
print("Done")