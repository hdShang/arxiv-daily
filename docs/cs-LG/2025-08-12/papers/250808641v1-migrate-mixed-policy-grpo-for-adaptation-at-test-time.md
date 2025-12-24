---
layout: default
title: "MiGrATe: Mixed-Policy GRPO for Adaptation at Test-Time"
---

# MiGrATe: Mixed-Policy GRPO for Adaptation at Test-Time

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08641" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08641v1</a>
  <a href="https://arxiv.org/pdf/2508.08641.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08641v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08641v1', 'MiGrATe: Mixed-Policy GRPO for Adaptation at Test-Time')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peter Phan, Dhruv Agarwal, Kavitha Srinivas, Horst Samulowitz, Pavan Kapanipathi, Andrew McCallum

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出MiGrATe以解决黑箱优化任务中的适应性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `黑箱优化` `大型语言模型` `在线测试时训练` `混合策略` `搜索算法` `适应性学习` `无监督学习`

## 📋 核心要点

1. 现有方法在黑箱优化任务中难以平衡探索与利用，导致解的质量不理想。
2. MiGrATe通过在线测试时训练，利用GRPO算法适应LLMs，避免了对手工训练数据的依赖。
3. 在多个复杂领域的实验中，MiGrATe consistently outperform inference-only and TTT baselines，显示出其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在黑箱优化任务中的应用日益广泛，然而现有方法在探索新解空间与利用高回报解之间的平衡上存在困难。本文提出MiGrATe，一种在线测试时训练（TTT）的方法，利用GRPO作为搜索算法，在推理过程中适应LLMs，无需外部训练数据。MiGrATe通过混合策略组构建程序，结合了在策略采样和两种离策略数据选择技术，旨在在保留探索的同时，偏向于对有前景区域的利用。实验结果表明，MiGrATe在多个复杂任务中表现优异，展示了在线TTT在无外部监督下的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在黑箱优化任务中的适应性问题，现有方法在探索新解空间与利用高回报解之间的平衡存在不足，限制了其在不同领域的可行性与扩展性。

**核心思路**：MiGrATe通过在线测试时训练（TTT）方法，利用GRPO作为搜索算法，在推理阶段适应LLMs，避免了对外部训练数据的需求。该方法结合了在策略采样与两种离策略数据选择技术，旨在在保留探索的同时，偏向于对有前景区域的利用。

**技术框架**：MiGrATe的整体架构包括混合策略组构建程序，主要模块包括在策略采样、贪婪采样（选择表现最佳的历史完成）和邻域采样（生成与高回报解结构相似的完成）。这些模块共同作用，优化策略梯度。

**关键创新**：MiGrATe的核心创新在于其混合策略组构建程序，通过结合在策略与离策略的采样方法，显著提高了对有前景区域的利用能力，同时保持了探索的灵活性。这一设计与传统方法的本质区别在于不再依赖手工训练数据。

**关键设计**：在MiGrATe中，关键参数设置包括采样策略的权重分配，损失函数的设计以确保对高回报解的偏向，以及网络结构的选择以支持高效的在线适应。

## 📊 实验亮点

在实验中，MiGrATe在字词搜索、分子优化和假设+程序归纳等三个复杂领域中表现优异， consistently outperforming inference-only and TTT baselines，显示出其在无外部监督下的在线TTT潜力，提升幅度显著。

## 🎯 应用场景

MiGrATe的研究成果在多个领域具有广泛的应用潜力，包括程序合成、分子设计等黑箱优化任务。其在线适应能力使得在没有外部监督的情况下，能够快速适应不同任务需求，提升解决方案的质量与效率。未来，该方法有望推动更多复杂搜索任务的研究与应用。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly being applied to black-box optimization tasks, from program synthesis to molecule design. Prior work typically leverages in-context learning to iteratively guide the model towards better solutions. Such methods, however, often struggle to balance exploration of new solution spaces with exploitation of high-reward ones. Recently, test-time training (TTT) with synthetic data has shown promise in improving solution quality. However, the need for hand-crafted training data tailored to each task limits feasibility and scalability across domains. To address this problem, we introduce MiGrATe-a method for online TTT that uses GRPO as a search algorithm to adapt LLMs at inference without requiring external training data. MiGrATe operates via a mixed-policy group construction procedure that combines on-policy sampling with two off-policy data selection techniques: greedy sampling, which selects top-performing past completions, and neighborhood sampling (NS), which generates completions structurally similar to high-reward ones. Together, these components bias the policy gradient towards exploitation of promising regions in solution space, while preserving exploration through on-policy sampling. We evaluate MiGrATe on three challenging domains-word search, molecule optimization, and hypothesis+program induction on the Abstraction and Reasoning Corpus (ARC)-and find that it consistently outperforms both inference-only and TTT baselines, demonstrating the potential of online TTT as a solution for complex search tasks without external supervision.

