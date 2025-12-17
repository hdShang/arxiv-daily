---
layout: default
title: OneOcc: Semantic Occupancy Prediction for Legged Robots with a Single Panoramic Camera
---

# OneOcc: Semantic Occupancy Prediction for Legged Robots with a Single Panoramic Camera

**arXiv**: [2511.03571v1](https://arxiv.org/abs/2511.03571) | [PDF](https://arxiv.org/pdf/2511.03571.pdf)

**作者**: Hao Shi, Ze Wang, Shangwei Guo, Mengfei Duan, Song Wang, Teng Chen, Kailun Yang, Lin Wang, Kaiwei Wang

---

## 💡 一句话要点

**提出OneOcc框架，用于足式机器人的全景语义占据预测，解决身体抖动和360度连续性问题。**

**关键词**: `语义占据预测` `全景相机` `足式机器人` `双投影融合` `轻量解码器` `运动补偿`

## 📋 核心要点

1. 核心问题：足式机器人因步态导致身体抖动，现有语义场景补全系统多针对轮式平台，缺乏360度连续感知。
2. 方法要点：结合双投影融合、双网格体素化和轻量解码器，实现特征级运动补偿和多尺度融合。
3. 实验或效果：在QuadOcc和H3O基准上达到新SOTA，提升mIoU指标，模块轻量可部署。

## 📄 摘要（原文）

> Robust 3D semantic occupancy is crucial for legged/humanoid robots, yet most
> semantic scene completion (SSC) systems target wheeled platforms with
> forward-facing sensors. We present OneOcc, a vision-only panoramic SSC
> framework designed for gait-introduced body jitter and 360{\deg} continuity.
> OneOcc combines: (i) Dual-Projection fusion (DP-ER) to exploit the annular
> panorama and its equirectangular unfolding, preserving 360{\deg} continuity and
> grid alignment; (ii) Bi-Grid Voxelization (BGV) to reason in Cartesian and
> cylindrical-polar spaces, reducing discretization bias and sharpening
> free/occupied boundaries; (iii) a lightweight decoder with Hierarchical AMoE-3D
> for dynamic multi-scale fusion and better long-range/occlusion reasoning; and
> (iv) plug-and-play Gait Displacement Compensation (GDC) learning feature-level
> motion correction without extra sensors. We also release two panoramic
> occupancy benchmarks: QuadOcc (real quadruped, first-person 360{\deg}) and
> Human360Occ (H3O) (CARLA human-ego 360{\deg} with RGB, Depth, semantic
> occupancy; standardized within-/cross-city splits). OneOcc sets new
> state-of-the-art (SOTA): on QuadOcc it beats strong vision baselines and
> popular LiDAR ones; on H3O it gains +3.83 mIoU (within-city) and +8.08
> (cross-city). Modules are lightweight, enabling deployable full-surround
> perception for legged/humanoid robots. Datasets and code will be publicly
> available at https://github.com/MasterHow/OneOcc.

