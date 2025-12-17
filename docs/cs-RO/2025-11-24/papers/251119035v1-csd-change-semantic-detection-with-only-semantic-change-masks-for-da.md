---
layout: default
title: CSD: Change Semantic Detection with only Semantic Change Masks for Damage Assessment in Conflict Zones
---

# CSD: Change Semantic Detection with only Semantic Change Masks for Damage Assessment in Conflict Zones

**arXiv**: [2511.19035v1](https://arxiv.org/abs/2511.19035) | [PDF](https://arxiv.org/pdf/2511.19035.pdf)

**作者**: Kai Zhenga, Zhenkai Wu, Fupeng Wei, Miaolan Zhou, Kai Lie, Haitao Guo, Lei Ding, Wei Zhang, Hang-Cheng Dong

---

## 💡 一句话要点

**提出MC-DiSNet以解决冲突区域损伤评估中的语义变化检测问题**

**关键词**: `语义变化检测` `损伤评估` `多尺度网络` `DINOv3` `冲突区域遥感`

## 📋 核心要点

1. 核心问题：冲突区域损伤评估数据有限、标注困难，语义变化模糊且区域小。
2. 方法要点：使用预训练DINOv3和多尺度交叉注意力孪生网络提取特征。
3. 实验或效果：在Gaza-Change和SECOND数据集上验证，性能优异，支持实际应用。

## 📄 摘要（原文）

> Accurately and swiftly assessing damage from conflicts is crucial for humanitarian aid and regional stability. In conflict zones, damaged zones often share similar architectural styles, with damage typically covering small areas and exhibiting blurred boundaries. These characteristics lead to limited data, annotation difficulties, and significant recognition challenges, including high intra-class similarity and ambiguous semantic changes. To address these issues, we introduce a pre-trained DINOv3 model and propose a multi-scale cross-attention difference siamese network (MC-DiSNet). The powerful visual representation capability of the DINOv3 backbone enables robust and rich feature extraction from bi-temporal remote sensing images. We also release a new Gaza-change dataset containing high-resolution satellite image pairs from 2023-2024 with pixel-level semantic change annotations. It is worth emphasizing that our annotations only include semantic pixels of changed areas. Unlike conventional semantic change detection (SCD), our approach eliminates the need for large-scale semantic annotations of bi-temporal images, instead focusing directly on the changed regions. We term this new task change semantic detection (CSD). The CSD task represents a direct extension of binary change detection (BCD). Due to the limited spatial extent of semantic regions, it presents greater challenges than traditional SCD tasks. We evaluated our method under the CSD framework on both the Gaza-Change and SECOND datasets. Experimental results demonstrate that our proposed approach effectively addresses the CSD task, and its outstanding performance paves the way for practical applications in rapid damage assessment across conflict zones.

