---
layout: default
title: PRISM-Bench: A Benchmark of Puzzle-Based Visual Tasks with CoT Error Detection
---

# PRISM-Bench: A Benchmark of Puzzle-Based Visual Tasks with CoT Error Detection

**arXiv**: [2510.23594v1](https://arxiv.org/abs/2510.23594) | [PDF](https://arxiv.org/pdf/2510.23594.pdf)

**作者**: Yusu Qian, Cheng Wan, Chao Jia, Yinfei Yang, Qingyu Zhao, Zhe Gan

---

## 💡 一句话要点

**提出PRISM-Bench基准，通过视觉谜题和思维链错误检测评估多模态推理能力。**

**关键词**: `视觉推理基准` `思维链错误检测` `多模态大语言模型` `逻辑一致性评估` `诊断评估协议`

## 📋 核心要点

1. 核心问题：现有模型在视觉推理中流畅生成与忠实推理间存在差距，难以检测逻辑错误。
2. 方法要点：设计包含单步错误的思维链任务，要求模型识别首个错误步骤。
3. 实验效果：评估显示先进模型在错误检测上表现不佳，突显诊断评估的必要性。

## 📄 摘要（原文）

> We introduce \textbf{PRISM-Bench}, a benchmark of puzzle-based visual
> challenges designed to evaluate not only whether models can solve problems, but
> how their reasoning unfolds. Unlike prior evaluations that measure only
> final-answer accuracy, PRISM-Bench introduces a diagnostic task: given a visual
> puzzle and a step-by-step chain-of-thought (CoT) containing exactly one error,
> models must identify the first incorrect step. This setting enables
> fine-grained assessment of logical consistency, error detection, and visual
> reasoning. The puzzles in PRISM-Bench require multi-step symbolic, geometric,
> and analogical reasoning, resisting shortcuts based on superficial pattern
> matching. Evaluations across state-of-the-art MLLMs reveal a persistent gap
> between fluent generation and faithful reasoning: models that produce plausible
> CoTs often fail to locate simple logical faults. By disentangling answer
> generation from reasoning verification, PRISM-Bench offers a sharper lens on
> multimodal reasoning competence and underscores the need for diagnostic
> evaluation protocols in the development of trustworthy MLLMs.

