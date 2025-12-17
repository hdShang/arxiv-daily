---
layout: default
title: University Building Recognition Dataset in Thailand for the mission-oriented IoT sensor system
---

# University Building Recognition Dataset in Thailand for the mission-oriented IoT sensor system

**arXiv**: [2512.05468v1](https://arxiv.org/abs/2512.05468) | [PDF](https://arxiv.org/pdf/2512.05468.pdf)

**作者**: Takara Taniguchi, Yudai Ueda, Atsuya Muramatsu, Kohki Hashimoto, Ryo Yagi, Hideya Ochiai, Chaodit Aswakul

---

## 💡 一句话要点

**提出泰国朱拉隆功大学建筑识别数据集，支持面向任务的无线自组织联邦学习系统。**

**关键词**: `建筑识别数据集` `无线自组织联邦学习` `视觉变换器` `物联网传感器系统` `泰国场景`

## 📋 核心要点

1. 核心问题：面向任务的物联网传感器系统需特定数据集，现有数据集如UTBR可能不适用于泰国场景。
2. 方法要点：开发CUBR数据集，专为泰国朱拉隆功大学建筑识别设计，作为WAFL-ViT的案例研究。
3. 实验或效果：在WAFL场景下训练比自训练场景获得更高准确率，数据集已公开可用。

## 📄 摘要（原文）

> Many industrial sectors have been using of machine learning at inference mode on edge devices. Future directions show that training on edge devices is promising due to improvements in semiconductor performance. Wireless Ad Hoc Federated Learning (WAFL) has been proposed as a promising approach for collaborative learning with device-to-device communication among edges. In particular, WAFL with Vision Transformer (WAFL-ViT) has been tested on image recognition tasks with the UTokyo Building Recognition Dataset (UTBR). Since WAFL-ViT is a mission-oriented sensor system, it is essential to construct specific datasets by each mission. In our work, we have developed the Chulalongkorn University Building Recognition Dataset (CUBR), which is specialized for Chulalongkorn University as a case study in Thailand. Additionally, our results also demonstrate that training on WAFL scenarios achieves better accuracy than self-training scenarios. Dataset is available in https://github.com/jo2lxq/wafl/.

