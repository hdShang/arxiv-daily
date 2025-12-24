---
layout: default
title: "RePO: Replay-Enhanced Policy Optimization"
---

# RePO: Replay-Enhanced Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09340" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09340v1</a>
  <a href="https://arxiv.org/pdf/2506.09340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09340v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09340v1', 'RePO: Replay-Enhanced Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siheng Li, Zhanhui Zhou, Wai Lam, Chao Yang, Chaochao Lu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-11

**备注**: Project Page: https://github.com/SihengLi99/RePO

**🔗 代码/项目**: [GITHUB](https://github.com/SihengLi99/RePO)

---

## 💡 一句话要点

**提出Replay-Enhanced Policy Optimization以解决RL数据效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `策略优化` `重放策略` `数据效率` `数学推理` `模型优化`

## 📋 核心要点

1. 现有的群体相对策略优化方法在计算效率和数据利用率上存在显著不足，限制了其在大型语言模型中的应用。
2. 本文提出的RePO方法通过重放策略从重放缓冲区中获取离线样本，优化策略时能够利用更丰富的样本信息。
3. 实验结果显示，RePO在多个基准测试中显著提升了模型性能，同时增加了计算成本和有效优化步骤的数量。

## 📝 摘要（中文）

强化学习（RL）在优化大型语言模型（LLMs）中至关重要。近期的群体相对策略优化（GRPO）方法通过每个提示估计多个在线策略输出的优势，导致计算成本高且数据效率低。为了解决这一问题，本文提出了Replay-Enhanced Policy Optimization（RePO），利用多样化的重放策略从重放缓冲区中检索离线样本，使得每个提示的策略优化能够基于更广泛和多样的样本集进行。实验表明，RePO在五个LLMs的七个数学推理基准上，相较于GRPO，Qwen2.5-Math-1.5B和Qwen3-1.7B的平均性能分别提升了18.4和4.1分。

## 🔬 方法详解

**问题定义**：现有的群体相对策略优化（GRPO）方法在每个提示上需要多个在线输出以估计优势，这导致了高计算成本和低数据效率。

**核心思路**：RePO通过引入多样化的重放策略，从重放缓冲区中提取离线样本，使得策略优化能够基于更广泛的样本集进行，从而提高数据利用效率。

**技术框架**：RePO的整体架构包括重放缓冲区的管理、样本的多样化选择以及策略优化的实施。主要模块包括样本采集、优势估计和策略更新。

**关键创新**：RePO的核心创新在于利用离线样本进行策略优化，这与传统的在线策略优化方法形成了鲜明对比，显著提高了样本的多样性和利用率。

**关键设计**：在实验中，RePO设置了在线和离线样本数量均为8，并通过特定的损失函数和优化算法来提升模型的学习效率。

## 📊 实验亮点

实验结果显示，RePO在Qwen2.5-Math-1.5B和Qwen3-1.7B模型上分别实现了18.4和4.1的性能提升，相较于GRPO，计算成本仅增加了15%，而有效优化步骤增加了48%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和教育技术等。通过提高大型语言模型的优化效率，RePO能够在实际应用中显著提升模型的响应质量和准确性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) is vital for optimizing large language models (LLMs). Recent Group Relative Policy Optimization (GRPO) estimates advantages using multiple on-policy outputs per prompt, leading to high computational costs and low data efficiency. To address this, we introduce Replay-Enhanced Policy Optimization (RePO), which leverages diverse replay strategies to retrieve off-policy samples from a replay buffer, allowing policy optimization based on a broader and more diverse set of samples for each prompt. Experiments on five LLMs across seven mathematical reasoning benchmarks demonstrate that RePO achieves absolute average performance gains of $18.4$ and $4.1$ points for Qwen2.5-Math-1.5B and Qwen3-1.7B, respectively, compared to GRPO. Further analysis indicates that RePO increases computational cost by $15\%$ while raising the number of effective optimization steps by $48\%$ for Qwen3-1.7B, with both on-policy and off-policy sample numbers set to $8$. The repository can be accessed at https://github.com/SihengLi99/RePO.

