---
layout: default
title: OmniText: A Training-Free Generalist for Controllable Text-Image Manipulation
---

# OmniText: A Training-Free Generalist for Controllable Text-Image Manipulation

**arXiv**: [2510.24093v1](https://arxiv.org/abs/2510.24093) | [PDF](https://arxiv.org/pdf/2510.24093.pdf)

**作者**: Agus Gunawan, Samuel Teodoro, Yun Chen, Soo Ye Kim, Jihyong Oh, Munchurl Kim

---

## 💡 一句话要点

**提出OmniText训练免费通用方法，解决文本图像操作中的文本移除、风格控制和重复字母问题。**

**关键词**: `文本图像操作` `训练免费方法` `注意力机制` `文本移除` `风格控制` `基准数据集`

## 📋 核心要点

1. 核心问题：现有文本修复方法无法移除文本、缺乏风格控制且易生成重复字母。
2. 方法要点：利用自注意力反转和交叉注意力重分布实现文本移除与风格内容控制。
3. 实验或效果：在OmniText-Bench基准上实现SOTA性能，与专业方法相当。

## 📄 摘要（原文）

> Recent advancements in diffusion-based text synthesis have demonstrated
> significant performance in inserting and editing text within images via
> inpainting. However, despite the potential of text inpainting methods, three
> key limitations hinder their applicability to broader Text Image Manipulation
> (TIM) tasks: (i) the inability to remove text, (ii) the lack of control over
> the style of rendered text, and (iii) a tendency to generate duplicated
> letters. To address these challenges, we propose OmniText, a training-free
> generalist capable of performing a wide range of TIM tasks. Specifically, we
> investigate two key properties of cross- and self-attention mechanisms to
> enable text removal and to provide control over both text styles and content.
> Our findings reveal that text removal can be achieved by applying
> self-attention inversion, which mitigates the model's tendency to focus on
> surrounding text, thus reducing text hallucinations. Additionally, we
> redistribute cross-attention, as increasing the probability of certain text
> tokens reduces text hallucination. For controllable inpainting, we introduce
> novel loss functions in a latent optimization framework: a cross-attention
> content loss to improve text rendering accuracy and a self-attention style loss
> to facilitate style customization. Furthermore, we present OmniText-Bench, a
> benchmark dataset for evaluating diverse TIM tasks. It includes input images,
> target text with masks, and style references, covering diverse applications
> such as text removal, rescaling, repositioning, and insertion and editing with
> various styles. Our OmniText framework is the first generalist method capable
> of performing diverse TIM tasks. It achieves state-of-the-art performance
> across multiple tasks and metrics compared to other text inpainting methods and
> is comparable with specialist methods.

