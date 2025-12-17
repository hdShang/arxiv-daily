---
layout: default
title: IPR-1: Interactive Physical Reasoner
---

# IPR-1: Interactive Physical Reasoner

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15407" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15407</a>
  <a href="https://arxiv.org/pdf/2511.15407.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15407" onclick="toggleFavorite(this, '2511.15407', 'IPR-1: Interactive Physical Reasoner')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyu Zhang, Lifeng Zhuo, Tianxi Tan, Guocan Xie, Xian Nie, Yan Li, Renjie Zhao, Zizhu He, Ziyu Wang, Jiting Cai, Yong-Lu Li

**分类**: cs.AI, cs.CV, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出IPR：结合世界模型与VLM的交互式物理推理器，解决复杂物理场景推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `物理推理` `交互学习` `世界模型` `视觉语言模型` `强化学习` `动作编码` `机器人控制`

## 📋 核心要点

1. 现有VLM和世界模型在复杂物理场景中推理能力不足，前者缺乏前瞻性，后者过度依赖视觉模仿。
2. IPR结合世界模型rollout和VLM策略，利用PhysCode对齐语义意图与动力学，提升推理能力。
3. 实验表明，IPR在G2U基准上表现出色，超越GPT-5，并具备零样本迁移能力，验证了物理交互的有效性。

## 📝 摘要（中文）

本文旨在研究智能体能否通过与环境的交互学习，并不断积累经验，从而获得类似人类的推理能力。为此，作者提出了一个名为Game-to-Unseen (G2U)的基准测试，包含1000多个具有显著视觉领域差异的异构游戏。现有的方法，包括视觉语言模型(VLM)和世界模型，难以捕捉潜在的物理规律和因果关系，因为它们过度关注视觉细节而非核心机制。VLM/VLA智能体擅长推理，但在交互环境中缺乏前瞻性；而世界模型擅长想象，但模仿的是视觉模式，而非分析物理和因果关系。因此，作者提出了交互式物理推理器(IPR)，它使用世界模型的rollout来评估和强化VLM的策略，并引入了PhysCode，一种以物理为中心的动作编码，将语义意图与动力学对齐，为预测和推理提供共享的动作空间。IPR在1000多个游戏上进行预训练后，在从原始直觉到目标驱动推理的各个层面上表现出强大的鲁棒性，甚至在整体上超过了GPT-5。研究表明，性能随着训练游戏和交互步骤的增加而提高，并且该模型还可以零样本迁移到未见过的游戏。这些结果支持以物理为中心的交互作为稳步提高物理推理能力的一种途径。

## 🔬 方法详解

**问题定义**：现有方法，如视觉语言模型（VLM）和世界模型，在处理复杂物理交互场景时存在局限性。VLM虽然擅长推理，但在交互环境中缺乏长远规划能力，无法进行有效的“look-ahead”；而世界模型虽然能够进行预测和想象，但往往侧重于模仿视觉模式，而非真正理解和利用物理规律和因果关系。因此，如何让智能体像人类一样，通过交互学习并掌握物理世界的内在规律，是一个亟待解决的问题。

**核心思路**：IPR的核心思路是结合VLM的推理能力和世界模型的预测能力，通过相互协作来提升整体的物理推理性能。具体来说，IPR利用世界模型进行rollout，预测未来可能发生的状态，并以此来评估和指导VLM的策略选择。同时，引入PhysCode作为一种以物理为中心的动作编码，将语义意图与动力学行为对齐，从而为预测和推理提供一个统一的动作空间。

**技术框架**：IPR的整体框架包含以下几个主要模块：1) VLM策略模块：负责根据当前环境状态生成动作策略；2) 世界模型模块：负责根据当前状态和动作预测未来的状态序列（rollout）；3) 策略评估模块：利用世界模型的rollout结果，对VLM的策略进行评估和打分；4) 策略强化模块：根据策略评估结果，对VLM的策略进行优化和调整；5) PhysCode模块：负责将高层语义意图转化为具体的物理动作指令，并作为VLM和世界模型之间的桥梁。

**关键创新**：IPR最重要的创新点在于其融合了VLM和世界模型的优势，并引入了PhysCode作为统一的动作空间。这种融合使得IPR既能够进行有效的推理，又能够进行长期的规划，从而在复杂物理交互场景中表现出更强的鲁棒性和泛化能力。与现有方法相比，IPR更加注重对物理规律和因果关系的理解和利用，而非仅仅依赖于视觉模式的模仿。

**关键设计**：PhysCode的设计是IPR的关键。它将动作空间分解为多个物理相关的参数，例如作用力的大小、方向、作用点等。通过对这些参数进行编码，PhysCode能够将高层语义意图转化为具体的物理动作指令，并为VLM和世界模型提供一个共享的动作空间。此外，IPR还采用了强化学习算法来优化VLM的策略，并使用对比学习方法来训练世界模型，使其能够更准确地预测未来的状态序列。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.15407/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.15407/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.15407/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，IPR在G2U基准测试中取得了显著的性能提升，甚至在整体上超过了GPT-5。具体来说，IPR在多个游戏任务上都取得了最高的得分，并且表现出强大的鲁棒性和泛化能力。此外，研究还发现，IPR的性能随着训练游戏数量和交互步骤的增加而不断提高，并且能够零样本迁移到未见过的游戏，这充分证明了IPR的有效性和潜力。

## 🎯 应用场景

IPR的研究成果具有广泛的应用前景，例如可以应用于机器人控制、游戏AI、自动驾驶等领域。通过让智能体具备更强的物理推理能力，可以使其在复杂环境中更好地完成任务，并实现更高级别的自主性和智能化。此外，IPR还可以用于教育领域，帮助学生更好地理解物理概念和规律。

## 📄 摘要（原文）

> Humans learn by observing, interacting with environments, and internalizing physics and causality. Here, we aim to ask whether an agent can similarly acquire human-like reasoning from interaction and keep improving with more experience. To study this, we introduce a Game-to-Unseen (G2U) benchmark of 1,000+ heterogeneous games that exhibit significant visual domain gaps. Existing approaches, including VLMs and world models, struggle to capture underlying physics and causality since they are not focused on core mechanisms and overfit to visual details. VLM/VLA agents reason but lack look-ahead in interactive settings, while world models imagine but imitate visual patterns rather than analyze physics and causality. We therefore propose IPR (Interactive Physical Reasoner), using world-model rollouts to score and reinforce a VLM's policy, and introduce PhysCode, a physics-centric action code aligning semantic intent with dynamics to provide a shared action space for prediction and reasoning. Pretrained on 1,000+ games, our IPR performs robustly on levels from primitive intuition to goal-driven reasoning, and even surpasses GPT-5 overall. We find that performance improves with more training games and interaction steps, and that the model also zero-shot transfers to unseen games. These results support physics-centric interaction as a path to steadily improving physical reasoning. Further demos and project details can be found atthis https URL.

