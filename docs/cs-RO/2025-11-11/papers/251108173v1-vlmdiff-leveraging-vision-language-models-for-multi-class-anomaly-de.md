---
layout: default
title: VLMDiff: Leveraging Vision-Language Models for Multi-Class Anomaly Detection with Diffusion
---

# VLMDiff: Leveraging Vision-Language Models for Multi-Class Anomaly Detection with Diffusion

**arXiv**: [2511.08173v1](https://arxiv.org/abs/2511.08173) | [PDF](https://arxiv.org/pdf/2511.08173.pdf)

**作者**: Samet Hicsonmez, Abd El Rahman Shabayek, Djamila Aouada

---

## 💡 一句话要点

**提出VLMDiff框架，利用视觉语言模型和扩散模型解决多类视觉异常检测问题**

**关键词**: `视觉异常检测` `扩散模型` `视觉语言模型` `多类检测` `无监督学习` `异常定位`

## 📋 核心要点

1. 多类真实图像中的视觉异常检测是重大挑战，现有方法泛化性差且需逐类训练
2. 集成预训练VLM和LDM，通过提示生成图像描述作为扩散模型条件，无需人工标注
3. 在Real-IAD和COCO-AD数据集上，像素级PRO指标提升高达25点和8点，优于先进方法

## 📄 摘要（原文）

> Detecting visual anomalies in diverse, multi-class real-world images is a significant challenge. We introduce \ours, a novel unsupervised multi-class visual anomaly detection framework. It integrates a Latent Diffusion Model (LDM) with a Vision-Language Model (VLM) for enhanced anomaly localization and detection. Specifically, a pre-trained VLM with a simple prompt extracts detailed image descriptions, serving as additional conditioning for LDM training. Current diffusion-based methods rely on synthetic noise generation, limiting their generalization and requiring per-class model training, which hinders scalability. \ours, however, leverages VLMs to obtain normal captions without manual annotations or additional training. These descriptions condition the diffusion model, learning a robust normal image feature representation for multi-class anomaly detection. Our method achieves competitive performance, improving the pixel-level Per-Region-Overlap (PRO) metric by up to 25 points on the Real-IAD dataset and 8 points on the COCO-AD dataset, outperforming state-of-the-art diffusion-based approaches. Code is available at https://github.com/giddyyupp/VLMDiff.

