---
layout: default
title: CCSD: Cross-Modal Compositional Self-Distillation for Robust Brain Tumor Segmentation with Missing Modalities
---

# CCSD: Cross-Modal Compositional Self-Distillation for Robust Brain Tumor Segmentation with Missing Modalities

**arXiv**: [2511.14599v1](https://arxiv.org/abs/2511.14599) | [PDF](https://arxiv.org/pdf/2511.14599.pdf)

**作者**: Dongqing Xie, Yonghuang Wu, Zisheng Ai, Jun Min, Zhencun Jiang, Shaojin Geng, Lei Wang

---

## 💡 一句话要点

**提出跨模态组合自蒸馏框架以解决脑肿瘤分割中模态缺失问题**

**关键词**: `脑肿瘤分割` `多模态MRI` `模态缺失` `自蒸馏` `跨模态学习` `深度学习模型`

## 📋 核心要点

1. 核心问题：多模态MRI中模态缺失严重影响脑肿瘤分割模型的性能与泛化能力
2. 方法要点：采用共享-特定编码器-解码器架构，结合分层模态自蒸馏和渐进模态组合蒸馏
3. 实验或效果：在公开基准测试中，CCSD在多种模态缺失场景下达到先进性能，泛化性强

## 📄 摘要（原文）

> The accurate segmentation of brain tumors from multi-modal MRI is critical for clinical diagnosis and treatment planning. While integrating complementary information from various MRI sequences is a common practice, the frequent absence of one or more modalities in real-world clinical settings poses a significant challenge, severely compromising the performance and generalizability of deep learning-based segmentation models. To address this challenge, we propose a novel Cross-Modal Compositional Self-Distillation (CCSD) framework that can flexibly handle arbitrary combinations of input modalities. CCSD adopts a shared-specific encoder-decoder architecture and incorporates two self-distillation strategies: (i) a hierarchical modality self-distillation mechanism that transfers knowledge across modality hierarchies to reduce semantic discrepancies, and (ii) a progressive modality combination distillation approach that enhances robustness to missing modalities by simulating gradual modality dropout during training. Extensive experiments on public brain tumor segmentation benchmarks demonstrate that CCSD achieves state-of-the-art performance across various missing-modality scenarios, with strong generalization and stability.

