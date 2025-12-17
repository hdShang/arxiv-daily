---
layout: default
title: OpenVE-3M: A Large-Scale High-Quality Dataset for Instruction-Guided Video Editing
---

# OpenVE-3M: A Large-Scale High-Quality Dataset for Instruction-Guided Video Editing

**arXiv**: [2512.07826v1](https://arxiv.org/abs/2512.07826) | [PDF](https://arxiv.org/pdf/2512.07826.pdf)

**作者**: Haoyang He, Jie Wang, Jiangning Zhang, Zhucun Xue, Xingyuan Bu, Qiangpeng Yang, Shilei Wen, Lei Xie

---

## 💡 一句话要点

**提出OpenVE-3M数据集以解决指令引导视频编辑领域缺乏大规模高质量数据的问题**

**关键词**: `指令引导视频编辑` `大规模数据集` `视频编辑基准` `空间对齐编辑` `非空间对齐编辑` `质量过滤`

## 📋 核心要点

1. 核心问题：指令引导视频编辑领域缺乏大规模、高质量数据集，阻碍模型发展。
2. 方法要点：构建OpenVE-3M数据集，包含空间对齐和非空间对齐编辑类型，通过精心设计的数据管道和质量过滤确保质量。
3. 实验或效果：基于数据集训练OpenVE-Edit模型，在OpenVE-Bench基准上超越所有开源模型，包括14B基线。

## 📄 摘要（原文）

> The quality and diversity of instruction-based image editing datasets are continuously increasing, yet large-scale, high-quality datasets for instruction-based video editing remain scarce. To address this gap, we introduce OpenVE-3M, an open-source, large-scale, and high-quality dataset for instruction-based video editing. It comprises two primary categories: spatially-aligned edits (Global Style, Background Change, Local Change, Local Remove, Local Add, and Subtitles Edit) and non-spatially-aligned edits (Camera Multi-Shot Edit and Creative Edit). All edit types are generated via a meticulously designed data pipeline with rigorous quality filtering. OpenVE-3M surpasses existing open-source datasets in terms of scale, diversity of edit types, instruction length, and overall quality. Furthermore, to address the lack of a unified benchmark in the field, we construct OpenVE-Bench, containing 431 video-edit pairs that cover a diverse range of editing tasks with three key metrics highly aligned with human judgment. We present OpenVE-Edit, a 5B model trained on our dataset that demonstrates remarkable efficiency and effectiveness by setting a new state-of-the-art on OpenVE-Bench, outperforming all prior open-source models including a 14B baseline. Project page is at https://github.com/lewandofskee/OpenVE.

