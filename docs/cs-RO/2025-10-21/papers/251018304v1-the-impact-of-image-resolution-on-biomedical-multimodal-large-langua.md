---
layout: default
title: The Impact of Image Resolution on Biomedical Multimodal Large Language Models
---

# The Impact of Image Resolution on Biomedical Multimodal Large Language Models

**arXiv**: [2510.18304v1](https://arxiv.org/abs/2510.18304) | [PDF](https://arxiv.org/pdf/2510.18304.pdf)

**作者**: Liangyu Chen, James Burgess, Jeffrey J Nirschl, Orr Zohar, Serena Yeung-Levy

---

## 💡 一句话要点

**研究图像分辨率对生物医学多模态大语言模型性能的影响，提出原生分辨率训练与混合分辨率策略**

**关键词**: `图像分辨率` `多模态大语言模型` `生物医学图像分析` `混合分辨率训练` `原生分辨率推理`

## 📋 核心要点

1. 核心问题：生物医学图像分析中，多模态大语言模型常处理低分辨率图像，导致关键信息丢失。
2. 方法要点：采用原生分辨率训练和推理，并引入混合分辨率训练以缓解分辨率不匹配问题。
3. 实验或效果：原生分辨率显著提升性能，分辨率不匹配严重降低性能，混合训练平衡计算与性能。

## 📄 摘要（原文）

> Imaging technologies are fundamental to biomedical research and modern
> medicine, requiring analysis of high-resolution images across various
> modalities. While multimodal large language models (MLLMs) show promise for
> biomedical image analysis, most are designed for low-resolution images from
> general-purpose datasets, risking critical information loss. We investigate how
> image resolution affects MLLM performance in biomedical applications and
> demonstrate that: (1) native-resolution training and inference significantly
> improve performance across multiple tasks, (2) misalignment between training
> and inference resolutions severely degrades performance, and (3)
> mixed-resolution training effectively mitigates misalignment and balances
> computational constraints with performance requirements. Based on these
> findings, we recommend prioritizing native-resolution inference and
> mixed-resolution datasets to optimize biomedical MLLMs for transformative
> impact in scientific research and clinical applications.

