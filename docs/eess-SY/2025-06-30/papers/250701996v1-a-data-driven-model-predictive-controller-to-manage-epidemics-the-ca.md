---
layout: default
title: "A Data-Driven Model Predictive Controller to manage epidemics: The case of SARS-CoV-2 in Mauritius"
---

# A Data-Driven Model Predictive Controller to manage epidemics: The case of SARS-CoV-2 in Mauritius

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.01996" class="toolbar-btn" target="_blank">📄 arXiv: 2507.01996v1</a>
  <a href="https://arxiv.org/pdf/2507.01996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.01996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.01996v1', 'A Data-Driven Model Predictive Controller to manage epidemics: The case of SARS-CoV-2 in Mauritius')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: S. Z. Sayed Hassen, A. Aboudonia, J. Lygeros

**分类**: q-bio.PE, eess.SY

**发布日期**: 2025-06-30

**备注**: 6 pages, 6 figures, European Control Conference 2025

---

## 💡 一句话要点

**提出数据驱动的模型预测控制以管理疫情**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `疫情管理` `模型预测控制` `数据驱动` `社交隔离` `公共卫生` `SIHRD模型` `毛里求斯` `SARS-CoV-2`

## 📋 核心要点

1. 现有疫情管理方法往往缺乏系统性，导致社交隔离政策的实施效果不佳。
2. 论文提出了一种基于数据驱动的模型预测控制方案，利用SIHRD模型优化隔离策略。
3. 模拟结果表明，通过短期提高隔离级别，住院人数和死亡人数显著减少，且社会经济影响微小。

## 📝 摘要（中文）

本研究探讨了在疫情期间实施系统性社交隔离政策的益处。我们基于从可用数据中识别的SIHRD模型，开发了一种混合整数数据驱动的模型预测控制（MPC）方案。以毛里求斯在2021年12月至2022年5月期间的SARS-CoV-2病毒传播为参考，设计的隔离方案控制决策变量取有限值，控制输入在最小时间后才能切换隔离级别。模拟结果验证了我们的设计，显示住院需求保持在医疗中心的承载能力内，通过短时间提高隔离级别，显著减少死亡人数，且对社会和经济影响微乎其微。此外，引入额外的隔离级别使得疫情控制更加平滑，显著减轻住院负担。

## 🔬 方法详解

**问题定义**：本论文旨在解决疫情期间社交隔离政策实施的有效性问题。现有方法往往缺乏系统性，导致疫情控制效果不理想，医疗资源承载压力增大。

**核心思路**：论文的核心思路是通过构建混合整数数据驱动的模型预测控制（MPC）方案，基于SIHRD模型优化隔离策略，确保在控制疫情的同时，降低对社会经济的影响。

**技术框架**：整体架构包括数据收集、模型识别、控制策略设计和模拟验证四个主要模块。首先收集疫情相关数据，然后识别SIHRD模型，接着设计控制策略，最后通过模拟验证效果。

**关键创新**：最重要的技术创新在于将混合整数MPC与SIHRD模型结合，允许控制决策在有限的隔离级别之间切换，从而实现更灵活的疫情管理。与现有方法相比，该方法在隔离级别的设计上更加系统和科学。

**关键设计**：关键参数设置包括隔离级别的取值范围和切换时间间隔，损失函数设计为综合考虑住院人数和死亡人数的加权和，确保控制策略的有效性和可行性。

## 📊 实验亮点

实验结果显示，通过短期提高隔离级别，住院人数保持在医疗中心的承载能力内，死亡人数显著减少，且对社会经济的影响微乎其微。引入额外的隔离级别使得疫情控制更加平滑，住院负担显著降低。

## 🎯 应用场景

该研究的潜在应用领域包括公共卫生政策制定、疫情应对策略优化和智能城市管理等。通过提供科学的隔离策略，可以有效降低疫情对社会的影响，提高公共卫生系统的响应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This work investigates the benefits of implementing a systematic approach to social isolation policies during epidemics. We develop a mixed integer data-driven model predictive control (MPC) scheme based on an SIHRD model which is identified from available data. The case of the spread of the SARS-CoV-2 virus (also known as COVID-19) in Mauritius is used as a reference point with data obtained during the period December 2021 to May 2022. The isolation scheme is designed with the control decision variable taking a finite set of values corresponding to the desired level of isolation. The control input is further restricted to shifting between levels only after a minimum amount of time. The simulation results validate our design, showing that the need for hospitalisation remains within the capacity of the health centres, with the number of deaths considerably reduced by raising the level of isolation for short periods of time with negligible social and economic impact. We also show that the introduction of additional isolation levels results in a smoother containment approach with a considerably reduced hospitalisation burden.

