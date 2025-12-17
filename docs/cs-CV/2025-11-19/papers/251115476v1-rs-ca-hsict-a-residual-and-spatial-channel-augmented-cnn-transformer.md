---
layout: default
title: RS-CA-HSICT: A Residual and Spatial Channel Augmented CNN Transformer Framework for Monkeypox Detection
---

# RS-CA-HSICT: A Residual and Spatial Channel Augmented CNN Transformer Framework for Monkeypox Detection

**arXiv**: [2511.15476v1](https://arxiv.org/abs/2511.15476) | [PDF](https://arxiv.org/pdf/2511.15476.pdf)

**作者**: Rashid Iqbal, Saddam Hussain Khan

---

## 💡 一句话要点

**提出RS-CA-HSICT混合框架以增强猴痘检测，结合CNN和Transformer优势。**

**关键词**: `猴痘检测` `CNN-Transformer混合` `残差学习` `空间注意力` `通道增强` `多尺度特征`

## 📋 核心要点

1. 核心问题：猴痘检测需处理局部纹理、全局上下文和噪声等复杂特征。
2. 方法要点：集成残差CNN、空间CNN和HSICT模块，增强特征多样性和长程依赖。
3. 实验效果：在Kaggle和多样数据集上准确率达98.30%，F1分数98.13%。

## 📄 摘要（原文）

> This work proposes a hybrid deep learning approach, namely Residual and Spatial Learning based Channel Augmented Integrated CNN-Transformer architecture, that leverages the strengths of CNN and Transformer towards enhanced MPox detection. The proposed RS-CA-HSICT framework is composed of an HSICT block, a residual CNN module, a spatial CNN block, and a CA, which enhances the diverse feature space, detailed lesion information, and long-range dependencies. The new HSICT module first integrates an abstract representation of the stem CNN and customized ICT blocks for efficient multihead attention and structured CNN layers with homogeneous (H) and structural (S) operations. The customized ICT blocks learn global contextual interactions and local texture extraction. Additionally, H and S layers learn spatial homogeneity and fine structural details by reducing noise and modeling complex morphological variations. Moreover, inverse residual learning enhances vanishing gradient, and stage-wise resolution reduction ensures scale invariance. Furthermore, the RS-CA-HSICT framework augments the learned HSICT channels with the TL-driven Residual and Spatial CNN maps for enhanced multiscale feature space capturing global and localized structural cues, subtle texture, and contrast variations. These channels, preceding augmentation, are refined through the Channel-Fusion-and-Attention block, which preserves discriminative channels while suppressing redundant ones, thereby enabling efficient computation. Finally, the spatial attention mechanism refines pixel selection to detect subtle patterns and intra-class contrast variations in Mpox. Experimental results on both the Kaggle benchmark and a diverse MPox dataset reported classification accuracy as high as 98.30% and an F1-score of 98.13%, which outperforms the existing CNNs and ViTs.

