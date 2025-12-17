---
layout: default
title: End-to-end Autonomous Vehicle Following System using Monocular Fisheye Camera
---

# End-to-end Autonomous Vehicle Following System using Monocular Fisheye Camera

**arXiv**: [2511.19011v1](https://arxiv.org/abs/2511.19011) | [PDF](https://arxiv.org/pdf/2511.19011.pdf)

**作者**: Jiale Zhang, Yeqiang Qian, Tong Qin, Mingyang Jiang, Siyuan Chen, Ming Yang

---

## 💡 一句话要点

**提出端到端车辆跟随框架，使用单目鱼眼相机提升通用场景性能。**

**关键词**: `车辆编队` `端到端学习` `单目鱼眼相机` `语义掩码` `动态采样` `闭环验证`

## 📋 核心要点

1. 核心问题：现有车辆编队系统依赖车道线和昂贵传感器，通用性受限。
2. 方法要点：引入语义掩码解决多帧数据因果混淆，动态采样机制精确跟踪前车轨迹。
3. 实验或效果：真实世界闭环验证显示，在多种场景下优于传统多阶段算法。

## 📄 摘要（原文）

> The increase in vehicle ownership has led to increased traffic congestion, more accidents, and higher carbon emissions. Vehicle platooning is a promising solution to address these issues by improving road capacity and reducing fuel consumption. However, existing platooning systems face challenges such as reliance on lane markings and expensive high-precision sensors, which limits their general applicability. To address these issues, we propose a vehicle following framework that expands its capability from restricted scenarios to general scenario applications using only a camera. This is achieved through our newly proposed end-to-end method, which improves overall driving performance. The method incorporates a semantic mask to address causal confusion in multi-frame data fusion. Additionally, we introduce a dynamic sampling mechanism to precisely track the trajectories of preceding vehicles. Extensive closed-loop validation in real-world vehicle experiments demonstrates the system's ability to follow vehicles in various scenarios, outperforming traditional multi-stage algorithms. This makes it a promising solution for cost-effective autonomous vehicle platooning. A complete real-world vehicle experiment is available at https://youtu.be/zL1bcVb9kqQ.

