---
layout: default
title: What's on Your Plate? Inferring Chinese Cuisine Intake from Wearable IMUs
---

# What's on Your Plate? Inferring Chinese Cuisine Intake from Wearable IMUs

**arXiv**: [2511.05292v1](https://arxiv.org/abs/2511.05292) | [PDF](https://arxiv.org/pdf/2511.05292.pdf)

**作者**: Jiaxi Yin, Pengcheng Wang, Han Ding, Fei Wang

---

## 💡 一句话要点

**提出CuisineSense系统，通过可穿戴IMU推断中餐摄入以解决传统方法偏差与隐私问题。**

**关键词**: `可穿戴传感器` `饮食监测` `中餐分类` `IMU数据分析` `两阶段检测`

## 📋 核心要点

1. 核心问题：传统饮食监测方法存在回忆偏差和隐私担忧，且现有可穿戴方法难以覆盖多样中餐。
2. 方法要点：集成智能手表手部动作与智能眼镜头部动态，采用两阶段检测管道过滤非进食行为。
3. 实验或效果：在11类食物数据集上验证，系统在进食状态检测和食物分类中达到高准确率。

## 📄 摘要（原文）

> Accurate food intake detection is vital for dietary monitoring and chronic
> disease prevention. Traditional self-report methods are prone to recall bias,
> while camera-based approaches raise concerns about privacy. Furthermore,
> existing wearable-based methods primarily focus on a limited number of food
> types, such as hamburgers and pizza, failing to address the vast diversity of
> Chinese cuisine. To bridge this gap, we propose CuisineSense, a system that
> classifies Chinese food types by integrating hand motion cues from a smartwatch
> with head dynamics from smart glasses. To filter out irrelevant daily
> activities, we design a two-stage detection pipeline. The first stage
> identifies eating states by distinguishing characteristic temporal patterns
> from non-eating behaviors. The second stage then conducts fine-grained food
> type recognition based on the motions captured during food intake. To evaluate
> CuisineSense, we construct a dataset comprising 27.5 hours of IMU recordings
> across 11 food categories and 10 participants. Experiments demonstrate that
> CuisineSense achieves high accuracy in both eating state detection and food
> classification, offering a practical solution for unobtrusive, wearable-based
> dietary monitoring.The system code is publicly available at
> https://github.com/joeeeeyin/CuisineSense.git.

