---
layout: default
title: "TROFI: Trajectory-Ranked Offline Inverse Reinforcement Learning"
---

# TROFI: Trajectory-Ranked Offline Inverse Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22008" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22008v1</a>
  <a href="https://arxiv.org/pdf/2506.22008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22008v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22008v1', 'TROFI: Trajectory-Ranked Offline Inverse Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alessandro Sestini, Joakim Bergdahl, Konrad Tollmar, Andrew D. Bagdanov, Linus Gisslén

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-27

**备注**: Published at Reinforcement Learning and Video Games Workshop at RLC 2025

---

## 💡 一句话要点

**提出TROFI以解决离线强化学习中的奖励函数缺失问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `逆强化学习` `奖励函数` `人类偏好` `策略学习` `视频游戏开发` `机器人控制`

## 📋 核心要点

1. 现有的离线强化学习方法依赖于预定义的奖励函数，但在实际应用中，尤其是视频游戏开发中，奖励函数的可用性往往不确定。
2. TROFI通过从人类偏好中学习奖励函数，进而对原始数据集进行标记，使得在没有最优轨迹的情况下也能有效训练策略。
3. 实验结果表明，TROFI在D4RL基准上表现优于基线，并且在3D游戏环境中验证了其有效性，展示了良好的策略学习能力。

## 📝 摘要（中文）

在离线强化学习中，智能体仅使用固定的存储过渡数据进行训练，但这需要数据集由奖励函数标记。在视频游戏开发等应用场景中，奖励函数的可用性并不总是得到保证。本文提出了轨迹排名离线逆强化学习（TROFI），一种在没有预定义奖励函数的情况下有效学习策略的新方法。TROFI首先从人类偏好中学习奖励函数，然后利用该函数对原始数据集进行标记，使其可用于策略训练。与其他方法相比，我们的方法不需要最优轨迹。通过在D4RL基准上的实验，我们证明了TROFI在性能上始终优于基线，并且与使用真实奖励学习策略的效果相当。此外，我们在3D游戏环境中验证了该方法的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决离线强化学习中缺乏预定义奖励函数的问题。现有方法通常依赖于最优轨迹进行训练，限制了其在实际应用中的灵活性和适用性。

**核心思路**：TROFI的核心思想是通过人类偏好学习奖励函数，并利用该函数对原始数据集进行标记，从而使得策略学习不再依赖于最优轨迹。这样的设计使得方法在实际应用中更具适应性。

**技术框架**：TROFI的整体架构包括两个主要阶段：首先是从人类偏好中学习奖励函数，其次是利用学习到的奖励函数对原始数据集进行标记，最后在标记后的数据集上训练策略。

**关键创新**：TROFI的最大创新在于其不依赖于最优轨迹，能够在缺乏奖励函数的情况下有效学习策略。这一方法与传统的逆强化学习方法形成了鲜明对比，后者通常需要最优轨迹作为输入。

**关键设计**：在设计上，TROFI采用了特定的损失函数来优化奖励模型，并在网络结构上进行了调整，以确保奖励函数能够有效地反映人类偏好。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在D4RL基准测试中，TROFI的表现始终优于基线方法，且在某些任务中与使用真实奖励函数学习的策略效果相当，展示了其强大的策略学习能力。此外，在3D游戏环境中的验证进一步支持了TROFI的有效性。

## 🎯 应用场景

TROFI的研究成果在多个领域具有潜在应用价值，尤其是在视频游戏开发、机器人控制和人机交互等场景中。通过有效学习策略而不依赖于明确的奖励函数，TROFI能够加速智能体的训练过程，并提高其在复杂环境中的适应能力。未来，该方法可能会推动更多基于人类偏好的智能系统的开发。

## 📄 摘要（原文）

> In offline reinforcement learning, agents are trained using only a fixed set of stored transitions derived from a source policy. However, this requires that the dataset be labeled by a reward function. In applied settings such as video game development, the availability of the reward function is not always guaranteed. This paper proposes Trajectory-Ranked OFfline Inverse reinforcement learning (TROFI), a novel approach to effectively learn a policy offline without a pre-defined reward function. TROFI first learns a reward function from human preferences, which it then uses to label the original dataset making it usable for training the policy. In contrast to other approaches, our method does not require optimal trajectories. Through experiments on the D4RL benchmark we demonstrate that TROFI consistently outperforms baselines and performs comparably to using the ground truth reward to learn policies. Additionally, we validate the efficacy of our method in a 3D game environment. Our studies of the reward model highlight the importance of the reward function in this setting: we show that to ensure the alignment of a value function to the actual future discounted reward, it is fundamental to have a well-engineered and easy-to-learn reward function.

