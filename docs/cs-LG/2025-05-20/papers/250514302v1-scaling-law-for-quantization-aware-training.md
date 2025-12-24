---
layout: default
title: Scaling Law for Quantization-Aware Training
---

# Scaling Law for Quantization-Aware Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14302" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14302v1</a>
  <a href="https://arxiv.org/pdf/2505.14302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14302v1', 'Scaling Law for Quantization-Aware Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengzhao Chen, Chaoyi Zhang, Jing Liu, Yutao Zeng, Zeyue Xue, Zhiheng Liu, Yunshui Li, Jin Ma, Jie Huang, Xun Zhou, Ping Luo

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-20

**备注**: A unified scaling law for QAT that models quantization error as a function of model size, training data volume, and quantization group size

---

## 💡 一句话要点

**提出统一缩放法则以优化量化感知训练**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化感知训练` `大型语言模型` `量化误差` `混合精度` `模型优化` `训练数据量` `深度学习`

## 📋 核心要点

1. 现有的量化感知训练方法在处理4位精度时的缩放行为尚不明确，且忽视了训练数据量和量化粒度等关键因素。
2. 本文提出了一种统一的缩放法则，将量化误差与模型规模、训练数据量和量化组大小关联，为QAT提供了新的理论基础。
3. 通过268个实验，发现量化误差随着模型规模增加而减少，但训练标记和粗粒度量化会导致误差上升，提供了优化方向。

## 📝 摘要（中文）

大型语言模型（LLMs）需要大量计算和内存资源，给部署带来了挑战。量化感知训练（QAT）通过降低模型精度来应对这些挑战，但其缩放行为，尤其是在4位精度（W4A4）下，尚不明确。现有的QAT缩放法则往往忽视了训练标记数量和量化粒度等关键因素，限制了其适用性。本文提出了一种统一的QAT缩放法则，将量化误差建模为模型规模、训练数据量和量化组大小的函数。通过268个QAT实验，我们发现量化误差随着模型规模的增加而减少，但随着训练标记的增加和量化粒度的粗化而上升。我们还将W4A4量化误差分解为权重和激活组件，发现两者的敏感性不同，权重量化误差对训练标记的增加反应更为敏感。这些发现为QAT的研究和开发提供了重要的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决量化感知训练（QAT）在4位精度下的缩放行为不明确的问题。现有方法未能充分考虑训练标记数量和量化粒度等关键因素，导致其适用性受到限制。

**核心思路**：论文提出了一种统一的缩放法则，将量化误差视为模型规模、训练数据量和量化组大小的函数。这一方法通过系统性实验验证了不同因素对量化误差的影响，提供了新的理论框架。

**技术框架**：研究通过268个QAT实验，分析了模型规模、训练数据量和量化粒度对量化误差的影响。实验结果表明，量化误差的变化趋势与模型规模和训练数据量密切相关。

**关键创新**：最重要的创新在于将量化误差分解为权重和激活组件，并分析其对训练标记的敏感性。这一分解方法揭示了W4A4量化误差的主要来源，为优化提供了新的视角。

**关键设计**：在实验中，采用了混合精度量化的方法来解决激活量化误差的瓶颈，同时对权重量化误差进行了深入分析，发现随着训练数据的增加，权重量化误差最终会超过激活量化误差。

## 📊 实验亮点

实验结果显示，随着模型规模的增加，量化误差显著降低，而训练标记的增加和粗粒度量化则导致误差上升。通过混合精度量化，权重和激活量化误差可以收敛到相似水平，提供了有效的优化策略。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的优化和部署，尤其是在资源受限的环境中。通过改进量化感知训练，能够在保持模型性能的同时显著降低计算和内存需求，推动AI模型在实际应用中的广泛使用。

## 📄 摘要（原文）

> Large language models (LLMs) demand substantial computational and memory resources, creating deployment challenges. Quantization-aware training (QAT) addresses these challenges by reducing model precision while maintaining performance. However, the scaling behavior of QAT, especially at 4-bit precision (W4A4), is not well understood. Existing QAT scaling laws often ignore key factors such as the number of training tokens and quantization granularity, which limits their applicability. This paper proposes a unified scaling law for QAT that models quantization error as a function of model size, training data volume, and quantization group size. Through 268 QAT experiments, we show that quantization error decreases as model size increases, but rises with more training tokens and coarser quantization granularity. To identify the sources of W4A4 quantization error, we decompose it into weight and activation components. Both components follow the overall trend of W4A4 quantization error, but with different sensitivities. Specifically, weight quantization error increases more rapidly with more training tokens. Further analysis shows that the activation quantization error in the FC2 layer, caused by outliers, is the primary bottleneck of W4A4 QAT quantization error. By applying mixed-precision quantization to address this bottleneck, we demonstrate that weight and activation quantization errors can converge to similar levels. Additionally, with more training data, weight quantization error eventually exceeds activation quantization error, suggesting that reducing weight quantization error is also important in such scenarios. These findings offer key insights for improving QAT research and development.

