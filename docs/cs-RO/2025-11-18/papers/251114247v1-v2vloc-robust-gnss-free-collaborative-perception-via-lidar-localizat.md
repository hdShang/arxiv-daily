---
layout: default
title: V2VLoc: Robust GNSS-Free Collaborative Perception via LiDAR Localization
---

# V2VLoc: Robust GNSS-Free Collaborative Perception via LiDAR Localization

**arXiv**: [2511.14247v1](https://arxiv.org/abs/2511.14247) | [PDF](https://arxiv.org/pdf/2511.14247.pdf)

**作者**: Wenkai Lin, Qiming Xia, Wen Li, Xun Huang, Chenglu Wen

---

## 💡 一句话要点

**提出基于LiDAR定位的GNSS-free协作感知框架以解决GNSS缺失环境下的姿态对齐问题**

**关键词**: `协作感知` `LiDAR定位` `姿态估计` `时空对齐` `GNSS缺失环境` `多智能体系统`

## 📋 核心要点

1. 核心问题：GNSS缺失环境中多智能体姿态不准确，导致协作感知特征对齐困难
2. 方法要点：设计轻量PGC估计姿态与置信度，并开发PASTAT进行置信感知时空对齐
3. 实验或效果：在V2VLoc数据集上实现SOTA性能，并在真实数据集验证泛化性

## 📄 摘要（原文）

> Multi-agents rely on accurate poses to share and align observations, enabling a collaborative perception of the environment. However, traditional GNSS-based localization often fails in GNSS-denied environments, making consistent feature alignment difficult in collaboration. To tackle this challenge, we propose a robust GNSS-free collaborative perception framework based on LiDAR localization. Specifically, we propose a lightweight Pose Generator with Confidence (PGC) to estimate compact pose and confidence representations. To alleviate the effects of localization errors, we further develop the Pose-Aware Spatio-Temporal Alignment Transformer (PASTAT), which performs confidence-aware spatial alignment while capturing essential temporal context. Additionally, we present a new simulation dataset, V2VLoc, which can be adapted for both LiDAR localization and collaborative detection tasks. V2VLoc comprises three subsets: Town1Loc, Town4Loc, and V2VDet. Town1Loc and Town4Loc offer multi-traversal sequences for training in localization tasks, whereas V2VDet is specifically intended for the collaborative detection task. Extensive experiments conducted on the V2VLoc dataset demonstrate that our approach achieves state-of-the-art performance under GNSS-denied conditions. We further conduct extended experiments on the real-world V2V4Real dataset to validate the effectiveness and generalizability of PASTAT.

