---
layout: default
title: Multicalibration for LLM-based Code Generation
---

# Multicalibration for LLM-based Code Generation

**arXiv**: [2512.08810v1](https://arxiv.org/abs/2512.08810) | [PDF](https://arxiv.org/pdf/2512.08810.pdf)

**作者**: Viola Campos, Robin Kuschnereit, Adrian Ulges

---

## 💡 一句话要点

**提出多校准方法以提升代码大语言模型的置信度校准效果**

**关键词**: `代码生成` `大语言模型校准` `多校准` `置信度评估` `函数合成基准`

## 📋 核心要点

1. 研究代码大语言模型置信度校准问题，确保置信分数准确反映代码正确性概率
2. 采用多校准方法，考虑编程语言、代码长度和复杂度等因素，提升校准性能
3. 在三个函数合成基准上测试四种多校准方法，相比基线校准提升0.37技能分数

## 📄 摘要（原文）

> As AI-based code generation becomes widespread, researchers are investigating the calibration of code LLMs - ensuring their confidence scores faithfully represent the true likelihood of code correctness. To do so, we investigate multicalibration, which can capture additional factors about a coding problem, such as complexity, code length, or programming language used. We study four multicalibration approaches on three function synthesis benchmarks, using latest-generation code LLMs (Qwen3 Coder, GPT-OSS, DeepSeek-R1-Distill). Our results demonstrate that multicalibration can yield distinct improvements over both uncalibrated token likelihoods (+1.03 in skill score) and baseline calibrations (+0.37 in skill score). We study the influence of the aforementioned factors in ablations, and make our dataset (consisting of code generations, likelihoods, and correctness labels) available for future research on code LLM calibration.

