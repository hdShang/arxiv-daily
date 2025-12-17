---
layout: default
title: Gradient-Guided Learning Network for Infrared Small Target Detection
---

# Gradient-Guided Learning Network for Infrared Small Target Detection

**arXiv**: [2512.09497v1](https://arxiv.org/abs/2512.09497) | [PDF](https://arxiv.org/pdf/2512.09497.pdf)

**作者**: Jinmiao Zhao, Chuang Yu, Zelin Shi, Yunpeng Liu, Yingdi Zhang

---

## 💡 一句话要点

**提出梯度引导学习网络以解决红外小目标检测中边缘定位不准确和目标易被背景淹没的问题**

**关键词**: `红外小目标检测` `梯度引导学习` `双分支网络` `特征融合` `深度学习`

## 📋 核心要点

1. 核心问题：红外小目标尺寸小、特征少，导致现有方法边缘定位不准确且目标易被背景淹没
2. 方法要点：首次引入梯度幅值图像，设计双分支特征提取网络和双向引导融合模块，增强边缘细节和特征融合
3. 实验或效果：在公开真实和合成数据集上实现最优结果，代码已开源

## 📄 摘要（原文）

> Recently, infrared small target detection has attracted extensive attention. However, due to the small size and the lack of intrinsic features of infrared small targets, the existing methods generally have the problem of inaccurate edge positioning and the target is easily submerged by the background. Therefore, we propose an innovative gradient-guided learning network (GGL-Net). Specifically, we are the first to explore the introduction of gradient magnitude images into the deep learning-based infrared small target detection method, which is conducive to emphasizing the edge details and alleviating the problem of inaccurate edge positioning of small targets. On this basis, we propose a novel dual-branch feature extraction network that utilizes the proposed gradient supplementary module (GSM) to encode raw gradient information into deeper network layers and embeds attention mechanisms reasonably to enhance feature extraction ability. In addition, we construct a two-way guidance fusion module (TGFM), which fully considers the characteristics of feature maps at different levels. It can facilitate the effective fusion of multi-scale feature maps and extract richer semantic information and detailed information through reasonable two-way guidance. Extensive experiments prove that GGL-Net has achieves state-of-the-art results on the public real NUAA-SIRST dataset and the public synthetic NUDT-SIRST dataset. Our code has been integrated into https://github.com/YuChuang1205/MSDA-Net

