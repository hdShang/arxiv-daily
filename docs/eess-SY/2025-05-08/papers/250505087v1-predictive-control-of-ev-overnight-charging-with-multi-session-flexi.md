---
layout: default
title: Predictive Control of EV Overnight Charging with Multi-Session Flexibility
---

# Predictive Control of EV Overnight Charging with Multi-Session Flexibility

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05087" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05087v1</a>
  <a href="https://arxiv.org/pdf/2505.05087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05087v1', 'Predictive Control of EV Overnight Charging with Multi-Session Flexibility')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Felix Wieberneit, Emanuele Crisostomi, Anthony Quinn, Robert Shorten

**分类**: eess.SY

**发布日期**: 2025-05-08

---

## 💡 一句话要点

**提出多会话灵活性预测控制以优化电动车夜间充电**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `电动车充电` `模型预测控制` `二氧化碳减排` `智能电网` `能源灵活性` `家庭能源管理` `可再生能源利用`

## 📋 核心要点

1. 现有方法通常假设电动车每晨需充满电，限制了充电灵活性，导致能源利用效率低下。
2. 本文提出了一种基于模型预测控制（MPC）的调度策略，允许将充电推迟至后续夜晚，从而优化电力分配。
3. 实验结果表明，多会话规划在减少二氧化碳排放方面具有显著优势，最高可减少46%的排放量。

## 📝 摘要（中文）

大多数电动车（EV）在家中夜间充电，用户对充电时间的精确性要求不高，因此这一特性为充电控制算法提供了灵活性。本文放宽了电动车每晨需充满电的假设，允许将多余的能量充电推迟至后续夜晚，从而提升控制充电的性能。我们考虑使用简单的家庭智能插座，调度电力供应，以最小化多会话预测期内的二氧化碳排放，最长可达七天。基于英国国家电网的碳强度数据，我们展示了多会话规划在减少排放方面的显著潜力，相较于无控制充电可减少40%至46%的排放，相较于单会话规划可减少19%至26%。此外，我们评估了电动车用户的驾驶和充电行为如何影响可用灵活性及其对减排潜力的影响。

## 🔬 方法详解

**问题定义**：本文旨在解决电动车夜间充电灵活性不足的问题。现有方法假设电动车每晨需充满电，导致充电调度缺乏灵活性，无法有效利用可再生能源。

**核心思路**：论文提出了一种新的调度策略，允许将多余的充电推迟至后续夜晚，利用模型预测控制（MPC）优化电力分配，以最小化二氧化碳排放。

**技术框架**：整体架构包括数据收集、碳强度预测、充电调度和执行四个主要模块。首先收集电网的碳强度数据，然后进行预测，接着基于预测结果进行充电调度，最后通过智能插座执行调度策略。

**关键创新**：最重要的技术创新在于引入多会话灵活性，允许充电推迟，从而显著提高了电力利用效率和减排效果。这与传统的单一会话充电方法形成了鲜明对比。

**关键设计**：在模型预测控制中，设置了碳排放的损失函数，并考虑了用户的充电行为和驾驶模式，以优化调度策略的灵活性和有效性。

## 📊 实验亮点

实验结果显示，采用多会话规划的充电策略相比于无控制充电可减少40%至46%的二氧化碳排放，相较于单会话规划可减少19%至26%。此外，基于14个不同地区的碳强度数据，研究还揭示了地方能源结构对减排效果的显著影响。

## 🎯 应用场景

该研究的潜在应用领域包括家庭电动车充电管理、智能电网优化及可再生能源的高效利用。通过优化充电调度，不仅可以降低用户的电费支出，还能有效减少碳排放，推动可持续发展。未来，该方法可扩展至更大规模的电动车充电网络，进一步提升电力系统的灵活性和可靠性。

## 📄 摘要（原文）

> The majority of electric vehicles (EVs) are charged domestically overnight, where the precise timing of power allocation is not important to the user, thus representing a source of flexibility that can be leveraged by charging control algorithms. In this paper, we relax the common assumption, that EVs require full charge every morning, enabling additional flexibility to defer charging of surplus energy to subsequent nights, which can enhance the performance of controlled charging. In particular, we consider a simple domestic smart plug, scheduling power delivery with the objective to minimize CO$_2$ emissions over prediction horizons of multiple sessions -- up to seven days ahead -- utilising model predictive control (MPC). Based on carbon intensity data from the UK National Grid, we demonstrate significant potential for emission reductions with multi-session planning of 40 to 46\% compared to uncontrolled charging and 19 to 26\% compared to single-session planning. Furthermore, we assess, how the driving and charging behaviour of EV users affects the available flexibility and consequentially the potential for emission reductions. Finally, using grid carbon intensity data from 14 different UK regions, we report significant variations in absolute emission reductions based on the local energy mix.

