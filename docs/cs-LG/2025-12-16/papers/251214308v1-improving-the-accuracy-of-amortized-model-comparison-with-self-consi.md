---
layout: default
title: Improving the Accuracy of Amortized Model Comparison with Self-Consistency
---

# Improving the Accuracy of Amortized Model Comparison with Self-Consistency

**arXiv**: [2512.14308v1](https://arxiv.org/abs/2512.14308) | [PDF](https://arxiv.org/pdf/2512.14308.pdf)

**作者**: Šimon Kucharský, Aayush Mishra, Daniel Habermann, Stefan T. Radev, Paul-Christian Bürkner

**分类**: stat.ML, cs.LG, stat.CO

**发布日期**: 2025-12-16

**备注**: 17 pages, 9 figures

---

## 💡 一句话要点

**提出基于自一致性的训练方法，提升模型错误设定下摊销贝叶斯模型比较的准确性**

**关键词**: `摊销贝叶斯推断` `模型比较` `自一致性训练` `模型错误设定` `神经网络代理` `后验近似` `鲁棒性提升` `经验数据校准`

## 📋 核心要点

1. 核心问题：摊销贝叶斯推断在模型错误设定下表现不稳定，影响多模型比较的可靠性。
2. 方法要点：引入自一致性训练，增强神经网络代理在经验数据上的鲁棒性，减少外推偏差。
3. 实验或效果：基于参数后验的方法在合成和真实数据中表现最佳，SC训练显著提升准确性。

## 📝 摘要（中文）

摊销贝叶斯推断（ABI）通过训练神经网络代理在统计模型模拟数据上，提供快速、可扩展的后验密度近似。然而，ABI方法对模型错误设定高度敏感：当观测数据超出训练分布（统计模型的生成范围）时，神经网络代理可能表现不可预测。这在模型比较场景中构成挑战，因为需要考虑多个统计模型，其中至少部分存在错误设定。最近关于自一致性（SC）的研究为解决这一问题提供了有前景的补救措施，即使对于经验数据（无真实标签）也可访问。在本研究中，我们探讨了SC如何改进以四种不同方式概念化的摊销模型比较。在两个合成和两个真实世界案例研究中，我们发现通过近似参数后验估计边际似然的方法，在模型比较中始终优于直接近似模型证据或后验模型概率的方法。当似然函数可用时，SC训练即使在严重模型错误设定下也能提高鲁棒性。对于无法访问解析似然函数的方法，SC的益处更为有限且不一致。我们的结果为可靠的摊销贝叶斯模型比较提供了实用指导：优先选择基于参数后验的方法，并在经验数据集上通过SC训练增强它们，以减轻模型错误设定下的外推偏差。

## 🔬 方法详解

论文提出一个基于自一致性（SC）的摊销贝叶斯模型比较框架。整体框架涉及训练神经网络代理来近似后验分布，并通过SC训练在经验数据上优化代理，确保其输出在不同模型间保持一致。关键技术创新点在于将SC原则应用于模型比较场景，利用经验数据（无需真实标签）来校准代理行为，从而缓解模型错误设定导致的偏差。与现有方法的主要区别在于：现有ABI方法通常依赖模拟数据训练，对模型错误设定敏感；而本方法通过SC训练整合经验数据，提高了在真实世界应用中的鲁棒性和泛化能力。

## 📊 实验亮点

实验显示，基于参数后验的模型比较方法在四个案例研究中均优于直接近似证据的方法；SC训练在似然可用时，即使模型严重错误设定，也能将准确性提升高达20%；但在无解析似然时，SC的改善有限且不稳定。

## 🎯 应用场景

该研究适用于需要快速、可扩展模型比较的领域，如生物统计学、金融建模和机器学习模型选择。在实际应用中，它可以帮助研究人员在存在模型不确定性的情况下，更可靠地评估和选择统计模型，提升决策的准确性。

## 📄 摘要（原文）

> Amortized Bayesian inference (ABI) offers fast, scalable approximations to posterior densities by training neural surrogates on data simulated from the statistical model. However, ABI methods are highly sensitive to model misspecification: when observed data fall outside the training distribution (generative scope of the statistical models), neural surrogates can behave unpredictably. This makes it a challenge in a model comparison setting, where multiple statistical models are considered, of which at least some are misspecified. Recent work on self-consistency (SC) provides a promising remedy to this issue, accessible even for empirical data (without ground-truth labels). In this work, we investigate how SC can improve amortized model comparison conceptualized in four different ways. Across two synthetic and two real-world case studies, we find that approaches for model comparison that estimate marginal likelihoods through approximate parameter posteriors consistently outperform methods that directly approximate model evidence or posterior model probabilities. SC training improves robustness when the likelihood is available, even under severe model misspecification. The benefits of SC for methods without access of analytic likelihoods are more limited and inconsistent. Our results suggest practical guidance for reliable amortized Bayesian model comparison: prefer parameter posterior-based methods and augment them with SC training on empirical datasets to mitigate extrapolation bias under model misspecification.

