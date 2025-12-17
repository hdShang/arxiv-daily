---
layout: default
title: LLMs-based Augmentation for Domain Adaptation in Long-tailed Food Datasets
---

# LLMs-based Augmentation for Domain Adaptation in Long-tailed Food Datasets

**arXiv**: [2511.16037v1](https://arxiv.org/abs/2511.16037) | [PDF](https://arxiv.org/pdf/2511.16037.pdf)

**作者**: Qing Wang, Chong-Wah Ngo, Ee-Peng Lim, Qianru Sun

---

## 💡 一句话要点

**提出基于大语言模型的框架以解决长尾食品数据集中的领域适应问题**

**关键词**: `食品识别` `领域适应` `长尾分布` `多模态学习` `大语言模型` `细粒度分类`

## 📋 核心要点

1. 核心问题：食品图像存在领域偏移、长尾分布和细粒度视觉差异。
2. 方法要点：利用LLMs解析图像生成文本，对齐多模态特征于共享嵌入空间。
3. 实验或效果：在多个食品数据集上优于现有长尾、领域适应和细粒度方法。

## 📄 摘要（原文）

> Training a model for food recognition is challenging because the training samples, which are typically crawled from the Internet, are visually different from the pictures captured by users in the free-living environment. In addition to this domain-shift problem, the real-world food datasets tend to be long-tailed distributed and some dishes of different categories exhibit subtle variations that are difficult to distinguish visually. In this paper, we present a framework empowered with large language models (LLMs) to address these challenges in food recognition. We first leverage LLMs to parse food images to generate food titles and ingredients. Then, we project the generated texts and food images from different domains to a shared embedding space to maximize the pair similarities. Finally, we take the aligned features of both modalities for recognition. With this simple framework, we show that our proposed approach can outperform the existing approaches tailored for long-tailed data distribution, domain adaptation, and fine-grained classification, respectively, on two food datasets.

