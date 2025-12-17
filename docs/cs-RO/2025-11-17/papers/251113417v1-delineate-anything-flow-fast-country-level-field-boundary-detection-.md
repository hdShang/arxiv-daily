---
layout: default
title: Delineate Anything Flow: Fast, Country-Level Field Boundary Detection from Any Source
---

# Delineate Anything Flow: Fast, Country-Level Field Boundary Detection from Any Source

**arXiv**: [2511.13417v1](https://arxiv.org/abs/2511.13417) | [PDF](https://arxiv.org/pdf/2511.13417.pdf)

**作者**: Mykola Lavreniuk, Nataliia Kussul, Andrii Shelestov, Yevhenii Salii, Volodymyr Kuzin, Sergii Skakun, Zoltan Szantoi

---

## 💡 一句话要点

**提出Delineate Anything Flow方法，用于快速、大规模农业田块边界检测**

**关键词**: `实例分割` `农业遥感` `边界检测` `大规模数据集` `零样本泛化` `矢量边界`

## 📋 核心要点

1. 现有方法常产生不完整边界、合并相邻田块，且难以扩展。
2. 结合DelAny实例分割模型与结构化后处理，生成拓扑一致矢量边界。
3. 在乌克兰应用中，6小时内完成全国边界检测，精度和速度显著提升。

## 📄 摘要（原文）

> Accurate delineation of agricultural field boundaries from satellite imagery is essential for land management and crop monitoring, yet existing methods often produce incomplete boundaries, merge adjacent fields, and struggle to scale. We present the Delineate Anything Flow (DelAnyFlow) methodology, a resolution-agnostic approach for large-scale field boundary mapping. DelAnyFlow combines the DelAny instance segmentation model, based on a YOLOv11 backbone and trained on the large-scale Field Boundary Instance Segmentation-22M (FBIS 22M) dataset, with a structured post-processing, merging, and vectorization sequence to generate topologically consistent vector boundaries. FBIS 22M, the largest dataset of its kind, contains 672,909 multi-resolution image patches (0.25-10m) and 22.9million validated field instances. The DelAny model delivers state-of-the-art accuracy with over 100% higher mAP and 400x faster inference than SAM2. DelAny demonstrates strong zero-shot generalization and supports national-scale applications: using Sentinel 2 data for 2024, DelAnyFlow generated a complete field boundary layer for Ukraine (603,000km2) in under six hours on a single workstation. DelAnyFlow outputs significantly improve boundary completeness relative to operational products from Sinergise Solutions and NASA Harvest, particularly in smallholder and fragmented systems (0.25-1ha). For Ukraine, DelAnyFlow delineated 3.75M fields at 5m and 5.15M at 2.5m, compared to 2.66M detected by Sinergise Solutions and 1.69M by NASA Harvest. This work delivers a scalable, cost-effective methodology for field delineation in regions lacking digital cadastral data. A project landing page with links to model weights, code, national-scale vector outputs, and dataset is available at https://lavreniuk.github.io/Delineate-Anything/.

