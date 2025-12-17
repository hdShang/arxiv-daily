---
layout: default
title: RecTok: Reconstruction Distillation along Rectified Flow
---

# RecTok: Reconstruction Distillation along Rectified Flow

**arXiv**: [2512.13421v1](https://arxiv.org/abs/2512.13421) | [PDF](https://arxiv.org/pdf/2512.13421.pdf)

**作者**: Qingyu Shi, Size Wu, Jinbin Bai, Kaidong Yu, Yujing Wang, Yunhai Tong, Xiangtai Li, Xuelong Li

---

## 💡 一句话要点

**提出RecTok通过流语义蒸馏和重建对齐蒸馏，提升高维视觉分词器在扩散模型中的性能。**

**关键词**: `视觉分词器` `扩散模型` `流匹配` `语义蒸馏` `图像重建` `生成质量`

## 📋 核心要点

1. 核心问题：高维视觉分词器在重建保真度和语义表达间存在权衡，导致生成质量受限。
2. 方法要点：利用流匹配中的前向流作为训练空间，通过蒸馏视觉基础模型语义和掩码特征重建损失增强语义。
3. 实验或效果：在gFID-50K上达到SOTA，随维度增加性能持续提升，保持语义丰富的潜在空间结构。

## 📄 摘要（原文）

> Visual tokenizers play a crucial role in diffusion models. The dimensionality of latent space governs both reconstruction fidelity and the semantic expressiveness of the latent feature. However, a fundamental trade-off is inherent between dimensionality and generation quality, constraining existing methods to low-dimensional latent spaces. Although recent works have leveraged vision foundation models to enrich the semantics of visual tokenizers and accelerate convergence, high-dimensional tokenizers still underperform their low-dimensional counterparts. In this work, we propose RecTok, which overcomes the limitations of high-dimensional visual tokenizers through two key innovations: flow semantic distillation and reconstruction--alignment distillation. Our key insight is to make the forward flow in flow matching semantically rich, which serves as the training space of diffusion transformers, rather than focusing on the latent space as in previous works. Specifically, our method distills the semantic information in VFMs into the forward flow trajectories in flow matching. And we further enhance the semantics by introducing a masked feature reconstruction loss. Our RecTok achieves superior image reconstruction, generation quality, and discriminative performance. It achieves state-of-the-art results on the gFID-50K under both with and without classifier-free guidance settings, while maintaining a semantically rich latent space structure. Furthermore, as the latent dimensionality increases, we observe consistent improvements. Code and model are available at https://shi-qingyu.github.io/rectok.github.io.

