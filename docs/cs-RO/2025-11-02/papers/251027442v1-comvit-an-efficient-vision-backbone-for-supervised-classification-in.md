---
layout: default
title: CoMViT: An Efficient Vision Backbone for Supervised Classification in Medical Imaging
---

# CoMViT: An Efficient Vision Backbone for Supervised Classification in Medical Imaging

**arXiv**: [2510.27442v1](https://arxiv.org/abs/2510.27442) | [PDF](https://arxiv.org/pdf/2510.27442.pdf)

**作者**: Aon Safdar, Mohamed Saadeldin

---

## 💡 一句话要点

**提出CoMViT以解决医学影像中ViT计算高和过拟合问题**

**关键词**: `医学影像分类` `视觉Transformer` `轻量模型` `泛化能力` `计算效率`

## 📋 核心要点

1. ViT在医学影像中计算需求高且易在小数据集过拟合
2. 集成卷积分词器、对角掩码等技术优化架构
3. 在12个MedMNIST数据集上性能稳健，参数仅约4.5M

## 📄 摘要（原文）

> Vision Transformers (ViTs) have demonstrated strong potential in medical
> imaging; however, their high computational demands and tendency to overfit on
> small datasets limit their applicability in real-world clinical scenarios. In
> this paper, we present CoMViT, a compact and generalizable Vision Transformer
> architecture optimized for resource-constrained medical image analysis. CoMViT
> integrates a convolutional tokenizer, diagonal masking, dynamic temperature
> scaling, and pooling-based sequence aggregation to improve performance and
> generalization. Through systematic architectural optimization, CoMViT achieves
> robust performance across twelve MedMNIST datasets while maintaining a
> lightweight design with only ~4.5M parameters. It matches or outperforms deeper
> CNN and ViT variants, offering up to 5-20x parameter reduction without
> sacrificing accuracy. Qualitative Grad-CAM analyses show that CoMViT
> consistently attends to clinically relevant regions despite its compact size.
> These results highlight the potential of principled ViT redesign for developing
> efficient and interpretable models in low-resource medical imaging settings.

