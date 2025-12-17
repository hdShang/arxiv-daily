---
layout: default
title: SSDLabeler: Realistic semi-synthetic data generation for multi-label artifact classification in EEG
---

# SSDLabeler: Realistic semi-synthetic data generation for multi-label artifact classification in EEG

**arXiv**: [2512.05500v1](https://arxiv.org/abs/2512.05500) | [PDF](https://arxiv.org/pdf/2512.05500.pdf)

**作者**: Taketo Akama, Akima Connelly, Shun Minamikawa, Natalia Polouliakh

---

## 💡 一句话要点

**提出SSDLabeler框架以生成逼真的半合成数据，用于EEG多标签伪迹分类。**

**关键词**: `脑电图伪迹分类` `半合成数据生成` `独立成分分析` `多标签学习` `信号处理`

## 📋 核心要点

1. 核心问题：EEG伪迹分类受限于手动标注数据，无法覆盖真实EEG的多样性和复杂性。
2. 方法要点：通过ICA分解、RMS和PSD标准验证伪迹，并重新注入多种伪迹类型到干净数据中。
3. 实验或效果：相比先前方法，在原始EEG上训练的分类器准确性提高，支持伪迹共现和复杂性的处理。

## 📄 摘要（原文）

> EEG recordings are inherently contaminated by artifacts such as ocular, muscular, and environmental noise, which obscure neural activity and complicate preprocessing. Artifact classification offers advantages in stability and transparency, providing a viable alternative to ICA-based methods that enable flexible use alongside human inspections and across various applications. However, artifact classification is limited by its training data as it requires extensive manual labeling, which cannot fully cover the diversity of real-world EEG. Semi-synthetic data (SSD) methods have been proposed to address this limitation, but prior approaches typically injected single artifact types using ICA components or required separately recorded artifact signals, reducing both the realism of the generated data and the applicability of the method. To overcome these issues, we introduce SSDLabeler, a framework that generates realistic, annotated SSDs by decomposing real EEG with ICA, epoch-level artifact verification using RMS and PSD criteria, and reinjecting multiple artifact types into clean data. When applied to train a multi-label artifact classifier, it improved accuracy on raw EEG across diverse conditions compared to prior SSD and raw EEG training, establishing a scalable foundation for artifact handling that captures the co-occurrence and complexity of real EEG.

