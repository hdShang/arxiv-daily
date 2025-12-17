---
layout: default
title: FreqEdit: Preserving High-Frequency Features for Robust Multi-Turn Image Editing
---

# FreqEdit: Preserving High-Frequency Features for Robust Multi-Turn Image Editing

**arXiv**: [2512.01755v1](https://arxiv.org/abs/2512.01755) | [PDF](https://arxiv.org/pdf/2512.01755.pdf)

**作者**: Yucheng Liao, Jiajun Liang, Kaiqian Cui, Baoquan Zhao, Haoran Xie, Wei Liu, Qing Li, Xudong Mao

---

## 💡 一句话要点

**提出FreqEdit框架以解决多轮图像编辑中的高频特征丢失问题**

**关键词**: `多轮图像编辑` `高频特征保留` `训练免费框架` `自适应注入` `路径补偿` `指令遵循`

## 📋 核心要点

1. 核心问题：多轮图像编辑导致高频信息渐进丢失，引发质量下降
2. 方法要点：通过高频特征注入、自适应注入策略和路径补偿机制，无需训练实现稳定编辑
3. 实验或效果：在10+轮次编辑中优于七种基线，保持身份和指令遵循

## 📄 摘要（原文）

> Instruction-based image editing through natural language has emerged as a powerful paradigm for intuitive visual manipulation. While recent models achieve impressive results on single edits, they suffer from severe quality degradation under multi-turn editing. Through systematic analysis, we identify progressive loss of high-frequency information as the primary cause of this quality degradation. We present FreqEdit, a training-free framework that enables stable editing across 10+ consecutive iterations. Our approach comprises three synergistic components: (1) high-frequency feature injection from reference velocity fields to preserve fine-grained details, (2) an adaptive injection strategy that spatially modulates injection strength for precise region-specific control, and (3) a path compensation mechanism that periodically recalibrates the editing trajectory to prevent over-constraint. Extensive experiments demonstrate that FreqEdit achieves superior performance in both identity preservation and instruction following compared to seven state-of-the-art baselines.

