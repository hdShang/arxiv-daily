---
layout: default
title: CLUE: Controllable Latent space of Unprompted Embeddings for Diversity Management in Text-to-Image Synthesis
---

# CLUE: Controllable Latent space of Unprompted Embeddings for Diversity Management in Text-to-Image Synthesis

**arXiv**: [2511.10993v1](https://arxiv.org/abs/2511.10993) | [PDF](https://arxiv.org/pdf/2511.10993.pdf)

**作者**: Keunwoo Park, Jihye Chae, Joong Ho Ahn, Jihoon Kweon

---

## 💡 一句话要点

**提出CLUE框架，通过可控潜在空间在有限数据下实现多样稳定图像生成。**

**关键词**: `文本到图像合成` `可控潜在空间` `数据增强` `医学图像生成` `Stable Diffusion` `多样性管理`

## 📋 核心要点

1. 核心问题：文本到图像合成在专业领域（如医学）数据有限时，难以平衡多样性与稳定性。
2. 方法要点：基于Stable Diffusion，引入Style Encoder和额外注意力层，独立于提示控制风格嵌入。
3. 实验或效果：在耳炎数据集上，FID降至9.30，合成数据训练F1达83.21%，优于基线。

## 📄 摘要（原文）

> Text-to-image synthesis models require the ability to generate diverse images while maintaining stability. To overcome this challenge, a number of methods have been proposed, including the collection of prompt-image datasets and the integration of additional data modalities during training. Although these methods have shown promising results in general domains, they face limitations when applied to specialized fields such as medicine, where only limited types and insufficient amounts of data are available. We present CLUE (Controllable Latent space of Unprompted Embeddings), a generative model framework that achieves diverse generation while maintaining stability through fixed-format prompts without requiring any additional data. Based on the Stable Diffusion architecture, CLUE employs a Style Encoder that processes images and prompts to generate style embeddings, which are subsequently fed into a new second attention layer of the U-Net architecture. Through Kullback-Leibler divergence, the latent space achieves continuous representation of image features within Gaussian regions, independent of prompts. Performance was assessed on otitis media dataset. CLUE reduced FID to 9.30 (vs. 46.81) and improved recall to 70.29% (vs. 49.60%). A classifier trained on synthetic-only data at 1000% scale achieved an F1 score of 83.21% (vs. 73.83%). Combining synthetic data with equal amounts of real data achieved an F1 score of 94.76%, higher than when using only real data. On an external dataset, synthetic-only training achieved an F1 score of 76.77% (vs. 60.61%) at 1000% scale. The combined approach achieved an F1 score of 85.78%, higher than when using only the internal dataset. These results demonstrate that CLUE enables diverse yet stable image generation from limited datasets and serves as an effective data augmentation method for domain-specific applications.

