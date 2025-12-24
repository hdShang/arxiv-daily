---
layout: default
title: "Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought"
---

# Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23365" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23365v2</a>
  <a href="https://arxiv.org/pdf/2509.23365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23365v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23365v2', 'Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanlin Zhu, Shibo Hao, Zhiting Hu, Jiantao Jiao, Stuart Russell, Yuandong Tian

**分类**: cs.LG

**发布日期**: 2025-09-27 (更新: 2025-10-06)

**备注**: 29 pages, 5 figures

---

## 💡 一句话要点

**揭示连续思维链中叠加机制的涌现：通过训练动态分析Transformer的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `连续思维链` `大型语言模型` `推理能力` `叠加机制` `训练动态` `Transformer` `有向图可达性` `索引匹配logit`

## 📋 核心要点

1. 大型语言模型推理能力不足，连续思维链通过隐式并行思考提升推理能力，但其训练动态尚不明确。
2. 本文通过分析简化的Transformer在有向图可达性问题上的训练动态，揭示叠加机制的涌现过程。
3. 理论分析表明，索引匹配logit在训练中会先增加后有界，平衡探索和利用，实验结果验证了理论。

## 📝 摘要（中文）

本文研究了连续思维链（continuous CoT）如何提升大型语言模型（LLMs）的推理能力，该方法通过隐式并行思考实现。前期工作已证明，配备连续CoT的两层Transformer可以通过在连续思维中保持多个推理轨迹的叠加来有效解决有向图可达性问题。然而，叠加机制如何从基于梯度的训练方法中自然学习仍然不清楚。为了填补这一空白，我们从理论上分析了一个简化的两层Transformer在有向图可达性问题上的训练动态，揭示了叠加机制如何在训练过程中涌现，分为两个阶段：（i）自回归扩展连续思维的思维生成阶段，以及（ii）将思维转化为最终答案的预测阶段。我们的分析表明，在使用连续思维进行训练时，索引匹配logit（反映模型局部搜索能力强度的重要指标）将首先增加，然后在温和的假设下保持有界。有界的索引匹配logit有效地平衡了推理过程中的探索和利用：模型将利用局部问题结构来识别合理的搜索轨迹，并在不确定哪个解决方案正确时，为多个此类轨迹分配相当的权重以进行探索，从而产生叠加。我们的实验结果跟踪了logits的增长，进一步验证了我们的理论。

## 🔬 方法详解

**问题定义**：论文旨在理解并解释大型语言模型中，连续思维链（Continuous Chain-of-Thought, Continuous CoT）方法如何通过梯度下降训练，涌现出叠加（Superposition）机制，从而提升模型在复杂推理任务（如有向图可达性问题）上的性能。现有方法缺乏对这种涌现过程的理论解释，无法解释模型如何学习并行维护多个推理路径。

**核心思路**：论文的核心思路是通过分析一个简化的两层Transformer模型在训练过程中的动态变化，特别是关注索引匹配logit（index-matching logit）的变化。索引匹配logit反映了模型局部搜索的能力。论文认为，通过控制索引匹配logit的增长，可以平衡模型在推理过程中的探索（exploration）和利用（exploitation），从而实现多个推理路径的叠加。

**技术框架**：论文将训练过程分为两个阶段：(1) **思维生成阶段**：模型自回归地扩展连续思维，生成一系列中间推理步骤。(2) **预测阶段**：模型将生成的连续思维转化为最终答案。论文主要分析了索引匹配logit在这两个阶段的变化，并推导了其增长的上下界。

**关键创新**：论文的关键创新在于从理论上揭示了连续思维链中叠加机制的涌现过程。通过分析索引匹配logit的动态变化，解释了模型如何在训练过程中学习并行维护多个可能的推理路径，从而提升推理能力。这与传统的单路径推理方法形成对比，后者容易陷入局部最优解。

**关键设计**：论文的关键设计包括：(1) 使用简化的两层Transformer模型，便于理论分析。(2) 关注索引匹配logit，作为衡量模型局部搜索能力的关键指标。(3) 推导索引匹配logit增长的上下界，证明其在训练过程中会先增加后有界。(4) 通过实验验证理论分析的正确性，观察logits的增长情况。

## 📊 实验亮点

实验结果表明，索引匹配logit在训练初期快速增长，随后趋于稳定，验证了理论分析的正确性。通过跟踪logits的增长，观察到模型在不确定正确答案时，会为多个可能的推理路径分配相似的权重，从而实现叠加。这些实验结果为理解连续思维链的训练动态提供了有力支持。

## 🎯 应用场景

该研究成果有助于更好地理解和优化大型语言模型的推理能力，可应用于问答系统、知识图谱推理、规划和决策等领域。通过理解叠加机制的涌现，可以设计更有效的训练方法和模型架构，提升模型在复杂推理任务中的性能，并可能推动通用人工智能的发展。

## 📄 摘要（原文）

> Previous work shows that the chain of continuous thought (continuous CoT) improves the reasoning capability of large language models (LLMs) by enabling implicit parallel thinking, and a subsequent work provided theoretical insight by showing that a two-layer transformer equipped with continuous CoT can efficiently solve directed graph reachability by maintaining a superposition of multiple reasoning traces in the continuous thought. However, it remains unclear how the superposition mechanism is naturally learned from gradient-based training methods. To fill this gap, we theoretically analyze the training dynamics of a simplified two-layer transformer on the directed graph reachability problem to unveil how the superposition mechanism emerges during training in two training stages -- (i) a thought-generation stage that autoregressively expands the continuous thought, and (ii) a prediction stage that converts the thought into the final answer. Our analysis reveals that during training using continuous thought, the index-matching logit, an important quantity which reflects the strength of the model's local search ability, will first increase and then remain bounded under mild assumptions. The bounded index-matching logit effectively balances exploration and exploitation during the reasoning process: the model will exploit local problem structures to identify plausible search traces, and assign comparable weights to multiple such traces to explore when it is uncertain about which solution is correct, which results in superposition. Our experimental results tracking the growth of logits further validate our theory.

