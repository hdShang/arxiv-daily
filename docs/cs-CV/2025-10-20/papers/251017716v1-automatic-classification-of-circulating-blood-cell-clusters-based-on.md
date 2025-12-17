---
layout: default
title: Automatic Classification of Circulating Blood Cell Clusters based on Multi-channel Flow Cytometry Imaging
---

# Automatic Classification of Circulating Blood Cell Clusters based on Multi-channel Flow Cytometry Imaging

**arXiv**: [2510.17716v1](https://arxiv.org/abs/2510.17716) | [PDF](https://arxiv.org/pdf/2510.17716.pdf)

**作者**: Suqiang Ma, Subhadeep Sengupta, Yao Lee, Beikang Gu, Xianyan Chen, Xianqiao Wang, Yang Liu, Mengjia Xu, Galit H. Frydman, He Li

---

## 💡 一句话要点

**提出基于多通道流式细胞术成像的循环血细胞簇自动分类框架**

**关键词**: `循环血细胞簇` `多通道流式细胞术` `YOLOv11模型` `细胞类型识别` `图像分类` `荧光染色`

## 📋 核心要点

1. 核心问题：循环血细胞簇自动分析工具缺乏，其不规则形状和异质细胞类型增加识别难度
2. 方法要点：采用两步策略，先微调YOLOv11模型分类图像，再叠加轮廓与荧光区域识别细胞类型
3. 实验或效果：在簇分类和表型识别中准确率超过95%，有效处理细胞碎片和染色伪影

## 📄 摘要（原文）

> Circulating blood cell clusters (CCCs) containing red blood cells (RBCs),
> white blood cells(WBCs), and platelets are significant biomarkers linked to
> conditions like thrombosis, infection, and inflammation. Flow cytometry, paired
> with fluorescence staining, is commonly used to analyze these cell clusters,
> revealing cell morphology and protein profiles. While computational approaches
> based on machine learning have advanced the automatic analysis of single-cell
> flow cytometry images, there is a lack of effort to build tools to
> automatically analyze images containing CCCs. Unlike single cells, cell
> clusters often exhibit irregular shapes and sizes. In addition, these cell
> clusters often consist of heterogeneous cell types, which require multi-channel
> staining to identify the specific cell types within the clusters. This study
> introduces a new computational framework for analyzing CCC images and
> identifying cell types within clusters. Our framework uses a two-step analysis
> strategy. First, it categorizes images into cell cluster and non-cluster groups
> by fine-tuning the You Only Look Once(YOLOv11) model, which outperforms
> traditional convolutional neural networks (CNNs), Vision Transformers (ViT).
> Then, it identifies cell types by overlaying cluster contours with regions from
> multi-channel fluorescence stains, enhancing accuracy despite cell debris and
> staining artifacts. This approach achieved over 95% accuracy in both cluster
> classification and phenotype identification. In summary, our automated
> framework effectively analyzes CCC images from flow cytometry, leveraging both
> bright-field and fluorescence data. Initially tested on blood cells, it holds
> potential for broader applications, such as analyzing immune and tumor cell
> clusters, supporting cellular research across various diseases.

