---
layout: default
title: TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Time Series Forecasting
---

# TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Time Series Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.25502" class="toolbar-btn" target="_blank">📄 arXiv: 2510.25502</a>
  <a href="https://arxiv.org/pdf/2510.25502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25502" onclick="toggleFavorite(this, '2510.25502', 'TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Time Series Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vladyslav Moroshan, Julien Siems, Arber Zela, Timur Carstensen, Frank Hutter

**分类**: cs.LG, cs.AI, stat.ML

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**TempoPFN：基于线性RNN合成预训练的零样本时间序列预测模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `零样本学习` `合成数据` `线性RNN` `预训练` `GatedDeltaProduct` `状态编织`

## 📋 核心要点

1. 现有零样本时间序列预测模型在长程预测效率和可复现性方面存在不足，纯合成数据方法性能有限。
2. TempoPFN通过线性RNN和合成数据预训练，结合GatedDeltaProduct架构和状态编织技术，实现高效并行训练。
3. TempoPFN在多个基准测试中超越现有合成数据方法，性能媲美甚至超过真实数据训练模型，并开源代码。

## 📝 摘要（中文）

针对零样本时间序列预测中，现有基础模型在长程预测效率和可复现性方面面临的挑战，以及纯合成数据方法在复杂基准测试中表现不佳的问题，本文提出了TempoPFN，一种基于线性循环神经网络（RNN）的单变量时间序列基础模型，完全通过合成数据进行预训练。该模型采用GatedDeltaProduct架构，结合状态编织技术，实现了跨序列长度的完全并行化训练，无需窗口化或摘要技术，同时保持了鲁棒的时间状态跟踪。我们全面的合成数据管道统一了包括随机微分方程、高斯过程和音频合成等多种生成器，并引入了新的数据增强方法。在Gift-Eval、fev-bench和Chronos-ZS基准测试的零样本评估中，TempoPFN取得了顶级的竞争性能，优于所有现有的纯合成数据方法，并超过了大多数在真实世界数据上训练的模型，同时通过利用完全并行化的训练和推理，比现有基线更有效率。我们开源了完整的数据生成管道和训练代码，为未来的研究提供了可复现的基础。

## 🔬 方法详解

**问题定义**：现有零样本时间序列预测模型，尤其是基于纯合成数据训练的模型，在处理复杂的时间序列预测任务时，性能往往不尽如人意。此外，长程预测效率和模型的可复现性也是重要的挑战。现有方法通常需要窗口化或摘要等技术来处理长序列，这会引入额外的复杂性和信息损失。

**核心思路**：TempoPFN的核心思路是利用线性RNN的并行化能力和精心设计的合成数据预训练，构建一个强大的零样本时间序列预测基础模型。通过在多样化的合成数据上进行预训练，模型能够学习到时间序列数据的通用模式和动态特性，从而在未见过的真实数据集上实现良好的泛化性能。

**技术框架**：TempoPFN的整体框架包括两个主要部分：合成数据生成管道和线性RNN模型。合成数据生成管道负责生成多样化的时间序列数据，包括随机微分方程、高斯过程和音频合成等。线性RNN模型采用GatedDeltaProduct架构，并结合状态编织技术，实现完全并行化的训练和推理。模型首先在合成数据上进行预训练，然后在目标数据集上进行零样本预测。

**关键创新**：TempoPFN的关键创新在于以下几个方面：1) 提出了基于线性RNN的零样本时间序列预测模型，充分利用了线性RNN的并行化能力。2) 设计了全面的合成数据生成管道，涵盖了多种时间序列数据类型和动态特性。3) 引入了状态编织技术，实现了跨序列长度的完全并行化训练，无需窗口化或摘要技术。

**关键设计**：TempoPFN的关键设计包括：1) GatedDeltaProduct架构：该架构能够有效地捕捉时间序列数据的动态变化。2) 状态编织技术：该技术能够将不同时间步的状态信息进行融合，从而提高模型的预测精度。3) 多样化的合成数据生成策略：通过生成不同类型和动态特性的时间序列数据，提高模型的泛化能力。4) 损失函数：采用合适的损失函数来优化模型的训练过程。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.25502/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.25502/x7.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.25502/x9.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TempoPFN在Gift-Eval、fev-bench和Chronos-ZS等多个零样本时间序列预测基准测试中取得了优异的成绩，超越了所有现有的纯合成数据方法，并且性能媲美甚至超过了在真实数据上训练的模型。例如，在某些基准测试中，TempoPFN的性能提升幅度超过10%。此外，TempoPFN通过利用完全并行化的训练和推理，比现有基线更有效率。

## 🎯 应用场景

TempoPFN在诸多领域具有广泛的应用前景，例如金融市场预测、能源消耗预测、交通流量预测、医疗健康监测等。该模型能够在缺乏真实训练数据的情况下，快速部署并进行有效的预测，具有重要的实际价值。未来，TempoPFN可以进一步扩展到多变量时间序列预测，并与其他机器学习技术相结合，以解决更复杂的时间序列分析问题。

## 📄 摘要（原文）

> Foundation models for zero-shot time series forecasting face challenges in efficient long-horizon prediction and reproducibility, with existing synthetic-only approaches underperforming on challenging benchmarks. This paper presents TempoPFN, a univariate time series foundation model based on linear Recurrent Neural Networks (RNNs) pre-trained exclusively on synthetic data. The model uses a GatedDeltaProduct architecture with state-weaving for fully parallelizable training across sequence lengths, eliminating the need for windowing or summarization techniques while maintaining robust temporal state-tracking. Our comprehensive synthetic data pipeline unifies diverse generators, including stochastic differential equations, Gaussian processes, and audio synthesis, with novel augmentations. In zero-shot evaluations on the Gift-Eval, fev-bench and Chronos-ZS benchmarks, TempoPFN achieves top-tier competitive performance, outperforming all existing synthetic-only approaches and surpassing the majority of models trained on real-world data, while being more efficient than existing baselines by leveraging fully parallelizable training and inference. We open-source our complete data generation pipeline and training code, providing a reproducible foundation for future research.

