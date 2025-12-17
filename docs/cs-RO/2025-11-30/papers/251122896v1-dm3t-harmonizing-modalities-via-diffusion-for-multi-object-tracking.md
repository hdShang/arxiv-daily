---
layout: default
title: DM$^3$T: Harmonizing Modalities via Diffusion for Multi-Object Tracking
---

# DM$^3$T: Harmonizing Modalities via Diffusion for Multi-Object Tracking

**arXiv**: [2511.22896v1](https://arxiv.org/abs/2511.22896) | [PDF](https://arxiv.org/pdf/2511.22896.pdf)

**作者**: Weiran Li, Yeqiang Liu, Yijie Wei, Mina Han, Qiannan Guo, Zhenbo Li

---

## 💡 一句话要点

**提出DM³T框架，通过扩散模型迭代对齐特征以解决多模态多目标跟踪中的模态融合挑战。**

**关键词**: `多模态融合` `扩散模型` `多目标跟踪` `特征对齐` `自动驾驶`

## 📋 核心要点

1. 核心问题：可见光与热红外模态特征分布差异大，传统融合方法易导致冲突，降低跟踪精度。
2. 方法要点：设计跨模态扩散融合模块，迭代投影特征到共享流形，并引入扩散精炼器增强统一表示。
3. 实验或效果：在VT-MOT基准上达到41.7 HOTA，相对现有最优方法提升1.54%。

## 📄 摘要（原文）

> Multi-object tracking (MOT) is a fundamental task in computer vision with critical applications in autonomous driving and robotics. Multimodal MOT that integrates visible light and thermal infrared information is particularly essential for robust autonomous driving systems. However, effectively fusing these heterogeneous modalities is challenging. Simple strategies like concatenation or addition often fail to bridge the significant non-linear distribution gap between their feature representations, which can lead to modality conflicts and degrade tracking accuracy. Drawing inspiration from the connection between multimodal MOT and the iterative refinement in diffusion models, this paper proposes DM$^3$T, a novel framework that reformulates multimodal fusion as an iterative feature alignment process to generate accurate and temporally coherent object trajectories. Our approach performs iterative cross-modal harmonization through a proposed Cross-Modal Diffusion Fusion (C-MDF) module. In this process, features from both modalities provide mutual guidance, iteratively projecting them onto a shared, consistent feature manifold. This enables the learning of complementary information and achieves deeper fusion compared to conventional methods. Additionally, we introduce a plug-and-play Diffusion Refiner (DR) to enhance and refine the unified feature representation. To further improve tracking robustness, we design a Hierarchical Tracker that adaptively handles confidence estimation. DM$^3$T unifies object detection, state estimation, and data association into a comprehensive online tracking framework without complex post-processing. Extensive experiments on the VT-MOT benchmark demonstrate that our method achieves 41.7 HOTA, representing a 1.54% relative improvement over existing state-of-the-art methods. The code and models are available at https://vranlee.github.io/DM-3-T/.

