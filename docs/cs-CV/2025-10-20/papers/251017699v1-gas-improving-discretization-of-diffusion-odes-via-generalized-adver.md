---
layout: default
title: GAS: Improving Discretization of Diffusion ODEs via Generalized Adversarial Solver
---

# GAS: Improving Discretization of Diffusion ODEs via Generalized Adversarial Solver

**arXiv**: [2510.17699v1](https://arxiv.org/abs/2510.17699) | [PDF](https://arxiv.org/pdf/2510.17699.pdf)

**作者**: Aleksandr Oganov, Ilya Bykov, Eva Neudachina, Mishan Aliev, Alexander Tolmachev, Alexander Sidorov, Aleksandr Zuev, Andrey Okhotin, Denis Rakitin, Aibek Alanov

---

## 💡 一句话要点

**提出广义对抗求解器以改进扩散ODE离散化，提升生成质量与效率**

**关键词**: `扩散模型` `ODE求解器` `对抗训练` `模型蒸馏` `采样效率`

## 📋 核心要点

1. 扩散模型采样计算成本高，现有蒸馏方法依赖复杂训练且细节保留不足
2. 引入广义求解器参数化，无需额外训练技巧，结合对抗训练减少伪影
3. 在相似资源约束下，性能优于现有求解器训练方法，代码已开源

## 📄 摘要（原文）

> While diffusion models achieve state-of-the-art generation quality, they
> still suffer from computationally expensive sampling. Recent works address this
> issue with gradient-based optimization methods that distill a few-step ODE
> diffusion solver from the full sampling process, reducing the number of
> function evaluations from dozens to just a few. However, these approaches often
> rely on intricate training techniques and do not explicitly focus on preserving
> fine-grained details. In this paper, we introduce the Generalized Solver: a
> simple parameterization of the ODE sampler that does not require additional
> training tricks and improves quality over existing approaches. We further
> combine the original distillation loss with adversarial training, which
> mitigates artifacts and enhances detail fidelity. We call the resulting method
> the Generalized Adversarial Solver and demonstrate its superior performance
> compared to existing solver training methods under similar resource
> constraints. Code is available at https://github.com/3145tttt/GAS.

