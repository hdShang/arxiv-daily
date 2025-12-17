---
layout: default
title: Scalable Policy Evaluation with Video World Models
---

# Scalable Policy Evaluation with Video World Models

**arXiv**: [2511.11520v1](https://arxiv.org/abs/2511.11520) | [PDF](https://arxiv.org/pdf/2511.11520.pdf)

**作者**: Wei-Cheng Tseng, Jinwei Gu, Qinsheng Zhang, Hanzi Mao, Ming-Yu Liu, Florian Shkurti, Lin Yen-Chen

---

## 💡 一句话要点

**提出基于动作条件视频生成模型的可扩展策略评估方法，以解决机器人策略真实测试成本高的问题。**

**关键词**: `策略评估` `视频生成模型` `动作条件建模` `机器人操作` `模拟到现实差距` `可扩展学习`

## 📋 核心要点

1. 核心问题：机器人策略真实评估成本高、风险大，仿真环境构建困难且存在模拟到现实的差距。
2. 方法要点：将动作条件融入预训练视频生成模型，利用互联网视频数据减少配对数据需求。
3. 实验或效果：在策略排序和预测值与实际值相关性等指标上，模型显示出无需真实交互的评估潜力。

## 📄 摘要（原文）

> Training generalist policies for robotic manipulation has shown great promise, as they enable language-conditioned, multi-task behaviors across diverse scenarios. However, evaluating these policies remains difficult because real-world testing is expensive, time-consuming, and labor-intensive. It also requires frequent environment resets and carries safety risks when deploying unproven policies on physical robots. Manually creating and populating simulation environments with assets for robotic manipulation has not addressed these issues, primarily due to the significant engineering effort required and the often substantial sim-to-real gap, both in terms of physics and rendering. In this paper, we explore the use of action-conditional video generation models as a scalable way to learn world models for policy evaluation. We demonstrate how to incorporate action conditioning into existing pre-trained video generation models. This allows leveraging internet-scale in-the-wild online videos during the pre-training stage, and alleviates the need for a large dataset of paired video-action data, which is expensive to collect for robotic manipulation. Our paper examines the effect of dataset diversity, pre-trained weight and common failure cases for the proposed evaluation pipeline.Our experiments demonstrate that, across various metrics, including policy ranking and the correlation between actual policy values and predicted policy values, these models offer a promising approach for evaluating policies without requiring real-world interactions.

