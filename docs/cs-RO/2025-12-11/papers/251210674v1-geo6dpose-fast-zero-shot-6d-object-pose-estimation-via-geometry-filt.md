---
layout: default
title: Geo6DPose: Fast Zero-Shot 6D Object Pose Estimation via Geometry-Filtered Feature Matching
---

# Geo6DPose: Fast Zero-Shot 6D Object Pose Estimation via Geometry-Filtered Feature Matching

**arXiv**: [2512.10674v1](https://arxiv.org/abs/2512.10674) | [PDF](https://arxiv.org/pdf/2512.10674.pdf)

**作者**: Javier Villena Toro, Mehdi Tarkian

---

## 💡 一句话要点

**提出Geo6DPose，通过几何过滤特征匹配实现快速零样本6D物体姿态估计，适用于机器人部署。**

**关键词**: `零样本学习` `6D姿态估计` `几何过滤` `特征匹配` `机器人视觉` `本地推理`

## 📋 核心要点

1. 核心问题：现有零样本6D姿态估计方法依赖大规模模型和云端推理，导致高延迟、高能耗和部署风险，不适用于计算受限的机器人场景。
2. 方法要点：结合基础模型视觉特征与几何过滤策略，通过模板与场景特征匹配、3D投影和RANSAC恢复姿态，无需训练或网络访问。
3. 实验或效果：在单GPU上实现亚秒级推理，平均召回率与更大基线相当（53.7 AR，1.08 FPS），提升对噪声、杂乱和部分遮挡的鲁棒性。

## 📄 摘要（原文）

> Recent progress in zero-shot 6D object pose estimation has been driven largely by large-scale models and cloud-based inference. However, these approaches often introduce high latency, elevated energy consumption, and deployment risks related to connectivity, cost, and data governance; factors that conflict with the practical constraints of real-world robotics, where compute is limited and on-device inference is frequently required. We introduce Geo6DPose, a lightweight, fully local, and training-free pipeline for zero-shot 6D pose estimation that trades model scale for geometric reliability. Our method combines foundation model visual features with a geometric filtering strategy: Similarity maps are computed between onboarded template DINO descriptors and scene patches, and mutual correspondences are established by projecting scene patch centers to 3D and template descriptors to the object model coordinate system. Final poses are recovered via correspondence-driven RANSAC and ranked using a weighted geometric alignment metric that jointly accounts for reprojection consistency and spatial support, improving robustness to noise, clutter, and partial visibility. Geo6DPose achieves sub-second inference on a single commodity GPU while matching the average recall of significantly larger zero-shot baselines (53.7 AR, 1.08 FPS). It requires no training, fine-tuning, or network access, and remains compatible with evolving foundation backbones, advancing practical, fully local 6D perception for robotic deployment.

