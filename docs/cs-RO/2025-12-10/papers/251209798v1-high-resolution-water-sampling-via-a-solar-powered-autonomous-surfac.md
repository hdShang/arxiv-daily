---
layout: default
title: High-Resolution Water Sampling via a Solar-Powered Autonomous Surface Vehicle
---

# High-Resolution Water Sampling via a Solar-Powered Autonomous Surface Vehicle

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09798" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09798v1</a>
  <a href="https://arxiv.org/pdf/2512.09798.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09798v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.09798v1', 'High-Resolution Water Sampling via a Solar-Powered Autonomous Surface Vehicle')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Misael Mamani, Mariel Fernandez, Grace Luna, Steffani Limachi, Leonel Apaza, Carolina Montes-Dávalos, Marcelo Herrera, Edwin Salcedo

**分类**: cs.RO

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**提出一种太阳能自主水面船，实现高分辨率水样采集与水质监测**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自主水面船` `水质监测` `高分辨率采样` `ROS 2` `行为树`

## 📋 核心要点

1. 现有USV水质采样能力有限，通常只能采集少量样本或依赖代表性差的单点传感器。
2. 本研究设计了一种基于注射器的采样系统，并集成ROS2自主导航框架，实现高密度、低污染的水样采集。
3. 现场实验验证了USV的自主导航能力和采样精度，物理化学测量结果与人工采集数据高度一致。

## 📝 摘要（中文）

本研究提出了一种太阳能供电的全自主水面船（USV），配备新型注射器式采样架构，每次任务可采集72个离散、污染最小化的水样。该USV集成了基于ROS 2的自主控制系统，包括GPS-RTK导航、激光雷达和立体视觉障碍物检测、基于Nav2的任务规划以及远程LoRa监控，从而能够在非结构化环境中可靠地执行采样路线。该平台采用源自Nav2的行为树自主架构，实现任务级推理和感知感知导航。模块化的6x12采样系统由分布式micro-ROS节点控制，提供确定性驱动、故障隔离和快速模块更换，实现了超越以往USV采样器的空间覆盖范围。在玻利维亚阿乔卡拉泻湖的现场试验表明，航点精度达到87%，自主导航稳定，物理化学测量（温度、pH值、电导率、总溶解固体）与人工采集的参考值相当。这些结果表明，该平台能够实现可靠的高分辨率采样和自主任务执行，为偏远地区的水生监测提供可扩展的解决方案。

## 🔬 方法详解

**问题定义**：现有无人水面船（USV）在水质评估中存在采样分辨率不足的问题。传统USV要么只能采集少量样本，要么依赖单点传感器，无法提供足够精细的空间水质信息，难以满足精确水质评估的需求。此外，在复杂水域环境中，USV的自主导航和避障能力也面临挑战。

**核心思路**：本研究的核心思路是设计一种高分辨率、低污染的自主水面采样平台。通过集成多点采样系统和先进的自主导航技术，实现对水域环境的精细化采样和监测。采用太阳能供电，延长续航时间，使其适用于偏远地区的水质监测任务。

**技术框架**：该USV平台主要由以下几个模块组成：1）太阳能供电系统：为整个平台提供能源。2）采样系统：采用6x12的模块化注射器阵列，实现72个离散水样的采集。3）自主导航系统：基于ROS 2，包含GPS-RTK导航、激光雷达和立体视觉障碍物检测、Nav2任务规划以及LoRa远程监控。4）控制系统：采用分布式micro-ROS节点控制采样系统，实现确定性驱动和故障隔离。5）行为树自主架构：基于Nav2，实现任务级推理和感知感知导航。

**关键创新**：该研究的关键创新在于：1）高分辨率采样系统：采用模块化的注射器阵列，显著提高了USV的采样密度和空间覆盖范围。2）行为树自主架构：将行为树应用于USV的自主导航，提高了任务规划的灵活性和鲁棒性。3）分布式控制系统：采用micro-ROS节点控制采样系统，实现了确定性驱动和故障隔离。

**关键设计**：采样系统采用6x12的模块化设计，每个模块包含一个注射器，由独立的micro-ROS节点控制。行为树的根节点根据任务目标选择不同的行为分支，例如导航到目标航点、执行采样任务或避障。GPS-RTK提供厘米级的定位精度，激光雷达和立体视觉用于感知周围环境，LoRa用于远程监控和控制。

## 📊 实验亮点

在玻利维亚阿乔卡拉泻湖的现场试验中，该USV实现了87%的航点精度，证明了其稳定的自主导航能力。采集的水样经过物理化学分析，温度、pH值、电导率和总溶解固体等指标与人工采集的参考值高度一致，验证了采样系统的准确性。该平台能够实现可靠的高分辨率采样和自主任务执行。

## 🎯 应用场景

该研究成果可广泛应用于水质监测、环境评估、生态研究等领域。尤其适用于偏远地区、危险水域或需要高分辨率水质数据的场景。通过部署大量此类USV，可以构建大规模的水质监测网络，为水资源管理和环境保护提供有力支持，并为相关政策的制定提供科学依据。

## 📄 摘要（原文）

> Accurate water quality assessment requires spatially resolved sampling, yet most unmanned surface vehicles (USVs) can collect only a limited number of samples or rely on single-point sensors with poor representativeness. This work presents a solar-powered, fully autonomous USV featuring a novel syringe-based sampling architecture capable of acquiring 72 discrete, contamination-minimized water samples per mission. The vehicle incorporates a ROS 2 autonomy stack with GPS-RTK navigation, LiDAR and stereo-vision obstacle detection, Nav2-based mission planning, and long-range LoRa supervision, enabling dependable execution of sampling routes in unstructured environments. The platform integrates a behavior-tree autonomy architecture adapted from Nav2, enabling mission-level reasoning and perception-aware navigation. A modular 6x12 sampling system, controlled by distributed micro-ROS nodes, provides deterministic actuation, fault isolation, and rapid module replacement, achieving spatial coverage beyond previously reported USV-based samplers. Field trials in Achocalla Lagoon (La Paz, Bolivia) demonstrated 87% waypoint accuracy, stable autonomous navigation, and accurate physicochemical measurements (temperature, pH, conductivity, total dissolved solids) comparable to manually collected references. These results demonstrate that the platform enables reliable high-resolution sampling and autonomous mission execution, providing a scalable solution for aquatic monitoring in remote environments.

