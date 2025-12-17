---
layout: default
title: Learning an Image Editing Model without Image Editing Pairs
---

# Learning an Image Editing Model without Image Editing Pairs

**arXiv**: [2510.14978v1](https://arxiv.org/abs/2510.14978) | [PDF](https://arxiv.org/pdf/2510.14978.pdf)

**作者**: Nupur Kumari, Sheng-Yu Wang, Nanxuan Zhao, Yotam Nitzan, Yuheng Li, Krishna Kumar Singh, Richard Zhang, Eli Shechtman, Jun-Yan Zhu, Xun Huang

---

## 💡 一句话要点

**提出无配对数据图像编辑训练范式，利用视觉语言模型反馈优化扩散模型**

**关键词**: `图像编辑` `无配对训练` `扩散模型` `视觉语言模型` `分布匹配损失` `端到端优化`

## 📋 核心要点

1. 核心问题：图像编辑模型依赖大规模输入-目标配对数据，难以获取且易传播预训练模型伪影
2. 方法要点：通过展开扩散模型训练，结合视觉语言模型评估编辑指令遵循和内容保留，提供端到端梯度优化
3. 实验或效果：在标准基准测试中，无配对数据下性能与监督训练模型相当，优于基于强化学习的方法

## 📄 摘要（原文）

> Recent image editing models have achieved impressive results while following
> natural language editing instructions, but they rely on supervised fine-tuning
> with large datasets of input-target pairs. This is a critical bottleneck, as
> such naturally occurring pairs are hard to curate at scale. Current workarounds
> use synthetic training pairs that leverage the zero-shot capabilities of
> existing models. However, this can propagate and magnify the artifacts of the
> pretrained model into the final trained model. In this work, we present a new
> training paradigm that eliminates the need for paired data entirely. Our
> approach directly optimizes a few-step diffusion model by unrolling it during
> training and leveraging feedback from vision-language models (VLMs). For each
> input and editing instruction, the VLM evaluates if an edit follows the
> instruction and preserves unchanged content, providing direct gradients for
> end-to-end optimization. To ensure visual fidelity, we incorporate distribution
> matching loss (DMD), which constrains generated images to remain within the
> image manifold learned by pretrained models. We evaluate our method on standard
> benchmarks and include an extensive ablation study. Without any paired data,
> our method performs on par with various image editing diffusion models trained
> on extensive supervised paired data, under the few-step setting. Given the same
> VLM as the reward model, we also outperform RL-based techniques like Flow-GRPO.

