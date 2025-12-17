---
layout: default
title: Fare: Failure Resilience in Learned Visual Navigation Control
---

# Fare: Failure Resilience in Learned Visual Navigation Control

**arXiv**: [2510.24680v1](https://arxiv.org/abs/2510.24680) | [PDF](https://arxiv.org/pdf/2510.24680.pdf)

**作者**: Zishuo Wang, Joel Loo, David Hsu

---

## 💡 一句话要点

**提出Fare框架以构建视觉导航中失败恢复的模仿学习策略**

**关键词**: `视觉导航` `模仿学习` `失败恢复` `分布外检测` `鲁棒控制`

## 📋 核心要点

1. 模仿学习策略在分布外场景中易出现不可预测失败
2. Fare嵌入分布外检测与识别，无需失败数据，并配对恢复启发式
3. 真实世界实验显示Fare实现跨架构失败恢复，提升长距离导航鲁棒性

## 📄 摘要（原文）

> While imitation learning (IL) enables effective visual navigation, IL
> policies are prone to unpredictable failures in out-of-distribution (OOD)
> scenarios. We advance the notion of failure-resilient policies, which not only
> detect failures but also recover from them automatically. Failure recognition
> that identifies the factors causing failure is key to informing recovery: e.g.
> pinpointing image regions triggering failure detections can provide cues to
> guide recovery. We present Fare, a framework to construct failure-resilient IL
> policies, embedding OOD-detection and recognition in them without using
> explicit failure data, and pairing them with recovery heuristics. Real-world
> experiments show that Fare enables failure recovery across two different policy
> architectures, enabling robust long-range navigation in complex environments.

