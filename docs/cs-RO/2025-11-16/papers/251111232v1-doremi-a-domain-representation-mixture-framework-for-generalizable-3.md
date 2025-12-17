---
layout: default
title: DoReMi: A Domain-Representation Mixture Framework for Generalizable 3D Understanding
---

# DoReMi: A Domain-Representation Mixture Framework for Generalizable 3D Understanding

**arXiv**: [2511.11232v1](https://arxiv.org/abs/2511.11232) | [PDF](https://arxiv.org/pdf/2511.11232.pdf)

**作者**: Mingwei Xing, Xinliang Wang, Yifeng Shi

---

## 💡 一句话要点

**提出DoReMi框架以解决多源点云泛化问题**

**关键词**: `3D点云理解` `多域泛化` `混合专家框架` `动态路由` `自监督学习`

## 📋 核心要点

1. 核心问题：多源点云密度和噪声差异导致负迁移，限制3D模型泛化。
2. 方法要点：混合专家框架结合领域感知和统一表示分支，动态路由优化专家利用。
3. 实验效果：在ScanNet和S3DIS基准上达到80.1%和77.2% mIoU，性能优越。

## 📄 摘要（原文）

> The generalization of 3D deep learning across multiple domains remains limited by the limited scale of existing datasets and the high heterogeneity of multi-source point clouds. Point clouds collected from different sensors (e.g., LiDAR scans and mesh-derived point clouds) exhibit substantial discrepancies in density and noise distribution, resulting in negative transfer during multi-domain fusion. Most existing approaches focus exclusively on either domain-aware or domain-general features, overlooking the potential synergy between them. To address this, we propose DoReMi (Domain-Representation Mixture), a Mixture-of-Experts (MoE) framework that jointly models Domain-aware Experts branch and a unified Representation branch to enable cooperative learning between specialized and generalizable knowledge. DoReMi dynamically activates domain-aware expert branch via Domain-Guided Spatial Routing (DSR) for context-aware expert selection and employs Entropy-Controlled Dynamic Allocation (EDA) for stable and efficient expert utilization, thereby adaptively modeling diverse domain distributions. Complemented by a frozen unified representation branch pretrained through robust multi-attribute self-supervised learning, DoReMi preserves cross-domain geometric and structural priors while maintaining global consistency. We evaluate DoReMi across multiple 3D understanding benchmarks. Notably, DoReMi achieves 80.1% mIoU on ScanNet Val and 77.2% mIoU on S3DIS, demonstrating competitive or superior performance compared to existing approaches, and showing strong potential as a foundation framework for future 3D understanding research. The code will be released soon.

