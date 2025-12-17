---
layout: default
title: DeblurSDI: Blind Image Deblurring Using Self-diffusion
---

# DeblurSDI: Blind Image Deblurring Using Self-diffusion

**arXiv**: [2510.27439v1](https://arxiv.org/abs/2510.27439) | [PDF](https://arxiv.org/pdf/2510.27439.pdf)

**作者**: Yanlong Yang, Guanxiong Luo

---

## 💡 一句话要点

**提出DeblurSDI框架，通过自扩散实现零样本盲图像去模糊。**

**关键词**: `盲图像去模糊` `自扩散` `零样本学习` `自监督框架` `模糊核估计`

## 📋 核心要点

1. 盲图像去卷积是病态逆问题，需同时估计清晰图像和模糊核。
2. 方法基于自扩散，迭代优化神经网络，无需预训练，结合数据一致性和L1稀疏约束。
3. 实验显示在高度退化场景下，能稳定恢复清晰图像和准确模糊核。

## 📄 摘要（原文）

> Blind image deconvolution is a challenging ill-posed inverse problem, where
> both the latent sharp image and the blur kernel are unknown. Traditional
> methods often rely on handcrafted priors, while modern deep learning approaches
> typically require extensive pre-training on large external datasets, limiting
> their adaptability to real-world scenarios. In this work, we propose DeblurSDI,
> a zero-shot, self-supervised framework based on self-diffusion (SDI) that
> requires no prior training. DeblurSDI formulates blind deconvolution as an
> iterative reverse self-diffusion process that starts from pure noise and
> progressively refines the solution. At each step, two randomly-initialized
> neural networks are optimized continuously to refine the sharp image and the
> blur kernel. The optimization is guided by an objective function combining data
> consistency with a sparsity-promoting L1-norm for the kernel. A key innovation
> is our noise scheduling mechanism, which stabilizes the optimization and
> provides remarkable robustness to variations in blur kernel size. These allow
> DeblurSDI to dynamically learn an instance-specific prior tailored to the input
> image. Extensive experiments demonstrate that DeblurSDI consistently achieves
> superior performance, recovering sharp images and accurate kernels even in
> highly degraded scenarios.

