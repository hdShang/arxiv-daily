---
layout: default
title: Generalisation Bounds of Zero-Shot Economic Forecasting using Time Series Foundation Models
---

# Generalisation Bounds of Zero-Shot Economic Forecasting using Time Series Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15705" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15705v2</a>
  <a href="https://arxiv.org/pdf/2506.15705.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15705v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15705v2', 'Generalisation Bounds of Zero-Shot Economic Forecasting using Time Series Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jittarin Jetwiriyanon, Teo Susnjak, Surangika Ranathunga

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-08-02)

**DOI**: [10.3390/make7040135](https://doi.org/10.3390/make7040135)

---

## 💡 一句话要点

**提出时间序列基础模型进行零-shot经济预测以解决数据稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `零-shot学习` `宏观经济` `模型评估` `数据稀缺`

## 📋 核心要点

1. 现有的经济预测方法依赖于大量的训练数据和定制模型，限制了其在数据稀缺情况下的应用。
2. 本研究提出使用时间序列基础模型（TSFMs）进行零-shot预测，旨在简化经济指标的预测过程。
3. 实验结果显示，TSFMs在稳定经济条件下的预测性能与传统多变量模型相当，但在快速经济冲击时表现较差。

## 📝 摘要（中文）

本研究探讨了时间序列基础模型（TSFMs）在宏观经济指标零-shot预测能力。我们在单变量条件下应用TSFMs进行经济指标预测，避免了使用大量训练数据集训练定制计量经济模型的需求。通过对三种最先进的TSFMs（Chronos、TimeGPT和Moirai）进行严格的回测，结果表明，适当设计的TSFMs能够内化丰富的经济动态，适应制度转变，并在没有额外定制的情况下提供良好的不确定性估计。研究发现，在稳定经济条件下，TSFMs的表现可以与经典模型相匹配或超越，但在快速冲击期间表现可能会下降。这些发现为实践者提供了关于何时进行零-shot部署以进行宏观经济监测和战略规划的指导。

## 🔬 方法详解

**问题定义**：本研究旨在解决在数据稀缺情况下，传统经济预测模型的依赖性和局限性。现有方法通常需要大量的历史数据和复杂的模型定制，难以快速适应经济变化。

**核心思路**：论文提出利用时间序列基础模型（TSFMs）进行零-shot经济预测，旨在通过内化经济动态来简化预测过程，避免繁琐的模型训练和数据准备。

**技术框架**：研究中采用了三种最先进的TSFMs（Chronos、TimeGPT和Moirai），在无额外定制的情况下进行回测。整体流程包括数据预处理、模型应用和结果评估三个主要阶段。

**关键创新**：最重要的技术创新在于TSFMs能够在没有任何微调的情况下，直接应用于宏观经济指标的预测，展现出与经典模型相当的性能。与现有方法的本质区别在于其对数据的依赖性大幅降低。

**关键设计**：模型的关键设计包括选择适当的时间序列特征、损失函数的设置以及模型架构的优化，确保在数据稀缺和结构性变化的情况下，仍能提供可靠的预测结果。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，经过严格回测的TSFMs在稳定经济条件下的预测性能与传统多变量模型相当，甚至在某些情况下超越了经典模型。然而，在快速经济冲击期间，TSFMs的表现有所下降，显示出其在应对突发事件时的脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括宏观经济监测、政策制定和战略规划等。通过简化经济预测过程，TSFMs可以帮助决策者在数据稀缺的情况下快速获取经济动态信息，从而提高响应速度和决策质量。未来，随着模型的进一步优化和推广，可能会在更多经济领域得到应用。

## 📄 摘要（原文）

> This study investigates zero-shot forecasting capabilities of Time Series Foundation Models (TSFMs) for macroeconomic indicators. We apply TSFMs to forecasting economic indicators under univariate conditions, bypassing the need for train bespoke econometric models using and extensive training datasets. Our experiments were conducted on a case study dataset, without additional customisation. We rigorously back-tested three state-of-the-art TSFMs (Chronos, TimeGPT and Moirai) under data-scarce conditions and structural breaks. Our results demonstrate that appropriately engineered TSFMs can internalise rich economic dynamics, accommodate regime shifts, and deliver well-behaved uncertainty estimates out of the box, while matching state-of-the-art multivariate models on this domain. Our findings suggest that, without any fine-tuning, TSFMs can match or exceed classical models during stable economic conditions. However, they are vulnerable to degradation in performances during periods of rapid shocks. The findings offer guidance to practitioners on when zero-shot deployments are viable for macroeconomic monitoring and strategic planning.

