---
layout: default
title: SatDreamer360: Multiview-Consistent Generation of Ground-Level Scenes from Satellite Imagery
---

# SatDreamer360: Multiview-Consistent Generation of Ground-Level Scenes from Satellite Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00600" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00600v2</a>
  <a href="https://arxiv.org/pdf/2506.00600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00600v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00600v2', 'SatDreamer360: Multiview-Consistent Generation of Ground-Level Scenes from Satellite Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianghui Ze, Beiyi Zhu, Zhenbo Song, Jianfeng Lu, Yujiao Shi

**分类**: cs.CV

**发布日期**: 2025-05-31 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出SatDreamer360以解决卫星图像生成多视角一致地面场景问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `卫星图像` `多视角生成` `几何一致性` `三平面表示` `自动导航` `数字双胞城市` `全景合成`

## 📋 核心要点

1. 现有方法主要集中在合成单个地面全景，难以生成多视角一致的序列，且通常依赖额外输入，存在视角差异问题。
2. 本文提出SatDreamer360框架，通过三平面表示法和光线基础的像素注意机制，从单幅卫星图像生成几何一致的多视角全景。
3. 实验结果表明，SatDreamer360在卫星到地面对齐和多视角一致性方面显著优于现有方法，展示了其有效性。

## 📝 摘要（中文）

从卫星图像生成多视角一致的360度地面场景是一项具有广泛应用的挑战性任务，涉及模拟、自动导航和数字双胞城市等领域。现有方法主要集中在合成单个地面全景，通常依赖高度图或手工投影等辅助输入，难以生成多视角一致的序列。本文提出了SatDreamer360框架，能够从单幅卫星图像生成几何一致的多视角地面全景，前提是给定预定义的姿态轨迹。为了解决地面与卫星图像之间的视角差异，我们采用了三平面表示法来编码场景特征，并设计了一种基于光线的像素注意机制，从三平面中检索视角特定的特征。为了保持多帧一致性，我们引入了全景极线约束注意模块，根据已知的相对姿态对特征进行对齐。为支持评估，我们引入了VIGOR++，这是一个大规模数据集，用于从卫星图像生成多视角地面全景，通过增强原始VIGOR数据集，增加了更多的地面视图图像及其姿态注释。实验表明，SatDreamer360在卫星到地面对齐和多视角一致性方面均优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决从卫星图像生成多视角一致的地面场景的问题。现有方法往往只能合成单个全景图，缺乏多视角一致性，且依赖于高度图等辅助输入，导致视角差异显著。

**核心思路**：论文提出的SatDreamer360框架通过三平面表示法来编码场景特征，并设计了一种光线基础的像素注意机制，以便从三平面中提取视角特定的特征，从而生成几何一致的多视角全景。

**技术框架**：整体架构包括三大模块：三平面表示模块、光线基础像素注意机制和全景极线约束注意模块。三平面表示模块负责编码场景特征，光线基础像素注意机制用于提取视角特征，而全景极线约束注意模块则确保多帧之间的特征一致性。

**关键创新**：最重要的技术创新在于引入了三平面表示法和全景极线约束注意模块，这使得生成的多视角全景在几何上保持一致，克服了现有方法在多视角合成中的不足。

**关键设计**：在模型设计中，采用了特定的损失函数以优化视角一致性，并通过调整网络结构以适应三平面表示法，确保生成的全景图在不同视角下具有一致性和真实性。

## 📊 实验亮点

实验结果显示，SatDreamer360在卫星到地面对齐方面的性能提升显著，相较于现有方法，生成的多视角全景在一致性和真实感上均有明显改善，具体性能数据未详细列出，但实验表明其优越性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在城市规划、虚拟现实和自动驾驶等领域。通过生成一致的多视角地面场景，SatDreamer360能够为模拟环境提供更真实的视觉体验，并支持数字双胞城市的构建与维护，推动智能城市的发展。

## 📄 摘要（原文）

> Generating multiview-consistent $360^\circ$ ground-level scenes from satellite imagery is a challenging task with broad applications in simulation, autonomous navigation, and digital twin cities. Existing approaches primarily focus on synthesizing individual ground-view panoramas, often relying on auxiliary inputs like height maps or handcrafted projections, and struggle to produce multiview consistent sequences. In this paper, we propose SatDreamer360, a framework that generates geometrically consistent multi-view ground-level panoramas from a single satellite image, given a predefined pose trajectory. To address the large viewpoint discrepancy between ground and satellite images, we adopt a triplane representation to encode scene features and design a ray-based pixel attention mechanism that retrieves view-specific features from the triplane. To maintain multi-frame consistency, we introduce a panoramic epipolar-constrained attention module that aligns features across frames based on known relative poses. To support the evaluation, we introduce {VIGOR++}, a large-scale dataset for generating multi-view ground panoramas from a satellite image, by augmenting the original VIGOR dataset with more ground-view images and their pose annotations. Experiments show that SatDreamer360 outperforms existing methods in both satellite-to-ground alignment and multiview consistency.

