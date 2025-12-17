---
layout: default
title: GPTFace: Generative Pre-training of Facial-Linguistic Transformer by Span Masking and Weakly Correlated Text-image Data
---

# GPTFace: Generative Pre-training of Facial-Linguistic Transformer by Span Masking and Weakly Correlated Text-image Data

**arXiv**: [2510.18345v1](https://arxiv.org/abs/2510.18345) | [PDF](https://arxiv.org/pdf/2510.18345.pdf)

**作者**: Yudong Li, Hao Li, Xianxu Hou, Linlin Shen

---

## 💡 一句话要点

**提出GPTFace模型，利用网络数据预训练解决面部知识学习可扩展性问题。**

**关键词**: `面部知识学习` `生成预训练` `自监督学习` `图像-文本匹配` `面部编辑`

## 📋 核心要点

1. 面部知识预训练研究不足，依赖人工标注数据集，可扩展性有限。
2. 采用自监督任务预训练，包括掩码图像/语言建模和图像-文本匹配。
3. 实验显示在属性分类和表情识别等任务中性能可比肩先进模型。

## 📄 摘要（原文）

> Compared to the prosperity of pre-training models in natural image
> understanding, the research on large-scale pre-training models for facial
> knowledge learning is still limited. Current approaches mainly rely on manually
> assembled and annotated face datasets for training, but labeling such datasets
> is labor-intensive and the trained models have limited scalability beyond the
> training data. To address these limitations, we present a generative
> pre-training model for facial knowledge learning that leverages large-scale
> web-built data for training. We use texts and images containing human faces
> crawled from the internet and conduct pre-training on self-supervised tasks,
> including masked image/language modeling (MILM) and image-text matching (ITM).
> During the generation stage, we further utilize the image-text matching loss to
> pull the generation distribution towards the control signal for controllable
> image/text generation. Experimental results demonstrate that our model achieves
> comparable performance to state-of-the-art pre-training models for various
> facial downstream tasks, such as attribution classification and expression
> recognition. Furthermore, our approach is also applicable to a wide range of
> face editing tasks, including face attribute editing, expression manipulation,
> mask removal, and photo inpainting.

