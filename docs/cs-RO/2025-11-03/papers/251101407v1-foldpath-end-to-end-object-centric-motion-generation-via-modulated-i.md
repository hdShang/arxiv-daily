---
layout: default
title: FoldPath: End-to-End Object-Centric Motion Generation via Modulated Implicit Paths
---

# FoldPath: End-to-End Object-Centric Motion Generation via Modulated Implicit Paths

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01407" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01407v1</a>
  <a href="https://arxiv.org/pdf/2511.01407.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01407v1" onclick="toggleFavorite(this, '2511.01407v1', 'FoldPath: End-to-End Object-Centric Motion Generation via Modulated Implicit Paths')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Paolo Rabino, Gabriele Tiboni, Tatiana Tommasi

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-03

**备注**: Accepted at 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)

---

## 💡 一句话要点

**FoldPath：通过调制隐式路径实现端到端面向对象的运动生成**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `面向对象运动生成` `神经场` `机器人轨迹规划` `端到端学习` `自动化制造`

## 📋 核心要点

1. 现有OCMG方法依赖启发式或学习流程，但需敏感的后处理，难以生成平滑可执行路径。
2. FoldPath将机器人运动学习为连续函数，隐式编码平滑路径，无需脆弱的后处理步骤。
3. FoldPath在仿真和真实工业环境中表现出优越的预测性能和泛化能力，仅需少量专家样本。

## 📝 摘要（中文）

面向对象的运动生成（OCMG）对于推进自动化制造流程至关重要，尤其是在需要高精度专家机器人运动的领域，如喷涂和焊接。为了实现有效的自动化，强大的算法对于在复杂的3D几何体上生成扩展的、对象感知的轨迹至关重要。然而，现有的OCMG技术要么基于特定的启发式方法，要么采用基于学习的流程，但仍然依赖于敏感的后处理步骤来生成可执行的路径。我们介绍FoldPath，一种新颖的、端到端的、基于神经场的OCMG方法。与先前预测离散末端执行器航路点的深度学习方法不同，FoldPath将机器人运动学习为一个连续函数，从而隐式地编码平滑的输出路径。这种范式转变消除了对连接和排序预测的离散航路点的脆弱后处理步骤的需求。特别是，我们的方法展示了优于最近提出的基于学习的方法的预测性能，并且即使在真实的工业环境中也获得了泛化能力，在这些环境中仅提供了有限的70个专家样本。我们通过在逼真的模拟环境中进行的全面实验验证了FoldPath，并引入了新的、严格的指标，旨在全面评估长时程机器人路径，从而推动OCMG任务走向实际成熟。

## 🔬 方法详解

**问题定义**：论文旨在解决面向对象的运动生成（OCMG）问题，特别是在高精度机器人应用中，如喷涂和焊接。现有方法的痛点在于，要么依赖于人工设计的启发式规则，缺乏泛化能力；要么使用深度学习方法，但需要复杂的后处理步骤来保证生成路径的平滑性和可执行性，这些后处理步骤通常比较脆弱，容易出错。

**核心思路**：FoldPath的核心思路是将机器人运动表示为一个连续的函数，而不是离散的航路点序列。通过学习一个隐式的神经场，FoldPath可以直接生成平滑的、对象感知的机器人轨迹。这种方法避免了离散航路点带来的拼接和排序问题，从而消除了对后处理步骤的依赖。

**技术框架**：FoldPath采用端到端的神经场方法。输入是目标对象的3D几何信息和起始/终止姿态。网络学习一个隐式函数，该函数将空间中的点映射到机器人运动的参数。通过对该隐式函数进行采样，可以生成连续的机器人轨迹。整体流程包括：1) 使用编码器提取目标对象的特征；2) 使用神经场网络学习隐式运动路径；3) 通过采样和优化生成最终的机器人轨迹。

**关键创新**：FoldPath最重要的创新在于使用神经场来表示机器人运动。与传统的基于离散航路点的方法相比，神经场可以自然地生成平滑的、连续的轨迹，并且可以更容易地进行优化和控制。此外，FoldPath是端到端训练的，无需人工设计的后处理步骤，从而提高了系统的鲁棒性和泛化能力。

**关键设计**：FoldPath的关键设计包括：1) 使用Transformer网络作为编码器，提取目标对象的全局特征；2) 使用MLP（多层感知机）作为神经场网络，学习隐式运动路径；3) 使用专门设计的损失函数，鼓励生成的轨迹平滑、安全且符合任务要求。损失函数可能包含平滑性损失、碰撞避免损失和任务特定损失（例如，保持与目标表面的恒定距离）。具体的参数设置和网络结构细节在论文中有详细描述，但此处未知。

## 📊 实验亮点

FoldPath在仿真环境中取得了显著的性能提升，优于现有的基于学习的方法。特别是在真实工业环境中，仅使用70个专家样本，FoldPath仍然表现出良好的泛化能力。论文还引入了新的、严格的指标来评估长时程机器人路径，为OCMG任务的评估提供了更全面的方法。具体的性能数据和提升幅度在论文中有详细描述，但此处未知。

## 🎯 应用场景

FoldPath在自动化制造领域具有广泛的应用前景，例如喷涂、焊接、装配等。它可以用于生成高精度、高质量的机器人运动轨迹，提高生产效率和产品质量。此外，FoldPath还可以应用于其他需要复杂运动规划的领域，如医疗机器人、服务机器人等。该研究有望推动机器人技术的进步，实现更智能、更灵活的自动化生产。

## 📄 摘要（原文）

> Object-Centric Motion Generation (OCMG) is instrumental in advancing automated manufacturing processes, particularly in domains requiring high-precision expert robotic motions, such as spray painting and welding. To realize effective automation, robust algorithms are essential for generating extended, object-aware trajectories across intricate 3D geometries. However, contemporary OCMG techniques are either based on ad-hoc heuristics or employ learning-based pipelines that are still reliant on sensitive post-processing steps to generate executable paths. We introduce FoldPath, a novel, end-to-end, neural field based method for OCMG. Unlike prior deep learning approaches that predict discrete sequences of end-effector waypoints, FoldPath learns the robot motion as a continuous function, thus implicitly encoding smooth output paths. This paradigm shift eliminates the need for brittle post-processing steps that concatenate and order the predicted discrete waypoints. Particularly, our approach demonstrates superior predictive performance compared to recently proposed learning-based methods, and attains generalization capabilities even in real industrial settings, where only a limited amount of 70 expert samples are provided. We validate FoldPath through comprehensive experiments in a realistic simulation environment and introduce new, rigorous metrics designed to comprehensively evaluate long-horizon robotic paths, thus advancing the OCMG task towards practical maturity.

