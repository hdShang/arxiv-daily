---
layout: default
title: "FM4NPP: A Scaling Foundation Model for Nuclear and Particle Physics"
---

# FM4NPP: A Scaling Foundation Model for Nuclear and Particle Physics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14087" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14087v1</a>
  <a href="https://arxiv.org/pdf/2508.14087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14087v1', 'FM4NPP: A Scaling Foundation Model for Nuclear and Particle Physics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Park, Shuhang Li, Yi Huang, Xihaier Luo, Haiwang Yu, Yeonju Go, Christopher Pinkenburg, Yuewei Lin, Shinjae Yoo, Joseph Osborn, Jin Huang, Yihui Ren

**分类**: cs.LG, cs.AI, hep-ex

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出FM4NPP以解决粒子物理实验数据稀疏问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `粒子物理` `自监督学习` `基础模型` `数据稀疏` `多任务学习` `神经网络` `模型可扩展性`

## 📋 核心要点

1. 现有方法在处理粒子物理实验数据时面临稀疏性和空间分布的挑战，难以有效提取信息。
2. 论文提出了一种新颖的自监督训练方法，结合了大规模数据集和任务特定适配器，以提升模型的通用性和可扩展性。
3. 实验结果显示，所提出的基础模型在所有下游任务中均超越基线模型，且在数据高效适应性方面表现优异。

## 📝 摘要（中文）

大型语言模型通过自监督学习革命性地推动了人工智能的发展，激发了科学基础模型的研究。然而，将这一能力应用于实验粒子物理学面临挑战，因为探测器数据的稀疏性和空间分布特性与自然语言截然不同。本研究探讨了粒子物理学基础模型的可扩展性和通用性，提出了一个包含超过1100万粒子碰撞事件的新数据集及一系列下游任务和标注数据进行评估。我们提出了一种新颖的自监督训练方法，并展示了其神经可扩展性，模型参数高达1.88亿。通过冻结权重和任务特定适配器，该基础模型在所有下游任务中均优于基线模型，且表现出强大的数据高效适应能力。进一步分析表明，该模型提取的表示是任务无关的，但可以通过单一线性映射为不同下游任务进行专业化。

## 🔬 方法详解

**问题定义**：本研究旨在解决粒子物理实验数据的稀疏性和空间分布特性对模型训练的影响。现有方法在处理此类数据时，往往无法有效提取有用信息，导致性能不足。

**核心思路**：论文提出了一种新颖的自监督训练方法，利用大规模的粒子碰撞事件数据集，结合任务特定适配器，旨在提升模型的可扩展性和通用性。通过冻结权重并引入适配器，模型能够在不同任务间实现高效迁移学习。

**技术框架**：整体架构包括数据预处理、模型训练和任务适配三个主要模块。首先，利用新数据集进行自监督训练，接着通过冻结模型权重并添加适配器来适应不同下游任务，最后进行评估和优化。

**关键创新**：最重要的技术创新在于提出了一种适用于粒子物理数据的自监督训练方法，并结合任务特定适配器，使得模型在多任务学习中表现出色。这一方法与传统的单一任务训练方法有本质区别。

**关键设计**：在模型设计中，采用了高达1.88亿参数的神经网络结构，使用特定的损失函数来优化自监督学习过程，并通过线性映射实现任务适应性。

## 📊 实验亮点

实验结果表明，所提出的基础模型在所有下游任务中均优于基线模型，特别是在数据高效适应性方面表现突出，展示了强大的泛化能力和适应性，具体性能提升幅度未详细说明。

## 🎯 应用场景

该研究的潜在应用领域包括粒子物理实验数据分析、科学计算以及其他需要处理稀疏数据的领域。通过提升模型在复杂任务中的表现，未来可能推动粒子物理学的研究进展，并为相关领域的科学探索提供新的工具和方法。

## 📄 摘要（原文）

> Large language models have revolutionized artificial intelligence by enabling large, generalizable models trained through self-supervision. This paradigm has inspired the development of scientific foundation models (FMs). However, applying this capability to experimental particle physics is challenging due to the sparse, spatially distributed nature of detector data, which differs dramatically from natural language. This work addresses if an FM for particle physics can scale and generalize across diverse tasks. We introduce a new dataset with more than 11 million particle collision events and a suite of downstream tasks and labeled data for evaluation. We propose a novel self-supervised training method for detector data and demonstrate its neural scalability with models that feature up to 188 million parameters. With frozen weights and task-specific adapters, this FM consistently outperforms baseline models across all downstream tasks. The performance also exhibits robust data-efficient adaptation. Further analysis reveals that the representations extracted by the FM are task-agnostic but can be specialized via a single linear mapping for different downstream tasks.

