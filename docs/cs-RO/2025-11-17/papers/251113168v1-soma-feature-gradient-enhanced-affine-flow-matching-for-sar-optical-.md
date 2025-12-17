---
layout: default
title: SOMA: Feature Gradient Enhanced Affine-Flow Matching for SAR-Optical Registration
---

# SOMA: Feature Gradient Enhanced Affine-Flow Matching for SAR-Optical Registration

**arXiv**: [2511.13168v1](https://arxiv.org/abs/2511.13168) | [PDF](https://arxiv.org/pdf/2511.13168.pdf)

**作者**: Haodong Wang, Tao Zhuo, Xiuwei Zhang, Hanlin Yin, Wencong Wu, Yanning Zhang

---

## 💡 一句话要点

**提出SOMA框架以解决SAR与光学图像像素级配准问题**

**关键词**: `SAR-光学配准` `特征梯度增强` `仿射流匹配` `多模态图像处理` `深度学习框架`

## 📋 核心要点

1. SAR与光学图像因成像机制差异导致配准困难，现有深度学习方法效果不佳
2. 引入特征梯度增强器和全局-局部仿射流匹配器，提升特征区分度和配准精度
3. 在SEN1-2和GFGE_SO数据集上，CMR@1px分别提升12.29%和18.50%

## 📄 摘要（原文）

> Achieving pixel-level registration between SAR and optical images remains a challenging task due to their fundamentally different imaging mechanisms and visual characteristics. Although deep learning has achieved great success in many cross-modal tasks, its performance on SAR-Optical registration tasks is still unsatisfactory. Gradient-based information has traditionally played a crucial role in handcrafted descriptors by highlighting structural differences. However, such gradient cues have not been effectively leveraged in deep learning frameworks for SAR-Optical image matching. To address this gap, we propose SOMA, a dense registration framework that integrates structural gradient priors into deep features and refines alignment through a hybrid matching strategy. Specifically, we introduce the Feature Gradient Enhancer (FGE), which embeds multi-scale, multi-directional gradient filters into the feature space using attention and reconstruction mechanisms to boost feature distinctiveness. Furthermore, we propose the Global-Local Affine-Flow Matcher (GLAM), which combines affine transformation and flow-based refinement within a coarse-to-fine architecture to ensure both structural consistency and local accuracy. Experimental results demonstrate that SOMA significantly improves registration precision, increasing the CMR@1px by 12.29% on the SEN1-2 dataset and 18.50% on the GFGE_SO dataset. In addition, SOMA exhibits strong robustness and generalizes well across diverse scenes and resolutions.

