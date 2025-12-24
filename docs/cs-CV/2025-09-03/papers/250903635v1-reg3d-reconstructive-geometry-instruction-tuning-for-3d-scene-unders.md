---
layout: default
title: "Reg3D: Reconstructive Geometry Instruction Tuning for 3D Scene Understanding"
---

# Reg3D: Reconstructive Geometry Instruction Tuning for 3D Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03635" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03635v1</a>
  <a href="https://arxiv.org/pdf/2509.03635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03635v1', 'Reg3D: Reconstructive Geometry Instruction Tuning for 3D Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongpei Zheng, Lintao Xiang, Qijun Yang, Qian Lin, Hujun Yin

**分类**: cs.CV

**发布日期**: 2025-09-03

**备注**: 16 pages, 6 figures

---

## 💡 一句话要点

**提出Reg3D，通过重建几何指令微调提升3D场景理解能力**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景理解` `多模态学习` `几何重建` `指令微调` `空间推理`

## 📋 核心要点

1. 现有3D场景理解方法依赖纯文本监督，缺乏几何约束，难以学习鲁棒的空间表示。
2. Reg3D采用重建几何指令微调框架，利用3D几何信息作为输入和学习目标，实现双重监督。
3. 实验表明，Reg3D在多个3D场景理解任务上取得了显著的性能提升，验证了其有效性。

## 📝 摘要（中文）

大型多模态模型（LMMs）的快速发展显著提升了2D视觉理解能力，但将这些能力扩展到3D场景理解仍然是一个重大挑战。现有方法主要依赖于纯文本监督，无法提供学习鲁棒3D空间表示所需的几何约束。本文提出了Reg3D，一种新颖的重建几何指令微调框架，通过将几何感知监督直接融入训练过程来解决这一局限性。我们的核心思想是，有效的3D理解需要重建潜在的几何结构，而不仅仅是描述它们。与仅在输入层面注入3D信息的方法不同，Reg3D采用双重监督范式，利用3D几何信息作为输入和显式学习目标。具体而言，我们在双编码器架构中设计了互补的对象级和帧级重建任务，强制执行几何一致性，以鼓励空间推理能力的开发。在ScanQA、Scan2Cap、ScanRefer和SQA3D上的大量实验表明，Reg3D提供了显著的性能改进，为空间感知多模态模型建立了一种新的训练范式。

## 🔬 方法详解

**问题定义**：现有的大型多模态模型在2D视觉理解方面取得了显著进展，但将其扩展到3D场景理解仍然面临挑战。现有方法主要依赖于文本监督，缺乏对3D几何信息的有效利用，导致模型难以学习鲁棒的空间表示，无法很好地理解3D场景的几何结构和空间关系。

**核心思路**：Reg3D的核心思路是通过重建几何结构来提升3D场景理解能力。与仅仅描述3D场景不同，Reg3D强制模型学习重建场景的几何信息，从而更好地理解场景的空间结构。这种重建过程可以提供更强的几何约束，帮助模型学习更鲁棒的3D表示。

**技术框架**：Reg3D采用双编码器架构，包含文本编码器和3D场景编码器。该框架使用双重监督范式，同时利用3D几何信息作为输入和学习目标。具体来说，框架包含对象级重建任务和帧级重建任务。对象级重建任务旨在重建场景中各个对象的3D几何形状，而帧级重建任务旨在重建整个场景的3D结构。这两个任务相互补充，共同促进模型对3D场景的理解。

**关键创新**：Reg3D的关键创新在于引入了重建几何指令微调框架，将3D几何信息作为显式的学习目标。与现有方法不同，Reg3D不仅在输入层面注入3D信息，还在输出层面强制模型重建3D几何结构。这种双重监督范式可以提供更强的几何约束，帮助模型学习更鲁棒的3D表示。

**关键设计**：Reg3D的关键设计包括对象级重建损失和帧级重建损失。对象级重建损失用于衡量模型重建单个对象几何形状的准确性，而帧级重建损失用于衡量模型重建整个场景几何结构的准确性。此外，Reg3D还采用了对比学习策略，鼓励模型学习区分不同的3D场景。具体的网络结构和参数设置根据不同的任务和数据集进行调整。

## 📊 实验亮点

Reg3D在ScanQA、Scan2Cap、ScanRefer和SQA3D等多个3D场景理解任务上取得了显著的性能提升。例如，在ScanQA任务上，Reg3D的性能超过了现有最佳方法，取得了显著的提升。实验结果表明，Reg3D能够有效地利用3D几何信息，提升模型对3D场景的理解能力。

## 🎯 应用场景

Reg3D的研究成果可应用于机器人导航、自动驾驶、虚拟现实、增强现实等领域。通过提升3D场景理解能力，可以使机器人更好地感知周围环境，实现更智能的导航和交互。在自动驾驶领域，可以提高车辆对周围环境的感知精度，从而提升驾驶安全性。在VR/AR领域，可以创建更逼真的3D场景，提升用户体验。

## 📄 摘要（原文）

> The rapid development of Large Multimodal Models (LMMs) has led to remarkable progress in 2D visual understanding; however, extending these capabilities to 3D scene understanding remains a significant challenge. Existing approaches predominantly rely on text-only supervision, which fails to provide the geometric constraints required for learning robust 3D spatial representations. In this paper, we introduce Reg3D, a novel Reconstructive Geometry Instruction Tuning framework that addresses this limitation by incorporating geometry-aware supervision directly into the training process. Our key insight is that effective 3D understanding necessitates reconstructing underlying geometric structures rather than merely describing them. Unlike existing methods that inject 3D information solely at the input level, Reg3D adopts a dual-supervision paradigm that leverages 3D geometric information both as input and as explicit learning targets. Specifically, we design complementary object-level and frame-level reconstruction tasks within a dual-encoder architecture, enforcing geometric consistency to encourage the development of spatial reasoning capabilities. Extensive experiments on ScanQA, Scan2Cap, ScanRefer, and SQA3D demonstrate that Reg3D delivers substantial performance improvements, establishing a new training paradigm for spatially aware multimodal models.

