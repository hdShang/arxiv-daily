---
layout: default
title: STEMS: Spatial-Temporal Enhanced Safe Multi-Agent Coordination for Building Energy Management
---

# STEMS: Spatial-Temporal Enhanced Safe Multi-Agent Coordination for Building Energy Management

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14112" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14112</a>
  <a href="https://arxiv.org/pdf/2510.14112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14112" onclick="toggleFavorite(this, '2510.14112', 'STEMS: Spatial-Temporal Enhanced Safe Multi-Agent Coordination for Building Energy Management')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huiliang Zhang, Di Wu, Arnaud Zinflou, Benoit Boulet

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出STEMS框架，利用时空增强安全多智能体协同优化建筑能源管理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `建筑能源管理` `时空图神经网络` `安全约束控制` `图卷积网络` `Transformer模型` `协同优化`

## 📋 核心要点

1. 现有建筑能源管理方法难以充分利用建筑间的时空依赖关系，缺乏严格的安全保障，且系统复杂性高，限制了其在多建筑系统中的应用。
2. STEMS框架通过融合GCN-Transformer架构学习时空图表示，并结合控制屏障函数的多智能体强化学习算法，实现安全约束下的协同能源管理。
3. 实验结果表明，STEMS在成本、排放和安全性方面均优于现有方法，同时保持了良好的舒适度，并在极端天气下表现出鲁棒性。

## 📝 摘要（中文）

建筑能源管理对于实现碳减排目标、提高居住舒适度和降低能源成本至关重要。协同建筑能源管理面临着在多建筑系统中利用时空依赖性并确保运行安全的关键挑战。现有的多建筑能源系统面临三个主要挑战：时空信息利用不足、缺乏严格的安全保障以及系统复杂性。本文提出了一种时空增强安全多智能体协同（STEMS）框架，这是一种用于协同建筑能源管理的新型安全约束多智能体强化学习框架。STEMS集成了两个核心组件：（1）使用GCN-Transformer融合架构的时空图表示学习框架，用于捕获建筑间的关系和时间模式；（2）结合控制屏障函数以提供数学安全保证的安全约束多智能体RL算法。在真实建筑数据集上的大量实验表明，STEMS的性能优于现有方法，成本降低21%，排放降低18%，并将安全违规从35.1%显著降低到5.6%，同时仅以0.13的不舒适比例保持最佳舒适度。该框架还在极端天气条件下表现出强大的鲁棒性，并在不同建筑类型中保持有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决多建筑能源管理中的协同优化问题，现有方法难以充分利用建筑间的时空依赖关系，缺乏对系统安全性的严格保障，并且系统复杂性较高，难以部署和维护。这些痛点导致能源效率低下，安全风险增加，以及运维成本上升。

**核心思路**：论文的核心思路是利用图神经网络（GCN）和Transformer模型来学习建筑间的空间和时间依赖关系，构建一个时空图表示，然后使用安全约束的多智能体强化学习算法，在保证系统安全的前提下，实现多建筑的协同能源管理。这种设计能够更有效地利用信息，提高能源效率，并确保系统运行的安全性。

**技术框架**：STEMS框架包含两个主要模块：1) 时空图表示学习模块，该模块使用GCN-Transformer融合架构，首先使用GCN捕获建筑间的空间关系，然后使用Transformer模型捕获时间序列上的依赖关系，最终生成一个综合的时空图表示。2) 安全约束多智能体强化学习模块，该模块使用多智能体强化学习算法，每个建筑作为一个智能体，通过学习控制策略来优化能源使用。同时，该模块还结合了控制屏障函数（Control Barrier Functions, CBF），以确保系统运行的安全性，避免出现违规行为。

**关键创新**：该论文的关键创新在于将时空图表示学习与安全约束多智能体强化学习相结合，提出了一种新的协同能源管理框架。传统的能源管理方法通常只考虑单个建筑的优化，而忽略了建筑间的相互影响。STEMS框架通过学习建筑间的时空依赖关系，能够更有效地进行协同优化。此外，通过引入控制屏障函数，STEMS框架能够提供数学上的安全保证，避免出现安全违规行为。

**关键设计**：在时空图表示学习模块中，GCN和Transformer的融合方式是一个关键设计。论文可能采用了某种加权融合或者注意力机制来平衡GCN和Transformer的贡献。在安全约束多智能体强化学习模块中，控制屏障函数的选择和参数设置至关重要，需要根据具体的系统特性进行调整。此外，奖励函数的设计也需要仔细考虑，以平衡能源效率、舒适度和安全性之间的关系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.14112/figs/intro.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.14112/figs/single_agent.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.14112/figs/radar_charts_comparison.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，STEMS框架在真实建筑数据集上实现了显著的性能提升。与现有方法相比，STEMS能够降低21%的能源成本，减少18%的碳排放，并将安全违规率从35.1%大幅降低至5.6%，同时保持了良好的舒适度（不舒适比例仅为0.13%）。此外，STEMS在极端天气条件下表现出强大的鲁棒性，并在不同类型的建筑物中保持有效性。

## 🎯 应用场景

STEMS框架可应用于城市级别的多建筑群能源管理，例如商业区、工业园区和住宅社区。通过优化能源分配和使用，降低能源成本和碳排放，提高能源利用效率，并保障系统运行安全。该研究有助于推动智慧城市和可持续能源发展，具有重要的社会和经济价值。

## 📄 摘要（原文）

> Building energy management is essential for achieving carbon reduction goals, improving occupant comfort, and reducing energy costs. Coordinated building energy management faces critical challenges in exploiting spatial-temporal dependencies while ensuring operational safety across multi-building systems. Current multi-building energy systems face three key challenges: insufficient spatial-temporal information exploitation, lack of rigorous safety guarantees, and system complexity. This paper proposes Spatial-Temporal Enhanced Safe Multi-Agent Coordination (STEMS), a novel safety-constrained multi-agent reinforcement learning framework for coordinated building energy management. STEMS integrates two core components: (1) a spatial-temporal graph representation learning framework using a GCN-Transformer fusion architecture to capture inter-building relationships and temporal patterns, and (2) a safety-constrained multi-agent RL algorithm incorporating Control Barrier Functions to provide mathematical safety guarantees. Extensive experiments on real-world building datasets demonstrate STEMS's superior performance over existing methods, showing that STEMS achieves 21% cost reduction, 18% emission reduction, and dramatically reduces safety violations from 35.1% to 5.6% while maintaining optimal comfort with only 0.13 discomfort proportion. The framework also demonstrates strong robustness during extreme weather conditions and maintains effectiveness across different building types.

