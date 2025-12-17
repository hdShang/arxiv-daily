---
layout: default
title: Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations
---

# Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations

**arXiv**: [2512.14428v1](https://arxiv.org/abs/2512.14428) | [PDF](https://arxiv.org/pdf/2512.14428.pdf)

**作者**: Aaron Kurda, Simon Steuernagel, Lukas Jung, Marcus Baum

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: 9 pages, 4 figures, submitted to International Journal of Robotics Research (IJRR)

---

## 💡 一句话要点

**Odyssey：面向GNSS拒止环境的车载激光雷达-惯性里程计数据集**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)** **3D感知与状态估计 (Perception & State Est)**

**关键词**: `激光雷达` `惯性里程计` `GNSS拒止` `数据集` `环形激光陀螺仪` `自动驾驶` `同步定位与建图`

## 📋 核心要点

1. 现有LIO/SLAM数据集在GNSS拒止环境下缺乏长期精确的地面真值，限制了相关算法的评估和研究。
2. Odyssey数据集利用导航级环形激光陀螺仪(RLG)的INS提供高精度地面真值，适用于长时间GNSS拒止环境。
3. 该数据集包含隧道、停车场、拥堵交通等多种场景，并提供三重重复轨迹和地理坐标，支持LIO、地点识别等任务。

## 📝 摘要（中文）

激光雷达-惯性里程计(LIO)和同步定位与建图(SLAM)系统的开发和评估需要精确的地面真值。全球导航卫星系统(GNSS)通常被用作基础，但其信号在受阻环境中由于多径效应或信号丢失而变得不可靠。现有数据集通过结合惯性测量单元(IMU)的测量来补偿GNSS信号的零星丢失，但常用的基于微机电系统(MEMS)或光纤陀螺仪(FOG)的系统不允许对GNSS拒止环境进行长期研究。为了弥补这一差距，我们提出了Odyssey，一个LIO数据集，专注于GNSS拒止环境，如隧道和停车场，以及其他未被充分代表但普遍存在的场景，如走走停停的交通、颠簸的道路和广阔的田野。我们的地面真值来自配备环形激光陀螺仪(RLG)的导航级惯性导航系统(INS)，与现有数据集中使用的IMU相比，具有卓越的偏置稳定性，能够对GNSS拒止环境进行长期和准确的研究。这使得Odyssey成为第一个公开提供的基于RLG的INS数据集。除了为LIO提供数据外，我们还通过所有轨迹的三重重复以及通过提供精确的地理坐标来整合外部地图数据，来支持其他任务，如地点识别。所有数据、数据加载器和其他材料都可以在https://odyssey.uni-goettingen.de/ 上在线获取。

## 🔬 方法详解

**问题定义**：现有LIO和SLAM算法的评估依赖于精确的地面真值，而GNSS在遮挡环境中信号不稳定。虽然现有数据集使用IMU进行补偿，但常用的MEMS或FOG-based IMU在长时间GNSS拒止环境中精度不足，无法提供可靠的地面真值。因此，需要一个能够在长时间GNSS拒止环境下提供高精度地面真值的数据集，以支持LIO和SLAM算法的开发和评估。

**核心思路**：Odyssey数据集的核心思路是使用导航级的惯性导航系统(INS)结合环形激光陀螺仪(RLG)来生成高精度的地面真值。RLG相比于MEMS和FOG具有更高的精度和更低的漂移，能够在长时间的GNSS拒止环境中保持较高的定位精度。通过这种方式，Odyssey数据集能够为LIO和SLAM算法提供可靠的评估基准。

**技术框架**：Odyssey数据集的采集平台包括激光雷达、相机和导航级INS。INS使用RLG作为核心传感器，提供高精度的姿态和位置信息。数据集包含多种场景，包括隧道、停车场、城市街道和开阔区域。所有轨迹都重复三次，以支持地点识别等任务。此外，数据集还提供精确的地理坐标，方便整合外部地图数据。数据采集后，使用高精度算法对INS数据进行处理，生成最终的地面真值。

**关键创新**：Odyssey数据集的关键创新在于使用了导航级的RLG-based INS来生成地面真值。这是第一个公开可用的包含RLG-based INS的LIO数据集。与现有数据集相比，Odyssey在GNSS拒止环境下的地面真值精度更高，能够支持更长时间的算法评估。

**关键设计**：Odyssey数据集的关键设计包括：1) 使用导航级RLG-based INS以获得高精度地面真值；2) 包含多种具有挑战性的GNSS拒止场景；3) 提供三重重复轨迹以支持地点识别；4) 提供精确的地理坐标以方便整合外部地图数据；5) 提供数据加载器和其他工具，方便用户使用数据集。

## 📊 实验亮点

Odyssey数据集是首个公开的包含RLG-based INS的LIO数据集，在GNSS拒止环境下具有更高的地面真值精度。数据集包含多种具有挑战性的场景，如隧道、停车场和拥堵交通，并提供三重重复轨迹和地理坐标，为LIO、SLAM和地点识别等任务提供了丰富的数据支持。该数据集为相关算法的开发和评估提供了一个重要的基准。

## 🎯 应用场景

Odyssey数据集可广泛应用于自动驾驶、机器人导航、无人机等领域。它为LIO和SLAM算法的开发、测试和评估提供了一个可靠的平台，尤其是在GNSS信号受限或不可用的环境中。该数据集能够促进相关算法在隧道、停车场、室内环境等场景中的应用，并推动自主导航技术的发展。

## 📄 摘要（原文）

> The development and evaluation of Lidar-Inertial Odometry (LIO) and Simultaneous Localization and Mapping (SLAM) systems requires a precise ground truth. The Global Navigation Satellite System (GNSS) is often used as a foundation for this, but its signals can be unreliable in obstructed environments due to multi-path effects or loss-of-signal. While existing datasets compensate for the sporadic loss of GNSS signals by incorporating Inertial Measurement Unit (IMU) measurements, the commonly used Micro-Electro-Mechanical Systems (MEMS) or Fiber Optic Gyroscope (FOG)-based systems do not permit the prolonged study of GNSS-denied environments. To close this gap, we present Odyssey, a LIO dataset with a focus on GNSS-denied environments such as tunnels and parking garages as well as other underrepresented, yet ubiquitous situations such as stop-and-go-traffic, bumpy roads and wide open fields. Our ground truth is derived from a navigation-grade Inertial Navigation System (INS) equipped with a Ring Laser Gyroscope (RLG), offering exceptional bias stability characteristics compared to IMUs used in existing datasets and enabling the prolonged and accurate study of GNSS-denied environments. This makes Odyssey the first publicly available dataset featuring a RLG-based INS. Besides providing data for LIO, we also support other tasks, such as place recognition, through the threefold repetition of all trajectories as well as the integration of external mapping data by providing precise geodetic coordinates. All data, dataloader and other material is available online at https://odyssey.uni-goettingen.de/ .

