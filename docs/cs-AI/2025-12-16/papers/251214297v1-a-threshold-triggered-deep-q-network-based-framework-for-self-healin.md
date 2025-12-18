---
layout: default
title: A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks
---

# A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14297" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14297v1</a>
  <a href="https://arxiv.org/pdf/2512.14297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14297v1', 'A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agrippina Mwangi, León Navarro-Hilfiker, Lukasz Brewka, Mikkel Gryning, Elena Fumagalli, Madeleine Gibescu

**分类**: cs.NI, cs.AI, cs.ET, cs.PF, hep-ex

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于阈值触发深度Q网络的自愈框架，用于软件定义IIoT边缘网络**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `软件定义网络` `工业物联网` `深度强化学习` `自愈网络` `Q网络` `路由优化` `热管理`

## 📋 核心要点

1. 软件定义工业网络易受随机扰动影响，导致服务降级，现有方法难以实时适应和优化。
2. 提出一种基于阈值触发的深度Q网络自愈代理，通过强化学习自主学习最优路由和资源分配策略。
3. 实验表明，该代理在中断恢复性能上优于现有方法，并能主动维持交换机的热稳定性。

## 📝 摘要（中文）

本研究提出了一种基于阈值触发的深度Q网络自愈代理，用于自主检测、分析和缓解软件定义工业网络中的中断，并实时调整路由行为和资源分配。这些中断通常由良性流量突发和交换机热波动等随机扰动引起，违反了IEC 61850派生的服务质量要求和用户定义的服务级别协议。该代理在一个基于云的概念验证测试平台上部署的三集群交换机网络中进行了训练、验证和测试。仿真结果表明，与基线最短路径和负载均衡路由方法相比，该代理将中断恢复性能提高了53.84%，并且优于最先进的方法，包括自适应网络模糊推理系统（13.1%）和基于深度Q网络和流量预测的路由优化方法（21.5%）。此外，该代理通过在需要时主动启动外部机架冷却来维持交换机的热稳定性。这些发现突出了深度强化学习在构建部署于任务关键型、时间敏感型应用场景中的软件定义工业网络中的弹性的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决软件定义工业物联网边缘网络中，由于流量突发、交换机热波动等随机扰动导致的网络中断问题。现有方法，如静态路由和简单的负载均衡，无法有效应对这些动态变化，导致服务质量下降，甚至影响关键控制信号的传输。现有基于预测的优化方法也存在预测不准确的问题。

**核心思路**：论文的核心思路是利用深度强化学习（DRL）训练一个智能代理，使其能够自主学习和适应网络环境的变化，实时调整路由策略和资源分配，从而实现网络的自愈。通过设置阈值触发机制，代理能够及时响应网络异常，避免性能下降。

**技术框架**：该框架包含以下主要模块：1) **环境感知模块**：负责收集网络状态信息，如链路负载、交换机温度等。2) **阈值触发模块**：当网络状态超过预设阈值时，触发自愈代理。3) **深度Q网络（DQN）代理**：根据当前网络状态选择合适的动作（如调整路由、启动冷却），并根据环境反馈更新Q值。4) **执行模块**：执行DQN代理选择的动作。5) **奖励函数设计**：奖励函数用于指导DQN代理的学习，目标是最大化网络性能和稳定性。

**关键创新**：该论文的关键创新在于：1) **阈值触发机制**：只有当网络状态超过预设阈值时才触发自愈代理，减少了不必要的干预，提高了效率。2) **深度Q网络的应用**：利用DQN强大的学习能力，使代理能够自主学习复杂的网络环境，并做出最优决策。3) **综合考虑网络性能和热稳定性**：奖励函数同时考虑了网络性能（如延迟、吞吐量）和交换机热稳定性，实现了更全面的优化。

**关键设计**：DQN采用多层感知机结构，输入为网络状态信息，输出为每个动作的Q值。奖励函数的设计至关重要，需要平衡网络性能和热稳定性之间的关系。例如，可以设置延迟降低为正奖励，温度升高为负奖励。阈值的设置也需要仔细考虑，过高可能导致响应不及时，过低可能导致频繁干预。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14297v1/Images/Fig1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14297v1/Images/Fig2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14297v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，所提出的基于阈值触发的深度Q网络自愈代理在中断恢复性能方面优于基线最短路径和负载均衡路由方法53.84%。此外，该代理的性能也优于最先进的方法，包括自适应网络模糊推理系统（13.1%）和基于深度Q网络和流量预测的路由优化方法（21.5%）。该代理还能有效维持交换机的热稳定性。

## 🎯 应用场景

该研究成果可应用于各种软件定义的工业物联网边缘网络，特别是在任务关键型和时间敏感型应用场景中，如智能制造、智能电网和工业自动化。通过实现网络的自愈能力，可以提高系统的可靠性和可用性，减少人工干预，降低运营成本，并确保关键控制信号的及时传输。

## 📄 摘要（原文）

> Stochastic disruptions such as flash events arising from benign traffic bursts and switch thermal fluctuations are major contributors to intermittent service degradation in software-defined industrial networks. These events violate IEC~61850-derived quality-of-service requirements and user-defined service-level agreements, hindering the reliable and timely delivery of control, monitoring, and best-effort traffic in IEC~61400-25-compliant wind power plants. Failure to maintain these requirements often results in delayed or lost control signals, reduced operational efficiency, and increased risk of wind turbine generator downtime.
>   To address these challenges, this study proposes a threshold-triggered Deep Q-Network self-healing agent that autonomically detects, analyzes, and mitigates network disruptions while adapting routing behavior and resource allocation in real time. The proposed agent was trained, validated, and tested on an emulated tri-clustered switch network deployed in a cloud-based proof-of-concept testbed.
>   Simulation results show that the proposed agent improves disruption recovery performance by 53.84% compared to a baseline shortest-path and load-balanced routing approach and outperforms state-of-the-art methods, including the Adaptive Network-based Fuzzy Inference System by 13.1% and the Deep Q-Network and traffic prediction-based routing optimization method by 21.5%, in a super-spine leaf data-plane architecture.
>   Additionally, the agent maintains switch thermal stability by proactively initiating external rack cooling when required. These findings highlight the potential of deep reinforcement learning in building resilience in software-defined industrial networks deployed in mission-critical, time-sensitive application scenarios.

