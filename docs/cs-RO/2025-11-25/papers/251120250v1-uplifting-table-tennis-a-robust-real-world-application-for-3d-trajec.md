---
layout: default
title: Uplifting Table Tennis: A Robust, Real-World Application for 3D Trajectory and Spin Estimation
---

# Uplifting Table Tennis: A Robust, Real-World Application for 3D Trajectory and Spin Estimation

**arXiv**: [2511.20250v1](https://arxiv.org/abs/2511.20250) | [PDF](https://arxiv.org/pdf/2511.20250.pdf)

**作者**: Daniel Kienzle, Katja Ludwig, Julian Lorenz, Shin'ichi Satoh, Rainer Lienhart

---

## 💡 一句话要点

**提出两阶段管道以解决真实世界乒乓球3D轨迹和旋转估计问题**

**关键词**: `3D轨迹估计` `乒乓球分析` `单目视频处理` `合成数据训练` `鲁棒性增强` `端到端系统`

## 📋 核心要点

1. 核心问题：单目视频中乒乓球3D运动估计因缺乏真实3D标注而难以泛化到噪声环境
2. 方法要点：前端感知使用2D监督，后端提升网络基于物理合成数据训练，增强鲁棒性
3. 实验或效果：集成检测器实现端到端应用，提升轨迹和旋转分析的实用性和性能

## 📄 摘要（原文）

> Obtaining the precise 3D motion of a table tennis ball from standard monocular videos is a challenging problem, as existing methods trained on synthetic data struggle to generalize to the noisy, imperfect ball and table detections of the real world. This is primarily due to the inherent lack of 3D ground truth trajectories and spin annotations for real-world video. To overcome this, we propose a novel two-stage pipeline that divides the problem into a front-end perception task and a back-end 2D-to-3D uplifting task. This separation allows us to train the front-end components with abundant 2D supervision from our newly created TTHQ dataset, while the back-end uplifting network is trained exclusively on physically-correct synthetic data. We specifically re-engineer the uplifting model to be robust to common real-world artifacts, such as missing detections and varying frame rates. By integrating a ball detector and a table keypoint detector, our approach transforms a proof-of-concept uplifting method into a practical, robust, and high-performing end-to-end application for 3D table tennis trajectory and spin analysis.

