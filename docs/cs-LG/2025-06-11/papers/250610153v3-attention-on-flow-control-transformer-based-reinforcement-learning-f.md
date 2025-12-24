---
layout: default
title: "Attention on flow control: transformer-based reinforcement learning for lift regulation in highly disturbed flows"
---

# Attention on flow control: transformer-based reinforcement learning for lift regulation in highly disturbed flows

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10153" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10153v3</a>
  <a href="https://arxiv.org/pdf/2506.10153.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10153v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10153v3', 'Attention on flow control: transformer-based reinforcement learning for lift regulation in highly disturbed flows')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhecheng Liu, Jeff D. Eldredge

**分类**: physics.flu-dyn, cs.LG

**发布日期**: 2025-06-11 (更新: 2025-11-07)

---

## 💡 一句话要点

**提出基于变压器的强化学习以解决强干扰流中的升力调节问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `变压器` `流体控制` `升力调节` `气流干扰` `非线性控制` `迁移学习`

## 📋 核心要点

1. 现有的线性流控制策略在面对强干扰时表现不佳，无法有效应对非线性相互作用带来的挑战。
2. 本研究提出了一种基于变压器的强化学习框架，利用有限的表面压力传感器来学习有效的升力调节策略。
3. 实验结果显示，所学策略在多个气流干扰环境中表现优于传统的比例控制，且具有良好的泛化能力。

## 📝 摘要（中文）

现有的线性流控制策略在强干扰序列中可能失效，因此本研究提出了一种基于变压器的强化学习框架，旨在通过俯仰控制有效调节任意长的气流干扰序列中的升力。随机气流导致的高方差流动仅通过有限的表面压力传感器观察，使得该控制问题比静态流动更具挑战性。通过预训练和任务级迁移学习加速训练，结果表明所学策略在升力调节上优于最佳比例控制，且随着干扰数量的增加，性能差距进一步扩大。

## 🔬 方法详解

**问题定义**：本研究旨在解决在强干扰流中升力调节的控制问题。现有的线性控制方法在面对强干扰时失效，无法有效应对非线性相互作用带来的复杂性。

**核心思路**：论文提出了一种基于变压器的强化学习框架，通过学习有效的控制策略来应对任意长的气流干扰序列，利用有限的传感器数据克服部分可观测性问题。

**技术框架**：整体架构包括预训练阶段（使用专家策略进行初始化），强化学习阶段（通过与环境交互学习控制策略），以及任务级迁移学习（将单一干扰训练的策略扩展到多个干扰）。

**关键创新**：最重要的技术创新在于引入变压器模型来处理部分可观测性问题，并通过预训练和迁移学习加速训练过程，这与传统的线性控制方法有本质区别。

**关键设计**：在网络结构上，采用变压器架构以捕捉时序特征，损失函数设计为结合升力调节效果和控制努力的综合指标，参数设置上优化了俯仰控制的配置。

## 📊 实验亮点

实验结果表明，所学的控制策略在多个气流干扰环境中表现优于最佳比例控制，随着干扰数量的增加，性能差距进一步扩大，显示出良好的泛化能力。具体而言，所提出的策略在小数量干扰环境中训练后，能够有效适应任意长的干扰序列。

## 🎯 应用场景

该研究的潜在应用领域包括航空航天、无人机控制及其他需要在复杂流动环境中进行精确控制的工程领域。通过提升升力调节的效率和准确性，能够显著改善飞行器的稳定性和性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> A linear flow control strategy designed for weak disturbances may not remain effective in sequences of strong disturbances due to nonlinear interactions, but it is sensible to leverage it for developing a better strategy. In the present study, we propose a transformer-based reinforcement learning (RL) framework to learn an effective control strategy for regulating aerodynamic lift in arbitrarily long gust sequences via pitch control. The random gusts produce intermittent, high-variance flows observed only through limited surface pressure sensors, making this control problem inherently challenging compared to stationary flows. The transformer addresses the challenge of partial observability from the limited surface pressures. We demonstrate that the training can be accelerated with two techniques -- pretraining with an expert policy (here, linear control) and task-level transfer learning (here, extending a policy trained on isolated gusts to multiple gusts). We show that the learned strategy outperforms the best proportional control, with the performance gap widening as the number of gusts increases. The control strategy learned in an environment with a small number of successive gusts is shown to effectively generalize to an environment with an arbitrarily long sequence of gusts. We investigate the pivot configuration and show that quarter-chord pitching control can achieve superior lift regulation with substantially less control effort compared to mid-chord pitching control. Through a decomposition of the lift, we attribute this advantage to the dominant added-mass contribution accessible via quarter-chord pitching.

