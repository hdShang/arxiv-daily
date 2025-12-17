---
layout: default
title: The Finer the Better: Towards Granular-aware Open-set Domain Generalization
---

# The Finer the Better: Towards Granular-aware Open-set Domain Generalization

**arXiv**: [2511.16979v1](https://arxiv.org/abs/2511.16979) | [PDF](https://arxiv.org/pdf/2511.16979.pdf)

**作者**: Yunyun Wang, Zheng Duan, Xinyue Liao, Ke-Jia Chen, Songcan Chen

---

## 💡 一句话要点

**提出SeeCLIP框架以解决开放集域泛化中细粒度未知类识别难题**

**关键词**: `开放集域泛化` `视觉语言模型` `细粒度语义` `对比学习` `伪未知生成`

## 📋 核心要点

1. 核心问题：开放集域泛化中模型易对与已知类视觉相似的硬未知类过度自信
2. 方法要点：通过语义增强提示和双工对比学习提升细粒度视觉语言对齐
3. 实验或效果：在五个基准测试中准确率提升3%，H-score提升5%

## 📄 摘要（原文）

> Open-Set Domain Generalization (OSDG) tackles the realistic scenario where deployed models encounter both domain shifts and novel object categories. Despite impressive progress with vision-language models like CLIP, existing methods still fall into the dilemma between structural risk of known-classes and open-space risk from unknown-classes, and easily suffers from over-confidence, especially when distinguishing ``hard unknowns" that share fine-grained visual similarities with known classes. To this end, we propose a Semantic-enhanced CLIP (SeeCLIP) framework that explicitly addresses this dilemma through fine-grained semantic enhancement. In SeeCLIP, we propose a semantic-aware prompt enhancement module to decompose images into discriminative semantic tokens, enabling nuanced vision-language alignment beyond coarse category labels. To position unknown prompts effectively, we introduce duplex contrastive learning with complementary objectives, that is, repulsion to maintain separability from known classes, and cohesion to preserve semantic proximity. Further, our semantic-guided diffusion module synthesizes pseudo-unknowns by perturbing extracted semantic tokens, generating challenging samples that are visually similar to known classes yet exhibit key local differences. These hard negatives force the model to learn finer decision boundaries. Extensive experiments across five benchmarks demonstrate consistent improvements of 3% accuracy and 5% H-score over state-of-the-art methods.

