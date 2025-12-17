---
layout: default
title: Seeing What Matters: Visual Preference Policy Optimization for Visual Generation
---

# Seeing What Matters: Visual Preference Policy Optimization for Visual Generation

**arXiv**: [2511.18719v1](https://arxiv.org/abs/2511.18719) | [PDF](https://arxiv.org/pdf/2511.18719.pdf)

**作者**: Ziqi Ni, Yuanzhi Liang, Rui Li, Yi Zhou, Haibing Huang, Chi Zhang, Xuelong Li

---

## 💡 一句话要点

**提出ViPO方法以解决视觉生成中GRPO忽略空间结构的问题**

**关键词**: `视觉生成` `强化学习` `策略优化` `像素级优势` `感知结构模块`

## 📋 核心要点

1. 核心问题：GRPO依赖单标量奖励，忽略视觉内容的空间和时间结构
2. 方法要点：使用感知结构模块构建像素级优势图，优化重要区域
3. 实验或效果：在图像和视频基准上优于GRPO，提升对齐和泛化能力

## 📄 摘要（原文）

> Reinforcement learning (RL) has become a powerful tool for post-training visual generative models, with Group Relative Policy Optimization (GRPO) increasingly used to align generators with human preferences. However, existing GRPO pipelines rely on a single scalar reward per sample, treating each image or video as a holistic entity and ignoring the rich spatial and temporal structure of visual content. This coarse supervision hinders the correction of localized artifacts and the modeling of fine-grained perceptual cues. We introduce Visual Preference Policy Optimization (ViPO), a GRPO variant that lifts scalar feedback into structured, pixel-level advantages. ViPO employs a Perceptual Structuring Module that uses pretrained vision backbones to construct spatially and temporally aware advantage maps, redistributing optimization pressure toward perceptually important regions while preserving the stability of standard GRPO. Across both image and video benchmarks, ViPO consistently outperforms vanilla GRPO, improving in-domain alignment with human-preference rewards and enhancing generalization on out-of-domain evaluations. The method is architecture-agnostic, lightweight, and fully compatible with existing GRPO training pipelines, providing a more expressive and informative learning signal for visual generation.

