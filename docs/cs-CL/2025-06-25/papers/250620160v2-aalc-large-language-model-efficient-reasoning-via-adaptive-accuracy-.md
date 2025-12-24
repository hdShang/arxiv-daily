---
layout: default
title: "AALC: Large Language Model Efficient Reasoning via Adaptive Accuracy-Length Control"
---

# AALC: Large Language Model Efficient Reasoning via Adaptive Accuracy-Length Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20160" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20160v2</a>
  <a href="https://arxiv.org/pdf/2506.20160.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20160v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20160v2', 'AALC: Large Language Model Efficient Reasoning via Adaptive Accuracy-Length Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruosen Li, Ziming Luo, Quan Zhang, Ruochen Li, Ben Zhou, Ali Payani, Xinya Du

**分类**: cs.CL

**发布日期**: 2025-06-25 (更新: 2025-08-08)

---

## 💡 一句话要点

**提出AALC以解决大型推理模型效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `强化学习` `动态长度控制` `准确性优化` `推理效率`

## 📋 核心要点

1. 现有大型推理模型在生成冗长思维链时，导致高延迟和成本，且准确性提升有限。
2. AALC通过引入基于准确性的长度奖励，动态调整训练过程中的正确性与简洁性，优化推理效率。
3. 实验结果表明，AALC在保持或提升准确性的同时，响应长度减少超过50%，有效抑制冗余推理模式。

## 📝 摘要（中文）

大型推理模型（LRMs）通过生成冗长的思维链来实现令人印象深刻的推理能力，但这种“过度思考”导致高延迟和成本，而准确性提升却不明显。本文提出AALC，一种轻量级的、基于准确性的长度奖励，集成于强化学习中，动态平衡训练过程中的正确性与简洁性。通过将验证准确性纳入奖励，并采用平滑的动态调度长度惩罚，AALC在目标性能达到之前延迟长度惩罚。通过在标准和分布外数学基准上的广泛实验，我们展示了该方法在保持或提升原始准确性的同时，响应长度减少超过50%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在生成冗长思维链时的效率低下问题，现有方法在准确性提升与响应时间之间存在矛盾。

**核心思路**：AALC通过引入动态长度奖励机制，结合验证准确性，优化模型训练过程中的推理效率，减少冗余推理。

**技术框架**：AALC的整体架构包括奖励机制、长度惩罚调度和强化学习训练模块，动态调整模型的输出长度与准确性。

**关键创新**：AALC的核心创新在于将长度惩罚延迟到目标性能达到后，避免了简单的输出截断，促进了更高效的推理路径。

**关键设计**：在设计中，AALC采用平滑的动态调度长度惩罚，并将验证准确性作为奖励的一部分，确保模型在训练过程中能够平衡准确性与简洁性。

## 📊 实验亮点

实验结果显示，AALC在标准和分布外数学基准上，响应长度减少超过50%，同时保持或提升了原始准确性。这表明AALC在推理效率和准确性之间实现了有效的平衡，具有显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动化推理等。通过提高大型推理模型的效率，AALC能够在实时应用中显著降低响应时间，同时保持高准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large reasoning models (LRMs) achieve impressive reasoning capabilities by generating lengthy chain-of-thoughts, but this "overthinking" incurs high latency and cost without commensurate accuracy gains. In this work, we introduce AALC, a lightweight, accuracy-aware length reward integrated into reinforcement learning that dynamically balances correctness and brevity during training. By incorporating validation accuracy into the reward and employing a smooth, dynamically scheduled length penalty, AALC delays length penalty until target performance is met. Through extensive experiments across standard and out-of-distribution math benchmarks, we show that our approach reduces response length by over 50% while maintaining or even improving the original accuracy. Furthermore, qualitative analysis reveals that our method curbs redundant reasoning patterns such as excessive subgoal setting and verification, leading to structurally refined outputs rather than naive truncation. We also identify that efficiency gains are accompanied by reduced interpretability: models trained with AALC omit some narrative framing and explanatory context. These findings highlight the potential of reward-based strategies to guide LRMs toward more efficient, generalizable reasoning paths.

