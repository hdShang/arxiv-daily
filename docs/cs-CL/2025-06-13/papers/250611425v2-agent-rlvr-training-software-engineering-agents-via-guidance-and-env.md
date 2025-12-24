---
layout: default
title: "Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards"
---

# Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11425" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11425v2</a>
  <a href="https://arxiv.org/pdf/2506.11425.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11425v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11425v2', 'Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeff Da, Clinton Wang, Xiang Deng, Yuntao Ma, Nikhil Barhate, Sean Hendryx

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-06-20)

---

## 💡 一句话要点

**提出Agent-RLVR以解决复杂软件工程任务中的奖励稀疏问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `软件工程` `代理指导` `可验证奖励` `多步骤问题解决` `智能编程助手`

## 📋 核心要点

1. 现有的RLVR方法在复杂的代理环境中表现不佳，导致高失败率，尤其是在多步骤问题解决中。
2. Agent-RLVR通过引入代理指导机制，利用多种信息线索来引导代理，帮助其在复杂任务中找到成功路径。
3. 实验结果显示，Agent-RLVR将Qwen-2.5-72B-Instruct在SWE-Bench Verified上的pass@1性能从9.4%提升至22.4%，并进一步提升至27.8%。

## 📝 摘要（中文）

可验证奖励的强化学习（RLVR）已成为提升大型语言模型推理能力的主要方法，并在数学和竞争编程等可验证领域取得了显著成功。然而，当应用于代理环境时，RLVR的有效性显著降低，这些环境通常涉及多步骤的复杂问题解决，导致高失败率。本文提出了Agent-RLVR框架，通过引入代理指导机制，利用多样的信息线索引导代理朝向成功轨迹，从而在软件工程任务中提升RLVR的效果。实验结果表明，Agent-RLVR显著提高了Qwen-2.5-72B-Instruct在SWE-Bench Verified上的pass@1性能，从9.4%提升至22.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决RLVR在复杂代理环境中的低效问题，尤其是在多步骤问题解决时，奖励稀疏导致的训练困难。

**核心思路**：Agent-RLVR通过引入代理指导机制，模拟人类教师的引导，帮助代理在复杂任务中找到成功路径，促进自我改进。

**技术框架**：Agent-RLVR的训练流程包括：代理首先尝试解决任务生成初始轨迹，随后通过单元测试验证这些轨迹，并结合代理指导进行再尝试，最后基于这些指导轨迹的奖励更新代理策略。

**关键创新**：最重要的创新在于引入了代理指导机制，通过多样的信息线索引导代理，显著提升了RLVR在复杂环境中的有效性。

**关键设计**：在训练过程中，设计了多种信息线索，包括高层战略计划和动态反馈，以增强代理的学习能力和环境探索能力。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文。

## 📊 实验亮点

实验结果表明，Agent-RLVR显著提升了Qwen-2.5-72B-Instruct在SWE-Bench Verified上的pass@1性能，从9.4%提升至22.4%，并通过指导增强的数据进一步提升至27.8%。这一成果展示了在复杂环境中应用RLVR的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程、自动化测试和智能编程助手等。通过提升代理在复杂任务中的表现，Agent-RLVR有望在实际软件开发中提供更高效的支持，推动智能化软件工程的发展。未来，该方法还可以扩展到其他需要复杂决策和多步骤推理的领域。

## 📄 摘要（原文）

> Reinforcement Learning from Verifiable Rewards (RLVR) has been widely adopted as the de facto method for enhancing the reasoning capabilities of large language models and has demonstrated notable success in verifiable domains like math and competitive programming tasks. However, the efficacy of RLVR diminishes significantly when applied to agentic environments. These settings, characterized by multi-step, complex problem solving, lead to high failure rates even for frontier LLMs, as the reward landscape is too sparse for effective model training via conventional RLVR. In this work, we introduce Agent-RLVR, a framework that makes RLVR effective in challenging agentic settings, with an initial focus on software engineering tasks. Inspired by human pedagogy, Agent-RLVR introduces agent guidance, a mechanism that actively steers the agent towards successful trajectories by leveraging diverse informational cues. These cues, ranging from high-level strategic plans to dynamic feedback on the agent's errors and environmental interactions, emulate a teacher's guidance, enabling the agent to navigate difficult solution spaces and promotes active self-improvement via additional environment exploration. In the Agent-RLVR training loop, agents first attempt to solve tasks to produce initial trajectories, which are then validated by unit tests and supplemented with agent guidance. Agents then reattempt with guidance, and the agent policy is updated with RLVR based on the rewards of these guided trajectories. Agent-RLVR elevates the pass@1 performance of Qwen-2.5-72B-Instruct from 9.4% to 22.4% on SWE-Bench Verified. We find that our guidance-augmented RLVR data is additionally useful for test-time reward model training, shown by further boosting pass@1 to 27.8%. Agent-RLVR lays the groundwork for training agents with RLVR in complex, real-world environments where conventional RL methods struggle.

