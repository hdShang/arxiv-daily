---
layout: default
title: On the Theoretical Foundation of Sparse Dictionary Learning in Mechanistic Interpretability
---

# On the Theoretical Foundation of Sparse Dictionary Learning in Mechanistic Interpretability

**arXiv**: [2512.05534v1](https://arxiv.org/abs/2512.05534) | [PDF](https://arxiv.org/pdf/2512.05534.pdf)

**作者**: Yiming Tang, Harshvardhan Saini, Yizhen Liao, Dianbo Liu

---

## 💡 一句话要点

**提出统一理论框架以分析稀疏字典学习在机制可解释性中的优化问题**

**关键词**: `稀疏字典学习` `机制可解释性` `优化理论` `特征解耦` `神经网络表示`

## 📋 核心要点

1. 核心问题：稀疏字典学习方法缺乏统一理论分析，现有理论局限于特定约束
2. 方法要点：建立统一优化框架，涵盖稀疏自编码器等多种方法，分析优化景观
3. 实验或效果：理论解释特征吸收等现象，并通过控制实验验证理论结果

## 📄 摘要（原文）

> As AI models achieve remarkable capabilities across diverse domains, understanding what representations they learn and how they process information has become increasingly important for both scientific progress and trustworthy deployment. Recent works in mechanistic interpretability have shown that neural networks represent meaningful concepts as directions in their representation spaces and often encode many concepts in superposition. Various sparse dictionary learning (SDL) methods, including sparse autoencoders, transcoders, and crosscoders, address this by training auxiliary models with sparsity constraints to disentangle these superposed concepts into interpretable features. These methods have demonstrated remarkable empirical success but have limited theoretical understanding. Existing theoretical work is limited to sparse autoencoders with tied-weight constraints, leaving the broader family of SDL methods without formal grounding. In this work, we develop the first unified theoretical framework considering SDL as one unified optimization problem. We demonstrate how diverse methods instantiate the theoretical framwork and provide rigorous analysis on the optimization landscape. We provide the first theoretical explanations for some empirically observed phenomena, including feature absorption, dead neurons, and the neuron resampling technique. We further design controlled experiments to validate our theoretical results.

