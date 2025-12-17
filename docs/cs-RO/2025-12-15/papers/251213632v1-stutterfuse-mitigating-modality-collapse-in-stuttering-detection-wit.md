---
layout: default
title: StutterFuse: Mitigating Modality Collapse in Stuttering Detection with Jaccard-Weighted Metric Learning and Gated Fusion
---

# StutterFuse: Mitigating Modality Collapse in Stuttering Detection with Jaccard-Weighted Metric Learning and Gated Fusion

**arXiv**: [2512.13632v1](https://arxiv.org/abs/2512.13632) | [PDF](https://arxiv.org/pdf/2512.13632.pdf)

**作者**: Guransh Singh, Md Shah Fahad

---

## 💡 一句话要点

**提出StutterFuse检索增强分类器，通过Jaccard加权度量学习和门控融合缓解口吃检测中的模态崩溃问题**

**关键词**: `口吃检测` `检索增强分类` `多标签学习` `度量学习` `门控融合` `病理语音处理`

## 📋 核心要点

1. 核心问题：现有参数化模型难以区分训练数据中稀缺的重叠性口吃现象，且检索增强方法在病理语音处理中尚未探索
2. 方法要点：构建基于临床案例的非参数记忆库，采用Jaccard加权度量学习优化多标签集合相似性，设计门控专家混合融合策略
3. 实验效果：在SEP-28k数据集上获得0.65加权F1分数，表现出优异的零样本跨语言泛化能力

## 📄 摘要（原文）

> Stuttering detection breaks down when disfluencies overlap. Existing parametric models struggle to distinguish complex, simultaneous disfluencies (e.g., a 'block' with a 'prolongation') due to the scarcity of these specific combinations in training data. While Retrieval-Augmented Generation (RAG) has revolutionized NLP by grounding models in external knowledge, this paradigm remains unexplored in pathological speech processing. To bridge this gap, we introduce StutterFuse, the first Retrieval-Augmented Classifier (RAC) for multi-label stuttering detection. By conditioning a Conformer encoder on a non-parametric memory bank of clinical examples, we allow the model to classify by reference rather than memorization. We further identify and solve "Modality Collapse", an "Echo Chamber" effect where naive retrieval boosts recall but degrades precision. We mitigate this using: (1) SetCon, a Jaccard-Weighted Metric Learning objective that optimizes for multi-label set similarity, and (2) a Gated Mixture-of-Experts fusion strategy that dynamically arbitrates between acoustic evidence and retrieved context. On the SEP-28k dataset, StutterFuse achieves a weighted F1-score of 0.65, outperforming strong baselines and demonstrating remarkable zero-shot cross-lingual generalization.

