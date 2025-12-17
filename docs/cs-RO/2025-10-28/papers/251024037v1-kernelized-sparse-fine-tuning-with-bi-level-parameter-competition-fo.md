---
layout: default
title: Kernelized Sparse Fine-Tuning with Bi-level Parameter Competition for Vision Models
---

# Kernelized Sparse Fine-Tuning with Bi-level Parameter Competition for Vision Models

**arXiv**: [2510.24037v1](https://arxiv.org/abs/2510.24037) | [PDF](https://arxiv.org/pdf/2510.24037.pdf)

**作者**: Shufan Shen, Junshu Sun, Shuhui Wang, Qingming Huang

---

## 💡 一句话要点

**提出SNELLA方法以高效微调视觉模型，解决内存高和权重定位不准问题。**

**关键词**: `参数高效微调` `稀疏调优` `视觉模型` `内存优化` `非线性核函数` `双层稀疏分配`

## 📋 核心要点

1. 核心问题：现有稀疏微调方法内存使用高，且权重定位忽略微调过程调整。
2. 方法要点：使用非线性核函数扩展低秩分解，并引入双层稀疏分配机制。
3. 实验或效果：在分类等任务中实现SOTA性能，内存减少31.1%-39.9%。

## 📄 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) aims to adapt pre-trained vision
> models to downstream tasks. Among PEFT paradigms, sparse tuning achieves
> remarkable performance by adjusting only the weights most relevant to
> downstream tasks, rather than densely tuning the entire weight matrix. Current
> methods follow a two-stage paradigm. First, it locates task-relevant weights by
> gradient information, which overlooks the parameter adjustments during
> fine-tuning and limits the performance. Second, it updates only the located
> weights by applying a sparse mask to the gradient of the weight matrix, which
> results in high memory usage due to the storage of all weight matrices in the
> optimizer. In this paper, we propose a one-stage method named SNELLA to
> overcome the above limitations. For memory usage, SNELLA selectively updates
> the weight matrix by adding it to another sparse matrix that is merged by two
> low-rank learnable matrices. We extend the low-rank decomposition by
> introducing nonlinear kernel functions, thereby increasing the rank of the
> resulting merged matrix to prevent the interdependency among weight updates,
> enabling better adaptation to downstream tasks. For locating task-relevant
> weights, we propose an adaptive bi-level sparsity allocation mechanism that
> encourages weights to compete across and inside layers based on their
> importance scores in an end-to-end manner. Extensive experiments are conducted
> on classification, segmentation, and generation tasks using different
> pre-trained vision models. The results show that SNELLA achieves SOTA
> performance with low memory usage. Notably, SNELLA obtains 1.8% (91.9% v.s.
> 90.1%) higher Top-1 accuracy on the FGVC benchmark compared to SPT-LoRA.
> Compared to previous methods, SNELLA achieves a memory reduction of 31.1%-39.9%
> across models with parameter scales from 86M to 632M. Our source codes are
> available at https://github.com/ssfgunner/SNELL.

