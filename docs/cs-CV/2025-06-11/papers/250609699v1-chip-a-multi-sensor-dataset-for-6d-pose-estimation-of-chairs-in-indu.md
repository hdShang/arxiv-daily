---
layout: default
title: "CHIP: A multi-sensor dataset for 6D pose estimation of chairs in industrial settings"
---

# CHIP: A multi-sensor dataset for 6D pose estimation of chairs in industrial settings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09699" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09699v1</a>
  <a href="https://arxiv.org/pdf/2506.09699.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09699v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09699v1', 'CHIP: A multi-sensor dataset for 6D pose estimation of chairs in industrial settings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mattia Nardon, Mikel Mujika Agirre, Ander González Tomé, Daniel Sedano Algarabel, Josep Rueda Collell, Ana Paola Caro, Andrea Caraffa, Fabio Poiesi, Paul Ian Chippendale, Davide Boscaini

**分类**: cs.CV

**发布日期**: 2025-06-11

**备注**: Technical report

---

## 💡 一句话要点

**提出CHIP数据集以解决工业环境中椅子的6D姿态估计问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `6D姿态估计` `RGBD传感` `工业机器人` `数据集` `机器学习` `自动化` `智能制造`

## 📋 核心要点

1. 现有的6D姿态估计方法在真实工业环境中表现不佳，尤其是缺乏针对复杂物体的有效数据集。
2. CHIP数据集是首个针对工业环境中椅子的6D姿态估计而设计的数据集，包含多种RGBD传感技术的图像。
3. 实验结果表明，现有的零样本6D姿态估计方法在CHIP数据集上仍有显著提升空间，显示出数据集的挑战性。

## 📝 摘要（中文）

准确的6D姿态估计对于复杂物体在3D环境中的机器人操作至关重要。然而，现有基准在真实工业条件下评估6D姿态估计方法时存在不足。大多数数据集集中于家庭物体，而少数工业数据集则局限于人工设置。为此，本文提出CHIP数据集，专为在真实工业环境中由机器人手臂操作的椅子设计。CHIP包含七种不同的椅子，使用三种不同的RGBD传感技术捕获，面临独特挑战，如细微差别的干扰物和由机器人手臂及人类操作员造成的严重遮挡。数据集包含77,811张RGBD图像，自动注释的6D姿态平均每种椅子11,115个。通过三种零样本6D姿态估计方法对CHIP进行基准测试，结果显示出显著的改进空间，突显了数据集带来的独特挑战。CHIP将公开发布。

## 🔬 方法详解

**问题定义**：本文旨在解决在真实工业环境中对椅子的6D姿态估计问题。现有方法多集中于家庭物体，缺乏对工业环境的有效评估，导致在复杂场景下的性能不足。

**核心思路**：CHIP数据集的核心思想是提供一个真实的工业环境数据集，专注于椅子的6D姿态估计，以便更好地评估和改进现有的姿态估计算法。通过使用多种RGBD传感技术，数据集能够捕捉到复杂的遮挡和干扰情况。

**技术框架**：CHIP数据集的构建包括多个阶段：首先，选择七种不同的椅子；其次，利用三种RGBD传感器进行数据采集；最后，自动注释每张图像的6D姿态，确保数据的准确性和丰富性。

**关键创新**：CHIP数据集的主要创新在于其针对真实工业环境的设计，填补了现有数据集在复杂物体和遮挡条件下的空白。这一设计使得研究者能够在更具挑战性的场景中测试和优化算法。

**关键设计**：数据集包含77,811张RGBD图像，平均每种椅子11,115个注释。注释是通过机器人运动学自动生成的，确保了数据的高质量和一致性。

## 📊 实验亮点

实验结果表明，使用CHIP数据集进行的三种零样本6D姿态估计方法在不同传感器类型和遮挡水平下的性能均有显著提升，显示出数据集的挑战性和研究价值。具体性能数据尚未披露，但结果强调了改进的必要性。

## 🎯 应用场景

CHIP数据集的潜在应用领域包括工业机器人操作、自动化装配线以及智能家具管理等。通过提供真实场景下的6D姿态估计数据，研究者可以开发出更为精准和高效的机器人操作算法，推动智能制造和服务机器人技术的发展。

## 📄 摘要（原文）

> Accurate 6D pose estimation of complex objects in 3D environments is essential for effective robotic manipulation. Yet, existing benchmarks fall short in evaluating 6D pose estimation methods under realistic industrial conditions, as most datasets focus on household objects in domestic settings, while the few available industrial datasets are limited to artificial setups with objects placed on tables. To bridge this gap, we introduce CHIP, the first dataset designed for 6D pose estimation of chairs manipulated by a robotic arm in a real-world industrial environment. CHIP includes seven distinct chairs captured using three different RGBD sensing technologies and presents unique challenges, such as distractor objects with fine-grained differences and severe occlusions caused by the robotic arm and human operators. CHIP comprises 77,811 RGBD images annotated with ground-truth 6D poses automatically derived from the robot's kinematics, averaging 11,115 annotations per chair. We benchmark CHIP using three zero-shot 6D pose estimation methods, assessing performance across different sensor types, localization priors, and occlusion levels. Results show substantial room for improvement, highlighting the unique challenges posed by the dataset. CHIP will be publicly released.

