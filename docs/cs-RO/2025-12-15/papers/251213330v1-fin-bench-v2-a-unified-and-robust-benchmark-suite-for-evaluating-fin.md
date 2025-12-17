---
layout: default
title: FIN-bench-v2: A Unified and Robust Benchmark Suite for Evaluating Finnish Large Language Models
---

# FIN-bench-v2: A Unified and Robust Benchmark Suite for Evaluating Finnish Large Language Models

**arXiv**: [2512.13330v1](https://arxiv.org/abs/2512.13330) | [PDF](https://arxiv.org/pdf/2512.13330.pdf)

**作者**: Joona Kytöniemi, Jousia Piha, Akseli Reunamo, Fedor Vitiugin, Farrokh Mehryary, Sampo Pyysalo

---

## 💡 一句话要点

**提出FIN-bench-v2统一基准套件以评估芬兰语大语言模型**

**关键词**: `芬兰语大语言模型` `基准评估` `任务鲁棒性` `多任务覆盖` `公开数据集`

## 📋 核心要点

1. 核心问题：缺乏统一且鲁棒的芬兰语大语言模型评估基准
2. 方法要点：整合并扩展现有基准，通过模型学习曲线筛选鲁棒任务
3. 实验或效果：评估指令调优模型，公开数据集和评估配置

## 📄 摘要（原文）

> We introduce FIN-bench-v2, a unified benchmark suite for evaluating large language models in Finnish. FIN-bench-v2 consolidates Finnish versions of widely used benchmarks together with an updated and expanded version of the original FIN-bench into a single, consistently formatted collection, covering multiple-choice and generative tasks across reading comprehension, commonsense reasoning, sentiment analysis, world knowledge, and alignment. All datasets are converted to HuggingFace Datasets, which include both cloze and multiple-choice prompt formulations with five variants per task, and we incorporate human annotation or review for machine-translated resources such as GoldenSwag and XED. To select robust tasks, we pretrain a set of 2.15B-parameter decoder-only models and use their learning curves to compute monotonicity, signal-to-noise, non-random performance, and model ordering consistency, retaining only tasks that satisfy all criteria. We further evaluate a set of larger instruction-tuned models to characterize performance across tasks and prompt formulations. All datasets, prompts, and evaluation configurations are publicly available via our fork of the Language Model Evaluation Harness at https://github.com/LumiOpen/lm-evaluation-harness. Supplementary resources are released in a separate repository at https://github.com/TurkuNLP/FIN-bench-v2.

