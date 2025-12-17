---
layout: default
title: Non-Aligned Reference Image Quality Assessment for Novel View Synthesis
---

# Non-Aligned Reference Image Quality Assessment for Novel View Synthesis

**arXiv**: [2511.08155v1](https://arxiv.org/abs/2511.08155) | [PDF](https://arxiv.org/pdf/2511.08155.pdf)

**作者**: Abhijay Ghildyal, Rajesh Sureddi, Nabajeet Barman, Saman Zadtootaghaj, Alan Bovik

---

## 💡 一句话要点

**提出非对齐参考图像质量评估框架以解决新视角合成中的质量评估挑战**

**关键词**: `新视角合成` `图像质量评估` `非对齐参考` `对比学习` `DINOv2嵌入` `合成失真数据`

## 📋 核心要点

1. 核心问题：新视角合成图像在缺乏像素对齐参考时，现有全参考和无参考方法评估效果不佳
2. 方法要点：基于对比学习框架，结合LoRA增强的DINOv2嵌入，使用合成失真数据进行训练
3. 实验或效果：模型在多种参考条件下优于现有方法，并通过用户研究验证与主观评分强相关

## 📄 摘要（原文）

> Evaluating the perceptual quality of Novel View Synthesis (NVS) images remains a key challenge, particularly in the absence of pixel-aligned ground truth references. Full-Reference Image Quality Assessment (FR-IQA) methods fail under misalignment, while No-Reference (NR-IQA) methods struggle with generalization. In this work, we introduce a Non-Aligned Reference (NAR-IQA) framework tailored for NVS, where it is assumed that the reference view shares partial scene content but lacks pixel-level alignment. We constructed a large-scale image dataset containing synthetic distortions targeting Temporal Regions of Interest (TROI) to train our NAR-IQA model. Our model is built on a contrastive learning framework that incorporates LoRA-enhanced DINOv2 embeddings and is guided by supervision from existing IQA methods. We train exclusively on synthetically generated distortions, deliberately avoiding overfitting to specific real NVS samples and thereby enhancing the model's generalization capability. Our model outperforms state-of-the-art FR-IQA, NR-IQA, and NAR-IQA methods, achieving robust performance on both aligned and non-aligned references. We also conducted a novel user study to gather data on human preferences when viewing non-aligned references in NVS. We find strong correlation between our proposed quality prediction model and the collected subjective ratings. For dataset and code, please visit our project page: https://stootaghaj.github.io/nova-project/

