---
layout: default
title: Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation
---

# Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24263" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24263v1</a>
  <a href="https://arxiv.org/pdf/2505.24263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24263v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24263v1', 'Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Naila Shafirni Hidayat, Muhammad Dehan Al Kautsar, Alfan Farizki Wicaksono, Fajri Koto

**分类**: cs.CL

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出数据泄漏模拟方法以提升LLM评估的透明性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据泄漏检测` `大型语言模型` `评估透明性` `n-gram方法` `半半问题` `实例级检测` `基准测试`

## 📋 核心要点

1. 现有的数据泄漏检测方法主要集中在识别异常值，缺乏在模拟泄漏条件下的有效评估。
2. 本文提出了一种新的半半问题方法，并比较了置换法和n-gram方法在模拟泄漏场景下的表现。
3. 实验结果显示，n-gram方法在F1-score上表现最佳，并且通过改进技术支持实例级检测，降低了计算开销。

## 📝 摘要（中文）

大型语言模型（LLMs）的性能不断提升，然而训练数据的透明度不足引发了对评估集与训练集重叠的担忧。尽管已有研究提出了数据泄漏检测方法，但这些方法主要集中在识别异常值，并未在受控的模拟泄漏条件下进行评估。本文比较了现有的泄漏检测技术，包括置换法和n-gram方法，并探索了一种轻量级的方法——半半问题。尽管半半问题提供了低成本的替代方案，但分析表明n-gram方法在F1-score上表现最佳。此外，本文还对这些技术进行了改进，以支持实例级检测并减少计算开销。基于最佳方法，我们创建了MMLU和HellaSwag的清理版本，并重新评估了多种LLM。研究结果为更可靠和透明的评估提供了实际路径，并建议在发布基准结果前进行污染检查。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型评估中训练数据与评估集重叠的问题，现有方法在模拟泄漏条件下的有效性不足。

**核心思路**：通过比较多种数据泄漏检测技术，提出了一种轻量级的半半问题方法，并在受控环境中模拟真实泄漏场景，以评估其有效性。

**技术框架**：研究首先在持续预训练设置下模拟数据泄漏场景，然后应用不同的泄漏检测方法，包括置换法、n-gram方法和半半问题，最后进行实例级检测和结果清理。

**关键创新**：最重要的创新在于提出了半半问题方法，并在模拟泄漏条件下系统比较了多种检测技术，发现n-gram方法在性能上优于其他方法。

**关键设计**：在技术细节上，研究对n-gram方法进行了优化，以提高F1-score，并在实例级检测中减少计算开销，确保方法的实用性和效率。

## 📊 实验亮点

实验结果表明，n-gram方法在F1-score上 consistently outperform 其他检测方法，提供了更高的准确性。通过改进技术，实例级检测的计算开销显著降低，为实际应用提供了更高效的解决方案。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的评估和基准测试，尤其是在需要确保评估结果透明性和公正性的场景。通过提供清理后的数据集和改进的检测方法，研究为未来的模型评估提供了可靠的工具，可能会影响模型开发和评估的标准流程。

## 📄 摘要（原文）

> The performance of large language models (LLMs) continues to improve, as reflected in rising scores on standard benchmarks. However, the lack of transparency around training data raises concerns about potential overlap with evaluation sets and the fairness of reported results. Although prior work has proposed methods for detecting data leakage, these approaches primarily focus on identifying outliers and have not been evaluated under controlled simulated leakage conditions. In this work, we compare existing leakage detection techniques, namely permutation and n-gram-based methods, under a continual pretraining setup that simulates real-world leakage scenarios, and additionally explore a lightweight method we call semi-half question. Although semi-half offers a low-cost alternative, our analysis shows that the n-gram method consistently achieves the highest F1-score. We also refine these techniques to support instance-level detection and reduce computational overhead. Leveraging the best-performing method, we create cleaned versions of MMLU and HellaSwag, and re-evaluate several LLMs. Our findings present a practical path toward more reliable and transparent evaluations, and we recommend contamination checks as a standard step before releasing benchmark results.

