---
layout: default
title: FGM-HD: Boosting Generation Diversity of Fractal Generative Models through Hausdorff Dimension Induction
---

# FGM-HD: Boosting Generation Diversity of Fractal Generative Models through Hausdorff Dimension Induction

**arXiv**: [2511.08945v1](https://arxiv.org/abs/2511.08945) | [PDF](https://arxiv.org/pdf/2511.08945.pdf)

**作者**: Haowei Zhang, Yuanpei Zhao, Jizhe Zhou, Mao Li

---

## 💡 一句话要点

**提出基于Hausdorff维度的FGM-HD方法以增强分形生成模型的输出多样性**

**关键词**: `分形生成模型` `Hausdorff维度` `生成多样性` `图像生成` `拒绝采样` `损失调度`

## 📋 核心要点

1. 核心问题：分形生成模型因自相似性导致生成图像多样性不足
2. 方法要点：引入可学习Hausdorff维度估计与动量调度损失，结合拒绝采样
3. 实验或效果：在ImageNet上多样性提升39%，图像质量保持相当

## 📄 摘要（原文）

> Improving the diversity of generated results while maintaining high visual quality remains a significant challenge in image generation tasks. Fractal Generative Models (FGMs) are efficient in generating high-quality images, but their inherent self-similarity limits the diversity of output images. To address this issue, we propose a novel approach based on the Hausdorff Dimension (HD), a widely recognized concept in fractal geometry used to quantify structural complexity, which aids in enhancing the diversity of generated outputs. To incorporate HD into FGM, we propose a learnable HD estimation method that predicts HD directly from image embeddings, addressing computational cost concerns. However, simply introducing HD into a hybrid loss is insufficient to enhance diversity in FGMs due to: 1) degradation of image quality, and 2) limited improvement in generation diversity. To this end, during training, we adopt an HD-based loss with a monotonic momentum-driven scheduling strategy to progressively optimize the hyperparameters, obtaining optimal diversity without sacrificing visual quality. Moreover, during inference, we employ HD-guided rejection sampling to select geometrically richer outputs. Extensive experiments on the ImageNet dataset demonstrate that our FGM-HD framework yields a 39\% improvement in output diversity compared to vanilla FGMs, while preserving comparable image quality. To our knowledge, this is the very first work introducing HD into FGM. Our method effectively enhances the diversity of generated outputs while offering a principled theoretical contribution to FGM development.

