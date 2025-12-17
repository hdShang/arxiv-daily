---
layout: default
title: mViSE: A Visual Search Engine for Analyzing Multiplex IHC Brain Tissue Images
---

# mViSE: A Visual Search Engine for Analyzing Multiplex IHC Brain Tissue Images

**arXiv**: [2512.11745v1](https://arxiv.org/abs/2512.11745) | [PDF](https://arxiv.org/pdf/2512.11745.pdf)

**作者**: Liqiang Huang, Rachel W. Mills, Saikiran Mandula, Lin Bai, Mahtab Jeyhani, John Redell, Hien Van Nguyen, Saurabh Prasad, Dragan Maric, Badrinath Roysam

---

## 💡 一句话要点

**提出mViSE视觉搜索引擎以分析脑组织多重免疫组化图像，无需编程实现查询驱动分析。**

**关键词**: `脑组织图像分析` `多重免疫组化` `视觉搜索引擎` `自监督学习` `信息论检索` `QuPath插件`

## 📋 核心要点

1. 核心问题：脑组织全切片多重成像产生信息密集图像，分析困难且需定制软件。
2. 方法要点：采用分治策略组织数据，结合自监督学习训练多重编码器，支持信息论方法检索相似细胞群落。
3. 实验或效果：验证了检索单细胞、组织区域及划分皮层和脑区的能力，提供开源QuPath插件。

## 📄 摘要（原文）

> Whole-slide multiplex imaging of brain tissue generates massive information-dense images that are challenging to analyze and require custom software. We present an alternative query-driven programming-free strategy using a multiplex visual search engine (mViSE) that learns the multifaceted brain tissue chemoarchitecture, cytoarchitecture, and myeloarchitecture. Our divide-and-conquer strategy organizes the data into panels of related molecular markers and uses self-supervised learning to train a multiplex encoder for each panel with explicit visual confirmation of successful learning. Multiple panels can be combined to process visual queries for retrieving similar communities of individual cells or multicellular niches using information-theoretic methods. The retrievals can be used for diverse purposes including tissue exploration, delineating brain regions and cortical cell layers, profiling and comparing brain regions without computer programming. We validated mViSE's ability to retrieve single cells, proximal cell pairs, tissue patches, delineate cortical layers, brain regions and sub-regions. mViSE is provided as an open-source QuPath plug-in.

