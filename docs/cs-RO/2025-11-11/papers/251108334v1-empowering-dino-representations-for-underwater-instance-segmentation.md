---
layout: default
title: Empowering DINO Representations for Underwater Instance Segmentation via Aligner and Prompter
---

# Empowering DINO Representations for Underwater Instance Segmentation via Aligner and Prompter

**arXiv**: [2511.08334v1](https://arxiv.org/abs/2511.08334) | [PDF](https://arxiv.org/pdf/2511.08334.pdf)

**作者**: Zhiyang Chen, Chen Zhang, Hao Fang, Runmin Cong

---

## 💡 一句话要点

**提出DiveSeg框架，通过AquaStyle Aligner和ObjectPrior Prompter增强DINO表示，以解决水下实例分割问题。**

**关键词**: `水下实例分割` `DINO模型` `AquaStyle Aligner` `ObjectPrior Prompter` `海洋视觉` `实例分割框架`

## 📋 核心要点

1. 核心问题：水下实例分割需结合像素级理解和实例级区分，应用于海洋资源探索和生态保护。
2. 方法要点：引入AquaStyle Aligner嵌入水下颜色风格特征，ObjectPrior Prompter提供基于二值分割的对象先验。
3. 实验或效果：在UIIS和USIS10K数据集上实现最先进性能，代码已开源。

## 📄 摘要（原文）

> Underwater instance segmentation (UIS), integrating pixel-level understanding and instance-level discrimination, is a pivotal technology in marine resource exploration and ecological protection. In recent years, large-scale pretrained visual foundation models, exemplified by DINO, have advanced rapidly and demonstrated remarkable performance on complex downstream tasks. In this paper, we demonstrate that DINO can serve as an effective feature learner for UIS, and we introduce DiveSeg, a novel framework built upon two insightful components: (1) The AquaStyle Aligner, designed to embed underwater color style features into the DINO fine-tuning process, facilitating better adaptation to the underwater domain. (2) The ObjectPrior Prompter, which incorporates binary segmentation-based prompts to deliver object-level priors, provides essential guidance for instance segmentation task that requires both object- and instance-level reasoning. We conduct thorough experiments on the popular UIIS and USIS10K datasets, and the results show that DiveSeg achieves the state-of-the-art performance. Code: https://github.com/ettof/Diveseg.

