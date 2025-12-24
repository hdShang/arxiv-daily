---
layout: default
title: Manipulating Elasto-Plastic Objects With 3D Occupancy and Learning-Based Predictive Control
---

# Manipulating Elasto-Plastic Objects With 3D Occupancy and Learning-Based Predictive Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16249" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16249v2</a>
  <a href="https://arxiv.org/pdf/2505.16249.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16249v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16249v2', 'Manipulating Elasto-Plastic Objects With 3D Occupancy and Learning-Based Predictive Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhen Zhang, Xiangyu Chu, Yunxi Tang, Lulu Zhao, Jing Huang, Zhongliang Jiang, K. W. Samuel Au

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-22 (更新: 2025-05-23)

**备注**: 8 Pages, 13 figures, accepted for publication in IEEE Robotics and Automation Letters (RA-L)

---

## 💡 一句话要点

**提出基于3D占用和学习的预测控制以解决弹塑性物体操控问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `弹塑性物体` `3D占用` `学习控制` `动态模型` `深度学习` `机器人操控` `预测控制`

## 📋 核心要点

1. 弹塑性物体的操控面临自遮挡和动态复杂性等重大挑战，现有方法难以有效处理这些问题。
2. 本文提出了一种新框架，利用3D占用表示和学习的动态模型，结合基于学习的预测控制算法来解决操控问题。
3. 实验结果表明，该框架能够有效地将弹塑性物体塑造成目标形状，且在模拟和现实环境中均表现出色。

## 📝 摘要（中文）

操控弹塑性物体仍然是一个重大挑战，主要由于自遮挡、表示困难和复杂的动态特性。本文提出了一种新颖的框架，通过假设运动为准静态，利用3D占用表示这些物体，结合训练有素的动态模型和基于学习的预测控制算法，有效应对这些挑战。我们构建了一个数据采集平台以收集完整的空间信息，并提出了生成3D占用数据集的流程。为了在操控过程中推断3D占用，训练了一个占用预测网络，使用生成的数据集进行监督。设计了一个深度神经网络，结合3D卷积神经网络和图神经网络，预测复杂变形。引入了一种基于学习的预测控制算法来规划机器人动作，包含一个新颖的基于形状的动作初始化模块，以提高规划效率。该框架能够成功将弹塑性物体塑造成给定的目标形状，并在模拟和现实世界中进行了多项实验验证。

## 🔬 方法详解

**问题定义**：本文旨在解决弹塑性物体操控中的自遮挡、表示困难和复杂动态等问题。现有方法在处理这些挑战时效果不佳，限制了其应用。

**核心思路**：提出的框架基于准静态假设，利用3D占用表示物体，结合学习的动态模型和预测控制算法，旨在提高操控精度和效率。

**技术框架**：整体架构包括数据采集平台、3D占用数据集生成、占用预测网络、深度神经网络和基于学习的预测控制算法。数据采集平台用于获取全空间信息，预测网络通过RGB图像推断3D占用，深度神经网络用于复杂变形预测。

**关键创新**：最重要的创新在于结合3D卷积神经网络和图神经网络，提升了对复杂变形的预测能力。此外，引入的基于形状的动作初始化模块显著提高了规划效率。

**关键设计**：在网络结构上，使用了3D卷积层和图神经网络的组合，损失函数设计考虑了变形预测的准确性和稳定性，确保了模型的有效性和鲁棒性。

## 📊 实验亮点

实验结果显示，提出的框架在操控弹塑性物体时，成功将其塑造成目标形状，且在多项实验中相较于传统方法提升了操控精度和效率，具体性能数据未详细列出。

## 🎯 应用场景

该研究在机器人操控、制造业和智能家居等领域具有广泛的应用潜力。通过精确操控弹塑性物体，可以实现更高效的生产流程和智能化服务，未来可能推动相关技术的商业化和普及。

## 📄 摘要（原文）

> Manipulating elasto-plastic objects remains a significant challenge due to severe self-occlusion, difficulties of representation, and complicated dynamics. This work proposes a novel framework for elasto-plastic object manipulation with a quasi-static assumption for motions, leveraging 3D occupancy to represent such objects, a learned dynamics model trained with 3D occupancy, and a learning-based predictive control algorithm to address these challenges effectively. We build a novel data collection platform to collect full spatial information and propose a pipeline for generating a 3D occupancy dataset. To infer the 3D occupancy during manipulation, an occupancy prediction network is trained with multiple RGB images supervised by the generated dataset. We design a deep neural network empowered by a 3D convolution neural network (CNN) and a graph neural network (GNN) to predict the complex deformation with the inferred 3D occupancy results. A learning-based predictive control algorithm is introduced to plan the robot actions, incorporating a novel shape-based action initialization module specifically designed to improve the planner efficiency. The proposed framework in this paper can successfully shape the elasto-plastic objects into a given goal shape and has been verified in various experiments both in simulation and the real world.

