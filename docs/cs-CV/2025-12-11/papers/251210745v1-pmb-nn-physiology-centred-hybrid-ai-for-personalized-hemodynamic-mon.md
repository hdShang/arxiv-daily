---
layout: default
title: PMB-NN: Physiology-Centred Hybrid AI for Personalized Hemodynamic Monitoring from Photoplethysmography
---

# PMB-NN: Physiology-Centred Hybrid AI for Personalized Hemodynamic Monitoring from Photoplethysmography

**arXiv**: [2512.10745v1](https://arxiv.org/abs/2512.10745) | [PDF](https://arxiv.org/pdf/2512.10745.pdf)

**作者**: Yaowen Zhang, Libera Fresiello, Peter H. Veltink, Dirk W. Donker, Ying Wang

---

## 💡 一句话要点

**提出PMB-NN混合AI方法，结合深度学习与生理模型，用于基于光电容积描记的个性化血流动力学监测。**

**关键词**: `血流动力学监测` `光电容积描记` `混合人工智能` `生理模型约束` `血压估计` `可解释性`

## 📋 核心要点

1. 核心问题：现有基于光电容积描记的血压估计方法缺乏可解释性，难以监测血流动力学参数。
2. 方法要点：PMB-NN统一深度学习与基于外周阻力和动脉顺应性的2元素Windkessel模型，作为物理约束进行训练。
3. 实验或效果：在10名健康成人中验证，PMB-NN在血压估计准确性与生理合理性上优于基准模型，并识别出外周阻力和动脉顺应性。

## 📄 摘要（原文）

> Continuous monitoring of blood pressure (BP) and hemodynamic parameters such as peripheral resistance (R) and arterial compliance (C) are critical for early vascular dysfunction detection. While photoplethysmography (PPG) wearables has gained popularity, existing data-driven methods for BP estimation lack interpretability. We advanced our previously proposed physiology-centered hybrid AI method-Physiological Model-Based Neural Network (PMB-NN)-in blood pressure estimation, that unifies deep learning with a 2-element Windkessel based model parameterized by R and C acting as physics constraints. The PMB-NN model was trained in a subject-specific manner using PPG-derived timing features, while demographic information was used to infer an intermediate variable: cardiac output. We validated the model on 10 healthy adults performing static and cycling activities across two days for model's day-to-day robustness, benchmarked against deep learning (DL) models (FCNN, CNN-LSTM, Transformer) and standalone Windkessel based physiological model (PM). Validation was conducted on three perspectives: accuracy, interpretability and plausibility. PMB-NN achieved systolic BP accuracy (MAE: 7.2 mmHg) comparable to DL benchmarks, diastolic performance (MAE: 3.9 mmHg) lower than DL models. However, PMB-NN exhibited higher physiological plausibility than both DL baselines and PM, suggesting that the hybrid architecture unifies and enhances the respective merits of physiological principles and data-driven techniques. Beyond BP, PMB-NN identified R (ME: 0.15 mmHg$\cdot$s/ml) and C (ME: -0.35 ml/mmHg) during training with accuracy similar to PM, demonstrating that the embedded physiological constraints confer interpretability to the hybrid AI framework. These results position PMB-NN as a balanced, physiologically grounded alternative to purely data-driven approaches for daily hemodynamic monitoring.

