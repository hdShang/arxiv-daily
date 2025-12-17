---
layout: default
title: Identifying & Interactively Refining Ambiguous User Goals for Data Visualization Code Generation
---

# Identifying & Interactively Refining Ambiguous User Goals for Data Visualization Code Generation

**arXiv**: [2510.09390v1](https://arxiv.org/abs/2510.09390) | [PDF](https://arxiv.org/pdf/2510.09390.pdf)

**作者**: Mert İnan, Anthony Sicilia, Alex Xie, Saujas Vaduguru, Daniel Fried, Malihe Alikhani

---

## 💡 一句话要点

**提出歧义分类与多轮对话方法，以提升数据可视化代码生成的准确性。**

**关键词**: `数据可视化` `代码生成` `自然语言歧义` `多轮对话` `语用模型` `歧义分类`

## 📋 核心要点

1. 核心问题：自然语言歧义导致数据可视化代码生成不准确，影响用户意图匹配。
2. 方法要点：构建歧义分类法，并基于语用模型设计多轮对话策略以澄清目标。
3. 实验或效果：在DS-1000数据集上验证歧义指标优于基线，模拟用户研究显示对话提升代码准确率。

## 📄 摘要（原文）

> Establishing shared goals is a fundamental step in human-AI communication.
> However, ambiguities can lead to outputs that seem correct but fail to reflect
> the speaker's intent. In this paper, we explore this issue with a focus on the
> data visualization domain, where ambiguities in natural language impact the
> generation of code that visualizes data. The availability of multiple views on
> the contextual (e.g., the intended plot and the code rendering the plot) allows
> for a unique and comprehensive analysis of diverse ambiguity types. We develop
> a taxonomy of types of ambiguity that arise in this task and propose metrics to
> quantify them. Using Matplotlib problems from the DS-1000 dataset, we
> demonstrate that our ambiguity metrics better correlate with human annotations
> than uncertainty baselines. Our work also explores how multi-turn dialogue can
> reduce ambiguity, therefore, improve code accuracy by better matching user
> goals. We evaluate three pragmatic models to inform our dialogue strategies:
> Gricean Cooperativity, Discourse Representation Theory, and Questions under
> Discussion. A simulated user study reveals how pragmatic dialogues reduce
> ambiguity and enhance code accuracy, highlighting the value of multi-turn
> exchanges in code generation.

