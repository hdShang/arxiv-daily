---
layout: default
title: TRACE: A Framework for Analyzing and Enhancing Stepwise Reasoning in Vision-Language Models
---

# TRACE: A Framework for Analyzing and Enhancing Stepwise Reasoning in Vision-Language Models

**arXiv**: [2512.05943v1](https://arxiv.org/abs/2512.05943) | [PDF](https://arxiv.org/pdf/2512.05943.pdf)

**作者**: Shima Imani, Seungwhan Moon, Lambert Mathias, Lu Zhang, Babak Damavandi

---

## 💡 一句话要点

**提出TRACE框架以解决视觉语言模型在数学和科学推理中的透明性和一致性评估问题**

**关键词**: `视觉语言模型` `推理评估` `一致性分析` `辅助推理集` `模型调试` `数学推理`

## 📋 核心要点

1. 核心问题：标准最终答案评估掩盖推理错误，导致视觉语言模型在数学和科学推理中可靠性不足
2. 方法要点：利用辅助推理集分解复杂问题，通过基于一致性的指标评估中间步骤，诊断推理轨迹
3. 实验或效果：实验显示一致性相关于最终答案正确性，能定位失败步骤，支持模型改进和过滤不可靠路径

## 📄 摘要（原文）

> Reliable mathematical and scientific reasoning remains an open challenge for large vision-language models. Standard final-answer evaluation often masks reasoning errors, allowing silent failures to persist. To address this gap, we introduce TRACE, a framework for Transparent Reasoning And Consistency Evaluation that diagnoses reasoning trajectories rather than only end results. At its core, TRACE leverages Auxiliary Reasoning Sets, compact sub question answer pairs that decompose complex problems, evaluate intermediate steps through consistency-based metrics, and expose failures overlooked by standard evaluation. Our experiments show that consistency across ARS correlates with final-answer correctness and helps pinpoint the reasoning steps where failures arise, offering actionable signals for model improvement. Furthermore, TRACE defines confidence regions that distinguish reliable from unreliable reasoning paths, supporting effective filtering, debugging, and model refinement.

