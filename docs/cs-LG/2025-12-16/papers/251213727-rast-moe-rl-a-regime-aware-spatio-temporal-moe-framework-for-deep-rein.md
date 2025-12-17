---
layout: default
title: RAST-MoE-RL: A Regime-Aware Spatio-Temporal MoE Framework for Deep Reinforcement Learning in Ride-Hailing
---

# RAST-MoE-RL: A Regime-Aware Spatio-Temporal MoE Framework for Deep Reinforcement Learning in Ride-Hailing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13727" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13727</a>
  <a href="https://arxiv.org/pdf/2512.13727.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13727" onclick="toggleFavorite(this, '2512.13727', 'RAST-MoE-RL: A Regime-Aware Spatio-Temporal MoE Framework for Deep Reinforcement Learning in Ride-Hailing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhan Tang, Kangxin Cui, Jung Ho Park, Yibo Zhao, Xuan Jiang, Haoze He, Dingyi Zhuang, Shenhao Wang, Jiangbo Yu, Haris Koutsopoulos, Jinhua Zhao

**分类**: cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出RAST-MoE-RL框架，解决网约车中复杂时空动态下的自适应延迟匹配问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `网约车调度` `强化学习` `混合专家模型` `时空建模` `自适应延迟匹配`

## 📋 核心要点

1. 现有网约车调度方法在处理复杂时空动态时存在不足，或过度简化交通模型，或无法有效捕捉时空模式。
2. RAST-MoE-RL框架通过引入Regime-Aware的MoE编码器，使专家能够自动学习专门化，提升表征能力和计算效率。
3. 实验表明，该框架在真实Uber数据上显著提升了奖励，降低了匹配和接载延迟，并展现了良好的鲁棒性和训练稳定性。

## 📝 摘要（中文）

网约车平台面临在高度不确定的供需条件下平衡乘客等待时间和整体系统效率的挑战。自适应延迟匹配通过决定立即分配司机或批量处理请求，从而在匹配延迟和接载延迟之间进行权衡。由于结果会在具有随机动态的长时程中累积，因此强化学习(RL)是一个合适的框架。然而，现有的方法通常过度简化交通动态或使用浅层编码器，从而错失了复杂的时空模式。我们引入了Regime-Aware Spatio-Temporal Mixture-of-Experts (RAST-MoE)，它将自适应延迟匹配形式化为一个配备了自注意力MoE编码器的regime-aware MDP。与单体网络不同，我们的专家可以自动专门化，从而提高表示能力，同时保持计算效率。一个物理信息驱动的拥塞代理保留了真实的密度-速度反馈，从而能够进行数百万次高效的rollout，而自适应奖励方案则可以防止病态策略。我们的框架仅使用12M参数，就优于强大的基线。在真实的Uber轨迹数据（旧金山）上，它将总奖励提高了13%以上，并将平均匹配和接载延迟分别降低了10%和15%。它展示了跨越未见过的需求regime的鲁棒性和稳定的训练。这些发现突出了MoE增强的RL在具有复杂时空动态的大规模决策中的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决网约车平台中，如何在不确定的供需条件下，通过自适应延迟匹配策略，最小化乘客等待时间和提升系统整体效率的问题。现有方法的痛点在于无法有效建模复杂的时空交通动态，或者使用过于简化的模型导致性能受限。

**核心思路**：论文的核心思路是将自适应延迟匹配问题建模为一个regime-aware的马尔可夫决策过程(MDP)，并利用MoE（Mixture-of-Experts）结构来增强对时空状态的表征能力。通过让不同的专家学习不同的交通状态模式，从而提高模型的泛化能力和效率。

**技术框架**：RAST-MoE-RL框架包含以下主要模块：1) Regime-Aware MDP：将自适应延迟匹配问题形式化为MDP，并根据不同的交通状态（regime）调整策略。2) 自注意力MoE编码器：使用自注意力机制的MoE结构来编码时空状态信息，不同的专家负责处理不同的状态模式。3) 物理信息拥塞代理：利用物理信息来建模交通拥塞，从而实现更真实的模拟环境。4) 自适应奖励方案：设计奖励函数，鼓励模型学习合理的调度策略，并防止出现病态行为。

**关键创新**：该论文的关键创新在于将MoE结构引入到网约车调度的强化学习框架中，并结合regime-aware MDP和物理信息拥塞代理，从而实现了更高效和鲁棒的调度策略。与现有方法的本质区别在于，RAST-MoE-RL能够自动学习和适应不同的交通状态模式，而不需要人工设计复杂的交通模型。

**关键设计**：MoE编码器使用自注意力机制来捕捉时空依赖关系。奖励函数的设计考虑了匹配延迟、接载延迟和系统效率等多个因素，并采用自适应策略来调整奖励权重。物理信息拥塞代理利用宏观交通流模型来模拟交通拥塞现象。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13727/image/model.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13727/image/training_testing_comparison_smooth0.6.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13727/image/combined_expert_and_performance.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RAST-MoE-RL框架在真实的Uber轨迹数据（旧金山）上，将总奖励提高了13%以上，并将平均匹配和接载延迟分别降低了10%和15%。该框架仅使用12M参数，就优于其他强大的基线方法，并且展现了跨越未见过的需求regime的鲁棒性和稳定的训练。

## 🎯 应用场景

该研究成果可应用于实际的网约车平台，提升调度效率，降低乘客等待时间，并提高平台整体的运营效率和用户满意度。此外，该框架的设计思路也可以推广到其他具有复杂时空动态的大规模决策问题，例如物流调度、交通信号控制等。

## 📄 摘要（原文）

> Ride-hailing platforms face the challenge of balancing passenger waiting times with overall system efficiency under highly uncertain supply-demand conditions. Adaptive delayed matching creates a trade-off between matching and pickup delays by deciding whether to assign drivers immediately or batch requests. Since outcomes accumulate over long horizons with stochastic dynamics, reinforcement learning (RL) is a suitable framework. However, existing approaches often oversimplify traffic dynamics or use shallow encoders that miss complex spatiotemporal patterns.We introduce the Regime-Aware Spatio-Temporal Mixture-of-Experts (RAST-MoE), which formalizes adaptive delayed matching as a regime-aware MDP equipped with a self-attention MoE encoder. Unlike monolithic networks, our experts specialize automatically, improving representation capacity while maintaining computational efficiency. A physics-informed congestion surrogate preserves realistic density-speed feedback, enabling millions of efficient rollouts, while an adaptive reward scheme guards against pathological strategies.With only 12M parameters, our framework outperforms strong baselines. On real-world Uber trajectory data (San Francisco), it improves total reward by over 13%, reducing average matching and pickup delays by 10% and 15% respectively. It demonstrates robustness across unseen demand regimes and stable training. These findings highlight the potential of MoE-enhanced RL for large-scale decision-making with complex spatiotemporal dynamics.

