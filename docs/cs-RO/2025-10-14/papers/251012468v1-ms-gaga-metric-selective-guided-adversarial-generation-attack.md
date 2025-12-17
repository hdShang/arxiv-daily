---
layout: default
title: MS-GAGA: Metric-Selective Guided Adversarial Generation Attack
---

# MS-GAGA: Metric-Selective Guided Adversarial Generation Attack

**arXiv**: [2510.12468v1](https://arxiv.org/abs/2510.12468) | [PDF](https://arxiv.org/pdf/2510.12468.pdf)

**作者**: Dion J. X. Ho, Gabriel Lee Jun Rong, Niharika Shrivastava, Harshavardhan Abichandani, Pai Chet Ng, Xiaoxiao Miao

---

## 💡 一句话要点

**提出MS-GAGA框架以在黑盒设置下生成可转移且视觉不可察觉的对抗样本攻击深度伪造检测器**

**关键词**: `对抗攻击` `深度伪造检测` `黑盒设置` `可转移性` `视觉不可察觉性` `两阶段框架`

## 📋 核心要点

1. 核心问题：在黑盒设置下生成可转移且视觉不可察觉的对抗样本攻击深度伪造检测器
2. 方法要点：采用两阶段框架，第一阶段生成对抗候选，第二阶段基于指标选择优化
3. 实验或效果：在未见检测器上实现高达27%的误分类率提升

## 📄 摘要（原文）

> We present MS-GAGA (Metric-Selective Guided Adversarial Generation Attack), a
> two-stage framework for crafting transferable and visually imperceptible
> adversarial examples against deepfake detectors in black-box settings. In Stage
> 1, a dual-stream attack module generates adversarial candidates: MNTD-PGD
> applies enhanced gradient calculations optimized for small perturbation
> budgets, while SG-PGD focuses perturbations on visually salient regions. This
> complementary design expands the adversarial search space and improves
> transferability across unseen models. In Stage 2, a metric-aware selection
> module evaluates candidates based on both their success against black-box
> models and their structural similarity (SSIM) to the original image. By jointly
> optimizing transferability and imperceptibility, MS-GAGA achieves up to 27%
> higher misclassification rates on unseen detectors compared to state-of-the-art
> attacks.

