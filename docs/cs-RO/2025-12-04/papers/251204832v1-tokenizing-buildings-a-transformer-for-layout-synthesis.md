---
layout: default
title: Tokenizing Buildings: A Transformer for Layout Synthesis
---

# Tokenizing Buildings: A Transformer for Layout Synthesis

**arXiv**: [2512.04832v1](https://arxiv.org/abs/2512.04832) | [PDF](https://arxiv.org/pdf/2512.04832.pdf)

**作者**: Manuel Ladron de Guevara, Jinmo Rhee, Ardavan Bidgoli, Vaidas Razgaitis, Michael Bergin

---

## 💡 一句话要点

**提出Small Building Model（SBM），一种基于Transformer的架构，用于建筑信息建模（BIM）场景中的布局合成。**

**关键词**: `建筑信息建模` `布局合成` `Transformer架构` `特征嵌入` `自回归预测` `语义检索`

## 📋 核心要点

1. 核心问题：如何将建筑元素的异构特征集统一为序列，同时保留组合结构，以进行建筑布局合成。
2. 方法要点：设计统一嵌入模块，学习分类和连续特征的联合表示，并训练Transformer骨干，支持编码器模式和编码器-解码器模式。
3. 实验或效果：SBM学习紧凑的房间嵌入，实现强语义检索，并在生成布局中减少碰撞和边界违规，提高可导航性。

## 📄 摘要（原文）

> We introduce Small Building Model (SBM), a Transformer-based architecture for layout synthesis in Building Information Modeling (BIM) scenes. We address the question of how to tokenize buildings by unifying heterogeneous feature sets of architectural elements into sequences while preserving compositional structure. Such feature sets are represented as a sparse attribute-feature matrix that captures room properties. We then design a unified embedding module that learns joint representations of categorical and possibly correlated continuous feature groups. Lastly, we train a single Transformer backbone in two modes: an encoder-only pathway that yields high-fidelity room embeddings, and an encoder-decoder pipeline for autoregressive prediction of room entities, referred to as Data-Driven Entity Prediction (DDEP). Experiments across retrieval and generative layout synthesis show that SBM learns compact room embeddings that reliably cluster by type and topology, enabling strong semantic retrieval. In DDEP mode, SBM produces functionally sound layouts, with fewer collisions and boundary violations and improved navigability.

