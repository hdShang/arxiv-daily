---
layout: default
title: Adaptive Knowledge Transferring with Switching Dual-Student Framework for Semi-Supervised Medical Image Segmentation
---

# Adaptive Knowledge Transferring with Switching Dual-Student Framework for Semi-Supervised Medical Image Segmentation

**arXiv**: [2510.24366v1](https://arxiv.org/abs/2510.24366) | [PDF](https://arxiv.org/pdf/2510.24366.pdf)

**作者**: Thanh-Huy Nguyen, Hoang-Thien Nguyen, Ba-Thinh Lam, Vi Vu, Bach X. Nguyen, Jianhua Xing, Tianyang Wang, Xingjian Li, Min Xu

---

## 💡 一句话要点

**提出切换双学生框架以解决半监督医学图像分割中知识传递不可靠问题**

**关键词**: `半监督学习` `医学图像分割` `教师-学生框架` `双学生架构` `知识传递` `伪标签优化`

## 📋 核心要点

1. 核心问题：教师-学生框架中强相关性和不可靠知识传递限制学习效果
2. 方法要点：引入切换双学生架构和损失感知指数移动平均策略
3. 实验或效果：在3D医学图像数据集上优于现有半监督方法，提升分割精度

## 📄 摘要（原文）

> Teacher-student frameworks have emerged as a leading approach in
> semi-supervised medical image segmentation, demonstrating strong performance
> across various tasks. However, the learning effects are still limited by the
> strong correlation and unreliable knowledge transfer process between teacher
> and student networks. To overcome this limitation, we introduce a novel
> switching Dual-Student architecture that strategically selects the most
> reliable student at each iteration to enhance dual-student collaboration and
> prevent error reinforcement. We also introduce a strategy of Loss-Aware
> Exponential Moving Average to dynamically ensure that the teacher absorbs
> meaningful information from students, improving the quality of pseudo-labels.
> Our plug-and-play framework is extensively evaluated on 3D medical image
> segmentation datasets, where it outperforms state-of-the-art semi-supervised
> methods, demonstrating its effectiveness in improving segmentation accuracy
> under limited supervision.

