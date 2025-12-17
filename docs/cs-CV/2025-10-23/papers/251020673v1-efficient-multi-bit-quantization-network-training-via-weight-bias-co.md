---
layout: default
title: Efficient Multi-bit Quantization Network Training via Weight Bias Correction and Bit-wise Coreset Sampling
---

# Efficient Multi-bit Quantization Network Training via Weight Bias Correction and Bit-wise Coreset Sampling

**arXiv**: [2510.20673v1](https://arxiv.org/abs/2510.20673) | [PDF](https://arxiv.org/pdf/2510.20673.pdf)

**作者**: Jinhee Kim, Jae Jun An, Kang Eun Jeon, Jong Hwan Ko

---

## 💡 一句话要点

**提出权重偏置校正与位级核心集采样以降低多比特量化网络训练开销**

**关键词**: `多比特量化` `权重偏置校正` `核心集采样` `训练效率` `神经网络部署`

## 📋 核心要点

1. 多比特量化网络训练开销大，需重复全数据集更新和额外微调
2. 权重偏置校正对齐激活分布，位级核心集采样利用梯度重要性选择子集
3. 在多个数据集和架构上验证，训练时间减少达7.88倍，精度保持或提升

## 📄 摘要（原文）

> Multi-bit quantization networks enable flexible deployment of deep neural
> networks by supporting multiple precision levels within a single model.
> However, existing approaches suffer from significant training overhead as
> full-dataset updates are repeated for each supported bit-width, resulting in a
> cost that scales linearly with the number of precisions. Additionally, extra
> fine-tuning stages are often required to support additional or intermediate
> precision options, further compounding the overall training burden. To address
> this issue, we propose two techniques that greatly reduce the training overhead
> without compromising model utility: (i) Weight bias correction enables shared
> batch normalization and eliminates the need for fine-tuning by neutralizing
> quantization-induced bias across bit-widths and aligning activation
> distributions; and (ii) Bit-wise coreset sampling strategy allows each child
> model to train on a compact, informative subset selected via gradient-based
> importance scores by exploiting the implicit knowledge transfer phenomenon.
> Experiments on CIFAR-10/100, TinyImageNet, and ImageNet-1K with both ResNet and
> ViT architectures demonstrate that our method achieves competitive or superior
> accuracy while reducing training time up to 7.88x. Our code is released at
> https://github.com/a2jinhee/EMQNet_jk.

