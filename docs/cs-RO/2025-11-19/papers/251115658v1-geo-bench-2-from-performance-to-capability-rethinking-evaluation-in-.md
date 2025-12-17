---
layout: default
title: GEO-Bench-2: From Performance to Capability, Rethinking Evaluation in Geospatial AI
---

# GEO-Bench-2: From Performance to Capability, Rethinking Evaluation in Geospatial AI

**arXiv**: [2511.15658v1](https://arxiv.org/abs/2511.15658) | [PDF](https://arxiv.org/pdf/2511.15658.pdf)

**作者**: Naomi Simumba, Nils Lehmann, Paolo Fraccaro, Hamed Alemohammad, Geeth De Mel, Salman Khan, Manil Maskey, Nicolas Longepe, Xiao Xiang Zhu, Hannah Kerner, Juan Bernabe-Moreno, Alexander Lacoste

---

## 💡 一句话要点

**提出GEO-Bench-2评估框架以解决地理空间AI中标准化评估缺失问题**

**关键词**: `地理空间基础模型` `标准化评估` `多任务基准` `能力分组` `模型比较` `地球观测`

## 📋 核心要点

1. 核心问题：地理空间基础模型缺乏统一评估标准，影响公平比较和方法创新。
2. 方法要点：引入能力分组和灵活评估协议，覆盖多任务和多数据集。
3. 实验或效果：实验显示无单一模型主导所有任务，强调任务特定模型选择。

## 📄 摘要（原文）

> Geospatial Foundation Models (GeoFMs) are transforming Earth Observation (EO), but evaluation lacks standardized protocols. GEO-Bench-2 addresses this with a comprehensive framework spanning classification, segmentation, regression, object detection, and instance segmentation across 19 permissively-licensed datasets. We introduce ''capability'' groups to rank models on datasets that share common characteristics (e.g., resolution, bands, temporality). This enables users to identify which models excel in each capability and determine which areas need improvement in future work. To support both fair comparison and methodological innovation, we define a prescriptive yet flexible evaluation protocol. This not only ensures consistency in benchmarking but also facilitates research into model adaptation strategies, a key and open challenge in advancing GeoFMs for downstream tasks.
>   Our experiments show that no single model dominates across all tasks, confirming the specificity of the choices made during architecture design and pretraining. While models pretrained on natural images (ConvNext ImageNet, DINO V3) excel on high-resolution tasks, EO-specific models (TerraMind, Prithvi, and Clay) outperform them on multispectral applications such as agriculture and disaster response. These findings demonstrate that optimal model choice depends on task requirements, data modalities, and constraints. This shows that the goal of a single GeoFM model that performs well across all tasks remains open for future research. GEO-Bench-2 enables informed, reproducible GeoFM evaluation tailored to specific use cases. Code, data, and leaderboard for GEO-Bench-2 are publicly released under a permissive license.

