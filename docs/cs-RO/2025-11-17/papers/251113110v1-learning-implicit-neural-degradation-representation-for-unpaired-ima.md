---
layout: default
title: Learning Implicit Neural Degradation Representation for Unpaired Image Dehazing
---

# Learning Implicit Neural Degradation Representation for Unpaired Image Dehazing

**arXiv**: [2511.13110v1](https://arxiv.org/abs/2511.13110) | [PDF](https://arxiv.org/pdf/2511.13110.pdf)

**作者**: Shuaibin Fan, Senming Zhong, Wenchao Yan, Minglong Xue

---

## 💡 一句话要点

**提出隐式神经退化表示方法以解决无配对图像去雾中非均匀雾分布建模问题**

**关键词**: `图像去雾` `隐式神经表示` `无监督学习` `非线性依赖` `残差增强`

## 📋 核心要点

1. 核心问题：现有方法难以平衡非均匀雾分布的细粒度特征与全局一致性建模
2. 方法要点：结合通道独立与依赖机制，设计隐式神经表示建模雾退化连续函数
3. 实验或效果：在公共和真实数据集上实现竞争性去雾性能，代码开源

## 📄 摘要（原文）

> Image dehazing is an important task in the field of computer vision, aiming at restoring clear and detail-rich visual content from haze-affected images. However, when dealing with complex scenes, existing methods often struggle to strike a balance between fine-grained feature representation of inhomogeneous haze distribution and global consistency modeling. Furthermore, to better learn the common degenerate representation of haze in spatial variations, we propose an unsupervised dehaze method for implicit neural degradation representation. Firstly, inspired by the Kolmogorov-Arnold representation theorem, we propose a mechanism combining the channel-independent and channel-dependent mechanisms, which efficiently enhances the ability to learn from nonlinear dependencies. which in turn achieves good visual perception in complex scenes. Moreover, we design an implicit neural representation to model haze degradation as a continuous function to eliminate redundant information and the dependence on explicit feature extraction and physical models. To further learn the implicit representation of the haze features, we also designed a dense residual enhancement module from it to eliminate redundant information. This achieves high-quality image restoration. Experimental results show that our method achieves competitive dehaze performance on various public and real-world datasets. This project code will be available at https://github.com/Fan-pixel/NeDR-Dehaze.

