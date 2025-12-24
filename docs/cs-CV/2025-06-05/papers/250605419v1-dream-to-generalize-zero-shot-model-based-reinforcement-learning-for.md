---
layout: default
title: "Dream to Generalize: Zero-Shot Model-Based Reinforcement Learning for Unseen Visual Distractions"
---

# Dream to Generalize: Zero-Shot Model-Based Reinforcement Learning for Unseen Visual Distractions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05419" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05419v1</a>
  <a href="https://arxiv.org/pdf/2506.05419.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05419v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05419v1', 'Dream to Generalize: Zero-Shot Model-Based Reinforcement Learning for Unseen Visual Distractions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeongsoo Ha, Kyungsoo Kim, Yusung Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-05

**备注**: AAAI 2023

**🔗 代码/项目**: [GITHUB](https://github.com/JeongsooHa/DrG.git)

---

## 💡 一句话要点

**提出Dream to Generalize以解决视觉干扰下的零-shot模型强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模型基础强化学习` `视觉干扰` `自监督学习` `对比学习` `递归动态模型` `泛化能力` `机器人控制`

## 📋 核心要点

1. 现有的模型基础强化学习在面对视觉干扰时表现不佳，无法有效处理现实场景中的任务无关干扰。
2. 论文提出的Dream to Generalize方法通过双重对比学习和递归状态逆动态模型，增强了世界模型对视觉干扰的鲁棒性。
3. 实验结果显示，Dr. G在复杂背景下的表现显著提升，分别在DeepMind Control和Robosuite中提高了117%和14%。

## 📝 摘要（中文）

模型基础强化学习（MBRL）已被用于高维图像观察中的视觉控制任务。然而，现有的MBRL算法在面对观察中的视觉干扰时表现不佳。这些与任务无关的干扰（如云、阴影和光线）在现实场景中可能会持续存在。本研究提出了一种新颖的自监督方法Dream to Generalize（Dr. G），用于零-shot MBRL。Dr. G通过双重对比学习训练其编码器和世界模型，有效捕捉多视角数据增强中的任务相关特征。此外，我们还引入了一种递归状态逆动态模型，帮助世界模型更好地理解时间结构。实验结果表明，Dr. G在复杂自然视频背景下的泛化性能显著提升，分别在DeepMind Control套件和Robosuite中的随机环境中实现了117%和14%的性能提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决模型基础强化学习在面对视觉干扰时的性能下降问题。现有方法在训练观察中表现良好，但在真实场景中遇到云、阴影等干扰时效果不佳。

**核心思路**：论文提出的Dream to Generalize（Dr. G）方法通过自监督学习和双重对比学习，旨在从多视角数据中提取任务相关特征，从而提高模型的泛化能力。

**技术框架**：Dr. G的整体架构包括编码器、世界模型和递归状态逆动态模型。编码器通过对比学习提取特征，世界模型利用这些特征进行环境模拟，而递归状态逆动态模型则帮助理解时间结构。

**关键创新**：最重要的创新点在于引入双重对比学习和递归状态逆动态模型，这使得模型能够更好地适应视觉干扰，与传统方法相比，显著提升了鲁棒性和泛化能力。

**关键设计**：在模型设计中，采用了特定的损失函数来优化对比学习过程，并通过多视角数据增强来提高特征提取的有效性。网络结构经过精心设计，以确保在复杂背景下的稳定性和准确性。

## 📊 实验亮点

实验结果表明，Dr. G在DeepMind Control套件中实现了117%的性能提升，在Robosuite中的随机环境中提升了14%。这些结果显示了该方法在处理复杂视觉背景时的显著优势，超越了现有的基线模型，证明了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶和智能监控等需要处理复杂视觉信息的场景。通过提高模型在视觉干扰下的鲁棒性，Dr. G能够在实际应用中提供更可靠的性能，推动智能系统在动态环境中的应用。未来，该方法可能会影响更多领域的视觉感知和决策制定。

## 📄 摘要（原文）

> Model-based reinforcement learning (MBRL) has been used to efficiently solve vision-based control tasks in highdimensional image observations. Although recent MBRL algorithms perform well in trained observations, they fail when faced with visual distractions in observations. These task-irrelevant distractions (e.g., clouds, shadows, and light) may be constantly present in real-world scenarios. In this study, we propose a novel self-supervised method, Dream to Generalize (Dr. G), for zero-shot MBRL. Dr. G trains its encoder and world model with dual contrastive learning which efficiently captures task-relevant features among multi-view data augmentations. We also introduce a recurrent state inverse dynamics model that helps the world model to better understand the temporal structure. The proposed methods can enhance the robustness of the world model against visual distractions. To evaluate the generalization performance, we first train Dr. G on simple backgrounds and then test it on complex natural video backgrounds in the DeepMind Control suite, and the randomizing environments in Robosuite. Dr. G yields a performance improvement of 117% and 14% over prior works, respectively. Our code is open-sourced and available at https://github.com/JeongsooHa/DrG.git

