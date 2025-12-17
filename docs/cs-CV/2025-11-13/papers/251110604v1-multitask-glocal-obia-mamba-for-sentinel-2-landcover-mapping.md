---
layout: default
title: Multitask GLocal OBIA-Mamba for Sentinel-2 Landcover Mapping
---

# Multitask GLocal OBIA-Mamba for Sentinel-2 Landcover Mapping

**arXiv**: [2511.10604v1](https://arxiv.org/abs/2511.10604) | [PDF](https://arxiv.org/pdf/2511.10604.pdf)

**作者**: Zack Dewis, Yimin Zhu, Zhengsen Xu, Mabel Heffring, Saeid Taleghanidoozdoozan, Kaylee Xiao, Motasem Alkayid, Lincoln Linlin Xu

---

## 💡 一句话要点

**提出多任务全局-局部OBIA-Mamba模型以增强Sentinel-2土地覆盖分类**

**关键词**: `土地覆盖分类` `多任务学习` `Mamba模型` `对象图像分析` `全局-局部架构` `Sentinel-2影像`

## 📋 核心要点

1. Sentinel-2土地覆盖分类面临空间异质性和上下文信息等数据挑战
2. 设计OBIA-Mamba模型使用超像素作为Mamba令牌，减少冗余计算并保留细节
3. 在加拿大阿尔伯塔测试，相比先进方法，分类精度更高、细节更精细

## 📄 摘要（原文）

> Although Sentinel-2 based land use and land cover (LULC) classification is critical for various environmental monitoring applications, it is a very difficult task due to some key data challenges (e.g., spatial heterogeneity, context information, signature ambiguity). This paper presents a novel Multitask Glocal OBIA-Mamba (MSOM) for enhanced Sentinel-2 classification with the following contributions. First, an object-based image analysis (OBIA) Mamba model (OBIA-Mamba) is designed to reduce redundant computation without compromising fine-grained details by using superpixels as Mamba tokens. Second, a global-local (GLocal) dual-branch convolutional neural network (CNN)-mamba architecture is designed to jointly model local spatial detail and global contextual information. Third, a multitask optimization framework is designed to employ dual loss functions to balance local precision with global consistency. The proposed approach is tested on Sentinel-2 imagery in Alberta, Canada, in comparison with several advanced classification approaches, and the results demonstrate that the proposed approach achieves higher classification accuracy and finer details that the other state-of-the-art methods.

