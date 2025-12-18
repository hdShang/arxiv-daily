---
layout: default
title: Sampling-Based Optimization with Parallelized Physics Simulator for Bimanual Manipulation
---

# Sampling-Based Optimization with Parallelized Physics Simulator for Bimanual Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21264" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21264v1</a>
  <a href="https://arxiv.org/pdf/2511.21264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21264v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21264v1', 'Sampling-Based Optimization with Parallelized Physics Simulator for Bimanual Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iryna Hurova, Alinjar Dan, Karl Kruusamäe, Arun Kumar Singh

**分类**: cs.RO

**发布日期**: 2025-11-26

**备注**: 9 pages, 5 figures

---

## 💡 一句话要点

**提出基于并行物理模拟优化的采样方法，解决复杂双臂操作任务。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双臂操作` `采样优化` `物理模拟` `GPU加速` `Model Predictive Path Integral Control` `sim-to-real迁移` `机器人` `MuJoCo`

## 📋 核心要点

1. 端到端学习在双臂操作中面临泛化性挑战，尤其是在复杂环境中。
2. 论文提出基于采样的优化框架，利用GPU加速的物理模拟器作为世界模型。
3. 实验表明，该方法能有效解决复杂双臂操作任务，并实现sim-to-real迁移。

## 📝 摘要（中文）

近年来，双臂操作已成为机器人领域的研究热点，端到端学习是解决双臂任务的主要策略。然而，这种基于学习的方法存在泛化能力差的局限性，尤其是在复杂环境中。本文提出了一种替代方案：一个基于采样的优化框架，它利用GPU加速的物理模拟器作为其世界模型。我们证明了该方法可以解决存在静态障碍物的复杂双臂操作任务。我们的贡献是一种定制的Model Predictive Path Integral Control (MPPI)算法，该算法由精心设计的任务特定成本函数指导，并使用GPU加速的MuJoCo来高效评估机器人与物体的交互。我们将此方法应用于解决PerAct基准测试中更具挑战性的任务版本，例如需要通过障碍训练场进行点对点的球体转移。此外，我们确定我们的方法可以在通用GPU上实现实时性能，并通过利用MuJoCo中的独特功能来促进成功的sim-to-real迁移。最后，本文对样本复杂度和鲁棒性进行了统计分析，量化了我们方法的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂环境下双臂操作任务的规划问题。现有端到端学习方法难以泛化到新的、复杂的场景，尤其是在存在障碍物时，需要大量的训练数据，并且难以保证安全性。

**核心思路**：论文的核心思路是利用基于采样的优化方法，结合GPU加速的物理模拟器，构建一个高效且可泛化的双臂操作规划框架。通过物理模拟器，可以快速评估不同动作序列的代价，从而找到最优的动作序列。

**技术框架**：整体框架包括以下几个主要模块：1) 状态空间采样：在机器人的关节空间或任务空间中进行采样，生成候选的动作序列。2) 物理模拟：使用GPU加速的MuJoCo物理引擎，对每个候选动作序列进行模拟，评估其与环境的交互，并计算相应的代价。3) 优化：使用Model Predictive Path Integral Control (MPPI)算法，根据代价函数对采样得到的动作序列进行优化，选择最优的动作序列。4) 轨迹执行：将优化后的动作序列发送给机器人执行。

**关键创新**：论文的关键创新在于将采样优化与GPU加速的物理模拟相结合，并设计了任务特定的代价函数。这种方法能够在复杂环境中快速找到可行的双臂操作方案，并且具有良好的泛化能力。此外，利用MuJoCo的特性，实现了sim-to-real的迁移。

**关键设计**：论文中关键的设计包括：1) 任务特定的代价函数：根据不同的任务，设计不同的代价函数，例如，对于点对点转移任务，代价函数可以包括目标距离、碰撞惩罚等。2) MPPI算法的参数设置：需要根据具体的任务和环境，调整MPPI算法的参数，例如，采样数量、噪声水平等。3) MuJoCo的配置：需要合理配置MuJoCo的参数，例如，仿真步长、接触参数等，以保证仿真的精度和效率。

## 📊 实验亮点

该方法在PerAct基准测试的更具挑战性版本上进行了验证，例如通过障碍训练场进行点对点的球体转移。实验结果表明，该方法能够在通用GPU上实现实时性能，并且通过利用MuJoCo的独特功能，实现了成功的sim-to-real迁移。论文还对样本复杂度和鲁棒性进行了统计分析，量化了该方法的性能。

## 🎯 应用场景

该研究成果可应用于各种需要双臂操作的场景，例如：工业自动化中的装配、搬运，医疗机器人中的辅助手术，以及家庭服务机器人中的物品整理等。通过结合物理模拟和优化算法，可以提高机器人在复杂环境中的操作能力和鲁棒性，降低开发成本，加速机器人的实际应用。

## 📄 摘要（原文）

> In recent years, dual-arm manipulation has become an area of strong interest in robotics, with end-to-end learning emerging as the predominant strategy for solving bimanual tasks. A critical limitation of such learning-based approaches, however, is their difficulty in generalizing to novel scenarios, especially within cluttered environments. This paper presents an alternative paradigm: a sampling-based optimization framework that utilizes a GPU-accelerated physics simulator as its world model. We demonstrate that this approach can solve complex bimanual manipulation tasks in the presence of static obstacles. Our contribution is a customized Model Predictive Path Integral Control (MPPI) algorithm, \textbf{guided by carefully designed task-specific cost functions,} that uses GPU-accelerated MuJoCo for efficiently evaluating robot-object interaction. We apply this method to solve significantly more challenging versions of tasks from the PerAct$^{2}$ benchmark, such as requiring the point-to-point transfer of a ball through an obstacle course. Furthermore, we establish that our method achieves real-time performance on commodity GPUs and facilitates successful sim-to-real transfer by leveraging unique features within MuJoCo. The paper concludes with a statistical analysis of the sample complexity and robustness, quantifying the performance of our approach. The project website is available at: https://sites.google.com/view/bimanualakslabunitartu .

