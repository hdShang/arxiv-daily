---
layout: default
title: "Ella: Embodied Social Agents with Lifelong Memory"
---

# Ella: Embodied Social Agents with Lifelong Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24019" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24019v1</a>
  <a href="https://arxiv.org/pdf/2506.24019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24019v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24019v1', 'Ella: Embodied Social Agents with Lifelong Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongxin Zhang, Zheyuan Zhang, Zeyuan Wang, Zunzhe Zhang, Lixing Fang, Qinhong Zhou, Chuang Gan

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-30

**🔗 代码/项目**: [PROJECT_PAGE](https://umass-embodied-agi.github.io/Ella/)

---

## 💡 一句话要点

**提出Ella以解决社交智能体的终身学习问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社交智能体` `终身学习` `多模态记忆` `开放世界` `自主进化` `深度学习` `语义记忆` `情节记忆`

## 📋 核心要点

1. 现有社交智能体在动态环境中缺乏长期记忆能力，难以有效学习和适应复杂的社交场景。
2. Ella通过构建一个结构化的多模态记忆系统，整合语义记忆和情节记忆，实现了终身学习和自主进化。
3. 实验结果显示，Ella在与其他智能体的互动中表现出色，能够有效影响和合作，提升了社交智能体的学习能力。

## 📝 摘要（中文）

我们介绍了Ella，一个能够在3D开放世界中进行终身学习的具身社交智能体。Ella通过日常视觉观察和社交互动积累经验并获取知识。其核心是一个结构化的长期多模态记忆系统，能够有效存储、更新和检索信息。该系统包括以名称为中心的语义记忆和捕捉多模态经验的时空情节记忆。通过将这一终身记忆系统与基础模型相结合，Ella能够为决策提供相关信息，规划日常活动，建立社交关系，并在与其他智能生物共存的过程中自主进化。实验结果表明，Ella能够有效影响、引导和合作其他智能体以实现目标，展示了通过观察和社交互动进行有效学习的能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有社交智能体在动态环境中缺乏长期记忆和学习能力的问题。现有方法往往无法有效处理复杂的社交互动和环境变化，导致智能体的适应性不足。

**核心思路**：Ella的核心思路是构建一个结构化的长期多模态记忆系统，结合语义记忆和情节记忆，以支持智能体在开放世界中的终身学习和自主决策。这样的设计使得智能体能够更好地组织和利用其经验。

**技术框架**：Ella的整体架构包括两个主要模块：名称中心的语义记忆用于组织知识，时空情节记忆用于捕捉多模态经验。通过与基础模型的集成，Ella能够在社交互动中检索和应用相关信息。

**关键创新**：Ella的关键创新在于其多模态记忆系统的结构化设计，使得智能体能够在复杂的社交环境中有效学习和适应。这一设计与传统的单一记忆模型有本质区别，提供了更强的灵活性和适应性。

**关键设计**：在技术细节上，Ella的记忆系统通过动态更新机制来维护信息的时效性，并采用特定的损失函数来优化记忆的存储和检索效率。网络结构方面，Ella结合了深度学习模型，以增强其学习能力和决策能力。

## 📊 实验亮点

实验结果表明，Ella在与15个智能体的社交活动中表现优异，能够有效影响和引导其他智能体，达成共同目标。与基线模型相比，Ella在社交互动中的学习效率提升显著，展示了其在动态环境中的适应能力。

## 🎯 应用场景

Ella的研究成果具有广泛的应用潜力，特别是在社交机器人、虚拟助手和智能游戏等领域。通过提升智能体的社交能力和学习能力，Ella可以在多种场景中提供更自然和有效的交互体验，未来可能推动人机协作和智能体的自主发展。

## 📄 摘要（原文）

> We introduce Ella, an embodied social agent capable of lifelong learning within a community in a 3D open world, where agents accumulate experiences and acquire knowledge through everyday visual observations and social interactions. At the core of Ella's capabilities is a structured, long-term multimodal memory system that stores, updates, and retrieves information effectively. It consists of a name-centric semantic memory for organizing acquired knowledge and a spatiotemporal episodic memory for capturing multimodal experiences. By integrating this lifelong memory system with foundation models, Ella retrieves relevant information for decision-making, plans daily activities, builds social relationships, and evolves autonomously while coexisting with other intelligent beings in the open world. We conduct capability-oriented evaluations in a dynamic 3D open world where 15 agents engage in social activities for days and are assessed with a suite of unseen controlled evaluations. Experimental results show that Ella can influence, lead, and cooperate with other agents well to achieve goals, showcasing its ability to learn effectively through observation and social interaction. Our findings highlight the transformative potential of combining structured memory systems with foundation models for advancing embodied intelligence. More videos can be found at https://umass-embodied-agi.github.io/Ella/.

