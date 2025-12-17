---
layout: default
title: RoboLoc: A Benchmark Dataset for Point Place Recognition and Localization in Indoor-Outdoor Integrated Environments
---

# RoboLoc: A Benchmark Dataset for Point Place Recognition and Localization in Indoor-Outdoor Integrated Environments

**arXiv**: [2512.01194v1](https://arxiv.org/abs/2512.01194) | [PDF](https://arxiv.org/pdf/2512.01194.pdf)

**作者**: Jaejin Jeon, Seonghoon Ryoo, Sang-Duck Lee, Soomok Lee, Seungwoo Jeong

---

## 💡 一句话要点

**提出RoboLoc基准数据集以解决室内外集成环境中无GPS地点识别与定位问题**

**关键词**: `地点识别` `室内外定位` `LiDAR数据集` `域转移` `机器人导航` `基准测试`

## 📋 核心要点

1. 核心问题：现有LiDAR数据集多关注室外场景，缺乏室内外无缝域转移，影响机器人定位鲁棒性。
2. 方法要点：RoboLoc包含真实机器人轨迹、多样高程剖面和结构化室内与非结构化室外域间过渡。
3. 实验或效果：基准测试多种先进模型，包括点基、体素基和BEV架构，评估其跨域泛化能力。

## 📄 摘要（原文）

> Robust place recognition is essential for reliable localization in robotics, particularly in complex environments with fre- quent indoor-outdoor transitions. However, existing LiDAR-based datasets often focus on outdoor scenarios and lack seamless domain shifts. In this paper, we propose RoboLoc, a benchmark dataset designed for GPS-free place recognition in indoor-outdoor environments with floor transitions. RoboLoc features real-world robot trajectories, diverse elevation profiles, and transitions between structured indoor and unstructured outdoor domains. We benchmark a variety of state-of-the-art models, point-based, voxel-based, and BEV-based architectures, highlighting their generalizability domain shifts. RoboLoc provides a realistic testbed for developing multi-domain localization systems in robotics and autonomous navigation

