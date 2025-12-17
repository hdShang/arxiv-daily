---
layout: default
title: DEAP-3DSAM: Decoder Enhanced and Auto Prompt SAM for 3D Medical Image Segmentation
---

# DEAP-3DSAM: Decoder Enhanced and Auto Prompt SAM for 3D Medical Image Segmentation

**arXiv**: [2511.19071v1](https://arxiv.org/abs/2511.19071) | [PDF](https://arxiv.org/pdf/2511.19071.pdf)

**作者**: Fangda Chen, Jintao Tang, Pancheng Wang, Ting Wang, Shasha Li, Ting Deng

---

## 💡 一句话要点

**提出DEAP-3DSAM以解决3D医学图像分割中的空间特征损失和手动提示依赖问题**

**关键词**: `3D医学图像分割` `特征增强` `自动提示生成` `双注意力机制` `腹部肿瘤分割`

## 📋 核心要点

1. 核心问题：SAM在3D医学图像分割中因伪3D处理导致空间特征损失，且依赖手动提示
2. 方法要点：设计特征增强解码器融合图像特征，并引入双注意力提示器自动生成提示
3. 实验或效果：在四个腹部肿瘤数据集上实现SOTA性能，验证模块有效性

## 📄 摘要（原文）

> The Segment Anything Model (SAM) has recently demonstrated significant potential in medical image segmentation. Although SAM is primarily trained on 2D images, attempts have been made to apply it to 3D medical image segmentation. However, the pseudo 3D processing used to adapt SAM results in spatial feature loss, limiting its performance. Additionally, most SAM-based methods still rely on manual prompts, which are challenging to implement in real-world scenarios and require extensive external expert knowledge. To address these limitations, we introduce the Decoder Enhanced and Auto Prompt SAM (DEAP-3DSAM) to tackle these limitations. Specifically, we propose a Feature Enhanced Decoder that fuses the original image features with rich and detailed spatial information to enhance spatial features. We also design a Dual Attention Prompter to automatically obtain prompt information through Spatial Attention and Channel Attention. We conduct comprehensive experiments on four public abdominal tumor segmentation datasets. The results indicate that our DEAP-3DSAM achieves state-of-the-art performance in 3D image segmentation, outperforming or matching existing manual prompt methods. Furthermore, both quantitative and qualitative ablation studies confirm the effectiveness of our proposed modules.

