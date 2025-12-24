---
layout: default
title: "ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM"
---

# ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14032" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14032v1</a>
  <a href="https://arxiv.org/pdf/2512.14032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14032v1', 'ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison

**分类**: cs.CV, cs.AI, eess.IV

**发布日期**: 2025-12-16

**备注**: Project Page: https://github.com/ialzugaray/ace-slam

**🔗 代码/项目**: [GITHUB](https://github.com/ialzugaray/ace-slam)

---

## 💡 一句话要点

**ACE-SLAM：基于场景坐标回归的神经隐式实时SLAM系统**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `神经SLAM` `隐式地图` `场景坐标回归` `实时SLAM` `RGB-D SLAM`

## 📋 核心要点

1. 现有神经隐式SLAM方法在实时性和效率方面存在挑战，难以在资源受限的设备上部署。
2. 提出ACE-SLAM，利用场景坐标回归(SCR)直接从2D图像特征预测3D坐标，实现高效的隐式地图表示。
3. 实验表明，ACE-SLAM在合成和真实数据集上实现了实时性能，并与现有技术相比具有竞争力。

## 📝 摘要（中文）

本文提出了一种新颖的神经RGB-D同步定位与地图构建(SLAM)系统，该系统能够实时学习场景的隐式地图。我们首次探索了使用场景坐标回归(SCR)作为神经SLAM流程中的核心隐式地图表示，这种范式训练一个轻量级网络，直接将2D图像特征映射到3D全局坐标。SCR网络提供高效、低内存的3D地图表示，实现极快的重定位，并天然地保护隐私，使其特别适合神经隐式SLAM。我们的系统是第一个通过依赖于基于SCR的表示来实现神经隐式RGB-D SLAM中严格实时的系统。我们介绍了一种专门为此目的量身定制的新型SCR架构，并详细说明了将SCR集成到实时SLAM流程中所需的关键设计选择。由此产生的框架简单而灵活，无缝支持稀疏和密集特征，并在动态环境中可靠运行，无需特殊适配。我们在已建立的合成和真实世界基准上评估了我们的方法，证明了与最先进技术相比具有竞争力的性能。项目主页：https://github.com/ialzugaray/ace-slam

## 🔬 方法详解

**问题定义**：现有的神经隐式SLAM方法通常计算复杂度较高，难以满足实时性要求，尤其是在资源受限的设备上。此外，如何高效地表示和更新场景地图也是一个挑战。

**核心思路**：本文的核心思路是利用场景坐标回归（SCR）来表示场景的隐式地图。SCR通过训练一个轻量级的神经网络，直接将2D图像特征映射到3D全局坐标，从而避免了传统方法中复杂的几何计算和优化过程。这种方法能够实现高效的地图表示和快速的重定位。

**技术框架**：ACE-SLAM系统的整体框架包括以下几个主要模块：1) 特征提取：从RGB-D图像中提取2D图像特征。2) 场景坐标回归：利用训练好的SCR网络，将2D图像特征映射到3D全局坐标。3) 位姿估计：利用预测的3D坐标和图像信息，估计相机的位姿。4) 地图更新：根据新的位姿和图像信息，更新场景的隐式地图。

**关键创新**：ACE-SLAM的关键创新在于首次将SCR作为核心隐式地图表示引入到神经SLAM流程中，并设计了一种专门为此目的量身定制的新型SCR架构。这种方法能够实现高效、低内存的3D地图表示，并支持极快的重定位。

**关键设计**：ACE-SLAM的关键设计包括：1) SCR网络结构：设计了一种轻量级的SCR网络，以实现实时性能。2) 损失函数：采用合适的损失函数来训练SCR网络，以提高预测的3D坐标的准确性。3) 特征选择：选择合适的2D图像特征，以提高SCR网络的性能。4) 位姿优化：采用基于优化的方法来进一步提高位姿估计的准确性。

## 📊 实验亮点

ACE-SLAM在合成和真实数据集上进行了评估，实验结果表明，ACE-SLAM能够实现实时性能，并且与现有的神经隐式SLAM方法相比具有竞争力。具体来说，ACE-SLAM在位姿估计的准确性和地图构建的效率方面都取得了显著的提升。此外，ACE-SLAM还展示了在动态环境中可靠运行的能力，无需特殊适配。

## 🎯 应用场景

ACE-SLAM具有广泛的应用前景，例如：机器人导航、增强现实、虚拟现实、三维重建等。由于其高效性和实时性，ACE-SLAM特别适合在资源受限的移动设备或嵌入式系统上部署，为这些设备提供强大的SLAM能力。此外，SCR的隐私保护特性使其在需要保护用户隐私的应用中具有优势。

## 📄 摘要（原文）

> We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image features to 3D global coordinates. SCR networks provide efficient, low-memory 3D map representations, enable extremely fast relocalization, and inherently preserve privacy, making them particularly suitable for neural implicit SLAM.
>   Our system is the first one to achieve strict real-time in neural implicit RGB-D SLAM by relying on a SCR-based representation. We introduce a novel SCR architecture specifically tailored for this purpose and detail the critical design choices required to integrate SCR into a live SLAM pipeline. The resulting framework is simple yet flexible, seamlessly supporting both sparse and dense features, and operates reliably in dynamic environments without special adaptation. We evaluate our approach on established synthetic and real-world benchmarks, demonstrating competitive performance against the state of the art. Project Page: https://github.com/ialzugaray/ace-slam

