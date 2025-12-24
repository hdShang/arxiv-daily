---
layout: default
title: "OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation"
---

# OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19480" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19480v1</a>
  <a href="https://arxiv.org/pdf/2509.19480.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19480v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19480v1', 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Noriaki Hirose, Catherine Glossop, Dhruv Shah, Sergey Levine

**分类**: cs.RO, cs.LG

**发布日期**: 2025-09-23

**备注**: 9 pages, 7 figures, 6 tables

---

## 💡 一句话要点

**OmniVLA：用于机器人导航的通用模态视觉-语言-动作模型**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人导航` `多模态学习` `视觉语言动作模型` `通用模态` `随机模态融合`

## 📋 核心要点

1. 现有机器人导航策略大多基于单一模态训练，限制了其在真实场景中的适应性，难以灵活组合语言、坐标或视觉参考等目标。
2. OmniVLA利用高容量VLA骨干网络，通过随机模态融合策略，结合2D姿势、图像和自然语言等多种模态进行训练。
3. OmniVLA在未见环境中表现出强大的泛化能力，对模态缺失具有鲁棒性，并能理解新的自然语言指令，优于单模态基线。

## 📝 摘要（中文）

本文提出了一种用于机器人基础模型的训练框架，该框架支持基于视觉的导航的通用模态目标条件。该方法利用高容量的视觉-语言-动作（VLA）骨干网络，并通过随机模态融合策略，使用三种主要目标模态（2D姿势、自我中心图像和自然语言）及其组合进行训练。这种设计不仅扩展了可用数据集的范围，还鼓励策略发展更丰富的几何、语义和视觉表示。由此产生的模型OmniVLA，实现了对未见环境的强大泛化能力，对稀缺模态的鲁棒性，以及遵循新的自然语言指令的能力。实验表明，OmniVLA在各种模态上优于专业基线，并为微调到新的模态和任务提供了灵活的基础。OmniVLA为广泛通用和灵活的导航策略以及构建通用模态机器人基础模型的可扩展路径提供了一个方向。

## 🔬 方法详解

**问题定义**：现有机器人导航策略通常针对单一模态目标进行训练，例如仅依赖图像、语言或坐标。这限制了它们在真实世界中的应用，因为人类通常可以灵活地组合多种模态的信息来指导导航。因此，如何构建一个能够理解和融合多种模态目标信息的通用导航模型是一个关键问题。

**核心思路**：本文的核心思路是训练一个能够接受多种模态输入（包括2D姿势、自我中心图像和自然语言）的视觉-语言-动作（VLA）模型。通过随机模态融合策略，模型可以学习到不同模态之间的关联性，并能够根据可用的模态信息进行导航。这种设计使得模型能够更好地适应真实世界的复杂场景，并提高其泛化能力。

**技术框架**：OmniVLA模型采用一个高容量的VLA骨干网络。训练过程中，模型接收2D姿势、自我中心图像和自然语言指令作为输入，并通过一个随机模态融合模块将这些信息融合在一起。融合后的信息被输入到策略网络中，策略网络输出机器人的动作指令。整个框架采用端到端的方式进行训练。

**关键创新**：OmniVLA的关键创新在于其通用模态目标条件设计和随机模态融合策略。与以往的单模态导航模型不同，OmniVLA能够同时处理多种模态的输入，并学习到它们之间的关联性。随机模态融合策略鼓励模型学习更鲁棒的表示，使其能够适应不同模态信息缺失的情况。

**关键设计**：在训练过程中，作者采用了随机模态融合策略，即随机选择输入模态的组合。这种策略可以有效地防止模型过度依赖于单一模态，并鼓励模型学习更通用的表示。损失函数的设计也至关重要，需要平衡不同模态之间的贡献，并确保模型能够准确地执行导航任务。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

OmniVLA在未见环境中表现出强大的泛化能力，显著优于单模态基线。实验结果表明，OmniVLA能够成功地遵循新的自然语言指令，并且对模态缺失具有很强的鲁棒性。具体性能数据和对比结果可在论文的实验部分找到。

## 🎯 应用场景

OmniVLA具有广泛的应用前景，可用于家庭服务机器人、自动驾驶汽车、无人机等领域。该模型能够理解多种形式的目标指令，并适应不同的环境条件，从而提高机器人的自主性和智能化水平。未来，OmniVLA可以进一步扩展到更多的模态和任务，成为通用机器人平台的基础。

## 📄 摘要（原文）

> Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

