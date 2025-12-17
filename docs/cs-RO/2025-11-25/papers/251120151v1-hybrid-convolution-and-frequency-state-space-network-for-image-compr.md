---
layout: default
title: Hybrid Convolution and Frequency State Space Network for Image Compression
---

# Hybrid Convolution and Frequency State Space Network for Image Compression

**arXiv**: [2511.20151v1](https://arxiv.org/abs/2511.20151) | [PDF](https://arxiv.org/pdf/2511.20151.pdf)

**作者**: Haodong Pan, Hao Wei, Yusong Wang, Nanning Zheng, Caigui Jiang

---

## 💡 一句话要点

**提出HCFSSNet混合网络，结合卷积与频率状态空间以提升学习图像压缩性能**

**关键词**: `学习图像压缩` `混合网络架构` `频率状态空间` `自适应频率调制` `熵模型优化`

## 📋 核心要点

1. 核心问题：Transformer和状态空间模型在图像压缩中可能忽略局部高频细节和频率特性
2. 方法要点：使用CNN提取局部高频结构，VFSS块建模长程低频信息并集成AFMM优化比特分配
3. 实验或效果：在Kodak等数据集上BD率降低18-24%，参数更少，性能优于MambaIC

## 📄 摘要（原文）

> Learned image compression (LIC) has recently benefited from Transformer based and state space model (SSM) based architectures. Convolutional neural networks (CNNs) effectively capture local high frequency details, whereas Transformers and SSMs provide strong long range modeling capabilities but may cause structural information loss or ignore frequency characteristics that are crucial for compression. In this work we propose HCFSSNet, a Hybrid Convolution and Frequency State Space Network for LIC. HCFSSNet uses CNNs to extract local high frequency structures and introduces a Vision Frequency State Space (VFSS) block that models long range low frequency information. The VFSS block combines an Omni directional Neighborhood State Space (VONSS) module, which scans features horizontally, vertically and diagonally, with an Adaptive Frequency Modulation Module (AFMM) that applies content adaptive weighting of discrete cosine transform frequency components for more efficient bit allocation. To further reduce redundancy in the entropy model, we integrate AFMM with a Swin Transformer to form a Frequency Swin Transformer Attention Module (FSTAM) for frequency aware side information modeling. Experiments on the Kodak, Tecnick and CLIC Professional Validation datasets show that HCFSSNet achieves competitive rate distortion performance compared with recent SSM based codecs such as MambaIC, while using significantly fewer parameters. On Kodak, Tecnick and CLIC, HCFSSNet reduces BD rate over the VTM anchor by 18.06, 24.56 and 22.44 percent, respectively, providing an efficient and interpretable hybrid architecture for future learned image compression systems.

