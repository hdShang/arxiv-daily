---
layout: default
title: Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning
---

# Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16813" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16813v1</a>
  <a href="https://arxiv.org/pdf/2512.16813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16813v1', 'Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bahman Abolhassani, Tugba Erpek, Kemal Davaslioglu, Yalin E. Sagduyu, Sastry Kompella

**分类**: cs.NI, cs.AI, cs.DC, cs.LG, eess.SP

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于QMIX的多智能体强化学习方法，提升集群网络在反应式干扰下的抗干扰能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `集群网络` `抗干扰` `反应式干扰` `QMIX` `通信安全`

## 📋 核心要点

1. 现有固定功率或静态信道跳频等方法难以有效应对反应式干扰对集群通信的威胁。
2. 采用基于QMIX的多智能体强化学习框架，使智能体能够协同选择信道和功率，提升抗干扰能力。
3. 实验表明，QMIX能快速收敛到接近最优的策略，显著提高吞吐量并降低干扰发生率。

## 📝 摘要（中文）

本文提出了一种基于QMIX算法的多智能体强化学习(MARL)框架，旨在提高集群通信在反应式干扰下的弹性。反应式干扰机会选择性地干扰智能体间的通信，从而破坏集群的完整性和任务成功率，对机器人集群网络构成严重的安全威胁。传统的对策，如固定功率控制或静态信道跳频，在很大程度上对这种自适应的对抗无效。本文考虑了一个多发射机-接收机对共享信道的网络，同时一个具有马尔可夫阈值动态的反应式干扰机感知总功率并做出相应反应。每个智能体联合选择发射频率（信道）和功率，QMIX学习一个集中式但可分解的动作价值函数，从而实现协调但分散的执行。我们将QMIX与无信道复用设置中的genie-aided最优策略，以及在启用信道复用的更一般的衰落机制下的局部上限置信区间(UCB)和无状态反应策略进行基准测试。仿真结果表明，QMIX迅速收敛到接近genie-aided界限的协作策略，同时比基线实现更高的吞吐量和更低的干扰发生率，从而证明了MARL在竞争环境中保护自主集群的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人集群网络在反应式干扰下的通信安全问题。现有的固定功率控制和静态信道跳频等方法无法有效应对自适应的反应式干扰，导致集群通信中断，影响任务完成。反应式干扰机会根据感知到的总功率动态调整干扰策略，使得传统的静态防御手段失效。

**核心思路**：论文的核心思路是利用多智能体强化学习（MARL）来训练集群中的每个智能体，使其能够协同选择合适的信道和发射功率，从而避开干扰，提高通信的可靠性和效率。通过学习一个集中式但可分解的动作价值函数，实现智能体间的协调，同时保持分散执行的灵活性。

**技术框架**：整体框架包含多个发射机-接收机对，它们共享信道进行通信。一个反应式干扰机监听信道，并根据感知到的总功率决定是否进行干扰。每个智能体（发射机）通过QMIX算法学习最优的信道和功率选择策略。QMIX算法包含一个全局的混合网络，用于将每个智能体的局部Q值函数混合成一个全局的Q值函数，从而实现集中式训练和分散式执行。

**关键创新**：论文的关键创新在于将QMIX算法应用于集群网络的抗干扰问题，并设计了合适的奖励函数和状态空间，使得智能体能够学习到协同的抗干扰策略。与传统的单智能体强化学习方法相比，QMIX能够更好地处理多智能体环境中的信用分配问题，从而实现更有效的协同。此外，论文还考虑了反应式干扰机的自适应行为，使得学习到的策略更具鲁棒性。

**关键设计**：论文中，每个智能体的状态包括自身发射功率、信道状态信息以及邻居智能体的状态信息。动作空间包括可选择的信道和功率等级。奖励函数的设计旨在鼓励智能体成功传输数据包，同时避免被干扰。QMIX算法中的混合网络采用非线性结构，以更好地捕捉智能体之间的复杂关系。训练过程中，采用经验回放和目标网络等技术来提高学习的稳定性和效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16813v1/topology.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16813v1/based10.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16813v1/based8.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，QMIX算法能够快速收敛到接近genie-aided最优策略的性能水平，在吞吐量方面优于局部UCB和无状态反应策略等基线方法。具体而言，QMIX能够显著降低干扰发生率，并提高数据包的成功传输率。在信道复用场景下，QMIX仍然能够保持较高的性能，证明了其在复杂环境下的鲁棒性。

## 🎯 应用场景

该研究成果可应用于各种需要高可靠性通信的集群机器人系统，例如：灾难救援、环境监测、军事侦察等。通过提升集群网络在复杂电磁环境下的抗干扰能力，可以确保集群任务的顺利完成，具有重要的实际应用价值和军事意义。未来，该方法可以进一步扩展到更大规模的集群网络，并与其他抗干扰技术相结合，以实现更强大的抗干扰能力。

## 📄 摘要（原文）

> Reactive jammers pose a severe security threat to robotic-swarm networks by selectively disrupting inter-agent communications and undermining formation integrity and mission success. Conventional countermeasures such as fixed power control or static channel hopping are largely ineffective against such adaptive adversaries. This paper presents a multi-agent reinforcement learning (MARL) framework based on the QMIX algorithm to improve the resilience of swarm communications under reactive jamming. We consider a network of multiple transmitter-receiver pairs sharing channels while a reactive jammer with Markovian threshold dynamics senses aggregate power and reacts accordingly. Each agent jointly selects transmit frequency (channel) and power, and QMIX learns a centralized but factorizable action-value function that enables coordinated yet decentralized execution. We benchmark QMIX against a genie-aided optimal policy in a no-channel-reuse setting, and against local Upper Confidence Bound (UCB) and a stateless reactive policy in a more general fading regime with channel reuse enabled. Simulation results show that QMIX rapidly converges to cooperative policies that nearly match the genie-aided bound, while achieving higher throughput and lower jamming incidence than the baselines, thereby demonstrating MARL's effectiveness for securing autonomous swarms in contested environments.

