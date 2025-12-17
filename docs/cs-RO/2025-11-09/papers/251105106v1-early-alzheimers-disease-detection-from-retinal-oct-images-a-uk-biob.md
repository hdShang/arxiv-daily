---
layout: default
title: Early Alzheimer's Disease Detection from Retinal OCT Images: A UK Biobank Study
---

# Early Alzheimer's Disease Detection from Retinal OCT Images: A UK Biobank Study

**arXiv**: [2511.05106v1](https://arxiv.org/abs/2511.05106) | [PDF](https://arxiv.org/pdf/2511.05106.pdf)

**作者**: Yasemin Turkan, F. Boray Tek, M. Serdar Nazlı, Öykü Eren

---

## 💡 一句话要点

**提出基于视网膜OCT图像的深度学习模型，用于早期阿尔茨海默病检测。**

**关键词**: `阿尔茨海默病检测` `视网膜OCT图像` `深度学习分类` `数据增强` `UK Biobank数据集`

## 📋 核心要点

1. 核心问题：早期阿尔茨海默病检测挑战大，因影像早于临床诊断数年。
2. 方法要点：微调预训练模型，应用数据增强和年加权损失函数。
3. 实验或效果：ResNet-34在4年队列中AUC达0.62，低于临床应用阈值。

## 📄 摘要（原文）

> Alterations in retinal layer thickness, measurable using Optical Coherence
> Tomography (OCT), have been associated with neurodegenerative diseases such as
> Alzheimer's disease (AD). While previous studies have mainly focused on
> segmented layer thickness measurements, this study explored the direct
> classification of OCT B-scan images for the early detection of AD. To our
> knowledge, this is the first application of deep learning to raw OCT B-scans
> for AD prediction in the literature. Unlike conventional medical image
> classification tasks, early detection is more challenging than diagnosis
> because imaging precedes clinical diagnosis by several years. We fine-tuned and
> evaluated multiple pretrained models, including ImageNet-based networks and the
> OCT-specific RETFound transformer, using subject-level cross-validation
> datasets matched for age, sex, and imaging instances from the UK Biobank
> cohort. To reduce overfitting in this small, high-dimensional dataset, both
> standard and OCT-specific augmentation techniques were applied, along with a
> year-weighted loss function that prioritized cases diagnosed within four years
> of imaging. ResNet-34 produced the most stable results, achieving an AUC of
> 0.62 in the 4-year cohort. Although below the threshold for clinical
> application, our explainability analyses confirmed localized structural
> differences in the central macular subfield between the AD and control groups.
> These findings provide a baseline for OCT-based AD prediction, highlight the
> challenges of detecting subtle retinal biomarkers years before AD diagnosis,
> and point to the need for larger datasets and multimodal approaches.

