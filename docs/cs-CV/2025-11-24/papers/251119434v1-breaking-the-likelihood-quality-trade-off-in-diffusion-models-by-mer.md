---
layout: default
title: Breaking the Likelihood-Quality Trade-off in Diffusion Models by Merging Pretrained Experts
---

# Breaking the Likelihood-Quality Trade-off in Diffusion Models by Merging Pretrained Experts

**arXiv**: [2511.19434v1](https://arxiv.org/abs/2511.19434) | [PDF](https://arxiv.org/pdf/2511.19434.pdf)

**作者**: Yasin Esfandiari, Stefan Bauer, Sebastian U. Stich, Andrea Dittadi

---

## 💡 一句话要点

**提出专家切换采样方法以解决扩散模型中似然与图像质量权衡问题**

**关键词**: `扩散模型` `图像生成` `似然优化` `采样方法` `专家合并` `噪声切换`

## 📋 核心要点

1. 扩散模型存在似然与图像质量权衡：高噪声训练提升质量但损害似然，反之亦然
2. 方法结合预训练专家：高噪声用质量专家，低噪声用似然专家，无需重训练
3. 在CIFAR-10和ImageNet32上，合并模型优于单专家，改善或保持似然与质量

## 📄 摘要（原文）

> Diffusion models for image generation often exhibit a trade-off between perceptual sample quality and data likelihood: training objectives emphasizing high-noise denoising steps yield realistic images but poor likelihoods, whereas likelihood-oriented training overweights low-noise steps and harms visual fidelity. We introduce a simple plug-and-play sampling method that combines two pretrained diffusion experts by switching between them along the denoising trajectory. Specifically, we apply an image-quality expert at high noise levels to shape global structure, then switch to a likelihood expert at low noise levels to refine pixel statistics. The approach requires no retraining or fine-tuning -- only the choice of an intermediate switching step. On CIFAR-10 and ImageNet32, the merged model consistently matches or outperforms its base components, improving or preserving both likelihood and sample quality relative to each expert alone. These results demonstrate that expert switching across noise levels is an effective way to break the likelihood-quality trade-off in image diffusion models.

