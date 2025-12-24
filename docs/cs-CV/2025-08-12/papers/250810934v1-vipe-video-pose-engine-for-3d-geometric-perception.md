---
layout: default
title: "ViPE: Video Pose Engine for 3D Geometric Perception"
---

# ViPE: Video Pose Engine for 3D Geometric Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10934" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10934v1</a>
  <a href="https://arxiv.org/pdf/2508.10934.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10934v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10934v1', 'ViPE: Video Pose Engine for 3D Geometric Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahui Huang, Qunjie Zhou, Hesam Rabeti, Aleksandr Korovko, Huan Ling, Xuanchi Ren, Tianchang Shen, Jun Gao, Dmitry Slepichev, Chen-Hsuan Lin, Jiawei Ren, Kevin Xie, Joydeep Biswas, Laura Leal-Taixe, Sanja Fidler

**分类**: cs.CV, cs.GR, cs.RO, eess.IV

**发布日期**: 2025-08-12

**备注**: Paper website: https://research.nvidia.com/labs/toronto-ai/vipe/

---

## 💡 一句话要点

**提出ViPE以解决3D几何感知中的视频标注挑战**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D几何感知` `视频处理` `相机姿态估计` `深度图生成` `空间AI系统`

## 📋 核心要点

1. 现有方法在获取一致且精确的3D标注方面面临挑战，尤其是在处理无约束视频时。
2. ViPE通过高效估计相机内参、相机运动和密集深度图，提供了一种新的视频处理引擎。
3. ViPE在TUM/KITTI序列上分别比现有基线提高了18%和50%的性能，且在单个GPU上运行速度达到3-5FPS。

## 📝 摘要（中文）

准确的3D几何感知是多种空间AI系统的重要前提。然而，现有方法依赖于大规模训练数据，而从现实视频中获取一致且精确的3D标注仍然是一个关键挑战。本文提出了ViPE，一个高效且多功能的视频处理引擎，旨在弥补这一空白。ViPE能够从无约束的原始视频中高效估计相机内参、相机运动和密集的近度量深度图，且对动态自拍视频、电影镜头和行车记录仪等多种场景具有鲁棒性。我们在多个基准测试中对ViPE进行了评估，结果显示其在TUM/KITTI序列上分别比现有的未标定姿态估计基线提高了18%和50%，并且在单个GPU上以3-5FPS的速度运行。我们利用ViPE对大规模视频集合进行了标注，包含约10万条真实互联网视频、100万条高质量AI生成视频和2000条全景视频，总计约9600万帧，所有视频均标注了准确的相机姿态和密集深度图。我们开源了ViPE及标注数据集，希望加速空间AI系统的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决从无约束视频中获取准确3D几何感知的问题。现有方法通常依赖于大规模的标注数据，导致在实际应用中难以获取一致且精确的3D标注。

**核心思路**：ViPE的核心思路是通过高效的算法从原始视频中提取相机内参、运动信息和深度图，减少对大量标注数据的依赖，从而提高3D几何感知的准确性和效率。

**技术框架**：ViPE的整体架构包括相机内参估计、相机运动估计和深度图生成三个主要模块。首先，从视频中提取关键帧，然后通过这些帧进行相机参数的估计，最后生成密集的深度图。

**关键创新**：ViPE的主要创新在于其对多种相机模型的支持，包括针孔、广角和360°全景相机，且在动态场景下表现出色。这使得ViPE在处理多样化视频时具有更强的鲁棒性。

**关键设计**：在技术细节上，ViPE采用了特定的损失函数来优化相机运动和深度图的估计，同时在网络结构上进行了针对性的设计，以提高处理速度和准确性。

## 📊 实验亮点

ViPE在多个基准测试中表现优异，尤其是在TUM和KITTI序列上，分别比现有未标定姿态估计基线提高了18%和50%。此外，ViPE在标准输入分辨率下能够以3-5FPS的速度运行，显示出其高效性。

## 🎯 应用场景

ViPE的研究成果在多个领域具有潜在应用价值，包括自动驾驶、增强现实和虚拟现实等。通过提供准确的3D几何感知，ViPE能够为这些领域的空间AI系统提供更可靠的基础，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Accurate 3D geometric perception is an important prerequisite for a wide range of spatial AI systems. While state-of-the-art methods depend on large-scale training data, acquiring consistent and precise 3D annotations from in-the-wild videos remains a key challenge. In this work, we introduce ViPE, a handy and versatile video processing engine designed to bridge this gap. ViPE efficiently estimates camera intrinsics, camera motion, and dense, near-metric depth maps from unconstrained raw videos. It is robust to diverse scenarios, including dynamic selfie videos, cinematic shots, or dashcams, and supports various camera models such as pinhole, wide-angle, and 360° panoramas. We have benchmarked ViPE on multiple benchmarks. Notably, it outperforms existing uncalibrated pose estimation baselines by 18%/50% on TUM/KITTI sequences, and runs at 3-5FPS on a single GPU for standard input resolutions. We use ViPE to annotate a large-scale collection of videos. This collection includes around 100K real-world internet videos, 1M high-quality AI-generated videos, and 2K panoramic videos, totaling approximately 96M frames -- all annotated with accurate camera poses and dense depth maps. We open-source ViPE and the annotated dataset with the hope of accelerating the development of spatial AI systems.

