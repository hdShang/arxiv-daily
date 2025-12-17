---
layout: default
title: TiCAL:Typicality-Based Consistency-Aware Learning for Multimodal Emotion Recognition
---

# TiCAL:Typicality-Based Consistency-Aware Learning for Multimodal Emotion Recognition

**arXiv**: [2511.15085v1](https://arxiv.org/abs/2511.15085) | [PDF](https://arxiv.org/pdf/2511.15085.pdf)

**作者**: Wen Yin, Siyu Zhan, Cencen Liu, Xin Hu, Guiduo Duan, Xiurui Xie, Yuan-Fang Li, Tao He

---

## 💡 一句话要点

**提出TiCAL框架以解决多模态情感识别中的模态间情感冲突问题**

**关键词**: `多模态情感识别` `模态一致性学习` `典型性估计` `双曲空间嵌入` `情感冲突缓解`

## 📋 核心要点

1. 核心问题：多模态情感识别中，同一样本的不同模态可能表达冲突情感，现有方法常忽略此问题。
2. 方法要点：基于典型性估计动态评估样本一致性，并在双曲空间中嵌入特征以捕捉情感细微差异。
3. 实验或效果：在CMU-MOSEI和MER2023数据集上验证，性能提升约2.6%，优于现有最佳方法。

## 📄 摘要（原文）

> Multimodal Emotion Recognition (MER) aims to accurately identify human emotional states by integrating heterogeneous modalities such as visual, auditory, and textual data. Existing approaches predominantly rely on unified emotion labels to supervise model training, often overlooking a critical challenge: inter-modal emotion conflicts, wherein different modalities within the same sample may express divergent emotional tendencies. In this work, we address this overlooked issue by proposing a novel framework, Typicality-based Consistent-aware Multimodal Emotion Recognition (TiCAL), inspired by the stage-wise nature of human emotion perception. TiCAL dynamically assesses the consistency of each training sample by leveraging pseudo unimodal emotion labels alongside a typicality estimation. To further enhance emotion representation, we embed features in a hyperbolic space, enabling the capture of fine-grained distinctions among emotional categories. By incorporating consistency estimates into the learning process, our method improves model performance, particularly on samples exhibiting high modality inconsistency. Extensive experiments on benchmark datasets, e.g, CMU-MOSEI and MER2023, validate the effectiveness of TiCAL in mitigating inter-modal emotional conflicts and enhancing overall recognition accuracy, e.g., with about 2.6% improvements over the state-of-the-art DMD.

