---
layout: default
title: Infrared UAV Target Tracking with Dynamic Feature Refinement and Global Contextual Attention Knowledge Distillation
---

# Infrared UAV Target Tracking with Dynamic Feature Refinement and Global Contextual Attention Knowledge Distillation

**arXiv**: [2512.04581v1](https://arxiv.org/abs/2512.04581) | [PDF](https://arxiv.org/pdf/2512.04581.pdf)

**作者**: Houzhang Fang, Chenxing Wu, Kun Bai, Tianqi Chen, Xiaolin Wang, Xiyang Liu, Yi Chang, Luxin Yan

---

## 💡 一句话要点

**提出SiamDFF网络，通过动态特征融合与全局上下文注意力知识蒸馏，解决红外无人机目标跟踪中特征弱和背景复杂的问题。**

**关键词**: `红外目标跟踪` `无人机跟踪` `动态特征融合` `注意力机制` `知识蒸馏` `实时跟踪`

## 📋 核心要点

1. 红外无人机目标跟踪面临特征弱、背景复杂的挑战，影响准确性。
2. SiamDFF集成STEN、DSFAM和DCFAM模块，动态增强特征并引入知识蒸馏提升特征提取。
3. 在真实红外数据集上实验，优于现有方法，实现实时跟踪速度。

## 📄 摘要（原文）

> Unmanned aerial vehicle (UAV) target tracking based on thermal infrared imaging has been one of the most important sensing technologies in anti-UAV applications. However, the infrared UAV targets often exhibit weak features and complex backgrounds, posing significant challenges to accurate tracking. To address these problems, we introduce SiamDFF, a novel dynamic feature fusion Siamese network that integrates feature enhancement and global contextual attention knowledge distillation for infrared UAV target (IRUT) tracking. The SiamDFF incorporates a selective target enhancement network (STEN), a dynamic spatial feature aggregation module (DSFAM), and a dynamic channel feature aggregation module (DCFAM). The STEN employs intensity-aware multi-head cross-attention to adaptively enhance important regions for both template and search branches. The DSFAM enhances multi-scale UAV target features by integrating local details with global features, utilizing spatial attention guidance within the search frame. The DCFAM effectively integrates the mixed template generated from STEN in the template branch and original template, avoiding excessive background interference with the template and thereby enhancing the emphasis on UAV target region features within the search frame. Furthermore, to enhance the feature extraction capabilities of the network for IRUT without adding extra computational burden, we propose a novel tracking-specific target-aware contextual attention knowledge distiller. It transfers the target prior from the teacher network to the student model, significantly improving the student network's focus on informative regions at each hierarchical level of the backbone network. Extensive experiments on real infrared UAV datasets demonstrate that the proposed approach outperforms state-of-the-art target trackers under complex backgrounds while achieving a real-time tracking speed.

