---
layout: default
title: MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning
---

# MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13636" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13636</a>
  <a href="https://arxiv.org/pdf/2512.13636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13636" onclick="toggleFavorite(this, '2512.13636', 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Fu, Diankun Zhang, Zongchuang Zhao, Jianfeng Cui, Hongwei Xie, Bing Wang, Guang Chen, Dingkang Liang, Xiang Bai

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**MindDrive：提出基于在线强化学习的视觉-语言-动作模型，用于自动驾驶。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉-语言-动作模型` `强化学习` `大型语言模型` `在线学习` `轨迹规划` `Bench2Drive`

## 📋 核心要点

1. 现有VLA自动驾驶模型依赖模仿学习，存在分布偏移和因果混淆问题，泛化能力受限。
2. MindDrive通过在线强化学习，利用LLM进行场景推理和决策，并引入动作专家将语言决策映射为轨迹。
3. MindDrive在Bench2Drive基准测试中取得了显著成果，驾驶分数达到78.04，成功率达到55.09%。

## 📝 摘要（中文）

当前的自动驾驶视觉-语言-动作（VLA）模型主要依赖于模仿学习（IL），这带来了分布偏移和因果混淆等固有挑战。在线强化学习通过试错学习为解决这些问题提供了一条有希望的途径。然而，将在线强化学习应用于自动驾驶中的VLA模型受到连续动作空间中低效探索的阻碍。为了克服这个限制，我们提出了MindDrive，一个VLA框架，包含一个带有两组不同LoRA参数的大型语言模型（LLM）。一个LLM作为决策专家，用于场景推理和驾驶决策，而另一个作为动作专家，动态地将语言决策映射到可行的轨迹。通过将轨迹级别的奖励反馈到推理空间，MindDrive能够在有限的离散语言驾驶决策集合上进行试错学习，而不是直接在连续动作空间中操作。这种方法有效地平衡了复杂场景中的最优决策、类人驾驶行为以及在线强化学习中的高效探索。使用轻量级的Qwen-0.5B LLM，MindDrive在具有挑战性的Bench2Drive基准测试中实现了78.04的驾驶分数（DS）和55.09%的成功率（SR）。据我们所知，这是第一个证明在线强化学习对自动驾驶中VLA模型有效性的工作。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶中视觉-语言-动作模型（VLA）依赖模仿学习所带来的分布偏移和因果混淆问题。现有方法难以在复杂场景下进行有效的探索和学习，导致泛化能力不足。

**核心思路**：论文的核心思路是将在线强化学习引入VLA模型，通过试错学习来优化驾驶策略。为了解决连续动作空间中探索效率低下的问题，论文将连续动作空间离散化为有限的语言决策集合，并在该集合上进行强化学习。

**技术框架**：MindDrive框架包含一个大型语言模型（LLM），该LLM通过两组LoRA参数分别作为决策专家和动作专家。决策专家负责场景理解和驾驶决策，输出离散的语言指令。动作专家负责将这些语言指令转化为具体的车辆轨迹。系统通过将轨迹级别的奖励反馈给决策专家，实现端到端的强化学习。

**关键创新**：该论文最重要的创新在于将在线强化学习应用于VLA自动驾驶模型，并提出了一种将连续动作空间离散化为语言决策空间的方法，从而提高了探索效率。与传统的模仿学习方法相比，该方法能够通过试错学习来优化驾驶策略，从而更好地适应复杂场景。

**关键设计**：论文使用了轻量级的Qwen-0.5B LLM作为基础模型。LoRA参数用于调整LLM的行为，使其能够更好地适应驾驶任务。轨迹级别的奖励函数用于评估驾驶行为的优劣。通过精心设计的奖励函数，可以引导模型学习安全、高效的驾驶策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13636/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13636/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13636/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MindDrive在Bench2Drive基准测试中取得了显著成果，驾驶分数（DS）达到78.04，成功率（SR）达到55.09%。这些结果表明，该方法在复杂驾驶场景中具有很强的竞争力，并且能够有效地解决模仿学习所带来的问题。该论文是首个证明在线强化学习对自动驾驶中VLA模型有效性的工作。

## 🎯 应用场景

MindDrive的研究成果可应用于各种自动驾驶场景，例如城市道路、高速公路和越野环境。该方法能够提高自动驾驶系统的安全性和可靠性，并降低开发成本。未来，该研究可以扩展到其他机器人领域，例如无人机和家用机器人。

## 📄 摘要（原文）

> Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

