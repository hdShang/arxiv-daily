---
layout: default
title: Cuffless Blood Pressure Estimation from Six Wearable Sensor Modalities in Multi-Motion-State Scenarios
---

# Cuffless Blood Pressure Estimation from Six Wearable Sensor Modalities in Multi-Motion-State Scenarios

**arXiv**: [2512.01653v1](https://arxiv.org/abs/2512.01653) | [PDF](https://arxiv.org/pdf/2512.01653.pdf)

**作者**: Yiqiao Chen, Fazheng Xu, Zijian Huang, Juchi He, Zhenghui Feng

---

## 💡 一句话要点

**提出六模态无袖带血压估计框架，以解决多运动状态下血压监测的鲁棒性问题。**

**关键词**: `无袖带血压估计` `多模态传感器` `多运动状态` `对比学习` `混合专家模型` `可穿戴设备`

## 📋 核心要点

1. 核心问题：现有方法依赖PPG和ECG信号，在多运动状态下准确性下降。
2. 方法要点：结合六种传感器模态，使用分支编码器、对比学习和MoE回归头进行自适应估计。
3. 实验或效果：在公开数据集上，SBP和DBP的MAE分别为3.60和3.01 mmHg，达到临床标准。

## 📄 摘要（原文）

> Cardiovascular disease (CVD) is a leading cause of morbidity and mortality worldwide, and sustained hypertension is an often silent risk factor, making cuffless continuous blood pressure (BP) monitoring with wearable devices important for early screening and long-term management. Most existing cuffless BP estimation methods use only photoplethysmography (PPG) and electrocardiography (ECG) signals, alone or in combination. These models are typically developed under resting or quasi-static conditions and struggle to maintain robust accuracy in multi-motion-state scenarios. In this study, we propose a six-modal BP estimation framework that jointly leverages ECG, multi-channel PPG, attachment pressure, sensor temperature, and triaxial acceleration and angular velocity. Each modality is processed by a lightweight branch encoder, contrastive learning enforces cross-modal semantic alignment, and a mixture-of-experts (MoE) regression head adaptively maps the fused features to BP across motion states. Comprehensive experiments on the public Pulse Transit Time PPG Dataset, which includes running, walking, and sitting data from 22 subjects, show that the proposed method achieves mean absolute errors (MAE) of 3.60 mmHg for systolic BP (SBP) and 3.01 mmHg for diastolic BP (DBP). From a clinical perspective, it attains Grade A for SBP, DBP, and mean arterial pressure (MAP) according to the British Hypertension Society (BHS) protocol and meets the numerical criteria of the Association for the Advancement of Medical Instrumentation (AAMI) standard for mean error (ME) and standard deviation of error (SDE).

