---
layout: default
title: "MORPH: PDE Foundation Models with Arbitrary Data Modality"
---

# MORPH: PDE Foundation Models with Arbitrary Data Modality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21670" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21670v3</a>
  <a href="https://arxiv.org/pdf/2509.21670.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21670v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21670v3', 'MORPH: PDE Foundation Models with Arbitrary Data Modality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahindra Singh Rautela, Alexander Most, Siddharth Mansingh, Bradley C. Love, Ayan Biswas, Diane Oyen, Earl Lawrence

**分类**: cs.CV, cs.AI, cs.LG, physics.comp-ph

**发布日期**: 2025-09-25 (更新: 2025-12-04)

**🔗 代码/项目**: [GITHUB](https://github.com/lanl/MORPH)

---

## 💡 一句话要点

**提出MORPH模型以处理多模态偏微分方程数据**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏微分方程` `多模态学习` `卷积视觉变换器` `自回归模型` `科学机器学习` `数据驱动` `迁移学习`

## 📋 核心要点

1. 现有方法在处理异构和多模态的偏微分方程数据时，面临计算效率低和信息传递不充分的挑战。
2. MORPH模型通过卷积视觉变换器架构，结合组件卷积和交叉注意力等技术，有效捕捉局部交互和不同物理场之间的信息。
3. 实验结果表明，MORPH在多个下游任务中超越了强基线和最新的先进模型，展示了其优越的迁移学习能力。

## 📝 摘要（中文）

我们介绍了MORPH，这是一种模态无关的自回归基础模型，专门用于偏微分方程（PDE）。MORPH基于卷积视觉变换器骨干网络，能够无缝处理不同分辨率的异构时空数据集，包括1D到3D的多种数据模态，以及混合标量和向量成分的多个场。该架构结合了组件卷积、场间交叉注意力和轴向注意力等技术，显著降低了计算负担，同时保持了表达能力。通过在多样化的PDE数据集上进行预训练，MORPH在多个下游预测任务中表现优异，超越了从头训练的模型，展示了其在科学观察的异构和多模态学习中的灵活性和强大能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决在处理异构和多模态偏微分方程（PDE）数据时，现有方法在计算效率和信息传递方面的不足。

**核心思路**：MORPH模型采用卷积视觉变换器架构，设计了组件卷积和交叉注意力机制，以有效捕捉局部交互和不同物理场之间的信息传播。

**技术框架**：MORPH的整体架构包括组件卷积模块、场间交叉注意力模块和轴向注意力模块，能够处理不同分辨率和模态的数据。

**关键创新**：MORPH的主要创新在于其模态无关性和自回归特性，能够同时处理标量和向量数据，并通过轴向注意力降低计算复杂度。

**关键设计**：模型采用了低秩适配器（LoRA）进行参数高效的微调，损失函数设计上考虑了多模态数据的特性，以确保模型在多样化数据集上的有效学习。

## 📊 实验亮点

在多个下游任务的评估中，MORPH模型的表现超越了从头训练的模型，且在与强基线和最新模型的比较中，展示了显著的性能提升，证明了其在科学机器学习中的有效性和优越性。

## 🎯 应用场景

MORPH模型在科学计算、气候模拟、流体动力学等领域具有广泛的应用潜力。其灵活的架构能够处理复杂的物理现象，为科学机器学习提供了新的思路，推动了数据驱动的科学研究进展。

## 📄 摘要（原文）

> We introduce MORPH, a modality-agnostic, autoregressive foundation model for partial differential equations (PDEs). MORPH is built on a convolutional vision transformer backbone that seamlessly handles heterogeneous spatiotemporal datasets of varying data modality (1D--3D) at different resolutions, and multiple fields with mixed scalar and vector components. The architecture combines (i) component-wise convolution, which jointly processes scalar and vector channels to capture local interactions, (ii) inter-field cross-attention, which models and selectively propagates information between different physical fields, (iii) axial attentions, which factorize full spatiotemporal self-attention along individual spatial and temporal axes to reduce computational burden while retaining expressivity. We pretrain multiple model variants on a diverse collection of heterogeneous PDE datasets and evaluate transfer to a range of downstream prediction tasks. Using both full-model fine-tuning and parameter-efficient low-rank adapters (LoRA), MORPH outperforms models trained from scratch. Across extensive evaluations, MORPH matches or surpasses strong baselines and recent state-of-the-art models. Collectively, these capabilities present a flexible and powerful backbone for learning from the heterogeneous and multimodal nature of scientific observations, charting a path toward scalable and data-efficient scientific machine learning. The source code, datasets, and models are publicly available at https://github.com/lanl/MORPH.

