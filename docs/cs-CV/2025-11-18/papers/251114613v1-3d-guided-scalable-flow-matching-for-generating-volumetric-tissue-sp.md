---
layout: default
title: 3D-Guided Scalable Flow Matching for Generating Volumetric Tissue Spatial Transcriptomics from Serial Histology
---

# 3D-Guided Scalable Flow Matching for Generating Volumetric Tissue Spatial Transcriptomics from Serial Histology

**arXiv**: [2511.14613v1](https://arxiv.org/abs/2511.14613) | [PDF](https://arxiv.org/pdf/2511.14613.pdf)

**作者**: Mohammad Vali Sanian, Arshia Hemmat, Amirhossein Vahidi, Jonas Maaskola, Jimmy Tsz Hang Lee, Stanislaw Makarchuk, Yeliz Demirci, Nana-Jane Chipampe, Omer Bayraktar, Lassi Paavolainen, Mohammad Lotfollahi

---

## 💡 一句话要点

**提出HoloTea框架，通过3D引导流匹配从组织学图像生成体积空间转录组学数据**

**关键词**: `空间转录组学` `流匹配` `3D组织建模` `ControlNet` `基因表达预测`

## 📋 核心要点

1. 核心问题：现有方法忽略3D结构或无法生成可扩展的体积空间转录组学数据
2. 方法要点：使用相邻切片信息融合到ControlNet中，结合ZINB先验和空间经验先验进行流匹配
3. 实验或效果：在多个数据集上优于2D和3D基线，提高3D表达准确性和泛化能力

## 📄 摘要（原文）

> A scalable and robust 3D tissue transcriptomics profile can enable a holistic understanding of tissue organization and provide deeper insights into human biology and disease. Most predictive algorithms that infer ST directly from histology treat each section independently and ignore 3D structure, while existing 3D-aware approaches are not generative and do not scale well. We present Holographic Tissue Expression Inpainting and Analysis (HoloTea), a 3D-aware flow-matching framework that imputes spot-level gene expression from H&E while explicitly using information from adjacent sections. Our key idea is to retrieve morphologically corresponding spots on neighboring slides in a shared feature space and fuse this cross section context into a lightweight ControlNet, allowing conditioning to follow anatomical continuity. To better capture the count nature of the data, we introduce a 3D-consistent prior for flow matching that combines a learned zero-inflated negative binomial (ZINB) prior with a spatial-empirical prior constructed from neighboring sections. A global attention block introduces 3D H&E scaling linearly with the number of spots in the slide, enabling training and inference on large 3D ST datasets. Across three spatial transcriptomics datasets spanning different tissue types and resolutions, HoloTea consistently improves 3D expression accuracy and generalization compared to 2D and 3D baselines. We envision HoloTea advancing the creation of accurate 3D virtual tissues, ultimately accelerating biomarker discovery and deepening our understanding of disease.

