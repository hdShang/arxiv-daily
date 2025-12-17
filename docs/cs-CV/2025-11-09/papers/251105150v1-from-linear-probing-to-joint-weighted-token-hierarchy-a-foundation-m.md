---
layout: default
title: From Linear Probing to Joint-Weighted Token Hierarchy: A Foundation Model Bridging Global and Cellular Representations in Biomarker Detection
---

# From Linear Probing to Joint-Weighted Token Hierarchy: A Foundation Model Bridging Global and Cellular Representations in Biomarker Detection

**arXiv**: [2511.05150v1](https://arxiv.org/abs/2511.05150) | [PDF](https://arxiv.org/pdf/2511.05150.pdf)

**作者**: Jingsong Liu, Han Li, Nassir Navab, Peter J. Schüffler

---

## 💡 一句话要点

**提出联合加权令牌层次模型以融合全局和细胞级表示，提升数字病理学生物标志物检测性能**

**关键词**: `病理基础模型` `生物标志物检测` `自监督学习` `注意力机制` `数字病理学` `令牌融合`

## 📋 核心要点

1. 核心问题：现有病理基础模型依赖全局补丁嵌入，忽略细胞级形态学特征
2. 方法要点：结合大规模自监督预训练、细胞中心后调优和注意力池化融合局部与全局令牌
3. 实验或效果：在四个生物标志物任务中，平衡准确率最高提升8.3%，平均提高1.2%

## 📄 摘要（原文）

> AI-based biomarkers can infer molecular features directly from hematoxylin &
> eosin (H&E) slides, yet most pathology foundation models (PFMs) rely on global
> patch-level embeddings and overlook cell-level morphology. We present a PFM
> model, JWTH (Joint-Weighted Token Hierarchy), which integrates large-scale
> self-supervised pretraining with cell-centric post-tuning and attention pooling
> to fuse local and global tokens. Across four tasks involving four biomarkers
> and eight cohorts, JWTH achieves up to 8.3% higher balanced accuracy and 1.2%
> average improvement over prior PFMs, advancing interpretable and robust
> AI-based biomarker detection in digital pathology.

