---
layout: default
title: Evolutionary System 2 Reasoning: An Empirical Proof
---

# Evolutionary System 2 Reasoning: An Empirical Proof

**arXiv**: [2512.05760v1](https://arxiv.org/abs/2512.05760) | [PDF](https://arxiv.org/pdf/2512.05760.pdf)

**作者**: Zeyuan Ma, Wenqi Huang, Guo-Huan Song, Hongshu Guo, Sijie Ma, Zhiguang Cao, Yue-Jiao Gong

---

## 💡 一句话要点

**提出进化推理优化框架，通过进化策略增强大语言模型的系统2推理能力。**

**关键词**: `进化推理优化` `系统2推理` `大语言模型` `进化策略` `推理能力增强`

## 📋 核心要点

1. 核心问题：大语言模型在通用智能和系统2推理方面仍有限，能否进化获得类似人类的推理能力？
2. 方法要点：使用进化策略对LLM种群进行适者生存优化，最大化最佳个体的量化推理分数。
3. 实验或效果：实验显示GPT-5推理能力有限，但Qwen-7B经简单进化循环后可显著提升推理能力。

## 📄 摘要（原文）

> Machine intelligence marks the ultimate dream of making machines' intelligence comparable to human beings. While recent progress in Large Language Models (LLMs) show substantial specific skills for a wide array of downstream tasks, they more or less fall shorts in general intelligence. Following correlation between intelligence and system 2 reasoning (slow thinking), in this paper, we aim to answering a worthwhile research question: could machine intelligence such as LLMs be evolved to acquire reasoning ability (not specific skill) just like our human beings? To this end, we propose evolutionary reasoning optimization (ERO) framework which performs survival of the fittest over a population of LLMs to search for individual with strong reasoning ability. Given a reasoning task, ERO first initializes multiple LLMs as a population, after which an evolutionary strategy evolves the population to maximize quantified reasoning score of the best individual. Based on experiments on representative testsuites, we claim two surprising empirical discoveries: i) the latest LLMs such as GPT-5 still show limited system 2 reasoning ability; ii) with simple evolution-loop of ERO, a relatively weak model (Qwen-7B) could be enhanced to emerge powerful reasoning ability. Our project can be accessed at https://github.com/MetaEvo/ERO for reproduction needs.

