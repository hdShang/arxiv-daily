---
layout: default
title: Sharing the Learned Knowledge-base to Estimate Convolutional Filter Parameters for Continual Image Restoration
---

# Sharing the Learned Knowledge-base to Estimate Convolutional Filter Parameters for Continual Image Restoration

**arXiv**: [2511.05421v1](https://arxiv.org/abs/2511.05421) | [PDF](https://arxiv.org/pdf/2511.05421.pdf)

**作者**: Aupendu Kar, Krishnendu Ghosh, Prabir Kumar Biswas

---

## 💡 一句话要点

**提出共享知识库的卷积层修改方法，以在持续图像恢复中适应新任务而不忘旧任务。**

**关键词**: `持续学习` `图像恢复` `卷积层修改` `知识共享` `计算效率`

## 📋 核心要点

1. 核心问题：持续学习中图像恢复任务面临大图像尺寸和多样化退化挑战，现有方法需复杂架构修改。
2. 方法要点：通过简单修改卷积层，共享先前任务知识，无需改动主干架构，减少计算开销。
3. 实验或效果：实验验证新任务引入不损害旧任务性能，且新任务性能通过知识库适应得到提升。

## 📄 摘要（原文）

> Continual learning is an emerging topic in the field of deep learning, where
> a model is expected to learn continuously for new upcoming tasks without
> forgetting previous experiences. This field has witnessed numerous
> advancements, but few works have been attempted in the direction of image
> restoration. Handling large image sizes and the divergent nature of various
> degradation poses a unique challenge in the restoration domain. However,
> existing works require heavily engineered architectural modifications for new
> task adaptation, resulting in significant computational overhead.
> Regularization-based methods are unsuitable for restoration, as different
> restoration challenges require different kinds of feature processing. In this
> direction, we propose a simple modification of the convolution layer to adapt
> the knowledge from previous restoration tasks without touching the main
> backbone architecture. Therefore, it can be seamlessly applied to any deep
> architecture without any structural modifications. Unlike other approaches, we
> demonstrate that our model can increase the number of trainable parameters
> without significantly increasing computational overhead or inference time.
> Experimental validation demonstrates that new restoration tasks can be
> introduced without compromising the performance of existing tasks. We also show
> that performance on new restoration tasks improves by adapting the knowledge
> from the knowledge base created by previous restoration tasks. The code is
> available at https://github.com/aupendu/continual-restore.

