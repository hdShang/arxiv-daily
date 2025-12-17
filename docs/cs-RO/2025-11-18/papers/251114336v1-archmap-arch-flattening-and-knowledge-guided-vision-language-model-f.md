---
layout: default
title: ArchMap: Arch-Flattening and Knowledge-Guided Vision Language Model for Tooth Counting and Structured Dental Understanding
---

# ArchMap: Arch-Flattening and Knowledge-Guided Vision Language Model for Tooth Counting and Structured Dental Understanding

**arXiv**: [2511.14336v1](https://arxiv.org/abs/2511.14336) | [PDF](https://arxiv.org/pdf/2511.14336.pdf)

**作者**: Bohan Zhang, Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhuoxiao Li, Zhe Tang, Limin Yu, Jionglong Su

---

## 💡 一句话要点

**提出ArchMap框架，结合几何标准化与知识引导，实现3D口腔扫描的结构化理解。**

**关键词**: `3D口腔扫描` `几何标准化` `知识引导推理` `牙科结构化理解` `训练免费框架`

## 📋 核心要点

1. 核心问题：3D口腔扫描存在姿态变化、几何不完整和缺乏纹理，限制泛化与临床应用。
2. 方法要点：通过几何感知的牙弓展平模块和牙科知识库，实现训练免费的多模态推理。
3. 实验或效果：在1060病例中验证，牙计数、分区和临床条件识别准确高，优于监督基线。

## 📄 摘要（原文）

> A structured understanding of intraoral 3D scans is essential for digital orthodontics. However, existing deep-learning approaches rely heavily on modality-specific training, large annotated datasets, and controlled scanning conditions, which limit generalization across devices and hinder deployment in real clinical workflows. Moreover, raw intraoral meshes exhibit substantial variation in arch pose, incomplete geometry caused by occlusion or tooth contact, and a lack of texture cues, making unified semantic interpretation highly challenging. To address these limitations, we propose ArchMap, a training-free and knowledge-guided framework for robust structured dental understanding. ArchMap first introduces a geometry-aware arch-flattening module that standardizes raw 3D meshes into spatially aligned, continuity-preserving multi-view projections. We then construct a Dental Knowledge Base (DKB) encoding hierarchical tooth ontology, dentition-stage policies, and clinical semantics to constrain the symbolic reasoning space. We validate ArchMap on 1060 pre-/post-orthodontic cases, demonstrating robust performance in tooth counting, anatomical partitioning, dentition-stage classification, and the identification of clinical conditions such as crowding, missing teeth, prosthetics, and caries. Compared with supervised pipelines and prompted VLM baselines, ArchMap achieves higher accuracy, reduced semantic drift, and superior stability under sparse or artifact-prone conditions. As a fully training-free system, ArchMap demonstrates that combining geometric normalization with ontology-guided multimodal reasoning offers a practical and scalable solution for the structured analysis of 3D intraoral scans in modern digital orthodontics.

