---
layout: default
title: APEX: Action Priors Enable Efficient Exploration for Robust Motion Tracking on Legged Robots
---

# APEX: Action Priors Enable Efficient Exploration for Robust Motion Tracking on Legged Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09091" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09091v2</a>
  <a href="https://arxiv.org/pdf/2511.09091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09091v2" onclick="toggleFavorite(this, '2511.09091v2', 'APEX: Action Priors Enable Efficient Exploration for Robust Motion Tracking on Legged Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shivam Sood, Laukik Nakhwa, Sun Ge, Yuhong Cao, Jin Cheng, Fatemah Zargarbashi, Taerim Yoon, Sungjoon Choi, Stelian Coros, Guillaume Sartoretti

**分类**: cs.RO

**发布日期**: 2025-11-12 (更新: 2025-11-19)

**备注**: This work was intended as a replacement of arXiv:2505.10022 and any subsequent updates will appear there

**🔗 代码/项目**: [PROJECT_PAGE](https://marmotlab.github.io/APEX/)

---

## 💡 一句话要点

**APEX：利用动作先验实现腿式机器人稳健运动跟踪的高效探索**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `腿式机器人` `运动跟踪` `强化学习` `动作先验` `专家演示` `多评论家` `机器人控制`

## 📋 核心要点

1. 现有腿式机器人运动跟踪方法依赖大量调参和参考数据，限制了其适应性。
2. APEX通过衰减动作先验引导强化学习探索，并结合多评论家框架平衡性能与风格。
3. 实验表明，APEX提高了样本效率和泛化能力，无需参考数据即可实现稳健的运动跟踪。

## 📝 摘要（中文）

本文提出APEX（动作先验实现高效探索），一种即插即用的扩展方法，用于提升现有运动跟踪算法的性能。APEX无需部署期间的参考数据，提高了样本效率，并减少了参数调整工作。APEX通过结合衰减动作先验将专家演示直接整合到强化学习（RL）中，最初将探索偏向于专家演示，但逐渐允许策略独立探索。结合多评论家框架，平衡了任务性能和运动风格。此外，APEX使单个策略能够学习多样化的运动，并在不同地形和速度下迁移类似参考的风格，同时对奖励设计的变化保持鲁棒性。通过在模拟和Unitree Go2机器人上的大量实验验证了该方法的有效性。APEX利用演示来指导RL训练期间的探索，而无需对它们施加明确的偏差，从而使腿式机器人能够以更高的稳定性、效率和泛化能力进行学习。该方法为指导驱动的RL铺平了道路，以促进从运动到操作的各种机器人任务中自然技能的获取。

## 🔬 方法详解

**问题定义**：现有腿式机器人运动跟踪方法通常需要大量的参数调整，并且在部署时依赖参考数据，这限制了它们在不同环境和任务中的适应性和泛化能力。因此，如何提高运动跟踪算法的样本效率、鲁棒性和泛化能力，同时减少对参考数据的依赖，是一个重要的挑战。

**核心思路**：APEX的核心思路是将专家演示知识融入到强化学习的探索过程中，通过动作先验引导智能体初期探索，并随着训练的进行逐渐减弱先验的影响，允许智能体自主探索。这种方式既能利用专家知识加速学习，又能避免过度依赖专家知识而陷入局部最优。同时，采用多评论家框架来平衡任务性能和运动风格，从而获得更自然和鲁棒的运动策略。

**技术框架**：APEX的整体框架包括以下几个主要模块：1) 动作先验模块：利用专家演示数据构建动作先验，并在训练初期引导智能体的探索方向。2) 强化学习模块：采用强化学习算法（如PPO）训练运动控制策略。3) 多评论家模块：使用多个评论家网络分别评估任务性能和运动风格，并结合这些评估结果来优化策略。4) 衰减机制：随着训练的进行，逐渐减弱动作先验的影响，允许智能体自主探索。

**关键创新**：APEX的关键创新在于将动作先验与强化学习相结合，并设计了一种衰减机制，使得智能体能够在利用专家知识的同时，逐渐摆脱对专家知识的依赖，从而实现更高效和鲁棒的探索。此外，多评论家框架的设计也使得智能体能够同时优化任务性能和运动风格，从而获得更自然和逼真的运动效果。

**关键设计**：动作先验通常使用高斯分布建模，其均值和方差从专家演示数据中估计得到。衰减机制通常采用线性或指数衰减函数，控制动作先验的影响程度。多评论家框架中的每个评论家网络都独立评估策略的性能，并使用不同的奖励函数来衡量任务性能和运动风格。损失函数通常包括任务奖励、风格奖励和策略正则化项，用于优化策略。

## 📊 实验亮点

APEX在模拟和真实机器人（Unitree Go2）上进行了验证。实验结果表明，APEX显著提高了样本效率，减少了对参考数据的依赖，并实现了更鲁棒的运动跟踪。例如，APEX能够在不同地形和速度下迁移运动风格，并且对奖励函数的变化具有更强的鲁棒性。与现有方法相比，APEX在训练过程中表现出更高的稳定性和更快的收敛速度。

## 🎯 应用场景

APEX技术可广泛应用于各种腿式机器人应用场景，例如搜救、巡检、物流和家庭服务等。通过学习自然、类动物的运动方式，机器人可以在复杂地形和动态环境中更高效、更安全地执行任务。此外，该方法还可以推广到其他机器人任务，如操作和抓取，从而提高机器人的自主性和适应性。

## 📄 摘要（原文）

> Learning natural, animal-like locomotion from demonstrations has become a core paradigm in legged robotics. Despite the recent advancements in motion tracking, most existing methods demand extensive tuning and rely on reference data during deployment, limiting adaptability. We present APEX (Action Priors enable Efficient Exploration), a plug-and-play extension to state-of-the-art motion tracking algorithms that eliminates any dependence on reference data during deployment, improves sample efficiency, and reduces parameter tuning effort. APEX integrates expert demonstrations directly into reinforcement learning (RL) by incorporating decaying action priors, which initially bias exploration toward expert demonstrations but gradually allow the policy to explore independently. This is combined with a multi-critic framework that balances task performance with motion style. Moreover, APEX enables a single policy to learn diverse motions and transfer reference-like styles across different terrains and velocities, while remaining robust to variations in reward design. We validate the effectiveness of our method through extensive experiments in both simulation and on a Unitree Go2 robot. By leveraging demonstrations to guide exploration during RL training, without imposing explicit bias toward them, APEX enables legged robots to learn with greater stability, efficiency, and generalization. We believe this approach paves the way for guidance-driven RL to boost natural skill acquisition in a wide array of robotic tasks, from locomotion to manipulation. Website and code: https://marmotlab.github.io/APEX/.

