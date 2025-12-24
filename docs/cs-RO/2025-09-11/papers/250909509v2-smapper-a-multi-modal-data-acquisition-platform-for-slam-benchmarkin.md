---
layout: default
title: "SMapper: A Multi-Modal Data Acquisition Platform for SLAM Benchmarking"
---

# SMapper: A Multi-Modal Data Acquisition Platform for SLAM Benchmarking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09509" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09509v2</a>
  <a href="https://arxiv.org/pdf/2509.09509.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09509v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09509v2', 'SMapper: A Multi-Modal Data Acquisition Platform for SLAM Benchmarking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pedro Miguel Bastos Soares, Ali Tourani, Miguel Fernandez-Cortizas, Asier Bikandi-Noya, Holger Voos, Jose Luis Sanchez-Lopez

**分类**: cs.RO

**发布日期**: 2025-09-11 (更新: 2025-10-10)

**备注**: 13 pages, 5 figures, 6 tables

**🔗 代码/项目**: [PROJECT_PAGE](https://snt-arg.github.io/smapper_docs)

---

## 💡 一句话要点

**SMapper：用于SLAM基准测试的多模态数据采集平台**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `SLAM` `多模态数据` `数据集` `开放硬件` `机器人` `激光雷达` `视觉SLAM` `基准测试`

## 📋 核心要点

1. 现有SLAM数据集在传感模态、环境多样性和硬件设置可复现性方面存在局限，阻碍了相关研究的进展。
2. SMapper平台通过集成多种传感器（激光雷达、相机、IMU）并提供精确校准和同步，旨在提供高质量的多模态数据。
3. 论文发布了SMapper-light数据集，包含室内外场景，并提供了亚厘米级精度的地面真值，用于SLAM算法的基准测试。

## 📝 摘要（中文）

为了推进同步定位与地图构建（SLAM）和自主导航等领域的研究，可靠且可复现的多模态数据集至关重要。本文介绍了一种新型的开放硬件多传感器平台SMapper，专为SLAM研究设计。该设备集成了同步的激光雷达、多相机和惯性传感器，并由强大的校准和同步流程支持，确保跨模态的精确时空对齐。其开放和可复制的设计允许研究人员扩展其功能，并在手持和机器人安装场景中复现实验。此外，我们发布了SMapper-light，这是一个公开可用的SLAM数据集，包含代表性的室内和室外序列。该数据集包括紧密同步的多模态数据和来自离线激光雷达SLAM的亚厘米级精度的地面真值轨迹，以及密集的3D重建。论文还包含使用SMapper-light数据集对最先进的激光雷达和视觉SLAM框架进行的基准测试结果。通过结合开放硬件设计、可复现的数据收集和全面的基准测试，SMapper为推进SLAM算法的开发、评估和可复现性奠定了坚实的基础。

## 🔬 方法详解

**问题定义**：现有的SLAM数据集通常在传感器模态的丰富度、环境的多样性以及硬件配置的可复现性方面存在不足。这使得研究人员难以充分评估和比较不同的SLAM算法，也限制了算法在真实世界中的泛化能力。特别是缺乏精确同步的多模态数据，给多传感器融合SLAM算法的研究带来了挑战。

**核心思路**：SMapper的核心思路是构建一个开放硬件、多传感器融合的数据采集平台，并提供配套的校准和同步流程，以生成高质量、可复现的多模态数据集。通过开放硬件设计，鼓励研究人员复制和扩展平台，从而促进SLAM算法的开发和评估。

**技术框架**：SMapper平台主要包含以下几个模块：1) 硬件平台：集成了激光雷达、多相机和惯性测量单元（IMU）等多种传感器。2) 校准和同步流程：用于精确校准传感器之间的内外参数，并实现数据的时间同步。3) 数据采集软件：用于控制传感器的数据采集，并记录传感器数据。4) 数据集：包含使用SMapper平台采集的室内外场景数据，并提供地面真值轨迹和3D重建。

**关键创新**：SMapper的关键创新在于其开放硬件设计和精确的校准同步流程。开放硬件设计使得研究人员可以方便地复制和修改平台，从而满足不同的研究需求。精确的校准同步流程保证了多模态数据的时空对齐，为多传感器融合SLAM算法的研究提供了可靠的数据基础。

**关键设计**：SMapper平台采用了硬件触发同步机制，以保证传感器数据的时间同步精度。校准流程采用了基于优化的方法，以精确估计传感器之间的内外参数。SMapper-light数据集的地面真值轨迹是通过离线激光雷达SLAM算法获得的，并经过人工校正，以保证其精度。

## 📊 实验亮点

论文发布了SMapper-light数据集，该数据集包含室内和室外场景，并提供了亚厘米级精度的地面真值轨迹和密集的3D重建。在SMapper-light数据集上，论文对多种最先进的激光雷达和视觉SLAM框架进行了基准测试，为研究人员提供了一个评估和比较不同SLAM算法的平台。实验结果表明，SMapper平台采集的数据质量高，可以用于开发和评估高性能的SLAM算法。

## 🎯 应用场景

SMapper平台和SMapper-light数据集可广泛应用于机器人导航、自动驾驶、三维重建、虚拟现实等领域。该平台能够帮助研究人员开发和评估更鲁棒、更精确的SLAM算法，从而提高机器人在复杂环境中的自主导航能力。此外，该平台还可以用于构建高精度的三维地图，为虚拟现实应用提供支持。

## 📄 摘要（原文）

> Advancing research in fields such as Simultaneous Localization and Mapping (SLAM) and autonomous navigation critically depends on the availability of reliable and reproducible multimodal datasets. While several influential datasets have driven progress in these domains, they often suffer from limitations in sensing modalities, environmental diversity, and the reproducibility of the underlying hardware setups. To address these challenges, this paper introduces SMapper, a novel open-hardware, multi-sensor platform designed explicitly for, though not limited to, SLAM research. The device integrates synchronized LiDAR, multi-camera, and inertial sensing, supported by a robust calibration and synchronization pipeline that ensures precise spatio-temporal alignment across modalities. Its open and replicable design allows researchers to extend its capabilities and reproduce experiments across both handheld and robot-mounted scenarios. To demonstrate its practicality, we additionally release SMapper-light, a publicly available SLAM dataset containing representative indoor and outdoor sequences. The dataset includes tightly synchronized multimodal data and ground truth trajectories derived from offline LiDAR-based SLAM with sub-centimeter accuracy, alongside dense 3D reconstructions. Furthermore, the paper contains benchmarking results on state-of-the-art LiDAR and visual SLAM frameworks using the SMapper-light dataset. By combining open-hardware design, reproducible data collection, and comprehensive benchmarking, SMapper establishes a robust foundation for advancing SLAM algorithm development, evaluation, and reproducibility. The project's documentation, including source code, CAD models, and dataset links, is publicly available at https://snt-arg.github.io/smapper_docs.

