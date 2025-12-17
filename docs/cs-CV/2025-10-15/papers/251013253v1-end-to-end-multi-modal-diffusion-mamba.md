---
layout: default
title: End-to-End Multi-Modal Diffusion Mamba
---

# End-to-End Multi-Modal Diffusion Mamba

**arXiv**: [2510.13253v1](https://arxiv.org/abs/2510.13253) | [PDF](https://arxiv.org/pdf/2510.13253.pdf)

**作者**: Chunhao Lu, Qiang Lu, Meichen Dong, Jake Luo

---

## 💡 一句话要点

**提出多模态扩散Mamba以统一多模态处理，提升高维数据生成性能。**

**关键词**: `多模态学习` `扩散模型` `Mamba架构` `端到端模型` `高维数据生成`

## 📋 核心要点

1. 现有端到端多模态模型编码解码分离，阻碍联合表示学习。
2. 采用Mamba多步选择扩散模型和统一变分自编码器，渐进生成精炼模态信息。
3. 在图像生成、图像描述等任务中，性能优于现有模型，与SOTA模型竞争。

## 📄 摘要（原文）

> Current end-to-end multi-modal models utilize different encoders and decoders
> to process input and output information. This separation hinders the joint
> representation learning of various modalities. To unify multi-modal processing,
> we propose a novel architecture called MDM (Multi-modal Diffusion Mamba). MDM
> utilizes a Mamba-based multi-step selection diffusion model to progressively
> generate and refine modality-specific information through a unified variational
> autoencoder for both encoding and decoding. This innovative approach allows MDM
> to achieve superior performance when processing high-dimensional data,
> particularly in generating high-resolution images and extended text sequences
> simultaneously. Our evaluations in areas such as image generation, image
> captioning, visual question answering, text comprehension, and reasoning tasks
> demonstrate that MDM significantly outperforms existing end-to-end models
> (MonoFormer, LlamaGen, and Chameleon etc.) and competes effectively with SOTA
> models like GPT-4V, Gemini Pro, and Mistral. Our results validate MDM's
> effectiveness in unifying multi-modal processes while maintaining computational
> efficiency, establishing a new direction for end-to-end multi-modal
> architectures.

