---
layout: default
title: "VisionTS++: Cross-Modal Time Series Foundation Model with Continual Pre-trained Vision Backbones"
---

# VisionTS++: Cross-Modal Time Series Foundation Model with Continual Pre-trained Vision Backbones

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04379" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04379v3</a>
  <a href="https://arxiv.org/pdf/2508.04379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04379v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04379v3', 'VisionTS++: Cross-Modal Time Series Foundation Model with Continual Pre-trained Vision Backbones')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lefei Shen, Mouxiang Chen, Xu Liu, Han Fu, Xiaoxue Ren, Jianling Sun, Zhuo Li, Chenghao Liu

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-06 (更新: 2025-10-10)

**备注**: 19 pages

**🔗 代码/项目**: [GITHUB](https://github.com/HALF111/VisionTSpp)

---

## 💡 一句话要点

**提出VisionTS++以解决视觉模型在时间序列预测中的跨模态转移问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `跨模态学习` `视觉模型` `多变量建模` `概率预测` `深度学习` `持续预训练`

## 📋 核心要点

1. 现有方法在视觉模型与时间序列之间的跨模态转移面临数据模态差异、多变量预测差异和概率预测差异等挑战。
2. 本文提出的VisionTS++通过持续预训练视觉模型，结合视觉模型过滤和多分位预测等创新方法，解决了上述问题。
3. 实验结果显示，VisionTS++在23个数据集的GIFT-Eval基准测试中表现优异，MSE减少幅度达到6%-44%。

## 📝 摘要（中文）

近期研究表明，经过图像预训练的视觉模型可以作为时间序列基础模型（TSFM），通过将时间序列预测重构为图像重建。然而，由于数据模态差异、多变量预测差异和概率预测差异，视觉到时间序列的有效跨模态转移仍然具有挑战性。为此，本文提出了VisionTS++，该模型基于对视觉模型进行大规模时间序列的持续预训练。我们的方法引入了三项关键创新：视觉模型过滤以识别高质量序列，彩色多变量转换以增强跨变量建模，以及多分位预测以生成无参数假设的分位预测。实验结果表明，VisionTS++在分布内和分布外预测中均实现了最先进的性能，相较于专门的TSFM在均方误差（MSE）上减少了6%-44%。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉模型在时间序列预测中的跨模态转移问题，现有方法在数据模态、预测变量和输出形式上存在显著差异，导致性能不足。

**核心思路**：通过对视觉模型进行大规模时间序列的持续预训练，结合视觉模型过滤和多分位预测等技术，来缩小这些差距，从而提升时间序列预测的准确性和可靠性。

**技术框架**：整体架构包括三个主要模块：视觉模型过滤模块用于筛选高质量序列，彩色多变量转换模块将多变量时间序列编码为多子图RGB图像，以及多分位预测模块通过并行重建头生成分位预测。

**关键创新**：本文的关键创新在于引入视觉模型过滤和彩色多变量转换，前者帮助稳定预训练过程，后者增强了跨变量建模能力。此外，多分位预测方法允许在无参数假设下生成更为灵活的预测结果。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多分位预测的效果，并通过调整网络结构以适应多变量输入，确保模型能够有效处理不同数量的变量。

## 📊 实验亮点

实验结果显示，VisionTS++在GIFT-Eval基准测试中表现优异，较专门的时间序列基础模型在均方误差（MSE）上减少了6%-44%，并在23个数据集上排名第一，展示了其强大的预测能力和广泛的适用性。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场预测、气象数据分析和医疗健康监测等，能够为这些领域提供更为精准的时间序列预测解决方案。未来，VisionTS++有望推动跨模态学习的发展，促进不同数据类型的融合与应用。

## 📄 摘要（原文）

> Recent studies have indicated that vision models pre-trained on images can serve as time series foundation models (TSFMs) by reformulating time series forecasting (TSF) as image reconstruction. However, effective cross-modal transfer from vision to time series remains challenging due to three discrepancies: (1) the data-modality gap between structured, bounded image data and unbounded, heterogeneous time series; (2) the multivariate-forecasting gap between fixed RGB-three-channel vision models and time series with arbitrary numbers of variates; and (3) the probabilistic-forecasting gap between the deterministic outputs of vision models and the requirement for uncertainty-aware probabilistic predictions. To bridge these gaps, we propose VisonTS++, a TSFM based on continual pre-training of a vision model on large-scale time series. Our approach introduces three key innovations: (1) vision-model-based filtering to identify high-quality sequences to stabilize pre-training and mitigate modality gap; (2) colorized multivariate conversion, encoding multivariate series as multi-subfigure RGB images to enhance cross-variate modeling; (3) multi-quantile forecasting, using parallel reconstruction heads to generate quantile forecasts without parametric assumptions. Experiments show that VisionTS++ achieves state-of-the-art performance in both in-distribution and out-of-distribution forecasting, outperforming specialized TSFMs by 6%-44% in MSE reduction and ranking first in GIFT-Eval benchmark which comprises 23 datasets across 7 domains. Our work demonstrates that with appropriate adaptation, vision models can effectively generalize to TSF, thus advancing the pursuit of universal TSFMs. Code is available at https://github.com/HALF111/VisionTSpp.

