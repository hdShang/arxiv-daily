---
layout: default
title: "EDEN: Entorhinal Driven Egocentric Navigation Toward Robotic Deployment"
---

# EDEN: Entorhinal Driven Egocentric Navigation Toward Robotic Deployment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03046" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03046v1</a>
  <a href="https://arxiv.org/pdf/2506.03046.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03046v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03046v1', 'EDEN: Entorhinal Driven Egocentric Navigation Toward Robotic Deployment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mikolaj Walczak, Romina Aalishah, Wyatt Mackey, Brittany Story, David L. Boothe, Nicholas Waytowich, Xiaomin Lin, Tinoosh Mohsenin

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-03

---

## 💡 一句话要点

**提出EDEN框架以解决深度强化学习导航的脆弱性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `深度强化学习` `自主导航` `生物启发` `网格细胞` `机器人技术` `视觉传感器` `运动传感器` `PPO算法`

## 📋 核心要点

1. 现有的深度强化学习方法在动态和复杂环境中表现出脆弱性，难以适应变化的导航任务。
2. EDEN框架通过生物启发的网格细胞编码器，将传感器数据转化为可解释的空间表示，结合强化学习实现自主导航。
3. 实验结果显示，EDEN在简单场景中成功率达到99%，在复杂环境中超过94%，显著优于使用原始状态输入的基线代理。

## 📝 摘要（中文）

深度强化学习代理通常在面对变化场景时表现脆弱，而人类则展现出适应性和灵活性。为了解决这一问题，本文提出了EDEN，一个生物启发的导航框架，结合了学习的内嗅皮层网格细胞表示和强化学习，以实现自主导航。EDEN允许代理使用视觉和运动传感器数据进行路径积分和基于向量的导航。核心是网格细胞编码器，将自我中心运动转化为周期性空间编码，生成低维且可解释的位置嵌入。通过在MiniWorld和Gazebo模拟器中评估，EDEN在简单场景中实现了99%的成功率，在复杂平面图中也超过94%。

## 🔬 方法详解

**问题定义**：本文旨在解决深度强化学习代理在动态环境中的脆弱性，现有方法多依赖于原始状态输入，缺乏有效的空间表示能力。

**核心思路**：EDEN框架通过模仿生物内嗅皮层的导航机制，利用网格细胞编码器将运动数据转化为周期性空间编码，从而提高导航的灵活性和适应性。

**技术框架**：EDEN的整体架构包括网格细胞编码器、传感器数据处理模块和基于PPO的策略训练模块，能够有效整合视觉和运动传感器数据。

**关键创新**：EDEN的主要创新在于引入了可训练的网格细胞编码器，能够从视觉和运动传感器数据中生成周期性网格状模式，模拟生物体内的导航机制。

**关键设计**：在设计中，采用了轻量级的MiniWorld模拟器进行快速原型开发，并在高保真的Gazebo模拟器中进行真实物理和感知噪声的评估，确保了模型的有效性和可靠性。

## 📊 实验亮点

在实验中，EDEN在简单场景中实现了99%的成功率，在复杂的平面图中成功率超过94%，相较于使用原始状态输入的基线代理，表现出更高的效率和可靠性，显著提升了步进导航的表现。

## 🎯 应用场景

EDEN框架具有广泛的应用潜力，特别是在自主机器人导航、智能交通系统和增强现实等领域。通过提高机器人在复杂环境中的导航能力，EDEN能够推动智能系统的实际部署和应用，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Deep reinforcement learning agents are often fragile while humans remain adaptive and flexible to varying scenarios. To bridge this gap, we present EDEN, a biologically inspired navigation framework that integrates learned entorhinal-like grid cell representations and reinforcement learning to enable autonomous navigation. Inspired by the mammalian entorhinal-hippocampal system, EDEN allows agents to perform path integration and vector-based navigation using visual and motion sensor data. At the core of EDEN is a grid cell encoder that transforms egocentric motion into periodic spatial codes, producing low-dimensional, interpretable embeddings of position. To generate these activations from raw sensory input, we combine fiducial marker detections in the lightweight MiniWorld simulator and DINO-based visual features in the high-fidelity Gazebo simulator. These spatial representations serve as input to a policy trained with Proximal Policy Optimization (PPO), enabling dynamic, goal-directed navigation. We evaluate EDEN in both MiniWorld, for rapid prototyping, and Gazebo, which offers realistic physics and perception noise. Compared to baseline agents using raw state inputs (e.g., position, velocity) or standard convolutional image encoders, EDEN achieves a 99% success rate, within the simple scenarios, and >94% within complex floorplans with occluded paths with more efficient and reliable step-wise navigation. In addition, as a replacement of ground truth activations, we present a trainable Grid Cell encoder enabling the development of periodic grid-like patterns from vision and motion sensor data, emulating the development of such patterns within biological mammals. This work represents a step toward biologically grounded spatial intelligence in robotics, bridging neural navigation principles with reinforcement learning for scalable deployment.

