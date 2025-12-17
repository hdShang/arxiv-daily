---
layout: default
title: More than Segmentation: Benchmarking SAM 3 for Segmentation, 3D Perception, and Reconstruction in Robotic Surgery
---

# More than Segmentation: Benchmarking SAM 3 for Segmentation, 3D Perception, and Reconstruction in Robotic Surgery

**arXiv**: [2512.07596v1](https://arxiv.org/abs/2512.07596) | [PDF](https://arxiv.org/pdf/2512.07596.pdf)

**作者**: Wenzhen Dong, Jieming Yu, Yiming Huang, Hongqiu Wang, Lei Zhu, Albert C. S. Chung, Hongliang Ren, Long Bai

---

## 💡 一句话要点

**评估SAM 3在机器人手术中的分割、3D感知与重建性能，揭示其在零样本分割和3D重建方面的优势与局限。**

**关键词**: `零样本分割` `3D重建` `机器人手术` `语言提示` `动态视频跟踪` `单目深度估计`

## 📋 核心要点

1. 核心问题：评估SAM 3在机器人手术场景下的零样本分割、动态视频跟踪和3D重建能力，以验证其实际应用潜力。
2. 方法要点：使用点、边界框和语言提示进行零样本分割测试，并基于2D图像进行3D解剖结构重建，结合多个手术数据集进行综合评估。
3. 实验或效果：在MICCAI EndoVis基准上，SAM 3在空间提示下的图像和视频分割优于前代模型；零样本评估显示其在单目深度估计和3D器械重建方面表现良好，但在复杂动态场景中仍有局限。

## 📄 摘要（原文）

> The recent Segment Anything Model (SAM) 3 has introduced significant advancements over its predecessor, SAM 2, particularly with the integration of language-based segmentation and enhanced 3D perception capabilities. SAM 3 supports zero-shot segmentation across a wide range of prompts, including point, bounding box, and language-based prompts, allowing for more flexible and intuitive interactions with the model. In this empirical evaluation, we assess the performance of SAM 3 in robot-assisted surgery, benchmarking its zero-shot segmentation with point and bounding box prompts and exploring its effectiveness in dynamic video tracking, alongside its newly introduced language prompt segmentation. While language prompts show potential, their performance in the surgical domain is currently suboptimal, highlighting the need for further domain-specific training. Additionally, we investigate SAM 3's 3D reconstruction abilities, demonstrating its capacity to process surgical scene data and reconstruct 3D anatomical structures from 2D images. Through comprehensive testing on the MICCAI EndoVis 2017 and EndoVis 2018 benchmarks, SAM 3 shows clear improvements over SAM and SAM 2 in both image and video segmentation under spatial prompts, while zero-shot evaluations on SCARED, StereoMIS, and EndoNeRF indicate strong monocular depth estimation and realistic 3D instrument reconstruction, yet also reveal remaining limitations in complex, highly dynamic surgical scenes.

