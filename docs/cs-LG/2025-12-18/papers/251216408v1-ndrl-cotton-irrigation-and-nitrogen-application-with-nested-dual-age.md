---
layout: default
title: NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning
---

# NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16408" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16408v1</a>
  <a href="https://arxiv.org/pdf/2512.16408.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16408v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16408v1', 'NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruifeng Xu, Liang He

**分类**: cs.LG, cs.MA

**发布日期**: 2025-12-18

**备注**: Accepted by ICONIP 2025

---

## 💡 一句话要点

**提出嵌套双智能体强化学习NDRL，优化棉花灌溉施氮策略，提升产量和资源利用率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `农业灌溉` `氮肥施用` `双智能体` `作物模型` `精准农业`

## 📋 核心要点

1. 现有方法难以有效优化作物生长期间复杂的水氮组合，导致产量提升有限。
2. NDRL通过嵌套双智能体结构，父智能体宏观决策，子智能体精细调控，提升优化效率。
3. 实验表明，NDRL相较于基线方法，显著提升了棉花产量、灌溉用水生产率和氮素偏生产率。

## 📝 摘要（中文）

本文提出了一种嵌套双智能体强化学习（NDRL）方法，旨在解决作物生长过程中水氮组合优化的高复杂性和产量优化效果不佳的问题，以及量化轻微胁迫信号的困难和反馈延迟的问题，从而提高水氮调控的精确性和资源利用效率。NDRL中的父智能体基于预测的累积产量效益识别有希望的宏观灌溉和施肥行动，减少无效探索，同时保持目标与产量的一致性。子智能体的奖励函数结合了量化的水分胁迫因子（WSF）和氮素胁迫因子（NSF），并使用混合概率分布动态优化每日策略，从而提高产量和资源效率。使用2023年和2024年的田间试验数据校准和验证了农业技术转移决策支持系统（DSSAT），以模拟真实世界条件并与NDRL交互。实验结果表明，与最佳基线相比，模拟产量在2023年和2024年均提高了4.7%，灌溉用水生产率分别提高了5.6%和5.1%，氮素偏生产率分别提高了6.3%和1.0%。该方法推动了棉花灌溉和施氮技术的发展，为解决农业资源管理中的复杂性和精确性问题以及可持续农业发展提供了新思路。

## 🔬 方法详解

**问题定义**：论文旨在解决棉花种植过程中，如何精确控制灌溉和施氮量，以最大化产量并提高资源利用率的问题。现有方法的痛点在于难以量化作物对水氮的轻微胁迫信号，导致反馈延迟，无法进行精准的动态调节；同时，水氮组合优化的复杂性高，传统方法难以找到最优策略。

**核心思路**：论文的核心思路是利用嵌套双智能体强化学习框架，将宏观决策和微观调控相结合。父智能体负责根据预测的累积产量效益，选择有希望的宏观灌溉和施肥策略，减少无效探索。子智能体则根据量化的水分胁迫因子（WSF）和氮素胁迫因子（NSF），动态优化每日策略，从而提高产量和资源效率。

**技术框架**：NDRL的整体架构包含两个智能体：父智能体和子智能体。父智能体基于DSSAT模拟的作物生长状态，预测不同水氮组合的累积产量效益，并选择宏观策略。子智能体则根据每日的WSF和NSF，以及父智能体的宏观策略，利用混合概率分布动态调整灌溉和施氮量。DSSAT作为环境模拟器，提供作物生长状态的反馈，用于训练和评估NDRL。

**关键创新**：NDRL的关键创新在于嵌套双智能体结构和量化的胁迫因子。嵌套结构实现了宏观策略和微观调控的有效结合，提高了优化效率。WSF和NSF的引入，使得智能体能够感知作物对水氮的轻微胁迫，从而进行更精准的动态调节。与现有方法相比，NDRL能够更好地应对水氮组合优化的复杂性和反馈延迟问题。

**关键设计**：子智能体的奖励函数设计是关键，它结合了产量和资源利用率的指标，并引入了WSF和NSF作为惩罚项，以鼓励智能体在保证产量的同时，节约水氮资源。子智能体使用混合概率分布来选择每日策略，允许智能体在探索和利用之间进行平衡。父智能体使用深度Q网络（DQN）进行训练，子智能体使用策略梯度方法进行训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16408v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16408v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16408v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，NDRL在模拟环境下，相较于最佳基线方法，在2023年和2024年均实现了4.7%的产量提升。同时，灌溉用水生产率分别提高了5.6%和5.1%，氮素偏生产率分别提高了6.3%和1.0%。这些数据表明，NDRL能够有效提高产量和资源利用率，具有显著的优势。

## 🎯 应用场景

该研究成果可应用于精准农业领域，为棉花等作物的灌溉和施氮管理提供决策支持。通过NDRL，可以实现水肥资源的优化配置，提高作物产量和资源利用率，降低农业生产成本，减少环境污染，促进农业可持续发展。该方法具有推广价值，可应用于其他作物和地区，为解决全球粮食安全问题提供技术支持。

## 📄 摘要（原文）

> Effective irrigation and nitrogen fertilization have a significant impact on crop yield. However, existing research faces two limitations: (1) the high complexity of optimizing water-nitrogen combinations during crop growth and poor yield optimization results; and (2) the difficulty in quantifying mild stress signals and the delayed feedback, which results in less precise dynamic regulation of water and nitrogen and lower resource utilization efficiency. To address these issues, we propose a Nested Dual-Agent Reinforcement Learning (NDRL) method. The parent agent in NDRL identifies promising macroscopic irrigation and fertilization actions based on projected cumulative yield benefits, reducing ineffective explorationwhile maintaining alignment between objectives and yield. The child agent's reward function incorporates quantified Water Stress Factor (WSF) and Nitrogen Stress Factor (NSF), and uses a mixed probability distribution to dynamically optimize daily strategies, thereby enhancing both yield and resource efficiency. We used field experiment data from 2023 and 2024 to calibrate and validate the Decision Support System for Agrotechnology Transfer (DSSAT) to simulate real-world conditions and interact with NDRL. Experimental results demonstrate that, compared to the best baseline, the simulated yield increased by 4.7% in both 2023 and 2024, the irrigation water productivity increased by 5.6% and 5.1% respectively, and the nitrogen partial factor productivity increased by 6.3% and 1.0% respectively. Our method advances the development of cotton irrigation and nitrogen fertilization, providing new ideas for addressing the complexity and precision issues in agricultural resource management and for sustainable agricultural development.

