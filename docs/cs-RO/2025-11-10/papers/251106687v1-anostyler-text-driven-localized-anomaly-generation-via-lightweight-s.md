---
layout: default
title: AnoStyler: Text-Driven Localized Anomaly Generation via Lightweight Style Transfer
---

# AnoStyler: Text-Driven Localized Anomaly Generation via Lightweight Style Transfer

**arXiv**: [2511.06687v1](https://arxiv.org/abs/2511.06687) | [PDF](https://arxiv.org/pdf/2511.06687.pdf)

**作者**: Yulim So, Seokho Kang

---

## 💡 一句话要点

**提出AnoStyler以解决零样本异常生成中视觉真实性和资源依赖问题**

**关键词**: `异常生成` `风格迁移` `零样本学习` `轻量模型` `文本引导` `局部异常`

## 📋 核心要点

1. 现有异常生成方法存在视觉不真实、依赖大量真实图像或模型笨重的问题
2. 使用文本引导风格迁移，基于单张正常图像和文本提示生成局部异常
3. 在MVTec-AD和VisA数据集上验证，生成高质量异常图像并提升检测性能

## 📄 摘要（原文）

> Anomaly generation has been widely explored to address the scarcity of
> anomaly images in real-world data. However, existing methods typically suffer
> from at least one of the following limitations, hindering their practical
> deployment: (1) lack of visual realism in generated anomalies; (2) dependence
> on large amounts of real images; and (3) use of memory-intensive, heavyweight
> model architectures. To overcome these limitations, we propose AnoStyler, a
> lightweight yet effective method that frames zero-shot anomaly generation as
> text-guided style transfer. Given a single normal image along with its category
> label and expected defect type, an anomaly mask indicating the localized
> anomaly regions and two-class text prompts representing the normal and anomaly
> states are generated using generalizable category-agnostic procedures. A
> lightweight U-Net model trained with CLIP-based loss functions is used to
> stylize the normal image into a visually realistic anomaly image, where
> anomalies are localized by the anomaly mask and semantically aligned with the
> text prompts. Extensive experiments on the MVTec-AD and VisA datasets show that
> AnoStyler outperforms existing anomaly generation methods in generating
> high-quality and diverse anomaly images. Furthermore, using these generated
> anomalies helps enhance anomaly detection performance.

