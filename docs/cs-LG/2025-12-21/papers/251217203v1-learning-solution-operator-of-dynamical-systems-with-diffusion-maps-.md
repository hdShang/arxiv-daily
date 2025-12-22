---
layout: default
title: Learning solution operator of dynamical systems with diffusion maps kernel ridge regression
---

# Learning solution operator of dynamical systems with diffusion maps kernel ridge regression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17203" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17203v1</a>
  <a href="https://arxiv.org/pdf/2512.17203.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17203v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17203v1', 'Learning solution operator of dynamical systems with diffusion maps kernel ridge regression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiwoo Song, Daning Huang, John Harlim

**分类**: cs.LG, math.NA

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出基于扩散映射核岭回归(DM-KRR)的动力系统解算子学习方法，提升长期预测精度。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `动力系统` `解算子学习` `扩散映射` `核岭回归` `长期预测` `数据驱动` `几何结构`

## 📋 核心要点

1. 现有数据驱动模型在长期预测复杂动力系统时，由于未能有效捕捉系统内在几何结构，性能易下降。
2. 提出DM-KRR方法，利用扩散映射自适应系统不变集的几何结构，无需显式流形重建或吸引子建模。
3. 实验表明，DM-KRR在多种系统上优于现有随机特征、神经网络和算子学习方法，提升了预测精度和数据效率。

## 📝 摘要（中文）

许多科学和工程系统表现出复杂的非线性动力学，难以进行准确的长期预测。尽管数据驱动模型显示出潜力，但当控制长期行为的几何结构未知或表示不佳时，它们的性能通常会下降。本文证明，一个简单的核岭回归（KRR）框架，当与动态感知验证策略相结合时，为复杂动力系统的长期预测提供了一个强大的基线。通过采用从扩散映射导出的数据驱动核，所提出的扩散映射核岭回归（DM-KRR）方法隐式地适应系统不变集的内在几何结构，而无需显式流形重建或吸引子建模，这些过程通常限制预测性能。在包括光滑流形、混沌吸引子和高维时空流在内的广泛系统中，DM-KRR在准确性和数据效率方面始终优于最先进的随机特征、神经网络和算子学习方法。这些发现强调，长期预测能力不仅取决于模型的表达能力，而且关键在于通过动态一致的模型选择来尊重数据中编码的几何约束。总之，简单性、几何感知和强大的经验性能为可靠和高效地学习复杂动力系统指明了一条有希望的道路。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂动力系统长期预测精度低的问题。现有方法，如神经网络和算子学习，在处理具有复杂几何结构的动力系统时，往往难以捕捉到系统内在的几何约束，导致长期预测性能下降。这些方法通常需要大量的训练数据，并且对超参数的选择非常敏感。

**核心思路**：论文的核心思路是利用扩散映射（Diffusion Maps）来学习动力系统的内在几何结构，并将其融入到核岭回归（Kernel Ridge Regression, KRR）框架中。扩散映射能够有效地提取数据中的低维流形结构，从而使模型能够更好地适应系统的动态特性。通过这种方式，模型可以在不需要显式地进行流形重建或吸引子建模的情况下，实现对复杂动力系统的长期预测。

**技术框架**：DM-KRR方法主要包含以下几个阶段：1) 数据收集：从动力系统中采样得到训练数据。2) 扩散映射：利用扩散映射算法，从训练数据中学习得到一个数据驱动的核函数，该核函数能够反映系统内在的几何结构。3) 核岭回归：使用学习到的核函数，构建一个核岭回归模型，用于预测系统的未来状态。4) 动态感知验证：采用一种动态感知的验证策略，选择最优的模型参数，以保证模型在长期预测中的稳定性。

**关键创新**：DM-KRR的关键创新在于将扩散映射与核岭回归相结合，从而使模型能够自适应地学习动力系统的内在几何结构。与传统的核方法相比，DM-KRR的核函数是数据驱动的，能够更好地适应系统的动态特性。与神经网络等深度学习方法相比，DM-KRR具有更高的数据效率和更强的可解释性。

**关键设计**：扩散映射核的选择是关键。论文可能采用了基于扩散距离的核函数，例如高斯核。岭回归中的正则化参数需要仔细调整，以防止过拟合。动态感知验证策略可能涉及到对不同参数组合下的模型进行长期预测，并选择在验证集上表现最好的参数组合。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17203v1/pics/torus/torus_test_rmse_small.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17203v1/pics/lorenz/combined_lorenz_ks_small.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17203v1/pics/ks-travelling/ks_travelling_prediction_results_small.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DM-KRR在包括光滑流形、混沌吸引子和高维时空流在内的多个动力系统上进行了测试，实验结果表明，DM-KRR在预测精度和数据效率方面均优于现有的随机特征、神经网络和算子学习方法。具体性能提升数据未知，但摘要强调了“consistently outperforms state-of-the-art”和“accuracy and data efficiency”。

## 🎯 应用场景

该研究成果可应用于各种科学和工程领域，例如气候预测、流体动力学、机器人控制和金融建模等。通过提高复杂动力系统的长期预测精度，可以为决策提供更可靠的依据，并促进相关领域的发展。例如，在气候预测中，可以更准确地预测极端天气事件的发生；在机器人控制中，可以实现更稳定和高效的运动规划。

## 📄 摘要（原文）

> Many scientific and engineering systems exhibit complex nonlinear dynamics that are difficult to predict accurately over long time horizons. Although data-driven models have shown promise, their performance often deteriorates when the geometric structures governing long-term behavior are unknown or poorly represented. We demonstrate that a simple kernel ridge regression (KRR) framework, when combined with a dynamics-aware validation strategy, provides a strong baseline for long-term prediction of complex dynamical systems. By employing a data-driven kernel derived from diffusion maps, the proposed Diffusion Maps Kernel Ridge Regression (DM-KRR) method implicitly adapts to the intrinsic geometry of the system's invariant set, without requiring explicit manifold reconstruction or attractor modeling, procedures that often limit predictive performance. Across a broad range of systems, including smooth manifolds, chaotic attractors, and high-dimensional spatiotemporal flows, DM-KRR consistently outperforms state-of-the-art random feature, neural-network and operator-learning methods in both accuracy and data efficiency. These findings underscore that long-term predictive skill depends not only on model expressiveness, but critically on respecting the geometric constraints encoded in the data through dynamically consistent model selection. Together, simplicity, geometry awareness, and strong empirical performance point to a promising path for reliable and efficient learning of complex dynamical systems.

