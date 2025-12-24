---
layout: default
title: "OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds"
---

# OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02322" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02322v1</a>
  <a href="https://arxiv.org/pdf/2509.02322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02322v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02322v1', 'OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Longrong Yang, Zhixiong Zeng, Yufeng Zhong, Jing Huang, Liming Zheng, Lei Chen, Haibo Qiu, Zequn Qin, Lin Ma, Xi Li

**分类**: cs.CV

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**OmniActor：一种用于2D和3D世界的通用GUI和具身智能体**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态智能体` `具身智能` `GUI交互` `混合专家模型` `迁移学习`

## 📋 核心要点

1. 现有智能体研究多集中于GUI或具身环境，忽略了复杂任务中两种环境的交替交互需求。
2. OmniActor通过层异构MoE结构，分离深层参数以消除GUI和具身数据的冲突，共享浅层参数以利用协同。
3. 实验表明，OmniActor在GUI和具身任务中均优于单独训练的智能体，尤其在GUI任务中提升显著。

## 📝 摘要（中文）

多模态大型语言模型正朝着能够主动执行任务的多模态智能体发展。目前，大多数智能体研究集中在GUI或具身场景，分别对应于与2D虚拟世界或3D真实世界交互的智能体。然而，许多复杂任务通常需要智能体交替地与这两种类型的环境进行交互。我们最初混合GUI和具身数据进行训练，但发现数据冲突导致性能下降。进一步分析表明，GUI和具身数据在浅层和深层分别表现出协同和冲突，这类似于人脑中的大脑-小脑机制。为此，我们从结构和数据角度设计了一种高性能的通用智能体OmniActor。首先，我们提出了层异构MoE，通过分离深层参数来消除GUI和具身数据之间的冲突，同时通过共享浅层参数来利用它们的协同作用。通过成功地利用协同作用并消除冲突，OmniActor在GUI或具身任务中优于仅由GUI或具身数据训练的智能体。此外，我们统一了GUI和具身任务的动作空间，并从各种来源收集了大规模的GUI和具身数据用于训练。这显著提高了OmniActor在不同场景下的性能，尤其是在GUI任务中。代码将公开提供。

## 🔬 方法详解

**问题定义**：现有智能体研究通常只关注GUI（2D虚拟世界）或具身（3D真实世界）环境中的单一任务，而忽略了现实世界中许多复杂任务需要智能体在两种环境中交替交互的需求。直接混合GUI和具身数据进行训练会导致性能下降，因为两种数据之间存在冲突。

**核心思路**：论文的核心思路是借鉴人脑的大脑-小脑机制，认为GUI和具身数据在浅层具有协同作用，而在深层存在冲突。因此，通过设计一种特殊的网络结构，使得浅层参数共享，深层参数分离，从而既能利用两种数据的协同作用，又能避免冲突。

**技术框架**：OmniActor的整体架构基于Transformer模型。关键在于引入了Layer-heterogeneity MoE（混合专家）结构。浅层Transformer块的参数在GUI和具身任务之间共享，而深层Transformer块则使用MoE，为GUI和具身任务分配不同的专家网络。此外，论文还统一了GUI和具身任务的动作空间，并收集了大规模的GUI和具身数据用于训练。

**关键创新**：最重要的技术创新点是Layer-heterogeneity MoE结构，它能够有效地消除GUI和具身数据之间的冲突，并利用它们的协同作用。与现有方法相比，OmniActor能够更好地处理需要在GUI和具身环境中交替交互的复杂任务。

**关键设计**：Layer-heterogeneity MoE的关键设计在于确定哪些层应该共享参数，哪些层应该使用MoE。论文通过实验发现，浅层共享参数，深层使用MoE能够获得最佳性能。此外，MoE中专家网络的数量也是一个重要的参数，需要根据具体任务进行调整。损失函数方面，使用了标准的交叉熵损失函数。

## 📊 实验亮点

OmniActor在GUI和具身任务中均取得了显著的性能提升。具体来说，在GUI任务中，OmniActor的性能超过了仅使用GUI数据训练的智能体。在具身任务中，OmniActor的性能也超过了仅使用具身数据训练的智能体。这表明OmniActor成功地利用了GUI和具身数据之间的协同作用，并消除了冲突。

## 🎯 应用场景

OmniActor具有广泛的应用前景，例如智能家居控制、远程协作机器人、游戏AI等。它可以应用于需要智能体在虚拟GUI界面和真实物理世界中进行交互的各种场景，例如用户可以通过GUI界面控制机器人完成复杂的任务，或者让机器人在真实世界中自主完成任务，并在必要时通过GUI界面与用户进行交互。

## 📄 摘要（原文）

> Multimodal large language models are evolving toward multimodal agents capable of proactively executing tasks. Most agent research focuses on GUI or embodied scenarios, which correspond to agents interacting with 2D virtual worlds or 3D real worlds, respectively. However, many complex tasks typically require agents to interleavely interact with these two types of environment. We initially mix GUI and embodied data to train, but find the performance degeneration brought by the data conflict. Further analysis reveals that GUI and embodied data exhibit synergy and conflict at the shallow and deep layers, respectively, which resembles the cerebrum-cerebellum mechanism in the human brain. To this end, we propose a high-performance generalist agent OmniActor, designed from both structural and data perspectives. First, we propose Layer-heterogeneity MoE to eliminate the conflict between GUI and embodied data by separating deep-layer parameters, while leverage their synergy by sharing shallow-layer parameters. By successfully leveraging the synergy and eliminating the conflict, OmniActor outperforms agents only trained by GUI or embodied data in GUI or embodied tasks. Furthermore, we unify the action spaces of GUI and embodied tasks, and collect large-scale GUI and embodied data from various sources for training. This significantly improves OmniActor under different scenarios, especially in GUI tasks. The code will be publicly available.

