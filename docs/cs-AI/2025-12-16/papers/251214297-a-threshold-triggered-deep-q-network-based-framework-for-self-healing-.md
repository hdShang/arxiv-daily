---
layout: default
title: A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks
---

# A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14297" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14297</a>
  <a href="https://arxiv.org/pdf/2512.14297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14297" onclick="toggleFavorite(this, '2512.14297', 'A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agrippina Mwangi, León Navarro-Hilfiker, Lukasz Brewka, Mikkel Gryning, Elena Fumagalli, Madeleine Gibescu

**分类**: cs.NI, cs.AI, cs.ET, cs.PF

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出阈值触发深度Q网络框架以解决工业物联网边缘网络自愈问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度Q网络` `自愈机制` `工业物联网` `网络优化` `强化学习` `服务质量` `实时监测`

## 📋 核心要点

1. 现有方法在应对随机干扰时缺乏有效的自愈能力，导致服务质量下降和控制信号延迟。
2. 论文提出了一种基于阈值触发的深度Q网络自愈代理，能够实时检测和缓解网络干扰，优化资源分配。
3. 实验结果显示，该代理在干扰恢复性能上比基线方法提高了53.84%，并优于其他先进方法。

## 📝 摘要（中文）

随机干扰，如由于流量突发和交换机热波动引起的闪电事件，是软件定义工业网络中间歇性服务降级的主要原因。这些事件违反了IEC 61850衍生的服务质量要求和用户定义的服务水平协议，影响了控制、监测和尽力而为流量的可靠及时传输。为了解决这些挑战，本文提出了一种阈值触发的深度Q网络自愈代理，能够自主检测、分析和缓解网络干扰，同时实时调整路由行为和资源分配。仿真结果表明，该代理的干扰恢复性能比基线方法提高了53.84%。

## 🔬 方法详解

**问题定义**：本文旨在解决软件定义工业网络中由于随机干扰导致的服务降级问题。现有方法在应对突发流量和设备热波动时，往往无法有效保持服务质量，导致控制信号延迟或丢失。

**核心思路**：论文提出的阈值触发深度Q网络自愈代理，利用深度强化学习技术，能够自主检测和分析网络状态，并在发生干扰时实时调整路由和资源分配，以提高网络的自愈能力和稳定性。

**技术框架**：该框架包括多个模块：首先是状态检测模块，实时监测网络状态；其次是决策模块，基于深度Q网络进行干扰分析和路由优化；最后是执行模块，实施调整措施，如资源重新分配和冷却启动。

**关键创新**：最重要的技术创新在于将深度Q网络与阈值触发机制结合，能够在干扰发生前主动采取措施，从而显著提高网络的恢复能力和稳定性。这一方法与传统的被动响应机制有本质区别。

**关键设计**：在设计中，代理的训练采用了仿真环境，关键参数包括学习率、折扣因子等。损失函数设计为均方误差，以优化Q值的估计。此外，网络结构采用了深度神经网络，以提高决策的准确性和效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14297/Images/Fig1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14297/Images/Fig2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14297/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，提出的自愈代理在干扰恢复性能上比基线的最短路径和负载均衡路由方法提高了53.84%。此外，与现有的自适应网络模糊推理系统相比，性能提升达13.1%，与基于深度Q网络和流量预测的优化方法相比提升21.5%。

## 🎯 应用场景

该研究的潜在应用领域包括工业物联网、智能电网和自动化控制系统等。通过提高网络的自愈能力，可以显著提升这些领域的服务质量和可靠性，尤其是在时间敏感的应用场景中，确保控制信号的及时传输和处理。未来，该技术有望在更多关键任务和高可用性系统中得到广泛应用。

## 📄 摘要（原文）

> Stochastic disruptions such as flash events arising from benign traffic bursts and switch thermal fluctuations are major contributors to intermittent service degradation in software-defined industrial networks. These events violate IEC~61850-derived quality-of-service requirements and user-defined service-level agreements, hindering the reliable and timely delivery of control, monitoring, and best-effort traffic in IEC~61400-25-compliant wind power plants. Failure to maintain these requirements often results in delayed or lost control signals, reduced operational efficiency, and increased risk of wind turbine generator downtime.To address these challenges, this study proposes a threshold-triggered Deep Q-Network self-healing agent that autonomically detects, analyzes, and mitigates network disruptions while adapting routing behavior and resource allocation in real time. The proposed agent was trained, validated, and tested on an emulated tri-clustered switch network deployed in a cloud-based proof-of-concept testbed.Simulation results show that the proposed agent improves disruption recovery performance by 53.84% compared to a baseline shortest-path and load-balanced routing approach and outperforms state-of-the-art methods, including the Adaptive Network-based Fuzzy Inference System by 13.1% and the Deep Q-Network and traffic prediction-based routing optimization method by 21.5%, in a super-spine leaf data-plane architecture.Additionally, the agent maintains switch thermal stability by proactively initiating external rack cooling when required. These findings highlight the potential of deep reinforcement learning in building resilience in software-defined industrial networks deployed in mission-critical, time-sensitive application scenarios.

