---
layout: default
title: Muon is Provably Faster with Momentum Variance Reduction
---

# Muon is Provably Faster with Momentum Variance Reduction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16598" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16598v1</a>
  <a href="https://arxiv.org/pdf/2512.16598.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16598v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16598v1', 'Muon is Provably Faster with Momentum Variance Reduction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xun Qian, Hussein Rammal, Dmitry Kovalev, Peter Richtárik

**分类**: math.OC, cs.LG

**发布日期**: 2025-12-18

**备注**: 31 pages, 4 figures

---

## 💡 一句话要点

**提出动量方差减少的Muon优化器以提升深度学习性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度学习` `优化器` `动量方差减少` `非欧几里得优化` `收敛速度` `Gluon框架` `大型语言模型`

## 📋 核心要点

1. 现有的深度学习优化器在训练大型语言模型时，收敛速度和效率存在不足，尤其是传统的动量方法表现不佳。
2. 本文提出将动量方差减少（MVR）技术整合进Gluon框架，以提升优化器的收敛速度和性能，适用于多种非欧几里得优化方法。
3. 实验结果表明，整合MVR的优化器在迭代复杂度上显著优于传统方法，收敛速度从${	extcal O} (rac{1}{K^{1/4}})$提升至${	extcal O} (rac{1}{K^{1/3}})$。

## 📝 摘要（中文）

近期的实证研究表明，基于线性最小化oracle（LMO）并在特定非欧几里得范数球上优化的深度学习优化器，如Muon和Scion，在训练大型语言模型时优于Adam类方法。本文展示了通过将传统动量替换为动量方差减少（MVR），可以在理论上改进这些优化器的性能。我们将MVR整合进最近提出的Gluon框架，该框架能够捕捉Muon、Scion及其他特定的非欧几里得LMO方法，并在更一般的光滑性假设下工作，从而更好地反映神经网络的层级结构。在非凸情况下，我们以三种不同方式将MVR融入Gluon，均将收敛速度从${	extcal O} (rac{1}{K^{1/4}})$提升至${	extcal O} (rac{1}{K^{1/3}})$，并在星凸情况下提供了改进的收敛速率。最后，我们进行了多次数值实验，验证了所提算法在迭代复杂度方面的优越性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有深度学习优化器在训练大型语言模型时的收敛速度不足的问题，尤其是传统动量方法的局限性。

**核心思路**：通过将动量方差减少（MVR）技术引入Gluon框架，提升优化器的收敛性能，适应更复杂的非欧几里得空间。

**技术框架**：Gluon框架整合了Muon、Scion等多种优化方法，采用更一般的光滑性假设，分为三个主要模块：动量更新、方差减少和收敛分析。

**关键创新**：将MVR与Gluon框架结合，提供了理论上的收敛速率改进，尤其在非凸和星凸情况下表现突出，显著提升了优化器的效率。

**关键设计**：在设计中，采用了新的动量更新策略和损失函数，确保在不同的网络结构和参数设置下均能有效提升收敛速度。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16598v1/fig/MVR1gbs512.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16598v1/fig/MVR1gbs128.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16598v1/fig/MVR2gbs512.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，整合MVR的优化器在收敛速度上有显著提升，具体表现为收敛速率从${	extcal O} (rac{1}{K^{1/4}})$提升至${	extcal O} (rac{1}{K^{1/3}})$，并在星凸情况下也取得了更好的收敛性能，验证了所提方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等需要高效训练的深度学习任务。通过提升优化器的性能，能够加速模型训练过程，降低计算成本，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent empirical research has demonstrated that deep learning optimizers based on the linear minimization oracle (LMO) over specifically chosen Non-Euclidean norm balls, such as Muon and Scion, outperform Adam-type methods in the training of large language models. In this work, we show that such optimizers can be provably improved by replacing their vanilla momentum by momentum variance reduction (MVR). Instead of proposing and analyzing MVR variants of Muon and Scion separately, we incorporate MVR into the recently proposed Gluon framework, which captures Muon, Scion and other specific Non-Euclidean LMO-based methods as special cases, and at the same time works with a more general smoothness assumption which better captures the layer-wise structure of neural networks. In the non-convex case, we incorporate MVR into Gluon in three different ways. All of them improve the convergence rate from ${\cal O} (\frac{1}{K^{1/4}})$ to ${\cal O} (\frac{1}{K^{1/3}})$. Additionally, we provide improved rates in the star-convex case. Finally, we conduct several numerical experiments that verify the superior performance of our proposed algorithms in terms of iteration complexity.

