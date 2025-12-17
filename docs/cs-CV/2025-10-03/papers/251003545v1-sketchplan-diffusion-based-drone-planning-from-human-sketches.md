---
layout: default
title: SketchPlan: Diffusion Based Drone Planning From Human Sketches
---

# SketchPlan: Diffusion Based Drone Planning From Human Sketches

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03545" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03545v1</a>
  <a href="https://arxiv.org/pdf/2510.03545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03545v1" onclick="toggleFavorite(this, '2510.03545v1', 'SketchPlan: Diffusion Based Drone Planning From Human Sketches')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sixten Norelius, Aaron O. Feldman, Mac Schwager

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-03

**备注**: Code available at https://github.com/sixnor/SketchPlan

---

## 💡 一句话要点

**SketchPlan：基于扩散模型的无人机规划，从人类草图生成飞行路径**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `无人机规划` `扩散模型` `人机交互` `手绘草图` `路径生成`

## 📋 核心要点

1. 现有无人机路径规划方法难以直接利用人类直观的草图指令，限制了人机交互的便捷性。
2. SketchPlan利用扩散模型，将2D手绘草图与深度图像融合，生成3D飞行路径，实现人机协同的无人机导航。
3. 实验表明，SketchPlan在真实环境中表现出色，尤其在低/中等杂乱环境中成功率高达100%，显著优于其他方法。

## 📝 摘要（中文）

本文提出SketchPlan，一种基于扩散模型的规划器，它能够解释深度图像上的2D手绘草图，从而生成用于无人机导航的3D飞行路径。SketchPlan包含两个组件：SketchAdapter，学习将人类草图映射到投影的2D路径；DiffPath，一个扩散模型，从2D投影和第一人称视角的深度图像中推断3D轨迹。我们的模型实现了零样本的sim-to-real迁移，在以前未见过的真实环境中生成准确且安全的飞行路径。为了训练模型，我们使用一组多样化的逼真3D高斯溅射场景构建了一个包含32k飞行路径的合成数据集。我们通过计算3D飞行路径在相机平面上的2D投影来自动标记数据，并使用它来训练DiffPath扩散模型。然而，由于真实的人类2D草图与理想的2D投影有显著差异，我们额外使用真实人类草图标记了872条3D飞行路径，并使用它来训练SketchAdapter，以从人类草图中推断2D投影。我们在模拟和真实世界的实验中证明了SketchPlan的有效性，并通过消融实验表明，在人工标记和自动标记的混合数据上进行训练，以及模块化设计，显著提高了其正确解释人类意图和推断3D路径的能力。在真实世界的无人机测试中，SketchPlan在低/中等杂乱环境中实现了100%的成功率，在未见过的高杂乱环境中实现了40%的成功率，在任务完成方面优于关键消融实验20-60%。

## 🔬 方法详解

**问题定义**：现有无人机路径规划方法通常依赖于精确的环境地图或复杂的算法，难以直接理解和利用人类手绘草图这种直观的指令。这限制了人机交互的便捷性和效率，尤其是在复杂或未知的环境中。因此，如何将人类的意图通过简单的草图转化为可执行的无人机飞行路径是一个关键问题。

**核心思路**：SketchPlan的核心思路是将人类手绘草图作为引导信号，结合深度图像提供的环境信息，利用扩散模型生成符合人类意图且安全的3D飞行路径。通过学习草图与2D投影之间的映射关系，以及2D投影与3D轨迹之间的生成关系，实现从人类意图到无人机行动的桥梁。

**技术框架**：SketchPlan包含两个主要模块：SketchAdapter和DiffPath。SketchAdapter负责将人类手绘草图转换为2D投影路径，DiffPath则是一个扩散模型，它以2D投影路径和第一人称视角的深度图像作为输入，生成3D飞行轨迹。整个流程包括：1) 用户绘制2D草图；2) SketchAdapter将草图转换为2D投影；3) DiffPath结合2D投影和深度图像生成3D轨迹；4) 无人机执行生成的3D轨迹。

**关键创新**：SketchPlan的关键创新在于将扩散模型应用于无人机路径规划，并结合了人类手绘草图作为引导。与传统的基于优化的路径规划方法相比，扩散模型能够更好地处理不确定性和噪声，生成更鲁棒和自然的轨迹。此外，SketchAdapter的学习使得模型能够理解人类的意图，从而生成更符合人类期望的飞行路径。

**关键设计**：SketchAdapter采用神经网络结构，通过训练学习人类草图到2D投影的映射关系。DiffPath是一个条件扩散模型，其训练目标是根据给定的2D投影和深度图像，生成对应的3D飞行轨迹。为了提高模型的泛化能力，作者使用了大量的合成数据进行预训练，并使用少量真实数据进行微调。损失函数包括轨迹的平滑性损失、安全性损失以及与人类意图一致性的损失。

## 📊 实验亮点

SketchPlan在真实世界的无人机测试中表现出色。在低/中等杂乱环境中，SketchPlan实现了100%的任务完成成功率。即使在未见过的高杂乱环境中，SketchPlan也达到了40%的成功率，并且在任务完成方面，SketchPlan优于关键消融实验20-60%。这些结果表明，SketchPlan具有良好的泛化能力和鲁棒性。

## 🎯 应用场景

SketchPlan可应用于多种场景，如灾难救援、环境监测、物流配送等。在这些场景中，操作人员可以通过简单的手绘草图快速指定无人机的飞行路线，无需复杂的编程或地图信息。该技术有望提高无人机操作的效率和便捷性，降低操作门槛，并扩展无人机的应用范围。

## 📄 摘要（原文）

> We propose SketchPlan, a diffusion-based planner that interprets 2D hand-drawn sketches over depth images to generate 3D flight paths for drone navigation. SketchPlan comprises two components: a SketchAdapter that learns to map the human sketches to projected 2D paths, and DiffPath, a diffusion model that infers 3D trajectories from 2D projections and a first person view depth image. Our model achieves zero-shot sim-to-real transfer, generating accurate and safe flight paths in previously unseen real-world environments. To train the model, we build a synthetic dataset of 32k flight paths using a diverse set of photorealistic 3D Gaussian Splatting scenes. We automatically label the data by computing 2D projections of the 3D flight paths onto the camera plane, and use this to train the DiffPath diffusion model. However, since real human 2D sketches differ significantly from ideal 2D projections, we additionally label 872 of the 3D flight paths with real human sketches and use this to train the SketchAdapter to infer the 2D projection from the human sketch. We demonstrate SketchPlan's effectiveness in both simulated and real-world experiments, and show through ablations that training on a mix of human labeled and auto-labeled data together with a modular design significantly boosts its capabilities to correctly interpret human intent and infer 3D paths. In real-world drone tests, SketchPlan achieved 100\% success in low/medium clutter and 40\% in unseen high-clutter environments, outperforming key ablations by 20-60\% in task completion.

