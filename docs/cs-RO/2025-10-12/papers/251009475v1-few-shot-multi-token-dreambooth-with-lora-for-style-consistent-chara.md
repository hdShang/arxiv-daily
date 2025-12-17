---
layout: default
title: Few-shot multi-token DreamBooth with LoRa for style-consistent character generation
---

# Few-shot multi-token DreamBooth with LoRa for style-consistent character generation

**arXiv**: [2510.09475v1](https://arxiv.org/abs/2510.09475) | [PDF](https://arxiv.org/pdf/2510.09475.pdf)

**作者**: Ruben Pascual, Mikel Sesma-Sara, Aranzazu Jurio, Daniel Paternain, Mikel Galar

---

## 💡 一句话要点

**提出多令牌DreamBooth与LoRA方法，解决少样本风格一致角色生成问题**

**关键词**: `少样本学习` `角色生成` `风格一致性` `DreamBooth` `LoRA微调` `多令牌策略`

## 📋 核心要点

1. 核心问题：从少量参考角色生成无限新角色，需保持艺术风格和共享视觉特征。
2. 方法要点：结合多令牌策略和LoRA微调，提升细节捕捉和参数效率。
3. 实验效果：在五个数据集上评估，人类研究证实方法有效且生成高质量角色。

## 📄 摘要（原文）

> The audiovisual industry is undergoing a profound transformation as it is
> integrating AI developments not only to automate routine tasks but also to
> inspire new forms of art. This paper addresses the problem of producing a
> virtually unlimited number of novel characters that preserve the artistic style
> and shared visual traits of a small set of human-designed reference characters,
> thus broadening creative possibilities in animation, gaming, and related
> domains. Our solution builds upon DreamBooth, a well-established fine-tuning
> technique for text-to-image diffusion models, and adapts it to tackle two core
> challenges: capturing intricate character details beyond textual prompts and
> the few-shot nature of the training data. To achieve this, we propose a
> multi-token strategy, using clustering to assign separate tokens to individual
> characters and their collective style, combined with LoRA-based
> parameter-efficient fine-tuning. By removing the class-specific regularization
> set and introducing random tokens and embeddings during generation, our
> approach allows for unlimited character creation while preserving the learned
> style. We evaluate our method on five small specialized datasets, comparing it
> to relevant baselines using both quantitative metrics and a human evaluation
> study. Our results demonstrate that our approach produces high-quality, diverse
> characters while preserving the distinctive aesthetic features of the reference
> characters, with human evaluation further reinforcing its effectiveness and
> highlighting the potential of our method.

