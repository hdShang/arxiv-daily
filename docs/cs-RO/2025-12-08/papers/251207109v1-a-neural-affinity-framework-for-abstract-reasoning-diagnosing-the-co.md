---
layout: default
title: A Neural Affinity Framework for Abstract Reasoning: Diagnosing the Compositional Gap in Transformer Architectures via Procedural Task Taxonomy
---

# A Neural Affinity Framework for Abstract Reasoning: Diagnosing the Compositional Gap in Transformer Architectures via Procedural Task Taxonomy

**arXiv**: [2512.07109v1](https://arxiv.org/abs/2512.07109) | [PDF](https://arxiv.org/pdf/2512.07109.pdf)

**作者**: Miguel Ingram, Arthur Joseph Merritt

---

## 💡 一句话要点

**提出神经亲和力框架以诊断Transformer在抽象推理任务中的组合性差距**

**关键词**: `抽象推理` `Transformer架构` `任务分类法` `神经亲和力` `组合性差距` `ARC-AGI-2`

## 📋 核心要点

1. 核心问题：Transformer架构在抽象推理任务中存在组合性差距，导致局部模式学习与全局合成能力不匹配
2. 方法要点：基于规则代码分析构建9类任务分类法，用于评估任务与神经网络的亲和力
3. 实验或效果：在ARC-AGI-2测试集上，69.5%的任务显示高局部准确率但低全局准确率，验证了神经亲和力天花板效应

## 📄 摘要（原文）

> Responding to Hodel et al.'s (2024) call for a formal definition of task relatedness in re-arc, we present the first 9-category taxonomy of all 400 tasks, validated at 97.5% accuracy via rule-based code analysis. We prove the taxonomy's visual coherence by training a CNN on raw grid pixels (95.24% accuracy on S3, 36.25% overall, 3.3x chance), then apply the taxonomy diagnostically to the original ARC-AGI-2 test set. Our curriculum analysis reveals 35.3% of tasks exhibit low neural affinity for Transformers--a distributional bias mirroring ARC-AGI-2. To probe this misalignment, we fine-tuned a 1.7M-parameter Transformer across 302 tasks, revealing a profound Compositional Gap: 210 of 302 tasks (69.5%) achieve >80% cell accuracy (local patterns) but <10% grid accuracy (global synthesis). This provides direct evidence for a Neural Affinity Ceiling Effect, where performance is bounded by architectural suitability, not curriculum. Applying our framework to Li et al.'s independent ViTARC study (400 specialists, 1M examples each) confirms its predictive power: Very Low affinity tasks achieve 51.9% versus 77.7% for High affinity (p<0.001), with a task at 0% despite massive data. The taxonomy enables precise diagnosis: low-affinity tasks (A2) hit hard ceilings, while high-affinity tasks (C1) reach 99.8%. These findings indicate that progress requires hybrid architectures with affinity-aligned modules. We release our validated taxonomy,

