---
layout: default
title: ConStruct: Structural Distillation of Foundation Models for Prototype-Based Weakly Supervised Histopathology Segmentation
---

# ConStruct: Structural Distillation of Foundation Models for Prototype-Based Weakly Supervised Histopathology Segmentation

**arXiv**: [2512.10316v1](https://arxiv.org/abs/2512.10316) | [PDF](https://arxiv.org/pdf/2512.10316.pdf)

**作者**: Khang Le, Ha Thach, Anh M. Vu, Trang T. K. Vo, Han H. Huynh, David Yang, Minh H. N. Le, Thanh-Huy Nguyen, Akash Awasthi, Chandra Mohan, Zhu Han, Hien Van Nguyen

---

## 💡 一句话要点

**提出原型学习框架以解决弱监督组织病理学分割中结构完整性和语义一致性问题**

**关键词**: `弱监督语义分割` `组织病理学图像` `原型学习` `结构蒸馏` `文本引导对齐` `基础模型集成`

## 📋 核心要点

1. 核心问题：弱监督组织病理学分割中分类模型仅定位最显著区域，难以捕获组织结构的完整空间范围。
2. 方法要点：集成CONCH的形态感知表示、SegFormer的多尺度结构线索和文本引导语义对齐，通过文本引导原型初始化和结构蒸馏机制生成高质量伪掩码。
3. 实验或效果：在BCSS-WSSS数据集上优于现有方法，提升定位完整性和语义一致性，计算高效。

## 📄 摘要（原文）

> Weakly supervised semantic segmentation (WSSS) in histopathology relies heavily on classification backbones, yet these models often localize only the most discriminative regions and struggle to capture the full spatial extent of tissue structures. Vision-language models such as CONCH offer rich semantic alignment and morphology-aware representations, while modern segmentation backbones like SegFormer preserve fine-grained spatial cues. However, combining these complementary strengths remains challenging, especially under weak supervision and without dense annotations. We propose a prototype learning framework for WSSS in histopathological images that integrates morphology-aware representations from CONCH, multi-scale structural cues from SegFormer, and text-guided semantic alignment to produce prototypes that are simultaneously semantically discriminative and spatially coherent. To effectively leverage these heterogeneous sources, we introduce text-guided prototype initialization that incorporates pathology descriptions to generate more complete and semantically accurate pseudo-masks. A structural distillation mechanism transfers spatial knowledge from SegFormer to preserve fine-grained morphological patterns and local tissue boundaries during prototype learning. Our approach produces high-quality pseudo masks without pixel-level annotations, improves localization completeness, and enhances semantic consistency across tissue types. Experiments on BCSS-WSSS datasets demonstrate that our prototype learning framework outperforms existing WSSS methods while remaining computationally efficient through frozen foundation model backbones and lightweight trainable adapters.

