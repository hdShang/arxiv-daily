---
layout: default
title: Hierarchical Semantic Tree Anchoring for CLIP-Based Class-Incremental Learning
---

# Hierarchical Semantic Tree Anchoring for CLIP-Based Class-Incremental Learning

**arXiv**: [2511.15633v1](https://arxiv.org/abs/2511.15633) | [PDF](https://arxiv.org/pdf/2511.15633.pdf)

**作者**: Tao Hu, Lan Li, Zhen-Hao Xie, Da-Wei Zhou

---

## 💡 一句话要点

**提出HASTEN方法，通过层次语义树锚定解决CLIP类增量学习中的灾难性遗忘问题。**

**关键词**: `类增量学习` `CLIP模型` `层次语义树` `双曲空间嵌入` `灾难性遗忘缓解`

## 📋 核心要点

1. 核心问题：CLIP类增量学习未显式捕获层次结构，导致细粒度类特征漂移和灾难性遗忘。
2. 方法要点：使用外部知识图在双曲空间嵌入特征，并投影梯度到共享映射器零空间以减轻遗忘。
3. 实验效果：广泛实验显示HASTEN优于现有方法，提供统一结构化表示。

## 📄 摘要（原文）

> Class-Incremental Learning (CIL) enables models to learn new classes continually while preserving past knowledge. Recently, vision-language models like CLIP offer transferable features via multi-modal pre-training, making them well-suited for CIL. However, real-world visual and linguistic concepts are inherently hierarchical: a textual concept like "dog" subsumes fine-grained categories such as "Labrador" and "Golden Retriever," and each category entails its images. But existing CLIP-based CIL methods fail to explicitly capture this inherent hierarchy, leading to fine-grained class features drift during incremental updates and ultimately to catastrophic forgetting. To address this challenge, we propose HASTEN (Hierarchical Semantic Tree Anchoring) that anchors hierarchical information into CIL to reduce catastrophic forgetting. First, we employ an external knowledge graph as supervision to embed visual and textual features in hyperbolic space, effectively preserving hierarchical structure as data evolves. Second, to mitigate catastrophic forgetting, we project gradients onto the null space of the shared hyperbolic mapper, preventing interference with prior tasks. These two steps work synergistically to enable the model to resist forgetting by maintaining hierarchical relationships. Extensive experiments show that HASTEN consistently outperforms existing methods while providing a unified structured representation.

