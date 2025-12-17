---
layout: default
title: CodeFuse-CommitEval: Towards Benchmarking LLM's Power on Commit Message and Code Change Inconsistency Detection
---

# CodeFuse-CommitEval: Towards Benchmarking LLM's Power on Commit Message and Code Change Inconsistency Detection

**arXiv**: [2511.19875v1](https://arxiv.org/abs/2511.19875) | [PDF](https://arxiv.org/pdf/2511.19875.pdf)

**作者**: Qingyu Zhang, Puzhuo Liu, Peng Di, Chenxiong Qian

---

## 💡 一句话要点

**提出CODEFUSE-COMMITEVAL基准以评估LLM在提交消息与代码变更不一致检测中的能力**

**关键词**: `提交消息不一致检测` `大型语言模型基准` `代码变更分析` `增强策略评估` `语义不一致检测`

## 📋 核心要点

1. 核心问题：提交消息与代码变更不一致误导代码审查和维护，缺乏专用基准。
2. 方法要点：基于ApacheCM数据集，通过规则突变生成不一致消息，并验证样本质量。
3. 实验或效果：评估六种LLM，显示不一致检测更可靠，增强策略效果各异。

## 📄 摘要（原文）

> Version control relies on commit messages to convey the rationale for code changes, but these messages are often low quality and, more critically, inconsistent with their diffs-known as message-code inconsistency (MCI). MCIs mislead reviewers, hinder maintenance, contaminate research datasets, and may obscure security patches. Yet, no dedicated benchmark exists to evaluate models for MCI detection. We introduce CODEFUSE-COMMITEVAL, the first benchmark designed for MCI detection using large language models (LLMs). Built on the ApacheCM dataset for diversity and quality, we generate seven types of inconsistent messages through rule-guided mutations of originally consistent commits and apply two-fold validation to verify both positive and negative samples. Using this labeled dataset of message-diff pairs, we evaluate six state-of-the-art open-source LLMs under a vanilla setting and with three augmentation strategies: few-shot prompting, chain-of-thought, and extended context. Results show models detect inconsistent commits more reliably than consistent ones (average Recall 85.95%, Precision 80.28%, Specificity 63.8%); gpt-oss-20B performs best overall but uses over twice the tokens of others. Augmentation effects vary: adjacent context helps larger models but adds noise for smaller ones; few-shot improves accuracy and reduces token use, yet increases universally incorrect predictions; chain-of-thought boosts precision and specificity at the cost of recall and higher token consumption. Type-wise analysis reveals higher detectability for component, file-path, and operation inconsistencies, but lower accuracy and higher token cost for intent-level "purpose" inconsistencies. CODEFUSE-COMMITEVAL provides a rigorous foundation for measuring, comparing, and advancing MCI detection, highlighting the need for richer context and balanced data to capture high-level semantic gaps.

