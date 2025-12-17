---
layout: default
title: SkyDreamer: Interpretable End-to-End Vision-Based Drone Racing with Model-Based Reinforcement Learning
---

# SkyDreamer: Interpretable End-to-End Vision-Based Drone Racing with Model-Based Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14783" target="_blank" class="toolbar-btn">arXiv: 2510.14783v1</a>
    <a href="https://arxiv.org/pdf/2510.14783.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14783v1" 
            onclick="toggleFavorite(this, '2510.14783v1', 'SkyDreamer: Interpretable End-to-End Vision-Based Drone Racing with Model-Based Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Aderik Verraest, Stavrow Bahnam, Robin Ferede, Guido de Croon, Christophe De Wagter

**分类**: cs.RO

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**SkyDreamer：基于模型强化学习的可解释端到端视觉无人机竞速**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无人机竞速` `端到端学习` `模型强化学习` `视觉导航` `模拟到真实迁移`

## 📋 核心要点

1. 现有自主无人机竞速系统泛化性差，难以同时实现完全的模拟到真实迁移和机载执行。
2. SkyDreamer利用informed Dreamer，通过世界模型隐式估计状态和参数，实现端到端视觉无人机竞速。
3. 实验表明，SkyDreamer能实现高速飞行和复杂机动，并对视觉误差和电池耗尽具有鲁棒性。

## 📝 摘要（中文）

自主无人机竞速（ADR）系统近年来已达到冠军级水平，但仍然高度依赖于特定场景。端到端视觉方法具有更广泛的适用性，但目前还没有系统能够同时实现完全的模拟到真实迁移、机载执行和冠军级性能。本文提出了SkyDreamer，据我们所知，这是第一个端到端视觉ADR策略，可以直接从像素级表示映射到电机命令。SkyDreamer建立在informed Dreamer之上，这是一种基于模型的强化学习方法，其中世界模型解码为仅在训练期间可用的特权信息。通过将此概念扩展到端到端视觉ADR，世界模型有效地充当隐式状态和参数估计器，大大提高了可解释性。SkyDreamer完全在机载运行，无需外部辅助，通过使用从世界模型的隐藏状态解码的状态来跟踪进度，从而解决视觉歧义，并且不需要外部相机校准，从而可以在不同的无人机上快速部署而无需重新训练。真实世界的实验表明，SkyDreamer实现了稳健的高速飞行，执行了诸如倒环、Split-S和梯子等高难度动作，达到了高达21米/秒的速度和高达6g的加速度。它还通过对低质量分割掩码进行操作来展示了非平凡的视觉模拟到真实迁移，并通过准确估计最大可达到的电机RPM并实时调整其飞行路径来展示了对电池耗尽的鲁棒性。这些结果突出了SkyDreamer对现实差距的重要方面的适应性，在保持鲁棒性的同时仍然实现了极高速、敏捷的飞行。

## 🔬 方法详解

**问题定义**：现有自主无人机竞速系统通常依赖于特定环境和精确的传感器校准，泛化能力有限。端到端视觉方法虽然潜力巨大，但难以同时实现模拟到真实世界的迁移、机载实时执行以及冠军级别的性能。现有方法的痛点在于难以从视觉输入中准确估计无人机的状态和环境参数，导致控制策略不稳定且难以适应变化。

**核心思路**：SkyDreamer的核心思路是利用基于模型的强化学习，通过训练一个世界模型来学习环境的动态特性，并从中解码出无人机的状态和参数。这种方法允许策略网络直接从像素级别的视觉输入映射到电机控制命令，而无需显式地进行状态估计。通过在训练期间使用特权信息（privileged information）来指导世界模型的学习，可以提高状态估计的准确性和鲁棒性。

**技术框架**：SkyDreamer的整体框架包括以下几个主要模块：1) 视觉感知模块：接收无人机摄像头捕获的图像作为输入。2) 世界模型：学习环境的动态特性，并从视觉输入中解码出无人机的状态和参数。3) 策略网络：根据世界模型解码的状态和参数，生成电机控制命令。4) 环境交互模块：将控制命令发送给无人机，并接收新的视觉输入。整个系统采用端到端的训练方式，通过强化学习算法优化策略网络和世界模型的参数。

**关键创新**：SkyDreamer的关键创新在于将informed Dreamer的概念扩展到端到端的视觉无人机竞速。通过让世界模型解码出仅在训练期间可用的特权信息，SkyDreamer能够更准确地估计无人机的状态和参数，从而提高控制策略的鲁棒性和可解释性。此外，SkyDreamer无需外部相机校准，可以在不同的无人机上快速部署。

**关键设计**：SkyDreamer的关键设计包括：1) 使用DreamerV3作为基础的强化学习算法。2) 世界模型采用变分自编码器（VAE）结构，用于学习环境的潜在表示。3) 策略网络采用循环神经网络（RNN）结构，用于处理时序数据。4) 损失函数包括重构损失、KL散度损失和强化学习奖励。5) 为了提高对电池耗尽的鲁棒性，SkyDreamer会实时估计最大可达到的电机RPM，并根据剩余电量调整飞行路径。

## 📊 实验亮点

SkyDreamer在真实世界实验中表现出色，能够以高达21米/秒的速度和6g的加速度执行复杂的飞行机动，如倒环、Split-S和梯子。该系统还展示了良好的模拟到真实迁移能力，即使在低质量分割掩码上也能正常工作。此外，SkyDreamer对电池耗尽具有鲁棒性，能够实时调整飞行路径以适应剩余电量。

## 🎯 应用场景

SkyDreamer技术可应用于自主导航、智能巡检、物流配送等领域。通过提高无人机在复杂环境中的适应性和鲁棒性，可以降低对环境和人为干预的依赖，实现更高效、安全的无人机应用。该研究为开发更智能、更可靠的无人机系统奠定了基础。

## 📄 摘要（原文）

> Autonomous drone racing (ADR) systems have recently achieved champion-level performance, yet remain highly specific to drone racing. While end-to-end vision-based methods promise broader applicability, no system to date simultaneously achieves full sim-to-real transfer, onboard execution, and champion-level performance. In this work, we present SkyDreamer, to the best of our knowledge, the first end-to-end vision-based ADR policy that maps directly from pixel-level representations to motor commands. SkyDreamer builds on informed Dreamer, a model-based reinforcement learning approach where the world model decodes to privileged information only available during training. By extending this concept to end-to-end vision-based ADR, the world model effectively functions as an implicit state and parameter estimator, greatly improving interpretability. SkyDreamer runs fully onboard without external aid, resolves visual ambiguities by tracking progress using the state decoded from the world model's hidden state, and requires no extrinsic camera calibration, enabling rapid deployment across different drones without retraining. Real-world experiments show that SkyDreamer achieves robust, high-speed flight, executing tight maneuvers such as an inverted loop, a split-S and a ladder, reaching speeds of up to 21 m/s and accelerations of up to 6 g. It further demonstrates a non-trivial visual sim-to-real transfer by operating on poor-quality segmentation masks, and exhibits robustness to battery depletion by accurately estimating the maximum attainable motor RPM and adjusting its flight path in real-time. These results highlight SkyDreamer's adaptability to important aspects of the reality gap, bringing robustness while still achieving extremely high-speed, agile flight.

