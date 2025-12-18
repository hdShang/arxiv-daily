---
layout: default
title: MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning
---

# MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13636" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13636v2</a>
  <a href="https://arxiv.org/pdf/2512.13636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13636v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13636v2', 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Fu, Diankun Zhang, Zongchuang Zhao, Jianfeng Cui, Hongwei Xie, Bing Wang, Guang Chen, Dingkang Liang, Xiang Bai

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-15 (更新: 2025-12-16)

**备注**: 16 pages, 12 figures, 6 tables; Project Page: https://xiaomi-mlab.github.io/MindDrive/

---

## 💡 一句话要点

**MindDrive：提出基于在线强化学习的视觉-语言-动作模型，用于自动驾驶。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `视觉-语言-动作模型` `在线强化学习` `大语言模型` `模仿学习`

## 📋 核心要点

1. 现有VLA自动驾驶方法依赖模仿学习，存在分布偏移和因果混淆问题，难以适应复杂场景。
2. MindDrive通过在线强化学习，利用LLM进行场景推理和决策，并动态映射到可行轨迹，实现高效探索。
3. MindDrive在Bench2Drive基准测试上取得了显著成果，驾驶评分达到78.04，成功率达到55.09%。

## 📝 摘要（中文）

当前自动驾驶中的视觉-语言-动作（VLA）范式主要依赖于模仿学习（IL），这带来了诸如分布偏移和因果混淆等内在挑战。在线强化学习通过试错学习为解决这些问题提供了一条有希望的途径。然而，将在线强化学习应用于自动驾驶中的VLA模型受到连续动作空间中低效探索的阻碍。为了克服这一限制，我们提出了MindDrive，一个VLA框架，包含一个具有两组不同LoRA参数的大语言模型（LLM）。其中一个LLM作为决策专家，用于场景推理和驾驶决策，而另一个作为动作专家，动态地将语言决策映射到可行的轨迹。通过将轨迹级别的奖励反馈到推理空间，MindDrive能够在有限的离散语言驾驶决策集合上进行试错学习，而不是直接在连续动作空间中操作。这种方法有效地平衡了复杂场景中的最优决策、类人驾驶行为以及在线强化学习中的高效探索。使用轻量级的Qwen-0.5B LLM，MindDrive在具有挑战性的Bench2Drive基准测试上实现了78.04的驾驶评分（DS）和55.09%的成功率（SR）。据我们所知，这是第一个证明在线强化学习对自动驾驶中VLA模型有效性的工作。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶中视觉-语言-动作模型（VLA）在复杂场景下的决策问题。现有方法主要依赖模仿学习，存在分布偏移和因果混淆的固有缺陷，难以泛化到未见过的情况。此外，直接在连续动作空间中应用在线强化学习进行探索效率低下，阻碍了VLA模型的进一步优化。

**核心思路**：论文的核心思路是将连续动作空间中的探索问题转化为离散的语言决策空间中的探索问题。通过大语言模型（LLM）进行场景理解和决策，并将决策映射到具体的轨迹动作。利用在线强化学习，根据轨迹级别的奖励信号，优化LLM的决策能力，从而实现高效的试错学习。

**技术框架**：MindDrive框架包含一个LLM，并使用两组LoRA参数分别作为决策专家和动作专家。决策专家负责根据视觉输入和语言指令进行场景推理和驾驶决策，输出离散的语言指令。动作专家负责将语言指令转化为具体的车辆轨迹。在线强化学习模块根据环境反馈的奖励信号，更新决策专家的参数，从而优化驾驶策略。整体流程为：视觉输入 -> 决策专家（LLM）-> 语言指令 -> 动作专家（LLM）-> 车辆控制 -> 环境反馈 -> 强化学习更新决策专家。

**关键创新**：最重要的创新点在于将连续动作空间中的强化学习问题转化为离散语言决策空间中的强化学习问题。通过LLM的语言理解和生成能力，将复杂的驾驶任务分解为一系列可解释的语言指令，从而降低了强化学习的难度，提高了探索效率。此外，使用两组LoRA参数分别作为决策专家和动作专家，实现了决策和动作的解耦，提高了模型的灵活性和可扩展性。

**关键设计**：论文使用Qwen-0.5B作为基础LLM。使用LoRA（Low-Rank Adaptation）技术，仅训练少量参数，降低了计算成本。轨迹级别的奖励函数设计至关重要，需要综合考虑安全性、舒适性和效率。具体奖励函数的设计细节未知，但应包含碰撞惩罚、偏离道路惩罚、速度奖励等因素。语言指令集的设计也需要仔细考虑，需要覆盖常见的驾驶行为，并具有一定的泛化能力。

## 📊 实验亮点

MindDrive在Bench2Drive基准测试上取得了显著的成果，驾驶评分（DS）达到78.04，成功率（SR）达到55.09%。这些结果表明，基于在线强化学习的VLA模型在自动驾驶任务中具有巨大的潜力。与传统的模仿学习方法相比，MindDrive能够更好地适应未知的环境和场景，提高了自动驾驶系统的鲁棒性。

## 🎯 应用场景

该研究成果可应用于各种自动驾驶场景，尤其是在复杂、动态的城市环境中。通过在线强化学习不断优化驾驶策略，可以提高自动驾驶系统的安全性、可靠性和适应性。此外，该方法还可以扩展到其他机器人控制领域，例如无人机、服务机器人等，具有广泛的应用前景。

## 📄 摘要（原文）

> Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

