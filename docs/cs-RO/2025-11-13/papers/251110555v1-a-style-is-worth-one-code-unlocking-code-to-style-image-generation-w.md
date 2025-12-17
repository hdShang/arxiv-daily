---
layout: default
title: A Style is Worth One Code: Unlocking Code-to-Style Image Generation with Discrete Style Space
---

# A Style is Worth One Code: Unlocking Code-to-Style Image Generation with Discrete Style Space

**arXiv**: [2511.10555v1](https://arxiv.org/abs/2511.10555) | [PDF](https://arxiv.org/pdf/2511.10555.pdf)

**作者**: Huijie Liu, Shuhao Cui, Haoxiang Cao, Shuai Ma, Kai Wu, Guoliang Kang

---

## 💡 一句话要点

**提出CoTyle方法，通过数值代码生成新颖一致的视觉风格图像。**

**关键词**: `代码到风格生成` `离散风格空间` `扩散模型` `风格嵌入` `自回归生成`

## 📋 核心要点

1. 现有方法依赖文本提示或参考图像，难以保证风格一致性和多样性。
2. 训练离散风格码本和自回归风格生成器，将数值代码映射为风格嵌入以引导扩散模型。
3. 实验验证CoTyle能有效将数值代码转化为风格控制器，生成多样且一致的风格图像。

## 📄 摘要（原文）

> Innovative visual stylization is a cornerstone of artistic creation, yet generating novel and consistent visual styles remains a significant challenge. Existing generative approaches typically rely on lengthy textual prompts, reference images, or parameter-efficient fine-tuning to guide style-aware image generation, but often struggle with style consistency, limited creativity, and complex style representations. In this paper, we affirm that a style is worth one numerical code by introducing the novel task, code-to-style image generation, which produces images with novel, consistent visual styles conditioned solely on a numerical style code. To date, this field has only been primarily explored by the industry (e.g., Midjourney), with no open-source research from the academic community. To fill this gap, we propose CoTyle, the first open-source method for this task. Specifically, we first train a discrete style codebook from a collection of images to extract style embeddings. These embeddings serve as conditions for a text-to-image diffusion model (T2I-DM) to generate stylistic images. Subsequently, we train an autoregressive style generator on the discrete style embeddings to model their distribution, allowing the synthesis of novel style embeddings. During inference, a numerical style code is mapped to a unique style embedding by the style generator, and this embedding guides the T2I-DM to generate images in the corresponding style. Unlike existing methods, our method offers unparalleled simplicity and diversity, unlocking a vast space of reproducible styles from minimal input. Extensive experiments validate that CoTyle effectively turns a numerical code into a style controller, demonstrating a style is worth one code.

