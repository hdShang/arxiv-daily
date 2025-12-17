---
layout: default
title: PixCLIP: Achieving Fine-grained Visual Language Understanding via Any-granularity Pixel-Text Alignment Learning
---

# PixCLIP: Achieving Fine-grained Visual Language Understanding via Any-granularity Pixel-Text Alignment Learning

**arXiv**: [2511.04601v1](https://arxiv.org/abs/2511.04601) | [PDF](https://arxiv.org/pdf/2511.04601.pdf)

**作者**: Yicheng Xiao, Yu Chen, Haoxuan Ma, Jiale Hong, Caorui Li, Lingxiang Wu, Haiyun Guo, Jinqiao Wang

---

## 💡 一句话要点

**提出PixCLIP框架，通过像素级对齐和长文本处理解决细粒度视觉语言理解问题**

**关键词**: `像素级对齐` `长文本处理` `视觉语言理解` `多模态学习` `细粒度对齐`

## 📋 核心要点

1. 核心问题：CLIP模型在细粒度图像-文本对齐方面受限，文本编码器无法处理长文本序列
2. 方法要点：构建LongGRIT数据集，采用三分支框架实现任意粒度像素-文本对齐学习
3. 实验或效果：在像素级交互和长文本处理上取得突破，达到先进性能

## 📄 摘要（原文）

> While the Contrastive Language-Image Pretraining(CLIP) model has achieved
> remarkable success in a variety of downstream vison language understanding
> tasks, enhancing its capability for fine-grained image-text alignment remains
> an active research focus. To this end, most existing works adopt the strategy
> of explicitly increasing the granularity of visual information processing,
> e.g., incorporating visual prompts to guide the model focus on specific local
> regions within the image. Meanwhile, researches on Multimodal Large Language
> Models(MLLMs) have demonstrated that training with long and detailed textual
> descriptions can effectively improve the model's fine-grained vision-language
> alignment. However, the inherent token length limitation of CLIP's text encoder
> fundamentally limits CLIP to process more granular textual information embedded
> in long text sequences. To synergistically leverage the advantages of enhancing
> both visual and textual content processing granularity, we propose PixCLIP, a
> novel framework designed to concurrently accommodate visual prompt inputs and
> process lengthy textual descriptions. Specifically, we first establish an
> automated annotation pipeline capable of generating pixel-level localized,
> long-form textual descriptions for images. Utilizing this pipeline, we
> construct LongGRIT, a high-quality dataset comprising nearly 1.5 million
> samples. Secondly, we replace CLIP's original text encoder with the LLM and
> propose a three-branch pixel-text alignment learning framework, facilitating
> fine-grained alignment between image regions and corresponding textual
> descriptions at arbitrary granularity. Experiments demonstrate that PixCLIP
> showcases breakthroughs in pixel-level interaction and handling long-form
> texts, achieving state-of-the-art performance.

