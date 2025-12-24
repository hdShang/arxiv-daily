---
layout: default
title: "ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical Gaussian World Model"
---

# ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical Gaussian World Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19842" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19842v1</a>
  <a href="https://arxiv.org/pdf/2506.19842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19842v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19842v1', 'ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical Gaussian World Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-24

**🔗 代码/项目**: [GITHUB](https://github.com/April-Yz/ManiGaussian_Bimanual)

---

## 💡 一句话要点

**提出ManiGaussian++以解决双臂机器人多任务操控问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `双臂操控` `高斯模型` `多任务学习` `机器人技术` `时空动态`

## 📋 核心要点

1. 现有方法在双臂操控中忽视了多体交互，导致性能显著下降，无法有效处理复杂的时空动态。
2. 本文提出ManiGaussian++，通过分层高斯世界模型和任务导向的高斯点云来建模多体时空动态，提升双臂操控能力。
3. 实验结果显示，ManiGaussian++在10个模拟任务中性能提升20.2%，在9个真实任务中平均成功率达到60%。

## 📝 摘要（中文）

多任务机器人双臂操控日益受到关注，因为它能够实现需要复杂双臂协作模式的精细任务。现有的ManiGaussian方法在单臂设置中开创性地将时空动态编码为视觉表示，但在双臂系统中忽视了多体交互，导致性能显著下降。本文提出ManiGaussian++，通过分层高斯世界模型来改进多任务双臂操控，具体通过生成任务导向的高斯点云来区分作用臂和稳定臂，并建立领导-跟随架构以挖掘多体时空动态。实验结果表明，该方法在10个模拟任务中提升了20.2%的性能，并在9个具有挑战性的真实任务中平均成功率达到60%。

## 🔬 方法详解

**问题定义**：本文旨在解决双臂机器人多任务操控中的时空动态建模问题。现有的ManiGaussian方法在单臂设置中表现良好，但在双臂系统中由于忽视多体交互，导致性能显著下降。

**核心思路**：论文提出的核心思路是通过分层高斯世界模型来捕捉多体场景的动态特征，特别是区分作用臂和稳定臂的功能，以更好地理解和预测双臂操控中的时空动态。

**技术框架**：整体架构包括生成任务导向的高斯点云和建立领导-跟随架构。领导臂负责预测稳定臂运动引起的高斯点云变形，跟随臂则基于此生成作用臂运动的物理后果。

**关键创新**：最重要的技术创新在于引入了分层高斯世界模型和领导-跟随架构，使得多体时空动态的建模更加精确，显著提升了双臂操控的性能。

**关键设计**：在设计中，任务导向的高斯点云生成是关键步骤，此外，模型的损失函数和网络结构经过精心调整，以确保对多体动态的有效捕捉和预测。

## 📊 实验亮点

实验结果显示，ManiGaussian++在10个模拟任务中相比现有技术提升了20.2%的性能，并在9个具有挑战性的真实任务中实现了60%的平均成功率，展现了其在双臂操控中的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景，能够提升机器人在复杂环境中的操作能力和灵活性。未来，ManiGaussian++有望在更广泛的多任务操控应用中发挥重要作用，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Multi-task robotic bimanual manipulation is becoming increasingly popular as it enables sophisticated tasks that require diverse dual-arm collaboration patterns. Compared to unimanual manipulation, bimanual tasks pose challenges to understanding the multi-body spatiotemporal dynamics. An existing method ManiGaussian pioneers encoding the spatiotemporal dynamics into the visual representation via Gaussian world model for single-arm settings, which ignores the interaction of multiple embodiments for dual-arm systems with significant performance drop. In this paper, we propose ManiGaussian++, an extension of ManiGaussian framework that improves multi-task bimanual manipulation by digesting multi-body scene dynamics through a hierarchical Gaussian world model. To be specific, we first generate task-oriented Gaussian Splatting from intermediate visual features, which aims to differentiate acting and stabilizing arms for multi-body spatiotemporal dynamics modeling. We then build a hierarchical Gaussian world model with the leader-follower architecture, where the multi-body spatiotemporal dynamics is mined for intermediate visual representation via future scene prediction. The leader predicts Gaussian Splatting deformation caused by motions of the stabilizing arm, through which the follower generates the physical consequences resulted from the movement of the acting arm. As a result, our method significantly outperforms the current state-of-the-art bimanual manipulation techniques by an improvement of 20.2% in 10 simulated tasks, and achieves 60% success rate on average in 9 challenging real-world tasks. Our code is available at https://github.com/April-Yz/ManiGaussian_Bimanual.

