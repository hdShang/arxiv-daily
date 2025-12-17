---
layout: default
title: Coverage-Recon: Coordinated Multi-Drone Image Sampling with Online Map Feedback
---

# Coverage-Recon: Coordinated Multi-Drone Image Sampling with Online Map Feedback

**arXiv**: [2510.18347v1](https://arxiv.org/abs/2510.18347) | [PDF](https://arxiv.org/pdf/2510.18347.pdf)

**作者**: Muhammad Hanif, Reiji Terunuma, Takumi Sumino, Kelvin Cheng, Takeshi Hatanaka

---

## 💡 一句话要点

**提出Coverage-Recon算法，集成在线地图反馈以提升多无人机协同3D重建质量**

**关键词**: `多无人机协同` `3D地图重建` `覆盖控制` `实时反馈` `NeuralRecon算法` `安全约束`

## 📋 核心要点

1. 核心问题：多无人机协同3D重建需从多视角捕获关键点图像，以提升重建质量
2. 方法要点：使用QP角度感知覆盖控制器协调无人机运动，结合NeuralRecon实时生成3D网格并反馈不确定性
3. 实验或效果：仿真与实验验证，在线地图反馈比传统方法重建更完整准确

## 📄 摘要（原文）

> This article addresses collaborative 3D map reconstruction using multiple
> drones. Achieving high-quality reconstruction requires capturing images of
> keypoints within the target scene from diverse viewing angles, and coverage
> control offers an effective framework to meet this requirement. Meanwhile,
> recent advances in real-time 3D reconstruction algorithms make it possible to
> render an evolving map during flight, enabling immediate feedback to guide
> drone motion. Building on this, we present Coverage-Recon, a novel coordinated
> image sampling algorithm that integrates online map feedback to improve
> reconstruction quality on-the-fly. In Coverage-Recon, the coordinated motion of
> drones is governed by a Quadratic Programming (QP)-based angle-aware coverage
> controller, which ensures multi-viewpoint image capture while enforcing safety
> constraints. The captured images are processed in real time by the NeuralRecon
> algorithm to generate an evolving 3D mesh. Mesh changes across the scene are
> interpreted as indicators of reconstruction uncertainty and serve as feedback
> to update the importance index of the coverage control as the map evolves. The
> effectiveness of Coverage-Recon is validated through simulation and
> experiments, demonstrating both qualitatively and quantitatively that
> incorporating online map feedback yields more complete and accurate 3D
> reconstructions than conventional methods. Project page:
> https://htnk-lab.github.io/coverage-recon/

