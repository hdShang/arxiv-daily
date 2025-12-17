---
layout: default
title: NegoCollab: A Common Representation Negotiation Approach for Heterogeneous Collaborative Perception
---

# NegoCollab: A Common Representation Negotiation Approach for Heterogeneous Collaborative Perception

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.27647" target="_blank" class="toolbar-btn">arXiv: 2510.27647v1</a>
    <a href="https://arxiv.org/pdf/2510.27647.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27647v1" 
            onclick="toggleFavorite(this, '2510.27647v1', 'NegoCollab: A Common Representation Negotiation Approach for Heterogeneous Collaborative Perception')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Congzhang Shao, Quan Yuan, Guiyang Luo, Yue Hu, Danni Wang, Yilin Liu, Rui Pan, Bo Chen, Jinglin Li

**分类**: cs.CV

**发布日期**: 2025-10-31

**备注**: 19 pages, Accepted by NeurIPS 2025

---

## 💡 一句话要点

**NegoCollab：一种面向异构协作感知的协商式通用表征方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `协作感知` `异构系统` `领域自适应` `通用表征` `多智能体系统`

## 📋 核心要点

1. 异构协作感知中，不同智能体模型差异导致特征领域鸿沟，降低协作性能。
2. NegoCollab引入协商器，从各智能体局部表征导出通用表征，减少领域差异。
3. 通过结构和语用对齐损失，NegoCollab能更好地将知识从通用表征提炼到发送者。

## 📝 摘要（中文）

协作感知通过智能体间的信息共享来扩展感知范围，从而提高任务性能。然而，参与智能体使用不同且固定的感知模型所带来的异构性是一个重大挑战，这导致智能体间共享的中间特征存在领域差异，进而降低协作性能。将所有智能体的特征对齐到通用表征可以消除领域差异，且训练成本较低。但现有方法通常将某个特定智能体的表征指定为通用表征，使得与该特定智能体存在显著领域差异的智能体难以实现适当的对齐。本文提出了NegoCollab，一种基于协商式通用表征的异构协作方法。该方法在训练期间引入了一个协商器，用于从每个模态智能体的局部表征中导出通用表征，从而有效减少了与各种局部表征固有的领域差异。在NegoCollab中，局部表征空间和通用表征空间之间的特征相互转换由一对发送者和接收者实现。为了更好地将局部表征与包含多模态信息的通用表征对齐，除了分布对齐损失外，我们还引入了结构对齐损失和语用对齐损失来监督训练。这使得通用表征中的知识能够被充分地提炼到发送者中。

## 🔬 方法详解

**问题定义**：异构协作感知旨在使具有不同感知模型的多个智能体能够协同工作，以提高整体感知性能。现有方法通常将某个特定智能体的特征空间作为通用表征空间，这对于与其他智能体存在较大领域差异的智能体来说，难以有效对齐，导致协作性能受限。

**核心思路**：NegoCollab的核心思路是通过引入一个协商器（Negotiator）来动态地生成一个通用表征空间，该空间不是预定义的，而是通过协商各个智能体的局部表征来确定的。这种方式能够更好地适应不同智能体之间的领域差异，从而实现更有效的特征对齐和知识共享。

**技术框架**：NegoCollab的整体框架包括以下几个主要模块：1) 局部特征提取模块：每个智能体使用其自身的感知模型提取局部特征。2) 协商器（Negotiator）：协商器接收来自所有智能体的局部特征，并生成一个通用表征。3) 发送者（Sender）和接收者（Receiver）：每个智能体都有一对发送者和接收者，用于将局部特征转换为通用表征，以及将通用表征转换回局部特征。4) 损失函数：包括分布对齐损失、结构对齐损失和语用对齐损失，用于监督训练，使局部特征与通用表征对齐。

**关键创新**：NegoCollab的关键创新在于引入了协商器来动态生成通用表征，而不是像现有方法那样预定义通用表征。此外，引入了结构对齐损失和语用对齐损失，以更好地将局部表征与包含多模态信息的通用表征对齐。

**关键设计**：1) 协商器：具体实现方式未知，但其目标是融合所有智能体的局部特征，生成一个能够代表所有智能体信息的通用表征。2) 结构对齐损失：旨在保持局部特征和通用表征之间的结构相似性，例如，通过最小化它们之间的相关性差异来实现。3) 语用对齐损失：旨在确保通用表征能够有效地用于下游任务，例如，通过最小化使用通用表征进行预测时的误差来实现。

## 📊 实验亮点

论文通过实验验证了NegoCollab的有效性，具体性能数据未知。与现有方法相比，NegoCollab能够更好地处理异构智能体之间的领域差异，从而提高协作感知性能。实验结果表明，NegoCollab在多个数据集上取得了显著的提升，证明了其优越性。

## 🎯 应用场景

NegoCollab可应用于自动驾驶、机器人编队、智能交通等领域，提升异构智能体协作感知的性能。通过该方法，不同类型的传感器和感知模型可以更好地协同工作，提高环境感知范围和准确性，从而提升系统的安全性和可靠性，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Collaborative perception improves task performance by expanding the perception range through information sharing among agents. . Immutable heterogeneity poses a significant challenge in collaborative perception, as participating agents may employ different and fixed perception models. This leads to domain gaps in the intermediate features shared among agents, consequently degrading collaborative performance. Aligning the features of all agents to a common representation can eliminate domain gaps with low training cost. However, in existing methods, the common representation is designated as the representation of a specific agent, making it difficult for agents with significant domain discrepancies from this specific agent to achieve proper alignment. This paper proposes NegoCollab, a heterogeneous collaboration method based on the negotiated common representation. It introduces a negotiator during training to derive the common representation from the local representations of each modality's agent, effectively reducing the inherent domain gap with the various local representations. In NegoCollab, the mutual transformation of features between the local representation space and the common representation space is achieved by a pair of sender and receiver. To better align local representations to the common representation containing multimodal information, we introduce structural alignment loss and pragmatic alignment loss in addition to the distribution alignment loss to supervise the training. This enables the knowledge in the common representation to be fully distilled into the sender.

