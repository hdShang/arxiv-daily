---
layout: default
title: Order Matters: 3D Shape Generation from Sequential VR Sketches
---

# Order Matters: 3D Shape Generation from Sequential VR Sketches

**arXiv**: [2512.04761v1](https://arxiv.org/abs/2512.04761) | [PDF](https://arxiv.org/pdf/2512.04761.pdf)

**作者**: Yizi Chen, Sidi Wu, Tianyi Xiao, Nina Wiedemann, Loic Landrieu

---

## 💡 一句话要点

**提出VRSketch2Shape框架，利用顺序VR草图生成3D形状以提升几何保真度**

**关键词**: `VR草图生成` `3D形状重建` `顺序建模` `扩散模型` `多类别数据集`

## 📋 核心要点

1. 现有草图到形状模型忽略笔画顺序，丢失结构信息
2. 引入顺序感知编码器与扩散生成器，构建多类别数据集
3. 实验显示高几何保真度，能泛化到真实草图并处理部分草图

## 📄 摘要（原文）

> VR sketching lets users explore and iterate on ideas directly in 3D, offering a faster and more intuitive alternative to conventional CAD tools. However, existing sketch-to-shape models ignore the temporal ordering of strokes, discarding crucial cues about structure and design intent. We introduce VRSketch2Shape, the first framework and multi-category dataset for generating 3D shapes from sequential VR sketches. Our contributions are threefold: (i) an automated pipeline that generates sequential VR sketches from arbitrary shapes, (ii) a dataset of over 20k synthetic and 900 hand-drawn sketch-shape pairs across four categories, and (iii) an order-aware sketch encoder coupled with a diffusion-based 3D generator. Our approach yields higher geometric fidelity than prior work, generalizes effectively from synthetic to real sketches with minimal supervision, and performs well even on partial sketches. All data and models will be released open-source at https://chenyizi086.github.io/VRSketch2Shape_website.

