---
layout: default
title: Spotlight on Token Perception for Multimodal Reinforcement Learning
---

# Spotlight on Token Perception for Multimodal Reinforcement Learning

**arXiv**: [2510.09285v1](https://arxiv.org/abs/2510.09285) | [PDF](https://arxiv.org/pdf/2510.09285.pdf)

**作者**: Siyuan Huang, Xiaoye Qu, Yafu Li, Yun Luo, Zefeng He, Daizong Liu, Yu Cheng

---

## 💡 一句话要点

**提出视觉感知策略优化以增强多模态强化学习中的视觉推理能力**

**关键词**: `多模态强化学习` `令牌感知` `视觉依赖` `策略优化` `大型视觉语言模型` `推理基准`

## 📋 核心要点

1. 现有方法忽视视觉感知在强化学习优化中的作用，导致多模态推理能力受限
2. 引入令牌感知视角，通过重新加权轨迹优势和聚焦关键令牌优化策略
3. 在多个基准测试中显著优于现有模型，验证了方法的有效性和可扩展性

## 📄 摘要（原文）

> While Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the
> reasoning capabilities of Large Vision-Language Models (LVLMs), most existing
> methods in multimodal reasoning neglect the critical role of visual perception
> within the RLVR optimization process. In this paper, we undertake a pioneering
> exploration of multimodal RLVR through the novel perspective of token
> perception, which measures the visual dependency of each generated token. With
> a granular analysis of Chain-of-Thought (CoT) processes, we uncover two key
> insights: first, token perception in a rollout trajectory is sparsely
> distributed, where only a small fraction of tokens have high visual dependency
> for visually-grounded reasoning; second, different trajectories exhibit
> significant divergence in their overall visual dependency. Based on these
> observations, we propose Visually-Perceptive Policy Optimization (VPPO), a
> novel policy gradient algorithm that explicitly leverages token perception to
> refine the learning signal. Specifically, VPPO achieves this through a dual
> mechanism: it reweights a trajectory's advantage by its overall visual
> dependency, and focuses policy updates exclusively on perceptually pivotal
> tokens. On a comprehensive suite of eight perception and reasoning benchmarks,
> VPPO demonstrates substantial gains over leading open-source RL-tuned models,
> with its effectiveness consistently validated across 7B and 32B model scales.
> Our findings not only establish a new token-level perceptual perspective for
> analyzing multimodal RLVR but also present a novel and effective optimization
> strategy to significantly enhance the multimodal reasoning capabilities of
> LVLMs.

