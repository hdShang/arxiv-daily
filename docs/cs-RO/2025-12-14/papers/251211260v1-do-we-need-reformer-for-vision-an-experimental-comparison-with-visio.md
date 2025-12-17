---
layout: default
title: Do We Need Reformer for Vision? An Experimental Comparison with Vision Transformers
---

# Do We Need Reformer for Vision? An Experimental Comparison with Vision Transformers

**arXiv**: [2512.11260v1](https://arxiv.org/abs/2512.11260) | [PDF](https://arxiv.org/pdf/2512.11260.pdf)

**作者**: Ali El Bellaj, Mohammed-Amine Cheddadi, Rhassan Berber

---

## 💡 一句话要点

**比较Reformer与Vision Transformer在视觉任务中的效率与性能**

**关键词**: `视觉Transformer` `Reformer架构` `局部敏感哈希注意力` `计算效率` `高分辨率图像` `实验比较`

## 📋 核心要点

1. 核心问题：标准Vision Transformer因全局自注意力计算复杂度高，限制高分辨率输入应用。
2. 方法要点：采用Reformer架构，结合局部敏感哈希注意力降低理论复杂度至O(n log n)。
3. 实验或效果：在CIFAR-10上Reformer更准确，但在更大规模和高分辨率设置中ViT实际效率更高。

## 📄 摘要（原文）

> Transformers have recently demonstrated strong performance in computer vision, with Vision Transformers (ViTs) leveraging self-attention to capture both low-level and high-level image features. However, standard ViTs remain computationally expensive, since global self-attention scales quadratically with the number of tokens, which limits their practicality for high-resolution inputs and resource-constrained settings.
>   In this work, we investigate the Reformer architecture as an alternative vision backbone. By combining patch-based tokenization with locality-sensitive hashing (LSH) attention, our model approximates global self-attention while reducing its theoretical time complexity from $\mathcal{O}(n^2)$ to $\mathcal{O}(n \log n)$ in the sequence length $n$. We evaluate the proposed Reformer-based vision model on CIFAR-10 to assess its behavior on small-scale datasets, on ImageNet-100 to study its accuracy--efficiency trade-off in a more realistic setting, and on a high-resolution medical imaging dataset to evaluate the model under longer token sequences.
>   While the Reformer achieves higher accuracy on CIFAR-10 compared to our ViT-style baseline, the ViT model consistently outperforms the Reformer in our experiments in terms of practical efficiency and end-to-end computation time across the larger and higher-resolution settings. These results suggest that, despite the theoretical advantages of LSH-based attention, meaningful computation gains require sequence lengths substantially longer than those produced by typical high-resolution images.

