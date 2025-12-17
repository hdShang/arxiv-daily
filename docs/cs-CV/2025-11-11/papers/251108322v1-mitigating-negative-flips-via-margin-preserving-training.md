---
layout: default
title: Mitigating Negative Flips via Margin Preserving Training
---

# Mitigating Negative Flips via Margin Preserving Training

**arXiv**: [2511.08322v1](https://arxiv.org/abs/2511.08322) | [PDF](https://arxiv.org/pdf/2511.08322.pdf)

**作者**: Simone Ricci, Niccolò Biondi, Federico Pernici, Alberto Del Bimbo

---

## 💡 一句话要点

**提出边界保持训练方法以减少图像分类中的负翻转**

**关键词**: `图像分类` `负翻转` `边界保持` `蒸馏训练` `模型更新`

## 📋 核心要点

1. 核心问题：模型更新时负翻转增加，新类引入降低原类边界，导致性能下降
2. 方法要点：结合边界校准项和双源焦点蒸馏损失，平衡新旧类学习
3. 实验或效果：在图像分类基准上，显著降低负翻转率并保持高准确率

## 📄 摘要（原文）

> Minimizing inconsistencies across successive versions of an AI system is as crucial as reducing the overall error. In image classification, such inconsistencies manifest as negative flips, where an updated model misclassifies test samples that were previously classified correctly. This issue becomes increasingly pronounced as the number of training classes grows over time, since adding new categories reduces the margin of each class and may introduce conflicting patterns that undermine their learning process, thereby degrading performance on the original subset. To mitigate negative flips, we propose a novel approach that preserves the margins of the original model while learning an improved one. Our method encourages a larger relative margin between the previously learned and newly introduced classes by introducing an explicit margin-calibration term on the logits. However, overly constraining the logit margin for the new classes can significantly degrade their accuracy compared to a new independently trained model. To address this, we integrate a double-source focal distillation loss with the previous model and a new independently trained model, learning an appropriate decision margin from both old and new data, even under a logit margin calibration. Extensive experiments on image classification benchmarks demonstrate that our approach consistently reduces the negative flip rate with high overall accuracy.

