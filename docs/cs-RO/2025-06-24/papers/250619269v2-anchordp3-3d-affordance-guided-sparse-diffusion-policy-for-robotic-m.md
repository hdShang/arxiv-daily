---
layout: default
title: "AnchorDP3: 3D Affordance Guided Sparse Diffusion Policy for Robotic Manipulation"
---

# AnchorDP3: 3D Affordance Guided Sparse Diffusion Policy for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19269" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19269v2</a>
  <a href="https://arxiv.org/pdf/2506.19269.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19269v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19269v2', 'AnchorDP3: 3D Affordance Guided Sparse Diffusion Policy for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyan Zhao, Ke Fan, He-Yang Xu, Ning Qiao, Bo Peng, Wenlong Gao, Dongjiang Li, Hui Shen

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-24 (更新: 2025-06-25)

---

## 💡 一句话要点

**提出AnchorDP3以解决双臂机器人操控中的高随机性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `双臂机器人` `操控策略` `扩散政策` `语义分割` `多任务学习` `可用性锚点` `机器人技术` `自动化`

## 📋 核心要点

1. 现有的机器人操控方法在高度随机化的环境中表现不佳，难以有效处理复杂的任务场景。
2. AnchorDP3通过引入模拟器监督的语义分割和任务条件特征编码器，提升了多任务学习的效率和准确性。
3. 在RoboTwin基准测试中，AnchorDP3实现了98.7%的成功率，显著优于现有方法，展示了其强大的适应性。

## 📝 摘要（中文）

我们提出了AnchorDP3，一个用于双臂机器人操控的扩散策略框架，在高度随机化的环境中实现了最先进的性能。AnchorDP3整合了三项关键创新：(1) 使用渲染的真实标签进行模拟器监督的语义分割，明确分割任务关键对象，提供强大的可用性先验；(2) 任务条件特征编码器，处理每个任务的增强点云，实现高效的多任务学习；(3) 以可用性为锚的关键姿态扩散，简化了预测空间，强制动作专家同时预测机器人关节角度和末端执行器姿态。经过大规模程序生成的模拟数据训练，AnchorDP3在RoboTwin基准测试中实现了98.7%的平均成功率，展示了其在极端随机化条件下的强大能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决双臂机器人在高度随机化环境中进行操控时的效率和准确性问题。现有方法往往无法有效处理复杂的任务场景，导致成功率低下。

**核心思路**：AnchorDP3的核心思路是通过引入语义分割和特征编码器，结合可用性锚点，简化动作预测空间，从而提高机器人操控的效率和准确性。

**技术框架**：AnchorDP3的整体架构包括三个主要模块：模拟器监督的语义分割模块、任务条件特征编码器和可用性锚定的关键姿态扩散模块。通过这些模块的协同工作，实现了高效的多任务学习和精确的动作预测。

**关键创新**：AnchorDP3的主要创新在于使用语义分割明确分割任务关键对象，并通过关键姿态替代密集轨迹预测，显著简化了动作预测的复杂性。这种设计与现有方法的本质区别在于其对几何一致性的利用。

**关键设计**：在设计中，采用了轻量级的任务条件特征编码器，优化了网络结构以适应多任务学习。此外，损失函数的设计也考虑了动作专家同时预测关节角度和末端执行器姿态的需求，以加速收敛和提高准确性。

## 📊 实验亮点

在RoboTwin基准测试中，AnchorDP3实现了98.7%的平均成功率，显著优于现有方法，展示了其在极端随机化条件下的强大适应性。这一成果表明，AnchorDP3在处理复杂操控任务时具有显著的性能提升。

## 🎯 应用场景

AnchorDP3的研究成果在机器人操控领域具有广泛的应用潜力，尤其是在需要高效处理复杂任务的工业自动化、服务机器人和智能制造等场景。通过消除对人类示范的依赖，该框架有望实现完全自主的视觉运动策略生成，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> We present AnchorDP3, a diffusion policy framework for dual-arm robotic manipulation that achieves state-of-the-art performance in highly randomized environments. AnchorDP3 integrates three key innovations: (1) Simulator-Supervised Semantic Segmentation, using rendered ground truth to explicitly segment task-critical objects within the point cloud, which provides strong affordance priors; (2) Task-Conditioned Feature Encoders, lightweight modules processing augmented point clouds per task, enabling efficient multi-task learning through a shared diffusion-based action expert; (3) Affordance-Anchored Keypose Diffusion with Full State Supervision, replacing dense trajectory prediction with sparse, geometrically meaningful action anchors, i.e., keyposes such as pre-grasp pose, grasp pose directly anchored to affordances, drastically simplifying the prediction space; the action expert is forced to predict both robot joint angles and end-effector poses simultaneously, which exploits geometric consistency to accelerate convergence and boost accuracy. Trained on large-scale, procedurally generated simulation data, AnchorDP3 achieves a 98.7% average success rate in the RoboTwin benchmark across diverse tasks under extreme randomization of objects, clutter, table height, lighting, and backgrounds. This framework, when integrated with the RoboTwin real-to-sim pipeline, has the potential to enable fully autonomous generation of deployable visuomotor policies from only scene and instruction, totally eliminating human demonstrations from learning manipulation skills.

