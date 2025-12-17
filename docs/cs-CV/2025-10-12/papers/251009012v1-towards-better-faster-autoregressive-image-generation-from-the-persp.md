---
layout: default
title: Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy
---

# Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy

**arXiv**: [2510.09012v1](https://arxiv.org/abs/2510.09012) | [PDF](https://arxiv.org/pdf/2510.09012.pdf)

**作者**: Xiaoxiao Ma, Feng Zhao, Pengyang Ling, Haibo Qiu, Zhixiang Wei, Hu Yu, Jie Huang, Zhixiong Zeng, Lin Ma

---

## 💡 一句话要点

**提出熵引导解码策略以提升自回归图像生成的质量与速度**

**关键词**: `自回归图像生成` `熵引导解码` `动态温度控制` `推测解码` `图像令牌分布` `生成加速`

## 📋 核心要点

1. 核心问题：图像令牌信息密度低且空间分布不均，影响自回归生成质量与速度
2. 方法要点：动态温度控制与熵感知接受规则，平衡多样性、准确性和结构连贯性
3. 实验或效果：在多个基准测试中，质量提升且推理成本降至约85%，通用性强

## 📄 摘要（原文）

> In this work, we first revisit the sampling issues in current autoregressive
> (AR) image generation models and identify that image tokens, unlike text
> tokens, exhibit lower information density and non-uniform spatial distribution.
> Accordingly, we present an entropy-informed decoding strategy that facilitates
> higher autoregressive generation quality with faster synthesis speed.
> Specifically, the proposed method introduces two main innovations: 1) dynamic
> temperature control guided by spatial entropy of token distributions, enhancing
> the balance between content diversity, alignment accuracy, and structural
> coherence in both mask-based and scale-wise models, without extra computational
> overhead, and 2) entropy-aware acceptance rules in speculative decoding,
> achieving near-lossless generation at about 85\% of the inference cost of
> conventional acceleration methods. Extensive experiments across multiple
> benchmarks using diverse AR image generation models demonstrate the
> effectiveness and generalizability of our approach in enhancing both generation
> quality and sampling speed.

