---
layout: default
title: FlexICL: A Flexible Visual In-context Learning Framework for Elbow and Wrist Ultrasound Segmentation
---

# FlexICL: A Flexible Visual In-context Learning Framework for Elbow and Wrist Ultrasound Segmentation

**arXiv**: [2510.26049v1](https://arxiv.org/abs/2510.26049) | [PDF](https://arxiv.org/pdf/2510.26049.pdf)

**作者**: Yuyue Zhou, Jessica Knight, Shrimanti Ghosh, Banafshe Felfeliyan, Jacob L. Jaremko, Abhilash R. Hareendranathan

---

## 💡 一句话要点

**提出FlexICL框架以解决肘腕超声分割中标注数据稀缺问题**

**关键词**: `视觉上下文学习` `超声图像分割` `医学影像` `标注效率` `模型鲁棒性`

## 📋 核心要点

1. 核心问题：肘腕骨折超声分割需专家标注，但标注成本高且耗时。
2. 方法要点：采用视觉上下文学习，仅需少量标注帧，通过图像拼接和增强策略提升性能。
3. 实验或效果：在四个数据集上，仅用5%训练图像，Dice系数优于现有模型1-27%。

## 📄 摘要（原文）

> Elbow and wrist fractures are the most common fractures in pediatric
> populations. Automatic segmentation of musculoskeletal structures in ultrasound
> (US) can improve diagnostic accuracy and treatment planning. Fractures appear
> as cortical defects but require expert interpretation. Deep learning (DL) can
> provide real-time feedback and highlight key structures, helping lightly
> trained users perform exams more confidently. However, pixel-wise expert
> annotations for training remain time-consuming and costly. To address this
> challenge, we propose FlexICL, a novel and flexible in-context learning (ICL)
> framework for segmenting bony regions in US images. We apply it to an
> intra-video segmentation setting, where experts annotate only a small subset of
> frames, and the model segments unseen frames. We systematically investigate
> various image concatenation techniques and training strategies for visual ICL
> and introduce novel concatenation methods that significantly enhance model
> performance with limited labeled data. By integrating multiple augmentation
> strategies, FlexICL achieves robust segmentation performance across four wrist
> and elbow US datasets while requiring only 5% of the training images. It
> outperforms state-of-the-art visual ICL models like Painter, MAE-VQGAN, and
> conventional segmentation models like U-Net and TransUNet by 1-27% Dice
> coefficient on 1,252 US sweeps. These initial results highlight the potential
> of FlexICL as an efficient and scalable solution for US image segmentation well
> suited for medical imaging use cases where labeled data is scarce.

