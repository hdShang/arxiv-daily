---
layout: default
title: "Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots"
---

# Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17369" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17369v1</a>
  <a href="https://arxiv.org/pdf/2510.17369.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17369v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17369v1', 'Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haochen Su, Cristian Meo, Francesco Stella, Andrea Peirone, Kai Junge, Josie Hughes

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-10-20

**备注**: Accepted by NeurIPS 2025 SpaVLE workshop. 4 pages, 2 figures(in main paper, excluding references and supplements)

---

## 💡 一句话要点

**提出将视觉-语言-动作模型应用于软机器人以解决安全交互问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `软机器人` `人机交互` `微调` `安全性` `适应性` `具身人工智能`

## 📋 核心要点

1. 现有的视觉-语言-动作模型主要应用于传统的刚性机械臂，缺乏在软机器人上的有效部署，导致安全交互能力不足。
2. 本文提出了一种结构化的微调和部署流程，针对软机器人进行视觉-语言-动作模型的优化，以实现安全的人机交互。
3. 实验结果表明，通过针对性的微调，软机器人在代表性操作任务中的表现与刚性机器人相当，展示了微调的重要性。

## 📝 摘要（中文）

随着机器人系统在以人为中心的非结构化环境中应用的增加，安全性、适应性和泛化能力变得至关重要。视觉-语言-动作（VLA）模型被提出作为一种语言引导的通用控制框架，但其应用主要限于传统的串联机械臂。本文展示了在软连续操纵器上部署VLA模型，以实现自主安全的人机交互。通过对两种最先进的VLA模型（OpenVLA-OFT和$π_0$）进行结构化微调和部署评估，研究表明，尽管现成策略因体现不匹配而失败，但通过有针对性的微调，软机器人能够与刚性机器人表现相当。研究结果强调了微调在弥合体现差距中的必要性，并展示了将VLA模型与软机器人结合的潜力，以实现安全灵活的具身人工智能。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉-语言-动作模型在软机器人上的应用问题，现有方法在刚性机器人上表现良好，但在软机器人上因体现不匹配而导致安全性和适应性不足。

**核心思路**：通过对VLA模型进行结构化微调，使其能够适应软机器人的特性，从而实现安全和灵活的人机交互。该方法强调了微调的重要性，以克服现有模型的局限性。

**技术框架**：整体架构包括模型选择、数据收集、微调和评估四个主要模块。首先选择两种VLA模型，然后在软机器人上进行数据收集，接着进行针对性的微调，最后评估其在操作任务中的表现。

**关键创新**：最重要的技术创新在于提出了一种有效的微调策略，使得VLA模型能够在软机器人上安全运行，解决了传统模型在软机器人应用中的体现不匹配问题。

**关键设计**：在微调过程中，采用了特定的损失函数和参数设置，以确保模型能够适应软机器人的动态特性，同时保持与刚性机器人相似的性能。

## 📊 实验亮点

实验结果显示，通过针对性的微调，软机器人在代表性操作任务中的表现与刚性机器人相当，成功实现了安全的人机交互。这一成果表明，微调对于弥合体现差距至关重要，且软机器人在复杂环境中的应用潜力巨大。

## 🎯 应用场景

该研究的潜在应用领域包括医疗机器人、服务机器人和人机协作系统等，能够在复杂和动态的环境中实现安全的交互。未来，随着软机器人技术的发展，该方法有望在更多实际场景中得到应用，提升人机协作的安全性和灵活性。

## 📄 摘要（原文）

> Robotic systems are increasingly expected to operate in human-centered, unstructured environments where safety, adaptability, and generalization are essential. Vision-Language-Action (VLA) models have been proposed as a language guided generalized control framework for real robots. However, their deployment has been limited to conventional serial link manipulators. Coupled by their rigidity and unpredictability of learning based control, the ability to safely interact with the environment is missing yet critical. In this work, we present the deployment of a VLA model on a soft continuum manipulator to demonstrate autonomous safe human-robot interaction. We present a structured finetuning and deployment pipeline evaluating two state-of-the-art VLA models (OpenVLA-OFT and $π_0$) across representative manipulation tasks, and show while out-of-the-box policies fail due to embodiment mismatch, through targeted finetuning the soft robot performs equally to the rigid counterpart. Our findings highlight the necessity of finetuning for bridging embodiment gaps, and demonstrate that coupling VLA models with soft robots enables safe and flexible embodied AI in human-shared environments.

