---
layout: default
title: RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback
---

# RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19767" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19767v1</a>
  <a href="https://arxiv.org/pdf/2505.19767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19767v1', 'RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyang Shu, Zhiwei Lin, Yongtao Wang

**分类**: cs.RO

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出RFTF以解决现有强化微调方法稀疏奖励问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `具身智能` `奖励机制` `价值模型` `任务执行` `适应能力` `微调技术`

## 📋 核心要点

1. 现有的强化微调方法依赖稀疏奖励，难以提供细粒度的反馈，限制了智能体的操作能力和泛化性能。
2. RFTF通过引入价值模型生成密集奖励，利用时间信息进行训练，减少对昂贵标签的依赖。
3. 实验表明，RFTF显著提升了具身智能体的表现，在CALVIN任务上取得了新的成功长度记录，并能快速适应新环境。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在具身智能领域展现出显著潜力，使得智能体能够遵循人类指令在物理环境中完成复杂任务。现有的具身智能体通常通过行为克隆进行训练，这需要昂贵的数据和计算资源，并受到人类示范的限制。为了解决这一问题，许多研究者探索将强化微调应用于具身智能体。然而，典型的强化微调方法通常依赖稀疏的基于结果的奖励，这限制了模型在特定动作上的反馈能力，从而影响其操作能力和泛化性能。本文提出了一种新颖的强化微调方法RFTF，利用价值模型在具身场景中生成密集奖励，消除了对昂贵机器人动作标签的需求，并通过GAE和样本平衡等技术增强微调效果。实验结果表明，使用RFTF微调的具身智能体在CALVIN ABC-D任务上取得了新的最先进性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化微调方法中稀疏奖励的问题，这种方法难以提供针对特定动作的细粒度反馈，限制了智能体的操作能力和泛化性能。

**核心思路**：RFTF的核心思路是利用价值模型生成密集奖励，通过时间信息的引入，消除对昂贵机器人动作标签的需求，从而提高微调效果。

**技术框架**：RFTF的整体架构包括价值模型的训练、奖励生成和微调过程。首先，价值模型利用时间信息进行训练，然后生成密集奖励，最后通过强化学习算法进行微调。

**关键创新**：RFTF的主要创新在于通过价值模型生成密集奖励，解决了传统方法中稀疏奖励的局限性。这一设计使得智能体能够获得更细致的反馈，从而提升操作能力和泛化性能。

**关键设计**：在RFTF中，采用了GAE（广义优势估计）和样本平衡等技术，以增强微调过程的有效性。此外，模型的训练过程中不再依赖昂贵的动作标签，降低了训练成本。

## 📊 实验亮点

实验结果显示，使用RFTF微调的具身智能体在CALVIN ABC-D任务上取得了平均成功长度4.296，超越了以往的最先进性能。此外，在新环境D中，经过少量的微调后，成功长度达到了4.301，展现了快速适应能力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动化任务执行和人机交互等。通过提升具身智能体的操作能力和适应性，RFTF可以在复杂的物理环境中实现更高效的任务执行，具有重要的实际价值和广泛的应用前景。未来，RFTF有望推动智能体在动态环境中的自主学习和适应能力的进一步提升。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have demonstrated significant potential in the field of embodied intelligence, enabling agents to follow human instructions to complete complex tasks in physical environments. Existing embodied agents are often trained through behavior cloning, which requires expensive data and computational resources and is constrained by human demonstrations. To address this issue, many researchers explore the application of reinforcement fine-tuning to embodied agents. However, typical reinforcement fine-tuning methods for embodied agents usually rely on sparse, outcome-based rewards, which struggle to provide fine-grained feedback for specific actions within an episode, thus limiting the model's manipulation capabilities and generalization performance. In this paper, we propose RFTF, a novel reinforcement fine-tuning method that leverages a value model to generate dense rewards in embodied scenarios. Specifically, our value model is trained using temporal information, eliminating the need for costly robot action labels. In addition, RFTF incorporates a range of techniques, such as GAE and sample balance to enhance the effectiveness of the fine-tuning process. By addressing the sparse reward problem in reinforcement fine-tuning, our method significantly improves the performance of embodied agents, delivering superior generalization and adaptation capabilities across diverse embodied tasks. Experimental results show that embodied agents fine-tuned with RFTF achieve new state-of-the-art performance on the challenging CALVIN ABC-D with an average success length of 4.296. Moreover, RFTF enables rapid adaptation to new environments. After fine-tuning in the D environment of CALVIN for a few episodes, RFTF achieved an average success length of 4.301 in this new environment.

