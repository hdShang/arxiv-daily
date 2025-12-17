---
layout: default
title: Correction of Decoupled Weight Decay
---

# Correction of Decoupled Weight Decay

**arXiv**: [2512.08217v1](https://arxiv.org/abs/2512.08217) | [PDF](https://arxiv.org/pdf/2512.08217.pdf)

**作者**: Jason Chuan-Chih Chou

---

## 💡 一句话要点

**提出基于稳态独立假设的权重衰减比例修正，以稳定训练动态并提升模型性能**

**关键词**: `权重衰减` `优化器` `训练动态` `稳态分析` `AdamW` `Scion优化器`

## 📋 核心要点

1. 核心问题：解耦权重衰减长期设为与学习率γ成正比，但近期有研究主张应设为γ²比例
2. 方法要点：基于稳态下更新与权重独立的假设，推导出解耦权重衰减∝γ²可稳定权重范数
3. 实验或效果：经验验证该比例能稳定权重和梯度范数，更好控制训练动态并改善性能

## 📄 摘要（原文）

> Decoupled weight decay, solely responsible for the performance advantage of AdamW over Adam, has long been set to proportional to learning rate $γ$ without questioning. Some researchers have recently challenged such assumption and argued that decoupled weight decay should be set $\propto γ^2$ instead based on orthogonality arguments at steady state. To the contrary, we find that eliminating the contribution of the perpendicular component of the update to the weight norm leads to little change to the training dynamics. Instead, we derive that decoupled weight decay $\propto γ^2$ results in stable weight norm based on the simple assumption that updates become independent of the weights at steady state, regardless of the nature of the optimizer. Based on the same assumption, we derive and empirically verify that the Total Update Contribution (TUC) of a minibatch under the Scion optimizer is better characterized by the momentum-dependent effective learning rate whose optimal value transfers and we show that decoupled weight decay $\propto γ^2$ leads to stable weight and gradient norms and allows us to better control the training dynamics and improve the model performance.

