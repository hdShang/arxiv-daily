---
layout: default
title: Fractured Chain-of-Thought Reasoning
---

# Fractured Chain-of-Thought Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12992" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12992v3</a>
  <a href="https://arxiv.org/pdf/2505.12992.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12992v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12992v3', 'Fractured Chain-of-Thought Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Baohao Liao, Hanze Dong, Yuhui Xu, Doyen Sahoo, Christof Monz, Junnan Li, Caiming Xiong

**分类**: cs.LG, cs.AI, cs.CL, stat.ML

**发布日期**: 2025-05-19 (更新: 2025-06-18)

**🔗 代码/项目**: [GITHUB](https://github.com/BaohaoLiao/frac-cot)

---

## 💡 一句话要点

**提出Fractured Sampling以提升大语言模型推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理效率` `大语言模型` `Chain-of-Thought` `Fractured Sampling` `自然语言处理` `实时应用`

## 📋 核心要点

1. 现有的Chain-of-Thought方法在推理过程中消耗大量token，限制了其在延迟敏感场景中的应用。
2. 论文提出Fractured Sampling，通过截断推理过程并在多个维度上进行插值，减少token消耗同时保持推理准确性。
3. 在五个不同的推理基准上，Fractured Sampling展示了优越的准确性与成本平衡，显著提升了模型的推理效率。

## 📝 摘要（中文）

推理时的扩展技术显著增强了大型语言模型（LLMs）的推理能力，但现有的Chain-of-Thought（CoT）提示方法在延迟敏感的场景中存在高代价问题。本文首先展示了截断CoT的有效性，随后提出Fractured Sampling策略，通过在推理轨迹数量、每条轨迹的最终解数量和推理深度等维度之间进行插值，显著提高了准确性与成本的平衡。实验表明，Fractured Sampling在多项推理基准上表现优越，提供了更高效的LLM推理方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有Chain-of-Thought方法在推理过程中高token消耗的问题，这限制了其在实际应用中的有效性。

**核心思路**：论文提出Fractured Sampling策略，通过截断推理过程，直接生成最终答案，从而减少token使用，同时保持推理的准确性。

**技术框架**：Fractured Sampling在推理过程中通过三个维度进行插值：推理轨迹数量、每条轨迹的最终解数量和推理深度。整体流程包括生成多个推理轨迹，选择最终解并进行截断。

**关键创新**：Fractured Sampling的核心创新在于其在推理过程中灵活调整各个维度的策略，从而实现更高效的推理过程，与传统的完整CoT方法相比，显著降低了token消耗。

**关键设计**：在Fractured Sampling中，关键参数包括推理轨迹的数量和截断深度，这些参数的选择直接影响最终的推理效果和token的使用效率。

## 📊 实验亮点

实验结果表明，Fractured Sampling在多个推理基准上均优于传统的Chain-of-Thought方法，具体表现为在相同token预算下，Pass@k指标显著提升，达到了更高的准确性与成本效益比。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过提升推理效率，Fractured Sampling能够使得大型语言模型在实时应用中更具竞争力，推动智能系统的广泛应用。

## 📄 摘要（原文）

> Inference-time scaling techniques have significantly bolstered the reasoning capabilities of large language models (LLMs) by harnessing additional computational effort at inference without retraining. Similarly, Chain-of-Thought (CoT) prompting and its extension, Long CoT, improve accuracy by generating rich intermediate reasoning trajectories, but these approaches incur substantial token costs that impede their deployment in latency-sensitive settings. In this work, we first show that truncated CoT, which stops reasoning before completion and directly generates the final answer, often matches full CoT sampling while using dramatically fewer tokens. Building on this insight, we introduce Fractured Sampling, a unified inference-time strategy that interpolates between full CoT and solution-only sampling along three orthogonal axes: (1) the number of reasoning trajectories, (2) the number of final solutions per trajectory, and (3) the depth at which reasoning traces are truncated. Through extensive experiments on five diverse reasoning benchmarks and several model scales, we demonstrate that Fractured Sampling consistently achieves superior accuracy-cost trade-offs, yielding steep log-linear scaling gains in Pass@k versus token budget. Our analysis reveals how to allocate computation across these dimensions to maximize performance, paving the way for more efficient and scalable LLM reasoning. Code is available at https://github.com/BaohaoLiao/frac-cot.

