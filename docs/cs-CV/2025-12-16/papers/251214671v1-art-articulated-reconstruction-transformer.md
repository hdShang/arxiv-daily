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

**提出ART以解决从稀疏多状态RGB图像重建完整3D关节物体的问题，实现类别无关的前馈建模。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `关节物体重建` `3D重建` `Transformer架构` `前馈模型` `类别无关建模` `部件预测` `物理仿真` `稀疏图像输入`

## 📋 核心要点

1. 现有方法依赖缓慢优化或脆弱对应关系，或局限于特定类别，难以高效重建通用关节物体。
2. ART将关节物体建模为刚性部件组装，使用Transformer架构从稀疏图像预测部件几何、纹理和关节参数。
3. 在多样化数据集上训练和评估，ART显著超越基线，实现了类别无关的快速重建，并支持物理仿真。

## 📝 摘要（中文）

我们介绍了ART（Articulated Reconstruction Transformer），这是一个类别无关的前馈模型，能够仅从稀疏的多状态RGB图像中重建完整的3D关节物体。先前的方法要么依赖于缓慢的优化过程，需要脆弱的跨状态对应关系，要么使用仅限于特定物体类别的前馈模型。相比之下，ART将关节物体视为刚性部件的组装体，将重建问题表述为基于部件的预测。我们新设计的Transformer架构将稀疏图像输入映射到一组可学习的部件槽，ART从中联合解码出统一表示，包括每个部件的3D几何、纹理和显式关节参数。所得重建结果具有物理可解释性，并易于导出用于仿真。通过在具有每部件监督的大规模多样化数据集上进行训练，并在多个基准测试中评估，ART相比现有基线取得了显著改进，为从图像输入重建关节物体建立了新的最先进水平。

## 🔬 方法详解

ART的整体框架是一个基于Transformer的前馈模型，输入稀疏多状态RGB图像，输出关节物体的完整3D重建。关键技术创新包括：将重建任务分解为部件级预测，通过可学习部件槽统一编码几何、纹理和关节参数；新设计的Transformer架构直接映射图像到部件表示，避免了传统优化中的对应关系依赖。与现有方法的主要区别在于，ART是类别无关的，不依赖于特定物体先验，且通过前馈方式实现快速推理，同时保持物理可解释性。

## 📊 实验亮点

ART在多个基准测试中显著优于现有基线，实现了类别无关的关节物体重建，重建质量高且速度快，支持从稀疏图像直接生成可仿真模型，为相关领域树立了新标准。

## 🎯 应用场景

该研究在机器人操作、虚拟现实和增强现实中有广泛应用潜力，例如用于模拟真实世界物体的交互、自动化装配或游戏开发。其物理可解释的重建结果可直接导出用于仿真，提升系统效率和安全性。

## 📄 摘要（原文）

> We introduce ART, Articulated Reconstruction Transformer -- a category-agnostic, feed-forward model that reconstructs complete 3D articulated objects from only sparse, multi-state RGB images. Previous methods for articulated object reconstruction either rely on slow optimization with fragile cross-state correspondences or use feed-forward models limited to specific object categories. In contrast, ART treats articulated objects as assemblies of rigid parts, formulating reconstruction as part-based prediction. Our newly designed transformer architecture maps sparse image inputs to a set of learnable part slots, from which ART jointly decodes unified representations for individual parts, including their 3D geometry, texture, and explicit articulation parameters. The resulting reconstructions are physically interpretable and readily exportable for simulation. Trained on a large-scale, diverse dataset with per-part supervision, and evaluated across diverse benchmarks, ART achieves significant improvements over existing baselines and establishes a new state of the art for articulated object reconstruction from image inputs.

