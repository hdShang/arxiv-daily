---
layout: default
title: Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3D Constrained Terrains
---

# Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3D Constrained Terrains

**arXiv**: [2511.14625v1](https://arxiv.org/abs/2511.14625) | [PDF](https://arxiv.org/pdf/2511.14625.pdf)

**作者**: Qingwei Ben, Botian Xu, Kailin Li, Feiyu Jia, Wentao Zhang, Jingping Wang, Jingbo Wang, Dahua Lin, Jiangmiao Pang

---

## 💡 一句话要点

**提出基于体素网格的人形机器人运动框架，用于3D受限地形导航**

**关键词**: `人形机器人运动` `体素网格感知` `端到端优化` `LiDAR仿真` `3D地形导航`

## 📋 核心要点

1. 现有感知方法仅提供局部平坦视图，无法捕捉完整3D结构
2. 使用体素化LiDAR数据和z分组2D CNN实现端到端优化控制策略
3. 实验在楼梯攀爬等场景中实现近100%成功率，超越地面障碍限制

## 📄 摘要（原文）

> Robust humanoid locomotion requires accurate and globally consistent perception of the surrounding 3D environment. However, existing perception modules, mainly based on depth images or elevation maps, offer only partial and locally flattened views of the environment, failing to capture the full 3D structure. This paper presents Gallant, a voxel-grid-based framework for humanoid locomotion and local navigation in 3D constrained terrains. It leverages voxelized LiDAR data as a lightweight and structured perceptual representation, and employs a z-grouped 2D CNN to map this representation to the control policy, enabling fully end-to-end optimization. A high-fidelity LiDAR simulation that dynamically generates realistic observations is developed to support scalable, LiDAR-based training and ensure sim-to-real consistency. Experimental results show that Gallant's broader perceptual coverage facilitates the use of a single policy that goes beyond the limitations of previous methods confined to ground-level obstacles, extending to lateral clutter, overhead constraints, multi-level structures, and narrow passages. Gallant also firstly achieves near 100% success rates in challenging scenarios such as stair climbing and stepping onto elevated platforms through improved end-to-end optimization.

