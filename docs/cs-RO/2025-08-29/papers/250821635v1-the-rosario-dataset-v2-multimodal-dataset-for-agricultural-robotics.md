---
layout: default
title: "The Rosario Dataset v2: Multimodal Dataset for Agricultural Robotics"
---

# The Rosario Dataset v2: Multimodal Dataset for Agricultural Robotics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21635" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21635v1</a>
  <a href="https://arxiv.org/pdf/2508.21635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21635v1', 'The Rosario Dataset v2: Multimodal Dataset for Agricultural Robotics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicolas Soncini, Javier Cremona, Erica Vidal, Maximiliano García, Gastón Castro, Taihú Pire

**分类**: cs.RO, cs.CV, eess.SY

**发布日期**: 2025-08-29

**备注**: First published on The International Journal of Robotics Research: https://journals.sagepub.com/doi/10.1177/02783649251368909

**期刊**: The Rosario dataset v2: Multi-modal dataset for agricultural robotics. The International Journal of Robotics Research. 2025;0(0)

**DOI**: [10.1177/02783649251368909](https://doi.org/10.1177/02783649251368909)

**🔗 代码/项目**: [PROJECT_PAGE](https://cifasis.github.io/rosariov2/)

---

## 💡 一句话要点

**提出多模态数据集以解决农业机器人定位与导航问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态数据集` `农业机器人` `SLAM算法` `传感器融合` `定位与导航` `精准农业` `数据采集系统`

## 📋 核心要点

1. 现有农业机器人在复杂环境中面临定位和导航的挑战，尤其是光照变化和地形不平等问题。
2. 本文提出了一个多模态数据集，旨在为农业机器人提供丰富的传感器数据，以支持算法的开发与评估。
3. 通过在数据集上运行现有的多模态SLAM方法，揭示了这些方法在农业环境中的应用局限性。

## 📝 摘要（中文）

本文介绍了在大豆作物田中收集的多模态数据集，包含超过两小时的传感器记录数据，涉及立体红外相机、彩色相机、加速度计、陀螺仪、磁力计、GNSS（单点定位、实时动态和后处理动态）以及轮子里程计。该数据集捕捉了农业环境中机器人面临的关键挑战，包括自然光照变化、运动模糊、崎岖地形和长时间的感知混叠序列。通过解决这些复杂性，数据集旨在支持农业机器人中定位、地图构建、感知和导航等先进算法的开发和基准测试。数据采集系统设计满足评估多模态SLAM系统的关键要求，包括传感器的硬件同步、6自由度的真实轨迹和长轨迹上的回环。

## 🔬 方法详解

**问题定义**：本文旨在解决农业机器人在复杂环境中进行定位和导航时面临的挑战，现有方法在自然光照变化和地形复杂性下表现不佳。

**核心思路**：通过构建一个多模态数据集，提供丰富的传感器数据，帮助研究人员开发和评估更先进的SLAM算法，以应对农业环境的特殊需求。

**技术框架**：数据集包括多种传感器数据，设计了硬件同步机制，确保数据的准确性和一致性。主要模块包括数据采集、数据处理和算法评估。

**关键创新**：数据集的创新之处在于其多模态特性和对农业环境挑战的针对性，提供了真实的6自由度地面真值数据，支持长轨迹的回环检测。

**关键设计**：在数据采集过程中，采用了多种传感器的组合，确保了数据的多样性和丰富性，特别是在光照和地形变化下的表现。

## 📊 实验亮点

实验结果表明，现有的多模态SLAM方法在农业环境中存在显著的性能限制，尤其是在处理光照变化和地形复杂性时。通过使用该数据集，研究人员能够识别并改进这些方法，推动农业机器人技术的进步。

## 🎯 应用场景

该研究的潜在应用领域包括农业机器人自主导航、作物监测和精准农业。通过提供多模态数据集，研究人员可以开发更为鲁棒的算法，提升农业生产效率，降低人工成本，推动智能农业的发展。

## 📄 摘要（原文）

> We present a multi-modal dataset collected in a soybean crop field, comprising over two hours of recorded data from sensors such as stereo infrared camera, color camera, accelerometer, gyroscope, magnetometer, GNSS (Single Point Positioning, Real-Time Kinematic and Post-Processed Kinematic), and wheel odometry. This dataset captures key challenges inherent to robotics in agricultural environments, including variations in natural lighting, motion blur, rough terrain, and long, perceptually aliased sequences. By addressing these complexities, the dataset aims to support the development and benchmarking of advanced algorithms for localization, mapping, perception, and navigation in agricultural robotics. The platform and data collection system is designed to meet the key requirements for evaluating multi-modal SLAM systems, including hardware synchronization of sensors, 6-DOF ground truth and loops on long trajectories.
>   We run multimodal state-of-the art SLAM methods on the dataset, showcasing the existing limitations in their application on agricultural settings. The dataset and utilities to work with it are released on https://cifasis.github.io/rosariov2/.

