---
layout: default
title: ImageSentinel: Protecting Visual Datasets from Unauthorized Retrieval-Augmented Image Generation
---

# ImageSentinel: Protecting Visual Datasets from Unauthorized Retrieval-Augmented Image Generation

**arXiv**: [2510.12119v1](https://arxiv.org/abs/2510.12119) | [PDF](https://arxiv.org/pdf/2510.12119.pdf)

**作者**: Ziyuan Luo, Yangyi Zhao, Ka Chun Cheung, Simon See, Renjie Wan

---

## 💡 一句话要点

**提出ImageSentinel框架以保护视觉数据集免遭未经授权的检索增强图像生成使用**

**关键词**: `图像数据集保护` `检索增强图像生成` `视觉语言模型` `哨兵图像` `保护验证`

## 📋 核心要点

1. 核心问题：检索增强图像生成系统未经授权使用私有图像数据集，传统数字水印方法失效
2. 方法要点：利用视觉语言模型合成哨兵图像，通过随机字符序列作为检索键实现保护验证
3. 实验或效果：实验显示ImageSentinel能有效检测未经授权使用，同时保持授权应用的生成质量

## 📄 摘要（原文）

> The widespread adoption of Retrieval-Augmented Image Generation (RAIG) has
> raised significant concerns about the unauthorized use of private image
> datasets. While these systems have shown remarkable capabilities in enhancing
> generation quality through reference images, protecting visual datasets from
> unauthorized use in such systems remains a challenging problem. Traditional
> digital watermarking approaches face limitations in RAIG systems, as the
> complex feature extraction and recombination processes fail to preserve
> watermark signals during generation. To address these challenges, we propose
> ImageSentinel, a novel framework for protecting visual datasets in RAIG. Our
> framework synthesizes sentinel images that maintain visual consistency with the
> original dataset. These sentinels enable protection verification through
> randomly generated character sequences that serve as retrieval keys. To ensure
> seamless integration, we leverage vision-language models to generate the
> sentinel images. Experimental results demonstrate that ImageSentinel
> effectively detects unauthorized dataset usage while preserving generation
> quality for authorized applications. Code is available at
> https://github.com/luo-ziyuan/ImageSentinel.

