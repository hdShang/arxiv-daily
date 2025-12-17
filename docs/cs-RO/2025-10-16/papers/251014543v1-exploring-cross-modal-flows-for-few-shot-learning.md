---
layout: default
title: Exploring Cross-Modal Flows for Few-Shot Learning
---

# Exploring Cross-Modal Flows for Few-Shot Learning

**arXiv**: [2510.14543v1](https://arxiv.org/abs/2510.14543) | [PDF](https://arxiv.org/pdf/2510.14543.pdf)

**作者**: Ziqi Jiang, Yanghao Wang, Long Chen

---

## 💡 一句话要点

**提出Flow Matching Alignment以解决复杂数据集中的跨模态对齐问题**

**关键词**: `跨模态学习` `少样本学习` `参数高效微调` `Flow Matching` `特征对齐` `噪声增强`

## 📋 核心要点

1. 现有参数高效微调方法仅单步调整，难以处理高度纠缠的跨模态特征
2. FMA通过多步调整学习跨模态速度场，并引入噪声增强和早停求解器
3. 实验显示FMA在多个基准和骨干网络上显著提升性能，尤其在挑战性数据集

## 📄 摘要（原文）

> Aligning features from different modalities, is one of the most fundamental
> challenges for cross-modal tasks. Although pre-trained vision-language models
> can achieve a general alignment between image and text, they often require
> parameter-efficient fine-tuning (PEFT) for further adjustment. Today's PEFT
> methods (e.g., prompt tuning, LoRA-based, or adapter-based) always selectively
> fine-tune a subset of parameters, which can slightly adjust either visual or
> textual features, and avoid overfitting. In this paper, we are the first to
> highlight that all existing PEFT methods perform one-step adjustment. It is
> insufficient for complex (or difficult) datasets, where features of different
> modalities are highly entangled. To this end, we propose the first
> model-agnostic multi-step adjustment approach by learning a cross-modal
> velocity field: Flow Matching Alignment (FMA). Specifically, to ensure the
> correspondence between categories during training, we first utilize a fixed
> coupling strategy. Then, we propose a noise augmentation strategy to alleviate
> the data scarcity issue. Finally, we design an early-stopping solver, which
> terminates the transformation process earlier, improving both efficiency and
> accuracy. Compared with one-step PEFT methods, FMA has the multi-step
> rectification ability to achieve more precise and robust alignment. Extensive
> results have demonstrated that FMA can consistently yield significant
> performance gains across various benchmarks and backbones, particularly on
> challenging datasets.

