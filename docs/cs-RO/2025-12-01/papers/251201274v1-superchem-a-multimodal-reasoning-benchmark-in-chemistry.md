---
layout: default
title: SUPERChem: A Multimodal Reasoning Benchmark in Chemistry
---

# SUPERChem: A Multimodal Reasoning Benchmark in Chemistry

**arXiv**: [2512.01274v1](https://arxiv.org/abs/2512.01274) | [PDF](https://arxiv.org/pdf/2512.01274.pdf)

**作者**: Zehua Zhao, Zhixian Huang, Junren Li, Siyu Lin, Junting Zhou, Fengqi Cao, Kun Zhou, Rui Ge, Tingting Long, Yuexiang Zhu, Yan Liu, Jie Zheng, Junnian Wei, Rong Zhu, Peng Zou, Wenyu Li, Zekai Cheng, Tian Ding, Yaxuan Wang, Yizhao Yan, Tingru Wei, Haowei Ming, Weijie Mao, Chen Sun, Yiming Liu, Zichen Wang, Zuo Zhang, Tong Yang, Hao Ma, Zhen Gao, Jian Pei

---

## 💡 一句话要点

**提出SUPERChem基准以评估大语言模型在化学领域的专家级推理能力**

**关键词**: `化学推理基准` `多模态评估` `推理路径保真度` `专家级问题` `大语言模型评估` `数据污染缓解`

## 📋 核心要点

1. 现有化学推理基准存在任务简化、缺乏过程评估和与专家技能不匹配的问题
2. SUPERChem包含500个专家策划的多模态推理密集型化学问题，采用推理路径保真度评分
3. 评估显示最佳模型GPT-5（高）准确率仅38.5%，低于人类基线40.3%，凸显挑战性

## 📄 摘要（原文）

> Current benchmarks for evaluating the chemical reasoning capabilities of Large Language Models (LLMs) are limited by oversimplified tasks, lack of process-level evaluation, and misalignment with expert-level chemistry skills. To address these issues, we introduce SUPERChem, a benchmark of 500 expert-curated reasoning-intensive chemistry problems, covering diverse subfields and provided in both multimodal and text-only formats. Original content and an iterative curation pipeline eliminate flawed items and mitigate data contamination. Each problem is paired with an expert-authored solution path, enabling Reasoning Path Fidelity (RPF) scoring to evaluate reasoning quality beyond final-answer accuracy. Evaluations against a human baseline of 40.3% accuracy show that even the best-performing model, GPT-5 (High), reaches only 38.5%, followed closely by Gemini 2.5 Pro (37.9%) and DeepSeek-V3.1-Think (37.3%). SUPERChem elicits multi-step, multimodal reasoning, reveals model-dependent effects of visual information, and distinguishes high-fidelity reasoners from heuristic ones. By providing a challenging benchmark and a reliable evaluation framework, SUPERChem aims to facilitate the advancement of LLMs toward expert-level chemical intelligence. The dataset of the benchmark is available at https://huggingface.co/datasets/ZehuaZhao/SUPERChem.

