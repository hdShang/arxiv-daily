---
layout: default
title: Metric-Fair Prompting: Treating Similar Samples Similarly
---

# Metric-Fair Prompting: Treating Similar Samples Similarly

**arXiv**: [2512.07608v1](https://arxiv.org/abs/2512.07608) | [PDF](https://arxiv.org/pdf/2512.07608.pdf)

**作者**: Jing Wang, Jie Shen, Xing Niu, Tong Zhang, Jeremy Weiss

---

## 💡 一句话要点

**提出度量公平提示框架，以提升大型语言模型在医学多选题中的个体公平性和准确性。**

**关键词**: `度量公平提示` `个体公平性` `医学问答` `大型语言模型` `Lipschitz约束` `置信度评分`

## 📋 核心要点

1. 核心问题：在医学多选题中，标准提示可能忽略相似问题间的公平性，导致不一致决策。
2. 方法要点：基于NLP嵌入计算问题相似度，通过联合处理相似问题对并施加Lipschitz约束，确保相似输入获得相似分数。
3. 实验或效果：在MedQA基准上，该框架相比标准单题提示提高了性能，证明公平引导的置信度推理能增强模型准确性。

## 📄 摘要（原文）

> We introduce \emph{Metric-Fair Prompting}, a fairness-aware prompting framework that guides large language models (LLMs) to make decisions under metric-fairness constraints. In the application of multiple-choice medical question answering, each {(question, option)} pair is treated as a binary instance with label $+1$ (correct) or $-1$ (incorrect). To promote {individual fairness}~--~treating similar instances similarly~--~we compute question similarity using NLP embeddings and solve items in \emph{joint pairs of similar questions} rather than in isolation. The prompt enforces a global decision protocol: extract decisive clinical features, map each \((\text{question}, \text{option})\) to a score $f(x)$ that acts as confidence, and impose a Lipschitz-style constraint so that similar inputs receive similar scores and, hence, consistent outputs. Evaluated on the {MedQA (US)} benchmark, Metric-Fair Prompting is shown to improve performance over standard single-item prompting, demonstrating that fairness-guided, confidence-oriented reasoning can enhance LLM accuracy on high-stakes clinical multiple-choice questions.

