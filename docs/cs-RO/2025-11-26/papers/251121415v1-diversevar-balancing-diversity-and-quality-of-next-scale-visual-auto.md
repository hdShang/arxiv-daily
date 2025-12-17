---
layout: default
title: DiverseVAR: Balancing Diversity and Quality of Next-Scale Visual Autoregressive Models
---

# DiverseVAR: Balancing Diversity and Quality of Next-Scale Visual Autoregressive Models

**arXiv**: [2511.21415v1](https://arxiv.org/abs/2511.21415) | [PDF](https://arxiv.org/pdf/2511.21415.pdf)

**作者**: Mingue Park, Prin Phunyaphibarn, Phillip Y. Lee, Minhyuk Sung

---

## 💡 一句话要点

**提出DiverseVAR框架以解决视觉自回归模型在测试时多样性不足的问题**

**关键词**: `视觉自回归模型` `多样性增强` `文本嵌入噪声` `尺度旅行精炼` `图像生成` `多尺度自编码器`

## 📋 核心要点

1. 核心问题：VAR模型在图像生成中多样性低，常对简单提示生成相似图像
2. 方法要点：结合文本嵌入噪声注入和尺度旅行潜在精炼，平衡多样性与质量
3. 实验或效果：显著提升多样性，最小化质量损失，实现多样性-质量帕累托前沿

## 📄 摘要（原文）

> We introduce DiverseVAR, a framework that enhances the diversity of text-conditioned visual autoregressive models (VAR) at test time without requiring retraining, fine-tuning, or substantial computational overhead. While VAR models have recently emerged as strong competitors to diffusion and flow models for image generation, they suffer from a critical limitation in diversity, often producing nearly identical images even for simple prompts. This issue has largely gone unnoticed amid the predominant focus on image quality. We address this limitation at test time in two stages. First, inspired by diversity enhancement techniques in diffusion models, we propose injecting noise into the text embedding. This introduces a trade-off between diversity and image quality: as diversity increases, the image quality sharply declines. To preserve quality, we propose scale-travel: a novel latent refinement technique inspired by time-travel strategies in diffusion models. Specifically, we use a multi-scale autoencoder to extract coarse-scale tokens that enable us to resume generation at intermediate stages. Extensive experiments show that combining text-embedding noise injection with our scale-travel refinement significantly enhances diversity while minimizing image-quality degradation, achieving a new Pareto frontier in the diversity-quality trade-off.

