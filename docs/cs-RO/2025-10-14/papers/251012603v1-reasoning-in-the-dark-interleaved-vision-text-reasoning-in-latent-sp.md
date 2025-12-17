---
layout: default
title: Reasoning in the Dark: Interleaved Vision-Text Reasoning in Latent Space
---

# Reasoning in the Dark: Interleaved Vision-Text Reasoning in Latent Space

**arXiv**: [2510.12603v1](https://arxiv.org/abs/2510.12603) | [PDF](https://arxiv.org/pdf/2510.12603.pdf)

**作者**: Chao Chen, Zhixin Ma, Yongqi Li, Yupeng Hu, Yinwei Wei, Wenjie Li, Liqiang Nie

---

## 💡 一句话要点

**提出IVT-LR方法以解决多模态推理中显式步骤依赖导致的标注成本高和推理延迟问题**

**关键词**: `多模态推理` `潜在空间推理` `推理效率优化` `隐式表示学习` `多模态大语言模型`

## 📋 核心要点

1. 核心问题：当前多模态推理方法依赖显式推理步骤，需要大量视觉-文本标注并引入高推理延迟
2. 方法要点：在潜在空间中注入视觉和文本信息，结合隐式文本和视觉表示进行推理
3. 实验或效果：在M3CoT和ScienceQA数据集上平均准确率提升5.45%，推理速度提升5倍以上

## 📄 摘要（原文）

> Multimodal reasoning aims to enhance the capabilities of MLLMs by
> incorporating intermediate reasoning steps before reaching the final answer. It
> has evolved from text-only reasoning to the integration of visual information,
> enabling the thought process to be conveyed through both images and text.
> Despite its effectiveness, current multimodal reasoning methods depend on
> explicit reasoning steps that require labor-intensive vision-text annotations
> and inherently introduce significant inference latency. To address these
> issues, we introduce multimodal latent reasoning with the advantages of
> multimodal representation, reduced annotation, and inference efficiency. To
> facilicate it, we propose Interleaved Vision-Text Latent Reasoning (IVT-LR),
> which injects both visual and textual information in the reasoning process
> within the latent space. Specifically, IVT-LR represents each reasoning step by
> combining two implicit parts: latent text (the hidden states from the previous
> step) and latent vision (a set of selected image embeddings). We further
> introduce a progressive multi-stage training strategy to enable MLLMs to
> perform the above multimodal latent reasoning steps. Experiments on M3CoT and
> ScienceQA demonstrate that our IVT-LR method achieves an average performance
> increase of 5.45% in accuracy, while simultaneously achieving a speed increase
> of over 5 times compared to existing approaches. Code available at
> https://github.com/FYYDCC/IVT-LR.

