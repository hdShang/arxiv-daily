---
layout: default
title: 2D Gaussians Spatial Transport for Point-supervised Density Regression
---

# 2D Gaussians Spatial Transport for Point-supervised Density Regression

**arXiv**: [2511.14477v1](https://arxiv.org/abs/2511.14477) | [PDF](https://arxiv.org/pdf/2511.14477.pdf)

**作者**: Miao Shang, Xiaopeng Hong

---

## 💡 一句话要点

**提出Gaussian Spatial Transport框架，利用高斯泼溅优化点监督密度回归任务。**

**关键词**: `高斯泼溅` `点监督密度回归` `最优传输` `人群计数` `地标检测`

## 📋 核心要点

1. 核心问题：点监督密度回归中图像坐标空间与标注图的概率度量传输效率低。
2. 方法要点：基于高斯泼溅估计像素-标注对应，推导贝叶斯概率传输计划。
3. 实验或效果：在人群计数和地标检测任务中验证有效性，消除训练中迭代计算。

## 📄 摘要（原文）

> This paper introduces Gaussian Spatial Transport (GST), a novel framework that leverages Gaussian splatting to facilitate transport from the probability measure in the image coordinate space to the annotation map. We propose a Gaussian splatting-based method to estimate pixel-annotation correspondence, which is then used to compute a transport plan derived from Bayesian probability. To integrate the resulting transport plan into standard network optimization in typical computer vision tasks, we derive a loss function that measures discrepancy after transport. Extensive experiments on representative computer vision tasks, including crowd counting and landmark detection, validate the effectiveness of our approach. Compared to conventional optimal transport schemes, GST eliminates iterative transport plan computation during training, significantly improving efficiency. Code is available at https://github.com/infinite0522/GST.

