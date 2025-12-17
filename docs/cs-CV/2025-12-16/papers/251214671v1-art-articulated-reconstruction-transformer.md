---
layout: default
title: ART: Articulated Reconstruction Transformer
---

# ART: Articulated Reconstruction Transformer

**arXiv**: [2512.14671v1](https://arxiv.org/abs/2512.14671) | [PDF](https://arxiv.org/pdf/2512.14671.pdf)

**作者**: Zizhang Li, Cheng Zhang, Zhengqin Li, Henry Howard-Jenkins, Zhaoyang Lv, Chen Geng, Jiajun Wu, Richard Newcombe, Jakob Engel, Zhao Dong

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project Page: https://kyleleey.github.io/ART/

---

## 💡 一句话要点

**提出ART以解决从稀疏多状态RGB图像重建完整3D关节物体的类别无关前馈建模问题**

**关键词**: `关节物体重建` `3D重建` `Transformer架构` `部件级预测` `类别无关建模` `前馈模型` `物理可解释性` `稀疏图像输入`

## 📋 核心要点

1. 现有方法依赖缓慢优化或局限于特定类别，难以高效重建多样化关节物体。
2. ART将关节物体建模为刚性部件组装体，通过Transformer架构实现部件级预测。
3. 在多个基准测试中，ART显著超越现有基线，建立了新的技术标杆。

## 📝 摘要（中文）

我们介绍了ART（Articulated Reconstruction Transformer）——一种类别无关的前馈模型，能够仅从稀疏的多状态RGB图像重建完整的3D关节物体。以往的关节物体重建方法要么依赖于脆弱的跨状态对应关系的缓慢优化，要么使用仅限于特定物体类别的前馈模型。相比之下，ART将关节物体视为刚性部件的组装体，将重建问题表述为基于部件的预测。我们新设计的Transformer架构将稀疏图像输入映射到一组可学习的部件槽，ART从中联合解码出各个部件的统一表示，包括其3D几何、纹理和显式关节参数。所得重建结果具有物理可解释性，并可轻松导出用于仿真。通过在具有逐部件监督的大规模多样化数据集上进行训练，并在多个基准测试中评估，ART相比现有基线取得了显著改进，为从图像输入进行关节物体重建建立了新的技术标杆。

## 🔬 方法详解

ART采用基于Transformer的前馈架构，整体框架将稀疏多状态RGB图像输入映射到一组可学习的部件槽，然后联合解码每个部件的3D几何、纹理和显式关节参数。关键技术创新在于将关节物体视为刚性部件组装体，并设计Transformer实现部件级预测，避免了传统方法对跨状态对应关系的依赖。与现有方法的主要区别在于其类别无关性和前馈特性，能够高效处理多样化物体，而无需缓慢优化或类别限制。

## 📊 实验亮点

ART在多个关节物体重建基准测试中显著超越现有基线，实现了更高的重建精度和效率，特别是在处理稀疏图像输入时表现出色，为相关任务建立了新的技术标杆。

## 🎯 应用场景

该研究在机器人操作、虚拟现实和仿真领域具有广泛应用价值，例如机器人抓取关节物体、虚拟环境中的物体交互模拟，以及增强现实中的实时物体重建，为物理可解释的3D建模提供了高效解决方案。

## 📄 摘要（原文）

> We introduce ART, Articulated Reconstruction Transformer -- a category-agnostic, feed-forward model that reconstructs complete 3D articulated objects from only sparse, multi-state RGB images. Previous methods for articulated object reconstruction either rely on slow optimization with fragile cross-state correspondences or use feed-forward models limited to specific object categories. In contrast, ART treats articulated objects as assemblies of rigid parts, formulating reconstruction as part-based prediction. Our newly designed transformer architecture maps sparse image inputs to a set of learnable part slots, from which ART jointly decodes unified representations for individual parts, including their 3D geometry, texture, and explicit articulation parameters. The resulting reconstructions are physically interpretable and readily exportable for simulation. Trained on a large-scale, diverse dataset with per-part supervision, and evaluated across diverse benchmarks, ART achieves significant improvements over existing baselines and establishes a new state of the art for articulated object reconstruction from image inputs.

