---
layout: default
title: Nested AutoRegressive Models
---

# Nested AutoRegressive Models

**arXiv**: [2510.23028v1](https://arxiv.org/abs/2510.23028) | [PDF](https://arxiv.org/pdf/2510.23028.pdf)

**作者**: Hongyu Wu, Xuhui Fan, Zhangkai Wu, Longbing Cao

---

## 💡 一句话要点

**提出嵌套自回归模型以降低图像生成计算成本并提升多样性**

**关键词**: `图像生成` `自回归模型` `多尺度架构` `计算效率` `样本多样性`

## 📋 核心要点

1. 自回归模型图像生成计算密集且样本多样性受限
2. 采用多尺度模块嵌套自回归架构，复杂度降至O(log n)
3. 结合流匹配损失，实现高效且多样化的图像生成

## 📄 摘要（原文）

> AutoRegressive (AR) models have demonstrated competitive performance in image
> generation, achieving results comparable to those of diffusion models. However,
> their token-by-token image generation mechanism remains computationally
> intensive and existing solutions such as VAR often lead to limited sample
> diversity. In this work, we propose a Nested AutoRegressive~(NestAR) model,
> which proposes nested AutoRegressive architectures in generating images. NestAR
> designs multi-scale modules in a hierarchical order. These different scaled
> modules are constructed in an AR architecture, where one larger-scale module is
> conditioned on outputs from its previous smaller-scale module. Within each
> module, NestAR uses another AR structure to generate ``patches'' of tokens. The
> proposed nested AR architecture reduces the overall complexity from
> $\mathcal{O}(n)$ to $\mathcal{O}(\log n)$ in generating $n$ image tokens, as
> well as increases image diversities. NestAR further incorporates flow matching
> loss to use continuous tokens, and develops objectives to coordinate these
> multi-scale modules in model training. NestAR achieves competitive image
> generation performance while significantly lowering computational cost.

