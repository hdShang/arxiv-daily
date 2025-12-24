---
layout: default
title: "PegasusFlow: Parallel Rolling-Denoising Score Sampling for Robot Diffusion Planner Flow Matching"
---

# PegasusFlow: Parallel Rolling-Denoising Score Sampling for Robot Diffusion Planner Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08435" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08435v1</a>
  <a href="https://arxiv.org/pdf/2509.08435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08435v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08435v1', 'PegasusFlow: Parallel Rolling-Denoising Score Sampling for Robot Diffusion Planner Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Ye, Haibo Gao, Peng Xu, Zhelin Zhang, Junqi Shan, Ao Zhang, Wei Zhang, Ruyi Zhou, Zongquan Deng, Liang Ding

**分类**: cs.RO

**发布日期**: 2025-09-10

**备注**: 8 pages, 7 figures, conference paper

**🔗 代码/项目**: [PROJECT_PAGE](https://masteryip.github.io/pegasusflow.github.io/)

---

## 💡 一句话要点

**PegasusFlow：用于机器人扩散规划器流匹配的并行滚动去噪分数采样**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人轨迹规划` `扩散模型` `流匹配` `并行采样` `滚动去噪` `加权基函数优化` `强化学习` `机器人导航`

## 📋 核心要点

1. 现有机器人轨迹规划依赖专家数据进行模仿学习，数据获取困难且训练流程低效，限制了扩散模型在机器人上的应用。
2. PegasusFlow通过分层滚动去噪框架，直接从环境交互中并行采样轨迹分数梯度，无需专家数据。
3. 提出的加权基函数优化（WBFO）算法，利用样条基表示，提高了采样效率和收敛速度，并在复杂地形运动规划中表现出色。

## 📝 摘要（中文）

扩散模型为机器人轨迹规划提供了强大的生成能力，但其在机器人上的实际部署受到一个关键瓶颈的阻碍：依赖于专家演示的模仿学习。这种范式对于数据稀缺的专用机器人来说通常是不切实际的，并且创建了一个低效的、理论上非最优的训练流程。为了克服这个问题，我们引入了PegasusFlow，一个分层滚动去噪框架，它能够直接且并行地从环境交互中采样轨迹分数梯度，完全绕过了对专家数据的需求。我们的核心创新是一种新的采样算法，加权基函数优化（WBFO），它利用样条基表示来实现优于传统方法（如MPPI）的采样效率和更快的收敛速度。该框架嵌入在一个可扩展的异步并行仿真架构中，该架构支持大规模并行rollout以实现高效的数据收集。在轨迹优化和机器人导航任务上的大量实验表明，我们的方法，特别是结合强化学习warm-start的Action-Value WBFO（AVWBFO），明显优于基线。在一个具有挑战性的跨越障碍任务中，我们的方法实现了100%的成功率，并且比次优方法快18%，验证了其在复杂地形运动规划中的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人轨迹规划中对专家数据依赖的问题。现有的基于模仿学习的方法，需要大量的专家数据，这在许多实际机器人应用中是难以获得的。此外，模仿学习的性能上限受限于专家数据质量，难以达到最优。

**核心思路**：论文的核心思路是通过直接从环境交互中学习轨迹分数梯度，避免对专家数据的依赖。通过并行采样和滚动去噪，可以高效地探索环境，并学习到高质量的轨迹。

**技术框架**：PegasusFlow框架包含以下主要模块：1) 并行仿真环境：用于大规模并行地进行轨迹rollout和数据收集。2) 滚动去噪模块：通过迭代地添加噪声和去噪，逐步优化轨迹。3) 加权基函数优化（WBFO）：用于高效地采样轨迹分数梯度。4) 强化学习warm-start（可选）：用于加速学习过程。

**关键创新**：论文的关键创新在于提出了加权基函数优化（WBFO）算法，该算法利用样条基表示来参数化轨迹，并通过优化基函数的权重来寻找最优轨迹。与传统的采样方法（如MPPI）相比，WBFO具有更高的采样效率和更快的收敛速度。此外，并行滚动去噪框架也提高了数据收集的效率。

**关键设计**：WBFO算法的关键设计包括：1) 使用样条基函数表示轨迹，减少了搜索空间。2) 使用加权策略来平衡探索和利用。3) 使用Action-Value函数来指导采样过程。损失函数的设计目标是最小化轨迹与目标状态之间的距离，并最大化轨迹的平滑度。并行仿真环境采用异步架构，以提高数据收集的吞吐量。

## 📊 实验亮点

在具有挑战性的跨越障碍任务中，PegasusFlow实现了100%的成功率，并且比次优方法快18%。在其他轨迹优化和机器人导航任务中，PegasusFlow也明显优于基线方法，验证了其在复杂环境下的有效性。Action-Value WBFO (AVWBFO) 结合强化学习 warm-start 进一步提升了性能。

## 🎯 应用场景

该研究成果可应用于各种机器人轨迹规划任务，例如自动驾驶、无人机导航、机器人操作等。特别是在数据稀缺或环境复杂的场景下，该方法具有显著优势。未来，该方法有望推动机器人自主学习和智能决策的发展，提高机器人在实际应用中的适应性和鲁棒性。

## 📄 摘要（原文）

> Diffusion models offer powerful generative capabilities for robot trajectory planning, yet their practical deployment on robots is hindered by a critical bottleneck: a reliance on imitation learning from expert demonstrations. This paradigm is often impractical for specialized robots where data is scarce and creates an inefficient, theoretically suboptimal training pipeline. To overcome this, we introduce PegasusFlow, a hierarchical rolling-denoising framework that enables direct and parallel sampling of trajectory score gradients from environmental interaction, completely bypassing the need for expert data. Our core innovation is a novel sampling algorithm, Weighted Basis Function Optimization (WBFO), which leverages spline basis representations to achieve superior sample efficiency and faster convergence compared to traditional methods like MPPI. The framework is embedded within a scalable, asynchronous parallel simulation architecture that supports massively parallel rollouts for efficient data collection. Extensive experiments on trajectory optimization and robotic navigation tasks demonstrate that our approach, particularly Action-Value WBFO (AVWBFO) combined with a reinforcement learning warm-start, significantly outperforms baselines. In a challenging barrier-crossing task, our method achieved a 100% success rate and was 18% faster than the next-best method, validating its effectiveness for complex terrain locomotion planning. https://masteryip.github.io/pegasusflow.github.io/

