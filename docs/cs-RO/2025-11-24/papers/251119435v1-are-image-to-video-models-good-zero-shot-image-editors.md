---
layout: default
title: Are Image-to-Video Models Good Zero-Shot Image Editors?
---

# Are Image-to-Video Models Good Zero-Shot Image Editors?

**arXiv**: [2511.19435v1](https://arxiv.org/abs/2511.19435) | [PDF](https://arxiv.org/pdf/2511.19435.pdf)

**作者**: Zechuan Zhang, Zhenyuan Chen, Zongxin Yang, Yi Yang

---

## 💡 一句话要点

**提出IF-Edit框架，利用图像到视频扩散模型实现零样本图像编辑**

**关键词**: `图像编辑` `视频扩散模型` `零样本学习` `推理增强` `潜在变量压缩`

## 📋 核心要点

1. 核心问题：视频扩散模型在零样本图像编辑中存在提示错位、冗余时间潜在变量和模糊后期帧问题
2. 方法要点：包括思维链提示增强、时间潜在变量丢弃和自一致后精炼步骤
3. 实验或效果：在多个基准测试中，在推理任务上表现优异，通用编辑任务保持竞争力

## 📄 摘要（原文）

> Large-scale video diffusion models show strong world simulation and temporal reasoning abilities, but their use as zero-shot image editors remains underexplored. We introduce IF-Edit, a tuning-free framework that repurposes pretrained image-to-video diffusion models for instruction-driven image editing. IF-Edit addresses three key challenges: prompt misalignment, redundant temporal latents, and blurry late-stage frames. It includes (1) a chain-of-thought prompt enhancement module that transforms static editing instructions into temporally grounded reasoning prompts; (2) a temporal latent dropout strategy that compresses frame latents after the expert-switch point, accelerating denoising while preserving semantic and temporal coherence; and (3) a self-consistent post-refinement step that sharpens late-stage frames using a short still-video trajectory. Experiments on four public benchmarks, covering non-rigid editing, physical and temporal reasoning, and general instruction edits, show that IF-Edit performs strongly on reasoning-centric tasks while remaining competitive on general-purpose edits. Our study provides a systematic view of video diffusion models as image editors and highlights a simple recipe for unified video-image generative reasoning.

