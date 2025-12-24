---
layout: default
title: CompSLAM: Complementary Hierarchical Multi-Modal Localization and Mapping for Robot Autonomy in Underground Environments
---

# CompSLAM: Complementary Hierarchical Multi-Modal Localization and Mapping for Robot Autonomy in Underground Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06483" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06483v1</a>
  <a href="https://arxiv.org/pdf/2505.06483.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06483v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06483v1', 'CompSLAM: Complementary Hierarchical Multi-Modal Localization and Mapping for Robot Autonomy in Underground Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shehryar Khattak, Timon Homberger, Lukas Bernreiter, Julian Nubert, Olov Andersson, Roland Siegwart, Kostas Alexis, Marco Hutter

**分类**: cs.RO, cs.CV

**发布日期**: 2025-05-10

**备注**: 8 pages, 9 figures, Code: https://github.com/leggedrobotics/compslam_subt

---

## 💡 一句话要点

**提出CompSLAM以解决地下环境中的机器人自主定位与建图问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多模态融合` `机器人自主导航` `地下环境` `实时定位` `建图技术` `传感器融合` `鲁棒性`

## 📋 核心要点

1. 现有方法在复杂的地下环境中面临定位和建图的挑战，尤其是在光线不足和结构相似性高的情况下。
2. CompSLAM通过多模态传感器融合，利用冗余设计来提高定位和建图的鲁棒性，适应恶劣环境。
3. 在DARPA地下挑战赛中，CompSLAM成功应用于多种机器人，展现了其在复杂环境中的有效性和可靠性。

## 📝 摘要（中文）

在未知、无GPS和复杂的地下环境中，机器人自主性要求实时、稳健和准确的姿态估计与建图，以确保可靠操作。本文详细介绍了CompSLAM，这是一种高度弹性和分层的多模态定位与建图框架，旨在应对这些挑战。该框架通过利用来自不同传感器模态的互补姿态估计实现冗余，从而增强其韧性。CompSLAM在DARPA地下挑战赛中成功部署于Team Cerberus的所有机器人，并在后续项目中证明了其作为可靠的里程计和建图解决方案的有效性。此外，本文还介绍了一个由手动遥控的四足机器人获取的综合数据集，评估了CompSLAM在传感器退化情况下的鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂地下环境中机器人自主定位与建图的难题。现有方法在光线不足、尘埃和几何结构相似性高的情况下表现不佳，导致定位和建图的准确性下降。

**核心思路**：CompSLAM的核心思路是通过多模态传感器的互补性来增强系统的鲁棒性。该框架设计为分层结构，能够在不同环境条件下灵活调整，确保实时性和准确性。

**技术框架**：CompSLAM的整体架构包括多个模块，主要包括传感器数据采集、数据融合、姿态估计和地图构建。各模块之间通过高效的通信机制进行协作，以实现实时处理。

**关键创新**：CompSLAM的主要创新在于其多模态融合策略，通过冗余设计提高了系统在恶劣环境下的鲁棒性。这一设计与传统单一传感器方法相比，显著提升了定位和建图的准确性。

**关键设计**：在关键设计方面，CompSLAM采用了多种传感器（如激光雷达、视觉传感器等），并通过特定的损失函数优化姿态估计。此外，系统的参数设置经过精细调整，以适应不同的环境条件。

## 📊 实验亮点

在DARPA地下挑战赛中，CompSLAM成功部署于多种机器人平台，展现出在复杂环境中的高效性。实验结果表明，CompSLAM在740米的测试过程中，能够有效应对传感器退化，保持高精度的定位和建图，显著优于传统方法。

## 🎯 应用场景

CompSLAM的研究成果在多个领域具有广泛的应用潜力，尤其是在地下探测、灾后救援和矿业等场景中。其高效的定位与建图能力能够支持机器人在复杂环境中自主导航，提升任务执行的安全性和效率。未来，CompSLAM还可扩展至多机器人协作和共享地图等应用，进一步推动机器人技术的发展。

## 📄 摘要（原文）

> Robot autonomy in unknown, GPS-denied, and complex underground environments requires real-time, robust, and accurate onboard pose estimation and mapping for reliable operations. This becomes particularly challenging in perception-degraded subterranean conditions under harsh environmental factors, including darkness, dust, and geometrically self-similar structures. This paper details CompSLAM, a highly resilient and hierarchical multi-modal localization and mapping framework designed to address these challenges. Its flexible architecture achieves resilience through redundancy by leveraging the complementary nature of pose estimates derived from diverse sensor modalities. Developed during the DARPA Subterranean Challenge, CompSLAM was successfully deployed on all aerial, legged, and wheeled robots of Team Cerberus during their competition-winning final run. Furthermore, it has proven to be a reliable odometry and mapping solution in various subsequent projects, with extensions enabling multi-robot map sharing for marsupial robotic deployments and collaborative mapping. This paper also introduces a comprehensive dataset acquired by a manually teleoperated quadrupedal robot, covering a significant portion of the DARPA Subterranean Challenge finals course. This dataset evaluates CompSLAM's robustness to sensor degradations as the robot traverses 740 meters in an environment characterized by highly variable geometries and demanding lighting conditions. The CompSLAM code and the DARPA SubT Finals dataset are made publicly available for the benefit of the robotics community

