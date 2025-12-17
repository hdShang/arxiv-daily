---
layout: default
title: LapFM: A Laparoscopic Segmentation Foundation Model via Hierarchical Concept Evolving Pre-training
---

# LapFM: A Laparoscopic Segmentation Foundation Model via Hierarchical Concept Evolving Pre-training

**arXiv**: [2512.08439v1](https://arxiv.org/abs/2512.08439) | [PDF](https://arxiv.org/pdf/2512.08439.pdf)

**作者**: Qing Xu, Kun Yuan, Yuxiang Luo, Yuhao Zhai, Wenting Duan, Nassir Navab, Zhen Chen

---

## 💡 一句话要点

**提出LapFM基础模型，通过分层概念演化预训练解决腹腔镜分割中标注稀缺与语义不一致问题。**

**关键词**: `腹腔镜分割` `基础模型` `分层概念演化` `伪标签生成` `无监督预训练` `手术场景理解`

## 📋 核心要点

1. 核心问题：手术分割因标注稀缺和跨程序语义不一致而受限，现有方法泛化能力差。
2. 方法要点：采用分层概念演化预训练，构建腹腔镜概念层次并迭代生成伪标签，从无标注图像中学习。
3. 实验或效果：在LapBench-114K基准上显著优于先进方法，实现粒度自适应泛化。

## 📄 摘要（原文）

> Surgical segmentation is pivotal for scene understanding yet remains hindered by annotation scarcity and semantic inconsistency across diverse procedures. Existing approaches typically fine-tune natural foundation models (e.g., SAM) with limited supervision, functioning merely as domain adapters rather than surgical foundation models. Consequently, they struggle to generalize across the vast variability of surgical targets. To bridge this gap, we present LapFM, a foundation model designed to evolve robust segmentation capabilities from massive unlabeled surgical images. Distinct from medical foundation models relying on inefficient self-supervised proxy tasks, LapFM leverages a Hierarchical Concept Evolving Pre-training paradigm. First, we establish a Laparoscopic Concept Hierarchy (LCH) via a hierarchical mask decoder with parent-child query embeddings, unifying diverse entities (i.e., Anatomy, Tissue, and Instrument) into a scalable knowledge structure with cross-granularity semantic consistency. Second, we propose a Confidence-driven Evolving Labeling that iteratively generates and filters pseudo-labels based on hierarchical consistency, progressively incorporating reliable samples from unlabeled images into training. This process yields LapBench-114K, a large-scale benchmark comprising 114K image-mask pairs. Extensive experiments demonstrate that LapFM significantly outperforms state-of-the-art methods, establishing new standards for granularity-adaptive generalization in universal laparoscopic segmentation. The source code is available at https://github.com/xq141839/LapFM.

