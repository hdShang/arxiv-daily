---
layout: default
title: NP-LoRA: Null Space Projection Unifies Subject and Style in LoRA Fusion
---

# NP-LoRA: Null Space Projection Unifies Subject and Style in LoRA Fusion

**arXiv**: [2511.11051v1](https://arxiv.org/abs/2511.11051) | [PDF](https://arxiv.org/pdf/2511.11051.pdf)

**作者**: Chuheng Chen, Xiaofei Zhou, Geyuan Zhang, Yong Huang

---

## 💡 一句话要点

**提出NP-LoRA以解决LoRA融合中的结构干扰问题**

**关键词**: `LoRA融合` `零空间投影` `结构干扰` `可控生成` `子空间分离`

## 📋 核心要点

1. 现有LoRA融合方法存在权重合并干扰，导致表示重叠和保真度下降
2. 通过零空间投影分离子空间，保护主方向免受干扰，并引入软投影机制
3. 实验显示NP-LoRA在融合质量上优于基线，无需重新训练

## 📄 摘要（原文）

> Low-Rank Adaptation (LoRA) fusion has emerged as a key technique for reusing and composing learned subject and style representations for controllable generation without costly retraining. However, existing methods rely on weight-based merging, where one LoRA often dominates the other, leading to interference and degraded fidelity. This interference is structural: separately trained LoRAs occupy low-rank high-dimensional subspaces, leading to non-orthogonal and overlapping representations. In this work, we analyze the internal structure of LoRAs and find their generative behavior is dominated by a few principal directions in the low-rank subspace, which should remain free from interference during fusion. To achieve this, we propose Null Space Projection LoRA (NP-LoRA), a projection-based framework for LoRA fusion that enforces subspace separation to prevent structural interference among principal directions. Specifically, we first extract principal style directions via singular value decomposition (SVD) and then project the subject LoRA into its orthogonal null space. Furthermore, we introduce a soft projection mechanism that enables smooth control over the trade-off between subject fidelity and style consistency. Experiments show NP-LoRA consistently improves fusion quality over strong baselines (e.g., DINO and CLIP-based metrics, with human and LLM preference scores), and applies broadly across backbones and LoRA pairs without retraining.

