---
layout: default
title: "Bridging Perspectives: Foundation Model Guided BEV Maps for 3D Object Detection and Tracking"
---

# Bridging Perspectives: Foundation Model Guided BEV Maps for 3D Object Detection and Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10287" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10287v1</a>
  <a href="https://arxiv.org/pdf/2510.10287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10287v1', 'Bridging Perspectives: Foundation Model Guided BEV Maps for 3D Object Detection and Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Markus Käppeler, Özgün Çiçek, Daniele Cattaneo, Claudius Gläser, Yakov Miron, Abhinav Valada

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-11

---

## 💡 一句话要点

**提出DualViewDistill，利用基础模型引导的BEV地图提升3D目标检测与跟踪性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D目标检测` `目标跟踪` `鸟瞰视图` `透视视图` `基础模型` `知识蒸馏` `自动驾驶` `BEV地图`

## 📋 核心要点

1. 当前基于相机的3D目标检测与跟踪方法通常仅依赖透视视图或鸟瞰视图特征，无法同时利用细粒度的物体细节和空间结构化的场景表示。
2. DualViewDistill通过基础模型引导的BEV地图，将DINOv2特征蒸馏到BEV表示中，并结合透视视图特征，实现混合表示，提升检测与跟踪性能。
3. 在nuScenes和Argoverse 2数据集上的实验表明，DualViewDistill达到了最先进的性能，验证了基础模型BEV地图在自动驾驶感知中的潜力。

## 📝 摘要（中文）

本文提出了一种混合检测和跟踪框架DualViewDistill，该框架融合了透视视图(PV)和鸟瞰视图(BEV)的相机图像特征，以利用它们互补的优势。该方法引入了由基础模型引导的BEV地图，利用描述性的DINOv2特征，并通过一种新颖的蒸馏过程将其提炼到BEV表示中。通过将PV特征与富含DINOv2语义和几何特征的BEV地图集成，我们的模型通过可变形聚合利用这种混合表示来增强3D目标检测和跟踪。在nuScenes和Argoverse 2基准测试上的大量实验表明，DualViewDistill实现了最先进的性能。结果表明，基础模型BEV地图有潜力为自动驾驶实现更可靠的感知。代码和预训练模型已公开。

## 🔬 方法详解

**问题定义**：现有基于相机的3D目标检测和跟踪方法，要么侧重于透视视图(PV)的精细物体细节，要么侧重于鸟瞰视图(BEV)的空间结构化场景表示，难以兼顾两者优势。这导致在复杂场景下，检测和跟踪的准确性和鲁棒性受到限制。

**核心思路**：DualViewDistill的核心思路是融合PV和BEV两种视图的优势。通过利用基础模型（DINOv2）提取的语义和几何特征，引导生成高质量的BEV地图，并将PV特征与这些BEV地图融合，从而实现更全面、更准确的场景理解。这样设计的目的是为了弥补单一视图的不足，充分利用不同视角的互补信息。

**技术框架**：DualViewDistill框架包含以下主要模块：1) PV特征提取模块：从相机图像中提取透视视图特征。2) 基础模型引导的BEV地图生成模块：利用DINOv2特征，通过蒸馏过程生成包含丰富语义和几何信息的BEV地图。3) 特征融合模块：将PV特征与BEV地图进行融合，采用可变形聚合的方式，自适应地选择和聚合不同位置的特征。4) 3D目标检测和跟踪模块：基于融合后的特征，进行3D目标检测和跟踪。

**关键创新**：该论文的关键创新在于提出了基础模型引导的BEV地图生成方法。与传统的BEV地图生成方法相比，该方法利用了预训练的基础模型（DINOv2）的强大特征提取能力，从而生成包含更丰富语义和几何信息的BEV地图。这种方法能够有效提升3D目标检测和跟踪的性能。

**关键设计**：在BEV地图生成过程中，采用了蒸馏训练的方式，将DINOv2特征迁移到BEV表示中。具体来说，使用DINOv2提取的图像特征作为teacher，BEV地图生成网络作为student，通过最小化teacher和student输出之间的差异，实现知识迁移。此外，在特征融合模块中，采用了可变形聚合的方式，允许模型自适应地选择和聚合不同位置的特征，从而更好地适应场景的变化。

## 📊 实验亮点

DualViewDistill在nuScenes和Argoverse 2基准测试上取得了显著的性能提升，达到了state-of-the-art水平。具体数据需要在论文中查找，但摘要中明确说明了优于现有方法。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、智能交通、机器人等领域。通过提升3D目标检测和跟踪的准确性和鲁棒性，可以提高自动驾驶系统的安全性，增强机器人对环境的感知能力。未来，该方法有望应用于更复杂的场景，例如城市交通、物流配送等。

## 📄 摘要（原文）

> Camera-based 3D object detection and tracking are essential for perception in autonomous driving. Current state-of-the-art approaches often rely exclusively on either perspective-view (PV) or bird's-eye-view (BEV) features, limiting their ability to leverage both fine-grained object details and spatially structured scene representations. In this work, we propose DualViewDistill, a hybrid detection and tracking framework that incorporates both PV and BEV camera image features to leverage their complementary strengths. Our approach introduces BEV maps guided by foundation models, leveraging descriptive DINOv2 features that are distilled into BEV representations through a novel distillation process. By integrating PV features with BEV maps enriched with semantic and geometric features from DINOv2, our model leverages this hybrid representation via deformable aggregation to enhance 3D object detection and tracking. Extensive experiments on the nuScenes and Argoverse 2 benchmarks demonstrate that DualViewDistill achieves state-of-the-art performance. The results showcase the potential of foundation model BEV maps to enable more reliable perception for autonomous driving. We make the code and pre-trained models available at https://dualviewdistill.cs.uni-freiburg.de .

