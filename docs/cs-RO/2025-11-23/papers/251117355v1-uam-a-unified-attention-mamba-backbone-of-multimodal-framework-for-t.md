---
layout: default
title: UAM: A Unified Attention-Mamba Backbone of Multimodal Framework for Tumor Cell Classification
---

# UAM: A Unified Attention-Mamba Backbone of Multimodal Framework for Tumor Cell Classification

**arXiv**: [2511.17355v1](https://arxiv.org/abs/2511.17355) | [PDF](https://arxiv.org/pdf/2511.17355.pdf)

**作者**: Taixi Chen, Jingyun Chen, Nancy Guo

---

## 💡 一句话要点

**提出统一注意力-Mamba骨干网络，用于肿瘤细胞分类的多模态框架**

**关键词**: `细胞级放射组学` `注意力机制` `Mamba架构` `多模态学习` `肿瘤分类` `图像分割`

## 📋 核心要点

1. 现有研究多关注切片或斑块级肿瘤分类，细胞级放射组学分析未被充分探索
2. 统一设计灵活结合注意力和Mamba模块，无需手动调整比例，提升编码能力
3. 实验显示细胞分类准确率从74%提升至78%，肿瘤分割精度从75%提升至80%

## 📄 摘要（原文）

> Cell-level radiomics features provide fine-grained insights into tumor phenotypes and have the potential to significantly enhance diagnostic accuracy on hematoxylin and eosin (H&E) images. By capturing micro-level morphological and intensity patterns, these features support more precise tumor identification and improve AI interpretability by highlighting diagnostically relevant cells for pathologist review. However, most existing studies focus on slide-level or patch-level tumor classification, leaving cell-level radiomics analysis largely unexplored. Moreover, there is currently no dedicated backbone specifically designed for radiomics data. Inspired by the recent success of the Mamba architecture in vision and language domains, we introduce a Unified Attention-Mamba (UAM) backbone for cell-level classification using radiomics features. Unlike previous hybrid approaches that integrate Attention and Mamba modules in fixed proportions, our unified design flexibly combines their capabilities within a single cohesive architecture, eliminating the need for manual ratio tuning and improving encode capability. We develop two UAM variants to comprehensively evaluate the benefits of this unified structure. Building on this backbone, we further propose a multimodal UAM framework that jointly performs cell-level classification and image segmentation. Experimental results demonstrate that UAM achieves state-of-the-art performance across both tasks on public benchmarks, surpassing leading image-based foundation models. It improves cell classification accuracy from 74% to 78% ($n$=349,882 cells), and tumor segmentation precision from 75% to 80% ($n$=406 patches). These findings highlight the effectiveness and promise of UAM as a unified and extensible multimodal foundation for radiomics-driven cancer diagnosis.

