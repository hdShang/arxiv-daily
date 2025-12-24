---
layout: default
title: "Reason-to-Recommend: Using Interaction-of-Thought Reasoning to Enhance LLM Recommendation"
---

# Reason-to-Recommend: Using Interaction-of-Thought Reasoning to Enhance LLM Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05069" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05069v2</a>
  <a href="https://arxiv.org/pdf/2506.05069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05069v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05069v2', 'Reason-to-Recommend: Using Interaction-of-Thought Reasoning to Enhance LLM Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keyu Zhao, Fengli Xu, Yong Li

**分类**: cs.IR, cs.AI

**发布日期**: 2025-06-05 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出R2Rec以解决推荐系统中隐式反馈的推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推荐系统` `大型语言模型` `推理机制` `隐式反馈` `强化学习` `个性化推荐` `用户交互`

## 📋 核心要点

1. 现有推荐系统方法在处理隐式用户反馈时缺乏有效的推理机制，导致推荐效果不佳。
2. 本文提出R2Rec框架，通过逐步掩蔽提示策略，将用户-物品交互转化为结构化的思维交互，增强推理能力。
3. 实验结果显示，R2Rec在多个真实数据集上显著提升了推荐性能，尤其在HitRatio@1上表现突出。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的进步，将其整合到推荐任务中因其强大的语义理解和灵活的提示能力而受到关注。现有方法主要通过编码用户-物品交互或元数据来进行推荐。然而，直接将推理方法应用于推荐系统效果不佳，因为用户反馈是隐式的且缺乏推理监督。为此，本文提出了R2Rec，一个增强推理的推荐框架，通过逐步掩蔽提示策略从用户-物品图中采样交互链，将其转换为结构化的思维交互。这使得LLMs能够基于隐式模式模拟逐步决策。实验结果表明，R2Rec在三个真实数据集上超越了经典和基于LLM的基线，HitRatio@1平均提升10.48%，相较于原始LLM提升131.81%。

## 🔬 方法详解

**问题定义**：本文旨在解决推荐系统中隐式用户反馈的推理问题。现有方法未能有效利用用户反馈的隐式性，导致推荐效果不理想。

**核心思路**：R2Rec框架通过采样用户-物品交互链，利用逐步掩蔽提示策略将其转化为结构化的思维交互，从而增强LLMs的推理能力，使其能够模拟逐步决策过程。

**技术框架**：R2Rec的整体架构包括两个主要阶段：第一阶段为监督微调，利用高质量的推理轨迹教授基本推理；第二阶段为强化学习，通过奖励信号优化推理过程，缓解稀疏的显式监督问题。

**关键创新**：R2Rec的主要创新在于将交互链转化为思维交互，允许LLMs进行逐步推理，这与传统方法的直接反馈处理方式有本质区别。

**关键设计**：在设计中，采用了逐步掩蔽提示策略，并结合了强化学习的奖励机制，以提升推理的准确性和有效性。

## 📊 实验亮点

实验结果表明，R2Rec在三个真实数据集上表现优异，HitRatio@1平均提升10.48%，相较于原始LLM提升131.81%。这些结果不仅证明了R2Rec的有效性，也展示了其在推荐系统中的潜在应用价值。

## 🎯 应用场景

该研究的潜在应用场景包括电商推荐、内容推荐和社交媒体推荐等领域。通过增强推荐系统的推理能力，R2Rec可以提供更精准的个性化推荐，提升用户体验，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Driven by advances in Large Language Models (LLMs), integrating them into recommendation tasks has gained interest due to their strong semantic understanding and prompt flexibility. Prior work encoded user-item interactions or metadata into prompts for recommendations. In parallel, LLM reasoning, boosted by test-time scaling and reinforcement learning, has excelled in fields like mathematics and code, where reasoning traces and correctness signals are clear, enabling high performance and interpretability. However, directly applying these reasoning methods to recommendation is ineffective because user feedback is implicit and lacks reasoning supervision. To address this, we propose $\textbf{R2Rec}$, a reasoning-enhanced recommendation framework that samples interaction chains from the user-item graph and converts them into structured interaction-of-thoughts via a progressive masked prompting strategy, with each thought representing stepwise reasoning grounded in interaction context. This allows LLMs to simulate step-by-step decision-making based on implicit patterns. We design a two-stage training pipeline: supervised fine-tuning teaches basic reasoning from high-quality traces, and reinforcement learning refines reasoning via reward signals, alleviating sparse explicit supervision. Experiments on three real-world datasets show R2Rec outperforms classical and LLM-based baselines with an average $\textbf{10.48%}$ improvement in HitRatio@1 and $\textbf{131.81%}$ gain over the original LLM. Furthermore, the explicit reasoning chains enhance interpretability by revealing the decision process. Our code is available at: https://anonymous.4open.science/r/R2Rec-7C5D.

