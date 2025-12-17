---
layout: default
title: VISTA: A Vision and Intent-Aware Social Attention Framework for Multi-Agent Trajectory Prediction
---

# VISTA: A Vision and Intent-Aware Social Attention Framework for Multi-Agent Trajectory Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10203" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10203v1</a>
  <a href="https://arxiv.org/pdf/2511.10203.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10203v1" onclick="toggleFavorite(this, '2511.10203v1', 'VISTA: A Vision and Intent-Aware Social Attention Framework for Multi-Agent Trajectory Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stephane Da Silva Martins, Emanuel Aldea, Sylvie Le Hégarat-Mascle

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-11-13

**备注**: Paper accepted at WACV 2026

---

## 💡 一句话要点

**VISTA：一种用于多智能体轨迹预测的视觉和意图感知社交注意力框架**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `多智能体轨迹预测` `社交注意力` `Transformer` `目标条件预测` `碰撞避免`

## 📋 核心要点

1. 现有方法在多智能体轨迹预测中难以同时捕捉长期目标和精细社交互动，导致预测不准确。
2. VISTA利用递归目标条件Transformer，结合交叉注意力融合、社交token注意力和成对注意力图，实现更准确的预测。
3. 实验表明，VISTA在MADRAS和SDD数据集上显著降低了碰撞率，并提高了预测精度，展现了其优越性。

## 📝 摘要（中文）

多智能体轨迹预测对于在密集、交互环境中运行的自主系统至关重要。现有方法通常无法联合捕捉智能体的长期目标和精细的社交互动，从而导致不切实际的多智能体未来轨迹。我们提出了VISTA，一种用于多智能体轨迹预测的递归目标条件Transformer。VISTA结合了(i)一个交叉注意力融合模块，将长时程意图与过去运动相结合，(ii)一个社交token注意力机制，用于跨智能体的灵活交互建模，以及(iii)成对注意力图，使社交影响模式在推理时可解释。我们的模型将单智能体目标条件预测转化为一个连贯的多智能体预测框架。除了标准位移指标外，我们还评估了轨迹碰撞率作为联合真实性的度量。在高度密集的MADRAS基准测试和SDD上，VISTA实现了最先进的精度，并显著减少了碰撞次数。在MADRAS上，它将强基线的平均碰撞率从2.14%降低到0.03%，在SDD上，它在提高ADE、FDE和minFDE的同时实现了零碰撞。这些结果表明，VISTA生成了符合社交规范、具有目标意识且可解释的轨迹，使其在安全关键型自主系统中具有应用前景。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体轨迹预测问题，现有方法的痛点在于无法有效融合智能体的长期意图和彼此之间的社交互动，导致预测的轨迹不真实，容易发生碰撞。现有方法通常只关注短期的运动模式，忽略了智能体的目标和社交关系，使得预测结果缺乏全局一致性和可解释性。

**核心思路**：论文的核心思路是利用Transformer架构，通过注意力机制显式地建模智能体的意图和社交互动。具体来说，VISTA模型将智能体的历史轨迹、目标和社交关系编码成向量表示，然后利用交叉注意力机制融合这些信息，从而预测未来的轨迹。这种方法能够更好地捕捉智能体之间的依赖关系，并生成更符合社交规范的轨迹。

**技术框架**：VISTA模型主要包含三个模块：(1)交叉注意力融合模块，用于融合长时程意图和过去运动信息；(2)社交token注意力机制，用于建模智能体之间的交互；(3)成对注意力图，用于可视化和解释社交影响模式。整个框架采用递归的方式进行预测，即每一步的预测都依赖于前一步的预测结果，从而实现长时程的轨迹预测。

**关键创新**：VISTA的关键创新在于其社交token注意力机制和成对注意力图。社交token注意力机制能够灵活地建模智能体之间的复杂交互，而无需预先定义固定的社交关系。成对注意力图则能够可视化智能体之间的社交影响模式，从而提高模型的可解释性。此外，VISTA还将单智能体目标条件预测扩展到多智能体场景，使其能够生成更连贯的多智能体轨迹。

**关键设计**：VISTA使用Transformer编码器-解码器结构，其中编码器用于提取智能体的特征表示，解码器用于生成未来的轨迹。交叉注意力融合模块使用多头注意力机制，将长时程意图和过去运动信息进行融合。社交token注意力机制使用可学习的token来表示智能体之间的社交关系。损失函数包括轨迹预测损失和碰撞损失，用于优化模型的预测精度和安全性。

## 📊 实验亮点

VISTA在MADRAS数据集上将平均碰撞率从2.14%降低到0.03%，在SDD数据集上实现了零碰撞，同时提高了ADE、FDE和minFDE等指标。这些结果表明，VISTA在多智能体轨迹预测方面取得了显著的性能提升，能够生成更安全、更真实的轨迹。

## 🎯 应用场景

VISTA在自动驾驶、机器人导航、人群行为分析等领域具有广泛的应用前景。它可以帮助自动驾驶车辆更好地理解周围车辆的意图和行为，从而做出更安全、更合理的决策。在机器人导航中，VISTA可以帮助机器人更好地规划路径，避免与行人或其他机器人发生碰撞。在人群行为分析中，VISTA可以用于预测人群的移动轨迹，从而为公共安全和城市规划提供支持。

## 📄 摘要（原文）

> Multi-agent trajectory prediction is crucial for autonomous systems operating in dense, interactive environments. Existing methods often fail to jointly capture agents' long-term goals and their fine-grained social interactions, which leads to unrealistic multi-agent futures. We propose VISTA, a recursive goal-conditioned transformer for multi-agent trajectory forecasting. VISTA combines (i) a cross-attention fusion module that integrates long-horizon intent with past motion, (ii) a social-token attention mechanism for flexible interaction modeling across agents, and (iii) pairwise attention maps that make social influence patterns interpretable at inference time. Our model turns single-agent goal-conditioned prediction into a coherent multi-agent forecasting framework. Beyond standard displacement metrics, we evaluate trajectory collision rates as a measure of joint realism. On the high-density MADRAS benchmark and on SDD, VISTA achieves state-of-the-art accuracy and substantially fewer collisions. On MADRAS, it reduces the average collision rate of strong baselines from 2.14 to 0.03 percent, and on SDD it attains zero collisions while improving ADE, FDE, and minFDE. These results show that VISTA generates socially compliant, goal-aware, and interpretable trajectories, making it promising for safety-critical autonomous systems.

