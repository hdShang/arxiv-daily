---
layout: default
title: "VisualToolAgent (VisTA): A Reinforcement Learning Framework for Visual Tool Selection"
---

# VisualToolAgent (VisTA): A Reinforcement Learning Framework for Visual Tool Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20289" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20289v2</a>
  <a href="https://arxiv.org/pdf/2505.20289.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20289v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20289v2', 'VisualToolAgent (VisTA): A Reinforcement Learning Framework for Visual Tool Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyi Huang, Yuyang Ji, Anirudh Sundara Rajan, Zefan Cai, Wen Xiao, Haohan Wang, Junjie Hu, Yong Jae Lee

**分类**: cs.CV

**发布日期**: 2025-05-26 (更新: 2025-07-19)

---

## 💡 一句话要点

**提出VisTA框架以解决工具选择的动态探索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `工具选择` `视觉推理` `动态探索` `群体相对策略优化` `多样性利用` `自动化`

## 📋 核心要点

1. 现有工具增强推理方法依赖无训练提示或大规模微调，缺乏主动工具探索，且假设工具多样性有限。
2. VisTA框架通过端到端强化学习，迭代优化工具选择策略，以任务结果作为反馈信号，支持动态工具组合。
3. 在多个基准测试中，VisTA相较于无训练基线表现出显著性能提升，尤其在处理分布外示例时效果显著。

## 📝 摘要（中文）

我们介绍了VisTA，一个新的强化学习框架，赋能视觉代理动态探索、选择和组合来自多样化库的工具，基于经验性能进行优化。现有的工具增强推理方法通常依赖于无训练的提示或大规模微调，缺乏主动的工具探索，且通常假设工具多样性有限，而微调方法还需要大量的人类监督。相较之下，VisTA利用端到端的强化学习，迭代优化复杂的、特定查询的工具选择策略，以任务结果作为反馈信号。通过群体相对策略优化（GRPO），我们的框架使代理能够自主发现有效的工具选择路径，而无需显式的推理监督。在ChartQA、Geometry3K和BlindTest基准上的实验表明，VisTA在无训练基线之上实现了显著的性能提升，尤其是在分布外示例上。这些结果突显了VisTA增强泛化能力、适应性利用多样化工具的能力，并为灵活的、经验驱动的视觉推理系统铺平了道路。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有工具选择方法在动态探索和多样性利用方面的不足，现有方法往往依赖于固定的工具集和大量人工监督。

**核心思路**：VisTA通过强化学习实现工具选择的动态优化，利用任务结果反馈不断调整选择策略，从而提升工具的使用效率和效果。

**技术框架**：VisTA的整体架构包括工具库的动态探索、策略优化模块和反馈机制。代理通过不断试验和调整，形成有效的工具选择路径。

**关键创新**：VisTA的主要创新在于引入群体相对策略优化（GRPO），使代理能够在没有显式推理监督的情况下，自主发现有效的工具选择策略。

**关键设计**：在设计中，VisTA采用了特定的损失函数来优化工具选择策略，并通过强化学习算法不断更新代理的策略网络，以适应不同任务的需求。

## 📊 实验亮点

实验结果显示，VisTA在ChartQA、Geometry3K和BlindTest基准上相较于无训练基线实现了显著的性能提升，尤其在处理分布外示例时，性能提升幅度达到XX%（具体数据未知），展示了其在工具选择和视觉推理中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括自动化工具选择、智能助手和机器人操作等。VisTA能够在多变的环境中灵活应对不同任务，提高工具使用的效率和准确性，未来可能在工业、医疗和教育等领域产生深远影响。

## 📄 摘要（原文）

> We introduce VisTA, a new reinforcement learning framework that empowers visual agents to dynamically explore, select, and combine tools from a diverse library based on empirical performance. Existing methods for tool-augmented reasoning either rely on training-free prompting or large-scale fine-tuning; both lack active tool exploration and typically assume limited tool diversity, and fine-tuning methods additionally demand extensive human supervision. In contrast, VisTA leverages end-to-end reinforcement learning to iteratively refine sophisticated, query-specific tool selection strategies, using task outcomes as feedback signals. Through Group Relative Policy Optimization (GRPO), our framework enables an agent to autonomously discover effective tool-selection pathways without requiring explicit reasoning supervision. Experiments on the ChartQA, Geometry3K, and BlindTest benchmarks demonstrate that VisTA achieves substantial performance gains over training-free baselines, especially on out-of-distribution examples. These results highlight VisTA's ability to enhance generalization, adaptively utilize diverse tools, and pave the way for flexible, experience-driven visual reasoning systems.

