---
layout: default
title: THIR: Topological Histopathological Image Retrieval
---

# THIR: Topological Histopathological Image Retrieval

**arXiv**: [2511.13170v1](https://arxiv.org/abs/2511.13170) | [PDF](https://arxiv.org/pdf/2511.13170.pdf)

**作者**: Zahra Tabatabaei, Jon Sporring

---

## 💡 一句话要点

**提出THIR框架，利用拓扑数据分析实现无监督组织病理图像检索。**

**关键词**: `拓扑数据分析` `图像检索` `无监督学习` `组织病理学` `持久同调`

## 📋 核心要点

1. 核心问题：乳腺癌诊断依赖准确图像检索，但传统方法需大量标注数据和GPU资源。
2. 方法要点：基于Betti数和持久同调提取拓扑特征，实现无监督图像相似性匹配。
3. 实验或效果：在BreaKHis数据集上优于现有方法，CPU处理全数据集不足20分钟。

## 📄 摘要（原文）

> According to the World Health Organization, breast cancer claimed the lives of approximately 685,000 women in 2020. Early diagnosis and accurate clinical decision making are critical in reducing this global burden. In this study, we propose THIR, a novel Content-Based Medical Image Retrieval (CBMIR) framework that leverages topological data analysis specifically, Betti numbers derived from persistent homology to characterize and retrieve histopathological images based on their intrinsic structural patterns. Unlike conventional deep learning approaches that rely on extensive training, annotated datasets, and powerful GPU resources, THIR operates entirely without supervision. It extracts topological fingerprints directly from RGB histopathological images using cubical persistence, encoding the evolution of loops as compact, interpretable feature vectors. The similarity retrieval is then performed by computing the distances between these topological descriptors, efficiently returning the top-K most relevant matches.
>   Extensive experiments on the BreaKHis dataset demonstrate that THIR outperforms state of the art supervised and unsupervised methods. It processes the entire dataset in under 20 minutes on a standard CPU, offering a fast, scalable, and training free solution for clinical image retrieval.

