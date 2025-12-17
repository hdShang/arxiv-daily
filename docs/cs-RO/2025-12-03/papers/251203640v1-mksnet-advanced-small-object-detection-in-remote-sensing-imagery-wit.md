---
layout: default
title: MKSNet: Advanced Small Object Detection in Remote Sensing Imagery with Multi-Kernel and Dual Attention Mechanisms
---

# MKSNet: Advanced Small Object Detection in Remote Sensing Imagery with Multi-Kernel and Dual Attention Mechanisms

**arXiv**: [2512.03640v1](https://arxiv.org/abs/2512.03640) | [PDF](https://arxiv.org/pdf/2512.03640.pdf)

**作者**: Jiahao Zhang, Xiao Zhao, Guangyu Gao

---

## 💡 一句话要点

**提出MKSNet，通过多核选择与双注意力机制解决遥感图像中小目标检测难题。**

**关键词**: `小目标检测` `遥感图像` `多核卷积` `注意力机制` `深度学习` `计算机视觉`

## 📋 核心要点

1. 核心问题：遥感图像高分辨率与小目标导致深层CNN信息丢失，背景复杂干扰检测。
2. 方法要点：引入多核选择机制自适应捕获上下文，结合空间与通道注意力优化特征表示。
3. 实验或效果：在DOTA-v1.0和HRSC2016基准上超越现有方法，验证了多尺度高分辨率处理能力。

## 📄 摘要（原文）

> Deep convolutional neural networks (DCNNs) have substantially advanced object detection capabilities, particularly in remote sensing imagery. However, challenges persist, especially in detecting small objects where the high resolution of these images and the small size of target objects often result in a loss of critical information in the deeper layers of conventional CNNs. Additionally, the extensive spatial redundancy and intricate background details typical in remote-sensing images tend to obscure these small targets. To address these challenges, we introduce Multi-Kernel Selection Network (MKSNet), a novel network architecture featuring a novel Multi-Kernel Selection mechanism. The MKS mechanism utilizes large convolutional kernels to effectively capture an extensive range of contextual information. This innovative design allows for adaptive kernel size selection, significantly enhancing the network's ability to dynamically process and emphasize crucial spatial details for small object detection. Furthermore, MKSNet also incorporates a dual attention mechanism, merging spatial and channel attention modules. The spatial attention module adaptively fine-tunes the spatial weights of feature maps, focusing more intensively on relevant regions while mitigating background noise. Simultaneously, the channel attention module optimizes channel information selection, improving feature representation and detection accuracy. Empirical evaluations on the DOTA-v1.0 and HRSC2016 benchmark demonstrate that MKSNet substantially surpasses existing state-of-the-art models in detecting small objects in remote sensing images. These results highlight MKSNet's superior ability to manage the complexities associated with multi-scale and high-resolution image data, confirming its effectiveness and innovation in remote sensing object detection.

