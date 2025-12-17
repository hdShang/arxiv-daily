---
layout: default
title: TinyDéjàVu: Smaller Memory Footprint & Faster Inference on Sensor Data Streams with Always-On Microcontrollers
---

# TinyDéjàVu: Smaller Memory Footprint & Faster Inference on Sensor Data Streams with Always-On Microcontrollers

**arXiv**: [2512.09786v1](https://arxiv.org/abs/2512.09786) | [PDF](https://arxiv.org/pdf/2512.09786.pdf)

**作者**: Zhaolan Huang, Emmanuel Baccelli

---

## 💡 一句话要点

**提出TinyDéjàVu框架以优化微控制器上传感器数据流推理的内存占用和计算效率**

**关键词**: `微控制器推理` `内存优化` `传感器数据流` `滑动窗口` `神经网络效率` `开源框架`

## 📋 核心要点

1. 核心问题：微控制器内存有限（如128kB RAM），需优化神经网络层间数据流以降低能耗和延长电池寿命
2. 方法要点：设计新算法减少RAM占用，通过消除重叠滑动窗口输入的冗余计算提升推理速度
3. 实验或效果：开源实现，硬件基准测试显示RAM使用减少超60%，冗余计算消除达90%

## 📄 摘要（原文）

> Always-on sensors are increasingly expected to embark a variety of tiny neural networks and to continuously perform inference on time-series of the data they sense. In order to fit lifetime and energy consumption requirements when operating on battery, such hardware uses microcontrollers (MCUs) with tiny memory budget e.g., 128kB of RAM. In this context, optimizing data flows across neural network layers becomes crucial. In this paper, we introduce TinyDéjàVu, a new framework and novel algorithms we designed to drastically reduce the RAM footprint required by inference using various tiny ML models for sensor data time-series on typical microcontroller hardware. We publish the implementation of TinyDéjàVu as open source, and we perform reproducible benchmarks on hardware. We show that TinyDéjàVu can save more than 60% of RAM usage and eliminate up to 90% of redundant compute on overlapping sliding window inputs.

