---
layout: default
title: VQRAE: Representation Quantization Autoencoders for Multimodal Understanding, Generation and Reconstruction
---

# VQRAE: Representation Quantization Autoencoders for Multimodal Understanding, Generation and Reconstruction

**arXiv**: [2511.23386v1](https://arxiv.org/abs/2511.23386) | [PDF](https://arxiv.org/pdf/2511.23386.pdf)

**作者**: Sinan Du, Jiahao Guo, Bo Li, Shuhao Cui, Zhengzhuo Xu, Yifu Luo, Yongxian Wei, Kun Gai, Xinggang Wang, Kai Wu, Chun Yuan

---

## 💡 一句话要点

**提出VQRAE以统一多模态理解、生成与重建的表示，通过向量量化自编码器实现连续语义特征与离散令牌的融合。**

**关键词**: `向量量化自编码器` `多模态统一表示` `语义VQ码本` `视觉理解与生成` `两阶段训练` `自回归扩展`

## 📋 核心要点

1. 核心问题：统一多模态理解、生成与重建的表示在单一标记器中是挑战，现有方法多采用双编码器范式。
2. 方法要点：基于预训练视觉基础模型，采用对称ViT解码器和两阶段训练策略，学习高维语义VQ码本，实现连续语义特征与离散令牌的统一。
3. 实验或效果：在视觉理解、生成和重建基准上表现竞争性，高维码本利用率达100%，在自回归范式中展现出良好的扩展性。

## 📄 摘要（原文）

> Unifying multimodal understanding, generation and reconstruction representation in a single tokenizer remains a key challenge in building unified models. Previous research predominantly attempts to address this in a dual encoder paradigm, e.g., utilizing the separate encoders for understanding and generation respectively or balancing semantic representations and low-level features with contrastive loss. In this paper, we propose VQRAE, a Vector Quantization version of Representation AutoEncoders, which pioneers the first exploration in unified representation to produce Continuous semantic features for image understanding and Discrete tokens for visual generation within a unified tokenizer. Specifically, we build upon pretrained vision foundation models with a symmetric ViT decoder and adopt a two-stage training strategy: first, it freezes the encoder and learns a high-dimensional semantic VQ codebook with pixel reconstruction objective; then jointly optimizes the encoder with self-distillation constraints. This design enables negligible semantic information for maintaining the ability of multimodal understanding, discrete tokens that are compatible for generation and fine-grained reconstruction. Besides, we identify the intriguing property in quantizing semantic encoders that rely on high-dimensional codebook in contrast to the previous common practice of low-dimensional codebook in image reconstruction. The semantic VQ codebook can achieve a 100% utilization ratio at a dimension of 1536. VQRAE presents competitive performance on several benchmarks of visual understanding, generation and reconstruction with promising scaling property in the autoregressive paradigm for its discrete merits.

