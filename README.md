# Project

This repository contains bird classification project.
Model used in this project is MobileNet, which is pretrained on ImageNet. 

## Basic setups
./logs contains files for tensorboard for visualizing training process.
./output contains model data, which can be used for inference

## To Test:
Run directly will load test files in ./test folder and perform testing procedure
_python main.py --mode=test_ to test and it will report metrics.

## To train:
Go to terminal, cd to this folder and type:
_python main.py --mode=train_ to train the neural network. 


## Options to run (hyperparameters and setup)
Since argparse is implemented, it is able to use additional argument to change code settings:

$ python3 main.py 

add *--output_dir=value* to change output directory
add *--epoch=value* to change epoch size
add *--learning_rate=value* to change learning rate
add *--train_batch_size=size* to change training batch size
add *--train_data_path=path* to change training data batch path

add *--traindata_size=value* to change training data size
add *--valdata_size=value* to change validation data size
add *--model=VGG16, VGG19, MobileNet* to change training neural network

## Dependencies

All dependencies are recoreded in requirements.txt

To install, use the following code:

'''
pip install -r requirements.txt 
'''

