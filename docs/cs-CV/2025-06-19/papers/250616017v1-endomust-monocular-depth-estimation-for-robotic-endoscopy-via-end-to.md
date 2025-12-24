---
layout: default
title: "EndoMUST: Monocular Depth Estimation for Robotic Endoscopy via End-to-end Multi-step Self-supervised Training"
---

# EndoMUST: Monocular Depth Estimation for Robotic Endoscopy via End-to-end Multi-step Self-supervised Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16017" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16017v1</a>
  <a href="https://arxiv.org/pdf/2506.16017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16017v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16017v1', 'EndoMUST: Monocular Depth Estimation for Robotic Endoscopy via End-to-end Multi-step Self-supervised Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liangjing Shao, Linxin Bai, Chenkang Du, Xinrong Chen

**分类**: cs.CV, cs.RO

**发布日期**: 2025-06-19

**备注**: Accepted by IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/BaymaxShao/EndoMUST)

---

## 💡 一句话要点

**提出EndoMUST以解决机器人内窥镜中的单目深度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `单目深度估计` `自我监督学习` `机器人内窥镜` `光流配准` `多尺度图像分解` `深度学习` `图像处理`

## 📋 核心要点

1. 现有方法在内窥镜场景中面临光照变化和稀疏纹理的挑战，影响深度估计的准确性。
2. 本文提出了一种多步高效微调的框架，通过分步骤训练相关网络，减少信息干扰。
3. 在SCARED数据集上，所提方法实现了自我监督深度估计的最新性能，误差降低4%至10%。

## 📝 摘要（中文）

单目深度估计和自我运动估计是机器人辅助内窥镜中场景感知和导航的重要任务。为应对内窥镜场景中的光照变化和稀疏纹理，现有方法引入了光流、外观流和内在图像分解等多种技术。然而，针对多个模块的有效训练策略仍然是解决光照问题和信息干扰的关键。本文提出了一种新颖的多步高效微调框架，在每个端到端训练的周期中，将过程分为光流配准、多尺度图像分解和多重变换对齐三个步骤。每一步仅训练相关网络，避免无关信息的干扰。基于对基础模型的参数高效微调，所提方法在SCARED数据集上实现了自我监督深度估计的最新性能，并在Hamlyn数据集上实现了零-shot深度估计，误差降低了4%至10%。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人内窥镜中的单目深度估计问题，现有方法在光照变化和稀疏纹理下表现不佳，导致深度估计不准确。

**核心思路**：提出了一种多步高效微调的训练策略，通过将训练过程分为光流配准、多尺度图像分解和多重变换对齐三个步骤，确保每一步只关注相关网络，减少信息干扰。

**技术框架**：整体架构包括三个主要模块：光流配准用于对齐图像，接着进行多尺度图像分解以提取不同层次的特征，最后通过多重变换对齐来增强特征的一致性。

**关键创新**：最重要的创新在于采用多步训练策略，允许在每个步骤中专注于特定任务，从而提高了自我监督深度估计的准确性，区别于传统方法的单一训练流程。

**关键设计**：在训练过程中，采用了参数高效微调的策略，设计了适应性损失函数，以优化每个模块的性能，同时确保网络结构能够有效处理内窥镜图像的特征。

## 📊 实验亮点

实验结果表明，所提方法在SCARED数据集上实现了自我监督深度估计的最新性能，相较于现有基线，误差降低了4%至10%。在Hamlyn数据集上，方法还实现了零-shot深度估计，进一步验证了其有效性。

## 🎯 应用场景

该研究在机器人辅助内窥镜领域具有重要应用潜力，能够提升内窥镜手术中的深度感知能力，进而提高手术的安全性和准确性。未来，该方法还可扩展到其他需要深度估计的医疗影像分析领域，具有广泛的实际价值。

## 📄 摘要（原文）

> Monocular depth estimation and ego-motion estimation are significant tasks for scene perception and navigation in stable, accurate and efficient robot-assisted endoscopy. To tackle lighting variations and sparse textures in endoscopic scenes, multiple techniques including optical flow, appearance flow and intrinsic image decomposition have been introduced into the existing methods. However, the effective training strategy for multiple modules are still critical to deal with both illumination issues and information interference for self-supervised depth estimation in endoscopy. Therefore, a novel framework with multistep efficient finetuning is proposed in this work. In each epoch of end-to-end training, the process is divided into three steps, including optical flow registration, multiscale image decomposition and multiple transformation alignments. At each step, only the related networks are trained without interference of irrelevant information. Based on parameter-efficient finetuning on the foundation model, the proposed method achieves state-of-the-art performance on self-supervised depth estimation on SCARED dataset and zero-shot depth estimation on Hamlyn dataset, with 4\%$\sim$10\% lower error. The evaluation code of this work has been published on https://github.com/BaymaxShao/EndoMUST.

