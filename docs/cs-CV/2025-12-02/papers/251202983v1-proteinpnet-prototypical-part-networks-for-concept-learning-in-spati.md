---
layout: default
title: ProteinPNet: Prototypical Part Networks for Concept Learning in Spatial Proteomics
---

# ProteinPNet: Prototypical Part Networks for Concept Learning in Spatial Proteomics

**arXiv**: [2512.02983v1](https://arxiv.org/abs/2512.02983) | [PDF](https://arxiv.org/pdf/2512.02983.pdf)

**作者**: Louis McConnell, Jieran Sun, Theo Maffei, Raphael Gottardo, Marianna Rapsomaniki

---

## 💡 一句话要点

**提出ProteinPNet原型部分网络，用于空间蛋白质组学中的概念学习，以发现肿瘤微环境空间模式。**

**关键词**: `空间蛋白质组学` `原型学习` `肿瘤微环境` `可解释人工智能` `概念学习` `空间模式发现`

## 📋 核心要点

1. 核心问题：理解肿瘤微环境空间架构对精准肿瘤学至关重要，需从空间蛋白质组学数据中识别可解释模式。
2. 方法要点：基于原型部分网络，通过监督训练直接学习判别性、可解释、忠实空间原型，无需后验解释模型。
3. 实验或效果：在合成和真实肺癌数据集上验证，原型与肿瘤亚型对齐，捕获免疫浸润和组织模块性差异特征。

## 📄 摘要（原文）

> Understanding the spatial architecture of the tumor microenvironment (TME) is critical to advance precision oncology. We present ProteinPNet, a novel framework based on prototypical part networks that discovers TME motifs from spatial proteomics data. Unlike traditional post-hoc explanability models, ProteinPNet directly learns discriminative, interpretable, faithful spatial prototypes through supervised training. We validate our approach on synthetic datasets with ground truth motifs, and further test it on a real-world lung cancer spatial proteomics dataset. ProteinPNet consistently identifies biologically meaningful prototypes aligned with different tumor subtypes. Through graphical and morphological analyses, we show that these prototypes capture interpretable features pointing to differences in immune infiltration and tissue modularity. Our results highlight the potential of prototype-based learning to reveal interpretable spatial biomarkers within the TME, with implications for mechanistic discovery in spatial omics.

