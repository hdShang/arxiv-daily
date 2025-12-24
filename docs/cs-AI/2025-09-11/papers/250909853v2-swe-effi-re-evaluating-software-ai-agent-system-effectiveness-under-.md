---
layout: default
title: "SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints"
---

# SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09853" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09853v2</a>
  <a href="https://arxiv.org/pdf/2509.09853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09853v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09853v2', 'SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyu Fan, Kirill Vasilevski, Dayi Lin, Boyuan Chen, Yihao Chen, Zhiqing Zhong, Jie M. Zhang, Pinjia He, Ahmed E. Hassan

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-11 (更新: 2025-09-18)

---

## 💡 一句话要点

**SWE-Effi：在资源约束下重新评估软件AI Agent系统的有效性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `软件工程` `AI Agent` `有效性评估` `资源约束` `大型语言模型`

## 📋 核心要点

1. 现有软件工程AI评估侧重准确率，忽略了资源消耗，无法反映真实场景下的有效性。
2. SWE-Effi通过综合考虑准确率和资源消耗（token、时间）来评估AI系统在软件工程任务中的有效性。
3. 实验表明，AI系统的有效性不仅取决于框架本身，还取决于其与基础模型的集成程度，并揭示了“token雪球”和“昂贵的失败”等问题。

## 📝 摘要（中文）

大型语言模型（LLMs）和代码Agent的进步显示出在软件工程（SWE）任务中辅助解决问题和添加功能方面的巨大潜力。现有的软件工程AI排行榜（例如SWE-bench）仅关注解决方案的准确性，忽略了资源受限世界中有效性的关键因素。为了解决这个差距，我们引入了SWE-Effi，这是一组新的指标，用于根据整体有效性得分重新评估AI系统。我们将有效性定义为结果的准确性（例如，问题解决率）与消耗的资源（例如，token和时间）之间的平衡。在本文中，我们通过使用新的多维指标在SWE-bench基准测试的子集上重新对流行的AI系统进行问题解决排名，从而专门关注软件工程场景。我们发现AI系统的有效性不仅取决于scaffold本身，还取决于它与基础模型的集成程度，这是以资源有效的方式实现强大性能的关键。我们还发现了诸如“token雪球”效应之类的系统性挑战，以及更重要的“昂贵的失败”模式。在这些情况下，Agent消耗过多的资源，同时陷入无法解决的任务中——这个问题不仅限制了实际部署，还增加了RL训练期间失败推广的成本。最后，我们观察到token预算下的有效性与时间预算下的有效性之间存在明显的权衡，这在管理项目预算和实现可扩展的强化学习（快速响应至关重要）中起着至关重要的作用。

## 🔬 方法详解

**问题定义**：现有软件工程AI评估基准（如SWE-bench）主要关注AI Agent解决问题的准确率，而忽略了实际应用中资源消耗的限制。这意味着即使一个Agent能够解决问题，但如果消耗了过多的计算资源（如token数量或运行时间），其在实际部署中的价值也会大打折扣。因此，需要一种更全面的评估方法，能够同时考虑准确率和资源消耗，从而更真实地反映AI Agent的有效性。

**核心思路**：SWE-Effi的核心思路是将AI Agent的有效性定义为准确率和资源消耗之间的平衡。具体来说，它通过引入新的多维指标，将解决问题的成功率与消耗的token数量和运行时间进行综合考虑。这样，一个Agent只有在保证较高准确率的同时，尽可能地减少资源消耗，才能被认为是有效的。这种设计理念更贴近实际应用场景，能够更好地指导AI Agent的开发和优化。

**技术框架**：SWE-Effi的评估框架主要包括以下几个步骤：1）选择或构建软件工程任务数据集（例如SWE-bench的子集）；2）运行待评估的AI Agent解决数据集中的问题；3）记录Agent解决问题的准确率以及消耗的token数量和运行时间；4）使用SWE-Effi定义的多维指标，综合评估Agent的有效性。这些指标可以根据实际需求进行调整和扩展，例如可以引入其他类型的资源消耗指标（如内存占用）或考虑不同任务的难度差异。

**关键创新**：SWE-Effi最重要的技术创新在于其对有效性的重新定义和多维指标的引入。它突破了传统评估方法只关注准确率的局限性，将资源消耗纳入评估体系，从而更全面地反映了AI Agent的实际价值。此外，SWE-Effi还揭示了一些重要的系统性挑战，如“token雪球”效应和“昂贵的失败”模式，这些发现对于指导AI Agent的优化具有重要意义。

**关键设计**：SWE-Effi的关键设计在于其多维指标的构建。这些指标需要能够有效地平衡准确率和资源消耗之间的关系，并能够反映不同类型资源消耗的影响。例如，可以采用加权平均的方式，将准确率、token数量和运行时间进行综合考虑，并根据实际需求调整权重。此外，还可以引入惩罚机制，对“昂贵的失败”情况进行惩罚，从而鼓励Agent更有效地利用资源。

## 📊 实验亮点

研究发现，AI系统的有效性不仅取决于框架本身，还取决于其与基础模型的集成程度。同时，揭示了“token雪球”效应和“昂贵的失败”模式，即Agent在无法解决的任务上消耗过多资源。此外，还观察到token预算和时间预算下的有效性之间存在权衡。

## 🎯 应用场景

SWE-Effi可用于评估和优化软件工程AI Agent，指导Agent设计，降低开发和部署成本。它还可应用于强化学习，通过快速评估Agent的有效性，加速训练过程。该研究有助于推动AI在软件工程领域的实际应用，提高软件开发的效率和质量。

## 📄 摘要（原文）

> The advancement of large language models (LLMs) and code agents has demonstrated significant potential to assist software engineering (SWE) tasks, such as autonomous issue resolution and feature addition. Existing AI for software engineering leaderboards (e.g., SWE-bench) focus solely on solution accuracy, ignoring the crucial factor of effectiveness in a resource-constrained world. This is a universal problem that also exists beyond software engineering tasks: any AI system should be more than correct - it must also be cost-effective. To address this gap, we introduce SWE-Effi, a set of new metrics to re-evaluate AI systems in terms of holistic effectiveness scores. We define effectiveness as the balance between the accuracy of outcome (e.g., issue resolve rate) and the resources consumed (e.g., token and time). In this paper, we specifically focus on the software engineering scenario by re-ranking popular AI systems for issue resolution on a subset of the SWE-bench benchmark using our new multi-dimensional metrics. We found that AI system's effectiveness depends not just on the scaffold itself, but on how well it integrates with the base model, which is key to achieving strong performance in a resource-efficient manner. We also identified systematic challenges such as the "token snowball" effect and, more significantly, a pattern of "expensive failures". In these cases, agents consume excessive resources while stuck on unsolvable tasks - an issue that not only limits practical deployment but also drives up the cost of failed rollouts during RL training. Lastly, we observed a clear trade-off between effectiveness under the token budget and effectiveness under the time budget, which plays a crucial role in managing project budgets and enabling scalable reinforcement learning, where fast responses are essential.

