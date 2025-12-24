---
layout: default
title: "mTSBench: Benchmarking Multivariate Time Series Anomaly Detection and Model Selection at Scale"
---

# mTSBench: Benchmarking Multivariate Time Series Anomaly Detection and Model Selection at Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21550" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21550v1</a>
  <a href="https://arxiv.org/pdf/2506.21550.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21550v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21550v1', 'mTSBench: Benchmarking Multivariate Time Series Anomaly Detection and Model Selection at Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaona Zhou, Constantin Brif, Ismini Lourentzou

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出mTSBench以解决多变量时间序列异常检测的基准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多变量时间序列` `异常检测` `模型选择` `基准评估` `无监督学习` `大型语言模型` `数据集构建`

## 📋 核心要点

1. 多变量时间序列异常检测面临变量间复杂依赖、时间动态和稀疏标签等挑战，现有方法难以全面解决这些问题。
2. 本文提出mTSBench，作为最大的MTS-AD基准，系统评估多种异常检测方法及无监督模型选择技术。
3. 实验结果显示，没有单一检测器在所有数据集上表现最佳，且现有选择方法仍存在显著改进空间。

## 📝 摘要（中文）

多变量时间序列异常检测（MTS-AD）在医疗、网络安全和工业监控等领域至关重要，但由于变量间复杂的依赖关系、时间动态和稀疏的异常标签，仍然面临挑战。本文提出了mTSBench，这是迄今为止最大的MTS-AD基准，涵盖了19个数据集中的344个标记时间序列和12个不同应用领域。mTSBench评估了24种异常检测方法，包括基于大型语言模型（LLM）的多变量时间序列检测器，并在标准化条件下系统性地基准化无监督模型选择技术。结果表明，没有单一检测器在所有数据集上表现优异，强调了模型选择的重要性。然而，即使是最先进的选择方法也远未达到最佳，揭示了关键的差距。mTSBench提供了一个统一的评估套件，以实现严格、可重复的比较，并促进未来在自适应异常检测和稳健模型选择方面的进展。

## 🔬 方法详解

**问题定义**：本文旨在解决多变量时间序列异常检测中的基准评估问题。现有方法在处理复杂的变量间依赖性和时间动态时表现不佳，且缺乏统一的评估标准。

**核心思路**：mTSBench通过构建一个包含344个标记时间序列的综合基准，系统性地评估24种异常检测方法，尤其是基于LLM的检测器，旨在为模型选择提供标准化的比较平台。

**技术框架**：mTSBench的整体架构包括数据集构建、异常检测方法评估和无监督模型选择技术的基准化。首先，收集并标记多种应用领域的数据集；其次，实施多种检测方法并进行性能评估；最后，分析模型选择的效果。

**关键创新**：mTSBench的主要创新在于其规模和系统性，首次提供了一个涵盖多种应用场景的统一评估平台，填补了现有基准的空白。

**关键设计**：在设计中，采用了标准化的评估指标和实验设置，确保不同方法的可比性。同时，针对不同模型的超参数进行了优化，以提高检测性能。

## 📊 实验亮点

实验结果表明，mTSBench在评估24种异常检测方法时，未发现任何单一检测器在所有数据集上表现最佳，强调了模型选择的重要性。尽管使用了最先进的选择方法，仍然存在显著的性能提升空间，揭示了当前技术的不足。

## 🎯 应用场景

该研究的潜在应用领域包括医疗监测、网络安全和工业设备监控等，能够帮助相关领域的研究人员和工程师更有效地识别异常情况。通过提供统一的评估框架，mTSBench将推动自适应异常检测技术的发展，提升模型选择的准确性和可靠性。

## 📄 摘要（原文）

> Multivariate time series anomaly detection (MTS-AD) is critical in domains like healthcare, cybersecurity, and industrial monitoring, yet remains challenging due to complex inter-variable dependencies, temporal dynamics, and sparse anomaly labels. We introduce mTSBench, the largest benchmark to date for MTS-AD and unsupervised model selection, spanning 344 labeled time series across 19 datasets and 12 diverse application domains. mTSBench evaluates 24 anomaly detection methods, including large language model (LLM)-based detectors for multivariate time series, and systematically benchmarks unsupervised model selection techniques under standardized conditions. Consistent with prior findings, our results confirm that no single detector excels across datasets, underscoring the importance of model selection. However, even state-of-the-art selection methods remain far from optimal, revealing critical gaps. mTSBench provides a unified evaluation suite to enable rigorous, reproducible comparisons and catalyze future advances in adaptive anomaly detection and robust model selection.

