---
layout: default
title: FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting
---

# FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14253" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14253</a>
  <a href="https://arxiv.org/pdf/2512.14253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14253" onclick="toggleFavorite(this, '2512.14253', 'FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingjian Wu, Hanyin Cheng, Xiangfei Qiu, Zhengyu Li, Jilin Hu, Chenjuan Guo, Bin Yang

**分类**: cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**FLAME：用于通用时间序列预测的流增强勒让德记忆模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `勒让德记忆` `归一化流` `零样本学习` `概率预测` `基础模型`

## 📋 核心要点

1. 现有时间序列预测模型在效率和鲁棒性方面存在挑战，尤其是在处理长程依赖和复杂分布时。
2. FLAME通过引入平移和缩放勒让德记忆，有效捕获数据中的归纳偏置，并利用归一化流建模预测分布。
3. 在TSFM-Bench和ProbTS等基准测试中，FLAME在确定性和概率性预测任务上均取得了领先的零样本性能。

## 📝 摘要（中文）

本文提出FLAME，一种极其轻量且强大的时间序列基础模型家族，它通过生成概率建模支持确定性和概率性预测，从而确保效率和鲁棒性。FLAME利用勒让德记忆来实现强大的泛化能力。通过在编码和解码阶段调整勒让德记忆的变体，即平移勒让德（LegT）和缩放勒让德（LegS），FLAME可以有效地捕获数据中固有的归纳偏置，并进行高效的远程推理。为了在保持效率的同时提高概率预测的准确性，FLAME采用基于归一化流的预测头，该预测头可以以生成方式对预测范围内任意复杂的分布进行建模。在包括TSFM-Bench和ProbTS在内的公认基准上的综合实验表明，FLAME在确定性和概率性预测任务上均具有一致的最先进的零样本性能。

## 🔬 方法详解

**问题定义**：时间序列预测旨在根据历史数据预测未来的时间序列值。现有方法在处理长程依赖、捕捉复杂分布以及实现高效的零样本泛化方面存在挑战。尤其是在概率预测中，如何准确建模预测范围内的任意复杂分布是一个难点。

**核心思路**：FLAME的核心思路是利用勒让德多项式的正交性和完备性，构建具有强大泛化能力的记忆模块。通过调整勒让德记忆的变体（平移和缩放），可以更好地适应不同时间序列数据的特性，从而捕获数据中的归纳偏置。此外，使用基于归一化流的预测头，可以灵活地建模任意复杂的预测分布。

**技术框架**：FLAME的整体框架包括编码器、解码器和预测头三个主要模块。编码器使用平移勒让德记忆（LegT）来提取输入时间序列的特征。解码器使用缩放勒让德记忆（LegS）来生成预测序列。预测头则使用归一化流来建模预测分布，从而实现概率预测。

**关键创新**：FLAME的关键创新在于以下几点：1) 提出了一种基于勒让德记忆的时间序列基础模型，具有强大的泛化能力。2) 通过引入平移和缩放勒让德记忆，更好地适应不同时间序列数据的特性。3) 采用基于归一化流的预测头，可以灵活地建模任意复杂的预测分布。与现有方法相比，FLAME在效率、鲁棒性和准确性方面均有所提升。

**关键设计**：FLAME的关键设计包括：1) 平移勒让德记忆（LegT）和缩放勒让德记忆（LegS）的具体实现方式，包括平移和缩放参数的选择。2) 归一化流预测头的具体结构，包括流的类型和层数。3) 损失函数的设计，包括确定性预测的损失函数和概率预测的损失函数。4) 模型训练的优化算法和超参数设置。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14253/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14253/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14253/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FLAME在TSFM-Bench和ProbTS等基准测试中取得了显著的成果。在确定性预测任务中，FLAME在多个数据集上超越了现有的最先进模型。在概率预测任务中，FLAME能够准确地建模预测分布，并取得了优异的预测性能。实验结果表明，FLAME在零样本学习方面具有强大的泛化能力。

## 🎯 应用场景

FLAME可应用于各种时间序列预测场景，如金融市场预测、能源需求预测、供应链管理、交通流量预测、天气预报等。其高效性和鲁棒性使其在资源受限的环境中也能发挥作用。未来，FLAME有望成为通用时间序列预测的基础模型，推动相关领域的发展。

## 📄 摘要（原文）

> In this work, we introduce FLAME, a family of extremely lightweight and capable Time Series Foundation Models, which support both deterministic and probabilistic forecasting via generative probabilistic modeling, thus ensuring both efficiency and robustness. FLAME utilizes the Legendre Memory for strong generalization capabilities. Through adapting variants of Legendre Memory, i.e., translated Legendre (LegT) and scaled Legendre (LegS), in the Encoding and Decoding phases, FLAME can effectively capture the inherent inductive bias within data and make efficient long-range inferences. To enhance the accuracy of probabilistic forecasting while keeping efficient, FLAME adopts a Normalization Flow based forecasting head, which can model the arbitrarily intricate distributions over the forecasting horizon in a generative manner. Comprehensive experiments on well-recognized benchmarks, including TSFM-Bench and ProbTS, demonstrate the consistent state-of-the-art zero-shot performance of FLAME on both deterministic and probabilistic forecasting tasks.

