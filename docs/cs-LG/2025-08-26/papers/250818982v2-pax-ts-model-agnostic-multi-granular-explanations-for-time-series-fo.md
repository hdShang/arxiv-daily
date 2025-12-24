---
layout: default
title: "PAX-TS: Model-agnostic multi-granular explanations for time series forecasting via localized perturbations"
---

# PAX-TS: Model-agnostic multi-granular explanations for time series forecasting via localized perturbations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18982" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18982v2</a>
  <a href="https://arxiv.org/pdf/2508.18982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18982v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18982v2', 'PAX-TS: Model-agnostic multi-granular explanations for time series forecasting via localized perturbations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tim Kreuzer, Jelena Zdravkovic, Panagiotis Papapetrou

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-26 (更新: 2025-11-15)

---

## 💡 一句话要点

**提出PAX-TS以解决时间序列预测模型的可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `可解释性` `模型无关` `局部扰动` `多粒度解释` `跨通道相关性` `算法比较` `性能模式`

## 📋 核心要点

1. 现有时间序列预测模型通常缺乏可解释性，无法提供有效的预测解释，限制了其应用。
2. PAX-TS是一种模型无关的后处理算法，通过局部输入扰动生成多粒度解释，适用于时间序列预测。
3. 实验结果表明，不同算法在相同数据集上的解释存在显著差异，PAX-TS能够有效捕捉模型行为并识别性能模式。

## 📝 摘要（中文）

时间序列预测在近年来取得了显著进展，尤其是变换器模型和大型语言模型推动了技术的前沿。然而，现代预测模型通常缺乏透明性，无法提供预测的解释，而现有的后处理可解释性方法如LIME并不适用于预测场景。为此，本文提出了PAX-TS，这是一种模型无关的后处理算法，旨在解释时间序列预测模型及其预测结果。该方法基于局部输入扰动，能够生成多粒度的解释，并能够表征多变量时间序列预测中的跨通道相关性。我们在七种算法和十个多样化数据集的基准测试中展示了该方法，并与其他两种先进的解释算法进行了比较，结果表明PAX-TS有效捕捉了模型的行为。

## 🔬 方法详解

**问题定义**：本文旨在解决时间序列预测模型的可解释性问题。现有的后处理可解释性方法如LIME不适用于时间序列预测，导致模型的决策过程不透明。

**核心思路**：PAX-TS通过局部输入扰动生成多粒度的解释，能够有效捕捉模型的行为，并表征多变量时间序列中的跨通道相关性。这种设计使得解释不仅限于单一粒度，而是能够从多个层面进行分析。

**技术框架**：PAX-TS的整体架构包括输入扰动生成模块、解释生成模块和性能评估模块。首先，通过对输入数据进行局部扰动，生成不同的预测结果；然后，分析这些结果以生成多粒度的解释；最后，通过性能评估模块验证解释的有效性。

**关键创新**：PAX-TS的主要创新在于其模型无关性和多粒度解释能力，能够在不同算法和数据集上有效应用，区别于传统的单一粒度解释方法。

**关键设计**：在参数设置上，PAX-TS采用了适应性扰动幅度，以确保生成的扰动既能影响预测结果，又不会过度干扰原始数据。损失函数设计上，强调了模型输出与扰动输入之间的相关性，以增强解释的准确性。

## 📊 实验亮点

实验结果显示，PAX-TS在七种不同算法和十个多样化数据集上表现出色，能够有效区分高性能与低性能算法的解释，且在预测误差上不同模式之间存在显著差异，验证了其对模型行为的有效捕捉能力。

## 🎯 应用场景

PAX-TS可广泛应用于金融、气象、医疗等领域的时间序列预测，帮助决策者理解模型的预测依据，从而提高预测的可信度和透明度。未来，该方法有望推动可解释人工智能的发展，促进模型在关键领域的应用。

## 📄 摘要（原文）

> Time series forecasting has seen considerable improvement during the last years, with transformer models and large language models driving advancements of the state of the art. Modern forecasting models are generally opaque and do not provide explanations for their forecasts, while well-known post-hoc explainability methods like LIME are not suitable for the forecasting context. We propose PAX-TS, a model-agnostic post-hoc algorithm to explain time series forecasting models and their forecasts. Our method is based on localized input perturbations and results in multi-granular explanations. Further, it is able to characterize cross-channel correlations for multivariate time series forecasts. We clearly outline the algorithmic procedure behind PAX-TS, demonstrate it on a benchmark with 7 algorithms and 10 diverse datasets, compare it with two other state-of-the-art explanation algorithms, and present the different explanation types of the method. We found that the explanations of high-performing and low-performing algorithms differ on the same datasets, highlighting that the explanations of PAX-TS effectively capture a model's behavior. Based on time step correlation matrices resulting from the benchmark, we identify 6 classes of patterns that repeatedly occur across different datasets and algorithms. We found that the patterns are indicators of performance, with noticeable differences in forecasting error between the classes. Lastly, we outline a multivariate example where PAX-TS demonstrates how the forecasting model takes cross-channel correlations into account. With PAX-TS, time series forecasting models' mechanisms can be illustrated in different levels of detail, and its explanations can be used to answer practical questions on forecasts.

