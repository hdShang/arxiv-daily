---
layout: default
title: Video Spatial Reasoning with Object-Centric 3D Rollout
---

# Video Spatial Reasoning with Object-Centric 3D Rollout

**arXiv**: [2511.13190v1](https://arxiv.org/abs/2511.13190) | [PDF](https://arxiv.org/pdf/2511.13190.pdf)

**作者**: Haoran Tang, Meng Cao, Ruyang Liu, Xiaoxi Liang, Linglong Li, Ge Li, Xiaodan Liang

---

## 💡 一句话要点

**提出对象中心3D展开策略以解决视频空间推理中的查询锁定问题**

**关键词**: `视频空间推理` `对象中心学习` `3D几何扰动` `多模态大语言模型` `强化学习优化`

## 📋 核心要点

1. 核心问题：现有多模态大模型在视频空间推理中易出现查询锁定，忽略上下文线索
2. 方法要点：通过结构化扰动3D几何并投影至2D，强制模型进行整体场景推理
3. 实验或效果：3B参数模型在VSI-Bench上达47.5%准确率，优于多个7B基线

## 📄 摘要（原文）

> Recent advances in Multi-modal Large Language Models (MLLMs) have showcased remarkable capabilities in vision-language understanding. However, enabling robust video spatial reasoning-the ability to comprehend object locations, orientations, and inter-object relationships in dynamic 3D scenes-remains a key unsolved challenge. Existing approaches primarily rely on spatially grounded supervised fine-tuning or reinforcement learning, yet we observe that such models often exhibit query-locked reasoning, focusing narrowly on objects explicitly mentioned in the prompt while ignoring critical contextual cues. To address this limitation, we propose Object-Centric 3D Rollout (OCR), a novel strategy that introduces structured perturbations to the 3D geometry of selected objects during training. By degrading object-specific visual cues and projecting the altered geometry into 2D space, OCR compels the model to reason holistically across the entire scene. We further design a rollout-based training pipeline that jointly leverages vanilla and region-noisy videos to optimize spatial reasoning trajectories. Experiments demonstrate state-of-the-art performance: our 3B-parameter model achieves 47.5% accuracy on VSI-Bench, outperforming several 7B baselines. Ablations confirm OCR's superiority over prior rollout strategies (e.g., T-GRPO, NoisyRollout).

