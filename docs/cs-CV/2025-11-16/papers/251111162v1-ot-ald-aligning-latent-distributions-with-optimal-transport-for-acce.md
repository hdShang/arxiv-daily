---
layout: default
title: OT-ALD: Aligning Latent Distributions with Optimal Transport for Accelerated Image-to-Image Translation
---

# OT-ALD: Aligning Latent Distributions with Optimal Transport for Accelerated Image-to-Image Translation

**arXiv**: [2511.11162v1](https://arxiv.org/abs/2511.11162) | [PDF](https://arxiv.org/pdf/2511.11162.pdf)

**作者**: Zhanpeng Wang, Shuting Cao, Yuhang Lu, Yuhan Li, Na Lei, Zhongxuan Luo

---

## 💡 一句话要点

**提出OT-ALD框架，利用最优传输对齐潜在分布以加速图像翻译**

**关键词**: `图像翻译` `最优传输` `扩散模型` `潜在分布对齐` `采样效率`

## 📋 核心要点

1. DDIB方法存在翻译效率低和潜在分布不匹配问题
2. 使用最优传输映射潜在分布，作为目标域反向扩散起点
3. 实验显示采样效率提升20.29%，FID分数平均降低2.6

## 📄 摘要（原文）

> The Dual Diffusion Implicit Bridge (DDIB) is an emerging image-to-image (I2I) translation method that preserves cycle consistency while achieving strong flexibility. It links two independently trained diffusion models (DMs) in the source and target domains by first adding noise to a source image to obtain a latent code, then denoising it in the target domain to generate the translated image. However, this method faces two key challenges: (1) low translation efficiency, and (2) translation trajectory deviations caused by mismatched latent distributions. To address these issues, we propose a novel I2I translation framework, OT-ALD, grounded in optimal transport (OT) theory, which retains the strengths of DDIB-based approach. Specifically, we compute an OT map from the latent distribution of the source domain to that of the target domain, and use the mapped distribution as the starting point for the reverse diffusion process in the target domain. Our error analysis confirms that OT-ALD eliminates latent distribution mismatches. Moreover, OT-ALD effectively balances faster image translation with improved image quality. Experiments on four translation tasks across three high-resolution datasets show that OT-ALD improves sampling efficiency by 20.29% and reduces the FID score by 2.6 on average compared to the top-performing baseline models.

