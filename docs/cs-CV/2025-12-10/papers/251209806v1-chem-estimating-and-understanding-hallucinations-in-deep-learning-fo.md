---
layout: default
title: CHEM: Estimating and Understanding Hallucinations in Deep Learning for Image Processing
---

# CHEM: Estimating and Understanding Hallucinations in Deep Learning for Image Processing

**arXiv**: [2512.09806v1](https://arxiv.org/abs/2512.09806) | [PDF](https://arxiv.org/pdf/2512.09806.pdf)

**作者**: Jianfei Li, Ines Rosellon-Inclan, Gitta Kutyniok, Jean-Luc Starck

---

## 💡 一句话要点

**提出CHEM方法以量化图像处理中的幻觉伪影，确保模型可信度**

**关键词**: `幻觉量化` `图像去卷积` `保形回归` `小波表示` `U形网络` `天文图像处理`

## 📋 核心要点

1. U-Net等U形架构在图像去卷积中易产生幻觉伪影，影响安全关键场景分析
2. CHEM利用小波和剪切波表示提取伪影，结合保形分位数回归进行无分布量化
3. 在CANDELS天文数据集上测试U-Net等模型，从近似理论角度探讨幻觉成因

## 📄 摘要（原文）

> U-Net and other U-shaped architectures have achieved significant success in image deconvolution tasks. However, challenges have emerged, as these methods might generate unrealistic artifacts or hallucinations, which can interfere with analysis in safety-critical scenarios. This paper introduces a novel approach for quantifying and comprehending hallucination artifacts to ensure trustworthy computer vision models. Our method, termed the Conformal Hallucination Estimation Metric (CHEM), is applicable to any image reconstruction model, enabling efficient identification and quantification of hallucination artifacts. It offers two key advantages: it leverages wavelet and shearlet representations to efficiently extract hallucinations of image features and uses conformalized quantile regression to assess hallucination levels in a distribution-free manner. Furthermore, from an approximation theoretical perspective, we explore the reasons why U-shaped networks are prone to hallucinations. We test the proposed approach on the CANDELS astronomical image dataset with models such as U-Net, SwinUNet, and Learnlets, and provide new perspectives on hallucination from different aspects in deep learning-based image processing.

