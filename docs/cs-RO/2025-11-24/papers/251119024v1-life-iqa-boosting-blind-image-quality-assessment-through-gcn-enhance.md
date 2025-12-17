---
layout: default
title: Life-IQA: Boosting Blind Image Quality Assessment through GCN-enhanced Layer Interaction and MoE-based Feature Decoupling
---

# Life-IQA: Boosting Blind Image Quality Assessment through GCN-enhanced Layer Interaction and MoE-based Feature Decoupling

**arXiv**: [2511.19024v1](https://arxiv.org/abs/2511.19024) | [PDF](https://arxiv.org/pdf/2511.19024.pdf)

**作者**: Long Tang, Guoquan Zhen, Jie Hao, Jianbo Zhang, Huiyu Duan, Liang Yuan, Guangtao Zhai

---

## 💡 一句话要点

**提出Life-IQA框架，通过GCN增强层交互和MoE特征解耦提升盲图像质量评估性能**

**关键词**: `盲图像质量评估` `图卷积网络` `专家混合模型` `特征交互` `特征解耦` `视觉编码器`

## 📋 核心要点

1. 核心问题：现有BIQA方法忽视浅层和深层特征对质量预测的不平等贡献，且质量解码架构探索不足
2. 方法要点：使用GCN增强层交互模块进行跨注意力，MoE模块解耦特征以处理不同失真类型
3. 实验或效果：在多个BIQA基准上实现SOTA性能，平衡准确性与成本优于Transformer解码器

## 📄 摘要（原文）

> Blind image quality assessment (BIQA) plays a crucial role in evaluating and optimizing visual experience. Most existing BIQA approaches fuse shallow and deep features extracted from backbone networks, while overlooking the unequal contributions to quality prediction. Moreover, while various vision encoder backbones are widely adopted in BIQA, the effective quality decoding architectures remain underexplored. To address these limitations, this paper investigates the contributions of shallow and deep features to BIQA, and proposes a effective quality feature decoding framework via GCN-enhanced \underline{l}ayer\underline{i}nteraction and MoE-based \underline{f}eature d\underline{e}coupling, termed \textbf{(Life-IQA)}. Specifically, the GCN-enhanced layer interaction module utilizes the GCN-enhanced deepest-layer features as query and the penultimate-layer features as key, value, then performs cross-attention to achieve feature interaction. Moreover, a MoE-based feature decoupling module is proposed to decouple fused representations though different experts specialized for specific distortion types or quality dimensions. Extensive experiments demonstrate that Life-IQA shows more favorable balance between accuracy and cost than a vanilla Transformer decoder and achieves state-of-the-art performance on multiple BIQA benchmarks.The code is available at: \href{https://github.com/TANGLONG2/Life-IQA/tree/main}{\texttt{Life-IQA}}.

