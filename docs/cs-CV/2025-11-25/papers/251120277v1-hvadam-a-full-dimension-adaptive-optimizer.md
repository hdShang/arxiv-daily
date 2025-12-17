---
layout: default
title: HVAdam: A Full-Dimension Adaptive Optimizer
---

# HVAdam: A Full-Dimension Adaptive Optimizer

**arXiv**: [2511.20277v1](https://arxiv.org/abs/2511.20277) | [PDF](https://arxiv.org/pdf/2511.20277.pdf)

**作者**: Yiheng Zhang, Shaowu Wu, Yuanzhuo Xu, Jiajun Wu, Shang Xu, Steve Drew, Xiaoguang Niu

---

## 💡 一句话要点

**提出Anon优化器，通过可调自适应解决Adam泛化差问题**

**关键词**: `自适应优化器` `深度学习优化` `收敛保证` `图像分类` `语言建模` `扩散模型`

## 📋 核心要点

1. 核心问题：Adam等自适应优化器在CNN等架构上泛化能力不如SGD
2. 方法要点：引入可调自适应机制和增量延迟更新，确保收敛
3. 实验或效果：在图像分类、扩散和语言建模任务中优于现有优化器

## 📄 摘要（原文）

> Adaptive optimizers such as Adam have achieved great success in training large-scale models like large language models and diffusion models. However, they often generalize worse than non-adaptive methods, such as SGD on classical architectures like CNNs. We identify a key cause of this performance gap: adaptivity in pre-conditioners, which limits the optimizer's ability to adapt to diverse optimization landscapes. To address this, we propose Anon (Adaptivity Non-restricted Optimizer with Novel convergence technique), a novel optimizer with continuously tunable adaptivity
>   , allowing it to interpolate between SGD-like and Adam-like behaviors and even extrapolate beyond both. To ensure convergence across the entire adaptivity spectrum, we introduce incremental delay update (IDU), a novel mechanism that is more flexible than AMSGrad's hard max-tracking strategy and enhances robustness to gradient noise. We theoretically establish convergence guarantees under both convex and non-convex settings. Empirically, Anon consistently outperforms state-of-the-art optimizers on representative image classification, diffusion, and language modeling tasks. These results demonstrate that adaptivity can serve as a valuable tunable design principle, and Anon provides the first unified and reliable framework capable of bridging the gap between classical and modern optimizers and surpassing their advantageous properties.

