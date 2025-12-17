---
layout: default
title: uCLIP: Parameter-Efficient Multilingual Extension of Vision-Language Models with Unpaired Data
---

# uCLIP: Parameter-Efficient Multilingual Extension of Vision-Language Models with Unpaired Data

**arXiv**: [2511.13036v1](https://arxiv.org/abs/2511.13036) | [PDF](https://arxiv.org/pdf/2511.13036.pdf)

**作者**: Dahyun Chung, Donghyun Shin, Yujin Sung, Seunggi Moon, Jinwoo Jeon, Byung-Jun Lee

---

## 💡 一句话要点

**提出uCLIP框架以解决低资源语言视觉-语言对齐问题**

**关键词**: `多语言视觉-语言模型` `参数高效对齐` `对比学习` `低资源语言` `图像-文本检索`

## 📋 核心要点

1. 核心问题：CLIP模型在低资源语言中泛化差，因多语言图像-文本数据稀缺。
2. 方法要点：仅训练轻量投影模块，冻结图像和文本编码器，使用英语表示作为语义锚点。
3. 实验或效果：在XM3600基准上，对五种低资源语言检索性能显著提升。

## 📄 摘要（原文）

> Contrastive Language-Image Pre-training (CLIP) has demonstrated strong generalization across a wide range of visual tasks by leveraging large-scale English-image pairs. However, its extension to low-resource languages remains limited due to the scarcity of high-quality multilingual image-text data. Existing multilingual vision-language models exhibit consistently low retrieval performance in underrepresented languages including Czech, Finnish, Croatian, Hungarian, and Romanian on the Crossmodal-3600 (XM3600) benchmark. To address this, we propose a lightweight and data-efficient framework for multilingual vision-language alignment. Our approach requires no image-text pairs or text-text pairs and freezes both the pretrained image encoder and multilingual text encoder during training. Only a compact 1.7M-parameter projection module is trained, using a contrastive loss over English representations as semantic anchors. This minimal training setup enables robust multilingual alignment even for languages with limited supervision. Extensive evaluation across multiple multilingual retrieval benchmarks confirms the effectiveness of our method, showing significant gains in five underrepresented languages where existing models typically underperform. These findings highlight the effectiveness of our pivot-based, parameter-efficient alignment strategy for inclusive multimodal learning.

