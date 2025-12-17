---
layout: default
title: CORE: Contrastive Masked Feature Reconstruction on Graphs
---

# CORE: Contrastive Masked Feature Reconstruction on Graphs

**arXiv**: [2512.13235v1](https://arxiv.org/abs/2512.13235) | [PDF](https://arxiv.org/pdf/2512.13235.pdf)

**作者**: Jianyuan Bo, Yuan Fang

---

## 💡 一句话要点

**提出CORE框架，通过结合掩码特征重建与对比学习增强图自监督学习性能**

**关键词**: `图自监督学习` `掩码特征重建` `对比学习` `节点分类` `图分类` `特征重建`

## 📋 核心要点

1. 核心问题：图自监督学习中生成式与对比式方法互补性不足，影响学习效果
2. 方法要点：在掩码特征重建中引入对比学习，利用原始与重建特征作为正对，掩码节点作为负样本
3. 实验或效果：在节点和图分类任务上显著超越MFR及GraphMAE等基线，达到先进水平

## 📄 摘要（原文）

> In the rapidly evolving field of self-supervised learning on graphs, generative and contrastive methodologies have emerged as two dominant approaches. Our study focuses on masked feature reconstruction (MFR), a generative technique where a model learns to restore the raw features of masked nodes in a self-supervised manner. We observe that both MFR and graph contrastive learning (GCL) aim to maximize agreement between similar elements. Building on this observation, we reveal a novel theoretical insight: under specific conditions, the objectives of MFR and node-level GCL converge, despite their distinct operational mechanisms. This theoretical connection suggests these approaches are complementary rather than fundamentally different, prompting us to explore their integration to enhance self-supervised learning on graphs. Our research presents Contrastive Masked Feature Reconstruction (CORE), a novel graph self-supervised learning framework that integrates contrastive learning into MFR. Specifically, we form positive pairs exclusively between the original and reconstructed features of masked nodes, encouraging the encoder to prioritize contextual information over the node's own features. Additionally, we leverage the masked nodes themselves as negative samples, combining MFR's reconstructive power with GCL's discriminative ability to better capture intrinsic graph structures. Empirically, our proposed framework CORE significantly outperforms MFR across node and graph classification tasks, demonstrating state-of-the-art results. In particular, CORE surpasses GraphMAE and GraphMAE2 by up to 2.80% and 3.72% on node classification tasks, and by up to 3.82% and 3.76% on graph classification tasks.

