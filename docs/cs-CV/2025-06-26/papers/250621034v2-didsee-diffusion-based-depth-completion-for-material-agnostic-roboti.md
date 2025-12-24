---
layout: default
title: "DidSee: Diffusion-Based Depth Completion for Material-Agnostic Robotic Perception and Manipulation"
---

# DidSee: Diffusion-Based Depth Completion for Material-Agnostic Robotic Perception and Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21034" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21034v2</a>
  <a href="https://arxiv.org/pdf/2506.21034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21034v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21034v2', 'DidSee: Diffusion-Based Depth Completion for Material-Agnostic Robotic Perception and Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenzhou Lyu, Jialing Lin, Wenqi Ren, Ruihao Xia, Feng Qian, Yang Tang

**分类**: cs.CV

**发布日期**: 2025-06-26 (更新: 2025-06-27)

**备注**: Project page: https://wenzhoulyu.github.io/DidSee/

---

## 💡 一句话要点

**提出DidSee以解决非朗伯物体的深度补全问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `深度补全` `扩散模型` `非朗伯物体` `机器人感知` `语义分割` `噪声调度` `任务特定损失` `机器学习`

## 📋 核心要点

1. 现有的深度补全方法在处理非朗伯物体时，因训练数据的多样性不足而难以泛化，导致性能不佳。
2. 本文提出DidSee框架，通过引入新的噪声调度器和无噪声训练方案，解决了信号泄漏和误差累积问题。
3. DidSee在多个基准测试中实现了最先进的性能，显著提升了类别级姿态估计和机器人抓取等下游任务的效果。

## 📝 摘要（中文）

商业RGB-D相机在处理非朗伯物体时常常产生噪声和不完整的深度图。传统的深度补全方法由于训练数据的多样性和规模有限，难以实现良好的泛化。为了解决这一问题，本文提出了DidSee，一个基于扩散模型的深度补全框架。通过引入重新缩放的噪声调度器和无噪声单步训练方案，DidSee有效消除了信号泄漏偏差，并优化了模型。此外，结合语义增强模块，DidSee能够实现深度补全与语义分割的联合，生成精确的深度图。实验结果表明，DidSee在多个基准测试中表现出色，具有良好的现实世界泛化能力，并显著提升了下游任务的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决商业RGB-D相机在处理非朗伯物体时产生的噪声和不完整深度图的问题。现有方法由于训练数据的多样性和规模有限，难以实现有效的深度补全。

**核心思路**：DidSee框架通过引入重新缩放的噪声调度器和无噪声单步训练方案，消除了信号泄漏偏差，并优化了模型的训练过程，以提高深度补全的精度。

**技术框架**：DidSee的整体架构包括三个主要模块：噪声调度器、无噪声训练模块和语义增强模块。噪声调度器用于控制信号与噪声的比例，无噪声训练模块则通过特定损失函数优化模型，语义增强模块实现深度补全与语义分割的联合。

**关键创新**：DidSee的主要创新在于引入了重新缩放的噪声调度器和无噪声单步训练方案，这与传统的扩散模型方法有本质区别，能够有效减少训练与推理之间的偏差。

**关键设计**：在参数设置上，DidSee采用了零终端信噪比的噪声调度器，并设计了任务特定的损失函数以优化模型性能。此外，语义增强模块通过对背景与物体的区分，提升了深度图的精细度。

## 📊 实验亮点

在多个基准测试中，DidSee实现了最先进的性能，相较于现有方法，深度补全精度提升了XX%，在类别级姿态估计和机器人抓取任务中表现尤为突出，展示了良好的现实世界泛化能力。

## 🎯 应用场景

DidSee框架在机器人感知和操作领域具有广泛的应用潜力，尤其是在处理复杂环境中的非朗伯物体时。其精确的深度补全能力可以显著提升机器人在抓取、导航和交互等任务中的表现，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Commercial RGB-D cameras often produce noisy, incomplete depth maps for non-Lambertian objects. Traditional depth completion methods struggle to generalize due to the limited diversity and scale of training data. Recent advances exploit visual priors from pre-trained text-to-image diffusion models to enhance generalization in dense prediction tasks. However, we find that biases arising from training-inference mismatches in the vanilla diffusion framework significantly impair depth completion performance. Additionally, the lack of distinct visual features in non-Lambertian regions further hinders precise prediction. To address these issues, we propose \textbf{DidSee}, a diffusion-based framework for depth completion on non-Lambertian objects. First, we integrate a rescaled noise scheduler enforcing a zero terminal signal-to-noise ratio to eliminate signal leakage bias. Second, we devise a noise-agnostic single-step training formulation to alleviate error accumulation caused by exposure bias and optimize the model with a task-specific loss. Finally, we incorporate a semantic enhancer that enables joint depth completion and semantic segmentation, distinguishing objects from backgrounds and yielding precise, fine-grained depth maps. DidSee achieves state-of-the-art performance on multiple benchmarks, demonstrates robust real-world generalization, and effectively improves downstream tasks such as category-level pose estimation and robotic grasping.

