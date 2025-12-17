---
layout: default
title: Revisiting Generalization Across Difficulty Levels: It's Not So Easy
---

# Revisiting Generalization Across Difficulty Levels: It's Not So Easy

**arXiv**: [2511.21692v1](https://arxiv.org/abs/2511.21692) | [PDF](https://arxiv.org/pdf/2511.21692.pdf)

**作者**: Yeganeh Kordi, Nihal V. Nayak, Max Zuo, Ilana Nguyen, Stephen H. Bach

---

## 💡 一句话要点

**评估大语言模型跨难度泛化能力，揭示训练数据难度范围的重要性**

**关键词**: `大语言模型` `泛化能力` `任务难度` `项目反应理论` `数据筛选` `模型评估`

## 📋 核心要点

1. 核心问题：大语言模型在不同任务难度下的泛化能力，影响数据筛选与评估策略
2. 方法要点：使用多种LLM输出和项目反应理论，客观量化示例难度，避免人为偏见
3. 实验或效果：跨难度泛化有限，训练数据需覆盖多种难度，避免单一难度风险

## 📄 摘要（原文）

> We investigate how well large language models (LLMs) generalize across different task difficulties, a key question for effective data curation and evaluation. Existing research is mixed regarding whether training on easier or harder data leads to better results, and whether those gains come on easier or harder test data. We address this question by conducting a systematic evaluation of LLMs' generalization across models, datasets, and fine-grained groups of example difficulty. We rank examples in six datasets using the outputs of thousands of different LLMs and Item Response Theory (IRT), a well-established difficulty metric in educational testing. Unlike prior work, our difficulty ratings are therefore determined solely by the abilities of many different LLMs, excluding human opinions of difficulty. With a more objective, larger-scale, and finer-grained analysis, we show that cross-difficulty generalization is often limited; training on either easy or hard data cannot achieve consistent improvements across the full range of difficulties. These results show the importance of having a range of difficulties in both training and evaluation data for LLMs, and that taking shortcuts with respect to difficulty is risky.

