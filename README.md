# AECR-Net

Contrastive Learning for Compact Single Image Dehazing, CVPR2021. Official Pytorch based implementation. 

## Paper

[arxiv](https://arxiv.org/abs/2104.09367)

![](img/aecrnet.png)

<img src="img/example.png" style="zoom:38%;" />

### Pytorch Version

- [x] model
- [x] CR loss
- [x] pretrained models

### MindSpore Version

https://github.com/Booooooooooo/AECRNet-MindSpore by @wyb

## Performance

![](img/performance.png)

## Others

**Pretrained models:**

https://pan.baidu.com/s/13crsXwwhkI5A3MlHtPihuA  password: xhyi


## 22-09-25 Update

### Directory Tree
```
.
├── create_dataset.py
├── datasets
│   ├── ITS_test
│   └── ITS_train
├── data_utils
│   ├── DH.py
│   ├── ITS_h5.py
│   ├── NH.py
│   └── __pycache__
├── img
│   ├── aecrnet.png
│   ├── example.png
│   ├── performance.png
│   └── trade_off.png
├── ITS_v2
│   ├── clear
│   ├── clear.zip
│   ├── hazy
│   ├── hazy.zip
│   ├── trans
│   └── trans.zip
├── logs
│   ├── ITS_train_cdnet_test
│   ├── its_train_ffa_test
│   └── ITS_train_ffa_test
├── logs_train
│   ├── args_ITS_train_cdnet_test.txt
│   ├── args_its_train_ffa_test.txt
│   ├── args_ITS_train_ffa_test.txt
│   └── ITS_train_cdnet_test.txt
├── metrics.py
├── models
│   ├── AECRNet.py
│   ├── CR.py
│   ├── DCNv2
│   ├── DCNv2.zip
│   ├── deconv.py
│   └── __pycache__
├── numpy_files
├── option.py
├── README.md
├── requirements
├── samples
│   ├── ITS_train_cdnet_test
│   ├── its_train_ffa_test
│   └── ITS_train_ffa_test
├── test.py
├── train_aecrnet.py
└── trained_models
    ├── ITS_train_cdnet_test.pk
    └── ITS_train_cdnet_test.pk.best
```