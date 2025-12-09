# Two-branch Dehazing - 非均匀去雾双分支网络

> **声明**: 本仓库是论文 *"A Two-Branch Neural Network for Non-Homogeneous Dehazing via Ensemble Learning"* 的**非官方复刻**，仅供学习和研究使用。本人并非原论文作者。

该方法在 NTIRE 2021 非均匀去雾挑战赛中获得亚军。

## 相关链接

- [挑战赛报告](https://openaccess.thecvf.com/content/CVPR2021W/NTIRE/papers/Ancuti_NTIRE_2021_NonHomogeneous_Dehazing_Challenge_Report_CVPRW_2021_paper.pdf)
- [原论文](https://openaccess.thecvf.com/content/CVPR2021W/NTIRE/papers/Yu_A_Two-Branch_Neural_Network_for_Non-Homogeneous_Dehazing_via_Ensemble_Learning_CVPRW_2021_paper.pdf)
- [获奖证书](https://data.vision.ee.ethz.ch/cvl/ntire21/NTIRE2021awards_certificates.pdf)

## 环境配置

本项目使用 [uv](https://github.com/astral-sh/uv) 进行依赖管理。

### 依赖项

- Python >= 3.12
- PyTorch
- torchvision
- opencv-python
- scikit-image
- tensorboardX

### 安装步骤

```shell
# 安装 uv (如果尚未安装)
pip install uv

# 同步项目依赖
uv sync
```

## 预训练权重与数据集

- 下载 [ImageNet 预训练权重](https://drive.google.com/file/d/1aZQyF16pziCxKlo7BvHHkrMwb8-RurO_/view?usp=sharing) 和 [模型权重](https://drive.google.com/file/d/1M2n6g7S5_sqPmTIAuI-IC30fhUmQr199/view?usp=sharing)
- 下载 [数据集](https://drive.google.com/drive/folders/1eeBA2V_l9-evSJ0XWhRAww6ftweq8hU_?usp=sharing)

训练集对 NH-HAZE-2020 进行了伽马校正处理。测试集由训练集中随机抽取的样本组成，用于评估训练效果。如需获取 NH-HAZE-2021 的验证和测试精度，请前往[官方比赛服务器](https://competitions.codalab.org/competitions/28032#learn_the_details-overview)。

## 使用方法

### 训练

```shell
python train.py --data_dir data -train_batch_size 8 --model_save_dir train_result
```

### 测试

```shell
python test.py --model_save_dir results
```

## 引用

如果您在研究中使用了本代码，请引用原论文：

```bibtex
@InProceedings{Yu_2021_CVPR,
    author    = {Yu, Yankun and Liu, Huan and Fu, Minghan and Chen, Jun and Wang, Xiyao and Wang, Keyan},
    title     = {A Two-Branch Neural Network for Non-Homogeneous Dehazing via Ensemble Learning},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    month     = {June},
    year      = {2021},
    pages     = {193-202}
}
```



