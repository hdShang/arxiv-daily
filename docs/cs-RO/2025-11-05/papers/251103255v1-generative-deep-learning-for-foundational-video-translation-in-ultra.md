---
layout: default
title: Generative deep learning for foundational video translation in ultrasound
---

# Generative deep learning for foundational video translation in ultrasound

**arXiv**: [2511.03255v1](https://arxiv.org/abs/2511.03255) | [PDF](https://arxiv.org/pdf/2511.03255.pdf)

**作者**: Nikolina Tomic Roshni Bhatnagar, Sarthak Jain, Connor Lau, Tien-Yu Liu, Laura Gambini, Rima Arnaout

---

## 💡 一句话要点

**提出生成式深度学习方法以解决超声子模态视频数据不平衡问题**

**关键词**: `生成式深度学习` `超声视频翻译` `数据不平衡` `对抗训练` `医学影像增强`

## 📋 核心要点

1. 超声数据中灰度与彩色多普勒子模态常不平衡，影响深度学习应用
2. 使用像素、对抗和感知损失，结合结构重建与去噪网络生成视频
3. 合成视频在分类、分割任务中与真实视频无显著差异，临床专家难以区分

## 📄 摘要（原文）

> Deep learning (DL) has the potential to revolutionize image acquisition and
> interpretation across medicine, however, attention to data imbalance and
> missingness is required. Ultrasound data presents a particular challenge
> because in addition to different views and structures, it includes several
> sub-modalities-such as greyscale and color flow doppler (CFD)-that are often
> imbalanced in clinical studies. Image translation can help balance datasets but
> is challenging for ultrasound sub-modalities to date. Here, we present a
> generative method for ultrasound CFD-greyscale video translation, trained on
> 54,975 videos and tested on 8,368. The method developed leveraged pixel-wise,
> adversarial, and perceptual loses and utilized two networks: one for
> reconstructing anatomic structures and one for denoising to achieve realistic
> ultrasound imaging. Average pairwise SSIM between synthetic videos and ground
> truth was 0.91+/-0.04. Synthetic videos performed indistinguishably from real
> ones in DL classification and segmentation tasks and when evaluated by blinded
> clinical experts: F1 score was 0.9 for real and 0.89 for synthetic videos; Dice
> score between real and synthetic segmentation was 0.97. Overall clinician
> accuracy in distinguishing real vs synthetic videos was 54+/-6% (42-61%),
> indicating realistic synthetic videos. Although trained only on heart videos,
> the model worked well on ultrasound spanning several clinical domains (average
> SSIM 0.91+/-0.05), demonstrating foundational abilities. Together, these data
> expand the utility of retrospectively collected imaging and augment the dataset
> design toolbox for medical imaging.

