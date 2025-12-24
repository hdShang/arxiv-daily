---
layout: default
title: "FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting"
---

# FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14253" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14253v1</a>
  <a href="https://arxiv.org/pdf/2512.14253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14253v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14253v1', 'FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingjian Wu, Hanyin Cheng, Xiangfei Qiu, Zhengyu Li, Jilin Hu, Chenjuan Guo, Bin Yang

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**FLAME：基于流增强勒让德记忆模型，用于通用时间序列预测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `勒让德多项式` `归一化流` `零样本学习` `长程依赖` `概率预测` `基础模型`

## 📋 核心要点

1. 现有时间序列预测模型在效率和鲁棒性方面存在挑战，尤其是在处理长程依赖和复杂分布时。
2. FLAME通过引入流增强的勒让德记忆模型，利用勒让德多项式的特性来捕获时间序列的归纳偏置，实现高效的长程推理。
3. 实验表明，FLAME在多个基准数据集上取得了最先进的零样本预测性能，包括确定性和概率性预测任务。

## 📝 摘要（中文）

本文提出FLAME，一种极其轻量且强大的时间序列基础模型家族，它通过生成概率建模支持确定性和概率性预测，从而确保效率和鲁棒性。FLAME利用勒让德记忆来实现强大的泛化能力。通过在编码和解码阶段调整勒让德记忆的变体，即平移勒让德(LegT)和缩放勒让德(LegS)，FLAME可以有效地捕获数据中固有的归纳偏置，并进行有效的长程推理。为了在保持效率的同时提高概率预测的准确性，FLAME采用基于归一化流的预测头，该预测头可以以生成方式对预测范围内任意复杂的分布进行建模。在TSFM-Bench和ProbTS等公认的基准上的综合实验表明，FLAME在确定性和概率性预测任务上都具有一致的最先进的零样本性能。

## 🔬 方法详解

**问题定义**：传统时间序列预测方法难以兼顾效率和鲁棒性，尤其是在处理具有复杂分布和长程依赖关系的数据时。现有方法在泛化能力和处理不确定性方面存在局限性，难以适应各种实际应用场景。

**核心思路**：FLAME的核心思路是利用勒让德多项式构建记忆模块，从而有效地捕获时间序列数据中的归纳偏置。通过在编码和解码阶段使用平移和缩放的勒让德多项式变体，模型能够更好地适应不同时间尺度和频率的模式。此外，采用基于归一化流的预测头，可以对预测范围内的复杂概率分布进行建模，从而提高概率预测的准确性。

**技术框架**：FLAME的整体框架包括编码器、记忆模块和解码器三个主要部分。编码器负责将输入时间序列转换为潜在表示。记忆模块利用勒让德多项式存储和提取时间序列中的关键信息。解码器则根据记忆模块的输出生成预测结果。对于概率预测，解码器后接一个基于归一化流的预测头，用于建模预测分布。

**关键创新**：FLAME的关键创新在于将勒让德记忆模块与归一化流预测头相结合。勒让德记忆模块能够有效地捕获时间序列的归纳偏置，提高模型的泛化能力。归一化流预测头则能够对预测范围内的复杂概率分布进行建模，提高概率预测的准确性。这种结合使得FLAME在确定性和概率性预测任务上都具有优异的性能。

**关键设计**：FLAME的关键设计包括：1) 使用平移和缩放的勒让德多项式变体，以适应不同时间尺度和频率的模式；2) 采用归一化流作为预测头，以建模预测分布的复杂性；3) 设计轻量级的网络结构，以提高模型的效率。具体的参数设置和损失函数选择取决于具体的应用场景和数据集。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14253v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14253v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14253v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FLAME在TSFM-Bench和ProbTS等基准数据集上取得了最先进的零样本预测性能。具体而言，FLAME在确定性和概率性预测任务上均优于现有方法，并在长程预测任务中表现出显著的优势。实验结果表明，FLAME能够有效地捕获时间序列的归纳偏置，并对复杂概率分布进行建模，从而提高预测的准确性和鲁棒性。

## 🎯 应用场景

FLAME可应用于各种时间序列预测场景，如金融市场预测、能源需求预测、供应链管理、交通流量预测和气候变化预测等。其高效性和鲁棒性使其能够处理大规模数据集和复杂的时间序列模式，为决策提供更准确的依据，具有广泛的应用前景。

## 📄 摘要（原文）

> In this work, we introduce FLAME, a family of extremely lightweight and capable Time Series Foundation Models, which support both deterministic and probabilistic forecasting via generative probabilistic modeling, thus ensuring both efficiency and robustness. FLAME utilizes the Legendre Memory for strong generalization capabilities. Through adapting variants of Legendre Memory, i.e., translated Legendre (LegT) and scaled Legendre (LegS), in the Encoding and Decoding phases, FLAME can effectively capture the inherent inductive bias within data and make efficient long-range inferences. To enhance the accuracy of probabilistic forecasting while keeping efficient, FLAME adopts a Normalization Flow based forecasting head, which can model the arbitrarily intricate distributions over the forecasting horizon in a generative manner. Comprehensive experiments on well-recognized benchmarks, including TSFM-Bench and ProbTS, demonstrate the consistent state-of-the-art zero-shot performance of FLAME on both deterministic and probabilistic forecasting tasks.

