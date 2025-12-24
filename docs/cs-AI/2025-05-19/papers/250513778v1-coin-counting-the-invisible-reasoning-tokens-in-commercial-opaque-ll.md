---
layout: default
title: "CoIn: Counting the Invisible Reasoning Tokens in Commercial Opaque LLM APIs"
---

# CoIn: Counting the Invisible Reasoning Tokens in Commercial Opaque LLM APIs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13778" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13778v1</a>
  <a href="https://arxiv.org/pdf/2505.13778.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13778v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13778v1', 'CoIn: Counting the Invisible Reasoning Tokens in Commercial Opaque LLM APIs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guoheng Sun, Ziyao Wang, Bowei Tian, Meng Liu, Zheyu Shen, Shwai He, Yexiao He, Wanghao Ye, Yiting Wang, Ang Li

**分类**: cs.AI

**发布日期**: 2025-05-19

**🔗 代码/项目**: [GITHUB](https://github.com/CASE-Lab-UMD/LLM-Auditing-CoIn)

---

## 💡 一句话要点

**提出CoIn框架以解决商业LLM API中的隐性推理令牌计数问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `计费透明度` `审计框架` `哈希树` `嵌入匹配` `商业API` `用户权益`

## 📋 核心要点

1. 现有商业LLM API在返回最终答案时隐藏推理过程，导致用户无法验证令牌的真实使用情况。
2. CoIn框架通过构建可验证的哈希树和嵌入基础的相关性匹配，审计隐藏令牌的数量和语义有效性。
3. 实验结果显示，CoIn在检测令牌计数膨胀方面的成功率高达94.7%，显著提升了计费透明度。

## 📝 摘要（中文）

随着后训练技术的发展，大型语言模型（LLMs）逐渐增强了结构化的多步骤推理能力，通常通过强化学习进行优化。这些增强推理的模型在复杂任务上优于标准LLMs，并支撑着许多商业LLM API。然而，为了保护专有行为并减少冗长，提供商通常在返回最终答案时隐藏推理痕迹。这种不透明性导致了关键的透明度缺口：用户为不可见的推理令牌付费，而这些令牌往往占据了费用的大部分，用户却无法验证其真实性。为了解决这一问题，本文提出了CoIn，一个验证框架，用于审计隐藏令牌的数量和语义有效性。实验表明，作为可信的第三方审计者，CoIn能够有效检测令牌计数膨胀，成功率高达94.7%，显示出在不透明的LLM服务中恢复计费透明度的强大能力。

## 🔬 方法详解

**问题定义**：本文旨在解决商业LLM API中隐性推理令牌计数的透明度问题。现有方法无法验证用户为不可见令牌支付的费用的真实性，可能导致令牌计数膨胀和不当收费。

**核心思路**：CoIn框架的核心思路是通过构建可验证的哈希树和嵌入基础的相关性匹配，来审计和验证隐藏令牌的数量和语义有效性，从而提高计费的透明度。

**技术框架**：CoIn的整体架构包括两个主要模块：首先，利用令牌嵌入指纹构建哈希树以检查令牌计数；其次，通过嵌入基础的相关性匹配来检测伪造的推理内容。

**关键创新**：CoIn的主要创新在于其能够有效审计隐藏令牌的数量和语义，填补了现有方法在透明度和验证能力上的空白。与传统方法相比，CoIn提供了一种新的验证机制，确保用户能够信任其支付的费用。

**关键设计**：在设计中，CoIn采用了高效的哈希算法以构建哈希树，并使用深度学习模型进行嵌入匹配，确保了高效性和准确性。具体的参数设置和损失函数设计在实验中经过优化，以提高检测的成功率。

## 📊 实验亮点

实验结果表明，CoIn在检测令牌计数膨胀方面的成功率高达94.7%，显著优于现有的审计方法。这一成果展示了CoIn在恢复商业LLM服务计费透明度方面的强大能力，为用户提供了可信的费用验证手段。

## 🎯 应用场景

CoIn框架的潜在应用领域包括商业LLM API的计费透明度审计、云计算服务的费用监控以及任何需要验证隐性数据处理的场景。其实际价值在于保护用户权益，防止不当收费，并促进LLM服务的公平性与透明度。未来，CoIn可能推动行业标准的建立，促进更广泛的技术应用。

## 📄 摘要（原文）

> As post-training techniques evolve, large language models (LLMs) are increasingly augmented with structured multi-step reasoning abilities, often optimized through reinforcement learning. These reasoning-enhanced models outperform standard LLMs on complex tasks and now underpin many commercial LLM APIs. However, to protect proprietary behavior and reduce verbosity, providers typically conceal the reasoning traces while returning only the final answer. This opacity introduces a critical transparency gap: users are billed for invisible reasoning tokens, which often account for the majority of the cost, yet have no means to verify their authenticity. This opens the door to token count inflation, where providers may overreport token usage or inject synthetic, low-effort tokens to inflate charges. To address this issue, we propose CoIn, a verification framework that audits both the quantity and semantic validity of hidden tokens. CoIn constructs a verifiable hash tree from token embedding fingerprints to check token counts, and uses embedding-based relevance matching to detect fabricated reasoning content. Experiments demonstrate that CoIn, when deployed as a trusted third-party auditor, can effectively detect token count inflation with a success rate reaching up to 94.7%, showing the strong ability to restore billing transparency in opaque LLM services. The dataset and code are available at https://github.com/CASE-Lab-UMD/LLM-Auditing-CoIn.

