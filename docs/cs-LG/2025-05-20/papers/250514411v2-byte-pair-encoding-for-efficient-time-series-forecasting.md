---
layout: default
title: Byte Pair Encoding for Efficient Time Series Forecasting
---

# Byte Pair Encoding for Efficient Time Series Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14411" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14411v2</a>
  <a href="https://arxiv.org/pdf/2505.14411.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14411v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14411v2', 'Byte Pair Encoding for Efficient Time Series Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leon Götz, Marcel Kollovieh, Stephan Günnemann, Leo Schwinn

**分类**: cs.LG

**发布日期**: 2025-05-20 (更新: 2025-08-05)

**备注**: 24 pages in total, 17 figures

---

## 💡 一句话要点

**提出基于模式的时间序列编码方法以提高预测效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `模式识别` `标记化方法` `条件解码` `计算效率` `机器学习` `数据压缩`

## 📋 核心要点

1. 现有时间序列标记化方法缺乏灵活性，导致在简单模式下生成过多标记，增加计算负担。
2. 本文提出了一种基于频繁模式的标记化方案，通过合并样本来自适应压缩时间序列，提升了效率。
3. 实验结果显示，该方法在时间序列预测上性能提升36%，效率提升1990%，并且条件解码进一步降低了均方误差。

## 📝 摘要（中文）

现有的时间序列标记化方法通常将固定数量的样本编码为单独的标记，这种不灵活的方式可能导致在简单模式下生成过多标记，从而增加计算开销。受字节对编码成功的启发，本文提出了一种首个以模式为中心的时间序列标记化方案。该方法基于频繁模式的离散词汇，将具有潜在模式的样本合并为标记，从而自适应地压缩时间序列。通过利用有限的模式集和时间序列的连续特性，我们进一步引入条件解码作为一种轻量级的后处理优化方法，无需梯度计算且不增加计算开销。在最近的时间序列基础模型上，我们的模式基础标记化提高了36%的预测性能，并平均提升了1990%的效率。条件解码进一步将均方误差降低了最多44%。

## 🔬 方法详解

**问题定义**：现有的时间序列标记化方法通常将固定数量的样本编码为单独的标记，这种方法在处理简单模式时会生成过多的标记，导致计算开销显著增加。

**核心思路**：本文提出了一种基于模式的标记化方案，利用频繁模式的离散词汇将样本合并为标记，从而实现自适应压缩，提升时间序列分析的效率和效果。

**技术框架**：该方法的整体架构包括模式识别、样本合并和条件解码三个主要模块。首先识别时间序列中的频繁模式，然后将相应样本合并为标记，最后通过条件解码进行后处理优化。

**关键创新**：最重要的创新在于提出了以模式为中心的标记化方案，能够根据时间序列的特性自适应生成标记，显著减少了计算开销，与传统方法形成鲜明对比。

**关键设计**：该方法的关键设计包括选择合适的频繁模式词汇、定义样本合并的策略，以及实现条件解码的具体算法，这些设计确保了方法的高效性和准确性。

## 📊 实验亮点

实验结果表明，基于模式的标记化方法在时间序列预测中性能提升了36%，效率提升达1990%。此外，条件解码技术进一步将均方误差降低了最多44%，显示出该方法在实际应用中的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场预测、气象数据分析和工业设备监控等。通过提高时间序列预测的效率和准确性，能够为决策提供更可靠的支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Existing time series tokenization methods predominantly encode a constant number of samples into individual tokens. This inflexible approach can generate excessive tokens for even simple patterns like extended constant values, resulting in substantial computational overhead. Inspired by the success of byte pair encoding, we propose the first pattern-centric tokenization scheme for time series analysis. Based on a discrete vocabulary of frequent motifs, our method merges samples with underlying patterns into tokens, compressing time series adaptively. Exploiting our finite set of motifs and the continuous properties of time series, we further introduce conditional decoding as a lightweight yet powerful post-hoc optimization method, which requires no gradient computation and adds no computational overhead. On recent time series foundation models, our motif-based tokenization improves forecasting performance by 36% and boosts efficiency by 1990% on average. Conditional decoding further reduces MSE by up to 44%. In an extensive analysis, we demonstrate the adaptiveness of our tokenization to diverse temporal patterns, its generalization to unseen data, and its meaningful token representations capturing distinct time series properties, including statistical moments and trends.

