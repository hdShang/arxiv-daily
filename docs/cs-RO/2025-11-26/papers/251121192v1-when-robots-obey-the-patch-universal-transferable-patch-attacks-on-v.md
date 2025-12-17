---
layout: default
title: When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models
---

# When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models

**arXiv**: [2511.21192v1](https://arxiv.org/abs/2511.21192) | [PDF](https://arxiv.org/pdf/2511.21192.pdf)

**作者**: Hui Lu, Yi Yu, Yiming Yang, Chenyu Yi, Qixin Zhang, Bingquan Shen, Alex C. Kot, Xudong Jiang

---

## 💡 一句话要点

**提出UPA-RFAS框架以构建通用可迁移对抗补丁攻击视觉-语言-动作模型**

**关键词**: `对抗补丁攻击` `视觉-语言-动作模型` `通用可迁移性` `鲁棒性优化` `特征空间学习`

## 📋 核心要点

1. 核心问题：VLA模型易受攻击，但现有补丁攻击在未知模型和黑盒设置下难以迁移。
2. 方法要点：结合特征空间目标、鲁棒性优化和VLA特定损失，学习共享特征空间中的通用补丁。
3. 实验效果：在多种VLA模型和物理执行中，攻击可跨模型、任务和视角迁移。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

