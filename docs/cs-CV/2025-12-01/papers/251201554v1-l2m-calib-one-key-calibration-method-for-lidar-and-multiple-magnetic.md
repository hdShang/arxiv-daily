---
layout: default
title: L2M-Calib: One-key Calibration Method for LiDAR and Multiple Magnetic Sensors
---

# L2M-Calib: One-key Calibration Method for LiDAR and Multiple Magnetic Sensors

**arXiv**: [2512.01554v1](https://arxiv.org/abs/2512.01554) | [PDF](https://arxiv.org/pdf/2512.01554.pdf)

**作者**: Qiyang Lyu, Wei Wang, Zhenyu Wu, Hongming Shen, Huiqin Zhou, Danwei Wang

---

## 💡 一句话要点

**提出L2M-Calib单键校准方法，用于激光雷达与多磁传感器融合系统的外参和内参联合估计。**

**关键词**: `传感器融合` `外参校准` `磁传感器` `激光雷达` `多模态感知` `鲁棒优化`

## 📋 核心要点

1. 核心问题：磁传感器与激光雷达融合缺乏有效校准技术，影响多模态感知的准确性。
2. 方法要点：采用迭代高斯-牛顿法优化外参，结合加权岭正则化总体最小二乘法校准内参，增强鲁棒性。
3. 实验或效果：在模拟和真实AGV场景中验证，方法在各种环境条件下实现高精度和鲁棒校准。

## 📄 摘要（原文）

> Multimodal sensor fusion enables robust environmental perception by leveraging complementary information from heterogeneous sensing modalities. However, accurate calibration is a critical prerequisite for effective fusion. This paper proposes a novel one-key calibration framework named L2M-Calib for a fused magnetic-LiDAR system, jointly estimating the extrinsic transformation between the two kinds of sensors and the intrinsic distortion parameters of the magnetic sensors. Magnetic sensors capture ambient magnetic field (AMF) patterns, which are invariant to geometry, texture, illumination, and weather, making them suitable for challenging environments. Nonetheless, the integration of magnetic sensing into multimodal systems remains underexplored due to the absence of effective calibration techniques. To address this, we optimize extrinsic parameters using an iterative Gauss-Newton scheme, coupled with the intrinsic calibration as a weighted ridge-regularized total least squares (w-RRTLS) problem, ensuring robustness against measurement noise and ill-conditioned data. Extensive evaluations on both simulated datasets and real-world experiments, including AGV-mounted sensor configurations, demonstrate that our method achieves high calibration accuracy and robustness under various environmental and operational conditions.

