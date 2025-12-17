---
layout: default
title: SparseWorld: A Flexible, Adaptive, and Efficient 4D Occupancy World Model Powered by Sparse and Dynamic Queries
---

# SparseWorld: A Flexible, Adaptive, and Efficient 4D Occupancy World Model Powered by Sparse and Dynamic Queries

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.17482" target="_blank" class="toolbar-btn">arXiv: 2510.17482v3</a>
    <a href="https://arxiv.org/pdf/2510.17482.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17482v3" 
            onclick="toggleFavorite(this, '2510.17482v3', 'SparseWorld: A Flexible, Adaptive, and Efficient 4D Occupancy World Model Powered by Sparse and Dynamic Queries')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Chenxu Dang, Haiyan Liu, Jason Bao, Pei An, Xinyue Tang, PanAn, Jie Ma, Bingchuan Sun, Yan Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-20 (更新: 2025-11-17)

**备注**: Accepted by AAAI2026 Code: https://github.com/MSunDYY/SparseWorld

---

## 💡 一句话要点

**SparseWorld：基于稀疏动态查询的灵活高效4D Occupancy世界模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Occupancy预测` `世界模型` `稀疏查询` `动态环境` `自动驾驶`

## 📋 核心要点

1. 现有Occupancy世界模型依赖静态和固定的嵌入或网格，限制了感知的灵活性，且“原地分类”与现实场景的动态性和连续性不符。
2. SparseWorld通过稀疏和动态查询，实现灵活、自适应和高效的4D Occupancy世界模型，提升了感知范围和动态捕捉能力。
3. 实验结果表明，SparseWorld在感知、预测和规划任务中均取得了SOTA性能，验证了其在灵活性、适应性和效率方面的优势。

## 📝 摘要（中文）

本文提出SparseWorld，一种新颖的4D Occupancy世界模型，它灵活、自适应且高效，由稀疏和动态查询驱动。该模型包含范围自适应感知模块，其中可学习的查询由自车状态调节，并富含时空关联，从而实现扩展范围的感知。为了有效捕捉场景的动态性，设计了状态条件预测模块，该模块用回归引导公式取代了基于分类的预测，从而精确地将动态查询与4D环境的连续性对齐。此外，专门设计了一种时间感知自调度训练策略，以实现平滑高效的训练。大量实验表明，SparseWorld在感知、预测和规划任务中均取得了最先进的性能。全面的可视化和消融研究进一步验证了SparseWorld在灵活性、适应性和效率方面的优势。

## 🔬 方法详解

**问题定义**：现有的Occupancy世界模型通常采用静态和固定的嵌入或网格，这限制了模型对环境变化的适应性。此外，它们通常采用“原地分类”的方法，即直接对网格中的每个单元进行分类，这与真实世界中物体运动的连续性和动态性不符。因此，如何设计一个能够灵活适应环境变化，并能有效捕捉物体动态信息的Occupancy世界模型是一个关键问题。

**核心思路**：SparseWorld的核心思路是利用稀疏和动态的查询来表示环境。与静态网格不同，这些查询可以根据自车状态和环境动态进行调整，从而实现更灵活和高效的感知。通过将预测任务转化为回归问题，模型能够更好地捕捉物体运动的连续性，避免了分类带来的离散化问题。

**技术框架**：SparseWorld的整体框架包含三个主要模块：范围自适应感知模块、状态条件预测模块和时间感知自调度训练策略。范围自适应感知模块负责生成和更新稀疏动态查询，这些查询受到自车状态的调节，并包含时空关联信息。状态条件预测模块利用这些查询来预测未来时刻的Occupancy状态，采用回归方法而非分类。时间感知自调度训练策略则用于优化模型的训练过程，提高训练效率。

**关键创新**：SparseWorld的关键创新在于其稀疏动态查询的设计和回归引导的预测方法。稀疏动态查询能够根据环境变化自适应地调整位置和数量，从而实现更高效的感知。回归引导的预测方法能够更好地捕捉物体运动的连续性，避免了分类带来的离散化问题。此外，时间感知自调度训练策略也提高了模型的训练效率。

**关键设计**：范围自适应感知模块中，可学习的查询通过自车状态进行调制，并使用注意力机制融合时空信息。状态条件预测模块使用回归损失函数来优化预测结果，并引入了状态条件编码器来捕捉环境的动态信息。时间感知自调度训练策略则根据训练进度动态调整学习率和损失权重。

## 📊 实验亮点

SparseWorld在多个任务上取得了SOTA性能。在感知任务中，其精度和召回率均优于现有方法。在预测任务中，其预测误差显著降低。在规划任务中，其规划路径的成功率更高。消融实验表明，稀疏动态查询和回归引导的预测方法对性能提升有显著贡献。

## 🎯 应用场景

SparseWorld具有广泛的应用前景，可应用于自动驾驶、机器人导航、增强现实等领域。在自动驾驶中，它可以提供更准确和鲁棒的环境感知，从而提高驾驶安全性。在机器人导航中，它可以帮助机器人更好地理解周围环境，从而实现更智能的导航。在增强现实中，它可以将虚拟物体与真实环境更好地融合，从而提供更沉浸式的体验。

## 📄 摘要（原文）

> Semantic occupancy has emerged as a powerful representation in world models for its ability to capture rich spatial semantics. However, most existing occupancy world models rely on static and fixed embeddings or grids, which inherently limit the flexibility of perception. Moreover, their ``in-place classification" over grids exhibits a potential misalignment with the dynamic and continuous nature of real scenarios. In this paper, we propose SparseWorld, a novel 4D occupancy world model that is flexible, adaptive, and efficient, powered by sparse and dynamic queries. We propose a Range-Adaptive Perception module, in which learnable queries are modulated by the ego vehicle states and enriched with temporal-spatial associations to enable extended-range perception. To effectively capture the dynamics of the scene, we design a State-Conditioned Forecasting module, which replaces classification-based forecasting with regression-guided formulation, precisely aligning the dynamic queries with the continuity of the 4D environment. In addition, We specifically devise a Temporal-Aware Self-Scheduling training strategy to enable smooth and efficient training. Extensive experiments demonstrate that SparseWorld achieves state-of-the-art performance across perception, forecasting, and planning tasks. Comprehensive visualizations and ablation studies further validate the advantages of SparseWorld in terms of flexibility, adaptability, and efficiency.

