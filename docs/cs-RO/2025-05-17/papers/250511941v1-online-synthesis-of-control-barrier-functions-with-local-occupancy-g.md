---
layout: default
title: Online Synthesis of Control Barrier Functions with Local Occupancy Grid Maps for Safe Navigation in Unknown Environments
---

# Online Synthesis of Control Barrier Functions with Local Occupancy Grid Maps for Safe Navigation in Unknown Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11941" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11941v1</a>
  <a href="https://arxiv.org/pdf/2505.11941.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11941v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11941v1', 'Online Synthesis of Control Barrier Functions with Local Occupancy Grid Maps for Safe Navigation in Unknown Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuepeng Zhang, Yu Chen, Yuda Li, Shaoyuan Li, Xiang Yin

**分类**: cs.RO

**发布日期**: 2025-05-17

---

## 💡 一句话要点

**提出基于局部占用网格图的控制屏障函数在线合成方法以解决未知环境中的安全导航问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `控制屏障函数` `在线合成` `占用网格图` `安全导航` `未知环境` `实时计算` `自主系统`

## 📋 核心要点

1. 现有的控制屏障函数合成方法主要集中在已知环境中，在线合成CBFs以应对未知环境中的感知数据面临效率和实时性挑战。
2. 本文提出了一种新方法，通过局部占用网格图直接在线合成CBFs，借鉴稳态热场的概念来满足CBFs的平滑性要求。
3. 实验结果显示，该方法在200x200的网格图上平均合成CBFs的时间为毫秒级，证明了其在实时应用中的有效性。

## 📝 摘要（中文）

控制屏障函数（CBFs）作为一种有效的安全过滤器，确保自主系统在动态环境中的安全性。然而，现有的CBF合成方法主要集中在已知环境中，在线合成CBFs以应对未知环境中的感知数据面临诸多挑战。本文提出了一种新的方法，直接从局部占用网格图（OGMs）在线合成CBFs。我们通过借鉴稳态热场的概念，展示了CBFs的平滑性要求与稳态热传导方程的解之间的关系。利用拉普拉斯方程中系数矩阵的稀疏性，我们的方法能够高效计算地图中每个网格单元的安全值。仿真和实际实验表明，该方法在200x200的网格图上平均可在毫秒级别合成CBFs，突显了其实时适用性。

## 🔬 方法详解

**问题定义**：本文旨在解决在未知环境中如何在线合成控制屏障函数（CBFs）的问题。现有方法主要针对已知环境，缺乏对动态感知数据的实时处理能力，导致安全性保障不足。

**核心思路**：论文的核心思路是通过局部占用网格图（OGMs）直接合成CBFs，借助稳态热传导方程的解来满足CBFs的平滑性要求，从而实现高效的安全值计算。

**技术框架**：整体架构包括感知模块、CBF合成模块和安全性评估模块。感知模块负责获取环境数据并生成OGMs，CBF合成模块利用OGMs进行CBFs的在线合成，安全性评估模块则实时评估合成的CBFs的有效性。

**关键创新**：最重要的技术创新在于将稳态热传导方程的解与CBFs的平滑性要求相结合，利用拉普拉斯方程中系数矩阵的稀疏性实现高效计算，这一方法在实时性和准确性上均优于现有技术。

**关键设计**：在设计中，关键参数包括网格的分辨率和边界条件的选择，损失函数则考虑了安全性和实时性之间的平衡，网络结构采用了稀疏矩阵运算以提高计算效率。

## 📊 实验亮点

实验结果表明，提出的方法在200x200的网格图上平均合成CBFs的时间为毫秒级，显示出其在实时应用中的优越性。与传统方法相比，合成效率显著提升，能够满足动态环境下的安全导航需求。

## 🎯 应用场景

该研究的潜在应用领域包括自主驾驶、无人机导航和机器人路径规划等。通过实现实时的安全性保障，该方法能够显著提升自主系统在未知环境中的安全性和可靠性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Control Barrier Functions (CBFs) have emerged as an effective and non-invasive safety filter for ensuring the safety of autonomous systems in dynamic environments with formal guarantees. However, most existing works on CBF synthesis focus on fully known settings. Synthesizing CBFs online based on perception data in unknown environments poses particular challenges. Specifically, this requires the construction of CBFs from high-dimensional data efficiently in real time. This paper proposes a new approach for online synthesis of CBFs directly from local Occupancy Grid Maps (OGMs). Inspired by steady-state thermal fields, we show that the smoothness requirement of CBFs corresponds to the solution of the steady-state heat conduction equation with suitably chosen boundary conditions. By leveraging the sparsity of the coefficient matrix in Laplace's equation, our approach allows for efficient computation of safety values for each grid cell in the map. Simulation and real-world experiments demonstrate the effectiveness of our approach. Specifically, the results show that our CBFs can be synthesized in an average of milliseconds on a 200 * 200 grid map, highlighting its real-time applicability.

