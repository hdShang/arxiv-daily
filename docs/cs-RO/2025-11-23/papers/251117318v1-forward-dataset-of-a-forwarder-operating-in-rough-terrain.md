---
layout: default
title: FORWARD: Dataset of a forwarder operating in rough terrain
---

# FORWARD: Dataset of a forwarder operating in rough terrain

**arXiv**: [2511.17318v1](https://arxiv.org/abs/2511.17318) | [PDF](https://arxiv.org/pdf/2511.17318.pdf)

**作者**: Mikael Lundbäck, Erik Wallin, Carola Häggström, Mattias Nyström, Andreas Grönlund, Mats Richardson, Petrus Jönsson, William Arnvik, Lucas Hedström, Arvid Fälldin, Martin Servin

---

## 💡 一句话要点

**提出FORWARD数据集以支持森林机械在崎岖地形中的可通行性、感知和自主控制研究**

**关键词**: `多模态数据集` `森林机械` `可通行性研究` `自主控制` `传感器融合` `地形感知`

## 📋 核心要点

1. 核心问题：森林机械在崎岖地形中作业时，如何提升可通行性、感知和自主控制能力。
2. 方法要点：提供高分辨率多模态数据，包括传感器记录、视频和地形数据，覆盖18小时作业。
3. 实验或效果：数据集用于开发AI模型和算法，支持模拟器校准和自动化场景测试。

## 📄 摘要（原文）

> We present FORWARD, a high-resolution multimodal dataset of a cut-to-length forwarder operating in rough terrain on two harvest sites in the middle part of Sweden. The forwarder is a large Komatsu model equipped with a variety of sensors, including RTK-GNSS, 360-camera, operator vibration sensors, internal CAN-bus signal recording, and multiple IMUs. The data includes event time logs recorded in 5 Hz with e.g., driving speed, fuel consumption, vehicle position with centimeter accuracy, and crane use while the vehicle operates in forest areas laser-scanned with very high-resolution, $\sim$1500 points per square meter. Production log files (StanForD standard) with time-stamped machine events, extensive video material, and terrain data in various formats are included as well. About 18 hours of regular wood extraction work during three days is annotated from 360-video material into individual work elements and included in the dataset. We also include scenario specifications of conducted experiments on forest roads and in terrain. Scenarios include repeatedly driving the same routes with and without steel tracks, different load weight, and different target driving speeds. The dataset is intended for developing models and algorithms for trafficability, perception, and autonomous control of forest machines using artificial intelligence, simulation, and experiments on physical testbeds. In part, we focus on forwarders traversing terrain, avoiding obstacles, and loading or unloading logs, with consideration for efficiency, fuel consumption, safety, and environmental impact. Other benefits of the open dataset include the ability to explore auto-generation and calibration of forestry machine simulators and automation scenario descriptions using the data recorded in the field.

