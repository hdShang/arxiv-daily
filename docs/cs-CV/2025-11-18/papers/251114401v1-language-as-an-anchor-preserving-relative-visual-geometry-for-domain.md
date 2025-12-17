---
layout: default
title: Language as an Anchor: Preserving Relative Visual Geometry for Domain Incremental Learning
---

# Language as an Anchor: Preserving Relative Visual Geometry for Domain Incremental Learning

**arXiv**: [2511.14401v1](https://arxiv.org/abs/2511.14401) | [PDF](https://arxiv.org/pdf/2511.14401.pdf)

**作者**: Shuyi Geng, Tao Zhou, Yi Zhou

---

## 💡 一句话要点

**提出LAVA框架，利用语言锚点解决领域增量学习中的语义失真问题**

**关键词**: `领域增量学习` `语言锚点` `相对几何对齐` `语义相似性` `知识保留` `视觉表示学习`

## 📋 核心要点

1. 核心问题：领域增量学习面临统一视觉空间导致语义失真与隔离参数导致知识碎片化的困境
2. 方法要点：使用文本锚点驱动相对对齐，保持视觉表示的相对几何结构一致
3. 实验或效果：在标准基准测试中显著优于现有方法，代码已开源

## 📄 摘要（原文）

> A key challenge in Domain Incremental Learning (DIL) is to continually learn under shifting distributions while preserving knowledge from previous domains. Existing methods face a fundamental dilemma. On one hand, projecting all domains into a single unified visual space leads to inter-domain interference and semantic distortion, as large shifts may vary with not only visual appearance but also underlying semantics. On the other hand, isolating domain-specific parameters causes knowledge fragmentation, creating "knowledge islands" that hamper knowledge reuse and exacerbate forgetting. To address this issue, we propose LAVA (Language-Anchored Visual Alignment), a novel DIL framework that replaces direct feature alignment with relative alignment driven by a text-based reference anchor. LAVA guides the visual representations of each incoming domain to preserve a consistent relative geometry, which is defined by mirroring the pairwise semantic similarities between the class names. This anchored geometric structure acts as a bridge across domains, enabling the retrieval of class-aware prior knowledge and facilitating robust feature aggregation. Extensive experiments on standard DIL benchmarks demonstrate that LAVA achieves significant performance improvements over state-of-the-arts. Code is available at https://github.com/ShuyiGeng/LAVA.

