---
layout: default
title: Dynamic Residual Encoding with Slide-Level Contrastive Learning for End-to-End Whole Slide Image Representation
---

# Dynamic Residual Encoding with Slide-Level Contrastive Learning for End-to-End Whole Slide Image Representation

**arXiv**: [2511.05034v1](https://arxiv.org/abs/2511.05034) | [PDF](https://arxiv.org/pdf/2511.05034.pdf)

**作者**: Jing Jin, Xu Liu, Te Gao, Zhihong Shi, Yixiong Liang, Ruiqing Zheng, Hulin Kuang, Min Zeng, Shichao Kan

---

## 💡 一句话要点

**提出动态残差编码与切片级对比学习以端到端学习全切片图像表示**

**关键词**: `全切片图像表示` `动态残差编码` `切片级对比学习` `记忆库` `癌症亚型分类` `突变预测`

## 📋 核心要点

1. 核心问题：全切片图像包含数万图块，GPU限制下难以在单个小批次中计算所有图块梯度。
2. 方法要点：使用记忆库存储图块特征，结合采样与检索特征进行残差编码生成表示。
3. 实验或效果：在癌症亚型分类、识别和突变预测任务中验证了方法的有效性。

## 📄 摘要（原文）

> Whole Slide Image (WSI) representation is critical for cancer subtyping,
> cancer recognition and mutation prediction.Training an end-to-end WSI
> representation model poses significant challenges, as a standard gigapixel
> slide can contain tens of thousands of image tiles, making it difficult to
> compute gradients of all tiles in a single mini-batch due to current GPU
> limitations. To address this challenge, we propose a method of dynamic residual
> encoding with slide-level contrastive learning (DRE-SLCL) for end-to-end WSI
> representation. Our approach utilizes a memory bank to store the features of
> tiles across all WSIs in the dataset. During training, a mini-batch usually
> contains multiple WSIs. For each WSI in the batch, a subset of tiles is
> randomly sampled and their features are computed using a tile encoder. Then,
> additional tile features from the same WSI are selected from the memory bank.
> The representation of each individual WSI is generated using a residual
> encoding technique that incorporates both the sampled features and those
> retrieved from the memory bank. Finally, the slide-level contrastive loss is
> computed based on the representations and histopathology reports ofthe WSIs
> within the mini-batch. Experiments conducted over cancer subtyping, cancer
> recognition, and mutation prediction tasks proved the effectiveness of the
> proposed DRE-SLCL method.

