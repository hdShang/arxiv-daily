---
layout: default
title: From Prompts to Printable Models: Support-Effective 3D Generation via Offset Direct Preference Optimization
---

# From Prompts to Printable Models: Support-Effective 3D Generation via Offset Direct Preference Optimization

**arXiv**: [2511.16434v1](https://arxiv.org/abs/2511.16434) | [PDF](https://arxiv.org/pdf/2511.16434.pdf)

**作者**: Chenming Wu, Xiaofan Li, Chengkai Dai

---

## 💡 一句话要点

**提出SEG框架以优化3D模型生成，减少3D打印支撑结构使用**

**关键词**: `3D模型生成` `直接偏好优化` `支撑结构优化` `3D打印效率` `材料节约`

## 📋 核心要点

1. 核心问题：3D打印中支撑结构导致材料浪费和生产延迟，现有技术仅事后优化
2. 方法要点：集成偏移直接偏好优化，在生成阶段模拟支撑结构以最小化需求
3. 实验或效果：在基准数据集上显著减少支撑体积，优于TRELLIS等基线模型

## 📄 摘要（原文）

> The transition from digital 3D models to physical objects via 3D printing often requires support structures to prevent overhanging features from collapsing during the fabrication process. While current slicing technologies offer advanced support strategies, they focus on post-processing optimizations rather than addressing the underlying need for support-efficient design during the model generation phase. This paper introduces SEG (\textit{\underline{S}upport-\underline{E}ffective \underline{G}eneration}), a novel framework that integrates Direct Preference Optimization with an Offset (ODPO) into the 3D generation pipeline to directly optimize models for minimal support material usage. By incorporating support structure simulation into the training process, SEG encourages the generation of geometries that inherently require fewer supports, thus reducing material waste and production time. We demonstrate SEG's effectiveness through extensive experiments on two benchmark datasets, Thingi10k-Val and GPT-3DP-Val, showing that SEG significantly outperforms baseline models such as TRELLIS, DPO, and DRO in terms of support volume reduction and printability. Qualitative results further reveal that SEG maintains high fidelity to input prompts while minimizing the need for support structures. Our findings highlight the potential of SEG to transform 3D printing by directly optimizing models during the generative process, paving the way for more sustainable and efficient digital fabrication practices.

