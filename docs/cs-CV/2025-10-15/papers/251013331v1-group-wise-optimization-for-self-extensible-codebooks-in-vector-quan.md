---
layout: default
title: Group-Wise Optimization for Self-Extensible Codebooks in Vector Quantized Models
---

# Group-Wise Optimization for Self-Extensible Codebooks in Vector Quantized Models

**arXiv**: [2510.13331v1](https://arxiv.org/abs/2510.13331) | [PDF](https://arxiv.org/pdf/2510.13331.pdf)

**作者**: Hong-Kai Zheng, Piji Li

---

## 💡 一句话要点

**提出Group-VQ以解决VQ模型码本崩溃问题，提升重建质量与码本灵活性。**

**关键词**: `向量量化模型` `码本优化` `分组训练` `图像重建` `自监督学习`

## 📋 核心要点

1. 核心问题：VQ-VAEs存在码本崩溃，现有方法限制码本学习能力，降低重建质量。
2. 方法要点：采用分组优化码本，独立优化每组，组内联合优化，并引入训练后码本重采样。
3. 实验或效果：图像重建实验显示重建指标提升，码本大小可训练后灵活调整。

## 📄 摘要（原文）

> Vector Quantized Variational Autoencoders (VQ-VAEs) leverage self-supervised
> learning through reconstruction tasks to represent continuous vectors using the
> closest vectors in a codebook. However, issues such as codebook collapse
> persist in the VQ model. To address these issues, existing approaches employ
> implicit static codebooks or jointly optimize the entire codebook, but these
> methods constrain the codebook's learning capability, leading to reduced
> reconstruction quality. In this paper, we propose Group-VQ, which performs
> group-wise optimization on the codebook. Each group is optimized independently,
> with joint optimization performed within groups. This approach improves the
> trade-off between codebook utilization and reconstruction performance.
> Additionally, we introduce a training-free codebook resampling method, allowing
> post-training adjustment of the codebook size. In image reconstruction
> experiments under various settings, Group-VQ demonstrates improved performance
> on reconstruction metrics. And the post-training codebook sampling method
> achieves the desired flexibility in adjusting the codebook size.

