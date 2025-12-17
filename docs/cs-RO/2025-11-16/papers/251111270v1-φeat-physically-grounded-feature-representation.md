---
layout: default
title: Φeat: Physically-Grounded Feature Representation
---

# Φeat: Physically-Grounded Feature Representation

**arXiv**: [2511.11270v1](https://arxiv.org/abs/2511.11270) | [PDF](https://arxiv.org/pdf/2511.11270.pdf)

**作者**: Giuseppe Vecchio, Adrien Kaiser, Rouffet Romain, Rosalie Martin, Elena Garces, Tamy Boubekeur

---

## 💡 一句话要点

**提出Φeat自监督视觉骨干，学习物理基础特征以增强物理感知任务**

**关键词**: `自监督学习` `物理基础特征` `材料识别` `对比学习` `视觉骨干网络`

## 📋 核心要点

1. 当前自监督特征将高层语义与几何、光照等物理因素纠缠，阻碍物理推理任务
2. 采用对比预训练策略，通过空间裁剪和物理增强学习材料身份特征
3. 评估显示特征相似性分析和材料选择中，Φeat捕获物理结构，超越语义分组

## 📄 摘要（原文）

> Foundation models have emerged as effective backbones for many vision tasks. However, current self-supervised features entangle high-level semantics with low-level physical factors, such as geometry and illumination, hindering their use in tasks requiring explicit physical reasoning. In this paper, we introduce $Φ$eat, a novel physically-grounded visual backbone that encourages a representation sensitive to material identity, including reflectance cues and geometric mesostructure. Our key idea is to employ a pretraining strategy that contrasts spatial crops and physical augmentations of the same material under varying shapes and lighting conditions. While similar data have been used in high-end supervised tasks such as intrinsic decomposition or material estimation, we demonstrate that a pure self-supervised training strategy, without explicit labels, already provides a strong prior for tasks requiring robust features invariant to external physical factors. We evaluate the learned representations through feature similarity analysis and material selection, showing that $Φ$eat captures physically-grounded structure beyond semantic grouping. These findings highlight the promise of unsupervised physical feature learning as a foundation for physics-aware perception in vision and graphics. These findings highlight the promise of unsupervised physical feature learning as a foundation for physics-aware perception in vision and graphics.

