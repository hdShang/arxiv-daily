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

🎯 **匹配领域**: **视觉里程计**

**关键词**: `动态场景理解` `一致实例场` `可变形3D高斯` `新视角全景分割` `开放词汇4D查询` `时空表示` `实例嵌入` `可微分光栅化`

## 📋 核心要点

1. 现有方法依赖离散跟踪或视角依赖特征，难以实现动态场景中对象身份的连续一致表示。
2. 提出一致实例场，基于可变形3D高斯建模时空点，解耦可见性与对象身份，并通过校准和重采样机制优化表示。
3. 在HyperNeRF和Neu3D数据集上，新视角全景分割和开放词汇4D查询任务性能显著提升，超越现有方法。

## 📝 摘要（中文）

我们引入了“一致实例场”，这是一种用于动态场景理解的连续且概率性的时空表示。与先前依赖离散跟踪或视角依赖特征的方法不同，我们的方法通过为每个时空点建模占用概率和条件实例分布，将可见性与持久对象身份解耦。为实现这一点，我们引入了一种基于可变形3D高斯的新型实例嵌入表示，该表示联合编码辐射度和语义信息，并通过可微分光栅化直接从输入RGB图像和实例掩码中学习。此外，我们引入了新机制来校准每个高斯的身份，并向语义活跃区域重新采样高斯，确保跨空间和时间的一致实例表示。在HyperNeRF和Neu3D数据集上的实验表明，我们的方法在新视角全景分割和开放词汇4D查询任务上显著优于最先进的方法。

## 🔬 方法详解

整体框架基于可变形3D高斯构建一致实例场，每个高斯编码辐射度和语义信息，通过可微分光栅化从RGB图像和实例掩码学习。关键技术创新包括：引入实例嵌入表示以联合建模对象身份和可见性；设计校准机制确保高斯身份一致性；实施重采样策略聚焦语义活跃区域。与现有方法的主要区别在于：避免了离散跟踪的局限性，提供连续概率表示；通过解耦设计增强时空一致性，而非依赖视角依赖特征。

## 📊 实验亮点

在HyperNeRF和Neu3D数据集上，新视角全景分割任务中准确率显著提高，开放词汇4D查询任务表现优异，验证了方法在动态场景理解中的有效性和鲁棒性，超越现有最先进方法。

## 🎯 应用场景

该研究可应用于自动驾驶、机器人导航和增强现实等领域，通过动态场景的连续理解，支持实时对象跟踪、环境交互和沉浸式体验，提升智能系统的感知和决策能力。

## 📄 摘要（原文）

> We introduce Consistent Instance Field, a continuous and probabilistic spatio-temporal representation for dynamic scene understanding. Unlike prior methods that rely on discrete tracking or view-dependent features, our approach disentangles visibility from persistent object identity by modeling each space-time point with an occupancy probability and a conditional instance distribution. To realize this, we introduce a novel instance-embedded representation based on deformable 3D Gaussians, which jointly encode radiance and semantic information and are learned directly from input RGB images and instance masks through differentiable rasterization. Furthermore, we introduce new mechanisms to calibrate per-Gaussian identities and resample Gaussians toward semantically active regions, ensuring consistent instance representations across space and time. Experiments on HyperNeRF and Neu3D datasets demonstrate that our method significantly outperforms state-of-the-art methods on novel-view panoptic segmentation and open-vocabulary 4D querying tasks.

