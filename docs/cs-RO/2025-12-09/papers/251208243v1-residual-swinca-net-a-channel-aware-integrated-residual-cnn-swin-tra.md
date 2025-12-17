---
layout: default
title: Residual-SwinCA-Net: A Channel-Aware Integrated Residual CNN-Swin Transformer for Malignant Lesion Segmentation in BUSI
---

# Residual-SwinCA-Net: A Channel-Aware Integrated Residual CNN-Swin Transformer for Malignant Lesion Segmentation in BUSI

**arXiv**: [2512.08243v1](https://arxiv.org/abs/2512.08243) | [PDF](https://arxiv.org/pdf/2512.08243.pdf)

**作者**: Saeeda Naz, Saddam Hussain Khan

---

## 💡 一句话要点

**提出Residual-SwinCA-Net用于乳腺超声图像恶性病灶分割，结合残差CNN与Swin Transformer提升特征提取能力。**

**关键词**: `医学图像分割` `残差网络` `Swin Transformer` `通道注意力` `乳腺超声` `病灶分割`

## 📋 核心要点

1. 核心问题：乳腺超声图像分割面临噪声干扰、病灶形态多变和局部-全局特征融合挑战。
2. 方法要点：集成残差CNN模块提取局部特征，定制Swin Transformer块学习全局依赖，并引入MSCAS模块增强通道注意力。
3. 实验或效果：在BUSI数据集上实现99.29%平均准确率，优于现有CNNs/ViTs方法，提升临床诊断性能。

## 📄 摘要（原文）

> A novel deep hybrid Residual-SwinCA-Net segmentation framework is proposed in the study for addressing such challenges by extracting locally correlated and robust features, incorporating residual CNN modules. Furthermore, for learning global dependencies, Swin Transformer blocks are customized using internal residual pathways, which reinforce gradient stability, refine local patterns, and facilitate global feature fusion. Formerly, for enhancing tissue continuity, ultrasound noise suppressions, and accentuating fine structural transitions Laplacian-of-Gaussian regional operator is applied, and for maintaining the morphological integrity of malignant lesion contours, a boundary-oriented operator has been incorporated. Subsequently, a contraction strategy was applied stage-wise by progressively reducing features-map progressively for capturing scale invariance and enhancing the robustness of structural variability. In addition, each decoder level prior augmentation integrates a new Multi-Scale Channel Attention and Squeezing (MSCAS) module. The MSCAS selectively emphasizes encoder salient maps, retains discriminative global context, and complementary local structures with minimal computational cost while suppressing redundant activations. Finally, the Pixel-Attention module encodes class-relevant spatial cues by adaptively weighing malignant lesion pixels while suppressing background interference. The Residual-SwinCA-Net and existing CNNs/ViTs techniques have been implemented on the publicly available BUSI dataset. The proposed Residual-SwinCA-Net framework outperformed and achieved 99.29% mean accuracy, 98.74% IoU, and 0.9041 Dice for breast lesion segmentation. The proposed Residual-SwinCA-Net framework improves the BUSI lesion diagnostic performance and strengthens timely clinical decision-making.

