---
layout: default
title: PLUTO-4: Frontier Pathology Foundation Models
---

# PLUTO-4: Frontier Pathology Foundation Models

**arXiv**: [2511.02826v1](https://arxiv.org/abs/2511.02826) | [PDF](https://arxiv.org/pdf/2511.02826.pdf)

**作者**: Harshith Padigela, Shima Nofallah, Atchuth Naveen Chilaparasetti, Ryun Han, Andrew Walker, Judy Shen, Chintan Shah, Blake Martin, Aashish Sood, Elliot Miller, Ben Glass, Andy Beck, Harsha Pokkalla, Syed Ashar Javed

---

## 💡 一句话要点

**提出PLUTO-4病理学基础模型，提升多尺度病理图像任务性能。**

**关键词**: `病理学基础模型` `视觉Transformer` `自监督学习` `多尺度部署` `诊断准确率提升`

## 📋 核心要点

1. 核心问题：病理学基础模型需处理多样任务，但现有模型在规模和效率上受限。
2. 方法要点：采用两种ViT架构，PLUTO-4S优化多尺度部署，PLUTO-4G专注大容量表示。
3. 实验或效果：在公开和内部基准测试中，PLUTO-4实现SOTA，诊断准确率提升11%。

## 📄 摘要（原文）

> Foundation models trained on large-scale pathology image corpora have
> demonstrated strong transfer capabilities across diverse histopathology tasks.
> Building on this progress, we introduce PLUTO-4, our next generation of
> pathology foundation models that extend the Pathology-Universal Transformer
> (PLUTO) to frontier scale. We share two complementary Vision Transformer
> architectures in the PLUTO-4 family: a compact and efficient PLUTO-4S model
> optimized for multi-scale deployment using a FlexiViT setup with 2D-RoPE
> embeddings, and a frontier-scale PLUTO-4G model trained with a single patch
> size to maximize representation capacity and stability. Both models are
> pretrained using a self-supervised objective derived from DINOv2 on a large
> multi-institutional corpus containing 551,164 WSIs from 137,144 patients across
> over 50 institutions, spanning over 60 disease types and over 100 stains.
> Comprehensive evaluation across public and internal benchmarks demonstrates
> that PLUTO-4 achieves state-of-the-art performance on tasks requiring varying
> spatial and biological context, including patch-level classification,
> segmentation, and slide-level diagnosis. The compact PLUTO-4S provides
> high-throughput and robust performance for practical deployment, while PLUTO-4G
> establishes new performance frontiers across multiple pathology benchmarks,
> including an 11% improvement in dermatopathology diagnosis. These diverse
> improvements underscore PLUTO-4's potential to transform real-world
> applications as a backbone for translational research and diagnostic use cases.

