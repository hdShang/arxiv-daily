---
layout: default
title: Learning to See Through a Baby's Eyes: Early Visual Diets Enable Robust Visual Intelligence in Humans and Machines
---

# Learning to See Through a Baby's Eyes: Early Visual Diets Enable Robust Visual Intelligence in Humans and Machines

**arXiv**: [2511.14440v1](https://arxiv.org/abs/2511.14440) | [PDF](https://arxiv.org/pdf/2511.14440.pdf)

**作者**: Yusen Cai, Bhargava Satya Nunna, Qing Lin, Mengmi Zhang

---

## 💡 一句话要点

**提出CATDiet模拟婴儿视觉饮食，提升自监督学习模型的鲁棒性**

**关键词**: `自监督学习` `婴儿视觉模拟` `鲁棒视觉识别` `时间连续性` `物体中心视频`

## 📋 核心要点

1. 核心问题：如何利用婴儿早期视觉发展模式增强机器视觉的鲁棒性
2. 方法要点：在自监督学习中引入灰度到彩色、模糊到清晰及时间连续性约束
3. 实验或效果：在十大数据集上验证，模型在物体识别和深度感知中表现更优

## 📄 摘要（原文）

> Newborns perceive the world with low-acuity, color-degraded, and temporally continuous vision, which gradually sharpens as infants develop. To explore the ecological advantages of such staged "visual diets", we train self-supervised learning (SSL) models on object-centric videos under constraints that simulate infant vision: grayscale-to-color (C), blur-to-sharp (A), and preserved temporal continuity (T)-collectively termed CATDiet. For evaluation, we establish a comprehensive benchmark across ten datasets, covering clean and corrupted image recognition, texture-shape cue conflict tests, silhouette recognition, depth-order classification, and the visual cliff paradigm. All CATDiet variants demonstrate enhanced robustness in object recognition, despite being trained solely on object-centric videos. Remarkably, models also exhibit biologically aligned developmental patterns, including neural plasticity changes mirroring synaptic density in macaque V1 and behaviors resembling infants' visual cliff responses. Building on these insights, CombDiet initializes SSL with CATDiet before standard training while preserving temporal continuity. Trained on object-centric or head-mounted infant videos, CombDiet outperforms standard SSL on both in-domain and out-of-domain object recognition and depth perception. Together, these results suggest that the developmental progression of early infant visual experience offers a powerful reverse-engineering framework for understanding the emergence of robust visual intelligence in machines. All code, data, and models will be publicly released.

