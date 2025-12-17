---
layout: default
title: SENCA-st: Integrating Spatial Transcriptomics and Histopathology with Cross Attention Shared Encoder for Region Identification in Cancer Pathology
---

# SENCA-st: Integrating Spatial Transcriptomics and Histopathology with Cross Attention Shared Encoder for Region Identification in Cancer Pathology

**arXiv**: [2511.08573v1](https://arxiv.org/abs/2511.08573) | [PDF](https://arxiv.org/pdf/2511.08573.pdf)

**作者**: Shanaka Liyanaarachchi, Chathurya Wijethunga, Shihab Aaquil Ahamed, Akthas Absar, Ranga Rodrigo

---

## 💡 一句话要点

**提出SENCA-st架构以整合空间转录组学与组织病理学，用于癌症病理区域识别**

**关键词**: `空间转录组学` `组织病理学` `交叉注意力` `肿瘤异质性` `区域识别`

## 📋 核心要点

1. 现有方法在整合空间转录组学与组织病理学时，易偏向一方导致信息丢失或噪声放大
2. 采用共享编码器与邻域交叉注意力机制，强调结构相似但功能不同的区域
3. 实验显示模型在检测肿瘤异质性和微环境区域方面优于现有方法

## 📄 摘要（原文）

> Spatial transcriptomics is an emerging field that enables the identification of functional regions based on the spatial distribution of gene expression. Integrating this functional information present in transcriptomic data with structural data from histopathology images is an active research area with applications in identifying tumor substructures associated with cancer drug resistance. Current histopathology-spatial-transcriptomic region segmentation methods suffer due to either making spatial transcriptomics prominent by using histopathology features just to assist processing spatial transcriptomics data or using vanilla contrastive learning that make histopathology images prominent due to only promoting common features losing functional information. In both extremes, the model gets either lost in the noise of spatial transcriptomics or overly smoothed, losing essential information. Thus, we propose our novel architecture SENCA-st (Shared Encoder with Neighborhood Cross Attention) that preserves the features of both modalities. More importantly, it emphasizes regions that are structurally similar in histopathology but functionally different on spatial transcriptomics using cross-attention. We demonstrate the superior performance of our model that surpasses state-of-the-art methods in detecting tumor heterogeneity and tumor micro-environment regions, a clinically crucial aspect.

