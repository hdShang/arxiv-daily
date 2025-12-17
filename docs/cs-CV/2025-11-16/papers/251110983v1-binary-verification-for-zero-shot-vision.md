---
layout: default
title: Binary Verification for Zero-Shot Vision
---

# Binary Verification for Zero-Shot Vision

**arXiv**: [2511.10983v1](https://arxiv.org/abs/2511.10983) | [PDF](https://arxiv.org/pdf/2511.10983.pdf)

**作者**: Jeffrey Liu, Rongbin Hu

---

## 💡 一句话要点

**提出无训练二进制验证工作流以增强零样本视觉任务性能**

**关键词**: `零样本视觉` `二进制验证` `多选问题` `真伪验证` `推理优化` `视觉语言模型`

## 📋 核心要点

1. 核心问题：开放查询在零样本视觉中易出错，需提升推理准确性。
2. 方法要点：通过量化和二值化步骤，将查询转为多选和真伪验证问题。
3. 实验效果：在多个任务中显著提升准确率，证明方法的通用性。

## 📄 摘要（原文）

> We propose a training-free, binary verification workflow for zero-shot vision with off-the-shelf VLMs. It comprises two steps: (i) quantization, which turns the open-ended query into a multiple-choice question (MCQ) with a small, explicit list of unambiguous candidates; and (ii) binarization, which asks one True/False question per candidate and resolves deterministically: if exactly one is True, select it; otherwise, revert to an MCQ over the remaining plausible candidates. We evaluate the workflow on referring expression grounding (REC), spatial reasoning (Spatial-Map, Spatial-Grid, Spatial-Maze), and BLINK-Jigsaw. Relative to answering open-ended queries directly, quantization to MCQ yields large gains, and True/False binarization provides a consistent additional boost. Across all tasks, the same workflow produces significant improvements, indicating generality. Our theory formalizes how open-ended vision queries can be quantized to MCQs and further binarized into True/False verifications, establishing a hardness ladder. A simple analysis explains why Boolean resolution boosts accuracy. Together, these components yield a simple and unified workflow that emphasizes inference-time design over task-specific training. It offers a practical, drop-in path to stronger zero-shot vision with today's VLMs.

