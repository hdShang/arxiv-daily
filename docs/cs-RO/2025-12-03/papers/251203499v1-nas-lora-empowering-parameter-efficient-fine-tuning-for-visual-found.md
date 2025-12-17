---
layout: default
title: NAS-LoRA: Empowering Parameter-Efficient Fine-Tuning for Visual Foundation Models with Searchable Adaptation
---

# NAS-LoRA: Empowering Parameter-Efficient Fine-Tuning for Visual Foundation Models with Searchable Adaptation

**arXiv**: [2512.03499v1](https://arxiv.org/abs/2512.03499) | [PDF](https://arxiv.org/pdf/2512.03499.pdf)

**作者**: Renqi Chen, Haoyang Su, Shixiang Tang

---

## 💡 一句话要点

**提出NAS-LoRA以增强视觉基础模型在特定下游任务中的参数高效微调能力**

**关键词**: `参数高效微调` `神经架构搜索` `视觉基础模型` `图像分割` `低秩适应`

## 📋 核心要点

1. 核心问题：SAM缺乏空间先验，难以适应医学和农业等专业领域。
2. 方法要点：在LoRA中集成轻量级NAS块，动态优化先验知识，并采用阶段优化策略。
3. 实验或效果：提升现有PEFT方法性能，训练成本降低24.14%，推理成本不变。

## 📄 摘要（原文）

> The Segment Anything Model (SAM) has emerged as a powerful visual foundation model for image segmentation. However, adapting SAM to specific downstream tasks, such as medical and agricultural imaging, remains a significant challenge. To address this, Low-Rank Adaptation (LoRA) and its variants have been widely employed to enhancing SAM's adaptation performance on diverse domains. Despite advancements, a critical question arises: can we integrate inductive bias into the model? This is particularly relevant since the Transformer encoder in SAM inherently lacks spatial priors within image patches, potentially hindering the acquisition of high-level semantic information. In this paper, we propose NAS-LoRA, a new Parameter-Efficient Fine-Tuning (PEFT) method designed to bridge the semantic gap between pre-trained SAM and specialized domains. Specifically, NAS-LoRA incorporates a lightweight Neural Architecture Search (NAS) block between the encoder and decoder components of LoRA to dynamically optimize the prior knowledge integrated into weight updates. Furthermore, we propose a stage-wise optimization strategy to help the ViT encoder balance weight updates and architectural adjustments, facilitating the gradual learning of high-level semantic information. Various Experiments demonstrate our NAS-LoRA improves existing PEFT methods, while reducing training cost by 24.14% without increasing inference cost, highlighting the potential of NAS in enhancing PEFT for visual foundation models.

