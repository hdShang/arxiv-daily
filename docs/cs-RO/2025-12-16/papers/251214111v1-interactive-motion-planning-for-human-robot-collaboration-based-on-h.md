---
layout: default
title: Interactive Motion Planning for Human-Robot Collaboration Based on Human-Centric Configuration Space Ergonomic Field
---

# Interactive Motion Planning for Human-Robot Collaboration Based on Human-Centric Configuration Space Ergonomic Field

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14111" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14111v1</a>
  <a href="https://arxiv.org/pdf/2512.14111.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14111v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14111v1', 'Interactive Motion Planning for Human-Robot Collaboration Based on Human-Centric Configuration Space Ergonomic Field')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenzui Li, Yiming Chen, Xi Wu, Tao Teng, Sylvain Calinon, Darwin Caldwell, Fei Chen

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: 10 pages, 9 figures

---

## 💡 一句话要点

**提出基于人机协作构型空间人体工学场的交互式运动规划方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人机协作` `运动规划` `人体工学` `构型空间` `机器人控制`

## 📋 核心要点

1. 现有的人机协作运动规划方法难以兼顾安全性、响应性和人体工学，导致工人疲劳和肌肉骨骼损伤风险。
2. 论文提出构型空间人体工学场（CSEF），通过量化人体工学质量并提供梯度，实现实时人体工学感知规划。
3. 实验表明，CSEF方法在多种人机协作任务中，能有效降低人体工学成本和肌肉激活，提升协作效率。

## 📝 摘要（中文）

本文提出了一种用于工业人机协作的运动规划方法，该方法需要保证无碰撞、响应迅速且符合人体工学安全，以减少疲劳和肌肉骨骼风险。我们提出了构型空间人体工学场（CSEF），这是一个在人体关节空间上的连续且可微的场，用于量化人体工学质量，并为实时人体工学感知规划提供梯度。一种高效的算法利用已建立的指标，通过关节权重和任务条件构建CSEF，并将其集成到与阻抗控制机器人兼容的基于梯度的规划器中。在2自由度基准测试中，基于CSEF的规划比基于任务空间人体工学的规划器实现了更高的成功率、更低的人体工学成本和更快的计算速度。在单手动引导、协同钻孔和双手协同搬运的双臂机器人硬件实验中，与点对点基线相比，CSEF方法能更快地降低人体工学成本，更紧密地跟踪优化后的关节目标，并降低肌肉激活。对于协同钻孔任务，基于CSEF的规划方法将平均人体工学评分降低了高达10.31%，对于双手协同搬运任务，则降低了5.60%，同时降低了关键肌肉群的激活，表明了该方法在实际部署中的益处。

## 🔬 方法详解

**问题定义**：论文旨在解决工业人机协作中，机器人运动规划如何同时保证安全性、响应性和人体工学的问题。现有方法通常只关注碰撞避免和任务完成，忽略了人体工学因素，导致工人长时间工作容易疲劳和受伤。现有基于任务空间人体工学的规划方法计算效率较低，难以满足实时性要求。

**核心思路**：论文的核心思路是将人体工学因素融入到机器人的构型空间中，构建一个连续且可微的构型空间人体工学场（CSEF）。CSEF能够量化不同机器人构型下的人体工学质量，并提供梯度信息，引导机器人朝着更符合人体工学的方向运动。通过在构型空间进行规划，可以避免任务空间规划的复杂性，提高规划效率。

**技术框架**：整体框架包括以下几个主要模块：1) 人体工学指标选择与加权：选择合适的人体工学指标（如关节角度、力矩等），并根据任务的重要性进行加权。2) 构型空间人体工学场（CSEF）构建：基于选定的人体工学指标和权重，在机器人构型空间中构建CSEF。3) 基于梯度的运动规划：利用CSEF提供的梯度信息，采用基于梯度的优化算法，生成符合人体工学的机器人运动轨迹。4) 机器人控制：将规划好的轨迹发送给机器人控制器，实现人机协作。

**关键创新**：论文最重要的技术创新点在于提出了构型空间人体工学场（CSEF）的概念，并将人体工学因素直接融入到机器人的构型空间中。与传统的基于任务空间的人体工学规划方法相比，CSEF方法能够更高效地评估和优化机器人运动的人体工学质量，从而实现实时的人体工学感知规划。

**关键设计**：CSEF的构建依赖于对人体工学指标的选取和加权。论文采用关节角度、力矩等常用的人体工学指标，并根据任务的特点进行加权。CSEF的具体形式是一个连续且可微的函数，可以使用高斯混合模型等方法进行建模。在基于梯度的运动规划中，需要选择合适的优化算法和步长，以保证规划的效率和稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14111v1/fig/cover.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14111v1/fig/CSEF.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14111v1/fig/framework_interactive_motion_planning.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，与基于任务空间人体工学的规划器相比，基于CSEF的规划器在2自由度基准测试中实现了更高的成功率、更低的人体工学成本和更快的计算速度。在双臂机器人硬件实验中，与点对点基线相比，CSEF方法将协同钻孔任务的平均人体工学评分降低了高达10.31%，将双手协同搬运任务的平均人体工学评分降低了5.60%，同时降低了关键肌肉群的激活。

## 🎯 应用场景

该研究成果可广泛应用于各种工业人机协作场景，例如汽车制造、电子装配、医疗康复等。通过优化机器人的运动轨迹，降低工人疲劳和受伤风险，提高生产效率和产品质量。未来，该方法还可以扩展到更复杂的人机协作任务中，例如多机器人协作、人机协同操作等。

## 📄 摘要（原文）

> Industrial human-robot collaboration requires motion planning that is collision-free, responsive, and ergonomically safe to reduce fatigue and musculoskeletal risk. We propose the Configuration Space Ergonomic Field (CSEF), a continuous and differentiable field over the human joint space that quantifies ergonomic quality and provides gradients for real-time ergonomics-aware planning. An efficient algorithm constructs CSEF from established metrics with joint-wise weighting and task conditioning, and we integrate it into a gradient-based planner compatible with impedance-controlled robots. In a 2-DoF benchmark, CSEF-based planning achieves higher success rates, lower ergonomic cost, and faster computation than a task-space ergonomic planner. Hardware experiments with a dual-arm robot in unimanual guidance, collaborative drilling, and bimanual cocarrying show faster ergonomic cost reduction, closer tracking to optimized joint targets, and lower muscle activation than a point-to-point baseline. CSEF-based planning method reduces average ergonomic scores by up to 10.31% for collaborative drilling tasks and 5.60% for bimanual co-carrying tasks while decreasing activation in key muscle groups, indicating practical benefits for real-world deployment.

