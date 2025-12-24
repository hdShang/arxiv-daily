---
layout: default
title: Towards Foundation Models for Experimental Readout Systems Combining Discrete and Continuous Data
---

# Towards Foundation Models for Experimental Readout Systems Combining Discrete and Continuous Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08736" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08736v2</a>
  <a href="https://arxiv.org/pdf/2505.08736.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08736v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08736v2', 'Towards Foundation Models for Experimental Readout Systems Combining Discrete and Continuous Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: James Giroux, Cristiano Fanelli

**分类**: cs.LG, hep-ex, nucl-ex, physics.ins-det

**发布日期**: 2025-05-13 (更新: 2025-07-18)

**备注**: 27 pages; 18 figures

---

## 💡 一句话要点

**提出原型基础模型以解决核物理实验读出系统中的数据处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基础模型` `核物理` `数据处理` `切伦科夫探测器` `生成模型` `条件生成` `专家混合` `高分辨率标记化`

## 📋 核心要点

1. 现有的标记化方案在处理低级探测器输入时存在分辨率损失和条件生成支持不足的问题。
2. 提出了四项创新，包括离散与连续变量的独立词汇、连续动力学条件和专家混合生成等。
3. 模型在高性能DIRC中经过验证，能够快速生成高保真的切伦科夫光子数据，并在重建任务中表现出良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种用于核物理的原型基础模型，能够处理未来电子离子对撞机中成像切伦科夫探测器的低级探测器输入。基于现有的下一个标记预测方法，我们旨在解决现有标记化方案导致的分辨率损失和有限的条件生成支持等潜在挑战。我们提出了四项关键创新：为离散和连续变量分别建立词汇，通过因果多头交叉注意力（CMHCA）结合；通过预置上下文嵌入实现连续动力学条件；可扩展且简单的高分辨率连续变量标记化，无需联合词汇膨胀；通过专家混合实现类条件生成。我们的模型能够快速、高保真地生成切伦科夫光子的像素和时间序列，并通过高性能DIRC中的闭合测试进行了验证。我们还展示了模型在重建任务（如π/ K介子识别和噪声过滤）中的泛化能力，并展示了其在特定目标下的微调能力。

## 🔬 方法详解

**问题定义**：本文旨在解决核物理实验中，特别是在电子离子对撞机的成像切伦科夫探测器中，低级探测器输入的处理问题。现有方法在标记化过程中常常导致分辨率损失，并且对条件生成的支持有限。

**核心思路**：论文提出了一种基础模型，通过分别为离散和连续变量建立词汇，并结合因果多头交叉注意力（CMHCA），以提高数据处理的精度和效率。

**技术框架**：整体架构包括四个主要模块：离散和连续变量的独立词汇、通过上下文嵌入实现的连续动力学条件、无联合词汇膨胀的高分辨率连续变量标记化，以及通过专家混合实现的类条件生成。

**关键创新**：最重要的创新点在于引入了独立的词汇体系和因果多头交叉注意力机制，这与现有方法的单一词汇体系形成了本质区别，显著提升了模型的生成能力。

**关键设计**：模型设计中采用了高分辨率的连续变量标记化策略，避免了联合词汇的膨胀，同时在损失函数和网络结构上进行了优化，以适应不同的生成任务。具体的参数设置和网络结构细节在实验部分进行了详细说明。

## 📊 实验亮点

实验结果表明，模型在高性能DIRC中能够快速生成高保真的切伦科夫光子数据，且在重建任务中表现出良好的泛化能力。与基线模型相比，生成的像素和时间序列在分辨率和准确性上有显著提升，验证了模型的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括核物理实验中的数据处理和分析，尤其是在高能物理实验中对探测器数据的快速处理和重建。未来，模型的设计理念和技术框架也可能扩展到其他领域，如医学成像和粒子物理学中的数据分析，具有重要的实际价值。

## 📄 摘要（原文）

> We present a (proto) Foundation Model for Nuclear Physics, capable of operating on low-level detector inputs from Imaging Cherenkov Detectors at the future Electron Ion Collider. Building upon established next-token prediction approaches, we aim to address potential challenges such as resolution loss from existing tokenization schemes and limited support for conditional generation. We propose four key innovations: (i) separate vocabularies for discrete and continuous variates, combined via Causal Multi-Head Cross-Attention (CMHCA), (ii) continuous kinematic conditioning through prepended context embeddings, (iii) scalable and simple, high-resolution continuous variate tokenization without joint vocabulary inflation, and (iv) class conditional generation through a Mixture of Experts. Our model enables fast, high-fidelity generation of pixel and time sequences for Cherenkov photons, validated through closure tests in the High Performance DIRC. We also show our model generalizes to reconstruction tasks such as pion/kaon identification, and noise filtering, in which we show its ability to leverage fine-tuning under specific objectives.

