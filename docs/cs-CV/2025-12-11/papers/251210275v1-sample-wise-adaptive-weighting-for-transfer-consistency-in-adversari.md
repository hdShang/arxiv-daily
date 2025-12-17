---
layout: default
title: Sample-wise Adaptive Weighting for Transfer Consistency in Adversarial Distillation
---

# Sample-wise Adaptive Weighting for Transfer Consistency in Adversarial Distillation

**arXiv**: [2512.10275v1](https://arxiv.org/abs/2512.10275) | [PDF](https://arxiv.org/pdf/2512.10275.pdf)

**作者**: Hongsin Lee, Hye Won Chung

---

## 💡 一句话要点

**提出样本自适应对抗蒸馏以提升对抗鲁棒性转移效果**

**关键词**: `对抗蒸馏` `鲁棒性转移` `样本自适应` `对抗训练` `教师-学生网络`

## 📋 核心要点

1. 核心问题：强教师网络未必提升学生鲁棒性，存在鲁棒饱和现象
2. 方法要点：基于对抗可转移性，自适应重加权训练样本，无额外计算成本
3. 实验或效果：在CIFAR-10等数据集上，SAAD优于现有方法，提升AutoAttack鲁棒性

## 📄 摘要（原文）

> Adversarial distillation in the standard min-max adversarial training framework aims to transfer adversarial robustness from a large, robust teacher network to a compact student. However, existing work often neglects to incorporate state-of-the-art robust teachers. Through extensive analysis, we find that stronger teachers do not necessarily yield more robust students-a phenomenon known as robust saturation. While typically attributed to capacity gaps, we show that such explanations are incomplete. Instead, we identify adversarial transferability-the fraction of student-crafted adversarial examples that remain effective against the teacher-as a key factor in successful robustness transfer. Based on this insight, we propose Sample-wise Adaptive Adversarial Distillation (SAAD), which reweights training examples by their measured transferability without incurring additional computational cost. Experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet show that SAAD consistently improves AutoAttack robustness over prior methods. Our code is available at https://github.com/HongsinLee/saad.

