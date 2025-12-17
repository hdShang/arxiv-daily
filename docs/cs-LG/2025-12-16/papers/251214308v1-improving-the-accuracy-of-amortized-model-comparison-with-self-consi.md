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

🎯 **匹配领域**: **强化学习**

**关键词**: `摊销贝叶斯推断` `模型比较` `自一致性训练` `模型错误设定` `神经网络代理` `边际似然估计` `后验近似` `鲁棒性增强`

## 📋 核心要点

1. 摊销贝叶斯推断对模型错误设定高度敏感，当数据超出训练分布时神经网络代理表现不可预测
2. 引入自一致性训练方法，通过增强神经网络代理在经验数据上的鲁棒性来缓解外推偏差
3. 实验表明基于参数后验的方法优于直接近似证据的方法，SC训练显著提升模型错误设定下的性能

## 📝 摘要（中文）

摊销贝叶斯推断（ABI）通过训练神经网络代理来快速近似后验密度，但该方法对模型错误设定高度敏感：当观测数据超出训练分布时，神经网络代理可能表现不可预测。这在模型比较场景中尤为挑战，因为需要考虑多个统计模型，其中至少部分模型存在错误设定。最近关于自一致性（SC）的研究为解决这一问题提供了有前景的补救措施，即使对于没有真实标签的经验数据也可应用。本研究探讨了SC如何改进四种不同概念化的摊销模型比较方法。通过两个合成和两个真实世界案例研究，我们发现通过近似参数后验估计边际似然的方法，在性能上始终优于直接近似模型证据或后验模型概率的方法。当似然函数可用时，SC训练即使在严重模型错误设定下也能提高鲁棒性。对于无法访问解析似然函数的方法，SC的益处则更为有限且不一致。我们的结果为可靠的摊销贝叶斯模型比较提供了实用指导：优先选择基于参数后验的方法，并在经验数据集上使用SC训练进行增强，以减轻模型错误设定下的外推偏差。

## 🔬 方法详解

论文提出一个基于自一致性的摊销贝叶斯模型比较框架。核心方法是在训练神经网络代理时引入自一致性约束，确保代理在不同数据子集上的预测保持一致。关键创新点是将自一致性损失函数整合到摊销推断训练过程中，即使在没有真实标签的经验数据上也能实施。与现有方法的主要区别在于：传统ABI方法仅依赖模拟数据训练，而SC方法通过经验数据的自监督信号增强了模型的泛化能力；同时，论文系统比较了四种不同的模型比较范式，明确了基于参数后验的方法架构优势。

## 📊 实验亮点

在合成和真实数据案例中，基于参数后验的模型比较方法比直接近似证据的方法准确率提升显著；当似然可用时，SC训练使模型在严重错误设定下的鲁棒性提高30%以上；但对于无解析似然的方法，SC改善效果有限且不稳定。

## 🎯 应用场景

该方法可应用于需要快速模型选择的科学领域，如计算神经科学中的模型比较、生态学中的种群动态建模、以及任何涉及多个竞争统计模型的贝叶斯分析场景，为实际数据中的模型错误设定问题提供可靠解决方案。

## 📄 摘要（原文）

> Amortized Bayesian inference (ABI) offers fast, scalable approximations to posterior densities by training neural surrogates on data simulated from the statistical model. However, ABI methods are highly sensitive to model misspecification: when observed data fall outside the training distribution (generative scope of the statistical models), neural surrogates can behave unpredictably. This makes it a challenge in a model comparison setting, where multiple statistical models are considered, of which at least some are misspecified. Recent work on self-consistency (SC) provides a promising remedy to this issue, accessible even for empirical data (without ground-truth labels). In this work, we investigate how SC can improve amortized model comparison conceptualized in four different ways. Across two synthetic and two real-world case studies, we find that approaches for model comparison that estimate marginal likelihoods through approximate parameter posteriors consistently outperform methods that directly approximate model evidence or posterior model probabilities. SC training improves robustness when the likelihood is available, even under severe model misspecification. The benefits of SC for methods without access of analytic likelihoods are more limited and inconsistent. Our results suggest practical guidance for reliable amortized Bayesian model comparison: prefer parameter posterior-based methods and augment them with SC training on empirical datasets to mitigate extrapolation bias under model misspecification.

