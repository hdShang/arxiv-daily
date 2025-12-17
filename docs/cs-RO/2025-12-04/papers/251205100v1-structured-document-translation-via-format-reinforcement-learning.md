---
layout: default
title: Structured Document Translation via Format Reinforcement Learning
---

# Structured Document Translation via Format Reinforcement Learning

**arXiv**: [2512.05100v1](https://arxiv.org/abs/2512.05100) | [PDF](https://arxiv.org/pdf/2512.05100.pdf)

**作者**: Haiyue Song, Johannes Eschbach-Dymanus, Hour Kaing, Sumire Honda, Hideki Tanaka, Bianka Buschbeck, Masao Utiyama

---

## 💡 一句话要点

**提出格式强化学习以优化结构化文档翻译，通过树相似度和节点翻译质量奖励提升性能。**

**关键词**: `结构化文档翻译` `强化学习` `XML树相似度` `节点翻译质量` `策略优化` `文档级处理`

## 📋 核心要点

1. 核心问题：现有结构化文本翻译局限于句子级别，难以处理复杂文档级XML或HTML结构。
2. 方法要点：基于监督微调模型，采用组相对策略优化，直接优化树相似度和节点翻译质量奖励。
3. 实验或效果：在SAP软件文档基准上，六项指标均有提升，分析显示不同奖励函数对结构和翻译质量改进的贡献。

## 📄 摘要（原文）

> Recent works on structured text translation remain limited to the sentence level, as they struggle to effectively handle the complex document-level XML or HTML structures. To address this, we propose \textbf{Format Reinforcement Learning (FormatRL)}, which employs Group Relative Policy Optimization on top of a supervised fine-tuning model to directly optimize novel structure-aware rewards: 1) TreeSim, which measures structural similarity between predicted and reference XML trees and 2) Node-chrF, which measures translation quality at the level of XML nodes. Additionally, we apply StrucAUC, a fine-grained metric distinguishing between minor errors and major structural failures. Experiments on the SAP software-documentation benchmark demonstrate improvements across six metrics and an analysis further shows how different reward functions contribute to improvements in both structural and translation quality.

