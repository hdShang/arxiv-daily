---
layout: default
title: "Pixels-to-Graph: Real-time Integration of Building Information Models and Scene Graphs for Semantic-Geometric Human-Robot Understanding"
---

# Pixels-to-Graph: Real-time Integration of Building Information Models and Scene Graphs for Semantic-Geometric Human-Robot Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22593" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22593v1</a>
  <a href="https://arxiv.org/pdf/2506.22593.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22593v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22593v1', 'Pixels-to-Graph: Real-time Integration of Building Information Models and Scene Graphs for Semantic-Geometric Human-Robot Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonello Longo, Chanyoung Chung, Matteo Palieri, Sung-Kyun Kim, Ali Agha, Cataldo Guaragnella, Shehryar Khattak

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-06-27

**备注**: Paper accepted to 2025 IEEE International Conference on Automation Science and Engineering (CASE)

---

## 💡 一句话要点

**提出Pixels-to-Graph方法以解决人机协作中的环境理解问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自主机器人` `环境理解` `建筑信息模型` `实时处理` `场景图生成`

## 📋 核心要点

1. 现有方法在机器人与人类操作员之间的环境理解上存在差距，尤其是在高层次表示与低层次几何信息之间的转换。
2. 本文提出的Pix2G方法通过实时生成结构化场景图，解决了从图像像素和LiDAR地图到环境表示的转换问题。
3. 实验结果表明，Pix2G方法在复杂环境中的实时探索和映射能力显著提升，验证了其有效性和实用性。

## 📝 摘要（中文）

随着自主机器人在高风险应用中的关键角色日益增强，机器人与人类操作员之间的高效合作与理解变得至关重要。传统的机器人规划通常依赖于3D几何信息，而人类操作员更习惯于使用高层次的环境表示，如建筑信息模型（BIM）的2D地图。为此，本文提出了一种名为Pixels-to-Graph（Pix2G）的新方法，能够实时从图像像素和LiDAR地图生成结构化场景图，旨在实现资源受限的机器人平台在未知环境中的自主探索。该方法在CPU上运行，输出去噪的2D环境地图和结构分割的3D点云，二者通过多层图进行无缝连接。通过使用NASA JPL NeBula-Spot机器人进行的真实世界实验，验证了该方法在复杂环境中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人与人类操作员之间在环境理解上的差距，特别是如何将高层次的2D建筑信息模型（BIM）与机器人所需的3D几何信息有效结合。现有方法通常依赖于复杂的3D几何数据，难以满足实时性和资源限制的需求。

**核心思路**：Pix2G方法的核心思想是通过实时处理图像像素和LiDAR数据，生成结构化的场景图，从而实现高效的环境理解。这种设计使得机器人能够在资源受限的情况下，快速适应未知环境。

**技术框架**：该方法的整体架构包括图像处理模块和LiDAR数据处理模块，二者结合生成去噪的2D环境地图和结构分割的3D点云。最终，利用多层图将这些信息进行整合，形成一个全面的环境表示。

**关键创新**：Pix2G的主要创新在于其轻量级设计，能够在CPU上高效运行，避免了对高性能GPU的依赖。此外，通过多层图的构建，增强了信息的层次性和可读性，这是与现有方法的本质区别。

**关键设计**：在技术细节上，Pix2G采用了特定的去噪算法和结构分割技术，以确保生成的2D和3D数据的准确性和一致性。同时，设计了适合CPU计算的高效算法，以满足实时处理的需求。

## 📊 实验亮点

在真实世界实验中，使用NASA JPL NeBula-Spot机器人进行的测试表明，Pix2G方法能够在复杂的车库和城市办公室环境中实现实时探索和映射，显著提高了环境理解的效率和准确性，验证了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、工业自动化和救援任务等场景。通过提高机器人对环境的理解能力，能够更好地支持人类操作员在复杂和危险环境中的决策与行动，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Autonomous robots are increasingly playing key roles as support platforms for human operators in high-risk, dangerous applications. To accomplish challenging tasks, an efficient human-robot cooperation and understanding is required. While typically robotic planning leverages 3D geometric information, human operators are accustomed to a high-level compact representation of the environment, like top-down 2D maps representing the Building Information Model (BIM). 3D scene graphs have emerged as a powerful tool to bridge the gap between human readable 2D BIM and the robot 3D maps. In this work, we introduce Pixels-to-Graph (Pix2G), a novel lightweight method to generate structured scene graphs from image pixels and LiDAR maps in real-time for the autonomous exploration of unknown environments on resource-constrained robot platforms. To satisfy onboard compute constraints, the framework is designed to perform all operation on CPU only. The method output are a de-noised 2D top-down environment map and a structure-segmented 3D pointcloud which are seamlessly connected using a multi-layer graph abstracting information from object-level up to the building-level. The proposed method is quantitatively and qualitatively evaluated during real-world experiments performed using the NASA JPL NeBula-Spot legged robot to autonomously explore and map cluttered garage and urban office like environments in real-time.

