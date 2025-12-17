---
layout: default
title: HiFusion: Hierarchical Intra-Spot Alignment and Regional Context Fusion for Spatial Gene Expression Prediction from Histopathology
---

# HiFusion: Hierarchical Intra-Spot Alignment and Regional Context Fusion for Spatial Gene Expression Prediction from Histopathology

**arXiv**: [2511.12969v1](https://arxiv.org/abs/2511.12969) | [PDF](https://arxiv.org/pdf/2511.12969.pdf)

**作者**: Ziqiao Weng, Yaoyu Fang, Jiahe Qian, Xinkun Wang, Lee AD Cooper, Weidong Cai, Bo Zhou

---

## 💡 一句话要点

**提出HiFusion框架，通过层次化建模和上下文融合从组织病理图像预测空间基因表达**

**关键词**: `空间转录组学` `基因表达预测` `深度学习框架` `组织病理图像` `多分辨率建模` `上下文融合`

## 📋 核心要点

1. 核心问题：现有方法难以捕捉斑点内生物异质性，且易受形态噪声影响
2. 方法要点：结合多分辨率子块分解和跨尺度注意力，增强特征一致性与上下文整合
3. 实验或效果：在多个数据集上实现最优性能，验证了2D和3D场景的鲁棒性

## 📄 摘要（原文）

> Spatial transcriptomics (ST) bridges gene expression and tissue morphology but faces clinical adoption barriers due to technical complexity and prohibitive costs. While computational methods predict gene expression from H&E-stained whole-slide images (WSIs), existing approaches often fail to capture the intricate biological heterogeneity within spots and are susceptible to morphological noise when integrating contextual information from surrounding tissue. To overcome these limitations, we propose HiFusion, a novel deep learning framework that integrates two complementary components. First, we introduce the Hierarchical Intra-Spot Modeling module that extracts fine-grained morphological representations through multi-resolution sub-patch decomposition, guided by a feature alignment loss to ensure semantic consistency across scales. Concurrently, we present the Context-aware Cross-scale Fusion module, which employs cross-attention to selectively incorporate biologically relevant regional context, thereby enhancing representational capacity. This architecture enables comprehensive modeling of both cellular-level features and tissue microenvironmental cues, which are essential for accurate gene expression prediction. Extensive experiments on two benchmark ST datasets demonstrate that HiFusion achieves state-of-the-art performance across both 2D slide-wise cross-validation and more challenging 3D sample-specific scenarios. These results underscore HiFusion's potential as a robust, accurate, and scalable solution for ST inference from routine histopathology.

