---
layout: default
title: From Low-Rank Features to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers
---

# From Low-Rank Features to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers

**arXiv**: [2511.15572v1](https://arxiv.org/abs/2511.15572) | [PDF](https://arxiv.org/pdf/2511.15572.pdf)

**作者**: Huiyuan Tian, Bonan Xu, Shijian Li, Xin Jin

---

## 💡 一句话要点

**提出特征提升与宽度对齐策略以解决ViT特征蒸馏中的编码不匹配问题**

**关键词**: `视觉Transformer` `特征蒸馏` `编码不匹配` `低秩特征` `知识蒸馏`

## 📋 核心要点

1. 核心问题：ViT特征蒸馏因全局低秩与个体令牌高带宽编码不匹配而失效
2. 方法要点：引入轻量投影器或仅扩展学生末块宽度以对齐特征编码
3. 实验或效果：在ImageNet-1K上提升DeiT-Tiny准确率至77.53%和78.23%

## 📄 摘要（原文）

> Feature-map knowledge distillation (KD) is highly effective for convolutional networks but often fails for Vision Transformers (ViTs). To understand this failure and guide method design, we conduct a two-view representation analysis of ViTs. First, a layer-wise Singular Value Decomposition (SVD) of full feature matrices shows that final-layer representations are globally low-rank: for CaiT-S24, only $121/61/34/14$ dimensions suffice to capture $99\%/95\%/90\%/80\%$ of the energy. In principle, this suggests that a compact student plus a simple linear projector should be enough for feature alignment, contradicting the weak empirical performance of standard feature KD. To resolve this paradox, we introduce a token-level Spectral Energy Pattern (SEP) analysis that measures how each token uses channel capacity. SEP reveals that, despite the global low-rank structure, individual tokens distribute energy over most channels, forming a high-bandwidth encoding pattern. This results in an encoding mismatch between wide teachers and narrow students. Motivated by this insight, we propose two minimal, mismatch-driven strategies: (1) post-hoc feature lifting with a lightweight projector retained during inference, or (2) native width alignment that widens only the student's last block to the teacher's width. On ImageNet-1K, these strategies reactivate simple feature-map distillation in ViTs, raising DeiT-Tiny accuracy from $74.86\%$ to $77.53\%$ and $78.23\%$ when distilling from CaiT-S24, while also improving standalone students trained without any teacher. Our analysis thus explains why ViT feature distillation fails and shows how exploiting low-rank structure yields effective, interpretable remedies and concrete design guidance for compact ViTs.

