---
layout: default
title: "GeoVLA: Empowering 3D Representations in Vision-Language-Action Models"
---

# GeoVLA: Empowering 3D Representations in Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09071" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09071v2</a>
  <a href="https://arxiv.org/pdf/2508.09071.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09071v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09071v2', 'GeoVLA: Empowering 3D Representations in Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, Jiale Cao

**分类**: cs.RO

**发布日期**: 2025-08-12 (更新: 2025-08-13)

**备注**: The project is visible at https://linsun449.github.io/GeoVLA/

---

## 💡 一句话要点

**提出GeoVLA以解决VLA模型在3D信息整合中的不足**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `3D几何信息` `机器人操作` `多模态融合` `深度学习`

## 📋 核心要点

1. 现有的VLA模型主要依赖2D视觉输入，缺乏对3D几何信息的利用，导致空间感知能力不足。
2. GeoVLA框架通过整合3D信息，使用视觉-语言模型和定制的点编码器生成融合的视觉-语言和3D几何嵌入。
3. 在LIBERO和ManiSkill2模拟基准测试中，GeoVLA实现了最先进的结果，并在真实任务中展现出显著的鲁棒性。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型作为一种新兴方法，能够使机器人遵循语言指令并预测相应动作。然而，现有的VLA模型主要依赖于2D视觉输入，忽视了3D物理世界中的丰富几何信息，限制了其空间感知能力和适应性。本文提出了GeoVLA，一个新颖的VLA框架，有效整合3D信息以提升机器人操作能力。该框架使用视觉-语言模型处理图像和语言指令，提取融合的视觉-语言嵌入。同时，将深度图转换为点云，并采用定制的点编码器生成独立的3D几何嵌入。这些嵌入被连接并由我们提出的空间感知动作专家处理，生成精确的动作序列。通过在模拟和真实环境中的广泛实验，GeoVLA展示了卓越的性能和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作（VLA）模型在处理3D信息时的不足，尤其是其对空间感知和适应性的限制。现有模型主要依赖于2D视觉输入，未能充分利用3D几何信息。

**核心思路**：GeoVLA通过引入3D信息，结合视觉-语言模型和定制的点编码器，生成融合的视觉-语言嵌入和独立的3D几何嵌入，从而提升机器人在复杂环境中的操作能力。

**技术框架**：GeoVLA的整体架构包括两个主要模块：视觉-语言模型（VLM）用于处理图像和语言指令，生成视觉-语言嵌入；点嵌入网络用于将深度图转换为点云并生成3D几何嵌入。随后，这些嵌入被连接并输入到3D增强动作专家中，生成精确的动作序列。

**关键创新**：GeoVLA的主要创新在于其有效整合了3D几何信息与视觉-语言信息，提出了3D增强动作专家，显著提升了机器人在复杂环境中的操作能力和适应性。

**关键设计**：在设计中，使用了定制的点编码器来处理点云数据，确保生成的3D几何嵌入能够独立于视觉-语言嵌入。此外，损失函数的设计考虑了多模态信息的融合，以优化动作序列的生成。

## 📊 实验亮点

GeoVLA在LIBERO和ManiSkill2模拟基准测试中实现了最先进的结果，展现出在真实任务中的显著鲁棒性，尤其是在高度适应性、尺度感知和视角不变性方面，表现优异。

## 🎯 应用场景

GeoVLA的研究成果在机器人操作、自动化制造和人机交互等领域具有广泛的应用潜力。通过提升机器人对3D环境的理解和适应能力，GeoVLA能够在复杂任务中实现更高的效率和准确性，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a promising approach for enabling robots to follow language instructions and predict corresponding actions. However, current VLA models mainly rely on 2D visual inputs, neglecting the rich geometric information in the 3D physical world, which limits their spatial awareness and adaptability. In this paper, we present GeoVLA, a novel VLA framework that effectively integrates 3D information to advance robotic manipulation. It uses a vision-language model (VLM) to process images and language instructions,extracting fused vision-language embeddings. In parallel, it converts depth maps into point clouds and employs a customized point encoder, called Point Embedding Network, to generate 3D geometric embeddings independently. These produced embeddings are then concatenated and processed by our proposed spatial-aware action expert, called 3D-enhanced Action Expert, which combines information from different sensor modalities to produce precise action sequences. Through extensive experiments in both simulation and real-world environments, GeoVLA demonstrates superior performance and robustness. It achieves state-of-the-art results in the LIBERO and ManiSkill2 simulation benchmarks and shows remarkable robustness in real-world tasks requiring height adaptability, scale awareness and viewpoint invariance.

