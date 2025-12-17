---
layout: default
title: Exploring the Underwater World Segmentation without Extra Training
---

# Exploring the Underwater World Segmentation without Extra Training

**arXiv**: [2511.07923v1](https://arxiv.org/abs/2511.07923) | [PDF](https://arxiv.org/pdf/2511.07923.pdf)

**作者**: Bingyu Li, Tao Huo, Da Zhang, Zhiyuan Zhao, Junyu Gao, Xuelong Li

---

## 💡 一句话要点

**提出Earth2Ocean框架，实现无额外训练的水下开放词汇分割。**

**关键词**: `水下分割` `开放词汇分割` `视觉-语言模型` `训练免费框架` `几何引导` `语义对齐`

## 📋 核心要点

1. 核心问题：现有分割模型局限于陆地场景，缺乏水下生物准确分割。
2. 方法要点：通过几何引导视觉掩码生成和类别-视觉语义对齐模块，迁移视觉-语言模型。
3. 实验或效果：在UOVSBench基准上显著提升性能，保持高效推理。

## 📄 摘要（原文）

> Accurate segmentation of marine organisms is vital for biodiversity monitoring and ecological assessment, yet existing datasets and models remain largely limited to terrestrial scenes. To bridge this gap, we introduce \textbf{AquaOV255}, the first large-scale and fine-grained underwater segmentation dataset containing 255 categories and over 20K images, covering diverse categories for open-vocabulary (OV) evaluation. Furthermore, we establish the first underwater OV segmentation benchmark, \textbf{UOVSBench}, by integrating AquaOV255 with five additional underwater datasets to enable comprehensive evaluation. Alongside, we present \textbf{Earth2Ocean}, a training-free OV segmentation framework that transfers terrestrial vision--language models (VLMs) to underwater domains without any additional underwater training. Earth2Ocean consists of two core components: a Geometric-guided Visual Mask Generator (\textbf{GMG}) that refines visual features via self-similarity geometric priors for local structure perception, and a Category-visual Semantic Alignment (\textbf{CSA}) module that enhances text embeddings through multimodal large language model reasoning and scene-aware template construction. Extensive experiments on the UOVSBench benchmark demonstrate that Earth2Ocean achieves significant performance improvement on average while maintaining efficient inference.

