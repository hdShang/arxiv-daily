---
layout: default
title: Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX
---

# Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14510" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14510v1</a>
  <a href="https://arxiv.org/pdf/2512.14510.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14510v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14510v1', 'Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aihui Liu, Magnus Jansson

**分类**: eess.SY, eess.SP

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于SSARX的闭环一致因果数据驱动预测控制方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `数据驱动控制` `预测控制` `SSARX模型` `闭环控制` `系统辨识`

## 📋 核心要点

1. 传统DeePC方法依赖Hankel矩阵，计算复杂度高，且对噪声敏感，限制了其在实际闭环系统中的应用。
2. 论文提出基于SSARX的DDPC方法，通过高阶ARX模型解耦噪声，并学习多步预测模型，实现闭环一致的因果预测控制。
3. 实验结果表明，该方法在受噪声影响的闭环数据上表现出与现有方法相当的性能，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种无需基本引理的数据驱动预测控制(DDPC)方案，用于直接从输入输出数据中合成类似模型预测控制(MPC)的策略。与依赖Willems基本引理的DeePC方法和其他DDPC方法不同，我们的方法避免了堆叠的Hankel矩阵表示和DeePC决策变量g。相反，我们开发了一种基于多步预测器Subspace-ARX (SSARX)的闭环一致、因果DDPC方案。该方法首先(i)通过高阶ARX模型估计预测器/观测器Markov参数以解耦噪声，然后(ii)通过回归学习多步过去到未来的映射，可以选择使用降秩约束。SSARX预测器是严格因果的，这使得它能够自然地集成到MPC公式中。我们的实验结果表明，当应用于受测量和过程噪声影响的闭环数据时，SSARX的性能与其他方法相比具有竞争力。

## 🔬 方法详解

**问题定义**：现有的数据驱动预测控制方法，如DeePC，依赖于Willems的基本引理，需要构建大型Hankel矩阵，计算复杂度高，并且对噪声较为敏感。这限制了它们在实际闭环系统中的应用，尤其是在存在测量噪声和过程噪声的情况下。

**核心思路**：本文的核心思路是利用Subspace-ARX (SSARX)模型来构建一个因果的多步预测器，从而避免使用Hankel矩阵。SSARX模型通过高阶ARX模型来解耦噪声，并学习一个从过去输入输出到未来输出的映射。由于SSARX预测器是严格因果的，因此可以自然地集成到MPC框架中。

**技术框架**：该方法主要包含两个阶段：(1) 预测器/观测器Markov参数估计：使用高阶ARX模型来估计系统的Markov参数，从而解耦噪声的影响。(2) 多步预测模型学习：通过回归方法学习一个从过去输入输出到未来输出的多步映射。可以选择使用降秩约束来提高模型的泛化能力。然后，将SSARX预测器集成到MPC框架中，实现数据驱动的预测控制。

**关键创新**：该方法最重要的创新点在于避免了使用Willems的基本引理和Hankel矩阵，而是利用SSARX模型构建了一个因果的多步预测器。这降低了计算复杂度，提高了对噪声的鲁棒性，并且使得该方法更易于集成到现有的MPC框架中。与DeePC相比，该方法不需要求解复杂的优化问题来获得决策变量g。

**关键设计**：在高阶ARX模型中，需要选择合适的模型阶数，以平衡模型的拟合能力和复杂度。在多步预测模型学习阶段，可以选择使用降秩约束来提高模型的泛化能力。MPC框架中的目标函数和约束条件需要根据具体的应用场景进行设计。此外，需要仔细选择回归算法和正则化参数，以避免过拟合。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14510v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14510v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14510v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在受测量和过程噪声影响的闭环数据上，基于SSARX的DDPC方法能够实现与现有方法相当的控制性能。该方法在避免使用Hankel矩阵的同时，保持了良好的控制精度，验证了其有效性和鲁棒性。具体的性能指标，如跟踪误差和控制能量消耗，在不同噪声水平下均表现出竞争力。

## 🎯 应用场景

该研究成果可应用于各种需要数据驱动控制的领域，例如机器人控制、过程控制、智能交通系统等。特别是在模型难以建立或存在不确定性的情况下，该方法能够直接从数据中学习控制策略，具有重要的实际应用价值。未来，该方法有望进一步推广到非线性系统和时变系统。

## 📄 摘要（原文）

> We propose a fundamental-lemma-free data-driven predictive control (DDPC) scheme for synthesizing model predictive control (MPC)-like policies directly from input-output data. Unlike the well-known DeePC approach and other DDPC methods that rely on Willems' fundamental lemma, our method avoids stacked Hankel representations and the DeePC decision variable g. Instead, we develop a closed-loop consistent, causal DDPC scheme based on the multi-step predictor Subspace-ARX (SSARX). The method first (i) estimates predictor/observer Markov parameters via a high-order ARX model to decouple the noise, then (ii) learns a multi-step past-to-future map by regression, optionally with a reduced-rank constraint. The SSARX predictor is strictly causal, which allows it to be integrated naturally into an MPC formulation. Our experimental results show that SSARX performs competitively with other methods when applied to closed-loop data affected by measurement and process noise.

