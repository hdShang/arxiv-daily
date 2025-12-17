---
layout: default
title: DualProtoSeg: Simple and Efficient Design with Text- and Image-Guided Prototype Learning for Weakly Supervised Histopathology Image Segmentation
---

# DualProtoSeg: Simple and Efficient Design with Text- and Image-Guided Prototype Learning for Weakly Supervised Histopathology Image Segmentation

**arXiv**: [2512.10314v1](https://arxiv.org/abs/2512.10314) | [PDF](https://arxiv.org/pdf/2512.10314.pdf)

**作者**: Anh M. Vu, Khang P. Le, Trang T. K. Vo, Ha Thach, Huy Hung Nguyen, David Yang, Han H. Huynh, Quynh Nguyen, Tuan M. Pham, Tuan-Anh Le, Minh H. N. Le, Thanh-Huy Nguyen, Akash Awasthi, Chandra Mohan, Zhu Han, Hien Van Nguyen

---

## 💡 一句话要点

**提出DualProtoSeg框架，通过文本和图像引导的原型学习解决弱监督组织病理图像分割问题**

**关键词**: `弱监督语义分割` `组织病理图像` `原型学习` `视觉语言对齐` `多尺度金字塔模块` `数字病理学`

## 📋 核心要点

1. 核心问题：弱监督组织病理图像分割面临类间同质、类内异质和CAM监督区域收缩效应
2. 方法要点：结合可学习提示调优生成文本原型，并与图像原型形成双模态原型库，增强语义和外观线索
3. 实验或效果：在BCSS-WSSS基准测试中超越现有方法，验证文本描述多样性和多模态原型的互补性

## 📄 摘要（原文）

> Weakly supervised semantic segmentation (WSSS) in histopathology seeks to reduce annotation cost by learning from image-level labels, yet it remains limited by inter-class homogeneity, intra-class heterogeneity, and the region-shrinkage effect of CAM-based supervision. We propose a simple and effective prototype-driven framework that leverages vision-language alignment to improve region discovery under weak supervision. Our method integrates CoOp-style learnable prompt tuning to generate text-based prototypes and combines them with learnable image prototypes, forming a dual-modal prototype bank that captures both semantic and appearance cues. To address oversmoothing in ViT representations, we incorporate a multi-scale pyramid module that enhances spatial precision and improves localization quality. Experiments on the BCSS-WSSS benchmark show that our approach surpasses existing state-of-the-art methods, and detailed analyses demonstrate the benefits of text description diversity, context length, and the complementary behavior of text and image prototypes. These results highlight the effectiveness of jointly leveraging textual semantics and visual prototype learning for WSSS in digital pathology.

