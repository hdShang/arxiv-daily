---
layout: default
title: Physics-Guided Learning of Meteorological Dynamics for Weather Downscaling and Forecasting
---

# Physics-Guided Learning of Meteorological Dynamics for Weather Downscaling and Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14555" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14555v2</a>
  <a href="https://arxiv.org/pdf/2505.14555.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14555v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14555v2', 'Physics-Guided Learning of Meteorological Dynamics for Weather Downscaling and Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingtao Luo, Shikai Fang, Binqing Wu, Qingsong Wen, Liang Sun

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-05-23)

**备注**: Published/Accepted in ACM SIGKDD 2025

**DOI**: [10.1145/3711896.3737081](https://doi.org/10.1145/3711896.3737081)

---

## 💡 一句话要点

**提出PhyDL-NWP以解决传统天气预报的计算与物理不足问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `天气预报` `深度学习` `物理引导` `数值天气预报` `模型微调` `自动微分` `物理一致性`

## 📋 核心要点

1. 现有的数值天气预报方法计算复杂且物理模型不完整，导致预测效果受限。
2. 提出PhyDL-NWP框架，通过将物理方程与深度学习模型结合，提升天气预报的准确性与效率。
3. 实验结果显示，PhyDL-NWP在推理速度上提升至170倍，同时保持较高的物理一致性。

## 📝 摘要（中文）

天气预报至关重要，但传统的数值天气预报方法在计算上消耗巨大且物理模型不完整。深度学习模型虽然提高了效率和准确性，但常常忽视物理法则，限制了其可解释性和泛化能力。本文提出了PhyDL-NWP，一个物理引导的深度学习框架，将物理方程与潜在力参数化整合到数据驱动模型中。该框架能够从任意时空坐标预测天气变量，通过自动微分计算物理项，并使用物理信息损失函数使预测与控制动力学对齐。PhyDL-NWP实现了无分辨率下的降尺度，模型微调开销极小，推理速度提升至170倍，参数量仅为55K。实验表明，PhyDL-NWP在预报性能和物理一致性上均有所提升。

## 🔬 方法详解

**问题定义**：本文旨在解决传统天气预报方法在计算复杂性和物理模型不足方面的挑战，导致的预测效果不佳的问题。

**核心思路**：PhyDL-NWP框架通过将物理方程与深度学习模型相结合，利用物理信息来指导模型学习，从而提高预测的准确性和可解释性。

**技术框架**：该框架包括数据输入模块、物理方程计算模块、深度学习模型和损失函数模块。数据输入模块接收时空坐标，物理方程模块通过自动微分计算物理项，深度学习模型进行预测，损失函数模块确保预测与物理规律一致。

**关键创新**：PhyDL-NWP的主要创新在于将物理方程与深度学习模型有效结合，形成物理引导的学习过程，这与传统方法的纯数据驱动模型形成了显著对比。

**关键设计**：在设计上，PhyDL-NWP使用了物理信息损失函数，确保模型输出符合物理规律，并且通过潜在力参数化减少了模型的复杂性，参数量仅为55K。

## 📊 实验亮点

实验结果表明，PhyDL-NWP在推理速度上实现了高达170倍的提升，相较于传统方法显著提高了预测性能和物理一致性，展现出其在天气预报领域的强大潜力。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在气象预报、气候模拟和环境监测等领域。通过提高天气预报的准确性和效率，PhyDL-NWP能够为决策支持系统提供更可靠的数据，进而影响农业、交通和灾害管理等多个行业的实际应用。

## 📄 摘要（原文）

> Weather forecasting is essential but remains computationally intensive and physically incomplete in traditional numerical weather prediction (NWP) methods. Deep learning (DL) models offer efficiency and accuracy but often ignore physical laws, limiting interpretability and generalization. We propose PhyDL-NWP, a physics-guided deep learning framework that integrates physical equations with latent force parameterization into data-driven models. It predicts weather variables from arbitrary spatiotemporal coordinates, computes physical terms via automatic differentiation, and uses a physics-informed loss to align predictions with governing dynamics. PhyDL-NWP enables resolution-free downscaling by modeling weather as a continuous function and fine-tunes pre-trained models with minimal overhead, achieving up to 170x faster inference with only 55K parameters. Experiments show that PhyDL-NWP improves both forecasting performance and physical consistency.

