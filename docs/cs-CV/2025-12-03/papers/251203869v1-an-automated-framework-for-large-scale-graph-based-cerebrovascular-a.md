---
layout: default
title: An Automated Framework for Large-Scale Graph-Based Cerebrovascular Analysis
---

# An Automated Framework for Large-Scale Graph-Based Cerebrovascular Analysis

**arXiv**: [2512.03869v1](https://arxiv.org/abs/2512.03869) | [PDF](https://arxiv.org/pdf/2512.03869.pdf)

**作者**: Daniele Falcetta, Liane S. Canas, Lorenzo Suppa, Matteo Pentassuglia, Jon Cleary, Marc Modat, Sébastien Ourselin, Maria A. Zuluaga

---

## 💡 一句话要点

**提出CaravelMetrics框架，通过图表示实现大规模脑血管自动化分析。**

**关键词**: `脑血管分析` `图表示` `骨架化` `多尺度特征` `自动化框架` `人口研究`

## 📋 核心要点

1. 核心问题：自动化量化脑血管形态与拓扑特征，支持血管健康与衰老研究。
2. 方法要点：集成骨架化、图谱分割和图构建，提取多尺度形态、拓扑、分形和几何特征。
3. 实验或效果：应用于570个3D TOF-MRA扫描，捕获年龄、性别和教育相关的血管复杂性变化。

## 📄 摘要（原文）

> We present CaravelMetrics, a computational framework for automated cerebrovascular analysis that models vessel morphology through skeletonization-derived graph representations. The framework integrates atlas-based regional parcellation, centerline extraction, and graph construction to compute fifteen morphometric, topological, fractal, and geometric features. The features can be estimated globally from the complete vascular network or regionally within arterial territories, enabling multiscale characterization of cerebrovascular organization. Applied to 570 3D TOF-MRA scans from the IXI dataset (ages 20-86), CaravelMetrics yields reproducible vessel graphs capturing age- and sex-related variations and education-associated increases in vascular complexity, consistent with findings reported in the literature. The framework provides a scalable and fully automated approach for quantitative cerebrovascular feature extraction, supporting normative modeling and population-level studies of vascular health and aging.

