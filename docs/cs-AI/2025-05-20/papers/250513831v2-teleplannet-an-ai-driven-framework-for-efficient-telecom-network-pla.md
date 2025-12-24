---
layout: default
title: TelePlanNet: An AI-Driven Framework for Efficient Telecom Network Planning
---

# TelePlanNet: An AI-Driven Framework for Efficient Telecom Network Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13831" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13831v2</a>
  <a href="https://arxiv.org/pdf/2505.13831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13831v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13831v2', 'TelePlanNet: An AI-Driven Framework for Efficient Telecom Network Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zongyuan Deng, Yujie Cai, Qing Liu, Shiyao Mu, Bin Lyu, Zhen Yang

**分类**: cs.AI

**发布日期**: 2025-05-20 (更新: 2025-05-27)

**备注**: 6 pages, 5 figures, 1 table

---

## 💡 一句话要点

**提出TelePlanNet以解决5G网络基站选址优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `5G网络规划` `基站选址` `多目标优化` `强化学习` `大型语言模型` `自动化规划` `电信运营商`

## 📋 核心要点

1. 基站选址在5G网络规划中面临效率低下和规划一致性不足的挑战，传统方法依赖人工经验，难以适应动态需求。
2. 本文提出TelePlanNet框架，结合大型语言模型和改进的GRPO强化学习，实现基站选址的高效多目标优化。
3. 实验结果显示，TelePlanNet的一致性提升至78%，显著优于传统手动方法，展示了其在电信网络规划中的应用潜力。

## 📝 摘要（中文）

基站选址是5G网络规划中的关键挑战，涉及覆盖、成本、用户满意度等多目标优化。传统手动方法效率低下，且规划与建设一致性不足。现有AI工具在某些方面有所改善，但仍难以满足动态网络条件和多目标需求。为此，本文提出TelePlanNet，一个基于AI的框架，集成三层架构以实现高效规划和大规模自动化。通过利用大型语言模型（LLMs）进行实时用户输入处理和意图对齐，并结合改进的群体相对策略优化（GRPO）强化学习训练规划模型，TelePlanNet能够有效解决多目标优化，评估候选站点并提供实用解决方案。实验结果表明，TelePlanNet的一致性提升至78%，显著优于手动方法，为电信运营商提供了高效、可扩展的网络规划工具。

## 🔬 方法详解

**问题定义**：本文旨在解决5G网络基站选址中的多目标优化问题，现有方法效率低下且难以满足动态网络条件，导致规划与建设的一致性不足。

**核心思路**：提出TelePlanNet框架，通过集成大型语言模型和强化学习技术，实时处理用户输入并优化基站选址过程，以实现高效的多目标优化。

**技术框架**：TelePlanNet采用三层架构，主要包括用户输入处理层、意图对齐层和规划优化层，确保信息流动和决策过程的高效性。

**关键创新**：最重要的创新在于结合了大型语言模型与改进的GRPO强化学习，能够实时响应用户需求并进行动态优化，显著提升了规划的一致性和效率。

**关键设计**：在模型训练中，采用了改进的群体相对策略优化算法，设置了适应性损失函数，以确保多目标优化的有效性和稳定性，同时设计了适合大规模数据处理的网络结构。

## 📊 实验亮点

实验结果表明，TelePlanNet在基站选址一致性方面达到了78%的提升，相较于传统手动方法有显著改善，展示了其在电信网络规划中的有效性和实用性。

## 🎯 应用场景

TelePlanNet框架在电信网络规划中具有广泛的应用潜力，能够为电信运营商提供高效的基站选址解决方案，优化网络覆盖和用户体验。未来，该框架可扩展至其他类型的网络规划和资源配置问题，推动智能城市和物联网的发展。

## 📄 摘要（原文）

> The selection of base station sites is a critical challenge in 5G network planning, which requires efficient optimization of coverage, cost, user satisfaction, and practical constraints. Traditional manual methods, reliant on human expertise, suffer from inefficiencies and are limited to an unsatisfied planning-construction consistency. Existing AI tools, despite improving efficiency in certain aspects, still struggle to meet the dynamic network conditions and multi-objective needs of telecom operators' networks. To address these challenges, we propose TelePlanNet, an AI-driven framework tailored for the selection of base station sites, integrating a three-layer architecture for efficient planning and large-scale automation. By leveraging large language models (LLMs) for real-time user input processing and intent alignment with base station planning, combined with training the planning model using the improved group relative policy optimization (GRPO) reinforcement learning, the proposed TelePlanNet can effectively address multi-objective optimization, evaluates candidate sites, and delivers practical solutions. Experiments results show that the proposed TelePlanNet can improve the consistency to 78%, which is superior to the manual methods, providing telecom operators with an efficient and scalable tool that significantly advances cellular network planning.

