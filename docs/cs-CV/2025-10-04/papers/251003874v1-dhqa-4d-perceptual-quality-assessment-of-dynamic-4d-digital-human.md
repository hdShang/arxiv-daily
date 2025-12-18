---
layout: default
title: DHQA-4D: Perceptual Quality Assessment of Dynamic 4D Digital Human
---

# DHQA-4D: Perceptual Quality Assessment of Dynamic 4D Digital Human

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03874" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03874v1</a>
  <a href="https://arxiv.org/pdf/2510.03874.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03874v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03874v1', 'DHQA-4D: Perceptual Quality Assessment of Dynamic 4D Digital Human')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunhao Li, Sijing Wu, Yucheng Zhu, Huiyu Duan, Zicheng Zhang, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-10-04

---

## 💡 一句话要点

**提出DHQA-4D数据集与DynaMesh-Rater模型，用于动态4D数字人感知质量评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态4D数字人` `质量评估` `多模态学习` `大型多模态模型` `数据集构建`

## 📋 核心要点

1. 现有动态4D数字人易受噪声影响，缺乏有效的质量评估方法来保证用户体验。
2. 提出DynaMesh-Rater，利用大型多模态模型融合视觉、运动和几何特征进行质量预测。
3. 构建大规模DHQA-4D数据集，实验证明DynaMesh-Rater优于现有质量评估方法。

## 📝 摘要（中文）

随着3D扫描和重建技术的快速发展，基于4D网格的动态数字人化身越来越受欢迎。高精度的动态数字人化身可以应用于游戏制作、动画生成和远程沉浸式通信等多个领域。然而，这些4D人体化身网格在采集、压缩和传输过程中容易受到各种噪声的退化，从而影响用户的观看体验。鉴于此，动态4D数字人的质量评估变得越来越重要。本文首先提出了一个大规模的动态数字人质量评估数据集DHQA-4D，其中包含32个高质量的真实扫描4D人体网格序列，1920个由11种纹理失真退化的扭曲纹理4D人体网格，以及它们对应的纹理和非纹理平均意见得分（MOS）。基于DHQA-4D数据集，我们分析了不同类型的失真对纹理动态4D网格和非纹理动态4D网格的人类感知的影响。此外，我们提出了一种新的基于大型多模态模型（LMM）的方法DynaMesh-Rater，该方法能够评估纹理4D网格和非纹理4D网格。具体而言，DynaMesh-Rater精心提取多维特征，包括来自投影2D视频的视觉特征、来自裁剪视频片段的运动特征以及来自4D人体网格的几何特征，以提供全面的质量相关信息。然后，我们利用LMM模型来整合多维特征，并采用基于LoRA的指令调优技术来训练LMM模型以预测质量分数。在DHQA-4D数据集上的大量实验结果表明，我们的DynaMesh-Rater方法优于以往的质量评估方法。

## 🔬 方法详解

**问题定义**：论文旨在解决动态4D数字人在采集、压缩和传输过程中引入的噪声导致的质量下降问题。现有方法难以有效评估动态4D数字人的感知质量，无法准确反映用户的主观体验。缺乏大规模数据集也限制了相关研究的进展。

**核心思路**：论文的核心思路是利用大型多模态模型（LMM）同时提取和融合动态4D数字人的视觉、运动和几何特征，从而更全面地评估其感知质量。通过构建大规模数据集并进行指令调优，使LMM能够准确预测主观质量评分。

**技术框架**：DynaMesh-Rater的整体框架包括以下几个主要模块：1) 数据集构建：构建包含高质量和失真4D数字人网格序列的DHQA-4D数据集。2) 特征提取：从投影的2D视频中提取视觉特征，从裁剪的视频片段中提取运动特征，并从4D人体网格中提取几何特征。3) 特征融合：使用LMM模型融合多维特征。4) 质量预测：利用LoRA进行指令调优，训练LMM模型预测质量分数。

**关键创新**：论文的关键创新在于：1) 构建了大规模的动态4D数字人质量评估数据集DHQA-4D，为相关研究提供了基准。2) 提出了DynaMesh-Rater，一种基于LMM的多模态质量评估方法，能够同时处理纹理和非纹理4D网格。3) 采用LoRA进行指令调优，提高了LMM在质量评估任务上的性能。与现有方法相比，DynaMesh-Rater能够更全面地提取和融合多维特征，从而更准确地评估感知质量。

**关键设计**：在特征提取方面，具体采用了哪些网络结构提取视觉、运动和几何特征，论文中未明确说明，属于未知信息。LoRA的参数设置和指令调优的具体策略也未详细描述，属于未知信息。损失函数的设计也未提及，属于未知信息。

## 📊 实验亮点

DynaMesh-Rater在DHQA-4D数据集上取得了显著的性能提升，超越了以往的质量评估方法。具体的性能数据和提升幅度在摘要中未明确给出，属于未知信息。但论文强调了DynaMesh-Rater在纹理和非纹理4D网格上的通用性和准确性。

## 🎯 应用场景

该研究成果可应用于游戏制作、动画生成、远程沉浸式通信等领域，提升用户体验。通过自动化的质量评估，可以优化4D数字人的采集、压缩和传输流程，降低成本并提高效率。未来，该技术有望应用于虚拟现实、增强现实等新兴领域，促进数字人技术的广泛应用。

## 📄 摘要（原文）

> With the rapid development of 3D scanning and reconstruction technologies, dynamic digital human avatars based on 4D meshes have become increasingly popular. A high-precision dynamic digital human avatar can be applied to various fields such as game production, animation generation, and remote immersive communication. However, these 4D human avatar meshes are prone to being degraded by various types of noise during the processes of collection, compression, and transmission, thereby affecting the viewing experience of users. In light of this fact, quality assessment of dynamic 4D digital humans becomes increasingly important. In this paper, we first propose a large-scale dynamic digital human quality assessment dataset, DHQA-4D, which contains 32 high-quality real-scanned 4D human mesh sequences, 1920 distorted textured 4D human meshes degraded by 11 textured distortions, as well as their corresponding textured and non-textured mean opinion scores (MOSs). Equipped with DHQA-4D dataset, we analyze the influence of different types of distortion on human perception for textured dynamic 4D meshes and non-textured dynamic 4D meshes. Additionally, we propose DynaMesh-Rater, a novel large multimodal model (LMM) based approach that is able to assess both textured 4D meshes and non-textured 4D meshes. Concretely, DynaMesh-Rater elaborately extracts multi-dimensional features, including visual features from a projected 2D video, motion features from cropped video clips, and geometry features from the 4D human mesh to provide comprehensive quality-related information. Then we utilize a LMM model to integrate the multi-dimensional features and conduct a LoRA-based instruction tuning technique to teach the LMM model to predict the quality scores. Extensive experimental results on the DHQA-4D dataset demonstrate the superiority of our DynaMesh-Rater method over previous quality assessment methods.

