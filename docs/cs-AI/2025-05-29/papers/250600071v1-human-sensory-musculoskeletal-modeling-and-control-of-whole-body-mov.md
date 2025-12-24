---
layout: default
title: Human sensory-musculoskeletal modeling and control of whole-body movements
---

# Human sensory-musculoskeletal modeling and control of whole-body movements

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00071" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00071v1</a>
  <a href="https://arxiv.org/pdf/2506.00071.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00071v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00071v1', 'Human sensory-musculoskeletal modeling and control of whole-body movements')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenhui Zuo, Guohao Lin, Chen Zhang, Shanning Zhuang, Yanan Sui

**分类**: q-bio.NC, cs.AI, cs.RO

**发布日期**: 2025-05-29

---

## 💡 一句话要点

**提出SMS-Human模型以解决人类运动控制的多感官整合问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `感官-肌肉骨骼模型` `深度强化学习` `多模态输入` `运动控制` `人机交互` `动态模拟` `机器人技术`

## 📋 核心要点

1. 核心问题：现有方法在高维控制和多感官信息整合方面面临挑战，难以准确模拟人类运动行为。
2. 方法要点：提出SMS-Human模型，结合精确的解剖结构与多模态感官输入，采用深度强化学习框架进行控制。
3. 实验或效果：模拟了双足行走、物体操作和骑行等任务，结果显示模拟行为与自然行为高度一致，揭示了新的肌肉骨骼动态特征。

## 📝 摘要（中文）

协调的人类运动依赖于多感官输入、传感器运动转换和运动执行，以及来自身体与环境交互的感官反馈。构建感官-肌肉骨骼系统的动态模型对于理解运动控制和研究人类行为至关重要。本文提出了一种名为SMS-Human的人类感官-肌肉骨骼模型，整合了骨骼、关节和肌腱单元的精确解剖表示，以及视觉、前庭、感觉和触觉等多模态感官输入。我们开发了一个分阶段的层次深度强化学习框架，以应对肌肉骨骼系统中高维控制的固有挑战。通过该框架，我们模拟了三种代表性运动任务，包括双足行走、视觉引导的物体操作和骑自行车的人机交互。结果显示自然与模拟的人类运动行为之间高度相似，模拟还揭示了无法直接测量的肌肉骨骼动态。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效整合多感官输入以控制复杂的人类运动。现有方法在处理高维控制和多模态信息时存在局限，难以真实模拟人类的运动行为。

**核心思路**：论文提出的SMS-Human模型通过精确的解剖表示和多模态感官输入的结合，利用深度强化学习框架来实现对肌肉骨骼系统的高效控制。这种设计旨在提高模型对复杂运动的适应性和准确性。

**技术框架**：整体架构包括三个主要模块：1) 感官输入模块，整合视觉、前庭、感觉和触觉信息；2) 动态模型模块，基于解剖结构建立肌肉骨骼系统的动态模型；3) 控制模块，采用分阶段的层次深度强化学习进行运动控制。

**关键创新**：最重要的创新在于将多模态感官信息与精确的肌肉骨骼解剖模型结合，形成了一个新的动态模型，显著提升了对复杂运动的模拟能力。与现有方法相比，该模型在处理高维控制时表现出更高的灵活性和准确性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化运动控制效果，并通过层次化的学习策略来逐步提升模型的性能。网络结构方面，结合了深度学习的优势，以适应多样化的运动任务。

## 📊 实验亮点

实验结果表明，SMS-Human模型在模拟双足行走、物体操作和骑行等任务时，表现出与自然人类运动行为的高度一致性。模型的动态特征揭示了无法直接测量的肌肉骨骼动态，展示了在高维控制任务中的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、虚拟现实、运动康复和人机交互等。通过深入理解人类运动的感知和控制机制，可以为设计具有更高智能的交互系统提供理论基础，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Coordinated human movement depends on the integration of multisensory inputs, sensorimotor transformation, and motor execution, as well as sensory feedback resulting from body-environment interaction. Building dynamic models of the sensory-musculoskeletal system is essential for understanding movement control and investigating human behaviours. Here, we report a human sensory-musculoskeletal model, termed SMS-Human, that integrates precise anatomical representations of bones, joints, and muscle-tendon units with multimodal sensory inputs involving visual, vestibular, proprioceptive, and tactile components. A stage-wise hierarchical deep reinforcement learning framework was developed to address the inherent challenges of high-dimensional control in musculoskeletal systems with integrated multisensory information. Using this framework, we demonstrated the simulation of three representative movement tasks, including bipedal locomotion, vision-guided object manipulation, and human-machine interaction during bicycling. Our results showed a close resemblance between natural and simulated human motor behaviours. The simulation also revealed musculoskeletal dynamics that could not be directly measured. This work sheds deeper insights into the sensorimotor dynamics of human movements, facilitates quantitative understanding of human behaviours in interactive contexts, and informs the design of systems with embodied intelligence.

