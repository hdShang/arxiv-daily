---
layout: default
title: Semantic-Guided Two-Stage GAN for Face Inpainting with Hybrid Perceptual Encoding
---

# Semantic-Guided Two-Stage GAN for Face Inpainting with Hybrid Perceptual Encoding

**arXiv**: [2512.05039v1](https://arxiv.org/abs/2512.05039) | [PDF](https://arxiv.org/pdf/2512.05039.pdf)

**作者**: Abhigyan Bhattacharya, Hiranmoy Roy

---

## 💡 一句话要点

**提出语义引导两阶段GAN，通过混合感知编码解决人脸修复中的语义不一致和纹理模糊问题。**

**关键词**: `人脸修复` `生成对抗网络` `语义引导` `混合感知编码` `两阶段合成` `动态注意力`

## 📋 核心要点

1. 核心问题：现有方法在大面积不规则掩码下易产生模糊纹理、语义不一致或结构失真。
2. 方法要点：采用语义引导分层合成，第一阶段结合CNN和Vision Transformer生成清晰语义布局，第二阶段多模态纹理生成器细化纹理。
3. 实验或效果：在CelebA-HQ和FFHQ数据集上优于现有方法，提升LPIPS、PSNR和SSIM指标，视觉结果更优。

## 📄 摘要（原文）

> Facial Image inpainting aim is to restore the missing or corrupted regions in face images while preserving identity, structural consistency and photorealistic image quality, a task specifically created for photo restoration. Though there are recent lot of advances in deep generative models, existing methods face problems with large irregular masks, often producing blurry textures on the edges of the masked region, semantic inconsistencies, or unconvincing facial structures due to direct pixel level synthesis approach and limited exploitation of facial priors. In this paper we propose a novel architecture, which address these above challenges through semantic-guided hierarchical synthesis. Our approach starts with a method that organizes and synthesizes information based on meaning, followed by refining the texture. This process gives clear insights into the facial structure before we move on to creating detailed images. In the first stage, we blend two techniques: one that focuses on local features with CNNs and global features with Vision Transformers. This helped us create clear and detailed semantic layouts. In the second stage, we use a Multi-Modal Texture Generator to refine these layouts by pulling in information from different scales, ensuring everything looks cohesive and consistent. The architecture naturally handles arbitrary mask configurations through dynamic attention without maskspecific training. Experiment on two datasets CelebA-HQ and FFHQ shows that our model outperforms other state-of-the-art methods, showing improvements in metrics like LPIPS, PSNR, and SSIM. It produces visually striking results with better semantic preservation, in challenging large-area inpainting situations.

