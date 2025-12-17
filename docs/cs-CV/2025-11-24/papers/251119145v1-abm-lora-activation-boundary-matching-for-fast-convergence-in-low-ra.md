---
layout: default
title: ABM-LoRA: Activation Boundary Matching for Fast Convergence in Low-Rank Adaptation
---

# ABM-LoRA: Activation Boundary Matching for Fast Convergence in Low-Rank Adaptation

**arXiv**: [2511.19145v1](https://arxiv.org/abs/2511.19145) | [PDF](https://arxiv.org/pdf/2511.19145.pdf)

**作者**: Dongha Lee, Jinhee Park, Minjun Kim, Junseok Kwon

---

## 💡 一句话要点

**提出ABM-LoRA以加速低秩适配器收敛，通过激活边界匹配优化初始化。**

**关键词**: `低秩适配` `初始化策略` `梯度投影` `激活边界匹配` `模型微调` `收敛加速`

## 📋 核心要点

1. LoRA随机初始化导致梯度更新不匹配，造成信息损失和收敛缓慢。
2. ABM-LoRA在训练前对齐适配器与预训练模型的激活边界，最大化梯度投影。
3. 在语言理解、对话生成和视觉识别任务中，ABM-LoRA显著提升收敛速度和准确率。

## 📄 摘要（原文）

> We propose Activation Boundary Matching for Low-Rank Adaptation (ABM-LoRA), a principled initialization strategy that substantially accelerates the convergence of low-rank adapters. While LoRA offers high parameter efficiency, its random initialization restricts gradient updates to a mismatched tangent space, causing significant information loss and hindering early convergence. Our ABM-LoRA addresses this by aligning the adapter's activation boundaries with those of the pretrained model before downstream training, thereby maximizing the projection of full-parameter gradients into the adapter subspace. This alignment sharply reduces information loss at initialization, yields a lower starting loss, and accelerates convergence. We demonstrate ABM-LoRA's effectiveness across diverse architectures and tasks: language understanding (T5-Base on GLUE), dialogue generation (LLaMA2-7B on WizardLM), and vision recognition (ViT-B/16 on VTAB-1K). On VTAB-1K, it achieves the highest accuracy among all methods, with strong gains on structured reasoning tasks requiring geometric understanding.

