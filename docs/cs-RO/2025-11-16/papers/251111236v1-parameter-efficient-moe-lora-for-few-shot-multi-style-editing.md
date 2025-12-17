---
layout: default
title: Parameter-Efficient MoE LoRA for Few-Shot Multi-Style Editing
---

# Parameter-Efficient MoE LoRA for Few-Shot Multi-Style Editing

**arXiv**: [2511.11236v1](https://arxiv.org/abs/2511.11236) | [PDF](https://arxiv.org/pdf/2511.11236.pdf)

**作者**: Cong Cao, Yujie Xu, Xiaodong Xu

---

## 💡 一句话要点

**提出参数高效MoE LoRA框架以解决少样本多风格图像编辑问题**

**关键词**: `少样本学习` `多风格图像编辑` `MoE LoRA` `参数高效微调` `扩散模型优化`

## 📋 核心要点

1. 核心问题：通用图像编辑模型在少样本新风格下效果不佳，需高效微调。
2. 方法要点：结合风格特定与共享路由的MoE LoRA，自动优化秩并集成对抗学习。
3. 实验或效果：在五风格数据集上超越现有方法，参数显著减少。

## 📄 摘要（原文）

> In recent years, image editing has garnered growing attention. However, general image editing models often fail to produce satisfactory results when confronted with new styles. The challenge lies in how to effectively fine-tune general image editing models to new styles using only a limited amount of paired data. To address this issue, this paper proposes a novel few-shot style editing framework. For this task, we construct a benchmark dataset that encompasses five distinct styles. Correspondingly, we propose a parameter-efficient multi-style Mixture-of-Experts Low-Rank Adaptation (MoE LoRA) with style-specific and style-shared routing mechanisms for jointly fine-tuning multiple styles. The style-specific routing ensures that different styles do not interfere with one another, while the style-shared routing adaptively allocates shared MoE LoRAs to learn common patterns. Our MoE LoRA can automatically determine the optimal ranks for each layer through a novel metric-guided approach that estimates the importance score of each single-rank component. Additionally, we explore the optimal location to insert LoRA within the Diffusion in Transformer (DiT) model and integrate adversarial learning and flow matching to guide the diffusion training process. Experimental results demonstrate that our proposed method outperforms existing state-of-the-art approaches with significantly fewer LoRA parameters.

