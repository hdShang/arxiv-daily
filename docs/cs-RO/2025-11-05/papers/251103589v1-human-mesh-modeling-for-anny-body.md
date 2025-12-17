---
layout: default
title: Human Mesh Modeling for Anny Body
---

# Human Mesh Modeling for Anny Body

**arXiv**: [2511.03589v1](https://arxiv.org/abs/2511.03589) | [PDF](https://arxiv.org/pdf/2511.03589.pdf)

**作者**: Romain Brégier, Guénolé Fiche, Laura Bravo-Sánchez, Thomas Lucas, Matthieu Armando, Philippe Weinzaepfel, Grégory Rogez, Fabien Baradel

---

## 💡 一句话要点

**提出Anny人体模型以解决现有模型依赖昂贵扫描和人口统计狭窄的问题**

**关键词**: `人体网格建模` `参数化人体模型` `合成数据生成` `人类网格恢复` `可解释形状空间` `开源模型`

## 📋 核心要点

1. 现有参数化人体模型依赖昂贵3D扫描，且形状空间专有、人口统计覆盖窄
2. 基于MakeHuman社区人类测量知识，构建可微分、无扫描的连续可解释形状空间
3. 使用WHO统计数据校准，生成多样化合成数据，HMR模型性能媲美扫描模型

## 📄 摘要（原文）

> Parametric body models are central to many human-centric tasks, yet existing
> models often rely on costly 3D scans and learned shape spaces that are
> proprietary and demographically narrow. We introduce Anny, a simple, fully
> differentiable, and scan-free human body model grounded in anthropometric
> knowledge from the MakeHuman community. Anny defines a continuous,
> interpretable shape space, where phenotype parameters (e.g. gender, age,
> height, weight) control blendshapes spanning a wide range of human forms --
> across ages (from infants to elders), body types, and proportions. Calibrated
> using WHO population statistics, it provides realistic and demographically
> grounded human shape variation within a single unified model. Thanks to its
> openness and semantic control, Anny serves as a versatile foundation for 3D
> human modeling -- supporting millimeter-accurate scan fitting, controlled
> synthetic data generation, and Human Mesh Recovery (HMR). We further introduce
> Anny-One, a collection of 800k photorealistic humans generated with Anny,
> showing that despite its simplicity, HMR models trained with Anny can match the
> performance of those trained with scan-based body models, while remaining
> interpretable and broadly representative. The Anny body model and its code are
> released under the Apache 2.0 license, making Anny an accessible foundation for
> human-centric 3D modeling.

