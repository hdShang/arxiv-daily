---
layout: default
title: EmoRAG: Evaluating RAG Robustness to Symbolic Perturbations
---

# EmoRAG: Evaluating RAG Robustness to Symbolic Perturbations

**arXiv**: [2512.01335v1](https://arxiv.org/abs/2512.01335) | [PDF](https://arxiv.org/pdf/2512.01335.pdf)

**作者**: Xinyun Zhou, Xinfeng Li, Yinan Peng, Ming Xu, Xuanwang Zhang, Miao Yu, Yidong Wang, Xiaojun Jia, Kun Wang, Qingsong Wen, XiaoFeng Wang, Wei Dong

---

## 💡 一句话要点

**提出EmoRAG以揭示检索增强生成系统对表情符号扰动的脆弱性**

**关键词**: `检索增强生成` `符号扰动` `表情符号攻击` `系统脆弱性` `对抗防御`

## 📋 核心要点

1. 核心问题：RAG系统对表情符号等符号扰动高度敏感，导致检索失效。
2. 方法要点：通过注入表情符号扰动查询，分析RAG的检索和生成机制。
3. 实验或效果：单表情符号可近100%误导检索，大参数模型更易受影响。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems are increasingly central to robust AI, enhancing large language model (LLM) faithfulness by incorporating external knowledge. However, our study unveils a critical, overlooked vulnerability: their profound susceptibility to subtle symbolic perturbations, particularly through near-imperceptible emoticon tokens such as "(@_@)" that can catastrophically mislead retrieval, termed EmoRAG. We demonstrate that injecting a single emoticon into a query makes it nearly 100% likely to retrieve semantically unrelated texts that contain a matching emoticon. Our extensive experiment across general question-answering and code domains, using a range of state-of-the-art retrievers and generators, reveals three key findings: (I) Single-Emoticon Disaster: Minimal emoticon injections cause maximal disruptions, with a single emoticon almost 100% dominating RAG output. (II) Positional Sensitivity: Placing an emoticon at the beginning of a query can cause severe perturbation, with F1-Scores exceeding 0.92 across all datasets. (III) Parameter-Scale Vulnerability: Counterintuitively, models with larger parameters exhibit greater vulnerability to the interference. We provide an in-depth analysis to uncover the underlying mechanisms of these phenomena. Furthermore, we raise a critical concern regarding the robustness assumption of current RAG systems, envisioning a threat scenario where an adversary exploits this vulnerability to manipulate the RAG system. We evaluate standard defenses and find them insufficient against EmoRAG. To address this, we propose targeted defenses, analyzing their strengths and limitations in mitigating emoticon-based perturbations. Finally, we outline future directions for building robust RAG systems.

