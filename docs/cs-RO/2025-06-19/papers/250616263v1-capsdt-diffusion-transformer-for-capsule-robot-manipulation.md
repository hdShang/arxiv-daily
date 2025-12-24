---
layout: default
title: "CapsDT: Diffusion-Transformer for Capsule Robot Manipulation"
---

# CapsDT: Diffusion-Transformer for Capsule Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16263" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16263v1</a>
  <a href="https://arxiv.org/pdf/2506.16263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16263v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16263v1', 'CapsDT: Diffusion-Transformer for Capsule Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiting He, Mingwu Su, Xinqi Jiang, Long Bai, Jiewen Lai, Hongliang Ren

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-19

**备注**: IROS 2025

---

## 💡 一句话要点

**提出CapsDT以解决内窥镜胶囊机器人操作问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `胶囊机器人` `内窥镜操作` `扩散变换器` `机器人控制` `医疗应用` `智能医疗`

## 📋 核心要点

1. 现有的内窥镜机器人在执行复杂任务时，缺乏有效的视觉和语言指令的结合，导致操作效率低下。
2. CapsDT模型通过融合视觉输入和文本指令，能够推断出相应的机器人控制信号，从而提升胶囊机器人在胃内的操作能力。
3. 实验结果显示，CapsDT在多种内窥镜任务中表现优异，成功率达到26.25%，显著优于现有方法。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型已成为一个重要的研究领域，展现出在多种应用中的潜力。然而，在内窥镜机器人，尤其是执行消化系统内操作的胶囊机器人方面，其性能尚未被探索。将VLA模型整合到内窥镜机器人中，可以实现人机之间更直观高效的交互，从而提高诊断准确性和治疗效果。本文设计了CapsDT，一种用于胶囊机器人在胃内操作的扩散变换器模型。通过处理交错的视觉输入和文本指令，CapsDT能够推断相应的机器人控制信号，以促进内窥镜任务的完成。此外，我们开发了一种胶囊内窥镜机器人系统，通过机械臂控制的磁铁来操作胶囊机器人，涵盖四种不同级别的内窥镜任务，并在胃模拟器中创建相应的胶囊机器人数据集。对各种机器人任务的全面评估表明，CapsDT作为一种强大的视觉-语言通用模型，在多种内窥镜任务中实现了最先进的性能，并在真实世界模拟操作中达到了26.25%的成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决内窥镜胶囊机器人在执行消化系统内操作时，缺乏有效的视觉与语言指令结合的问题。现有方法在复杂任务中表现不佳，难以实现高效的操作。

**核心思路**：CapsDT模型的核心思路是通过扩散变换器架构，融合视觉输入和文本指令，从而推断出相应的机器人控制信号。这种设计能够实现更直观的人机交互，提升操作的准确性和效率。

**技术框架**：CapsDT的整体架构包括视觉输入处理模块、文本指令解析模块和控制信号推断模块。视觉输入和文本指令通过交错的方式输入到模型中，经过处理后生成控制信号，指导胶囊机器人完成任务。

**关键创新**：CapsDT的主要创新在于将扩散变换器应用于胶囊机器人操作中，突破了传统方法在视觉和语言结合上的局限，提供了一种新的解决方案。

**关键设计**：模型的关键设计包括特定的损失函数用于优化视觉和语言的融合效果，以及网络结构中的多层变换器模块，以增强模型的表达能力和推断精度。具体参数设置和训练策略在实验部分进行了详细描述。

## 📊 实验亮点

CapsDT在多种内窥镜任务中表现出色，成功率达到26.25%，显著优于现有技术。此外，模型在处理复杂的视觉和语言输入方面展现了强大的能力，为未来的内窥镜机器人操作提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括医疗内窥镜操作、机器人辅助诊断和治疗等。CapsDT的成功应用能够提高内窥镜手术的效率和安全性，未来可能在更广泛的医疗场景中发挥重要作用，推动智能医疗的发展。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a prominent research area, showcasing significant potential across a variety of applications. However, their performance in endoscopy robotics, particularly endoscopy capsule robots that perform actions within the digestive system, remains unexplored. The integration of VLA models into endoscopy robots allows more intuitive and efficient interactions between human operators and medical devices, improving both diagnostic accuracy and treatment outcomes. In this work, we design CapsDT, a Diffusion Transformer model for capsule robot manipulation in the stomach. By processing interleaved visual inputs, and textual instructions, CapsDT can infer corresponding robotic control signals to facilitate endoscopy tasks. In addition, we developed a capsule endoscopy robot system, a capsule robot controlled by a robotic arm-held magnet, addressing different levels of four endoscopy tasks and creating corresponding capsule robot datasets within the stomach simulator. Comprehensive evaluations on various robotic tasks indicate that CapsDT can serve as a robust vision-language generalist, achieving state-of-the-art performance in various levels of endoscopy tasks while achieving a 26.25% success rate in real-world simulation manipulation.

