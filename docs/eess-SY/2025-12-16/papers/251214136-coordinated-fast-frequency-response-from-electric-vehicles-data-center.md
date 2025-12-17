---
layout: default
title: Coordinated Fast Frequency Response from Electric Vehicles, Data Centers, and Battery Energy Storage Systems
---

# Coordinated Fast Frequency Response from Electric Vehicles, Data Centers, and Battery Energy Storage Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14136" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14136</a>
  <a href="https://arxiv.org/pdf/2512.14136.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14136" onclick="toggleFavorite(this, '2512.14136', 'Coordinated Fast Frequency Response from Electric Vehicles, Data Centers, and Battery Energy Storage Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaojie Tao, Rajit Gadh

**分类**: eess.SY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种协同控制框架，聚合电动汽车、数据中心和储能系统，实现快速频率响应。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `快速频率响应` `电动汽车` `数据中心` `电池储能系统` `协同控制` `电网稳定性` `可再生能源` `分层控制`

## 📋 核心要点

1. 现代电网可再生能源渗透率高，系统惯性降低，需要分布式资源提供快速频率响应，但多种资源协同潜力未被充分挖掘。
2. 提出一种分层协同控制框架，聚合电动汽车、数据中心和电池储能系统，动态分配快速频率响应，实现稳定可靠的电网频率控制。
3. 基于IEEE 39节点系统的案例研究表明，该框架能显著改善频率下冲、降低频率变化率，并加速频率恢复，提升电网稳定性。

## 📝 摘要（中文）

随着高比例可再生能源的接入，现代电网的系统惯性显著降低，对来自分布式和非传统资源的快速频率响应(FFR)需求日益增加。虽然电动汽车(EVs)、数据中心和电池储能系统(BESS)都已展示了提供亚秒级有功功率支持的能力，但它们组合的频率响应潜力尚未得到系统评估。本文提出了一种协同控制框架，该框架聚合这些异构资源以提供快速、稳定和可靠的FFR。开发了电动汽车车队、数据中心UPS和工作负载调制以及BESS的动态模型，明确捕捉了它们的响应时间、功率限制和运行约束。引入了一种分层控制架构，其中上层协调器根据响应速度和可用容量在资源之间动态分配FFR，下层控制器实现实际的功率响应。基于IEEE 39节点测试系统的案例研究表明，与单资源FFR相比，协同的EV-DC-BESS框架可将频率最低点提高高达0.2 Hz，降低RoCoF，并加速频率恢复。结果证实，协同协调显著增强了电网稳定性，尤其是在低惯性场景中。这项工作突出了多资源聚合对于可再生能源主导电网中未来频率调节市场的价值。

## 🔬 方法详解

**问题定义**：论文旨在解决高比例可再生能源接入电网后，系统惯性降低，导致电网频率稳定性下降的问题。现有方法通常依赖于单一资源提供频率响应，无法充分利用电动汽车、数据中心和储能系统等多种分布式资源的潜力，且缺乏有效的协同控制策略。

**核心思路**：论文的核心思路是通过构建一个分层协同控制框架，将电动汽车、数据中心和储能系统聚合起来，根据各自的响应特性和可用容量，动态分配快速频率响应任务。这种协同方式能够充分利用不同资源的优势，提高频率响应的速度、稳定性和可靠性。

**技术框架**：该框架采用分层控制架构。上层协调器负责监测电网频率变化，并根据预设的优化目标，动态分配各个资源的频率响应任务。下层控制器则负责根据上层指令，控制电动汽车、数据中心和储能系统输出相应的有功功率。框架包含以下主要模块：电网频率监测模块、资源状态评估模块、优化分配模块和资源控制模块。

**关键创新**：该论文的关键创新在于提出了一个多资源协同的快速频率响应框架，能够充分利用电动汽车、数据中心和储能系统的互补特性，实现更快速、更稳定的频率响应。与传统的单一资源控制方法相比，该框架能够显著提高电网的频率稳定性，尤其是在低惯性场景下。

**关键设计**：论文针对电动汽车、数据中心和储能系统分别建立了动态模型，考虑了它们的响应时间、功率限制和运行约束。上层协调器采用优化算法，根据资源的响应速度、可用容量和成本等因素，动态分配频率响应任务。下层控制器则采用PID控制或模型预测控制等方法，实现精确的功率输出。

## 📊 实验亮点

基于IEEE 39节点测试系统的案例研究表明，与单资源FFR相比，协同的EV-DC-BESS框架可将频率最低点提高高达0.2 Hz，降低RoCoF，并加速频率恢复。结果证实，协同协调显著增强了电网稳定性，尤其是在低惯性场景中。

## 🎯 应用场景

该研究成果可应用于未来高比例可再生能源接入的智能电网中，通过聚合电动汽车、数据中心和储能系统等分布式资源，提供快速频率响应，提高电网的频率稳定性，降低停电风险。该技术有助于促进可再生能源的消纳，实现能源转型。

## 📄 摘要（原文）

> High renewable penetration has significantly reduced system inertia in modern power grids, increasing the need for fast frequency response (FFR) from distributed and non-traditional resources. While electric vehicles (EVs), data centers, and battery energy storage systems (BESS) have each demonstrated the capability to provide sub-second active power support, their combined frequency response potential has not been systematically evaluated. This paper proposes a coordinated control framework that aggregates these heterogeneous resources to provide fast, stable, and reliable FFR. Dynamic models for EV fleets, data center UPS and workload modulation, and BESS are developed, explicitly capturing their response times, power limits, and operational constraints. A hierarchical control architecture is introduced, where an upper-level coordinator dynamically allocates FFR among resources based on response speed and available capacity, and lower-level controllers implement the actual power response. Case studies based on the IEEE 39-bus test system demonstrate that the coordinated EV-DC-BESS framework improves frequency nadir by up to 0.2 Hz, reduces RoCoF, and accelerates frequency recovery compared with single-resource FFR. Results confirm that synergistic coordination significantly enhances grid stability, especially in low-inertia scenarios. This work highlights the value of multi-resource aggregation for future frequency regulation markets in renewable-dominated grids.

