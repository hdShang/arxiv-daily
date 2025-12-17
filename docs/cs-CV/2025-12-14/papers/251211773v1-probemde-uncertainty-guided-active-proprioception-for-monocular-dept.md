---
layout: default
title: ProbeMDE: Uncertainty-Guided Active Proprioception for Monocular Depth Estimation in Surgical Robotics
---

# ProbeMDE: Uncertainty-Guided Active Proprioception for Monocular Depth Estimation in Surgical Robotics

**arXiv**: [2512.11773v1](https://arxiv.org/abs/2512.11773) | [PDF](https://arxiv.org/pdf/2512.11773.pdf)

**作者**: Britton Jordan, Jordan Thompson, Jesse F. d'Almeida, Hao Li, Nithesh Kumar, Susheela Sharma Stern, Ipek Oguz, Robert J. Webster, Daniel Brown, Alan Kuntz, James Ferguson

---

## 💡 一句话要点

**提出ProbeMDE框架，结合RGB图像与稀疏本体感知测量以提升手术机器人单目深度估计精度**

**关键词**: `单目深度估计` `手术机器人` `不确定性引导` `主动感知` `本体感知测量` `模型集成`

## 📋 核心要点

1. 核心问题：单目深度估计在手术场景中因纹理缺失、镜面反射和遮挡导致预测不确定和不准确
2. 方法要点：利用模型集成预测密集深度图，基于不确定性梯度通过SVGD选择最优本体感知测量位置
3. 实验或效果：在模拟和物理实验中验证，优于基线方法，提高精度并减少所需测量次数

## 📄 摘要（原文）

> Monocular depth estimation (MDE) provides a useful tool for robotic perception, but its predictions are often uncertain and inaccurate in challenging environments such as surgical scenes where textureless surfaces, specular reflections, and occlusions are common. To address this, we propose ProbeMDE, a cost-aware active sensing framework that combines RGB images with sparse proprioceptive measurements for MDE. Our approach utilizes an ensemble of MDE models to predict dense depth maps conditioned on both RGB images and on a sparse set of known depth measurements obtained via proprioception, where the robot has touched the environment in a known configuration. We quantify predictive uncertainty via the ensemble's variance and measure the gradient of the uncertainty with respect to candidate measurement locations. To prevent mode collapse while selecting maximally informative locations to propriocept (touch), we leverage Stein Variational Gradient Descent (SVGD) over this gradient map. We validate our method in both simulated and physical experiments on central airway obstruction surgical phantoms. Our results demonstrate that our approach outperforms baseline methods across standard depth estimation metrics, achieving higher accuracy while minimizing the number of required proprioceptive measurements.

