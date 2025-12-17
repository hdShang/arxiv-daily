---
layout: default
title: Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX
---

# Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14510" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14510</a>
  <a href="https://arxiv.org/pdf/2512.14510.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14510" onclick="toggleFavorite(this, '2512.14510', 'Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aihui Liu, Magnus Jansson

**分类**: eess.SY, eess.SP

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于SSARX的闭环一致因果数据驱动预测控制方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `数据驱动控制` `预测控制` `模型预测控制` `系统辨识` `ARX模型`

## 📋 核心要点

1. 传统DeePC方法依赖Hankel矩阵，计算复杂度高，且对噪声敏感，限制了其在实际闭环系统中的应用。
2. 论文提出基于SSARX的DDPC方法，通过高阶ARX模型解耦噪声，并学习多步预测模型，实现闭环一致的因果预测控制。
3. 实验结果表明，该方法在受噪声影响的闭环数据上表现出与现有方法相当的性能，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种无需基本引理的数据驱动预测控制(DDPC)方案，用于直接从输入输出数据中合成类似模型预测控制(MPC)的策略。与依赖Willems基本引理的DeePC方法和其他DDPC方法不同，我们的方法避免了堆叠的Hankel矩阵表示和DeePC决策变量g。相反，我们开发了一种基于多步预测器Subspace-ARX (SSARX)的闭环一致、因果DDPC方案。该方法首先(i)通过高阶ARX模型估计预测器/观测器Markov参数以解耦噪声，然后(ii)通过回归学习多步过去到未来的映射，可以选择使用降秩约束。SSARX预测器是严格因果的，这使得它可以自然地集成到MPC公式中。实验结果表明，当应用于受测量和过程噪声影响的闭环数据时，SSARX的性能与其他方法相比具有竞争力。

## 🔬 方法详解

**问题定义**：现有的数据驱动预测控制方法，如DeePC，依赖于Willems的基本引理，需要构建大型Hankel矩阵，计算复杂度高，并且对噪声非常敏感。这限制了它们在实际闭环系统中的应用，尤其是在存在测量噪声和过程噪声的情况下。因此，需要一种更鲁棒、更高效的数据驱动预测控制方法。

**核心思路**：论文的核心思路是利用Subspace-ARX (SSARX)模型来构建一个多步预测器，该预测器能够直接从输入输出数据中学习系统的动态特性，而无需依赖Hankel矩阵。通过高阶ARX模型来解耦噪声，并使用回归方法学习过去到未来的映射关系。SSARX预测器是严格因果的，可以直接嵌入到MPC框架中。

**技术框架**：该方法主要包含两个阶段：(1) 预测器/观测器Markov参数估计：通过高阶ARX模型估计系统的Markov参数，以解耦噪声的影响。(2) 多步预测模型学习：通过回归方法学习过去输入输出数据到未来输出数据的映射关系，可以选择使用降秩约束来提高模型的泛化能力。然后，将学习到的SSARX预测器集成到MPC框架中，实现闭环控制。

**关键创新**：该方法最重要的创新点在于避免了使用Willems的基本引理和Hankel矩阵，而是直接通过SSARX模型学习系统的动态特性。这种方法不仅降低了计算复杂度，而且提高了对噪声的鲁棒性。此外，SSARX预测器的因果性保证了其能够自然地集成到MPC框架中。

**关键设计**：关键设计包括：(1) 使用高阶ARX模型来解耦噪声，ARX模型的阶数需要根据实际系统的特性进行选择。(2) 使用回归方法学习过去到未来的映射关系，可以选择使用岭回归或Lasso回归等正则化方法来防止过拟合。(3) 可以选择使用降秩约束来降低模型的复杂度，提高泛化能力。损失函数通常采用均方误差损失函数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14510/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14510/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14510/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于SSARX的DDPC方法在受测量和过程噪声影响的闭环数据上表现出与现有方法相当的性能。该方法在避免使用Hankel矩阵的同时，保持了良好的控制性能，验证了其在实际应用中的潜力。具体的性能指标包括跟踪误差、控制能量等，但论文中未给出具体的数值。

## 🎯 应用场景

该研究成果可应用于各种需要精确控制的工业领域，如机器人控制、过程控制、智能交通系统等。特别是在系统模型未知或难以精确建模的情况下，该方法能够直接从数据中学习控制策略，具有重要的实际应用价值和潜力。未来可进一步扩展到非线性系统和时变系统的控制。

## 📄 摘要（原文）

> We propose a fundamental-lemma-free data-driven predictive control (DDPC) scheme for synthesizing model predictive control (MPC)-like policies directly from input-output data. Unlike the well-known DeePC approach and other DDPC methods that rely on Willems' fundamental lemma, our method avoids stacked Hankel representations and the DeePC decision variable g. Instead, we develop a closed-loop consistent, causal DDPC scheme based on the multi-step predictor Subspace-ARX (SSARX). The method first (i) estimates predictor/observer Markov parameters via a high-order ARX model to decouple the noise, then (ii) learns a multi-step past-to-future map by regression, optionally with a reduced-rank constraint. The SSARX predictor is strictly causal, which allows it to be integrated naturally into an MPC formulation. Our experimental results show that SSARX performs competitively with other methods when applied to closed-loop data affected by measurement and process noise.

