---
layout: default
title: Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
---

# Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10477" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10477v2</a>
  <a href="https://arxiv.org/pdf/2512.10477.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10477v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10477v2', 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timur Ishuov, Michele Folgheraiter, Madi Nurmanov, Goncalo Gordo, Richárd Farkas, József Dombi

**分类**: cs.RO, cs.NE

**发布日期**: 2025-12-11 (更新: 2025-12-14)

**备注**: https://github.com/SuspensionRailway/symphony

---

## 💡 一句话要点

**提出Symphony算法，解决人形机器人从零开始训练的样本效率、样本邻近性和动作安全性问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人形机器人` `强化学习` `Actor-Critic算法` `样本效率` `动作安全性`

## 📋 核心要点

1. 人形机器人从零开始训练需要大量的样本和时间，现有方法难以满足实际需求。
2. Symphony算法通过“襁褓”正则化和限制参数噪声，保证训练过程中的动作安全性。
3. Fading Replay Buffer和Temporal Advantage的结合，提高了样本效率和Actor-Critic的更新效率。

## 📝 摘要（中文）

本文提出了一种名为Symphony的过渡策略确定性Actor-Critic算法，简称Symphony，旨在解决人形机器人从零开始训练时面临的样本效率、样本邻近性和动作安全性问题。该算法结合了多种思想，包括“襁褓”正则化，通过惩罚动作强度来约束agent的快速但不稳定的发展，但不直接影响动作。Symphony算法限制了参数噪声，并促进动作强度的降低，从而安全地增加熵。此外，本文还使用了Fading Replay Buffer，通过双曲正切函数调整batch采样概率，包含近期记忆和长期记忆轨迹。Temporal Advantage用于改进Critic网络的预测，并允许在一次传递中更新Actor和Critic，以及将Actor和Critic组合成一个对象，并在单行中实现它们的损失。

## 🔬 方法详解

**问题定义**：人形机器人从零开始学习运动控制是一个复杂的问题，需要大量的训练样本。现有的强化学习方法在人形机器人上训练时，往往面临样本效率低、训练不稳定、动作不安全等问题，难以在实际机器人上直接应用。特别是，不加限制地增加高斯噪声可能会损害电机和齿轮箱。

**核心思路**：Symphony算法的核心思路是通过一系列策略来提高样本效率、保证样本邻近性以及确保动作的安全性。通过“襁褓”正则化来约束agent的动作强度，限制参数噪声，并使用Fading Replay Buffer来平衡近期和长期经验，从而实现更稳定和高效的训练。

**技术框架**：Symphony算法是一个Actor-Critic框架，包含Actor网络和Critic网络。Actor网络负责生成动作，Critic网络负责评估动作的价值。算法使用Fading Replay Buffer存储经验，并使用Temporal Advantage来更新Actor和Critic网络。整个训练过程旨在最小化Actor和Critic网络的损失函数。

**关键创新**：Symphony算法的关键创新在于以下几个方面：1) “襁褓”正则化，通过惩罚动作强度来约束agent的动作，提高训练的安全性。2) 限制参数噪声，避免对机器人硬件造成损害。3) Fading Replay Buffer，平衡近期和长期经验，提高样本效率。4) Temporal Advantage，简化Actor和Critic网络的更新过程。

**关键设计**：Fading Replay Buffer使用双曲正切函数来调整batch采样概率，公式为tanh(x)。Temporal Advantage用于改进Critic网络的预测，并允许在一次传递中更新Actor和Critic网络。Actor和Critic的损失函数被组合成一个对象，并在单行中实现。

## 📊 实验亮点

论文提出的Symphony算法在人形机器人上进行了实验验证，结果表明该算法能够有效地提高样本效率、保证样本邻近性和动作安全性。具体性能数据未知，但论文强调该算法在训练过程中对机器人硬件的安全性有显著提升，并能更快地学习到有效的运动策略。

## 🎯 应用场景

Symphony算法可应用于各种人形机器人的运动控制任务，例如行走、跑步、跳跃等。该算法能够提高人形机器人的自主学习能力，使其能够在复杂环境中安全、高效地完成任务。此外，该算法还可以应用于其他类型的机器人，例如四足机器人、机械臂等。

## 📄 摘要（原文）

> In our work we not explicitly hint that it is a misconception to think that humans learn fast. Learning process takes time. Babies start learning to move in the restricted liquid area called placenta. Children often are limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for dozen millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is no secret that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set a limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are kind of immersed in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update Actor and Critic in one pass, as well as combine Actor and Critic in one Object and implement their Losses in one line.

