---
layout: default
title: A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks
---

# A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14297" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14297v1</a>
  <a href="https://arxiv.org/pdf/2512.14297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14297v1" onclick="toggleFavorite(this, '2512.14297v1', 'A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agrippina Mwangi, León Navarro-Hilfiker, Lukasz Brewka, Mikkel Gryning, Elena Fumagalli, Madeleine Gibescu

**分类**: cs.NI, cs.AI, cs.ET, cs.PF, hep-ex

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于阈值触发深度Q网络的自愈框架，用于软件定义IIoT边缘网络**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `软件定义网络` `工业物联网` `深度强化学习` `自愈网络` `网络优化`

## 📋 核心要点

1. 工业网络易受随机中断影响，导致服务降级，现有方法难以实时适应和优化。
2. 提出一种基于阈值触发的深度Q网络自愈代理，通过强化学习自主学习网络行为，实时调整路由和资源分配。
3. 实验表明，该代理在中断恢复性能上优于现有方法，并能主动维持交换机的热稳定性。

## 📝 摘要（中文）

本研究提出了一种基于阈值触发的深度Q网络自愈代理，用于自主检测、分析和缓解软件定义工业网络中的中断，并实时调整路由行为和资源分配。这些中断通常由良性流量突发和交换机热波动等随机事件引起，违反了IEC 61850派生的服务质量要求和用户定义的服务级别协议，从而阻碍了符合IEC 61400-25标准的风力发电厂中控制、监控和尽力而为流量的可靠和及时交付。该代理在一个基于云的概念验证测试平台上部署的仿真三集群交换机网络上进行了训练、验证和测试。仿真结果表明，与基线最短路径和负载均衡路由方法相比，该代理将中断恢复性能提高了53.84%，并且在超脊叶数据平面架构中，优于最先进的方法，包括自适应网络模糊推理系统（13.1%）和基于深度Q网络和流量预测的路由优化方法（21.5%）。此外，该代理通过在需要时主动启动外部机架冷却来维持交换机的热稳定性。这些发现突出了深度强化学习在构建部署在任务关键型、时间敏感型应用场景中的软件定义工业网络中的弹性方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决软件定义工业网络中，由于随机中断（如流量突发和交换机热波动）导致的服务质量下降问题。现有方法，如静态路由和简单的负载均衡，无法有效应对这些动态变化，导致控制信号延迟或丢失，降低运营效率，增加风力发电机停机风险。

**核心思路**：论文的核心思路是利用深度强化学习（DRL）训练一个智能代理，使其能够自主学习网络行为，并根据网络状态实时调整路由策略和资源分配。通过设定阈值触发机制，代理能够及时响应网络异常，实现自愈。

**技术框架**：该框架包含以下主要模块：1) **环境建模**：模拟软件定义工业网络的拓扑结构和流量模式。2) **状态观测**：实时监测网络状态，包括链路负载、交换机温度等。3) **动作选择**：基于深度Q网络（DQN）选择合适的路由策略和资源分配方案。4) **奖励函数设计**：根据网络性能指标（如延迟、丢包率、温度）设计奖励函数，引导代理学习最优策略。5) **阈值触发机制**：当网络状态超过预设阈值时，触发代理进行自愈操作。

**关键创新**：该论文的关键创新在于：1) **阈值触发机制**：通过设定阈值，可以更及时地响应网络异常，避免性能恶化。2) **深度Q网络自愈代理**：利用DQN强大的学习能力，实现自主学习和优化，无需人工干预。3) **综合考虑网络性能和设备健康**：奖励函数不仅考虑了网络性能指标，还考虑了交换机的温度，实现了更全面的优化。

**关键设计**：1) **DQN网络结构**：采用多层感知机（MLP）作为DQN的网络结构，输入为网络状态，输出为每个动作的Q值。2) **奖励函数**：奖励函数综合考虑了延迟、丢包率和交换机温度，并设置了相应的权重。3) **阈值设置**：根据经验和实验结果，设置了链路负载和交换机温度的阈值，用于触发自愈操作。4) **探索-利用策略**：采用ε-greedy策略进行探索和利用，平衡了学习效率和性能。

## 📊 实验亮点

实验结果表明，与基线最短路径和负载均衡路由方法相比，该代理将中断恢复性能提高了53.84%。此外，该代理在超脊叶数据平面架构中，优于自适应网络模糊推理系统（13.1%）和基于深度Q网络和流量预测的路由优化方法（21.5%）。该代理还能主动维持交换机的热稳定性，避免设备过热。

## 🎯 应用场景

该研究成果可应用于各种软件定义的工业网络，特别是对实时性和可靠性要求高的场景，如智能制造、智能电网和工业物联网。通过自主学习和优化，该方法能够提高网络的弹性和效率，降低运营成本，并减少人工干预的需求。未来，该技术有望扩展到更复杂的网络环境，并与其他人工智能技术相结合，实现更智能化的网络管理。

## 📄 摘要（原文）

> Stochastic disruptions such as flash events arising from benign traffic bursts and switch thermal fluctuations are major contributors to intermittent service degradation in software-defined industrial networks. These events violate IEC~61850-derived quality-of-service requirements and user-defined service-level agreements, hindering the reliable and timely delivery of control, monitoring, and best-effort traffic in IEC~61400-25-compliant wind power plants. Failure to maintain these requirements often results in delayed or lost control signals, reduced operational efficiency, and increased risk of wind turbine generator downtime.
>   To address these challenges, this study proposes a threshold-triggered Deep Q-Network self-healing agent that autonomically detects, analyzes, and mitigates network disruptions while adapting routing behavior and resource allocation in real time. The proposed agent was trained, validated, and tested on an emulated tri-clustered switch network deployed in a cloud-based proof-of-concept testbed.
>   Simulation results show that the proposed agent improves disruption recovery performance by 53.84% compared to a baseline shortest-path and load-balanced routing approach and outperforms state-of-the-art methods, including the Adaptive Network-based Fuzzy Inference System by 13.1% and the Deep Q-Network and traffic prediction-based routing optimization method by 21.5%, in a super-spine leaf data-plane architecture.
>   Additionally, the agent maintains switch thermal stability by proactively initiating external rack cooling when required. These findings highlight the potential of deep reinforcement learning in building resilience in software-defined industrial networks deployed in mission-critical, time-sensitive application scenarios.

