---
layout: default
title: "VolumetricSMPL: A Neural Volumetric Body Model for Efficient Interactions, Contacts, and Collisions"
---

# VolumetricSMPL: A Neural Volumetric Body Model for Efficient Interactions, Contacts, and Collisions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23236" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23236v1</a>
  <a href="https://arxiv.org/pdf/2506.23236.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23236v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23236v1', 'VolumetricSMPL: A Neural Volumetric Body Model for Efficient Interactions, Contacts, and Collisions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marko Mihajlovic, Siwei Zhang, Gen Li, Kaifeng Zhao, Lea Müller, Siyu Tang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-29

**备注**: [ICCV 2025] https://markomih.github.io/VolumetricSMPL

---

## 💡 一句话要点

**提出VolumetricSMPL以解决高效人机交互问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `体积模型` `神经网络` `人机交互` `计算机视觉` `高效推理` `姿态估计` `深度学习`

## 📋 核心要点

1. 现有的体积神经隐式人体模型在复杂的人体关节运动中表现不足，且计算和内存成本较高。
2. 本文提出的VolumetricSMPL通过神经混合权重（NBW）生成紧凑的MLP解码器，显著提高了计算效率。
3. 实验结果显示，VolumetricSMPL在推理速度上比现有模型快10倍，GPU内存使用量降低6倍，且准确性得到提升。

## 📝 摘要（中文）

参数化人体模型在计算机图形学和视觉中扮演着重要角色，应用范围从人类动作分析到理解人类与环境的交互。传统模型使用表面网格，难以高效处理与其他几何实体的交互。为此，本文提出VolumetricSMPL，一个利用神经混合权重（NBW）生成紧凑高效的MLP解码器的神经体积模型。与以往依赖大型MLP的方法不同，NBW通过预测的形状和姿态相关系数动态混合一小组学习的权重矩阵，显著提高计算效率并保持表达能力。实验结果表明，VolumetricSMPL在多个任务中表现优异，具有广泛的应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决传统表面网格模型在处理人机交互时的效率和鲁棒性问题。现有的体积神经隐式模型在复杂的人体运动和高计算成本方面存在不足。

**核心思路**：VolumetricSMPL通过引入神经混合权重（NBW），动态混合少量学习的权重矩阵，优化了模型的计算效率，同时保持了表达能力。

**技术框架**：该模型的整体架构包括输入的形状和姿态信息，通过NBW生成相应的权重矩阵，最终通过MLP解码器输出体积表示。主要模块包括输入处理、权重生成和体积解码。

**关键创新**：最重要的创新在于使用NBW动态混合权重，避免了传统方法中对大型MLP的依赖，从而在计算效率和内存使用上实现了显著提升。

**关键设计**：模型设计中采用了小型的MLP结构，并通过损失函数优化体积表示的准确性，同时在训练过程中调整权重矩阵以适应不同的形状和姿态。

## 📊 实验亮点

实验结果显示，VolumetricSMPL在推理速度上比现有的体积占用模型COAP快10倍，GPU内存使用量降低6倍，同时在准确性和可微分接触建模方面也有显著提升。这些结果表明该模型在处理复杂人机交互任务时的有效性。

## 🎯 应用场景

VolumetricSMPL在多个领域具有广泛的应用潜力，包括虚拟现实、增强现实和游戏开发等。其高效的人机交互能力可以提升用户体验，并为复杂场景中的人类行为分析提供支持。此外，该模型在机器人技术中也可用于提高人机协作的效率。

## 📄 摘要（原文）

> Parametric human body models play a crucial role in computer graphics and vision, enabling applications ranging from human motion analysis to understanding human-environment interactions. Traditionally, these models use surface meshes, which pose challenges in efficiently handling interactions with other geometric entities, such as objects and scenes, typically represented as meshes or point clouds. To address this limitation, recent research has explored volumetric neural implicit body models. However, existing works are either insufficiently robust for complex human articulations or impose high computational and memory costs, limiting their widespread use. To this end, we introduce VolumetricSMPL, a neural volumetric body model that leverages Neural Blend Weights (NBW) to generate compact, yet efficient MLP decoders. Unlike prior approaches that rely on large MLPs, NBW dynamically blends a small set of learned weight matrices using predicted shape- and pose-dependent coefficients, significantly improving computational efficiency while preserving expressiveness. VolumetricSMPL outperforms prior volumetric occupancy model COAP with 10x faster inference, 6x lower GPU memory usage, enhanced accuracy, and a Signed Distance Function (SDF) for efficient and differentiable contact modeling. We demonstrate VolumetricSMPL's strengths across four challenging tasks: (1) reconstructing human-object interactions from in-the-wild images, (2) recovering human meshes in 3D scenes from egocentric views, (3) scene-constrained motion synthesis, and (4) resolving self-intersections. Our results highlight its broad applicability and significant performance and efficiency gains.

