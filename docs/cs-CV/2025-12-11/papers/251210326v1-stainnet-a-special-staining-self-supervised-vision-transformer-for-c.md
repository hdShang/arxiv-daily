---
layout: default
title: StainNet: A Special Staining Self-Supervised Vision Transformer for Computational Pathology
---

# StainNet: A Special Staining Self-Supervised Vision Transformer for Computational Pathology

**arXiv**: [2512.10326v1](https://arxiv.org/abs/2512.10326) | [PDF](https://arxiv.org/pdf/2512.10326.pdf)

**作者**: Jiawen Li, Jiali Hu, Xitong Ling, Yongqiang Lv, Yuxuan Chen, Yizhi Wang, Tian Guan, Yifei Liu, Yonghong He

---

## 💡 一句话要点

**提出StainNet以解决特殊染色病理图像分析中现有基础模型受限的问题**

**关键词**: `计算病理学` `自监督学习` `视觉Transformer` `特殊染色` `基础模型` `图像检索`

## 📋 核心要点

1. 现有病理基础模型主要基于H&E染色图像预训练，在特殊染色临床应用中可能受限
2. StainNet采用自蒸馏自监督学习，基于ViT架构，在HISTAI数据库的140万特殊染色图像块上训练
3. 实验在肝恶性肿瘤分类和公开数据集上验证其性能，并进行了少样本学习和检索评估

## 📄 摘要（原文）

> Foundation models trained with self-supervised learning (SSL) on large-scale histological images have significantly accelerated the development of computational pathology. These models can serve as backbones for region-of-interest (ROI) image analysis or patch-level feature extractors in whole-slide images (WSIs) based on multiple instance learning (MIL). Existing pathology foundation models (PFMs) are typically pre-trained on Hematoxylin-Eosin (H&E) stained pathology images. However, images with special stains, such as immunohistochemistry, are also frequently used in clinical practice. PFMs pre-trained mainly on H\&E-stained images may be limited in clinical applications involving special stains. To address this issue, we propose StainNet, a specialized foundation model for special stains based on the vision transformer (ViT) architecture. StainNet adopts a self-distillation SSL approach and is trained on over 1.4 million patch images cropping from 20,231 publicly available special staining WSIs in the HISTAI database. To evaluate StainNet, we conduct experiments on an in-house slide-level liver malignancy classification task and two public ROI-level datasets to demonstrate its strong ability. We also perform few-ratio learning and retrieval evaluations, and compare StainNet with recently larger PFMs to further highlight its strengths. We have released the StainNet model weights at: https://huggingface.co/JWonderLand/StainNet.

