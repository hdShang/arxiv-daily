---
layout: default
title: Robust Alignment of the Human Embryo in 3D Ultrasound using PCA and an Ensemble of Heuristic, Atlas-based and Learning-based Classifiers Evaluated on the Rotterdam Periconceptional Cohort
---

# Robust Alignment of the Human Embryo in 3D Ultrasound using PCA and an Ensemble of Heuristic, Atlas-based and Learning-based Classifiers Evaluated on the Rotterdam Periconceptional Cohort

**arXiv**: [2511.03416v1](https://arxiv.org/abs/2511.03416) | [PDF](https://arxiv.org/pdf/2511.03416.pdf)

**作者**: Nikolai Herrmann, Marcella C. Zijta, Stefan Klein, Régine P. M. Steegers-Theunissen, Rene M. H. Wijnen, Bernadette S. de Bakker, Melek Rousian, Wietske A. P. Bastiaansen

---

## 💡 一句话要点

**提出基于PCA和分类器集成的方法，实现人类胚胎在3D超声中的标准化对齐。**

**关键词**: `3D超声对齐` `主成分分析` `分类器集成` `胚胎标准化` `产前监测`

## 📋 核心要点

1. 核心问题：3D超声图像中胚胎对齐标准化，以辅助产前生长监测和标准平面检测。
2. 方法要点：使用PCA提取胚胎主轴，结合启发式、图谱和随机森林分类器选择标准方向。
3. 实验效果：在2166张图像上测试，多数投票方法准确率达98.5%，代码已公开。

## 📄 摘要（原文）

> Standardized alignment of the embryo in three-dimensional (3D) ultrasound
> images aids prenatal growth monitoring by facilitating standard plane
> detection, improving visualization of landmarks and accentuating differences
> between different scans. In this work, we propose an automated method for
> standardizing this alignment. Given a segmentation mask of the embryo,
> Principal Component Analysis (PCA) is applied to the mask extracting the
> embryo's principal axes, from which four candidate orientations are derived.
> The candidate in standard orientation is selected using one of three
> strategies: a heuristic based on Pearson's correlation assessing shape, image
> matching to an atlas through normalized cross-correlation, and a Random Forest
> classifier. We tested our method on 2166 images longitudinally acquired 3D
> ultrasound scans from 1043 pregnancies from the Rotterdam Periconceptional
> Cohort, ranging from 7+0 to 12+6 weeks of gestational age. In 99.0% of images,
> PCA correctly extracted the principal axes of the embryo. The correct candidate
> was selected by the Pearson Heuristic, Atlas-based and Random Forest in 97.4%,
> 95.8%, and 98.4% of images, respectively. A Majority Vote of these selection
> methods resulted in an accuracy of 98.5%. The high accuracy of this pipeline
> enables consistent embryonic alignment in the first trimester, enabling
> scalable analysis in both clinical and research settings. The code is publicly
> available at:
> https://gitlab.com/radiology/prenatal-image-analysis/pca-3d-alignment.

