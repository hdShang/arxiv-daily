---
layout: default
title: "Kairos: Towards Adaptive and Generalizable Time Series Foundation Models"
---

# Kairos: Towards Adaptive and Generalizable Time Series Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25826" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25826v1</a>
  <a href="https://arxiv.org/pdf/2509.25826.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25826v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25826v1', 'Kairos: Towards Adaptive and Generalizable Time Series Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Feng, Shaocheng Lan, Yuchen Fang, Wenchao He, Lintao Ma, Xingyu Lu, Kan Ren

**分类**: cs.LG

**发布日期**: 2025-09-30

**🔗 代码/项目**: [PROJECT_PAGE](https://foundation-model-research.github.io/Kairos)

---

## 💡 一句话要点

**Kairos：面向自适应和泛化时间序列的通用模型框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列分析` `通用模型` `零样本学习` `自适应学习` `动态Patching` `Positional Embedding` `Transformer` `预训练`

## 📋 核心要点

1. 现有时间序列通用模型无法有效处理时间序列中异构的信息密度，尤其是在零样本学习场景下。
2. Kairos通过动态patching tokenizer和实例自适应positional embedding，自适应地调整tokenization粒度和positional encoding。
3. Kairos在PreSTS语料库上训练，并在GIFT-Eval和Time-Series-Library基准测试中，以更少的参数优于现有方法。

## 📝 摘要（中文）

时间序列通用模型（TSFMs）已成为时间序列分析的强大范例，这得益于在多样化数据语料库上的大规模预训练。然而，时间序列本质上在时间上表现出异构的信息密度，受系统状态和信号复杂性的影响，这带来了巨大的建模挑战，尤其是在零样本场景中。当前的TSFMs依赖于非自适应的处理流程，无法捕捉这种动态特性。例如，常见的tokenization策略（如固定大小的patching）强制执行严格的观察粒度，限制了它们适应不同信息密度的能力。类似地，传统的positional encoding施加了统一的时间尺度，使得难以对序列中不同的周期性和趋势进行建模。为了克服这些限制，我们提出了Kairos，一个灵活的TSFM框架，它集成了动态patching tokenizer和实例自适应positional embedding。Kairos自适应地选择tokenization粒度，并根据每个时间序列实例的独特特征定制positional encoding。Kairos在包含超过3000亿个时间点的可预测性分层时间序列（PreSTS）语料库上进行训练，并在推理阶段采用多patch预测策略，在两个常见的零样本基准GIFT-Eval和Time-Series-Library基准上实现了卓越的性能，在各种任务中始终优于已建立的方法。

## 🔬 方法详解

**问题定义**：现有时间序列通用模型（TSFMs）在处理具有异构信息密度的时间序列时存在局限性。固定大小的patching和统一的positional encoding无法适应不同时间序列实例的动态特性，导致零样本学习性能下降。现有方法无法根据时间序列的复杂度和系统状态自适应地调整处理粒度。

**核心思路**：Kairos的核心思路是引入自适应性，使其能够根据每个时间序列实例的特性动态调整tokenization粒度和positional encoding。通过动态patching tokenizer，Kairos可以根据信息密度选择合适的patch大小。通过实例自适应positional embedding，Kairos可以为每个时间序列定制positional encoding，从而更好地捕捉不同的周期性和趋势。

**技术框架**：Kairos的整体框架包括以下几个主要模块：1) **动态Patching Tokenizer**：根据时间序列的信息密度自适应地选择patch大小。2) **实例自适应Positional Embedding**：为每个时间序列实例生成定制的positional encoding。3) **Transformer Backbone**：使用Transformer模型进行时间序列的编码和预测。4) **多Patch预测**：在推理阶段，采用多patch预测策略，提高预测精度。

**关键创新**：Kairos的关键创新在于其自适应性。与传统的TSFMs相比，Kairos能够根据每个时间序列实例的特性动态调整tokenization粒度和positional encoding。这种自适应性使得Kairos能够更好地处理具有异构信息密度的时间序列，从而提高零样本学习性能。

**关键设计**：动态patching tokenizer的设计涉及如何衡量时间序列的信息密度，并根据信息密度选择合适的patch大小。实例自适应positional embedding的设计涉及如何为每个时间序列实例生成定制的positional encoding，以捕捉不同的周期性和趋势。PreSTS语料库的构建采用了可预测性分层策略，确保训练数据的多样性和代表性。多patch预测策略通过融合多个patch的预测结果，提高预测精度。

## 📊 实验亮点

Kairos在GIFT-Eval和Time-Series-Library两个零样本基准测试中取得了显著的性能提升。在GIFT-Eval上，Kairos在多个任务上超越了现有的TSFMs。在Time-Series-Library基准测试中，Kairos在各种任务中始终优于已建立的方法，并且使用了更少的参数，证明了其高效性和泛化能力。

## 🎯 应用场景

Kairos可应用于各种时间序列分析任务，如预测、分类、异常检测等。其自适应性和泛化能力使其在零样本学习场景下具有优势，适用于缺乏标注数据的领域。例如，在金融、医疗、工业等领域，Kairos可以用于预测股票价格、诊断疾病、预测设备故障等，具有广泛的应用前景和实际价值。

## 📄 摘要（原文）

> Time series foundation models (TSFMs) have emerged as a powerful paradigm for time series analysis, driven by large-scale pretraining on diverse data corpora. However, time series inherently exhibit heterogeneous information density over time, influenced by system states and signal complexity, presenting significant modeling challenges especially in a zero-shot scenario. Current TSFMs rely on non-adaptive processing pipelines that fail to capture this dynamic nature. For example, common tokenization strategies such as fixed-size patching enforce rigid observational granularity, limiting their ability to adapt to varying information densities. Similarly, conventional positional encodings impose a uniform temporal scale, making it difficult to model diverse periodicities and trends across series. To overcome these limitations, we propose Kairos, a flexible TSFM framework that integrates a dynamic patching tokenizer and an instance-adaptive positional embedding. Kairos adaptively selects tokenization granularity and tailors positional encodings to the unique characteristics of each time series instance. Trained on a large-scale Predictability-Stratified Time Series (PreSTS) corpus comprising over 300 billion time points and adopting a multi-patch prediction strategy in the inference stage, Kairos achieves superior performance with much fewer parameters on two common zero-shot benchmarks, GIFT-Eval and the Time-Series-Library benchmark, consistently outperforming established methods across diverse tasks. The project page is at https://foundation-model-research.github.io/Kairos .

