---
layout: default
title: Effective Attention-Guided Multi-Scale Medical Network for Skin Lesion Segmentation
---

# Effective Attention-Guided Multi-Scale Medical Network for Skin Lesion Segmentation

**arXiv**: [2512.07275v1](https://arxiv.org/abs/2512.07275) | [PDF](https://arxiv.org/pdf/2512.07275.pdf)

**作者**: Siyu Wang, Hua Wang, Huiyu Li, Fan Zhang

---

## 💡 一句话要点

**提出基于多尺度残差和注意力机制的编码器-解码器网络，以解决皮肤病灶分割中形状不规则和对比度低的挑战。**

**关键词**: `皮肤病灶分割` `多尺度特征融合` `注意力机制` `编码器-解码器网络` `医学图像处理`

## 📋 核心要点

1. 核心问题：皮肤病灶分割面临病灶形状不规则和图像对比度低的难题，影响早期检测和诊断准确性。
2. 方法要点：引入多分辨率多通道融合模块和交叉混合注意力模块，增强特征提取的深度和灵活性，并通过外部注意力桥补偿信息损失。
3. 实验或效果：在多个皮肤病灶数据集上验证，模型在分割准确性和鲁棒性上显著优于现有基于Transformer和卷积神经网络的方法。

## 📄 摘要（原文）

> In the field of healthcare, precise skin lesion segmentation is crucial for the early detection and accurate diagnosis of skin diseases. Despite significant advances in deep learning for image processing, existing methods have yet to effectively address the challenges of irregular lesion shapes and low contrast. To address these issues, this paper proposes an innovative encoder-decoder network architecture based on multi-scale residual structures, capable of extracting rich feature information from different receptive fields to effectively identify lesion areas. By introducing a Multi-Resolution Multi-Channel Fusion (MRCF) module, our method captures cross-scale features, enhancing the clarity and accuracy of the extracted information. Furthermore, we propose a Cross-Mix Attention Module (CMAM), which redefines the attention scope and dynamically calculates weights across multiple contexts, thus improving the flexibility and depth of feature capture and enabling deeper exploration of subtle features. To overcome the information loss caused by skip connections in traditional U-Net, an External Attention Bridge (EAB) is introduced, facilitating the effective utilization of information in the decoder and compensating for the loss during upsampling. Extensive experimental evaluations on several skin lesion segmentation datasets demonstrate that the proposed model significantly outperforms existing transformer and convolutional neural network-based models, showcasing exceptional segmentation accuracy and robustness.

