---
layout: default
title: "Super-LIO: A Robust and Efficient LiDAR-Inertial Odometry System with a Compact Mapping Strategy"
---

# Super-LIO: A Robust and Efficient LiDAR-Inertial Odometry System with a Compact Mapping Strategy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05723" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05723v1</a>
  <a href="https://arxiv.org/pdf/2509.05723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05723v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05723v1', 'Super-LIO: A Robust and Efficient LiDAR-Inertial Odometry System with a Compact Mapping Strategy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liansheng Wang, Xinke Zhang, Chenhui Li, Dongjiao He, Yihan Pan, Jianjun Yi

**分类**: cs.RO

**发布日期**: 2025-09-06

**备注**: 8 pages, 5 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Liansheng-Wang/Super-LIO.git)

---

## 💡 一句话要点

**提出Super-LIO以解决资源受限平台的LiDAR惯性测程问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LiDAR惯性测程` `八叉体体素` `映射更新` `启发式KNN` `自主系统` `高效算法` `资源受限平台`

## 📋 核心要点

1. 现有的LiDAR惯性测程系统在资源受限平台上难以实现高效和准确的性能，面临计算和内存的双重挑战。
2. Super-LIO提出了一种紧凑的八叉体体素映射结构OctVox，结合启发式KNN策略，旨在提高映射效率和准确性。
3. 实验结果显示，Super-LIO在X86和ARM平台上处理每帧的速度比现有最先进技术快约73%，且CPU资源消耗更低。

## 📝 摘要（中文）

LiDAR惯性测程（LIO）是自主系统的基础技术，但在资源受限平台上的应用面临计算和内存限制的挑战。我们提出了Super-LIO，一个高性能且准确的LIO系统，适用于空中机器人和移动自主系统等应用。Super-LIO的核心是一个紧凑的八叉体体素映射结构OctVox，限制每个体素为八个融合的子体素，从而实现严格的点密度控制和增量去噪。此外，Super-LIO设计了一种启发式引导的KNN策略（HKNN），通过利用空间局部性加速对应搜索，进一步减少运行时开销。我们在多个公开数据集和自收集数据集上评估了该系统，结果表明Super-LIO在效率和鲁棒性方面表现优越，同时保持竞争力的准确性。

## 🔬 方法详解

**问题定义**：本论文旨在解决在资源受限平台上实现高效且准确的LiDAR惯性测程（LIO）系统的问题。现有方法在计算和内存使用上存在明显不足，限制了其在实际应用中的部署。

**核心思路**：Super-LIO的核心思想是采用紧凑的八叉体体素映射结构OctVox，通过限制每个体素的子体素数量来控制点密度，并在映射更新过程中实现增量去噪。这种设计使得映射结构既简单又高效，便于与现有LIO框架集成。

**技术框架**：Super-LIO的整体架构包括数据采集、映射更新和对应搜索三个主要模块。首先，通过LiDAR和惯性传感器获取数据，然后使用OctVox进行映射更新，最后通过启发式KNN策略加速对应搜索。

**关键创新**：Super-LIO的关键创新在于OctVox映射结构和启发式KNN策略的结合。OctVox通过限制子体素数量实现了高效的点密度控制，而HKNN策略则通过空间局部性加速了对应搜索，与现有方法相比显著降低了计算开销。

**关键设计**：在OctVox中，每个体素最多包含八个子体素，确保了映射的精度和效率。HKNN策略利用空间局部性进行对应搜索，减少了不必要的计算，提升了整体运行速度。

## 📊 实验亮点

在实验中，Super-LIO在多个公开数据集和自收集数据集上表现出色，处理每帧的速度比现有最先进技术快约73%。此外，Super-LIO在X86和ARM平台上均展现出优越的效率和鲁棒性，同时保持了竞争力的准确性，充分证明了其在资源受限环境中的应用潜力。

## 🎯 应用场景

Super-LIO具有广泛的潜在应用场景，特别是在空中机器人、移动自主系统及其他需要实时环境感知的领域。其高效的映射和定位能力使其能够在复杂环境中实现自主导航，提升了自主系统的智能化水平。未来，Super-LIO可能在智能交通、无人驾驶和机器人等领域发挥重要作用。

## 📄 摘要（原文）

> LiDAR-Inertial Odometry (LIO) is a foundational technique for autonomous systems, yet its deployment on resource-constrained platforms remains challenging due to computational and memory limitations. We propose Super-LIO, a robust LIO system that demands both high performance and accuracy, ideal for applications such as aerial robots and mobile autonomous systems. At the core of Super-LIO is a compact octo-voxel-based map structure, termed OctVox, that limits each voxel to eight fused subvoxels, enabling strict point density control and incremental denoising during map updates. This design enables a simple yet efficient and accurate map structure, which can be easily integrated into existing LIO frameworks. Additionally, Super-LIO designs a heuristic-guided KNN strategy (HKNN) that accelerates the correspondence search by leveraging spatial locality, further reducing runtime overhead. We evaluated the proposed system using four publicly available datasets and several self-collected datasets, totaling more than 30 sequences. Extensive testing on both X86 and ARM platforms confirms that Super-LIO offers superior efficiency and robustness, while maintaining competitive accuracy. Super-LIO processes each frame approximately 73% faster than SOTA, while consuming less CPU resources. The system is fully open-source and plug-and-play compatible with a wide range of LiDAR sensors and platforms. The implementation is available at: https://github.com/Liansheng-Wang/Super-LIO.git

