---
layout: default
title: X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real
---

# X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07096" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07096v5</a>
  <a href="https://arxiv.org/pdf/2505.07096.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07096v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07096v5', 'X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prithwish Dan, Kushal Kedia, Angela Chao, Edward Weiyi Duan, Maximus Adrian Pace, Wei-Chiu Ma, Sanjiban Choudhury

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-11 (更新: 2025-11-09)

**🔗 代码/项目**: [PROJECT_PAGE](https://portal-cornell.github.io/X-Sim/)

---

## 💡 一句话要点

**提出X-Sim框架以解决机器人模仿学习中的动作标签缺失问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人操作` `模仿学习` `跨体现学习` `强化学习` `领域适应` `物体运动` `策略蒸馏`

## 📋 核心要点

1. 现有的跨体现方法在处理人类与机器人之间动作差异时效果不佳，导致模仿学习的效率低下。
2. X-Sim框架通过重建逼真模拟和物体运动跟踪，利用物体中心奖励来训练机器人操作策略，克服了动作标签缺失的问题。
3. 实验结果表明，X-Sim在任务进展上平均提高30%，数据收集时间减少10倍，并且具有良好的泛化能力。

## 📝 摘要（中文）

人类视频为训练机器人操作策略提供了一种可扩展的方法，但缺乏标准模仿学习算法所需的动作标签。现有的跨体现方法试图将人类动作映射到机器人动作，但在体现差异显著时往往失败。我们提出了X-Sim，一个通过物体运动作为密集且可转移信号的真实-模拟-真实框架，用于学习机器人策略。X-Sim首先从RGBD人类视频重建出逼真的模拟，并跟踪物体轨迹以定义以物体为中心的奖励。这些奖励用于在模拟中训练强化学习策略。学习到的策略随后通过合成回放转化为图像条件扩散策略。为了转移到现实世界，X-Sim引入了一种在线领域适应技术，在部署期间对齐真实和模拟观察。重要的是，X-Sim不需要任何机器人遥操作数据。我们在两个环境中的五个操作任务上进行了评估，结果显示：在手部跟踪和模拟到现实的基线之上，任务进展平均提高了30%；与行为克隆相比，数据收集时间减少了10倍；并且能够推广到新的相机视角和测试时变化。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人模仿学习中缺乏动作标签的问题。现有方法在处理人类与机器人之间的动作差异时表现不佳，导致学习效率低下。

**核心思路**：X-Sim框架通过将物体运动作为密集且可转移的信号，重建逼真模拟并定义物体中心奖励，从而有效训练机器人操作策略。

**技术框架**：X-Sim的整体架构包括三个主要阶段：首先从RGBD人类视频重建模拟环境；其次跟踪物体轨迹并定义奖励；最后通过在线领域适应技术将学习到的策略转移到现实世界。

**关键创新**：X-Sim的核心创新在于其真实-模拟-真实的学习框架，特别是通过物体运动作为奖励信号的使用，使得机器人能够在不同体现间有效迁移。

**关键设计**：在技术细节上，X-Sim采用了图像条件的扩散策略，并通过合成回放进行策略蒸馏，确保了在不同视角和光照条件下的鲁棒性。

## 📊 实验亮点

实验结果显示，X-Sim在五个操作任务中平均提高了30%的任务进展，相比于手部跟踪和模拟到现实的基线表现出显著优势。此外，与行为克隆相比，X-Sim在数据收集时间上减少了10倍，展示了其高效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过提高机器人在复杂环境中的操作能力，X-Sim能够显著提升机器人在实际应用中的效率和灵活性，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Human videos offer a scalable way to train robot manipulation policies, but lack the action labels needed by standard imitation learning algorithms. Existing cross-embodiment approaches try to map human motion to robot actions, but often fail when the embodiments differ significantly. We propose X-Sim, a real-to-sim-to-real framework that uses object motion as a dense and transferable signal for learning robot policies. X-Sim starts by reconstructing a photorealistic simulation from an RGBD human video and tracking object trajectories to define object-centric rewards. These rewards are used to train a reinforcement learning (RL) policy in simulation. The learned policy is then distilled into an image-conditioned diffusion policy using synthetic rollouts rendered with varied viewpoints and lighting. To transfer to the real world, X-Sim introduces an online domain adaptation technique that aligns real and simulated observations during deployment. Importantly, X-Sim does not require any robot teleoperation data. We evaluate it across 5 manipulation tasks in 2 environments and show that it: (1) improves task progress by 30% on average over hand-tracking and sim-to-real baselines, (2) matches behavior cloning with 10x less data collection time, and (3) generalizes to new camera viewpoints and test-time changes. Code and videos are available at https://portal-cornell.github.io/X-Sim/.

