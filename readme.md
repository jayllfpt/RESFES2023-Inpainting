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
Note that the following result maybe not as good as the paper because **they are trained only in 1 epoch**. You can get the final result in original author's github. 
### train
<p align="center">
  <img src="imgs/image9.png">
  <img src="imgs/image11.png">

</p>

### test
<p align="center">
  <img src="imgs/image14.png">
  <img src="imgs/image8.png">
  <img src="imgs/image10.png">
  <img src="imgs/image16.png">
</p>

### loss
<p align="center">
  <img src="imgs/loss_curve.png">
</p>

## Prepair the dataset
<br>See more details in the paper.</br>
![Ye-Sure's Paper]([https://github.com/jayllfpt/CVPong1972/blob/main/demo.gif](https://github.com/jayllfpt/RESFES2023-Inpainting/blob/main/Full_paper_HCMU.pdf))

## How to test

You can specify the folder address by the option --dataset_path, and set the pretrained model path by --load_model_dir when calling test.py as the following

```
python test.py 
```
**We train it 40 epochs with single GPU**, you can train it yourself for better performance or in custom dataset.

## How to train
Use train.py as the following 
```
python train.py --dataset_path yesuredata/train --data_file yesuretxt/train.txt --batch_size 4 --lr 2e-4
```
You can load the pretrained model by the option --load_model_dir too.

## Refs

- [x] 中文博客(https://blog.csdn.net/h8832077/article/details/105166776)
