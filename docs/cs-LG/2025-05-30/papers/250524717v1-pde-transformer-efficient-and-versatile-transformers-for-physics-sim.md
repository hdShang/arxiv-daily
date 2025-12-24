---
layout: default
title: "PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations"
---

# PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24717" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24717v1</a>
  <a href="https://arxiv.org/pdf/2505.24717.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24717v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24717v1', 'PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benjamin Holzschuh, Qiang Liu, Georg Kohl, Nils Thuerey

**分类**: cs.LG

**发布日期**: 2025-05-30

**备注**: ICML 2025. Code available at https://github.com/tum-pbs/pde-transformer

---

## 💡 一句话要点

**提出PDE-Transformer以提升物理仿真建模效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `物理仿真` `变换器架构` `偏微分方程` `代理建模` `自注意力机制` `大规模数据处理` `时空标记`

## 📋 核心要点

1. 现有的物理仿真建模方法在处理大规模数据时效率低下，难以同时学习多种类型的偏微分方程。
2. PDE-Transformer通过将不同物理通道嵌入为时空标记，并利用通道间自注意力机制，提升了模型的可扩展性和灵活性。
3. 预训练模型在多个下游任务中表现优异，相较于从头训练，性能显著提升，并超越了其他物理仿真基础模型架构。

## 📝 摘要（中文）

我们提出了PDE-Transformer，这是一种改进的基于变换器的架构，旨在对规则网格上的物理仿真进行代理建模。通过结合扩散变换器的最新架构改进以及针对大规模仿真的特定调整，我们构建了一种更具可扩展性和通用性的变换器架构，可作为物理科学领域大型基础模型的支撑。实验表明，我们的架构在16种不同类型的偏微分方程（PDE）的大型数据集上超越了现有的最先进的变换器架构。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有物理仿真建模方法在处理大规模数据时的低效问题，尤其是在同时学习多种类型的偏微分方程时，信息密度不均匀导致的性能下降。

**核心思路**：PDE-Transformer通过将不同物理通道作为独立的时空标记进行嵌入，利用通道间自注意力机制，保持了信息密度的一致性，从而提升了模型的学习能力和效率。

**技术框架**：该架构主要包括数据预处理模块、时空标记嵌入模块、通道间自注意力机制以及输出生成模块。通过这些模块的协同工作，PDE-Transformer能够有效处理复杂的物理仿真任务。

**关键创新**：PDE-Transformer的核心创新在于其独特的时空标记嵌入方式和通道间自注意力机制，这与传统的变换器架构相比，显著提升了对多种PDE的建模能力。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多任务学习效果，并在网络结构上进行了调整，以适应大规模物理仿真数据的处理需求。

## 📊 实验亮点

在实验中，PDE-Transformer在16种不同类型的偏微分方程上表现出色，超越了现有最先进的变换器架构，预训练模型在多个下游任务中性能提升显著，具体提升幅度未知。

## 🎯 应用场景

PDE-Transformer的潜在应用领域包括气候模拟、流体动力学、材料科学等物理科学领域。其高效的建模能力能够加速科学研究和工程应用，推动相关领域的技术进步与创新。

## 📄 摘要（原文）

> We introduce PDE-Transformer, an improved transformer-based architecture for surrogate modeling of physics simulations on regular grids. We combine recent architectural improvements of diffusion transformers with adjustments specific for large-scale simulations to yield a more scalable and versatile general-purpose transformer architecture, which can be used as the backbone for building large-scale foundation models in physical sciences. We demonstrate that our proposed architecture outperforms state-of-the-art transformer architectures for computer vision on a large dataset of 16 different types of PDEs. We propose to embed different physical channels individually as spatio-temporal tokens, which interact via channel-wise self-attention. This helps to maintain a consistent information density of tokens when learning multiple types of PDEs simultaneously. We demonstrate that our pre-trained models achieve improved performance on several challenging downstream tasks compared to training from scratch and also beat other foundation model architectures for physics simulations.

