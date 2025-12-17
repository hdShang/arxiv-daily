---
layout: default
title: A Lightweight Real-Time Low-Light Enhancement Network for Embedded Automotive Vision Systems
---

# A Lightweight Real-Time Low-Light Enhancement Network for Embedded Automotive Vision Systems

**arXiv**: [2512.02965v1](https://arxiv.org/abs/2512.02965) | [PDF](https://arxiv.org/pdf/2512.02965.pdf)

**作者**: Yuhan Chen, Yicui Shi, Guofa Li, Guangrui Bai, Jinyuan Shao, Xiangfei Huang, Wenbo Chu, Keqiang Li

---

## 💡 一句话要点

**提出UltraFast-LieNET以解决车载嵌入式系统在低光环境下实时图像增强的计算负担问题。**

**关键词**: `低光图像增强` `轻量级网络` `实时处理` `车载视觉系统` `动态移位卷积` `多尺度残差块`

## 📋 核心要点

1. 核心问题：低光环境如图像退化影响车载摄像头安全，现有算法计算量大，不适合车辆应用。
2. 方法要点：设计轻量级多尺度移位卷积网络，引入动态移位卷积和残差结构，参数最少仅36个。
3. 实验或效果：在LOLI-Street数据集上PSNR达26.51 dB，优于现有方法4.6 dB，仅用180参数，验证实时性与增强质量平衡。

## 📄 摘要（原文）

> In low-light environments like nighttime driving, image degradation severely challenges in-vehicle camera safety. Since existing enhancement algorithms are often too computationally intensive for vehicular applications, we propose UltraFast-LieNET, a lightweight multi-scale shifted convolutional network for real-time low-light image enhancement. We introduce a Dynamic Shifted Convolution (DSConv) kernel with only 12 learnable parameters for efficient feature extraction. By integrating DSConv with varying shift distances, a Multi-scale Shifted Residual Block (MSRB) is constructed to significantly expand the receptive field. To mitigate lightweight network instability, a residual structure and a novel multi-level gradient-aware loss function are incorporated. UltraFast-LieNET allows flexible parameter configuration, with a minimum size of only 36 parameters. Results on the LOLI-Street dataset show a PSNR of 26.51 dB, outperforming state-of-the-art methods by 4.6 dB while utilizing only 180 parameters. Experiments across four benchmark datasets validate its superior balance of real-time performance and enhancement quality under limited resources. Code is available at https://githubhttps://github.com/YuhanChen2024/UltraFast-LiNET

