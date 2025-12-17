---
layout: default
title: Odin: Oriented Dual-module Integration for Text-rich Network Representation Learning
---

# Odin: Oriented Dual-module Integration for Text-rich Network Representation Learning

**arXiv**: [2511.21416v1](https://arxiv.org/abs/2511.21416) | [PDF](https://arxiv.org/pdf/2511.21416.pdf)

**作者**: Kaifeng Hong, Yinglong Zhang, Xiaoying Hong, Xuewen Xia, Xing Xu

---

## 💡 一句话要点

**提出Odin架构以解决文本属性图中结构与文本融合问题**

**关键词**: `文本属性图` `图神经网络` `Transformer架构` `结构注入` `轻量模型` `多跳结构抽象`

## 📋 核心要点

1. 核心问题：现有方法难以结合文本理解与图结构，GNN易过平滑，Transformer忽略拓扑
2. 方法要点：通过定向双模块在Transformer特定层注入图结构，避免多跳扩散
3. 实验或效果：在多个基准上实现SOTA，轻量版保持性能并降低计算成本

## 📄 摘要（原文）

> Text-attributed graphs require models to effectively combine strong textual understanding with structurally informed reasoning. Existing approaches either rely on GNNs--limited by over-smoothing and hop-dependent diffusion--or employ Transformers that overlook graph topology and treat nodes as isolated sequences. We propose Odin (Oriented Dual-module INtegration), a new architecture that injects graph structure into Transformers at selected depths through an oriented dual-module mechanism.Unlike message-passing GNNs, Odin does not rely on multi-hop diffusion; instead, multi-hop structures are integrated at specific Transformer layers, yielding low-, mid-, and high-level structural abstraction aligned with the model's semantic hierarchy. Because aggregation operates on the global [CLS] representation, Odin fundamentally avoids over-smoothing and decouples structural abstraction from neighborhood size or graph topology. We further establish that Odin's expressive power strictly contains that of both pure Transformers and GNNs.To make the design efficient in large-scale or low-resource settings, we introduce Light Odin, a lightweight variant that preserves the same layer-aligned structural abstraction for faster training and inference. Experiments on multiple text-rich graph benchmarks show that Odin achieves state-of-the-art accuracy, while Light Odin delivers competitive performance with significantly reduced computational cost. Together, Odin and Light Odin form a unified, hop-free framework for principled structure-text integration. The source code of this model has been released at https://github.com/hongkaifeng/Odin.

