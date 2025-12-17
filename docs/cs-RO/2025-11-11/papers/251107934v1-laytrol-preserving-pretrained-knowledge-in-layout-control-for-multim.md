---
layout: default
title: Laytrol: Preserving Pretrained Knowledge in Layout Control for Multimodal Diffusion Transformers
---

# Laytrol: Preserving Pretrained Knowledge in Layout Control for Multimodal Diffusion Transformers

**arXiv**: [2511.07934v1](https://arxiv.org/abs/2511.07934) | [PDF](https://arxiv.org/pdf/2511.07934.pdf)

**作者**: Sida Huang, Siqi Huang, Ping Luo, Hongyuan Zhang

---

## 💡 一句话要点

**提出Laytrol网络以解决布局控制中预训练知识丢失问题**

**关键词**: `布局到图像生成` `扩散模型` `预训练知识保留` `布局控制网络` `数据集构建` `位置嵌入`

## 📋 核心要点

1. 核心问题：现有布局到图像方法导致生成图像质量低且风格不一致，丢失预训练知识。
2. 方法要点：构建LaySyn数据集并使用Laytrol网络继承MM-DiT参数，初始化布局编码器为文本编码器。
3. 实验或效果：定性和定量实验验证方法有效性，提升图像质量和风格一致性。

## 📄 摘要（原文）

> With the development of diffusion models, enhancing spatial controllability in text-to-image generation has become a vital challenge. As a representative task for addressing this challenge, layout-to-image generation aims to generate images that are spatially consistent with the given layout condition. Existing layout-to-image methods typically introduce the layout condition by integrating adapter modules into the base generative model. However, the generated images often exhibit low visual quality and stylistic inconsistency with the base model, indicating a loss of pretrained knowledge. To alleviate this issue, we construct the Layout Synthesis (LaySyn) dataset, which leverages images synthesized by the base model itself to mitigate the distribution shift from the pretraining data. Moreover, we propose the Layout Control (Laytrol) Network, in which parameters are inherited from MM-DiT to preserve the pretrained knowledge of the base model. To effectively activate the copied parameters and avoid disturbance from unstable control conditions, we adopt a dedicated initialization scheme for Laytrol. In this scheme, the layout encoder is initialized as a pure text encoder to ensure that its output tokens remain within the data domain of MM-DiT. Meanwhile, the outputs of the layout control network are initialized to zero. In addition, we apply Object-level Rotary Position Embedding to the layout tokens to provide coarse positional information. Qualitative and quantitative experiments demonstrate the effectiveness of our method.

