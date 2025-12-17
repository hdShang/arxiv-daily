---
layout: default
title: LAA3D: A Benchmark of Detecting and Tracking Low-Altitude Aircraft in 3D Space
---

# LAA3D: A Benchmark of Detecting and Tracking Low-Altitude Aircraft in 3D Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19057" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19057v1</a>
  <a href="https://arxiv.org/pdf/2511.19057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19057v1" onclick="toggleFavorite(this, '2511.19057v1', 'LAA3D: A Benchmark of Detecting and Tracking Low-Altitude Aircraft in 3D Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hai Wu, Shuai Tang, Jiale Wang, Longkun Zou, Mingyue Guo, Rongqin Liang, Ke Chen, Yaowei Wang

**分类**: cs.CV

**发布日期**: 2025-11-24

**备注**: 25 pages

---

## 💡 一句话要点

**LAA3D：构建低空飞行器三维感知基准数据集与单目3D检测基线。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `低空飞行器` `三维目标检测` `单目视觉` `数据集` `多目标跟踪`

## 📋 核心要点

1. 现有针对低空飞行器三维感知的公开数据集稀缺，限制了相关算法的研究和发展。
2. 构建大规模、多场景、多类别的LAA3D数据集，并提出单目3D检测基线MonoLAA，促进研究。
3. 实验表明，在合成数据上预训练的模型能够有效迁移到真实数据，验证了数据集的有效性。

## 📝 摘要（中文）

本文提出了LAA3D，一个大规模数据集，旨在推进低空飞行器（LAA）的三维检测和跟踪。LAA3D包含15,000张真实图像和600,000帧合成图像，涵盖城市和郊区等多种场景。它覆盖了多种空中目标类别，包括电动垂直起降（eVTOL）飞机、微型飞行器（MAV）和直升机。每个实例都标注了3D边界框、类别标签和实例ID，支持3D目标检测、3D多目标跟踪（MOT）和6-DoF姿态估计等任务。此外，本文还建立了LAA3D基准，集成了多个任务和方法，并采用统一的评估协议进行比较。同时，提出了MonoLAA，一种单目3D检测基线，能够从具有不同焦距的变焦相机中实现鲁棒的3D定位。在合成图像上预训练的模型经过微调后，能够有效地迁移到真实世界数据，表现出强大的sim-to-real泛化能力。LAA3D为未来低空3D目标感知研究提供了全面的基础。

## 🔬 方法详解

**问题定义**：现有方法缺乏专门针对低空飞行器三维感知的数据集，导致相关算法难以训练和评估。尤其是在复杂场景下，精确的3D目标检测和跟踪面临挑战。现有数据集通常关注自动驾驶场景，缺乏对低空飞行器，特别是eVTOL、MAV等新型飞行器的支持。

**核心思路**：本文的核心思路是构建一个大规模、多样化的数据集LAA3D，包含真实图像和合成图像，以弥补现有数据集的不足。同时，提出一个单目3D检测基线MonoLAA，利用单目图像实现对低空飞行器的3D定位，并验证数据集的有效性。通过sim-to-real的迁移学习，降低对大量真实标注数据的依赖。

**技术框架**：LAA3D数据集包含15,000张真实图像和600,000帧合成图像，涵盖多种场景和飞行器类型。每个实例都标注了3D边界框、类别标签和实例ID。MonoLAA是一个单目3D检测框架，具体架构细节未知，但强调了其在变焦相机下的鲁棒性。整体流程包括数据采集与标注、模型训练与评估、以及sim-to-real迁移学习。

**关键创新**：LAA3D数据集本身是最大的创新点，它填补了低空飞行器三维感知数据集的空白。MonoLAA的创新点在于其单目3D检测能力，以及在变焦相机下的鲁棒性。通过合成数据预训练和真实数据微调，实现了有效的sim-to-real迁移，降低了对大量真实标注数据的需求。

**关键设计**：数据集的关键设计在于其规模、多样性和标注质量。合成数据的生成策略，以及真实数据的采集和标注流程，对数据集的质量至关重要。MonoLAA的关键设计细节未知，但推测可能包括针对单目3D检测的损失函数设计、网络结构优化，以及针对变焦相机特点的图像处理技术。

## 📊 实验亮点

实验结果表明，在LAA3D数据集上训练的MonoLAA模型能够实现鲁棒的单目3D检测。通过在合成数据上预训练，并在真实数据上进行微调，模型能够有效地迁移到真实场景，表现出良好的泛化能力。具体的性能数据和对比基线未在摘要中明确给出，但强调了sim-to-real迁移的有效性。

## 🎯 应用场景

该研究成果可应用于低空交通管理、无人机自主导航、安防监控等领域。LAA3D数据集能够促进相关算法的开发和评估，提高低空飞行器的感知能力，为构建安全、高效的低空空域生态系统提供技术支撑。未来，该数据集可以进一步扩展，例如增加更多场景、飞行器类型和传感器数据。

## 📄 摘要（原文）

> Perception of Low-Altitude Aircraft (LAA) in 3D space enables precise 3D object localization and behavior understanding. However, datasets tailored for 3D LAA perception remain scarce. To address this gap, we present LAA3D, a large-scale dataset designed to advance 3D detection and tracking of low-altitude aerial vehicles. LAA3D contains 15,000 real images and 600,000 synthetic frames, captured across diverse scenarios, including urban and suburban environments. It covers multiple aerial object categories, including electric Vertical Take-Off and Landing (eVTOL) aircraft, Micro Aerial Vehicles (MAVs), and Helicopters. Each instance is annotated with 3D bounding box, class label, and instance identity, supporting tasks such as 3D object detection, 3D multi-object tracking (MOT), and 6-DoF pose estimation. Besides, we establish the LAA3D Benchmark, integrating multiple tasks and methods with unified evaluation protocols for comparison. Furthermore, we propose MonoLAA, a monocular 3D detection baseline, achieving robust 3D localization from zoom cameras with varying focal lengths. Models pretrained on synthetic images transfer effectively to real-world data with fine-tuning, demonstrating strong sim-to-real generalization. Our LAA3D provides a comprehensive foundation for future research in low-altitude 3D object perception.

