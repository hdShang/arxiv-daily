---
layout: default
title: Phys-Liquid: A Physics-Informed Dataset for Estimating 3D Geometry and Volume of Transparent Deformable Liquids
---

# Phys-Liquid: A Physics-Informed Dataset for Estimating 3D Geometry and Volume of Transparent Deformable Liquids

**arXiv**: [2511.11077v1](https://arxiv.org/abs/2511.11077) | [PDF](https://arxiv.org/pdf/2511.11077.pdf)

**作者**: Ke Ma, Yizhou Fang, Jean-Baptiste Weibel, Shuai Tan, Xinggang Wang, Yang Xiao, Yi Fang, Tian Xia

---

## 💡 一句话要点

**提出Phys-Liquid数据集以解决透明变形液体3D几何与体积估计问题**

**关键词**: `透明液体估计` `物理模拟数据集` `3D网格重建` `液体几何体积` `机器人液体操作`

## 📋 核心要点

1. 核心问题：透明液体因光学复杂性和动态变形，几何与体积估计困难
2. 方法要点：构建物理模拟数据集，含多场景图像和3D网格，支持重建流程
3. 实验或效果：验证显示重建精度和一致性优于现有基准，促进液体感知研究

## 📄 摘要（原文）

> Estimating the geometric and volumetric properties of transparent deformable liquids is challenging due to optical complexities and dynamic surface deformations induced by container movements. Autonomous robots performing precise liquid manipulation tasks, such as dispensing, aspiration, and mixing, must handle containers in ways that inevitably induce these deformations, complicating accurate liquid state assessment. Current datasets lack comprehensive physics-informed simulation data representing realistic liquid behaviors under diverse dynamic scenarios. To bridge this gap, we introduce Phys-Liquid, a physics-informed dataset comprising 97,200 simulation images and corresponding 3D meshes, capturing liquid dynamics across multiple laboratory scenes, lighting conditions, liquid colors, and container rotations. To validate the realism and effectiveness of Phys-Liquid, we propose a four-stage reconstruction and estimation pipeline involving liquid segmentation, multi-view mask generation, 3D mesh reconstruction, and real-world scaling. Experimental results demonstrate improved accuracy and consistency in reconstructing liquid geometry and volume, outperforming existing benchmarks. The dataset and associated validation methods facilitate future advancements in transparent liquid perception tasks. The dataset and code are available at https://dualtransparency.github.io/Phys-Liquid/.

