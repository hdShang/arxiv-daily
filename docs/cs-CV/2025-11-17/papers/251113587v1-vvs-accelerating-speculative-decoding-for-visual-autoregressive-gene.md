---
layout: default
title: VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping
---

# VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping

**arXiv**: [2511.13587v1](https://arxiv.org/abs/2511.13587) | [PDF](https://arxiv.org/pdf/2511.13587.pdf)

**作者**: Haotian Dong, Ye Li, Rongwei Lu, Chen Tang, Shu-Tao Xia, Zhi Wang

---

## 💡 一句话要点

**提出VVS框架以加速视觉自回归生成，通过部分验证跳过减少推理延迟**

**关键词**: `视觉自回归生成` `推测解码` `推理加速` `验证跳过` `特征缓存` `令牌调度`

## 📋 核心要点

1. 视觉自回归模型推理延迟高，推测解码无法直接减少前向传递次数
2. 利用视觉令牌可互换性，设计验证跳过、特征缓存和调度模块
3. 实验显示前向传递减少2.8倍，保持生成质量，优于传统方法

## 📄 摘要（原文）

> Visual autoregressive (AR) generation models have demonstrated strong potential for image generation, yet their next-token-prediction paradigm introduces considerable inference latency. Although speculative decoding (SD) has been proven effective for accelerating visual AR models, its "draft one step, then verify one step" paradigm prevents a direct reduction of the forward passes, thus restricting acceleration potential. Motivated by the visual token interchangeability, we for the first time to explore verification skipping in the SD process of visual AR model generation to explicitly cut the number of target model forward passes, thereby reducing inference latency. Based on an analysis of the drafting stage's characteristics, we observe that verification redundancy and stale feature reusability are key factors to retain generation quality and speedup for verification-free steps. Inspired by these two observations, we propose a novel SD framework VVS to accelerate visual AR generation via partial verification skipping, which integrates three complementary modules: (1) a verification-free token selector with dynamical truncation, (2) token-level feature caching and reuse, and (3) fine-grained skipped step scheduling. Consequently, VVS reduces the number of target model forward passes by a factor of $2.8\times$ relative to vanilla AR decoding while maintaining competitive generation quality, offering a superior speed-quality trade-off over conventional SD frameworks and revealing strong potential to reshape the SD paradigm.

