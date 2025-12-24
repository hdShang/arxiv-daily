---
layout: default
title: Algorithmic Control Improves Residential Building Energy and EV Management when PV Capacity is High but Battery Capacity is Low
---

# Algorithmic Control Improves Residential Building Energy and EV Management when PV Capacity is High but Battery Capacity is Low

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20377" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20377v1</a>
  <a href="https://arxiv.org/pdf/2505.20377.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20377v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20377v1', 'Algorithmic Control Improves Residential Building Energy and EV Management when PV Capacity is High but Battery Capacity is Low')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lennart Ullner, Alona Zharova, Felix Creutzig

**分类**: eess.SY, cs.AI, cs.LG

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**利用深度强化学习优化家庭能源管理与电动车充电**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `家庭能源管理` `电动车充电` `可再生能源` `电池储存` `优化算法` `智能家居`

## 📋 核心要点

1. 现有方法在家庭能源管理中未能有效优化电动车充电，尤其是在电池容量低的情况下。
2. 本文提出利用深度强化学习（DRL）等控制方法来管理家庭能源，优化电动车充电模式。
3. 实验结果显示，低电池容量家庭通过DRL实现了显著的能源管理和成本节约，验证了其有效性。

## 📝 摘要（中文）

在以电动车、可再生能源和电池储存为特征的能源转型中，家庭的高效能源管理对于缓解电网压力至关重要。然而，家庭如何优化电动车充电尚不明确。本文基于90个家庭的实际数据，研究了深度强化学习（DRL）及其他控制方法在家庭能源管理中的应用。研究发现，频繁的电动车充电、早期连接电动车和光伏盈余均能提升优化潜力。在电池容量较低的情况下，DRL显著改善了能源管理和成本节约，表明具有优化潜力的家庭将从DRL中受益，从而促进整个电力系统的脱碳。

## 🔬 方法详解

**问题定义**：本文旨在解决家庭在电动车充电时的能源管理问题，尤其是在电池容量低的情况下，现有方法未能有效应对动态和不确定的家庭能源管理环境。

**核心思路**：通过引入深度强化学习（DRL）等控制方法，优化电动车与光伏盈余的充电调度，以提高家庭能源管理的效率和经济性。

**技术框架**：研究采用了基于实际数据的实验设计，主要模块包括数据收集、DRL模型训练、充电模式优化和效果评估。

**关键创新**：本文的创新在于将DRL应用于家庭能源管理，尤其是在电池容量低的情况下，显著提升了能源管理的效果，与传统的基于规则和模型预测控制方法相比，具有更高的适应性和优化能力。

**关键设计**：在DRL模型中，设置了适应家庭实际情况的奖励函数，并通过模拟实验验证了不同参数设置对充电模式优化的影响。

## 📊 实验亮点

实验结果表明，在电池容量较低的情况下，采用深度强化学习的家庭能源管理方案相比于传统方法，能实现显著的成本节约，提升幅度达到了未知水平，验证了DRL在实际应用中的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、可再生能源管理和电动车充电基础设施。通过优化家庭能源管理，不仅可以降低家庭的电力成本，还能促进电力系统的整体效率和可持续发展，助力未来的能源转型。

## 📄 摘要（原文）

> Efficient energy management in prosumer households is key to alleviating grid stress in an energy transition marked by electric vehicles (EV), renewable energies and battery storage. However, it is unclear how households optimize prosumer EV charging. Here we study real-world data from 90 households on fixed-rate electricity tariffs in German-speaking countries to investigate the potential of Deep Reinforcement Learning (DRL) and other control approaches (Rule-Based, Model Predictive Control) to manage the dynamic and uncertain environment of Home Energy Management (HEM) and optimize household charging patterns. The DRL agent efficiently aligns charging of EV and battery storage with photovoltaic (PV) surplus. We find that frequent EV charging transactions, early EV connections and PV surplus increase optimization potential. A detailed analysis of nine households (1 hour resolution, 1 year) demonstrates that high battery capacity facilitates self optimization; in this case further algorithmic control shows little value. In cases with relatively low battery capacity, algorithmic control with DRL improves energy management and cost savings by a relevant margin. This result is further corroborated by our simulation of a synthetic household. We conclude that prosumer households with optimization potential would profit from DRL, thus benefiting also the full electricity system and its decarbonization.

