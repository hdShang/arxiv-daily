---
layout: default
title: Generalizing Vision-Language Models with Dedicated Prompt Guidance
---

# Generalizing Vision-Language Models with Dedicated Prompt Guidance

**arXiv**: [2512.02421v1](https://arxiv.org/abs/2512.02421) | [PDF](https://arxiv.org/pdf/2512.02421.pdf)

**作者**: Xinyao Li, Yinjie Min, Hongbo Chen, Zhekai Du, Fengling Li, Jingjing Li

---

## 💡 一句话要点

**提出GuiDG框架，通过专家引导提升视觉语言模型在领域泛化任务中的性能**

**关键词**: `视觉语言模型` `领域泛化` `提示调优` `跨模态注意力` `专家模型` `微调优化`

## 📋 核心要点

1. 核心问题：视觉语言模型微调在领域特异性和泛化能力间存在权衡，当前方法可能损害未见域的泛化能力
2. 方法要点：基于理论分析，采用两步骤框架，先通过提示调优获取源域专家，再通过跨模态注意力模块自适应集成专家指导视觉编码器微调
3. 实验或效果：在标准领域泛化基准和构建的ImageNet-DG数据集上，GuiDG优于现有微调方法，同时保持高效性

## 📄 摘要（原文）

> Fine-tuning large pretrained vision-language models (VLMs) has emerged as a prevalent paradigm for downstream adaptation, yet it faces a critical trade-off between domain specificity and domain generalization (DG) ability. Current methods typically fine-tune a universal model on the entire dataset, which potentially compromises the ability to generalize to unseen domains. To fill this gap, we provide a theoretical understanding of the generalization ability for VLM fine-tuning, which reveals that training multiple parameter-efficient expert models on partitioned source domains leads to better generalization than fine-tuning a universal model. Inspired by this finding, we propose a two-step domain-expert-Guided DG (GuiDG) framework. GuiDG first employs prompt tuning to obtain source domain experts, then introduces a Cross-Modal Attention module to guide the fine-tuning of the vision encoder via adaptive expert integration. To better evaluate few-shot DG, we construct ImageNet-DG from ImageNet and its variants. Extensive experiments on standard DG benchmarks and ImageNet-DG demonstrate that GuiDG improves upon state-of-the-art fine-tuning methods while maintaining efficiency.

