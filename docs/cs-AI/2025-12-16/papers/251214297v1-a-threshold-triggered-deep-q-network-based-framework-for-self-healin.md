---
layout: default
title: A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks
---

# A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks

**arXiv**: [2512.14297v1](https://arxiv.org/abs/2512.14297) | [PDF](https://arxiv.org/pdf/2512.14297.pdf)

**作者**: Agrippina Mwangi, León Navarro-Hilfiker, Lukasz Brewka, Mikkel Gryning, Elena Fumagalli, Madeleine Gibescu

**分类**: cs.NI, cs.AI, cs.ET, cs.PF, hep-ex

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于阈值触发的深度Q网络自愈框架，以解决软件定义工业物联网边缘网络中随机中断问题。**

**关键词**: `深度强化学习` `软件定义网络` `工业物联网` `自愈网络` `路由优化` `热管理` `边缘计算` `网络弹性`

## 📋 核心要点

1. 核心问题：随机中断（如流量突发和热波动）导致软件定义工业网络服务降级，违反服务质量要求，影响控制信号可靠交付。
2. 方法要点：提出阈值触发的深度Q网络自愈代理，自主检测、分析和缓解中断，实时调整路由和资源分配。
3. 实验或效果：在模拟网络中测试，中断恢复性能比基线方法提升53.84%，优于现有先进方法，并维持交换机热稳定性。

## 📝 摘要（中文）

软件定义工业网络中的随机中断（如良性流量突发和交换机热波动导致的闪断事件）是导致间歇性服务降级的主要原因，这些事件违反了IEC 61850衍生的服务质量要求和用户定义的服务级别协议，阻碍了符合IEC 61400-25的风力发电厂中控制、监控和尽力而为流量的可靠及时交付。未能维持这些要求通常会导致控制信号延迟或丢失、运行效率降低以及风力涡轮发电机停机风险增加。为解决这些挑战，本研究提出了一种阈值触发的深度Q网络自愈代理，能够自主检测、分析和缓解网络中断，同时实时调整路由行为和资源分配。该代理在基于云的概念验证测试平台中部署的模拟三集群交换机网络上进行了训练、验证和测试。仿真结果表明，与基线最短路径和负载均衡路由方法相比，所提出的代理将中断恢复性能提高了53.84%，并在超骨干叶数据平面架构中优于最先进的方法，包括自适应网络模糊推理系统（提升13.1%）以及基于深度Q网络和流量预测的路由优化方法（提升21.5%）。此外，该代理在需要时通过主动启动外部机架冷却来维持交换机热稳定性。这些发现突显了深度强化学习在构建部署在关键任务、时间敏感应用场景中的软件定义工业网络弹性方面的潜力。

## 🔬 方法详解

论文提出一个基于阈值触发的深度Q网络（DQN）自愈框架，整体框架包括一个自愈代理，通过深度强化学习在软件定义工业物联网边缘网络中实现自主网络管理。关键技术创新点在于结合阈值触发机制，当网络指标（如延迟或热波动）超过预设阈值时，触发DQN代理进行决策，以实时调整路由行为和资源分配，从而检测、分析和缓解随机中断。与现有方法的主要区别在于：它集成了自适应路由优化和热管理，而传统方法如最短路径路由或基于模糊推理的系统缺乏这种综合性和实时性；同时，相比纯DQN方法，阈值触发提高了决策效率，减少了不必要的计算开销。

## 📊 实验亮点

最重要的实验结果是：在模拟三集群交换机网络中，所提出的自愈代理将中断恢复性能比基线最短路径和负载均衡路由方法提高了53.84%；同时，在超骨干叶数据平面架构中，它优于自适应网络模糊推理系统（提升13.1%）和基于深度Q网络与流量预测的路由优化方法（提升21.5%），并有效维持了交换机热稳定性。

## 🎯 应用场景

该研究主要应用于软件定义工业物联网边缘网络，特别是在关键任务和时间敏感场景中，如风力发电厂的控制和监控系统。潜在应用领域包括智能电网、工业自动化和其他需要高可靠性和低延迟的网络环境，实际价值在于提升网络弹性和运行效率，减少停机风险。

## 📄 摘要（原文）

> Stochastic disruptions such as flash events arising from benign traffic bursts and switch thermal fluctuations are major contributors to intermittent service degradation in software-defined industrial networks. These events violate IEC~61850-derived quality-of-service requirements and user-defined service-level agreements, hindering the reliable and timely delivery of control, monitoring, and best-effort traffic in IEC~61400-25-compliant wind power plants. Failure to maintain these requirements often results in delayed or lost control signals, reduced operational efficiency, and increased risk of wind turbine generator downtime.
>   To address these challenges, this study proposes a threshold-triggered Deep Q-Network self-healing agent that autonomically detects, analyzes, and mitigates network disruptions while adapting routing behavior and resource allocation in real time. The proposed agent was trained, validated, and tested on an emulated tri-clustered switch network deployed in a cloud-based proof-of-concept testbed.
>   Simulation results show that the proposed agent improves disruption recovery performance by 53.84% compared to a baseline shortest-path and load-balanced routing approach and outperforms state-of-the-art methods, including the Adaptive Network-based Fuzzy Inference System by 13.1% and the Deep Q-Network and traffic prediction-based routing optimization method by 21.5%, in a super-spine leaf data-plane architecture.
>   Additionally, the agent maintains switch thermal stability by proactively initiating external rack cooling when required. These findings highlight the potential of deep reinforcement learning in building resilience in software-defined industrial networks deployed in mission-critical, time-sensitive application scenarios.

