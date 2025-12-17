---
layout: default
title: A Survey on Cache Methods in Diffusion Models: Toward Efficient Multi-Modal Generation
---

# A Survey on Cache Methods in Diffusion Models: Toward Efficient Multi-Modal Generation

**arXiv**: [2510.19755v1](https://arxiv.org/abs/2510.19755) | [PDF](https://arxiv.org/pdf/2510.19755.pdf)

**作者**: Jiacheng Liu, Xinyu Wang, Yuqi Lin, Zhikai Wang, Peiru Wang, Peiliang Cai, Qinming Zhou, Zhengan Yan, Zexuan Yan, Zhengyi Shi, Chang Zou, Yue Ma, Linfeng Zhang

---

## 💡 一句话要点

**综述扩散缓存方法以提升多模态生成效率**

**关键词**: `扩散模型` `缓存方法` `多模态生成` `高效推理` `训练自由加速`

## 📋 核心要点

1. 扩散模型因多步迭代和复杂网络导致高计算开销和延迟
2. 扩散缓存通过特征级跨步重用和层间调度实现无训练加速
3. 分析显示缓存从静态重用演进到动态预测，增强灵活性和集成性

## 📄 摘要（原文）

> Diffusion Models have become a cornerstone of modern generative AI for their
> exceptional generation quality and controllability. However, their inherent
> \textit{multi-step iterations} and \textit{complex backbone networks} lead to
> prohibitive computational overhead and generation latency, forming a major
> bottleneck for real-time applications. Although existing acceleration
> techniques have made progress, they still face challenges such as limited
> applicability, high training costs, or quality degradation.
>   Against this backdrop, \textbf{Diffusion Caching} offers a promising
> training-free, architecture-agnostic, and efficient inference paradigm. Its
> core mechanism identifies and reuses intrinsic computational redundancies in
> the diffusion process. By enabling feature-level cross-step reuse and
> inter-layer scheduling, it reduces computation without modifying model
> parameters. This paper systematically reviews the theoretical foundations and
> evolution of Diffusion Caching and proposes a unified framework for its
> classification and analysis.
>   Through comparative analysis of representative methods, we show that
> Diffusion Caching evolves from \textit{static reuse} to \textit{dynamic
> prediction}. This trend enhances caching flexibility across diverse tasks and
> enables integration with other acceleration techniques such as sampling
> optimization and model distillation, paving the way for a unified, efficient
> inference framework for future multimodal and interactive applications. We
> argue that this paradigm will become a key enabler of real-time and efficient
> generative AI, injecting new vitality into both theory and practice of
> \textit{Efficient Generative Intelligence}.

