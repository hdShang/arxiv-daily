---
layout: default
title: ActVAR: Activating Mixtures of Weights and Tokens for Efficient Visual Autoregressive Generation
---

# ActVAR: Activating Mixtures of Weights and Tokens for Efficient Visual Autoregressive Generation

**arXiv**: [2511.12893v1](https://arxiv.org/abs/2511.12893) | [PDF](https://arxiv.org/pdf/2511.12893.pdf)

**作者**: Kaixin Zhang, Ruiqing Yang, Yuan Zhang, Shan You, Tao Huang

---

## 💡 一句话要点

**提出ActVAR框架以解决视觉自回归模型计算成本高的问题**

**关键词**: `视觉自回归生成` `动态激活` `知识蒸馏` `计算效率优化` `令牌选择` `专家网络`

## 📋 核心要点

1. 视觉自回归模型序列增长导致计算成本剧增，静态剪枝破坏预训练依赖
2. 动态激活权重和令牌，分解FFN为专家子网，路由选择专家，门控选择令牌
3. ImageNet 256×256基准上，FLOPs减少21.2%，性能损失最小

## 📄 摘要（原文）

> Visual Autoregressive (VAR) models enable efficient image generation via next-scale prediction but face escalating computational costs as sequence length grows. Existing static pruning methods degrade performance by permanently removing weights or tokens, disrupting pretrained dependencies. To address this, we propose ActVAR, a dynamic activation framework that introduces dual sparsity across model weights and token sequences to enhance efficiency without sacrificing capacity. ActVAR decomposes feedforward networks (FFNs) into lightweight expert sub-networks and employs a learnable router to dynamically select token-specific expert subsets based on content. Simultaneously, a gated token selector identifies high-update-potential tokens for computation while reconstructing unselected tokens to preserve global context and sequence alignment. Training employs a two-stage knowledge distillation strategy, where the original VAR model supervises the learning of routing and gating policies to align with pretrained knowledge. Experiments on the ImageNet $256\times 256$ benchmark demonstrate that ActVAR achieves up to $21.2\%$ FLOPs reduction with minimal performance degradation.

