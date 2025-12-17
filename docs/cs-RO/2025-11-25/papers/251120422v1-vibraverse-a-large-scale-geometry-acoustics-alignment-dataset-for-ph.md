---
layout: default
title: VibraVerse: A Large-Scale Geometry-Acoustics Alignment Dataset for Physically-Consistent Multimodal Learning
---

# VibraVerse: A Large-Scale Geometry-Acoustics Alignment Dataset for Physically-Consistent Multimodal Learning

**arXiv**: [2511.20422v1](https://arxiv.org/abs/2511.20422) | [PDF](https://arxiv.org/pdf/2511.20422.pdf)

**作者**: Bo Pang, Chenxi Xu, Jierui Ren, Guoping Wang, Sheng Li

---

## 💡 一句话要点

**提出VibraVerse数据集与CLASP框架，以解决多模态学习中物理一致性问题。**

**关键词**: `多模态学习` `物理一致性` `几何-声学对齐` `对比学习` `数据集构建` `因果推理`

## 📋 核心要点

1. 现有视觉-语言多模态学习缺乏物理一致性，忽略几何、材料与声音的因果链。
2. 构建大规模几何-声学对齐数据集，通过物理属性计算模态参数合成声音。
3. 实验验证模型在几何-声音预测等任务中准确性和泛化性显著提升。

## 📄 摘要（原文）

> Understanding the physical world requires perceptual models grounded in physical laws rather than mere statistical correlations. However, existing multimodal learning frameworks, focused on vision and language, lack physical consistency and overlook the intrinsic causal relationships among an object's geometry, material, vibration modes, and the sounds it produces. We introduce VibraVerse, a large-scale geometry-acoustics alignment dataset that explicitly bridges the causal chain from 3D geometry -> physical attributes -> modal parameters -> acoustic signals. Each 3D model has explicit physical properties (density, Young's modulus, Poisson's ratio) and volumetric geometry, from which modal eigenfrequencies and eigenvectors are computed for impact sound synthesis under controlled excitations. To establish this coherence, we introduce CLASP, a contrastive learning framework for cross-modal alignment that preserves the causal correspondence between an object's physical structure and its acoustic response. This framework enforces physically consistent alignment across modalities, ensuring that every sample is coherent, traceable to the governing equations, and embedded within a unified representation space spanning shape, image, and sound. Built upon VibraVerse, we define a suite of benchmark tasks for geometry-to-sound prediction, sound-guided shape reconstruction, and cross-modal representation learning. Extensive validations on these tasks demonstrate that models trained on VibraVerse exhibit superior accuracy, interpretability, and generalization across modalities. These results establish VibraVerse as a benchmark for physically consistent and causally interpretable multimodal learning, providing a foundation for sound-guided embodied perception and a deeper understanding of the physical world. The dataset will be open-sourced.

