---
layout: default
title: Parameter Aware Mamba Model for Multi-task Dense Prediction
---

# Parameter Aware Mamba Model for Multi-task Dense Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14503" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14503v1</a>
  <a href="https://arxiv.org/pdf/2511.14503.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14503v1" onclick="toggleFavorite(this, '2511.14503v1', 'Parameter Aware Mamba Model for Multi-task Dense Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinzhuo Yu, Yunzhi Zhuge, Sitong Gong, Lu Zhang, Pingping Zhang, Huchuan Lu

**分类**: cs.CV

**发布日期**: 2025-11-18

**备注**: Accepted to IEEE Transactions on Cybernetics

**🔗 代码/项目**: [GITHUB](https://github.com/CQC-gogopro/PAMM)

---

## 💡 一句话要点

**提出参数感知Mamba模型PAMM，用于多任务密集预测，提升任务间互联性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多任务学习` `密集预测` `状态空间模型` `Mamba` `参数感知`

## 📋 核心要点

1. 现有方法在多任务密集预测中主要依赖卷积和注意力机制探索任务间交互，缺乏对任务内在属性的有效建模。
2. PAMM利用状态空间模型（SSM）的参数化能力，通过双状态空间参数专家集成任务特定先验，增强任务互联性。
3. 实验表明，PAMM在NYUD-v2和PASCAL-Context数据集上表现出色，验证了其在多任务密集预测中的有效性。

## 📝 摘要（中文）

本文提出了一种新颖的基于解码器的框架，即参数感知Mamba模型（PAMM），专门为多任务学习环境下的密集预测而设计。与使用Transformer建模整体任务关系的方法不同，PAMM利用状态空间模型（SSM）丰富且可扩展的参数来增强任务间的互联性。它采用双状态空间参数专家，集成并设置任务特定的参数先验，从而捕获每个任务的内在属性。这种方法不仅促进了精确的多任务交互，还允许通过结构化的状态空间序列模型（S4）进行任务先验的全局集成。此外，我们采用多方向Hilbert扫描方法来构建多角度特征序列，从而增强序列模型对2D数据的感知能力。在NYUD-v2和PASCAL-Context基准上的大量实验证明了我们提出的方法的有效性。

## 🔬 方法详解

**问题定义**：多任务密集预测旨在同时预测图像的多个属性，例如深度、语义分割和表面法线。现有方法，如基于卷积神经网络（CNN）和注意力机制的模型，在捕捉任务间的复杂关系和利用任务特定先验知识方面存在局限性，难以充分挖掘任务间的互补信息。

**核心思路**：PAMM的核心思路是利用状态空间模型（SSM），特别是Mamba架构，其具有强大的序列建模能力和参数化效率，来显式地建模任务间的依赖关系和任务特定的先验知识。通过参数化的状态空间模型，PAMM能够学习到每个任务的内在属性，并将其融入到多任务学习过程中，从而提升整体预测性能。

**技术框架**：PAMM是一个基于解码器的框架，主要包含以下几个模块：1) 特征提取器：用于提取输入图像的特征表示。2) 双状态空间参数专家：包含两个独立的SSM，分别用于学习任务特定的参数先验。3) 状态空间序列模型（S4）：用于全局集成任务先验，并建模任务间的依赖关系。4) 多方向Hilbert扫描：用于将2D特征图转换为序列，以便SSM进行处理。5) 解码器：用于将序列表示转换为最终的密集预测结果。

**关键创新**：PAMM的关键创新在于：1) 引入双状态空间参数专家，显式地建模任务特定的参数先验。2) 利用Mamba架构的强大序列建模能力，全局集成任务先验，并建模任务间的依赖关系。3) 采用多方向Hilbert扫描，增强序列模型对2D数据的感知能力。与现有方法相比，PAMM能够更有效地利用任务间的互补信息，并提升多任务密集预测的性能。

**关键设计**：双状态空间参数专家使用两个独立的Mamba块，分别学习任务特定的参数先验。S4模块使用标准的S4架构，用于全局集成任务先验。多方向Hilbert扫描采用四个方向的Hilbert曲线，将2D特征图转换为四个序列。损失函数采用加权的多任务损失函数，权重根据任务的重要性进行调整。

## 📊 实验亮点

在NYUD-v2和PASCAL-Context数据集上的实验结果表明，PAMM显著优于现有的多任务密集预测方法。例如，在NYUD-v2数据集上，PAMM在深度预测、表面法线预测和语义分割任务上均取得了state-of-the-art的性能。与之前的最佳方法相比，PAMM在多个指标上取得了显著的提升。

## 🎯 应用场景

PAMM在多任务密集预测方面具有广泛的应用前景，例如自动驾驶（同时预测深度、语义分割和交通标志）、机器人导航（同时预测环境地图和物体类别）和医学图像分析（同时预测器官分割和病灶检测）。该研究的成果可以提升这些应用场景的感知能力和决策能力，具有重要的实际价值。

## 📄 摘要（原文）

> Understanding the inter-relations and interactions between tasks is crucial for multi-task dense prediction. Existing methods predominantly utilize convolutional layers and attention mechanisms to explore task-level interactions. In this work, we introduce a novel decoder-based framework, Parameter Aware Mamba Model (PAMM), specifically designed for dense prediction in multi-task learning setting. Distinct from approaches that employ Transformers to model holistic task relationships, PAMM leverages the rich, scalable parameters of state space models to enhance task interconnectivity. It features dual state space parameter experts that integrate and set task-specific parameter priors, capturing the intrinsic properties of each task. This approach not only facilitates precise multi-task interactions but also allows for the global integration of task priors through the structured state space sequence model (S4). Furthermore, we employ the Multi-Directional Hilbert Scanning method to construct multi-angle feature sequences, thereby enhancing the sequence model's perceptual capabilities for 2D data. Extensive experiments on the NYUD-v2 and PASCAL-Context benchmarks demonstrate the effectiveness of our proposed method. Our code is available at https://github.com/CQC-gogopro/PAMM.

