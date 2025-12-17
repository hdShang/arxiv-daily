---
layout: default
title: Maximum Mean Discrepancy with Unequal Sample Sizes via Generalized U-Statistics
---

# Maximum Mean Discrepancy with Unequal Sample Sizes via Generalized U-Statistics

**arXiv**: [2512.13997v1](https://arxiv.org/abs/2512.13997) | [PDF](https://arxiv.org/pdf/2512.13997.pdf)

**作者**: Aaron Wei, Milad Jalali, Danica J. Sutherland

**分类**: stat.ML, cs.LG, math.ST, stat.ME

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于广义U统计量的最大均值差异方法，解决不等样本量下的两样本检验问题**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `最大均值差异` `两样本检验` `不等样本量` `广义U统计量` `渐近分布` `检验功效优化` `统计学习理论`

## 📋 核心要点

1. 现有MMD两样本检验方法通常假设等样本量，实际应用中需丢弃数据，降低检验功效
2. 通过扩展广义U统计量理论，重新刻画不等样本量下MMD估计量的渐近分布
3. 提出新准则优化不等样本量检验功效，保留所有数据，提升实际应用中的准确性和适用性

## 📝 摘要（中文）

现有的两样本检验技术，特别是基于选择核函数的最大均值差异方法，通常假设两个分布具有相等的样本量。在实际应用中，这些方法可能需要丢弃有价值的数据，不必要地降低检验功效。我们通过扩展广义U统计量理论并将其应用于通常的MMD估计量，解决了这一长期存在的限制，从而对不等样本量下MMD估计量的渐近分布进行了新的刻画（特别是在先前部分结果所需的比例范围之外）。这一推广还为优化不等样本量下MMD检验的功效提供了新的准则。我们的方法保留了所有可用数据，提高了实际场景中的检验准确性和适用性。在此过程中，我们对MMD估计量的方差给出了更清晰的刻画，揭示了一个可能令该领域研究者惊讶的现象：虽然零MMD意味着退化估计量，但有时也可能存在非零MMD的退化估计量；我们给出了一个构造，并证明这在常见情况下不会发生。

## 🔬 方法详解

论文的核心方法基于广义U统计量理论对最大均值差异进行扩展。整体框架是将传统的MMD估计量重新表述为广义U统计量，从而处理不等样本量的情况。关键技术创新点包括：推导了不等样本量下MMD估计量的渐近分布理论，特别是在非比例样本量下的完整刻画；提出了基于该理论的新检验功效优化准则。与现有方法的主要区别在于：不再需要丢弃数据或假设等样本量，能够充分利用所有可用样本；提供了更一般的理论框架，覆盖了先前部分结果未涉及的非比例样本量情况。

## 📊 实验亮点

论文最重要的实验结果包括：在不等样本量下，新方法相比传统丢弃数据的方法显著提高了检验功效；理论分析揭示了MMD估计量方差的新性质，包括非零MMD下可能存在的退化情况；实验验证了新优化准则的有效性。

## 🎯 应用场景

该方法在需要处理不等样本量的两样本检验场景中具有重要价值，如医学研究中的病例-对照研究、机器学习中的领域适应、异常检测等。实际应用中能够避免数据浪费，提高统计检验的准确性和可靠性。

## 📄 摘要（原文）

> Existing two-sample testing techniques, particularly those based on choosing a kernel for the Maximum Mean Discrepancy (MMD), often assume equal sample sizes from the two distributions. Applying these methods in practice can require discarding valuable data, unnecessarily reducing test power. We address this long-standing limitation by extending the theory of generalized U-statistics and applying it to the usual MMD estimator, resulting in new characterization of the asymptotic distributions of the MMD estimator with unequal sample sizes (particularly outside the proportional regimes required by previous partial results). This generalization also provides a new criterion for optimizing the power of an MMD test with unequal sample sizes. Our approach preserves all available data, enhancing test accuracy and applicability in realistic settings. Along the way, we give much cleaner characterizations of the variance of MMD estimators, revealing something that might be surprising to those in the area: while zero MMD implies a degenerate estimator, it is sometimes possible to have a degenerate estimator with nonzero MMD as well; we give a construction and a proof that it does not happen in common situations.

