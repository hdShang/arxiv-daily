---
layout: default
title: Fine-Tuning Open Video Generators for Cinematic Scene Synthesis: A Small-Data Pipeline with LoRA and Wan2.1 I2V
---

# Fine-Tuning Open Video Generators for Cinematic Scene Synthesis: A Small-Data Pipeline with LoRA and Wan2.1 I2V

**arXiv**: [2510.27364v1](https://arxiv.org/abs/2510.27364) | [PDF](https://arxiv.org/pdf/2510.27364.pdf)

**作者**: Meftun Akarsu, Kerem Catay, Sedat Bin Vedat, Enes Kutay Yarkan, Ilke Senturk, Arda Sar, Dafne Eksioglu

---

## 💡 一句话要点

**提出基于LoRA和Wan2.1 I2V的小数据管道，用于微调视频生成器以合成影视场景。**

**关键词**: `视频生成微调` `低秩适应` `影视场景合成` `小数据集训练` `扩散变换器`

## 📋 核心要点

1. 核心问题：如何从小数据集高效微调开源视频扩散模型，生成影视级场景。
2. 方法要点：两阶段流程，先使用LoRA学习视觉风格，再扩展为连贯视频序列。
3. 实验或效果：评估显示在电影保真度和时间稳定性上优于基础模型。

## 📄 摘要（原文）

> We present a practical pipeline for fine-tuning open-source video diffusion
> transformers to synthesize cinematic scenes for television and film production
> from small datasets. The proposed two-stage process decouples visual style
> learning from motion generation. In the first stage, Low-Rank Adaptation (LoRA)
> modules are integrated into the cross-attention layers of the Wan2.1 I2V-14B
> model to adapt its visual representations using a compact dataset of short
> clips from Ay Yapim's historical television film El Turco. This enables
> efficient domain transfer within hours on a single GPU. In the second stage,
> the fine-tuned model produces stylistically consistent keyframes that preserve
> costume, lighting, and color grading, which are then temporally expanded into
> coherent 720p sequences through the model's video decoder. We further apply
> lightweight parallelization and sequence partitioning strategies to accelerate
> inference without quality degradation. Quantitative and qualitative evaluations
> using FVD, CLIP-SIM, and LPIPS metrics, supported by a small expert user study,
> demonstrate measurable improvements in cinematic fidelity and temporal
> stability over the base model. The complete training and inference pipeline is
> released to support reproducibility and adaptation across cinematic domains.

