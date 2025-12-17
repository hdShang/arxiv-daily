---
layout: default
title: Text2Loc++: Generalizing 3D Point Cloud Localization from Natural Language
---

# Text2Loc++: Generalizing 3D Point Cloud Localization from Natural Language

**arXiv**: [2511.15308v1](https://arxiv.org/abs/2511.15308) | [PDF](https://arxiv.org/pdf/2511.15308.pdf)

**作者**: Yan Xia, Letian Shi, Yilin Di, Joao F. Henriques, Daniel Cremers

---

## 💡 一句话要点

**提出Text2Loc++以解决自然语言描述定位3D点云子图的问题**

**关键词**: `3D点云定位` `自然语言处理` `跨模态对齐` `对比学习` `城市规模数据集` `粗到精定位`

## 📋 核心要点

1. 核心问题：使用复杂多样的自然语言描述定位3D点云子图，支持城市规模场景
2. 方法要点：采用粗到精定位流程，结合跨模态对齐、掩码实例训练和分层对比学习
3. 实验或效果：在KITTI360Pose数据集上性能提升达15%，新数据集验证强泛化能力

## 📄 摘要（原文）

> We tackle the problem of localizing 3D point cloud submaps using complex and diverse natural language descriptions, and present Text2Loc++, a novel neural network designed for effective cross-modal alignment between language and point clouds in a coarse-to-fine localization pipeline. To support benchmarking, we introduce a new city-scale dataset covering both color and non-color point clouds from diverse urban scenes, and organize location descriptions into three levels of linguistic complexity. In the global place recognition stage, Text2Loc++ combines a pretrained language model with a Hierarchical Transformer with Max pooling (HTM) for sentence-level semantics, and employs an attention-based point cloud encoder for spatial understanding. We further propose Masked Instance Training (MIT) to filter out non-aligned objects and improve multimodal robustness. To enhance the embedding space, we introduce Modality-aware Hierarchical Contrastive Learning (MHCL), incorporating cross-modal, submap-, text-, and instance-level losses. In the fine localization stage, we completely remove explicit text-instance matching and design a lightweight yet powerful framework based on Prototype-based Map Cloning (PMC) and a Cascaded Cross-Attention Transformer (CCAT). Extensive experiments on the KITTI360Pose dataset show that Text2Loc++ outperforms existing methods by up to 15%. In addition, the proposed model exhibits robust generalization when evaluated on the new dataset, effectively handling complex linguistic expressions and a wide variety of urban environments. The code and dataset will be made publicly available.

