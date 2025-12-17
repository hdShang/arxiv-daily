---
layout: default
title: Conformal Correction for Efficiency May be at Odds with Entropy
---

# Conformal Correction for Efficiency May be at Odds with Entropy

**arXiv**: [2512.02704v1](https://arxiv.org/abs/2512.02704) | [PDF](https://arxiv.org/pdf/2512.02704.pdf)

**作者**: Senrong Xu, Tianyu Wang, Zenan Li, Yuan Yao, Taolue Chen, Feng Xu, Xiaoxing Ma

---

## 💡 一句话要点

**提出熵约束的保形校正方法，以在保形预测效率与熵之间探索帕累托最优。**

**关键词**: `保形预测` `不确定性量化` `熵约束` `效率优化` `帕累托最优` `机器学习模型`

## 📋 核心要点

1. 保形校正提升效率时可能与预测熵存在权衡，影响模型不确定性。
2. 通过熵约束的保形校正，在效率与熵之间寻求更好的帕累托最优解。
3. 在计算机视觉和图形数据集上实验，效率提升最高达34.4%，给定熵阈值。

## 📄 摘要（原文）

> Conformal prediction (CP) provides a comprehensive framework to produce statistically rigorous uncertainty sets for black-box machine learning models. To further improve the efficiency of CP, conformal correction is proposed to fine-tune or wrap the base model with an extra module using a conformal-aware inefficiency loss. In this work, we empirically and theoretically identify a trade-off between the CP efficiency and the entropy of model prediction. We then propose an entropy-constrained conformal correction method, exploring a better Pareto optimum between efficiency and entropy. Extensive experimental results on both computer vision and graph datasets demonstrate the efficacy of the proposed method. For instance, it can significantly improve the efficiency of state-of-the-art CP methods by up to 34.4%, given an entropy threshold.

