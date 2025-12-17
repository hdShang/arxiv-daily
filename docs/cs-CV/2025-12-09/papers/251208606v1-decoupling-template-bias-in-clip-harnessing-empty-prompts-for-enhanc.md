---
layout: default
title: Decoupling Template Bias in CLIP: Harnessing Empty Prompts for Enhanced Few-Shot Learning
---

# Decoupling Template Bias in CLIP: Harnessing Empty Prompts for Enhanced Few-Shot Learning

**arXiv**: [2512.08606v1](https://arxiv.org/abs/2512.08606) | [PDF](https://arxiv.org/pdf/2512.08606.pdf)

**作者**: Zhenyu Zhang, Guangyao Chen, Yixiong Zou, Zhimeng Huang, Yuhua Li

---

## 💡 一句话要点

**提出使用空提示框架以解决CLIP中模板-样本相似性偏差，提升少样本学习性能。**

**关键词**: `CLIP模型` `少样本学习` `模板偏差` `空提示` `对比学习` `分类鲁棒性`

## 📋 核心要点

1. 核心问题：CLIP中模板-样本相似性导致模型依赖模板而非真实类别对齐，降低分类准确性和鲁棒性。
2. 方法要点：引入空提示捕获无偏模板特征，通过预训练和少样本微调两阶段框架校准偏差。
3. 实验或效果：在多个基准测试中显著减少性能波动，提高分类准确率和鲁棒性。

## 📄 摘要（原文）

> The Contrastive Language-Image Pre-Training (CLIP) model excels in few-shot learning by aligning visual and textual representations. Our study shows that template-sample similarity (TSS), defined as the resemblance between a text template and an image sample, introduces bias. This bias leads the model to rely on template proximity rather than true sample-to-category alignment, reducing both accuracy and robustness in classification. We present a framework that uses empty prompts, textual inputs that convey the idea of "emptiness" without category information. These prompts capture unbiased template features and offset TSS bias. The framework employs two stages. During pre-training, empty prompts reveal and reduce template-induced bias within the CLIP encoder. During few-shot fine-tuning, a bias calibration loss enforces correct alignment between images and their categories, ensuring the model focuses on relevant visual cues. Experiments across multiple benchmarks demonstrate that our template correction method significantly reduces performance fluctuations caused by TSS, yielding higher classification accuracy and stronger robustness. The repository of this project is available at https://github.com/zhenyuZ-HUST/Decoupling-Template-Bias-in-CLIP.

