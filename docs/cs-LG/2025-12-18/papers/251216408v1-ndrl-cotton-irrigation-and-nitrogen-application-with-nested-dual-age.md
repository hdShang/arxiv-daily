---
layout: default
title: "NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning"
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

**提出NDRL方法以解决棉花灌溉与氮肥施用的复杂性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `棉花灌溉` `氮肥施用` `强化学习` `资源优化` `农业管理` `动态调节` `可持续发展`

## 📋 核心要点

1. 现有方法在优化水氮组合时复杂性高，导致产量优化效果不佳，且难以量化轻微压力信号，反馈延迟影响动态调节精度。
2. 本文提出的NDRL方法通过父代理和子代理的协作，优化灌溉和施肥策略，动态调整以提高资源利用效率和作物产量。
3. 实验结果显示，NDRL方法在2023年和2024年均实现了4.7%的产量提升，灌溉水生产率和氮部分生产率也有显著提高。

## 📝 摘要（中文）

有效的灌溉和氮肥施用对作物产量有显著影响。然而，现有研究面临两个主要限制：一是优化水氮组合的复杂性高，导致产量优化效果不佳；二是轻微压力信号的量化和反馈延迟，使得水氮动态调节精度不足，资源利用效率低。为了解决这些问题，本文提出了一种嵌套双代理强化学习（NDRL）方法。NDRL中的父代理基于预期的累计产量收益识别有前景的宏观灌溉和施肥动作，减少无效探索，同时保持目标与产量的一致性。子代理的奖励函数结合了量化的水分压力因子和氮压力因子，并使用混合概率分布动态优化日常策略，从而提高产量和资源效率。实验结果表明，与最佳基线相比，模拟产量在2023年和2024年均提高了4.7%，灌溉水生产率分别提高了5.6%和5.1%，氮部分生产率分别提高了6.3%和1.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决棉花灌溉与氮肥施用中的复杂优化问题，现有方法在水氮组合优化和动态调节精度方面存在不足，导致资源利用效率低下。

**核心思路**：提出嵌套双代理强化学习（NDRL）方法，通过父代理识别宏观策略，子代理动态优化日常策略，从而提高产量和资源利用效率。

**技术框架**：NDRL方法由父代理和子代理组成，父代理负责宏观决策，子代理根据量化的水分和氮压力因子进行微观调整，二者协同工作以实现优化目标。

**关键创新**：NDRL的创新在于通过双代理结构实现了对复杂环境的有效探索与利用，尤其是在动态调节方面，显著提高了资源使用效率。

**关键设计**：奖励函数结合了水分压力因子（WSF）和氮压力因子（NSF），采用混合概率分布进行策略优化，确保了动态调整的灵活性和准确性。

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

实验结果表明，NDRL方法在2023年和2024年均实现了4.7%的产量提升，灌溉水生产率分别提高了5.6%和5.1%，氮部分生产率分别提高了6.3%和1.0%，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括农业资源管理、精准灌溉和施肥技术等。通过优化水氮施用策略，能够有效提升作物产量和资源利用效率，推动可持续农业发展。未来，该方法可扩展至其他作物的管理与优化，具有广泛的实际价值。

## 📄 摘要（原文）

> Effective irrigation and nitrogen fertilization have a significant impact on crop yield. However, existing research faces two limitations: (1) the high complexity of optimizing water-nitrogen combinations during crop growth and poor yield optimization results; and (2) the difficulty in quantifying mild stress signals and the delayed feedback, which results in less precise dynamic regulation of water and nitrogen and lower resource utilization efficiency. To address these issues, we propose a Nested Dual-Agent Reinforcement Learning (NDRL) method. The parent agent in NDRL identifies promising macroscopic irrigation and fertilization actions based on projected cumulative yield benefits, reducing ineffective explorationwhile maintaining alignment between objectives and yield. The child agent's reward function incorporates quantified Water Stress Factor (WSF) and Nitrogen Stress Factor (NSF), and uses a mixed probability distribution to dynamically optimize daily strategies, thereby enhancing both yield and resource efficiency. We used field experiment data from 2023 and 2024 to calibrate and validate the Decision Support System for Agrotechnology Transfer (DSSAT) to simulate real-world conditions and interact with NDRL. Experimental results demonstrate that, compared to the best baseline, the simulated yield increased by 4.7% in both 2023 and 2024, the irrigation water productivity increased by 5.6% and 5.1% respectively, and the nitrogen partial factor productivity increased by 6.3% and 1.0% respectively. Our method advances the development of cotton irrigation and nitrogen fertilization, providing new ideas for addressing the complexity and precision issues in agricultural resource management and for sustainable agricultural development.

