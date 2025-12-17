---
layout: default
title: Elastic ViTs from Pretrained Models without Retraining
---

# Elastic ViTs from Pretrained Models without Retraining

**arXiv**: [2510.17700v1](https://arxiv.org/abs/2510.17700) | [PDF](https://arxiv.org/pdf/2510.17700.pdf)

**作者**: Walter Simoncini, Michael Dorkenwald, Tijmen Blankevoort, Cees G. M. Snoek, Yuki M. Asano

---

## 💡 一句话要点

**提出SnapViT方法，实现预训练视觉Transformer的弹性推理，无需重训练。**

**关键词**: `视觉Transformer` `结构化剪枝` `弹性推理` `进化算法` `自监督评分` `预训练模型`

## 📋 核心要点

1. 视觉基础模型尺寸固定，难以适应实际部署的计算约束。
2. 结合梯度与跨网络结构相关性，使用进化算法近似Hessian结构，无需标签或重训练。
3. 在多种模型上优于现有方法，生成弹性模型仅需数分钟，支持任意计算预算。

## 📄 摘要（原文）

> Vision foundation models achieve remarkable performance but are only
> available in a limited set of pre-determined sizes, forcing sub-optimal
> deployment choices under real-world constraints. We introduce SnapViT:
> Single-shot network approximation for pruned Vision Transformers, a new
> post-pretraining structured pruning method that enables elastic inference
> across a continuum of compute budgets. Our approach efficiently combines
> gradient information with cross-network structure correlations, approximated
> via an evolutionary algorithm, does not require labeled data, generalizes to
> models without a classification head, and is retraining-free. Experiments on
> DINO, SigLIPv2, DeIT, and AugReg models demonstrate superior performance over
> state-of-the-art methods across various sparsities, requiring less than five
> minutes on a single A100 GPU to generate elastic models that can be adjusted to
> any computational budget. Our key contributions include an efficient pruning
> strategy for pretrained Vision Transformers, a novel evolutionary approximation
> of Hessian off-diagonal structures, and a self-supervised importance scoring
> mechanism that maintains strong performance without requiring retraining or
> labels. Code and pruned models are available at: https://elastic.ashita.nl/

