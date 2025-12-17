---
layout: default
title: ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL
---

# ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07151" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07151v1</a>
  <a href="https://arxiv.org/pdf/2510.07151.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07151v1" onclick="toggleFavorite(this, '2510.07151v1', 'ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Egor Cherepanov, Alexey K. Kovalev, Aleksandr I. Panov

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-10-08

**备注**: 22 pages, 7 figures

---

## 💡 一句话要点

**ELMUR：利用外部层记忆和更新/重写机制，解决长时程强化学习问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `长时程强化学习` `外部记忆` `Transformer` `层局部记忆` `机器人控制`

## 📋 核心要点

1. 现有强化学习方法难以有效利用长期历史信息，导致在部分可观测和长时程任务中表现不佳。
2. ELMUR通过引入层局部外部记忆，并结合更新/重写机制，显著提升了模型对长期依赖关系的建模能力。
3. 实验表明，ELMUR在多个复杂任务中显著优于现有基线模型，验证了其在长时程强化学习中的有效性。

## 📝 摘要（中文）

本文提出了一种名为ELMUR（External Layer Memory with Update/Rewrite）的Transformer架构，用于解决部分可观测和长时程强化学习问题。ELMUR采用结构化的外部记忆，每一层都维护记忆嵌入，并通过双向交叉注意力机制与记忆嵌入交互，然后使用最近最少使用（LRU）的记忆模块，通过替换或凸混合的方式更新记忆。ELMUR能够将有效时程扩展到注意力窗口的10万倍，并在一个走廊长度高达百万步的合成T型迷宫任务中实现了100%的成功率。在POPGym中，ELMUR在超过一半的任务中优于基线模型。在MIKASA-Robo稀疏奖励的视觉操作任务中，ELMUR的性能几乎是强大基线模型的两倍。实验结果表明，结构化的层局部外部记忆为部分可观测下的决策提供了一种简单且可扩展的方法。

## 🔬 方法详解

**问题定义**：现实世界的机器人需要在部分可观测和长时程的环境中行动，关键线索可能在影响决策之前很久就出现。然而，大多数现代方法仅依赖于瞬时信息，而没有结合过去的经验。标准的循环神经网络或Transformer模型难以保留和利用长期依赖关系：上下文窗口会截断历史信息，而简单的记忆扩展方法在规模和稀疏性方面表现不佳。

**核心思路**：ELMUR的核心思路是为Transformer的每一层引入一个结构化的外部记忆模块。该模块允许每一层存储和检索与该层相关的长期信息，从而缓解了传统Transformer的上下文窗口限制。通过层局部记忆，模型可以更有效地学习和利用不同时间尺度上的信息。

**技术框架**：ELMUR基于Transformer架构，并在每一层添加了外部记忆模块。整体流程如下：1) 输入经过Transformer层处理；2) 每一层通过双向交叉注意力机制与外部记忆交互，提取相关信息；3) 使用LRU记忆模块更新外部记忆，可以选择替换或凸混合的方式。这种结构使得每一层都能维护自己的记忆表示，并根据当前输入动态更新。

**关键创新**：ELMUR的关键创新在于其结构化的层局部外部记忆。与全局共享的外部记忆相比，层局部记忆允许每一层学习和维护特定于该层的信息，从而提高了记忆的利用效率和模型的表达能力。此外，使用LRU机制进行记忆更新，保证了记忆模块能够存储最近最相关的信息。

**关键设计**：ELMUR的关键设计包括：1) 双向交叉注意力机制，用于在每一层提取与当前输入相关的记忆信息；2) LRU记忆模块，用于更新外部记忆，可以选择替换或凸混合的方式；3) 每一层维护独立的记忆嵌入，允许模型学习不同时间尺度上的信息。具体的参数设置和网络结构细节在论文中有详细描述，但摘要中未明确提及。

## 📊 实验亮点

ELMUR在合成T型迷宫任务中，走廊长度高达百万步时，实现了100%的成功率，有效时程扩展到注意力窗口的10万倍。在POPGym中，ELMUR在超过一半的任务中优于基线模型。在MIKASA-Robo稀疏奖励的视觉操作任务中，ELMUR的性能几乎是强大基线模型的两倍。这些结果表明，ELMUR在长时程强化学习任务中具有显著优势。

## 🎯 应用场景

ELMUR适用于需要长期记忆和推理的机器人控制、游戏AI、自动驾驶等领域。例如，在复杂环境中导航的机器人需要记住之前的路径和遇到的障碍物；在游戏中，AI需要记住玩家的行为模式和游戏状态。ELMUR的出现，有望提升这些应用场景中智能体的决策能力和适应性。

## 📄 摘要（原文）

> Real-world robotic agents must act under partial observability and long horizons, where key cues may appear long before they affect decision making. However, most modern approaches rely solely on instantaneous information, without incorporating insights from the past. Standard recurrent or transformer models struggle with retaining and leveraging long-term dependencies: context windows truncate history, while naive memory extensions fail under scale and sparsity. We propose ELMUR (External Layer Memory with Update/Rewrite), a transformer architecture with structured external memory. Each layer maintains memory embeddings, interacts with them via bidirectional cross-attention, and updates them through an Least Recently Used (LRU) memory module using replacement or convex blending. ELMUR extends effective horizons up to 100,000 times beyond the attention window and achieves a 100% success rate on a synthetic T-Maze task with corridors up to one million steps. In POPGym, it outperforms baselines on more than half of the tasks. On MIKASA-Robo sparse-reward manipulation tasks with visual observations, it nearly doubles the performance of strong baselines. These results demonstrate that structured, layer-local external memory offers a simple and scalable approach to decision making under partial observability.

