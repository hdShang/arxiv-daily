---
layout: default
title: "Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations"
---

# Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14428" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14428v1</a>
  <a href="https://arxiv.org/pdf/2512.14428.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14428v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14428v1', 'Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aaron Kurda, Simon Steuernagel, Lukas Jung, Marcus Baum

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: 9 pages, 4 figures, submitted to International Journal of Robotics Research (IJRR)

---

## 💡 一句话要点

**Odyssey：面向GNSS拒止环境的车载激光雷达-惯性里程计数据集**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `激光雷达` `惯性里程计` `GNSS拒止` `数据集` `环形激光陀螺仪` `自动驾驶` `同步定位与建图`

## 📋 核心要点

1. 现有LIO/SLAM数据集在GNSS拒止环境下精度不足，因为常用MEMS/FOG IMU的长期稳定性有限。
2. Odyssey数据集使用基于环形激光陀螺仪(RLG)的导航级INS提供高精度地面真值，尤其适用于GNSS拒止环境。
3. 该数据集包含隧道、停车场、拥堵交通等场景，并提供三重重复轨迹和大地坐标，支持多种任务。

## 📝 摘要（中文）

激光雷达-惯性里程计(LIO)和同步定位与建图(SLAM)系统的开发和评估需要精确的地面真值。全球导航卫星系统(GNSS)通常被用作基础，但在受阻环境中，由于多径效应或信号丢失，其信号可能不可靠。现有数据集通过结合惯性测量单元(IMU)的测量来补偿GNSS信号的零星丢失，但常用的基于微机电系统(MEMS)或光纤陀螺仪(FOG)的系统不允许对GNSS拒止环境进行长期研究。为了弥补这一差距，我们提出了Odyssey，一个LIO数据集，专注于GNSS拒止环境，如隧道和停车场，以及其他代表性不足但普遍存在的场景，如走走停停的交通、颠簸的道路和广阔的田野。我们的地面真值来自配备环形激光陀螺仪(RLG)的导航级惯性导航系统(INS)，与现有数据集中使用的IMU相比，具有出色的偏置稳定性，能够对GNSS拒止环境进行长期准确的研究。这使得Odyssey成为第一个公开提供的基于RLG的INS数据集。除了为LIO提供数据外，我们还通过所有轨迹的三重重复以及通过提供精确的大地坐标来整合外部地图数据，来支持其他任务，如地点识别。所有数据、数据加载器和其他材料都可以在https://odyssey.uni-goettingen.de/上在线获取。

## 🔬 方法详解

**问题定义**：现有LIO和SLAM算法在GNSS信号受限或完全缺失的环境中，例如隧道、停车场等，难以获得可靠的定位结果。这是因为常用的MEMS或FOG IMU存在较大的漂移误差，长时间运行后误差累积严重，导致定位精度下降。因此，需要一种能够在GNSS拒止环境下提供高精度地面真值的数据集，以便于LIO/SLAM算法的开发和评估。

**核心思路**：Odyssey数据集的核心思路是利用高精度的导航级惯性导航系统(INS)来生成地面真值。该INS配备了环形激光陀螺仪(RLG)，相比于MEMS和FOG，RLG具有更高的精度和更好的长期稳定性，能够有效抑制漂移误差的累积。通过RLG-INS提供的高精度姿态和位置信息，可以为LIO/SLAM算法提供可靠的参考。

**技术框架**：Odyssey数据集的采集平台包括车载激光雷达、惯性测量单元(IMU)和导航级惯性导航系统(INS)。数据采集流程如下：首先，车辆在各种场景下行驶，同时采集激光雷达点云、IMU数据和INS数据。然后，利用INS数据生成高精度的地面真值轨迹。最后，将激光雷达点云、IMU数据和地面真值轨迹进行同步和校准，形成最终的数据集。该数据集还包含三重重复轨迹，用于地点识别等任务。

**关键创新**：Odyssey数据集最关键的创新点在于使用了基于环形激光陀螺仪(RLG)的导航级INS来生成地面真值。这是第一个公开可用的包含RLG-INS的数据集。与现有数据集常用的MEMS或FOG IMU相比，RLG具有更高的精度和更好的长期稳定性，能够提供更可靠的地面真值，尤其是在GNSS拒止环境下。

**关键设计**：Odyssey数据集的关键设计包括：1) 使用导航级RLG-INS生成高精度地面真值；2) 包含多种具有挑战性的GNSS拒止环境，如隧道和停车场；3) 提供三重重复轨迹，用于地点识别等任务；4) 提供精确的大地坐标，方便与其他地图数据进行整合。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14428v1/figures/titleimage_lowres.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14428v1/figures/trajectory_parkhaus_lowres.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14428v1/figures/trajectory_marktplatz_lowres.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Odyssey数据集的关键亮点在于其高精度的地面真值，由基于环形激光陀螺仪(RLG)的导航级INS生成。与现有数据集相比，Odyssey在GNSS拒止环境下能够提供更可靠的定位参考。此外，该数据集包含多种具有挑战性的场景，如隧道、停车场、拥堵交通等，为LIO/SLAM算法的鲁棒性测试提供了良好的平台。三重重复轨迹的设计也为地点识别任务提供了便利。

## 🎯 应用场景

Odyssey数据集可广泛应用于自动驾驶、机器人导航、无人机等领域。尤其是在GNSS信号受限或缺失的环境中，如室内、隧道、城市峡谷等，该数据集能够帮助研究人员开发和评估更鲁棒、更精确的LIO/SLAM算法。此外，该数据集还可用于地点识别、地图构建等任务，具有重要的实际应用价值。

## 📄 摘要（原文）

> The development and evaluation of Lidar-Inertial Odometry (LIO) and Simultaneous Localization and Mapping (SLAM) systems requires a precise ground truth. The Global Navigation Satellite System (GNSS) is often used as a foundation for this, but its signals can be unreliable in obstructed environments due to multi-path effects or loss-of-signal. While existing datasets compensate for the sporadic loss of GNSS signals by incorporating Inertial Measurement Unit (IMU) measurements, the commonly used Micro-Electro-Mechanical Systems (MEMS) or Fiber Optic Gyroscope (FOG)-based systems do not permit the prolonged study of GNSS-denied environments. To close this gap, we present Odyssey, a LIO dataset with a focus on GNSS-denied environments such as tunnels and parking garages as well as other underrepresented, yet ubiquitous situations such as stop-and-go-traffic, bumpy roads and wide open fields. Our ground truth is derived from a navigation-grade Inertial Navigation System (INS) equipped with a Ring Laser Gyroscope (RLG), offering exceptional bias stability characteristics compared to IMUs used in existing datasets and enabling the prolonged and accurate study of GNSS-denied environments. This makes Odyssey the first publicly available dataset featuring a RLG-based INS. Besides providing data for LIO, we also support other tasks, such as place recognition, through the threefold repetition of all trajectories as well as the integration of external mapping data by providing precise geodetic coordinates. All data, dataloader and other material is available online at https://odyssey.uni-goettingen.de/ .

