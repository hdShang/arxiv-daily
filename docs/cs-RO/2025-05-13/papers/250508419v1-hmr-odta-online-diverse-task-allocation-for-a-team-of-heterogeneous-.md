---
layout: default
title: HMR-ODTA: Online Diverse Task Allocation for a Team of Heterogeneous Mobile Robots
---

# HMR-ODTA: Online Diverse Task Allocation for a Team of Heterogeneous Mobile Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08419" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08419v1</a>
  <a href="https://arxiv.org/pdf/2505.08419.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08419v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08419v1', 'HMR-ODTA: Online Diverse Task Allocation for a Team of Heterogeneous Mobile Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ashish Verma, Avinash Gautam, Tanishq Duhan, V. S. Shekhawat, Sudeept Mohan

**分类**: cs.RO

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出HMR-ODTA以解决异构移动机器人在线多任务分配问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `异构机器人` `动态调度` `多任务分配` `时间窗口` `在线优化` `服务机器人` `协调算法`

## 📋 核心要点

1. 现有方法未能有效处理动态重新调度和多样化服务需求，限制了机器人任务的灵活性。
2. 提出HMR-ODTA算法，通过异构机器人团队和动态调度机制，优化任务分配以满足时间约束。
3. 实验结果表明，算法在较小任务集上罚款减少近63%，在较大任务集上减少约50%，显著提升了调度效率。

## 📝 摘要（中文）

在医院等环境中，协调时间敏感的交付任务是一项复杂的挑战，尤其是在严格的时间窗口内管理多个在线取送请求时。传统方法未能有效应对动态重新调度或多样化服务需求，通常将机器人限制为单一任务类型。本文针对具有时间窗口的多取送问题（MPDPTW），提出了一种新颖的框架，利用异构机器人团队和高效的动态调度算法，支持动态任务重新调度。用户提交具有特定时间约束的请求，HMR-ODTA算法优化任务分配，以确保及时服务并处理延误或任务拒绝。大量仿真实验证明了该算法的有效性，对于较小的任务集（40-160个任务），罚款减少了近63%，而对于较大的任务集（160-280个任务），罚款减少了约50%。这些结果突显了该算法在多机器人系统中改善任务调度和协调的有效性，为在结构化、时间敏感的环境中提升交付性能提供了强有力的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决多取送问题（MPDPTW），现有方法在动态调度和多样化服务需求上存在不足，无法有效应对实时任务分配的挑战。

**核心思路**：HMR-ODTA算法通过利用异构机器人团队的优势，结合动态调度机制，能够灵活应对用户提交的具有时间约束的任务请求，从而优化任务分配。

**技术框架**：该框架包括任务请求接收、任务分配优化、动态调度和任务执行四个主要模块。首先接收用户请求，然后通过算法优化任务分配，最后进行动态调度以应对实时变化。

**关键创新**：HMR-ODTA的核心创新在于其支持动态任务重新调度的能力，允许机器人在任务执行过程中根据实时情况调整分配，与传统方法相比，显著提升了灵活性和效率。

**关键设计**：算法设计中考虑了任务的时间窗口、机器人能力和任务优先级等因素，采用了适应性调度策略，以确保在复杂环境中实现高效的任务分配和执行。

## 📊 实验亮点

实验结果显示，HMR-ODTA算法在较小任务集（40-160个任务）上罚款减少近63%，在较大任务集（160-280个任务）上减少约50%。这些数据表明，该算法在多机器人任务调度中的有效性和优越性，显著提升了任务完成率和服务及时性。

## 🎯 应用场景

该研究可广泛应用于医院、物流中心和智能仓储等领域，尤其是在需要快速响应和高效调度的时间敏感环境中。通过提升多机器人系统的协调能力，能够显著提高服务质量和客户满意度，未来可能推动智能配送和服务机器人技术的发展。

## 📄 摘要（原文）

> Coordinating time-sensitive deliveries in environments like hospitals poses a complex challenge, particularly when managing multiple online pickup and delivery requests within strict time windows using a team of heterogeneous robots. Traditional approaches fail to address dynamic rescheduling or diverse service requirements, typically restricting robots to single-task types. This paper tackles the Multi-Pickup and Delivery Problem with Time Windows (MPDPTW), where autonomous mobile robots are capable of handling varied service requests. The objective is to minimize late delivery penalties while maximizing task completion rates. To achieve this, we propose a novel framework leveraging a heterogeneous robot team and an efficient dynamic scheduling algorithm that supports dynamic task rescheduling. Users submit requests with specific time constraints, and our decentralized algorithm, Heterogeneous Mobile Robots Online Diverse Task Allocation (HMR-ODTA), optimizes task assignments to ensure timely service while addressing delays or task rejections. Extensive simulations validate the algorithm's effectiveness. For smaller task sets (40-160 tasks), penalties were reduced by nearly 63%, while for larger sets (160-280 tasks), penalties decreased by approximately 50%. These results highlight the algorithm's effectiveness in improving task scheduling and coordination in multi-robot systems, offering a robust solution for enhancing delivery performance in structured, time-critical environments.

