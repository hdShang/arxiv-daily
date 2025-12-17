---
layout: default
title: SensHRPS: Sensing Comfortable Human-Robot Proxemics and Personal Space With Eye-Tracking
---

# SensHRPS: Sensing Comfortable Human-Robot Proxemics and Personal Space With Eye-Tracking

**arXiv**: [2512.08518v1](https://arxiv.org/abs/2512.08518) | [PDF](https://arxiv.org/pdf/2512.08518.pdf)

**作者**: Nadezhda Kushina, Ko Watanabe, Aarthi Kannan, Ashita Ashok, Andreas Dengel, Karsten Berns

---

## 💡 一句话要点

**提出基于眼动追踪的舒适人机距离感知方法，以提升社交机器人交互体验。**

**关键词**: `人机交互` `眼动追踪` `距离感知` `机器学习` `舒适度评估` `社交机器人`

## 📋 核心要点

1. 核心问题：社交机器人需适应人类距离规范以确保用户舒适，但眼动特征在人机交互中的适用性未知。
2. 方法要点：使用移动眼动追踪和主观报告，在四个距离下评估用户舒适度，并基于注视特征训练机器学习模型。
3. 实验或效果：决策树模型表现最佳（F1分数0.73），最小瞳孔直径是关键预测因子，表明人机交互舒适阈值与人人交互不同。

## 📄 摘要（原文）

> Social robots must adjust to human proxemic norms to ensure user comfort and engagement. While prior research demonstrates that eye-tracking features reliably estimate comfort in human-human interactions, their applicability to interactions with humanoid robots remains unexplored. In this study, we investigate user comfort with the robot "Ameca" across four experimentally controlled distances (0.5 m to 2.0 m) using mobile eye-tracking and subjective reporting (N=19). We evaluate multiple machine learning and deep learning models to estimate comfort based on gaze features. Contrary to previous human-human studies where Transformer models excelled, a Decision Tree classifier achieved the highest performance (F1-score = 0.73), with minimum pupil diameter identified as the most critical predictor. These findings suggest that physiological comfort thresholds in human-robot interaction differ from human-human dynamics and can be effectively modeled using interpretable logic.

