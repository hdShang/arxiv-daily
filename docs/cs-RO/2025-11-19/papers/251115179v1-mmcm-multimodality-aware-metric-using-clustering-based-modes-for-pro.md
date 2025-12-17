---
layout: default
title: MMCM: Multimodality-aware Metric using Clustering-based Modes for Probabilistic Human Motion Prediction
---

# MMCM: Multimodality-aware Metric using Clustering-based Modes for Probabilistic Human Motion Prediction

**arXiv**: [2511.15179v1](https://arxiv.org/abs/2511.15179) | [PDF](https://arxiv.org/pdf/2511.15179.pdf)

**作者**: Kyotaro Tokoro, Hiromu Taketsugu, Norimichi Ukita

---

## 💡 一句话要点

**提出MMCM度量方法以评估概率性人体运动预测的多模态分布**

**关键词**: `人体运动预测` `概率预测` `多模态度量` `聚类分析` `运动有效性`

## 📋 核心要点

1. 核心问题：现有度量无法区分多模态覆盖与运动有效性，导致评估偏差。
2. 方法要点：通过聚类定义运动模式，评估预测运动的覆盖度和基于数据集的运动有效性。
3. 实验或效果：验证聚类模式合理，MMCM能准确评分多模态预测。

## 📄 摘要（原文）

> This paper proposes a novel metric for Human Motion Prediction (HMP). Since a single past sequence can lead to multiple possible futures, a probabilistic HMP method predicts such multiple motions. While a single motion predicted by a deterministic method is evaluated only with the difference from its ground truth motion, multiple predicted motions should also be evaluated based on their distribution. For this evaluation, this paper focuses on the following two criteria. \textbf{(a) Coverage}: motions should be distributed among multiple motion modes to cover diverse possibilities. \textbf{(b) Validity}: motions should be kinematically valid as future motions observable from a given past motion. However, existing metrics simply appreciate widely distributed motions even if these motions are observed in a single mode and kinematically invalid. To resolve these disadvantages, this paper proposes a Multimodality-aware Metric using Clustering-based Modes (MMCM). For (a) coverage, MMCM divides a motion space into several clusters, each of which is regarded as a mode. These modes are used to explicitly evaluate whether predicted motions are distributed among multiple modes. For (b) validity, MMCM identifies valid modes by collecting possible future motions from a motion dataset. Our experiments validate that our clustering yields sensible mode definitions and that MMCM accurately scores multimodal predictions. Code: https://github.com/placerkyo/MMCM

