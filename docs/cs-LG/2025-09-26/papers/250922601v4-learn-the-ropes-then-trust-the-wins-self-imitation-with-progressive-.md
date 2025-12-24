---
layout: default
title: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"
---

# Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22601" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22601v4</a>
  <a href="https://arxiv.org/pdf/2509.22601.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22601v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22601v4', 'Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yulei Qin, Xiaoyu Tan, Zhengbao He, Gang Li, Haojia Lin, Zongyi Li, Zihan Xu, Yuchen Shi, Siqi Cai, Renting Rui, Shaofei Cai, Yuzheng Cai, Xuan Zhang, Sheng Ye, Ke Li, Xing Sun

**分类**: cs.LG, cs.AI, cs.CL, cs.CV, cs.MA

**发布日期**: 2025-09-26 (更新: 2025-12-07)

**备注**: 45 pages, 14 figures

---

## 💡 一句话要点

**SPEAR：基于自模仿学习和渐进探索的Agentic强化学习方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `自模仿学习` `探索-利用平衡` `Agentic LLM` `课程学习`

## 📋 核心要点

1. 现有强化学习方法在Agent任务中，依赖策略熵促进探索，易导致多轮分布偏移和RL不稳定。
2. SPEAR方法通过自模仿学习，结合课程调度，逐步调整策略熵，平衡探索与利用。
3. 实验表明，SPEAR在ALFWorld、WebShop和AIME等任务中，显著提升了现有基线的成功率。

## 📝 摘要（中文）

强化学习是提升LLM在长时程、稀疏奖励Agent任务中战略性工具使用能力的主要范式，但面临探索-利用的根本挑战。现有研究通过策略熵来促进探索，但这种机械的熵最大化容易因多轮分布偏移导致RL不稳定。本文旨在Agent自身经验指导下实现渐进的探索-利用平衡，避免熵崩溃或失控发散。我们提出SPEAR，一种用于训练Agentic LLM的自模仿学习（SIL）方法。它扩展了vanilla SIL，通过逐步调整策略熵来分阶段地引导探索。具体而言，所提出的课程调度协调了内在奖励塑造和自模仿，以1）在开始时通过频繁的工具交互来加速探索，以及2）在熟悉环境后加强对成功策略的利用。我们还结合了工业RL优化技巧，构建了一个强大的基线Dr.BoT来展示我们的有效性。在ALFWorld和WebShop中，SPEAR将GRPO/GiGPO/Dr.BoT的成功率分别提高了高达16.1%/5.1%/8.6%和20.7%/11.8%/13.9%。在AIME24和AIME25中，SPEAR将Dr.BoT分别提高了高达3.8%和6.1%。这些收益仅带来10%-25%的额外理论复杂性，并且在实践中运行时开销可忽略不计，证明了SPEAR的即插即用可扩展性。

## 🔬 方法详解

**问题定义**：论文旨在解决Agentic强化学习中探索-利用的难题，特别是在长时程、稀疏奖励任务中。现有方法，如基于策略熵最大化的探索策略，容易导致RL训练不稳定，出现熵崩溃或策略发散等问题。这些问题阻碍了Agent有效学习和利用环境中的知识。

**核心思路**：SPEAR的核心思路是利用Agent自身的经验，通过自模仿学习（SIL）来引导探索。它不是简单地最大化策略熵，而是采用一种渐进式的探索策略，即在训练初期鼓励探索，在训练后期侧重利用。这种策略能够更好地平衡探索和利用，避免RL训练中的不稳定现象。

**技术框架**：SPEAR的技术框架主要包括以下几个阶段：1）经验收集：Agent与环境交互，收集经验数据；2）经验回放：将收集到的经验存储在回放缓冲区中；3）自模仿学习：从回放缓冲区中采样好的经验，用于更新Agent的策略；4）课程调度：根据训练进度，动态调整探索的强度。通过课程调度，在训练初期，Agent会更频繁地与环境交互，探索新的策略；在训练后期，Agent会更多地利用已知的成功策略。

**关键创新**：SPEAR的关键创新在于其渐进式的探索策略和课程调度机制。与传统的基于策略熵最大化的探索方法不同，SPEAR能够根据Agent的学习进度，动态调整探索的强度，从而更好地平衡探索和利用。此外，SPEAR还结合了自模仿学习，利用Agent自身的经验来指导探索，进一步提高了学习效率。

**关键设计**：SPEAR的关键设计包括：1）内在奖励塑造：通过设计内在奖励函数，鼓励Agent探索新的策略；2）自模仿损失函数：通过最小化当前策略与历史成功策略之间的差异，来提高策略的稳定性；3）课程调度策略：根据训练进度，动态调整内在奖励的权重和自模仿损失函数的系数。具体的参数设置需要根据不同的任务进行调整，但总体目标是确保Agent在训练初期能够充分探索，在训练后期能够有效利用。

## 📊 实验亮点

SPEAR在ALFWorld和WebShop等多个Agentic强化学习基准测试中取得了显著的性能提升。具体而言，SPEAR将GRPO/GiGPO/Dr.BoT在ALFWorld中的成功率分别提高了高达16.1%/5.1%/8.6%，在WebShop中提高了20.7%/11.8%/13.9%。此外，在AIME24和AIME25中，SPEAR将Dr.BoT分别提高了高达3.8%和6.1%。这些结果表明，SPEAR是一种有效且通用的Agentic强化学习方法。

## 🎯 应用场景

SPEAR方法具有广泛的应用前景，可应用于各种需要智能体与环境交互的任务，例如游戏AI、机器人控制、自动驾驶、对话系统等。通过提高智能体在复杂环境中的探索和利用能力，SPEAR能够帮助智能体更好地完成任务，提高效率和性能。该研究对于开发更智能、更可靠的智能体具有重要的实际价值。

## 📄 摘要（原文）

> Reinforcement learning (RL) is the dominant paradigm for sharpening strategic tool use capabilities of LLMs on long-horizon, sparsely-rewarded agent tasks, yet it faces a fundamental challenge of exploration-exploitation trade-off. Existing studies stimulate exploration through the lens of policy entropy, but such mechanical entropy maximization is prone to RL instability due to the multi-turn distribution shifting. In this paper, we target the progressive exploration-exploitation balance under the guidance of the agent's own experiences without succumbing to either entropy collapsing or runaway divergence. We propose SPEAR, a self-imitation learning (SIL) recipe for training agentic LLMs. It extends the vanilla SIL, where a replay buffer stores good experience for off-policy update, by gradually steering the policy entropy across stages. Specifically, the proposed curriculum scheduling harmonizes intrinsic reward shaping and self-imitation to 1) expedite exploration via frequent tool interactions at the beginning, and 2) strengthen exploitation of successful tactics upon convergence towards familiarity with the environment. We also combine bag-of-tricks of industrial RL optimizations for a strong baseline Dr.BoT to demonstrate our effectiveness. In ALFWorld and WebShop, SPEAR increases the success rates of GRPO/GiGPO/Dr.BoT by up to 16.1%/5.1%/8.6% and 20.7%/11.8%/13.9%, respectively. In AIME24 and AIME25, SPEAR boosts Dr.BoT by up to 3.8% and 6.1%, respectively. Such gains incur only 10%-25% extra theoretical complexity and negligible runtime overhead in practice, demonstrating the plug-and-play scalability of SPEAR.

