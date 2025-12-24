---
layout: default
title: "Dense-Jump Flow Matching with Non-Uniform Time Scheduling for Robotic Policies: Mitigating Multi-Step Inference Degradation"
---

# Dense-Jump Flow Matching with Non-Uniform Time Scheduling for Robotic Policies: Mitigating Multi-Step Inference Degradation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13574" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13574v1</a>
  <a href="https://arxiv.org/pdf/2509.13574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13574v1', 'Dense-Jump Flow Matching with Non-Uniform Time Scheduling for Robotic Policies: Mitigating Multi-Step Inference Degradation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zidong Chen, Zihao Guo, Peng Wang, ThankGod Itua Egbe, Yan Lyu, Chenghao Qian

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-16

---

## 💡 一句话要点

**提出Dense-Jump Flow Matching方法，通过非均匀时间调度优化机器人策略，缓解多步推理退化问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人策略学习` `Flow Matching` `非均匀时间调度` `多步推理` `泛化能力`

## 📋 核心要点

1. 现有Flow Matching方法在机器人策略学习中存在泛化能力饱和和多步推理性能退化的问题。
2. 论文提出Dense-Jump Flow Matching，通过非均匀时间调度训练和密集跳跃积分推理来解决上述问题。
3. 实验表明，该方法在多个机器人任务中显著提升了性能，最高可达23.7%。

## 📝 摘要（中文）

Flow Matching已成为学习高质量机器人生成策略的有效框架。然而，我们发现泛化能力沿轨迹快速饱和。此外，增加推理期间的欧拉积分步数反而会降低策略性能。我们认为这是由于(i)均匀间隔的积分步长过度采样了后期区域，从而限制了动作并降低了泛化能力；(ii)学习到的速度场在积分时间接近1时变为非Lipschitz连续，导致不稳定。为了解决这些问题，我们提出了一种新策略，该策略在训练期间利用非均匀时间调度（例如，U形），强调早期和晚期阶段以正则化策略训练，并在推理时采用密集跳跃积分调度，使用单步积分代替跳跃点之后的多步积分，以避免1附近的不稳定区域。本质上，我们的策略是一种高效的单步学习器，仍然可以通过多步积分来提高性能，在各种机器人任务中，性能比最先进的基线提高了高达23.7%。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人策略学习中，基于Flow Matching的方法在多步推理时性能下降的问题。现有方法采用均匀时间间隔进行积分，导致后期轨迹过度采样，限制了泛化能力，并且速度场在接近积分终点时变得不稳定，影响推理效果。

**核心思路**：论文的核心思路是通过非均匀时间调度来优化训练过程，并采用密集跳跃积分策略来优化推理过程。非均匀时间调度强调轨迹的早期和晚期阶段，以提高泛化能力和稳定性。密集跳跃积分则避免在速度场不稳定区域进行多步积分，从而提高推理性能。

**技术框架**：该方法包含两个主要部分：非均匀时间调度训练和密集跳跃积分推理。在训练阶段，使用U形时间调度策略，增加对轨迹起始和结束阶段的采样频率。在推理阶段，首先进行多步积分，直到达到一个预定义的跳跃点，然后使用单步积分完成剩余的轨迹。

**关键创新**：该方法最重要的创新点在于提出了密集跳跃积分策略，通过单步积分避免了速度场不稳定区域的多步积分，从而提高了推理的稳定性和性能。此外，非均匀时间调度策略也有助于提高模型的泛化能力。

**关键设计**：非均匀时间调度采用U形分布，具体参数需要根据任务进行调整。跳跃点的位置是影响性能的关键参数，需要在实验中进行优化。损失函数采用标准的Flow Matching损失函数，但可以根据需要添加额外的正则化项。

## 📊 实验亮点

实验结果表明，Dense-Jump Flow Matching方法在多个机器人任务中显著优于现有基线方法。例如，在某项任务中，该方法比最先进的基线方法提高了23.7%的性能。实验还验证了非均匀时间调度和密集跳跃积分策略的有效性。

## 🎯 应用场景

该研究成果可应用于各种机器人控制任务，例如机械臂运动规划、无人机导航、自动驾驶等。通过提高机器人策略的泛化能力和推理效率，可以使机器人在更复杂的环境中执行任务，并降低对训练数据的需求。该方法还可用于生成更逼真的机器人运动轨迹，提升用户体验。

## 📄 摘要（原文）

> Flow matching has emerged as a competitive framework for learning high-quality generative policies in robotics; however, we find that generalisation arises and saturates early along the flow trajectory, in accordance with recent findings in the literature. We further observe that increasing the number of Euler integration steps during inference counter-intuitively and universally degrades policy performance. We attribute this to (i) additional, uniformly spaced integration steps oversample the late-time region, thereby constraining actions towards the training trajectories and reducing generalisation; and (ii) the learned velocity field becoming non-Lipschitz as integration time approaches 1, causing instability. To address these issues, we propose a novel policy that utilises non-uniform time scheduling (e.g., U-shaped) during training, which emphasises both early and late temporal stages to regularise policy training, and a dense-jump integration schedule at inference, which uses a single-step integration to replace the multi-step integration beyond a jump point, to avoid unstable areas around 1. Essentially, our policy is an efficient one-step learner that still pushes forward performance through multi-step integration, yielding up to 23.7% performance gains over state-of-the-art baselines across diverse robotic tasks.

