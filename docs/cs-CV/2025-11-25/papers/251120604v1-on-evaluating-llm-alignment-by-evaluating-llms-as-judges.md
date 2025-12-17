---
layout: default
title: On Evaluating LLM Alignment by Evaluating LLMs as Judges
---

# On Evaluating LLM Alignment by Evaluating LLMs as Judges

**arXiv**: [2511.20604v1](https://arxiv.org/abs/2511.20604) | [PDF](https://arxiv.org/pdf/2511.20604.pdf)

**作者**: Yixin Liu, Pengfei Liu, Arman Cohan

---

## 💡 一句话要点

**提出AlignEval基准，通过评估LLM作为评判者来衡量其与人类偏好对齐**

**关键词**: `LLM对齐评估` `生成-评估一致性` `自动基准构建` `人类偏好对齐` `LLM评判能力`

## 📋 核心要点

1. 核心问题：LLM对齐评估依赖人类或强LLM评判，成本高且复杂
2. 方法要点：分析生成-评估一致性，构建基于LLM评判的基准AlignEval
3. 实验或效果：AlignEval在排名LLM时优于或匹配现有自动评估基准

## 📄 摘要（原文）

> Alignment with human preferences is an important evaluation aspect of LLMs, requiring them to be helpful, honest, safe, and to precisely follow human instructions. Evaluating large language models' (LLMs) alignment typically involves directly assessing their open-ended responses, requiring human annotators or strong LLM judges. Conversely, LLMs themselves have also been extensively evaluated as judges for assessing alignment. In this work, we examine the relationship between LLMs' generation and evaluation capabilities in aligning with human preferences. To this end, we first conduct a comprehensive analysis of the generation-evaluation consistency (GE-consistency) among various LLMs, revealing a strong correlation between their generation and evaluation capabilities when evaluated by a strong LLM preference oracle. Utilizing this finding, we propose a benchmarking paradigm that measures LLM alignment with human preferences without directly evaluating their generated outputs, instead assessing LLMs in their role as evaluators. Our evaluation shows that our proposed benchmark, AlignEval, matches or surpasses widely used automatic LLM evaluation benchmarks, such as AlpacaEval and Arena-Hard, in capturing human preferences when ranking LLMs. Our study offers valuable insights into the connection between LLMs' generation and evaluation capabilities, and introduces a benchmark that assesses alignment without directly evaluating model outputs.

