---
layout: default
title: Improving Deepfake Detection with Reinforcement Learning-Based Adaptive Data Augmentation
---

# Improving Deepfake Detection with Reinforcement Learning-Based Adaptive Data Augmentation

**arXiv**: [2511.07051v1](https://arxiv.org/abs/2511.07051) | [PDF](https://arxiv.org/pdf/2511.07051.pdf)

**作者**: Yuxuan Zhou, Tao Yu, Wen Huang, Yuheng Zhang, Tao Dai, Shu-Tao Xia

---

## 💡 一句话要点

**提出基于强化学习的自适应数据增强方法以提升深度伪造检测的泛化能力**

**关键词**: `深度伪造检测` `强化学习` `数据增强` `因果推理` `泛化能力` `对抗样本`

## 📋 核心要点

1. 核心问题：固定数据增强策略难以模拟真实伪造特征的多样性，导致检测器泛化能力不足。
2. 方法要点：结合强化学习和因果推理，动态生成对抗样本，从简单到复杂学习多域伪造特征。
3. 实验或效果：在多个跨域数据集上显著优于现有方法，提升检测器泛化性能。

## 📄 摘要（原文）

> The generalization capability of deepfake detectors is critical for
> real-world use. Data augmentation via synthetic fake face generation
> effectively enhances generalization, yet current SoTA methods rely on fixed
> strategies-raising a key question: Is a single static augmentation sufficient,
> or does the diversity of forgery features demand dynamic approaches? We argue
> existing methods overlook the evolving complexity of real-world forgeries
> (e.g., facial warping, expression manipulation), which fixed policies cannot
> fully simulate. To address this, we propose CRDA (Curriculum
> Reinforcement-Learning Data Augmentation), a novel framework guiding detectors
> to progressively master multi-domain forgery features from simple to complex.
> CRDA synthesizes augmented samples via a configurable pool of forgery
> operations and dynamically generates adversarial samples tailored to the
> detector's current learning state. Central to our approach is integrating
> reinforcement learning (RL) and causal inference. An RL agent dynamically
> selects augmentation actions based on detector performance to efficiently
> explore the vast augmentation space, adapting to increasingly challenging
> forgeries. Simultaneously, the agent introduces action space variations to
> generate heterogeneous forgery patterns, guided by causal inference to mitigate
> spurious correlations-suppressing task-irrelevant biases and focusing on
> causally invariant features. This integration ensures robust generalization by
> decoupling synthetic augmentation patterns from the model's learned
> representations. Extensive experiments show our method significantly improves
> detector generalizability, outperforming SOTA methods across multiple
> cross-domain datasets.

