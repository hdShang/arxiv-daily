---
layout: default
title: LayerEdit: Disentangled Multi-Object Editing via Conflict-Aware Multi-Layer Learning
---

# LayerEdit: Disentangled Multi-Object Editing via Conflict-Aware Multi-Layer Learning

**arXiv**: [2511.08251v1](https://arxiv.org/abs/2511.08251) | [PDF](https://arxiv.org/pdf/2511.08251.pdf)

**作者**: Fengyi Fu, Mengqi Huang, Lei Zhang, Zhendong Mao

---

## 💡 一句话要点

**提出LayerEdit框架以解决多对象图像编辑中的注意力纠缠问题**

**关键词**: `多对象图像编辑` `注意力解缠` `分层学习` `文本驱动编辑` `冲突感知`

## 📋 核心要点

1. 核心问题：现有方法忽视对象间交互，导致编辑泄漏或约束
2. 方法要点：通过分层分解、编辑和融合实现无冲突多对象编辑
3. 实验或效果：在复杂场景中验证了优越的编辑可控性和一致性

## 📄 摘要（原文）

> Text-driven multi-object image editing which aims to precisely modify multiple objects within an image based on text descriptions, has recently attracted considerable interest. Existing works primarily follow the localize-editing paradigm, focusing on independent object localization and editing while neglecting critical inter-object interactions. However, this work points out that the neglected attention entanglements in inter-object conflict regions, inherently hinder disentangled multi-object editing, leading to either inter-object editing leakage or intra-object editing constraints. We thereby propose a novel multi-layer disentangled editing framework LayerEdit, a training-free method which, for the first time, through precise object-layered decomposition and coherent fusion, enables conflict-free object-layered editing. Specifically, LayerEdit introduces a novel "decompose-editingfusion" framework, consisting of: (1) Conflict-aware Layer Decomposition module, which utilizes an attention-aware IoU scheme and time-dependent region removing, to enhance conflict awareness and suppression for layer decomposition. (2) Object-layered Editing module, to establish coordinated intra-layer text guidance and cross-layer geometric mapping, achieving disentangled semantic and structural modifications. (3) Transparency-guided Layer Fusion module, to facilitate structure-coherent inter-object layer fusion through precise transparency guidance learning. Extensive experiments verify the superiority of LayerEdit over existing methods, showing unprecedented intra-object controllability and inter-object coherence in complex multi-object scenarios. Codes are available at: https://github.com/fufy1024/LayerEdit.

