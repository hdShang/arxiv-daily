---
layout: default
title: A Lightweight Transfer Learning-Based State-of-Health Monitoring with Application to Lithium-ion Batteries in Unmanned Air Vehicles
---

# A Lightweight Transfer Learning-Based State-of-Health Monitoring with Application to Lithium-ion Batteries in Unmanned Air Vehicles

**arXiv**: [2512.08512v1](https://arxiv.org/abs/2512.08512) | [PDF](https://arxiv.org/pdf/2512.08512.pdf)

**作者**: Jiang Liu, Yan Qin, Wei Dai, Chau Yuen

---

## 💡 一句话要点

**提出轻量级迁移学习方法，用于无人机锂离子电池健康状态监测。**

**关键词**: `锂离子电池` `健康状态监测` `迁移学习` `轻量级模型` `无人机应用`

## 📋 核心要点

1. 核心问题：传统迁移学习在便携设备中计算资源消耗大，影响续航。
2. 方法要点：采用半监督迁移学习，通过构造性增量迁移学习迭代增加网络节点。
3. 实验或效果：在真实无人机电池数据集上验证，性能优于多种基线方法。

## 📄 摘要（原文）

> Accurate and rapid state-of-health (SOH) monitoring plays an important role in indicating energy information for lithium-ion battery-powered portable mobile devices. To confront their variable working conditions, transfer learning (TL) emerges as a promising technique for leveraging knowledge from data-rich source working conditions, significantly reducing the training data required for SOH monitoring from target working conditions. However, traditional TL-based SOH monitoring is infeasible when applied in portable mobile devices since substantial computational resources are consumed during the TL stage and unexpectedly reduce the working endurance. To address these challenges, this paper proposes a lightweight TL-based SOH monitoring approach with constructive incremental transfer learning (CITL). First, taking advantage of the unlabeled data in the target domain, a semi-supervised TL mechanism is proposed to minimize the monitoring residual in a constructive way, through iteratively adding network nodes in the CITL. Second, the cross-domain learning ability of node parameters for CITL is comprehensively guaranteed through structural risk minimization, transfer mismatching minimization, and manifold consistency maximization. Moreover, the convergence analysis of the CITL is given, theoretically guaranteeing the efficacy of TL performance and network compactness. Finally, the proposed approach is verified through extensive experiments with a realistic unmanned air vehicles (UAV) battery dataset collected from dozens of flight missions. Specifically, the CITL outperforms SS-TCA, MMD-LSTM-DA, DDAN, BO-CNN-TL, and AS$^3$LSTM, in SOH estimation by 83.73%, 61.15%, 28.24%, 87.70%, and 57.34%, respectively, as evaluated using the index root mean square error.

