---
layout: default
title: LungEvaty: A Scalable, Open-Source Transformer-based Deep Learning Model for Lung Cancer Risk Prediction in LDCT Screening
---

# LungEvaty: A Scalable, Open-Source Transformer-based Deep Learning Model for Lung Cancer Risk Prediction in LDCT Screening

**arXiv**: [2511.20116v1](https://arxiv.org/abs/2511.20116) | [PDF](https://arxiv.org/pdf/2511.20116.pdf)

**作者**: Johannes Brandt, Maulik Chevli, Rickmer Braren, Georgios Kaissis, Philip Müller, Daniel Rueckert

---

## 💡 一句话要点

**提出LungEvaty基于Transformer的深度学习模型，用于LDCT筛查中的肺癌风险预测**

**关键词**: `肺癌风险预测` `Transformer模型` `低剂量CT筛查` `全肺分析` `开源框架`

## 📋 核心要点

1. 核心问题：LDCT筛查中肺癌风险预测需可扩展方法，现有方法依赖像素注释或片段分析限制性能
2. 方法要点：使用全肺输入Transformer框架，无需区域监督，可选AIAG损失增强解剖注意力
3. 实验或效果：在超9万CT扫描上训练，匹配SOTA性能，提供开源可扩展解决方案

## 📄 摘要（原文）

> Lung cancer risk estimation is gaining increasing importance as more countries introduce population-wide screening programs using low-dose CT (LDCT). As imaging volumes grow, scalable methods that can process entire lung volumes efficiently are essential to tap into the full potential of these large screening datasets. Existing approaches either over-rely on pixel-level annotations, limiting scalability, or analyze the lung in fragments, weakening performance. We present LungEvaty, a fully transformer-based framework for predicting 1-6 year lung cancer risk from a single LDCT scan. The model operates on whole-lung inputs, learning directly from large-scale screening data to capture comprehensive anatomical and pathological cues relevant for malignancy risk. Using only imaging data and no region supervision, LungEvaty matches state-of-the-art performance, refinable by an optional Anatomically Informed Attention Guidance (AIAG) loss that encourages anatomically focused attention. In total, LungEvaty was trained on more than 90,000 CT scans, including over 28,000 for fine-tuning and 6,000 for evaluation. The framework offers a simple, data-efficient, and fully open-source solution that provides an extensible foundation for future research in longitudinal and multimodal lung cancer risk prediction.

