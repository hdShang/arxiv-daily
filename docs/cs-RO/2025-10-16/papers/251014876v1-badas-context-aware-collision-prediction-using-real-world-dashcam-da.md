---
layout: default
title: BADAS: Context Aware Collision Prediction Using Real-World Dashcam Data
---

# BADAS: Context Aware Collision Prediction Using Real-World Dashcam Data

**arXiv**: [2510.14876v1](https://arxiv.org/abs/2510.14876) | [PDF](https://arxiv.org/pdf/2510.14876.pdf)

**作者**: Roni Goldshmidt, Hamish Scott, Lorenzo Niccolini, Shizhan Zhu, Daniel Moura, Orly Zvitia

---

## 💡 一句话要点

**提出BADAS模型，利用真实行车记录仪数据预测自车碰撞，减少误报。**

**关键词**: `碰撞预测` `自车中心评估` `行车记录仪数据` `V-JEPA2骨干网络` `端到端训练` `时间到事故估计`

## 📋 核心要点

1. 现有碰撞预测方法难以区分自车威胁与无关事故，导致高误报率。
2. 使用V-JEPA2骨干网络端到端训练，提供公开和专有两种变体。
3. 在多个数据集上实现最优AP/AUC，并改进碰撞时间估计。

## 📄 摘要（原文）

> Existing collision prediction methods often fail to distinguish between
> ego-vehicle threats and random accidents not involving the ego vehicle, leading
> to excessive false alerts in real-world deployment. We present BADAS, a family
> of collision prediction models trained on Nexar's real-world dashcam collision
> dataset -- the first benchmark designed explicitly for ego-centric evaluation.
> We re-annotate major benchmarks to identify ego involvement, add consensus
> alert-time labels, and synthesize negatives where needed, enabling fair AP/AUC
> and temporal evaluation. BADAS uses a V-JEPA2 backbone trained end-to-end and
> comes in two variants: BADAS-Open (trained on our 1.5k public videos) and
> BADAS1.0 (trained on 40k proprietary videos). Across DAD, DADA-2000, DoTA, and
> Nexar, BADAS achieves state-of-the-art AP/AUC and outperforms a
> forward-collision ADAS baseline while producing more realistic time-to-accident
> estimates. We release our BADAS-Open model weights and code, along with
> re-annotations of all evaluation datasets to promote ego-centric collision
> prediction research.

