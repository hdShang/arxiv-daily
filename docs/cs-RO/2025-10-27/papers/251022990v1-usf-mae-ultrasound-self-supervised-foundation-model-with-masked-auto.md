---
layout: default
title: USF-MAE: Ultrasound Self-Supervised Foundation Model with Masked Autoencoding
---

# USF-MAE: Ultrasound Self-Supervised Foundation Model with Masked Autoencoding

**arXiv**: [2510.22990v1](https://arxiv.org/abs/2510.22990) | [PDF](https://arxiv.org/pdf/2510.22990.pdf)

**作者**: Youssef Megahed, Robin Ducharme, Mark Walker, Steven Hawken, Adrian D. C. Chan

---

## 💡 一句话要点

**提出USF-MAE自监督基础模型，通过掩码自编码解决超声图像标注稀缺问题。**

**关键词**: `超声图像分析` `自监督学习` `掩码自编码` `视觉变换器` `医学影像分类`

## 📋 核心要点

1. 超声图像解释困难，因噪声高、操作依赖性强，导致观察者间差异大。
2. 使用ViT架构，在37万超声图像上预训练，通过重建掩码补丁学习模态特定表示。
3. 在三个分类任务中微调，F1分数达81.6%、79.6%和82.4%，优于基线模型。

## 📄 摘要（原文）

> Ultrasound imaging is one of the most widely used diagnostic modalities,
> offering real-time, radiation-free assessment across diverse clinical domains.
> However, interpretation of ultrasound images remains challenging due to high
> noise levels, operator dependence, and limited field of view, resulting in
> substantial inter-observer variability. Current Deep Learning approaches are
> hindered by the scarcity of large labeled datasets and the domain gap between
> general and sonographic images, which limits the transferability of models
> pretrained on non-medical data. To address these challenges, we introduce the
> Ultrasound Self-Supervised Foundation Model with Masked Autoencoding (USF-MAE),
> the first large-scale self-supervised MAE framework pretrained exclusively on
> ultrasound data. The model was pre-trained on 370,000 2D and 3D ultrasound
> images curated from 46 open-source datasets, collectively termed OpenUS-46,
> spanning over twenty anatomical regions. This curated dataset has been made
> publicly available to facilitate further research and reproducibility. Using a
> Vision Transformer encoder-decoder architecture, USF-MAE reconstructs masked
> image patches, enabling it to learn rich, modality-specific representations
> directly from unlabeled data. The pretrained encoder was fine-tuned on three
> public downstream classification benchmarks: BUS-BRA (breast cancer), MMOTU-2D
> (ovarian tumors), and GIST514-DB (gastrointestinal stromal tumors). Across all
> tasks, USF-MAE consistently outperformed conventional CNN and ViT baselines,
> achieving F1-scores of 81.6%, 79.6%, and 82.4%, respectively. Despite not using
> labels during pretraining, USF-MAE approached the performance of the supervised
> foundation model UltraSam on breast cancer classification and surpassed it on
> the other tasks, demonstrating strong cross-anatomical generalization.

