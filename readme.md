## DMFN (Dense Multi-scale Fusion Network)

This is an unoffical repository for reproducing model DMFN from the paper [[Image Fine-grained Inpainting]](https://arxiv.org/abs/2002.02609). The original repository is [here](https://github.com/Zheng222/DMFN), but author have not commit the rest of implement code yet. 

<p align="center">
  <img src="imgs/DMFN.png">
</p>

## Prerequisites
- Python3.5 (or higher)
- pytorch 1.0(or higher) with GPU
- numpy
- OpenCV
- scipy
- tensorboardX


## RESULT

### Dataset
<p align="center">
  <img src="imgs/image9.png">
  <img src="imgs/image11.png">

</p>

### Result
<p align="center">
  <img src="imgs/image14.png">
  <img src="imgs/image8.png">
  <img src="imgs/image10.png">
  <img src="imgs/image16.png">
  <img src="imgs/res1.png">
  <img src="imgs/res2.png">
  <img src="imgs/res3.png">
</p>

## Prepair the dataset images
contact us: yesure2023@gmail.com

## How to test

You can specify the folder address by the option --dataset_path, and set the pretrained model path by --load_model_dir when calling test.py as the following

```
python test.py --dataset yesuredata/test --data_file yesuretxt/test.txt --load_model_dir checkpoints/40_net_DFBN.pth
```
**We train it 40 epochs with single GPU - GTX 1650**, you can train it yourself for better performance or in custom dataset.

## How to train
Use train.py as the following 
```
python train.py --dataset_path data_final --data_file yesuretxt/train1.txt --batch_size 4 --lr 2e-4 --epochs 40 --load_model_dir checkpoints/40_net_DFBN.pth
```
You can load the pretrained model by the option --load_model_dir and edit default params in 2 python files in 'options' folder, too.

## Refs

- [x] 中文博客(https://blog.csdn.net/h8832077/article/details/105166776)
