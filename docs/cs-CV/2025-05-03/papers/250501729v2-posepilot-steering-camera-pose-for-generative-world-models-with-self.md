---
layout: default
title: PosePilot: Steering Camera Pose for Generative World Models with Self-supervised Depth
---

# PosePilot: Steering Camera Pose for Generative World Models with Self-supervised Depth

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01729" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01729v2</a>
  <a href="https://arxiv.org/pdf/2505.01729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01729v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01729v2', 'PosePilot: Steering Camera Pose for Generative World Models with Self-supervised Depth')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bu Jin, Weize Li, Baihan Yang, Zhenxin Zhu, Junpeng Jiang, Huan-ang Gao, Haiyang Sun, Kun Zhan, Hengtong Hu, Xueyang Zhang, Peng Jia, Hao Zhao

**分类**: cs.CV

**发布日期**: 2025-05-03 (更新: 2025-07-18)

**备注**: Accepted at IEEE/RSJ IROS 2025

---

## 💡 一句话要点

**提出PosePilot以解决摄像头姿态控制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `摄像头姿态控制` `自监督学习` `生成模型` `运动结构` `自动驾驶`

## 📋 核心要点

1. 现有方法在摄像头姿态控制上存在精度不足和灵活性差的问题，影响了视角转换和场景动态的真实模拟。
2. PosePilot通过自监督深度估计和运动结构原理，建立摄像头姿态与视频生成的紧密耦合，提升了姿态控制能力。
3. 在自动驾驶和通用视频数据集上的实验结果显示，PosePilot在结构理解和运动推理方面显著优于现有方法。

## 📝 摘要（中文）

近年来，自动驾驶系统的进展凸显了世界模型在各种驾驶条件下实现鲁棒性和可泛化性能的潜力。然而，精确且灵活的摄像头姿态控制仍然是一个关键挑战。本文提出了PosePilot，一个轻量级且强大的框架，显著增强了生成世界模型中的摄像头姿态可控性。PosePilot借鉴自监督深度估计，利用运动结构原理建立摄像头姿态与视频生成之间的紧密耦合。通过自监督深度和姿态输出，模型能够直接从视频序列中推断深度和相对摄像头运动。这些输出驱动姿态感知的帧扭曲，并通过光度扭曲损失确保合成帧之间的几何一致性。通过引入反向扭曲步骤和姿态回归损失，进一步提高了视角精度和适应性。大量实验表明，PosePilot在扩散基础和自回归世界模型中显著增强了结构理解和运动推理能力。

## 🔬 方法详解

**问题定义**：本文旨在解决生成世界模型中摄像头姿态控制的精确性和灵活性不足的问题。现有方法在视角转换和场景动态模拟上存在局限性，导致生成效果不够真实。

**核心思路**：PosePilot的核心思路是通过自监督深度估计和运动结构原理，建立摄像头姿态与视频生成之间的紧密耦合，从而实现更高效的姿态控制。这样的设计使得模型能够直接从视频序列中推断出深度和相对运动，增强了生成的真实性。

**技术框架**：PosePilot的整体架构包括自监督深度和姿态输出模块、姿态感知帧扭曲模块、光度扭曲损失计算模块以及反向扭曲步骤和姿态回归损失模块。各模块协同工作，确保生成帧之间的几何一致性和视角的精确控制。

**关键创新**：PosePilot的主要创新在于将自监督深度估计与摄像头姿态控制紧密结合，形成了一种新的姿态控制机制。与现有方法相比，PosePilot在姿态可控性和生成质量上具有显著优势。

**关键设计**：PosePilot采用了光度扭曲损失来确保合成帧的几何一致性，并引入了反向扭曲步骤和姿态回归损失，以进一步提高视角的精确性和适应性。

## 📊 实验亮点

在大量实验中，PosePilot在自动驾驶和通用视频数据集上表现出色，相较于基线方法，结构理解和运动推理能力显著提升，具体性能提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

PosePilot的研究成果在自动驾驶、虚拟现实和增强现实等领域具有广泛的应用潜力。通过提升摄像头姿态控制的精确性和灵活性，PosePilot能够为这些领域提供更真实的场景模拟和交互体验，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Recent advancements in autonomous driving (AD) systems have highlighted the potential of world models in achieving robust and generalizable performance across both ordinary and challenging driving conditions. However, a key challenge remains: precise and flexible camera pose control, which is crucial for accurate viewpoint transformation and realistic simulation of scene dynamics. In this paper, we introduce PosePilot, a lightweight yet powerful framework that significantly enhances camera pose controllability in generative world models. Drawing inspiration from self-supervised depth estimation, PosePilot leverages structure-from-motion principles to establish a tight coupling between camera pose and video generation. Specifically, we incorporate self-supervised depth and pose readouts, allowing the model to infer depth and relative camera motion directly from video sequences. These outputs drive pose-aware frame warping, guided by a photometric warping loss that enforces geometric consistency across synthesized frames. To further refine camera pose estimation, we introduce a reverse warping step and a pose regression loss, improving viewpoint precision and adaptability. Extensive experiments on autonomous driving and general-domain video datasets demonstrate that PosePilot significantly enhances structural understanding and motion reasoning in both diffusion-based and auto-regressive world models. By steering camera pose with self-supervised depth, PosePilot sets a new benchmark for pose controllability, enabling physically consistent, reliable viewpoint synthesis in generative world models.

