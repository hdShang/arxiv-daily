---
layout: default
title: "Explainable Deep Neural Network for Multimodal ECG Signals: Intermediate vs Late Fusion"
---

# Explainable Deep Neural Network for Multimodal ECG Signals: Intermediate vs Late Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11666" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11666v2</a>
  <a href="https://arxiv.org/pdf/2508.11666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11666v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11666v2', 'Explainable Deep Neural Network for Multimodal ECG Signals: Intermediate vs Late Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timothy Oladunni, Ehimen Aneni

**分类**: eess.SP, cs.LG

**发布日期**: 2025-08-06 (更新: 2025-10-12)

---

## 💡 一句话要点

**提出多模态深度神经网络以提高心电图信号分类准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `深度学习` `心电图` `可解释性` `心血管疾病` `分类模型` `特征提取` `统计依赖性`

## 📋 核心要点

1. 现有单模态深度学习模型在心电图分类中存在过拟合和泛化能力不足的问题，限制了其在临床应用中的有效性。
2. 本研究提出了一种多模态深度神经网络，通过中间融合和后期融合策略比较，旨在提高心电图信号的分类准确性。
3. 实验结果显示，中间融合策略的准确率达到97%，相较于单独模型和后期融合均有显著提升，且模型可解释性得到增强。

## 📝 摘要（中文）

单模态深度学习模型的局限性，尤其是过拟合和泛化能力不足，促使多模态融合策略的研究。多模态深度神经网络（MDNN）能够整合不同数据域，为准确预测提供了有力解决方案。然而，最优的融合策略——中间融合（特征级）与后期融合（决策级）在高风险临床环境下的研究仍显不足。本研究比较了心电图信号在时间、频率和时频三个域中的中间融合与后期融合策略的有效性。实验结果表明，中间融合的准确率高达97%，显著优于后期融合，且模型的可解释性分析显示两者与离散化的心电图信号一致。提出的基于心电图域的多模态模型在预测能力和可解释性上均优于现有模型。

## 🔬 方法详解

**问题定义**：本研究旨在解决单模态深度学习模型在心电图（ECG）分类中的局限性，特别是过拟合和泛化能力不足的问题。现有方法在高风险临床环境下的有效性亟待提高。

**核心思路**：论文提出通过比较中间融合（特征级）与后期融合（决策级）策略，探索多模态深度神经网络（MDNN）在心电图信号分类中的最佳应用，以实现更高的预测准确性和可解释性。

**技术框架**：研究采用了多模态深度神经网络架构，整合时间、频率和时频三个域的心电图信号。主要模块包括特征提取层、融合层和分类层，分别负责信号处理、特征融合和最终分类。

**关键创新**：本研究的主要创新在于系统比较了中间融合与后期融合策略在心电图信号分类中的效果，发现中间融合在准确性和可解释性上均优于后期融合，填补了该领域的研究空白。

**关键设计**：在模型设计中，采用了特定的损失函数以优化分类性能，并通过互信息（MI）分析验证了离散化心电图信号与对应显著性图之间的统计依赖性。

## 📊 实验亮点

实验结果表明，中间融合策略的最高准确率达到97%，相较于单模态模型和后期融合模型的提升幅度显著，Cohen's d值分别为大于0.8和0.40，显示出中间融合在心电图分类中的优势。

## 🎯 应用场景

该研究的成果在心血管疾病的早期诊断和监测中具有重要应用潜力，能够为临床医生提供更为准确的决策支持。此外，增强的可解释性使得医疗AI系统在实际应用中更具可信度，推动了智能医疗的发展。

## 📄 摘要（原文）

> The limitations of unimodal deep learning models, particularly their tendency to overfit and limited generalizability, have renewed interest in multimodal fusion strategies. Multimodal deep neural networks (MDNN) have the capability of integrating diverse data domains and offer a promising solution for robust and accurate predictions. However, the optimal fusion strategy, intermediate fusion (feature-level) versus late fusion (decision-level) remains insufficiently examined, especially in high-stakes clinical contexts such as ECG-based cardiovascular disease (CVD) classification. This study investigates the comparative effectiveness of intermediate and late fusion strategies using ECG signals across three domains: time, frequency, and time-frequency. A series of experiments were conducted to identify the highest-performing fusion architecture. Results demonstrate that intermediate fusion consistently outperformed late fusion, achieving a peak accuracy of 97 percent, with Cohen's d > 0.8 relative to standalone models and d = 0.40 compared to late fusion. Interpretability analyses using saliency maps reveal that both models align with the discretized ECG signals. Statistical dependency between the discretized ECG signals and corresponding saliency maps for each class was confirmed using Mutual Information (MI). The proposed ECG domain-based multimodal model offers superior predictive capability and enhanced explainability, crucial attributes in medical AI applications, surpassing state-of-the-art models.

