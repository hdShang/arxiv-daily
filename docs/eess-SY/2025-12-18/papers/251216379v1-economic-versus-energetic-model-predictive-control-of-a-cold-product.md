---
layout: default
title: Economic versus energetic model predictive control of a cold production plant with thermal energy storage
---

# Economic versus energetic model predictive control of a cold production plant with thermal energy storage

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16379" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16379v1</a>
  <a href="https://arxiv.org/pdf/2512.16379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16379v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16379v1', 'Economic versus energetic model predictive control of a cold production plant with thermal energy storage')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manuel G. Satué, Manuel R. Arahal, Luis F. Acedo, Manuel G. Ortega

**分类**: eess.SY

**发布日期**: 2025-12-18

**备注**: 14 pages

**期刊**: Applied Thermal Engineering 210 (2022) 118309

**DOI**: [10.1016/j.applthermaleng.2022.118309](https://doi.org/10.1016/j.applthermaleng.2022.118309)

---

## 💡 一句话要点

**对比经济与能量型模型预测控制，优化冷库生产能耗与成本**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `能量优化` `经济优化` `冷库控制` `Simscape模型`

## 📋 核心要点

1. 多冷水机组冷却工厂面临机组负荷和分配问题，经济型模型预测控制通过最小化电费来解决此问题。
2. 论文对比了能量优化和经济优化两种目标在冷库控制中的效果，旨在为实际应用提供参考。
3. 实验结果表明，在用电高峰期，经济优化虽然降低了成本，但会导致能耗略微增加，需要权衡。

## 📝 摘要（中文）

本文首次对比了能量优化目标与经济优化目标在冷库生产中的应用。研究对象为采用风冷式冷水机组和冷能存储系统的制冷设备。论文将所建立的模型集成到Simscape中，并使用非凸混合优化方法，分别针对能量和经济目标获得最优控制轨迹。在不同场景和季节下的结果表明，尽管目前经济优化方法更为普遍，但能量优化方法也值得考虑。结果受电力季节和可用电价的影响。特别是在用电高峰期，考虑代表性电价时，使用经济优化方法代替能量优化方法会导致能耗增加约2.15%，但成本降低2.94%。

## 🔬 方法详解

**问题定义**：论文旨在解决多冷水机组冷却工厂中，如何优化冷库的运行，以降低能耗或成本的问题。现有方法主要集中于经济型模型预测控制，即以电费最小化为目标，但忽略了能量消耗本身可能带来的影响。

**核心思路**：论文的核心思路是对比能量优化和经济优化两种不同的目标函数，分析它们在不同场景下的性能差异。通过分别优化能量消耗和经济成本，研究两种策略对冷库运行的影响，从而为实际应用提供决策依据。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 建立冷库系统的Simscape模型，包括冷水机组和冷能存储系统；2) 设计能量优化和经济优化两种模型预测控制器，分别以能量消耗和经济成本为目标函数；3) 使用非凸混合优化方法求解最优控制轨迹；4) 在不同场景和季节下进行仿真实验，对比两种控制器的性能。

**关键创新**：论文的关键创新在于首次对能量优化和经济优化在冷库控制中进行了直接对比。以往的研究主要集中于经济优化，而忽略了能量消耗的影响。通过对比分析，论文揭示了两种优化目标在不同场景下的优缺点，为实际应用提供了更全面的信息。

**关键设计**：论文的关键设计包括：1) 精确的冷库系统Simscape模型，能够准确模拟冷库的运行特性；2) 合理的能量和经济目标函数，能够准确反映能量消耗和经济成本；3) 有效的非凸混合优化方法，能够求解复杂系统的最优控制轨迹。具体参数设置和损失函数细节未在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16379v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16379v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16379v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在用电高峰期，使用经济优化方法代替能量优化方法会导致能耗增加约2.15%，但成本降低2.94%。这表明在电价较高时，经济优化可能更具优势，但在其他情况下，能量优化可能更符合可持续发展的目标。具体的实验设置和对比基线未在摘要中详细说明，属于未知信息。

## 🎯 应用场景

该研究成果可应用于各种需要冷能供应的场景，如大型建筑物、数据中心、工业生产等。通过选择合适的优化目标，可以在降低能耗和降低成本之间进行权衡，从而实现冷库运行的最优化。研究结果有助于提高能源利用效率，降低运行成本，并为可持续发展做出贡献。

## 📄 摘要（原文）

> Economic model predictive control has been proposed as a means for solving the unit loading and unit allocation problem in multi-chiller cooling plants. The adjective economic stems from the use of financial cost due to electricity consumption in a time horizon, such is the loss function minimized at each sampling period. The energetic approach is rarely encountered. This article presents for the first time a comparison between the energetic optimization objective and the economic one. The comparison is made on a cooling plant using air-cooled water chillers and a cold storage system. Models developed have been integrated into Simscape, and non-convex mixed optimization methods used to achieve optimal control trajectories for both energetic and economic goals considered separately. The results over several scenarios, and in different seasons, support the consideration of the energetic approach despite the current prevalence of the economic one. The results are dependent on the electric season and the available tariffs. In particular, for the high electric season and considering a representative tariff, the results show that an increment of about 2.15% in energy consumption takes place when using the economic approach instead of the energetic one. On the other hand, a reduction in cost of 2.94% is achieved.

