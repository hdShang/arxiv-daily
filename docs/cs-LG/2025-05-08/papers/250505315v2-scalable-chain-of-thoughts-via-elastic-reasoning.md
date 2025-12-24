---
layout: default
title: Scalable Chain of Thoughts via Elastic Reasoning
---

# Scalable Chain of Thoughts via Elastic Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05315" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05315v2</a>
  <a href="https://arxiv.org/pdf/2505.05315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05315v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05315v2', 'Scalable Chain of Thoughts via Elastic Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhui Xu, Hanze Dong, Lei Wang, Doyen Sahoo, Junnan Li, Caiming Xiong

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-08 (更新: 2025-05-21)

**🔗 代码/项目**: [GITHUB](https://github.com/SalesforceAIResearch/Elastic-Reasoning)

---

## 💡 一句话要点

**提出弹性推理框架以解决大规模推理模型的输出长度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模推理模型` `弹性推理` `思维链` `预算约束` `自适应推理` `模型训练` `推理可靠性`

## 📋 核心要点

1. 现有的大规模推理模型在输出长度上缺乏控制，导致在实际应用中面临资源限制的挑战。
2. 本文提出的弹性推理框架将推理过程分为思考和解决两个阶段，允许独立的预算分配，从而提高推理的可靠性。
3. 实验证明，弹性推理在严格的预算限制下表现稳健，且训练成本显著低于传统方法，同时在无约束条件下也能产生更简洁的推理结果。

## 📝 摘要（中文）

大规模推理模型（LRMs）在复杂任务上取得了显著进展，通过生成扩展的思维链（CoT）来实现。然而，输出长度的不受控性在实际应用中带来了重大挑战，尤其是在推理时间、延迟或计算资源受限的情况下。本文提出了一种名为弹性推理的框架，明确将推理过程分为思考和解决两个阶段，并为其分配独立的预算。在测试阶段，弹性推理优先考虑解决方案的完整性，在严格的资源限制下显著提高了可靠性。我们还引入了一种轻量级的预算约束回滚策略，帮助模型在思考过程被截断时自适应推理，并能有效地推广到未见的预算约束。实验证明，弹性推理在数学和编程基准测试中表现出色，同时训练成本显著低于基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模推理模型在实际应用中输出长度不受控的问题，导致推理时间和计算资源的浪费。现有方法在资源限制下的可靠性不足，影响了其实际应用。

**核心思路**：弹性推理框架通过将推理过程分为思考和解决两个阶段，允许为每个阶段独立分配预算，从而提高推理的灵活性和可靠性。该设计使得模型能够在资源受限的情况下优先考虑解决方案的完整性。

**技术框架**：整体架构包括两个主要模块：思考阶段和解决阶段。思考阶段负责生成推理链，而解决阶段则专注于生成最终答案。通过预算约束回滚策略，模型能够在思考被截断时自适应调整推理过程。

**关键创新**：最重要的技术创新在于引入了预算约束回滚策略，使得模型能够在思考过程被截断时仍能有效推理。这一方法与现有的推理模型相比，显著提高了在资源限制下的推理可靠性。

**关键设计**：在模型训练中，采用了轻量级的预算约束回滚策略，结合GRPO（Gradient Rollout Policy Optimization）进行训练。该策略使得模型能够在不同的预算约束下进行自适应推理，而无需额外的训练数据。

## 📊 实验亮点

实验结果显示，弹性推理在数学（AIME, MATH500）和编程（LiveCodeBench, Codeforces）基准测试中表现出色，能够在严格的预算限制下保持稳健性。同时，其训练成本显著低于基线方法，且在无约束条件下也能生成更简洁高效的推理结果。

## 🎯 应用场景

弹性推理框架的潜在应用领域包括教育、编程辅助和复杂决策支持等场景。在这些领域中，推理模型需要在有限的时间和资源内提供可靠的答案。该研究的实际价值在于提高了推理模型在资源受限环境下的表现，未来可能推动智能助手和自动化系统的广泛应用。

## 📄 摘要（原文）

> Large reasoning models (LRMs) have achieved remarkable progress on complex tasks by generating extended chains of thought (CoT). However, their uncontrolled output lengths pose significant challenges for real-world deployment, where inference-time budgets on tokens, latency, or compute are strictly constrained. We propose Elastic Reasoning, a novel framework for scalable chain of thoughts that explicitly separates reasoning into two phases--thinking and solution--with independently allocated budgets. At test time, Elastic Reasoning prioritizes the completeness of solution segments, significantly improving reliability under tight resource constraints. To train models that are robust to truncated thinking, we introduce a lightweight budget-constrained rollout strategy, integrated into GRPO, which teaches the model to reason adaptively when the thinking process is cut short and generalizes effectively to unseen budget constraints without additional training. Empirical results on mathematical (AIME, MATH500) and programming (LiveCodeBench, Codeforces) benchmarks demonstrate that Elastic Reasoning performs robustly under strict budget constraints, while incurring significantly lower training cost than baseline methods. Remarkably, our approach also produces more concise and efficient reasoning even in unconstrained settings. Our code has been made available at https://github.com/SalesforceAIResearch/Elastic-Reasoning.

