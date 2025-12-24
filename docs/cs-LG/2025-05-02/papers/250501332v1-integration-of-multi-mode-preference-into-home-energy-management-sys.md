---
layout: default
title: Integration of Multi-Mode Preference into Home Energy Management System Using Deep Reinforcement Learning
---

# Integration of Multi-Mode Preference into Home Energy Management System Using Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01332" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01332v1</a>
  <a href="https://arxiv.org/pdf/2505.01332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01332v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01332v1', 'Integration of Multi-Mode Preference into Home Energy Management System Using Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammed Sumayli, Olugbenga Moses Anubi

**分类**: cs.LG, eess.SY, stat.AP

**发布日期**: 2025-05-02

**备注**: Accepted for publication in ASME journal of engineering for sustainable buildings and cities

---

## 💡 一句话要点

**提出基于深度强化学习的多模式偏好家庭能源管理系统以提升用户参与度**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `家庭能源管理` `深度强化学习` `用户偏好` `能源优化` `智能家居` `需求响应` `动态调整`

## 📋 核心要点

1. 现有的家庭能源管理系统往往忽视了消费者偏好的动态变化，导致优化效果不佳。
2. 本文提出了一种基于深度强化学习的HEMS框架，能够根据用户动态偏好进行能源优化。
3. 实验结果显示，该模型在优化能源消费方面表现优异，且计算效率高于传统方法。

## 📝 摘要（中文）

家庭能源管理系统（HEMS）在智能家居生态系统中扮演着重要角色，旨在提高能效、降低成本和改善用户舒适度。现有文献通常将消费者舒适度视为对标准设备设置的偏离，采用静态权重因子进行优化，忽视了消费者行为和偏好的动态特性。为此，本文提出了一种基于多模式深度强化学习的HEMS框架，旨在根据动态的消费者定义偏好进行优化。通过使用无模型的单代理深度强化学习算法，我们的框架不仅动态且用户友好。实验结果表明，该模型在不同偏好模式下优化能源消费表现优异，并在计算效率上超越了传统的混合整数线性规划算法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有家庭能源管理系统在优化消费者舒适度时对动态偏好的忽视问题。现有方法多依赖静态权重因子，无法适应消费者行为的变化。

**核心思路**：我们提出了一种基于深度强化学习的HEMS框架，允许用户根据个人偏好动态调整能源使用策略，从而提升用户参与度和满意度。

**技术框架**：该框架采用无模型的单代理深度强化学习算法，主要模块包括用户偏好输入、能源优化决策和反馈机制。通过实时数据（如电价、环境温度和设备功耗）进行动态调整。

**关键创新**：本研究的创新点在于引入多模式偏好机制，使得HEMS能够实时适应用户的动态需求，显著提升了系统的灵活性和用户体验。

**关键设计**：在模型设计中，采用了适应性损失函数和深度神经网络结构，确保模型能够高效处理多种输入数据，并快速做出优化决策。

## 📊 实验亮点

实验结果表明，所提出的深度强化学习模型在不同偏好模式下优化能源消费的效果显著，性能接近最优解，并在计算效率上优于传统的混合整数线性规划算法，显示出更高的实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、能源管理和需求响应程序。通过提升用户参与度和优化能源使用，能够有效降低家庭能源成本，并促进可持续发展。未来，该框架可扩展至更广泛的智能设备和能源系统中，推动智能家居技术的进一步发展。

## 📄 摘要（原文）

> Home Energy Management Systems (HEMS) have emerged as a pivotal tool in the smart home ecosystem, aiming to enhance energy efficiency, reduce costs, and improve user comfort. By enabling intelligent control and optimization of household energy consumption, HEMS plays a significant role in bridging the gap between consumer needs and energy utility objectives. However, much of the existing literature construes consumer comfort as a mere deviation from the standard appliance settings. Such deviations are typically incorporated into optimization objectives via static weighting factors. These factors often overlook the dynamic nature of consumer behaviors and preferences. Addressing this oversight, our paper introduces a multi-mode Deep Reinforcement Learning-based HEMS (DRL-HEMS) framework, meticulously designed to optimize based on dynamic, consumer-defined preferences. Our primary goal is to augment consumer involvement in Demand Response (DR) programs by embedding dynamic multi-mode preferences tailored to individual appliances. In this study, we leverage a model-free, single-agent DRL algorithm to deliver a HEMS framework that is not only dynamic but also user-friendly. To validate its efficacy, we employed real-world data at 15-minute intervals, including metrics such as electricity price, ambient temperature, and appliances' power consumption. Our results show that the model performs exceptionally well in optimizing energy consumption within different preference modes. Furthermore, when compared to traditional algorithms based on Mixed-Integer Linear Programming (MILP), our model achieves nearly optimal performance while outperforming in computational efficiency.

