---
layout: default
title: Informative Sample Selection Model for Skeleton-based Action Recognition with Limited Training Samples
---

# Informative Sample Selection Model for Skeleton-based Action Recognition with Limited Training Samples

**arXiv**: [2510.25345v1](https://arxiv.org/abs/2510.25345) | [PDF](https://arxiv.org/pdf/2510.25345.pdf)

**作者**: Zhigang Tu, Zhengbo Zhang, Jia Gong, Junsong Yuan, Bo Du

---

## 💡 一句话要点

**提出基于MDP的样本选择模型，以解决骨架动作识别中训练样本有限的问题**

**关键词**: `骨架动作识别` `半监督学习` `主动学习` `马尔可夫决策过程` `双曲空间` `元调优`

## 📋 核心要点

1. 核心问题：骨架动作识别中，主动学习选择样本时，代表性样本可能不具信息性，导致模型学习效率低
2. 方法要点：将半监督3D动作识别建模为MDP，在双曲空间中增强状态-动作对表示，并引入元调优策略
3. 实验或效果：在三个3D动作识别基准上验证了方法的有效性，未知具体性能指标

## 📄 摘要（原文）

> Skeleton-based human action recognition aims to classify human skeletal
> sequences, which are spatiotemporal representations of actions, into predefined
> categories. To reduce the reliance on costly annotations of skeletal sequences
> while maintaining competitive recognition accuracy, the task of 3D Action
> Recognition with Limited Training Samples, also known as semi-supervised 3D
> Action Recognition, has been proposed. In addition, active learning, which aims
> to proactively select the most informative unlabeled samples for annotation,
> has been explored in semi-supervised 3D Action Recognition for training sample
> selection. Specifically, researchers adopt an encoder-decoder framework to
> embed skeleton sequences into a latent space, where clustering information,
> combined with a margin-based selection strategy using a multi-head mechanism,
> is utilized to identify the most informative sequences in the unlabeled set for
> annotation. However, the most representative skeleton sequences may not
> necessarily be the most informative for the action recognizer, as the model may
> have already acquired similar knowledge from previously seen skeleton samples.
> To solve it, we reformulate Semi-supervised 3D action recognition via active
> learning from a novel perspective by casting it as a Markov Decision Process
> (MDP). Built upon the MDP framework and its training paradigm, we train an
> informative sample selection model to intelligently guide the selection of
> skeleton sequences for annotation. To enhance the representational capacity of
> the factors in the state-action pairs within our method, we project them from
> Euclidean space to hyperbolic space. Furthermore, we introduce a meta tuning
> strategy to accelerate the deployment of our method in real-world scenarios.
> Extensive experiments on three 3D action recognition benchmarks demonstrate the
> effectiveness of our method.

