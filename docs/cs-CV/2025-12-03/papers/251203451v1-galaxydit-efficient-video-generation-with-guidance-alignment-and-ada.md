---
layout: default
title: GalaxyDiT: Efficient Video Generation with Guidance Alignment and Adaptive Proxy in Diffusion Transformers
---

# GalaxyDiT: Efficient Video Generation with Guidance Alignment and Adaptive Proxy in Diffusion Transformers

**arXiv**: [2512.03451v1](https://arxiv.org/abs/2512.03451) | [PDF](https://arxiv.org/pdf/2512.03451.pdf)

**作者**: Zhiye Song, Steve Dai, Ben Keller, Brucek Khailany

---

## 💡 一句话要点

**提出GalaxyDiT方法，通过指导对齐和自适应代理加速扩散Transformer视频生成**

**关键词**: `视频生成` `扩散模型` `Transformer架构` `计算加速` `指导对齐` `代理选择`

## 📋 核心要点

1. 核心问题：扩散模型视频生成计算密集，迭代步骤多且分类器自由指导加倍计算需求，阻碍下游应用。
2. 方法要点：基于秩相关分析，训练免费地选择最优代理以实现计算重用，确保跨模型和参数规模的高效性。
3. 实验或效果：在Wan2.1-1.3B和Wan2.1-14B上实现1.87倍和2.37倍加速，VBench-2.0基准性能下降小于1%，高加速率下保真度优于先前方法。

## 📄 摘要（原文）

> Diffusion models have revolutionized video generation, becoming essential tools in creative content generation and physical simulation. Transformer-based architectures (DiTs) and classifier-free guidance (CFG) are two cornerstones of this success, enabling strong prompt adherence and realistic video quality. Despite their versatility and superior performance, these models require intensive computation. Each video generation requires dozens of iterative steps, and CFG doubles the required compute. This inefficiency hinders broader adoption in downstream applications.
>   We introduce GalaxyDiT, a training-free method to accelerate video generation with guidance alignment and systematic proxy selection for reuse metrics. Through rank-order correlation analysis, our technique identifies the optimal proxy for each video model, across model families and parameter scales, thereby ensuring optimal computational reuse. We achieve $1.87\times$ and $2.37\times$ speedup on Wan2.1-1.3B and Wan2.1-14B with only 0.97% and 0.72% drops on the VBench-2.0 benchmark. At high speedup rates, our approach maintains superior fidelity to the base model, exceeding prior state-of-the-art approaches by 5 to 10 dB in peak signal-to-noise ratio (PSNR).

