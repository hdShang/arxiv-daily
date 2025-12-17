---
layout: default
title: Adaptive Identification and Modeling of Clinical Pathways with Process Mining
---

# Adaptive Identification and Modeling of Clinical Pathways with Process Mining

**arXiv**: [2512.03787v1](https://arxiv.org/abs/2512.03787) | [PDF](https://arxiv.org/pdf/2512.03787.pdf)

**作者**: Francesco Vitale, Nicola Mazzocca

---

## 💡 一句话要点

**提出基于过程挖掘的两阶段建模方法，以自适应识别和建模临床路径，解决手动建模困难问题。**

**关键词**: `临床路径建模` `过程挖掘` `一致性检查` `自适应建模` `医疗数据分析`

## 📋 核心要点

1. 核心问题：手动建模临床路径困难，难以反映疾病变体或组合的实际最佳实践。
2. 方法要点：使用过程挖掘，通过历史数据构建参考模型，并基于新数据验证一致性以扩展知识库。
3. 实验或效果：在Synthea数据集上验证，AUC峰值达95.62%，弧度简洁度为67.11%。

## 📄 摘要（原文）

> Clinical pathways are specialized healthcare plans that model patient treatment procedures. They are developed to provide criteria-based progression and standardize patient treatment, thereby improving care, reducing resource use, and accelerating patient recovery. However, manual modeling of these pathways based on clinical guidelines and domain expertise is difficult and may not reflect the actual best practices for different variations or combinations of diseases. We propose a two-phase modeling method using process mining, which extends the knowledge base of clinical pathways by leveraging conformance checking diagnostics. In the first phase, historical data of a given disease is collected to capture treatment in the form of a process model. In the second phase, new data is compared against the reference model to verify conformance. Based on the conformance checking results, the knowledge base can be expanded with more specific models tailored to new variants or disease combinations. We demonstrate our approach using Synthea, a benchmark dataset simulating patient treatments for SARS-CoV-2 infections with varying COVID-19 complications. The results show that our method enables expanding the knowledge base of clinical pathways with sufficient precision, peaking to 95.62% AUC while maintaining an arc-degree simplicity of 67.11%.

