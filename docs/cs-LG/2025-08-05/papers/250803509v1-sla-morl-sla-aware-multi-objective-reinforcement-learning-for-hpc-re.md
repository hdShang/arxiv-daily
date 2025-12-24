---
layout: default
title: "SLA-MORL: SLA-Aware Multi-Objective Reinforcement Learning for HPC Resource Optimization"
---

# SLA-MORL: SLA-Aware Multi-Objective Reinforcement Learning for HPC Resource Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03509" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03509v1</a>
  <a href="https://arxiv.org/pdf/2508.03509.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03509v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03509v1', 'SLA-MORL: SLA-Aware Multi-Objective Reinforcement Learning for HPC Resource Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seraj Al Mahmud Mostafa, Aravind Mohan, Jianwu Wang

**分类**: cs.LG

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出SLA-MORL以解决云环境中资源优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多目标强化学习` `云计算` `资源优化` `服务水平协议` `高性能计算` `机器学习` `动态资源分配`

## 📋 核心要点

1. 现有方法在动态资源分配中面临SLA约束与训练时间、成本之间的矛盾，导致资源浪费或SLA违约。
2. SLA-MORL通过多目标强化学习框架，智能分配资源并动态调整优化优先级，解决了冷启动和动态适应问题。
3. 在实际评估中，SLA-MORL在关键任务上显著提高了性能，训练时间减少67.2%，成本降低68.8%，SLA合规性提升73.4%。

## 📝 摘要（中文）

在云环境中，机器学习工作负载的动态资源分配面临着在满足服务水平协议(SLA)约束的同时，最小化训练时间和运营成本的挑战。传统方法采用静态资源分配或单目标优化，导致SLA违约或资源浪费。本文提出了SLA-MORL，一个自适应的多目标强化学习框架，能够根据用户定义的偏好（时间、成本或平衡）智能分配GPU和CPU资源，同时确保SLA合规。我们的创新包括通过历史学习或高效基线运行进行智能初始化，减少初始探索开销60%；以及动态权重调整，根据实时SLA违约严重性自动调整优化优先级，形成自我修正系统。实验表明，SLA-MORL在13个不同的机器学习工作负载上实现了67.2%的训练时间减少、68.8%的成本降低和73.4%的SLA合规性提升。

## 🔬 方法详解

**问题定义**：本文解决的是在云环境中机器学习工作负载的动态资源分配问题。现有方法通常采用静态资源分配或单一目标优化，导致SLA违约或资源浪费，无法有效应对多目标优化的需求。

**核心思路**：SLA-MORL的核心思路是通过多目标强化学习框架，结合用户的资源分配偏好，实现GPU和CPU资源的智能动态分配，并确保SLA合规。该方法通过历史学习和动态权重调整来优化资源配置。

**技术框架**：SLA-MORL的整体架构包括状态表示、动作选择和奖励机制。状态表示为21维，涵盖资源利用率、训练进度和SLA合规性。采用actor-critic网络进行决策，支持9种可能的资源分配动作。

**关键创新**：SLA-MORL的两大创新在于智能初始化和动态权重调整。智能初始化通过历史数据减少了冷启动问题的影响，而动态权重调整根据实时SLA违约情况自动调整优化优先级，使得系统具备自我修正能力。

**关键设计**：在参数设置上，SLA-MORL采用了基于历史学习的初始化策略，损失函数设计考虑了多目标优化的平衡，网络结构则使用了actor-critic模型，以增强决策的灵活性和准确性。

## 📊 实验亮点

在对13个不同机器学习工作负载的评估中，SLA-MORL实现了67.2%的训练时间减少，68.8%的成本降低，以及73.4%的SLA合规性提升，相较于静态基线表现出显著的优势。

## 🎯 应用场景

SLA-MORL的研究成果在云计算和高性能计算(HPC)环境中具有广泛的应用潜力，尤其适用于需要动态资源管理的机器学习任务。其智能资源分配能力能够有效降低运营成本，提高训练效率，进而推动企业在AI领域的创新和发展。

## 📄 摘要（原文）

> Dynamic resource allocation for machine learning workloads in cloud environments remains challenging due to competing objectives of minimizing training time and operational costs while meeting Service Level Agreement (SLA) constraints. Traditional approaches employ static resource allocation or single-objective optimization, leading to either SLA violations or resource waste. We present SLA-MORL, an adaptive multi-objective reinforcement learning framework that intelligently allocates GPU and CPU resources based on user-defined preferences (time, cost, or balanced) while ensuring SLA compliance. Our approach introduces two key innovations: (1) intelligent initialization through historical learning or efficient baseline runs that eliminates cold-start problems, reducing initial exploration overhead by 60%, and (2) dynamic weight adaptation that automatically adjusts optimization priorities based on real-time SLA violation severity, creating a self-correcting system. SLA-MORL constructs a 21-dimensional state representation capturing resource utilization, training progress, and SLA compliance, enabling an actor-critic network to make informed allocation decisions across 9 possible actions. Extensive evaluation on 13 diverse ML workloads using production HPC infrastructure demonstrates that SLA-MORL achieves 67.2% reduction in training time for deadline-critical jobs, 68.8% reduction in costs for budget-constrained workloads, and 73.4% improvement in overall SLA compliance compared to static baselines. By addressing both cold-start inefficiency and dynamic adaptation challenges, SLA-MORL provides a practical solution for cloud resource management that balances performance, cost, and reliability in modern ML training environments.

