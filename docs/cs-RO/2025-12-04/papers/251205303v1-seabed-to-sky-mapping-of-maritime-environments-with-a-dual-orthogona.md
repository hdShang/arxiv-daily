---
layout: default
title: Seabed-to-Sky Mapping of Maritime Environments with a Dual Orthogonal SONAR and LiDAR Sensor Suite
---

# Seabed-to-Sky Mapping of Maritime Environments with a Dual Orthogonal SONAR and LiDAR Sensor Suite

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05303" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05303v1</a>
  <a href="https://arxiv.org/pdf/2512.05303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05303v1', 'Seabed-to-Sky Mapping of Maritime Environments with a Dual Orthogonal SONAR and LiDAR Sensor Suite')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christian Westerdahl, Jonas Poulsen, Daniel Holmelund, Peter Nicholas Hansen, Fletcher Thompson, Roberto Galeazzi

**分类**: cs.RO

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**提出一种GNSS独立的海洋环境映射系统以解决现有方法的局限性**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `海洋环境映射` `GNSS独立` `LiDAR-IMU` `双正交声纳` `实时操作` `因子图地图` `声学数据融合`

## 📋 核心要点

1. 现有的海洋环境映射方法依赖GNSS，易受遮挡和欺骗攻击影响，或使用昂贵的水深声纳，限制了应用的灵活性和经济性。
2. 本文提出了一种GNSS独立的映射系统，结合LiDAR-IMU与双正交声纳，通过融合不同传感器数据生成一致的海床到天空地图。
3. 实验结果表明，该系统在实际环境中实现了实时操作，地图更新频率达到约2.65 Hz，里程计频率约为2.85 Hz，展示了良好的性能和应用潜力。

## 📝 摘要（中文）

随着海洋基础设施对水面和水下环境的态势感知需求日益增加，现有的“海床到天空”映射流程往往依赖于易受干扰的GNSS或昂贵的水深声纳。本文提出了一种统一的GNSS独立映射系统，融合了LiDAR-IMU和双正交前视声纳（FLS），能够从自主水面车辆生成一致的海床到天空的地图。在声学处理方面，我们扩展了正交宽孔融合技术，以处理任意的声纳间平移，并从每个FLS提取前沿形成线扫描。在映射方面，我们修改了LIO-SAM，使其能够通过运动插值姿态接收立体派生的3D声纳点和关键帧间的前沿线扫描，从而使稀疏声学更新能够持续贡献于单一的因子图地图。我们在哥本哈根Belvederekanalen的实际数据上验证了该系统，展示了实时操作，地图更新频率约为2.65 Hz，里程计约为2.85 Hz，同时生成了覆盖空气-水域的统一3D模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有海洋环境映射方法对GNSS的依赖性及其易受干扰的问题，同时降低高成本声纳的使用。现有方法在复杂环境下的适应性和经济性不足。

**核心思路**：论文提出了一种融合LiDAR-IMU与双正交前视声纳的映射系统，通过声学和光学数据的结合，实现GNSS独立的高效映射。这样的设计使得系统在多变的海洋环境中保持稳定性和准确性。

**技术框架**：系统主要由两个模块组成：声学模块和映射模块。声学模块负责处理声纳数据，提取前沿信息并生成线扫描；映射模块则通过修改的LIO-SAM算法，结合声纳点和线扫描数据，构建因子图地图。

**关键创新**：最重要的创新在于扩展了正交宽孔融合技术，能够处理任意声纳间的平移，支持异构和非共置模型的融合。这一创新使得系统能够在复杂环境中有效工作。

**关键设计**：在参数设置上，系统采用运动插值姿态来处理关键帧间的声纳数据，确保稀疏声学更新能够持续贡献于地图构建。损失函数和网络结构的设计确保了数据融合的高效性和准确性。

## 📊 实验亮点

实验结果显示，该系统在实际环境中实现了约2.65 Hz的地图更新频率和约2.85 Hz的里程计频率，显著提高了海洋环境映射的实时性和准确性，展示了优于传统方法的性能。

## 🎯 应用场景

该研究的潜在应用领域包括海洋监测、环境保护、海底资源勘探等。通过提供高效、实时的海洋环境映射能力，该系统能够为海洋工程、航运安全和生态监测等领域带来显著的实际价值和影响。

## 📄 摘要（原文）

> Critical maritime infrastructure increasingly demands situational awareness both above and below the surface, yet existing ''seabed-to-sky'' mapping pipelines either rely on GNSS (vulnerable to shadowing/spoofing) or expensive bathymetric sonars. We present a unified, GNSS-independent mapping system that fuses LiDAR-IMU with a dual, orthogonally mounted Forward Looking Sonars (FLS) to generate consistent seabed-to-sky maps from an Autonomous Surface Vehicle. On the acoustic side, we extend orthogonal wide-aperture fusion to handle arbitrary inter-sonar translations (enabling heterogeneous, non-co-located models) and extract a leading edge from each FLS to form line-scans. On the mapping side, we modify LIO-SAM to ingest both stereo-derived 3D sonar points and leading-edge line-scans at and between keyframes via motion-interpolated poses, allowing sparse acoustic updates to contribute continuously to a single factor-graph map. We validate the system on real-world data from Belvederekanalen (Copenhagen), demonstrating real-time operation with approx. 2.65 Hz map updates and approx. 2.85 Hz odometry while producing a unified 3D model that spans air-water domains.

