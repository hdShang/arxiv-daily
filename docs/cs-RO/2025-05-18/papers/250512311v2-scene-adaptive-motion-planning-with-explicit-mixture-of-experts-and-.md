---
layout: default
title: Scene-Adaptive Motion Planning with Explicit Mixture of Experts and Interaction-Oriented Optimization
---

# Scene-Adaptive Motion Planning with Explicit Mixture of Experts and Interaction-Oriented Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12311" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12311v2</a>
  <a href="https://arxiv.org/pdf/2505.12311.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12311v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12311v2', 'Scene-Adaptive Motion Planning with Explicit Mixture of Experts and Interaction-Oriented Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongbiao Zhu, Liulong Ma, Xian Wu, Xin Deng, Xiaoyao Liang

**分类**: cs.RO

**发布日期**: 2025-05-18 (更新: 2025-05-30)

**备注**: Main text 10 pages with 7 figures

---

## 💡 一句话要点

**提出EMoE-Planner以解决复杂城市环境中的轨迹规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自主驾驶` `轨迹规划` `专家混合模型` `多模态学习` `环境交互` `智能交通` `机器人导航`

## 📋 核心要点

1. 核心问题：现有的轨迹规划方法难以处理复杂城市环境中的多模态轨迹，且单一专家模型无法有效应对多样化场景。
2. 方法要点：EMoE-Planner通过动态选择专家、提供多模态先验和考虑环境交互来提升轨迹规划的性能。
3. 实验或效果：在Nuplan数据集上的对比实验显示，该模型在几乎所有测试场景中均超越了现有最先进的模型。

## 📝 摘要（中文）

尽管经过十多年的发展，复杂城市环境中的自主驾驶轨迹规划仍面临重大挑战。这些挑战包括难以适应轨迹的多模态特性、单一专家模型在管理多样场景时的局限性，以及对环境交互考虑不足。为了解决这些问题，本文提出了EMoE-Planner，结合了三种创新方法。首先，显式的专家混合模型（MoE）通过共享场景路由器动态选择基于场景特定信息的专家。其次，规划器利用场景特定查询提供多模态先验，指导模型关注相关目标区域。最后，通过考虑自车与其他代理之间的交互，增强了预测模型和损失计算，从而显著提升了规划性能。实验结果表明，该模型在几乎所有测试场景中均优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂城市环境中自主驾驶轨迹规划的多模态特性和环境交互不足的问题。现有方法通常依赖单一专家模型，难以适应多样化的场景和复杂的环境交互。

**核心思路**：EMoE-Planner的核心思路是通过显式的专家混合模型（MoE）动态选择适合特定场景的专家，同时利用场景特定的查询来提供多模态先验，从而提升轨迹规划的准确性和灵活性。

**技术框架**：该方法的整体架构包括三个主要模块：显式MoE模块用于专家选择，场景特定查询模块用于生成多模态先验，以及交互增强模块用于考虑自车与其他代理的交互。

**关键创新**：最重要的技术创新在于显式MoE的动态专家选择机制和对环境交互的深入考虑，这与传统的静态专家模型形成了鲜明对比，显著提升了规划性能。

**关键设计**：在模型设计中，采用了共享场景路由器来实现专家选择，损失函数中引入了交互项以增强模型对环境的适应性，网络结构则通过多模态输入来提高预测的准确性。

## 📊 实验亮点

实验结果表明，EMoE-Planner在Nuplan数据集上的表现优于现有的最先进模型，几乎在所有测试场景中均实现了性能提升，首次使纯学习模型在闭环仿真中超越了基于规则的算法，显示出显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、智能交通系统和机器人导航等。通过提升轨迹规划的准确性和灵活性，EMoE-Planner能够在复杂城市环境中实现更安全、更高效的自动驾驶，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Despite over a decade of development, autonomous driving trajectory planning in complex urban environments continues to encounter significant challenges. These challenges include the difficulty in accommodating the multi-modal nature of trajectories, the limitations of single expert model in managing diverse scenarios, and insufficient consideration of environmental interactions. To address these issues, this paper introduces the EMoE-Planner, which incorporates three innovative approaches. Firstly, the Explicit MoE (Mixture of Experts) dynamically selects specialized experts based on scenario-specific information through a shared scene router. Secondly, the planner utilizes scene-specific queries to provide multi-modal priors, directing the model's focus towards relevant target areas. Lastly, it enhances the prediction model and loss calculation by considering the interactions between the ego vehicle and other agents, thereby significantly boosting planning performance. Comparative experiments were conducted on the Nuplan dataset against the state-of-the-art methods. The simulation results demonstrate that our model consistently outperforms SOTA models across nearly all test scenarios. Our model is the first pure learning model to achieve performance surpassing rule-based algorithms in almost all Nuplan closed-loop simulations.

