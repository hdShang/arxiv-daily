---
layout: default
title: Consistent Instance Field for Dynamic Scene Understanding
---

# Consistent Instance Field for Dynamic Scene Understanding

**arXiv**: [2512.14126v1](https://arxiv.org/abs/2512.14126) | [PDF](https://arxiv.org/pdf/2512.14126.pdf)

**作者**: Junyi Wu, Van Nguyen Nguyen, Benjamin Planche, Jiachen Tao, Changchang Sun, Zhongpai Gao, Zhenghao Zhao, Anwesa Choudhuri, Gengyu Zhang, Meng Zheng, Feiran Wang, Terrence Chen, Yan Yan, Ziyan Wu

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出一致实例场以解决动态场景理解中离散跟踪和视角依赖特征的不足，实现连续时空表示。**

**关键词**: `动态场景理解` `一致实例场` `可变形3D高斯` `新视角全景分割` `开放词汇查询` `时空表示` `实例嵌入` `可微分光栅化`

## 📋 核心要点

1. 核心问题：现有动态场景理解方法依赖离散跟踪或视角依赖特征，难以实现跨时空的一致对象身份表示。
2. 方法要点：提出一致实例场，基于可变形3D高斯建模占用概率和实例分布，解耦可见性与对象身份。
3. 实验或效果：在HyperNeRF和Neu3D数据集上，新视角全景分割和开放词汇4D查询任务性能显著提升。

## 📝 摘要（中文）

我们引入了“一致实例场”，这是一种用于动态场景理解的连续且概率性的时空表示。与先前依赖离散跟踪或视角依赖特征的方法不同，我们的方法通过为每个时空点建模占用概率和条件实例分布，将可见性与持久对象身份解耦。为实现这一点，我们引入了一种基于可变形3D高斯的新型实例嵌入表示，该表示联合编码辐射度和语义信息，并通过可微分光栅化直接从输入RGB图像和实例掩码中学习。此外，我们引入了新机制来校准每个高斯的身份，并向语义活跃区域重新采样高斯，确保跨空间和时间的一致实例表示。在HyperNeRF和Neu3D数据集上的实验表明，我们的方法在新视角全景分割和开放词汇4D查询任务上显著优于最先进的方法。

## 🔬 方法详解

整体框架基于可变形3D高斯，构建连续时空表示。关键技术创新点包括：实例嵌入表示联合编码辐射度和语义信息，通过可微分光栅化从RGB图像和实例掩码直接学习；引入校准机制和重采样策略，确保高斯身份一致并聚焦语义活跃区域。与现有方法的主要区别在于，它避免了离散跟踪，提供概率性表示，实现跨视角和时间的对象身份一致性。

## 📊 实验亮点

在HyperNeRF和Neu3D数据集上，新视角全景分割和开放词汇4D查询任务中，性能显著优于最先进方法，验证了一致实例场在动态场景理解中的有效性。

## 🎯 应用场景

该研究可应用于自动驾驶、机器人导航和增强现实等领域，支持动态场景的实时理解和交互，如新视角全景分割和开放词汇查询，提升环境感知和决策能力。

## 📄 摘要（原文）

> We introduce Consistent Instance Field, a continuous and probabilistic spatio-temporal representation for dynamic scene understanding. Unlike prior methods that rely on discrete tracking or view-dependent features, our approach disentangles visibility from persistent object identity by modeling each space-time point with an occupancy probability and a conditional instance distribution. To realize this, we introduce a novel instance-embedded representation based on deformable 3D Gaussians, which jointly encode radiance and semantic information and are learned directly from input RGB images and instance masks through differentiable rasterization. Furthermore, we introduce new mechanisms to calibrate per-Gaussian identities and resample Gaussians toward semantically active regions, ensuring consistent instance representations across space and time. Experiments on HyperNeRF and Neu3D datasets demonstrate that our method significantly outperforms state-of-the-art methods on novel-view panoptic segmentation and open-vocabulary 4D querying tasks.

