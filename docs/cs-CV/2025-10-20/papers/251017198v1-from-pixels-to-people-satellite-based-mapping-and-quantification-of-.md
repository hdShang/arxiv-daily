---
layout: default
title: From Pixels to People: Satellite-Based Mapping and Quantification of Riverbank Erosion and Lost Villages in Bangladesh
---

# From Pixels to People: Satellite-Based Mapping and Quantification of Riverbank Erosion and Lost Villages in Bangladesh

**arXiv**: [2510.17198v1](https://arxiv.org/abs/2510.17198) | [PDF](https://arxiv.org/pdf/2510.17198.pdf)

**作者**: M Saifuzzaman Rafat, Mohd Ruhul Ameen, Akif Islam, Abu Saleh Musa Miah, Jungpil Shin

---

## 💡 一句话要点

**提出基于SAM的河流侵蚀监测方法，用于孟加拉国村庄损失量化**

**关键词**: `河流侵蚀监测` `卫星图像分割` `Segment Anything模型` `土地损失量化` `孟加拉国数据集`

## 📋 核心要点

1. 核心问题：孟加拉国河流侵蚀导致村庄消失和土地损失，传统监测困难。
2. 方法要点：结合颜色通道分析和微调SAM掩码解码器，识别侵蚀特征。
3. 实验或效果：在自定义数据集上，mIoU达86.30%，Dice分数92.60%，优于传统方法。

## 📄 摘要（原文）

> The great rivers of Bangladesh, arteries of commerce and sustenance, are also
> agents of relentless destruction. Each year, they swallow whole villages and
> vast tracts of farmland, erasing communities from the map and displacing
> thousands of families. To track this slow-motion catastrophe has, until now,
> been a Herculean task for human analysts. Here we show how a powerful
> general-purpose vision model, the Segment Anything Model (SAM), can be adapted
> to this task with remarkable precision. To do this, we assembled a new dataset
> - a digital chronicle of loss compiled from historical Google Earth imagery of
> Bangladesh's most vulnerable regions, including Mokterer Char Union, Kedarpur
> Union, Balchipara village, and Chowhali Upazila, from 2003 to 2025. Crucially,
> this dataset is the first to include manually annotated data on the settlements
> that have vanished beneath the water. Our method first uses a simple
> color-channel analysis to provide a rough segmentation of land and water, and
> then fine-tunes SAM's mask decoder to recognize the subtle signatures of
> riverbank erosion. The resulting model demonstrates a keen eye for this
> destructive process, achieving a mean Intersection over Union of 86.30% and a
> Dice score of 92.60% - a performance that significantly surpasses traditional
> methods and off-the-shelf deep learning models. This work delivers three key
> contributions: the first annotated dataset of disappeared settlements in
> Bangladesh due to river erosion; a specialized AI model fine-tuned for this
> critical task; and a method for quantifying land loss with compelling visual
> evidence. Together, these tools provide a powerful new lens through which
> policymakers and disaster management agencies can monitor erosion, anticipate
> its trajectory, and ultimately protect the vulnerable communities in its path.

