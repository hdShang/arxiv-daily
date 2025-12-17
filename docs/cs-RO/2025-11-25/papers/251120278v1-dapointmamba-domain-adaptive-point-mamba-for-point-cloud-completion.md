---
layout: default
title: DAPointMamba: Domain Adaptive Point Mamba for Point Cloud Completion
---

# DAPointMamba: Domain Adaptive Point Mamba for Point Cloud Completion

**arXiv**: [2511.20278v1](https://arxiv.org/abs/2511.20278) | [PDF](https://arxiv.org/pdf/2511.20278.pdf)

**作者**: Yinghui Li, Qianyu Zhou, Di Shao, Hao Yang, Ye Zhu, Richard Dazeley, Xuequan Lu

---

## 💡 一句话要点

**提出DAPointMamba框架以解决领域自适应点云补全中的几何语义差异问题**

**关键词**: `领域自适应` `点云补全` `状态空间模型` `跨域对齐` `线性复杂度`

## 📋 核心要点

1. 核心问题：领域自适应点云补全中几何语义差异大，现有方法感受野有限或计算复杂度高
2. 方法要点：引入跨域补丁扫描和空间通道SSM对齐，增强局部对齐与全局语义一致性
3. 实验或效果：在合成和真实数据集上优于现有方法，计算复杂度低且推理延迟小

## 📄 摘要（原文）

> Domain adaptive point cloud completion (DA PCC) aims to narrow the geometric and semantic discrepancies between the labeled source and unlabeled target domains. Existing methods either suffer from limited receptive fields or quadratic complexity due to using CNNs or vision Transformers. In this paper, we present the first work that studies the adaptability of State Space Models (SSMs) in DA PCC and find that directly applying SSMs to DA PCC will encounter several challenges: directly serializing 3D point clouds into 1D sequences often disrupts the spatial topology and local geometric features of the target domain. Besides, the overlook of designs in the learning domain-agnostic representations hinders the adaptation performance. To address these issues, we propose a novel framework, DAPointMamba for DA PCC, that exhibits strong adaptability across domains and has the advantages of global receptive fields and efficient linear complexity. It has three novel modules. In particular, Cross-Domain Patch-Level Scanning introduces patch-level geometric correspondences, enabling effective local alignment. Cross-Domain Spatial SSM Alignment further strengthens spatial consistency by modulating patch features based on cross-domain similarity, effectively mitigating fine-grained structural discrepancies. Cross-Domain Channel SSM Alignment actively addresses global semantic gaps by interleaving and aligning feature channels. Extensive experiments on both synthetic and real-world benchmarks demonstrate that our DAPointMamba outperforms state-of-the-art methods with less computational complexity and inference latency.

