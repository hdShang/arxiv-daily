---
layout: default
title: Video-R4: Reinforcing Text-Rich Video Reasoning with Visual Rumination
---

# Video-R4: Reinforcing Text-Rich Video Reasoning with Visual Rumination

**arXiv**: [2511.17490v1](https://arxiv.org/abs/2511.17490) | [PDF](https://arxiv.org/pdf/2511.17490.pdf)

**作者**: Yolo Yunlong Tang, Daiki Shimada, Hang Hua, Chao Huang, Jing Bi, Rogerio Feris, Chenliang Xu

---

## 💡 一句话要点

**提出Video-R4模型，通过视觉反刍解决文本丰富视频中的细粒度推理问题**

**关键词**: `视频推理` `视觉反刍` `文本丰富视频` `强化学习` `多模态大模型` `细粒度证据`

## 📋 核心要点

1. 核心问题：文本丰富视频中细小、瞬态文本线索易被忽略，导致幻觉和推理失败
2. 方法要点：引入视觉反刍，迭代选择帧、放大区域、重新编码像素以更新推理状态
3. 实验或效果：在M4-ViteVQA上达到SOTA，并泛化到文档和通用视频QA任务

## 📄 摘要（原文）

> Understanding text-rich videos requires reading small, transient textual cues that often demand repeated inspection. Yet most video QA models rely on single-pass perception over fixed frames, leading to hallucinations and failures on fine-grained evidence. Inspired by how humans pause, zoom, and re-read critical regions, we introduce Video-R4 (Reinforcing Text-Rich Video Reasoning with Visual Rumination), a video reasoning LMM that performs visual rumination: iteratively selecting frames, zooming into informative regions, re-encoding retrieved pixels, and updating its reasoning state. We construct two datasets with executable rumination trajectories: Video-R4-CoT-17k for supervised practice and Video-R4-RL-30k for reinforcement learning. We propose a multi-stage rumination learning framework that progressively finetunes a 7B LMM to learn atomic and mixing visual operations via SFT and GRPO-based RL. Video-R4-7B achieves state-of-the-art results on M4-ViteVQA and further generalizes to multi-page document QA, slides QA, and generic video QA, demonstrating that iterative rumination is an effective paradigm for pixel-grounded multimodal reasoning.

