---
layout: default
title: Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX
---

# Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14510" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14510v1</a>
  <a href="https://arxiv.org/pdf/2512.14510.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14510v1" onclick="toggleFavorite(this, '2512.14510v1', 'Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aihui Liu, Magnus Jansson

**分类**: eess.SY, eess.SP

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出一种基于SSARX的闭环一致因果数据驱动预测控制方法，无需Fundamental Lemma。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `数据驱动控制` `预测控制` `SSARX模型` `系统辨识` `闭环控制`

## 📋 核心要点

1. 传统DeePC依赖Fundamental Lemma，计算复杂度高，且对噪声敏感。
2. 提出基于SSARX的DDPC方法，避免Hankel矩阵和决策变量g，实现闭环一致和因果性。
3. 实验表明，在受噪声影响的闭环数据上，SSARX方法性能与其他方法相当，具有竞争力。

## 📝 摘要（中文）

本文提出了一种数据驱动预测控制(DDPC)方案，用于直接从输入-输出数据中合成类似模型预测控制(MPC)的策略，该方案无需Fundamental Lemma。与依赖Willems' Fundamental Lemma的DeePC方法和其他DDPC方法不同，我们的方法避免了堆叠的Hankel矩阵表示和DeePC决策变量g。相反，我们开发了一种基于多步预测器Subspace-ARX (SSARX)的闭环一致、因果DDPC方案。该方法首先(i)通过高阶ARX模型估计预测器/观测器Markov参数以解耦噪声，然后(ii)通过回归学习多步过去到未来的映射，可以选择使用降秩约束。SSARX预测器是严格因果的，这使得它可以自然地集成到MPC公式中。实验结果表明，当应用于受测量和过程噪声影响的闭环数据时，SSARX的性能与其他方法相比具有竞争力。

## 🔬 方法详解

**问题定义**：传统的数据驱动预测控制方法，如DeePC，依赖于Willems的Fundamental Lemma，需要构建庞大的Hankel矩阵，计算复杂度高，并且对噪声较为敏感。这限制了其在实际工业场景中的应用，尤其是在数据质量不高的情况下。

**核心思路**：本文的核心思路是利用Subspace-ARX (SSARX)模型来构建一个多步预测器，该预测器能够直接从过去的输入输出数据预测未来的输出。通过这种方式，避免了对Fundamental Lemma的依赖，降低了计算复杂度，并提高了对噪声的鲁棒性。SSARX预测器的因果性保证了其能够自然地融入到MPC框架中。

**技术框架**：该方法主要包含两个阶段：(1) 预测器/观测器Markov参数估计：利用高阶ARX模型解耦噪声，估计系统的Markov参数。(2) 多步过去到未来映射学习：通过回归方法学习从过去输入输出到未来输出的映射关系，可以选择使用降秩约束来提高模型的泛化能力。然后，将学习到的SSARX预测器集成到MPC框架中，实现数据驱动的预测控制。

**关键创新**：该方法最重要的创新点在于提出了一个无需Fundamental Lemma的数据驱动预测控制框架。通过使用SSARX模型，避免了Hankel矩阵的构建，降低了计算复杂度，提高了对噪声的鲁棒性。此外，SSARX预测器的因果性保证了其能够自然地融入到MPC框架中，简化了控制器的设计。

**关键设计**：在高阶ARX模型中，需要选择合适的模型阶数以平衡模型的拟合能力和复杂度。在多步过去到未来映射学习中，可以选择使用降秩约束来提高模型的泛化能力，避免过拟合。MPC框架中，需要合理设置控制目标、约束条件和权重系数，以实现期望的控制性能。

## 📊 实验亮点

实验结果表明，在受测量和过程噪声影响的闭环数据上，基于SSARX的DDPC方法能够取得与现有方法相当的性能。这验证了该方法在实际应用中的可行性和竞争力，尤其是在数据质量不高的情况下，该方法具有一定的优势。

## 🎯 应用场景

该研究成果可应用于各种工业控制场景，如过程控制、机器人控制、智能交通系统等。尤其适用于难以建立精确数学模型的复杂系统，以及数据驱动的控制策略。该方法降低了对系统先验知识的依赖，提高了控制系统的自适应性和鲁棒性，具有重要的实际应用价值和潜在的未来影响。

## 📄 摘要（原文）

> We propose a fundamental-lemma-free data-driven predictive control (DDPC) scheme for synthesizing model predictive control (MPC)-like policies directly from input-output data. Unlike the well-known DeePC approach and other DDPC methods that rely on Willems' fundamental lemma, our method avoids stacked Hankel representations and the DeePC decision variable g. Instead, we develop a closed-loop consistent, causal DDPC scheme based on the multi-step predictor Subspace-ARX (SSARX). The method first (i) estimates predictor/observer Markov parameters via a high-order ARX model to decouple the noise, then (ii) learns a multi-step past-to-future map by regression, optionally with a reduced-rank constraint. The SSARX predictor is strictly causal, which allows it to be integrated naturally into an MPC formulation. Our experimental results show that SSARX performs competitively with other methods when applied to closed-loop data affected by measurement and process noise.

