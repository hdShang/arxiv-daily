---
layout: default
title: StableSketcher: Enhancing Diffusion Model for Pixel-based Sketch Generation via Visual Question Answering Feedback
---

# StableSketcher: Enhancing Diffusion Model for Pixel-based Sketch Generation via Visual Question Answering Feedback

**arXiv**: [2510.20093v1](https://arxiv.org/abs/2510.20093) | [PDF](https://arxiv.org/pdf/2510.20093.pdf)

**作者**: Jiho Park, Sieun Choi, Jaeyoon Seo, Jihie Kim

---

## 💡 一句话要点

**提出StableSketcher框架，通过视觉问答反馈增强扩散模型以生成像素级手绘草图**

**关键词**: `扩散模型` `草图生成` `视觉问答` `强化学习` `变分自编码器` `数据集构建`

## 📋 核心要点

1. 扩散模型在生成像素级手绘草图时面临抽象表达挑战，导致提示保真度不足
2. 方法包括微调变分自编码器优化潜在解码，并集成基于视觉问答的强化学习奖励函数
3. 实验显示，相比基线模型，生成草图在风格保真度和提示对齐方面有显著提升

## 📄 摘要（原文）

> Although recent advancements in diffusion models have significantly enriched
> the quality of generated images, challenges remain in synthesizing pixel-based
> human-drawn sketches, a representative example of abstract expression. To
> combat these challenges, we propose StableSketcher, a novel framework that
> empowers diffusion models to generate hand-drawn sketches with high prompt
> fidelity. Within this framework, we fine-tune the variational autoencoder to
> optimize latent decoding, enabling it to better capture the characteristics of
> sketches. In parallel, we integrate a new reward function for reinforcement
> learning based on visual question answering, which improves text-image
> alignment and semantic consistency. Extensive experiments demonstrate that
> StableSketcher generates sketches with improved stylistic fidelity, achieving
> better alignment with prompts compared to the Stable Diffusion baseline.
> Additionally, we introduce SketchDUO, to the best of our knowledge, the first
> dataset comprising instance-level sketches paired with captions and
> question-answer pairs, thereby addressing the limitations of existing datasets
> that rely on image-label pairs. Our code and dataset will be made publicly
> available upon acceptance.

