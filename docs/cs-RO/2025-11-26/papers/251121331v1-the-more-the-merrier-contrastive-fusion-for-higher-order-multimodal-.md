---
layout: default
title: The More, the Merrier: Contrastive Fusion for Higher-Order Multimodal Alignment
---

# The More, the Merrier: Contrastive Fusion for Higher-Order Multimodal Alignment

**arXiv**: [2511.21331v1](https://arxiv.org/abs/2511.21331) | [PDF](https://arxiv.org/pdf/2511.21331.pdf)

**作者**: Stefanos Koutoupis, Michaela Areti Zervou, Konstantinos Kontras, Maarten De Vos, Panagiotis Tsakalides, Grigorios Tsagatakis

---

## 💡 一句话要点

**提出ConFu框架以解决多模态高阶对齐中忽视成对关系的问题**

**关键词**: `多模态对齐` `对比学习` `高阶依赖` `融合表示` `检索任务`

## 📋 核心要点

1. 核心问题：多模态学习多限于成对对齐，高阶方法常忽略成对关系，影响单模态任务性能
2. 方法要点：引入融合模态对比项，联合嵌入单模态与融合模态，捕获高阶依赖如XOR关系
3. 实验或效果：在合成和真实基准上，ConFu在检索和分类任务中表现竞争性，支持统一检索

## 📄 摘要（原文）

> Learning joint representations across multiple modalities remains a central challenge in multimodal machine learning. Prevailing approaches predominantly operate in pairwise settings, aligning two modalities at a time. While some recent methods aim to capture higher-order interactions among multiple modalities, they often overlook or insufficiently preserve pairwise relationships, limiting their effectiveness on single-modality tasks. In this work, we introduce Contrastive Fusion (ConFu), a framework that jointly embeds both individual modalities and their fused combinations into a unified representation space, where modalities and their fused counterparts are aligned. ConFu extends traditional pairwise contrastive objectives with an additional fused-modality contrastive term, encouraging the joint embedding of modality pairs with a third modality. This formulation enables ConFu to capture higher-order dependencies, such as XOR-like relationships, that cannot be recovered through pairwise alignment alone, while still maintaining strong pairwise correspondence. We evaluate ConFu on synthetic and real-world multimodal benchmarks, assessing its ability to exploit cross-modal complementarity, capture higher-order dependencies, and scale with increasing multimodal complexity. Across these settings, ConFu demonstrates competitive performance on retrieval and classification tasks, while supporting unified one-to-one and two-to-one retrieval within a single contrastive framework.

