---
layout: default
title: Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations
---

# Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14428" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14428</a>
  <a href="https://arxiv.org/pdf/2512.14428.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14428" onclick="toggleFavorite(this, '2512.14428', 'Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aaron Kurda, Simon Steuernagel, Lukas Jung, Marcus Baum

**分类**: cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Odyssey：面向GNSS拒止环境的车载激光雷达-惯性里程计数据集**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `激光雷达` `惯性里程计` `GNSS拒止` `数据集` `环形激光陀螺仪` `自动驾驶` `同步定位与地图构建`

## 📋 核心要点

1. 现有LIO/SLAM数据集在GNSS拒止环境下精度不足，因为依赖MEMS或FOG的IMU难以长时间保持高精度。
2. Odyssey数据集使用基于环形激光陀螺仪(RLG)的导航级INS提供高精度地面真值，特别适用于GNSS拒止环境。
3. 该数据集包含隧道、停车场、拥堵交通等多种场景，并提供三重重复轨迹和大地坐标，支持LIO、地点识别等任务。

## 📝 摘要（中文）

激光雷达-惯性里程计(LIO)和同步定位与地图构建(SLAM)系统的开发与评估需要精确的地面真值。全球导航卫星系统(GNSS)通常被用作基础，但在受阻环境中，由于多径效应或信号丢失，其信号可能不可靠。现有数据集通过结合惯性测量单元(IMU)测量来补偿GNSS信号的零星丢失，但常用的基于微机电系统(MEMS)或光纤陀螺仪(FOG)的系统不允许对GNSS拒止环境进行长期研究。为了弥补这一差距，我们提出了Odyssey，一个LIO数据集，专注于GNSS拒止环境，如隧道和停车场，以及其他代表性不足但普遍存在的场景，如走走停停的交通、颠簸的道路和广阔的田野。我们的地面真值来自配备环形激光陀螺仪(RLG)的导航级惯性导航系统(INS)，与现有数据集中使用的IMU相比，具有卓越的偏置稳定性，能够对GNSS拒止环境进行长期准确的研究。这使得Odyssey成为第一个公开提供的基于RLG的INS数据集。除了为LIO提供数据外，我们还通过所有轨迹的三重重复以及通过提供精确的大地坐标来整合外部地图数据，来支持其他任务，如地点识别。所有数据、数据加载器和其他材料都可以在网上获得。

## 🔬 方法详解

**问题定义**：现有LIO和SLAM系统在GNSS信号弱或缺失的环境中，例如隧道、停车场等，定位精度会显著下降。这是因为常用的MEMS或FOG IMU的长期漂移误差较大，难以提供可靠的惯性导航信息，从而影响整体定位性能。因此，需要一个能够在GNSS拒止环境下提供高精度地面真值的数据集，用于LIO/SLAM算法的评估和改进。

**核心思路**：Odyssey数据集的核心思路是利用高精度的导航级惯性导航系统(INS)来生成地面真值。该INS配备了环形激光陀螺仪(RLG)，相比于MEMS和FOG，RLG具有更高的精度和更好的长期稳定性，能够有效抑制漂移误差，从而在GNSS拒止环境下提供可靠的定位信息。

**技术框架**：Odyssey数据集的采集平台是一个车载系统，集成了激光雷达、惯性测量单元(IMU)和全球导航卫星系统(GNSS)。其中，最关键的组件是导航级INS，它负责生成高精度的地面真值。数据集的采集过程包括在各种具有挑战性的环境中行驶，例如隧道、停车场、拥堵交通、颠簸道路和开阔场地。为了支持地点识别等任务，每条轨迹都重复采集了三次。此外，数据集还提供了精确的大地坐标，方便用户整合外部地图数据。

**关键创新**：Odyssey数据集最关键的创新在于使用了基于环形激光陀螺仪(RLG)的导航级INS来生成地面真值。这是第一个公开提供的包含RLG-based INS的数据集。与现有数据集常用的MEMS或FOG IMU相比，RLG具有更高的精度和更好的长期稳定性，能够有效抑制漂移误差，从而在GNSS拒止环境下提供更可靠的定位信息。

**关键设计**：Odyssey数据集的关键设计包括：1) 使用导航级INS生成高精度地面真值；2) 包含多种具有挑战性的GNSS拒止环境；3) 提供三重重复轨迹，支持地点识别等任务；4) 提供精确的大地坐标，方便整合外部地图数据；5) 提供数据加载器和其他相关工具，方便用户使用。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14428/figures/titleimage_lowres.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14428/figures/trajectory_parkhaus_lowres.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14428/figures/trajectory_marktplatz_lowres.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Odyssey数据集的关键亮点在于其高精度的地面真值，由基于环形激光陀螺仪(RLG)的导航级INS生成。与现有数据集相比，Odyssey在GNSS拒止环境下能够提供更可靠的定位信息，为LIO/SLAM算法的评估和改进提供了有力支持。此外，数据集包含多种具有挑战性的场景，并提供三重重复轨迹和大地坐标，为各种研究任务提供了丰富的资源。

## 🎯 应用场景

Odyssey数据集可广泛应用于自动驾驶、机器人导航、无人机等领域，尤其是在GNSS信号受限或不可用的环境中。该数据集能够帮助研究人员开发和评估更鲁棒、更精确的LIO/SLAM算法，从而提高自动驾驶车辆在复杂环境下的定位和导航能力，提升机器人和无人机在室内或地下环境中的自主作业能力。

## 📄 摘要（原文）

> The development and evaluation of Lidar-Inertial Odometry (LIO) and Simultaneous Localization and Mapping (SLAM) systems requires a precise ground truth. The Global Navigation Satellite System (GNSS) is often used as a foundation for this, but its signals can be unreliable in obstructed environments due to multi-path effects or loss-of-signal. While existing datasets compensate for the sporadic loss of GNSS signals by incorporating Inertial Measurement Unit (IMU) measurements, the commonly used Micro-Electro-Mechanical Systems (MEMS) or Fiber Optic Gyroscope (FOG)-based systems do not permit the prolonged study of GNSS-denied environments. To close this gap, we present Odyssey, a LIO dataset with a focus on GNSS-denied environments such as tunnels and parking garages as well as other underrepresented, yet ubiquitous situations such as stop-and-go-traffic, bumpy roads and wide open fields. Our ground truth is derived from a navigation-grade Inertial Navigation System (INS) equipped with a Ring Laser Gyroscope (RLG), offering exceptional bias stability characteristics compared to IMUs used in existing datasets and enabling the prolonged and accurate study of GNSS-denied environments. This makes Odyssey the first publicly available dataset featuring a RLG-based INS. Besides providing data for LIO, we also support other tasks, such as place recognition, through the threefold repetition of all trajectories as well as the integration of external mapping data by providing precise geodetic coordinates. All data, dataloader and other material is available online atthis https URL.

