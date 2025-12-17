---
layout: default
title: A Sensor-Aware Phenomenological Framework for Lidar Degradation Simulation and SLAM Robustness Evaluation
---

# A Sensor-Aware Phenomenological Framework for Lidar Degradation Simulation and SLAM Robustness Evaluation

**arXiv**: [2512.08653v1](https://arxiv.org/abs/2512.08653) | [PDF](https://arxiv.org/pdf/2512.08653.pdf)

**作者**: Doumegna Mawuto Koudjo Felix, Xianjia Yu, Zhuo Zou, Tomi Westerlund

---

## 💡 一句话要点

**提出传感器感知的激光雷达退化仿真框架，用于SLAM鲁棒性评估**

**关键词**: `激光雷达退化仿真` `SLAM鲁棒性评估` `传感器感知框架` `点云处理` `ROS兼容性`

## 📋 核心要点

1. 核心问题：现有激光雷达SLAM鲁棒性评估方法缺乏物理基础或传感器特异性
2. 方法要点：直接在真实点云上模拟可解释退化，保留几何、强度和时间结构
3. 实验或效果：在三种激光雷达架构和五种SLAM系统上验证，揭示鲁棒性模式

## 📄 摘要（原文）

> Lidar-based SLAM systems are highly sensitive to adverse conditions such as occlusion, noise, and field-of-view (FoV) degradation, yet existing robustness evaluation methods either lack physical grounding or do not capture sensor-specific behavior. This paper presents a sensor-aware, phenomenological framework for simulating interpretable lidar degradations directly on real point clouds, enabling controlled and reproducible SLAM stress testing. Unlike image-derived corruption benchmarks (e.g., SemanticKITTI-C) or simulation-only approaches (e.g., lidarsim), the proposed system preserves per-point geometry, intensity, and temporal structure while applying structured dropout, FoV reduction, Gaussian noise, occlusion masking, sparsification, and motion distortion. The framework features autonomous topic and sensor detection, modular configuration with four severity tiers (light--extreme), and real-time performance (less than 20 ms per frame) compatible with ROS workflows. Experimental validation across three lidar architectures and five state-of-the-art SLAM systems reveals distinct robustness patterns shaped by sensor design and environmental context. The open-source implementation provides a practical foundation for benchmarking lidar-based SLAM under physically meaningful degradation scenarios.

