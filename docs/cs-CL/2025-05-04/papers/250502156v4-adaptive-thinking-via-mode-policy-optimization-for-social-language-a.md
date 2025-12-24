---
layout: default
title: Adaptive Thinking via Mode Policy Optimization for Social Language Agents
---

# Adaptive Thinking via Mode Policy Optimization for Social Language Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02156" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02156v4</a>
  <a href="https://arxiv.org/pdf/2505.02156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02156v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02156v4', 'Adaptive Thinking via Mode Policy Optimization for Social Language Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minzheng Wang, Yongbin Li, Haobo Wang, Xinghua Zhang, Nan Xu, Bingli Wu, Fei Huang, Haiyang Yu, Wenji Mao

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-04 (更新: 2025-05-22)

**备注**: Work in Progress. The code and data are available, see https://github.com/MozerWang/AMPO

---

## 💡 一句话要点

**提出自适应模式学习以解决社交语言代理的推理深度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自适应学习` `社交智能` `推理深度` `语言代理` `模式优化` `动态切换` `多粒度思维`

## 📋 核心要点

1. 现有方法缺乏动态调整推理深度的能力，导致社交语言代理在复杂场景中的表现不佳。
2. 本文提出自适应模式学习（AML）框架，通过识别分层思维模式和开发AMPO算法，实现上下文感知的模式切换。
3. 实验结果显示，AML在任务表现上比GPT-4o提高了15.6%，且AMPO在推理链长度上减少了32.8%。

## 📝 摘要（中文）

有效的社交智能模拟要求语言代理能够动态调整推理深度，而这一能力在当前研究中明显缺乏。现有方法要么缺乏这种推理能力，要么在所有场景中强制执行统一的长链推理，导致过多的token使用和不灵活的社交模拟。为此，本文提出了自适应模式学习（AML）框架，旨在提高语言代理在动态社交互动中的自适应思维能力。我们首先基于认知控制理论识别了从直观反应到深度思考的分层思维模式，然后开发了自适应模式策略优化（AMPO）算法，以优化上下文感知的模式切换和推理。实验结果表明，AML在社交智能基准测试中比GPT-4o的任务表现提高了15.6%。

## 🔬 方法详解

**问题定义**：本文旨在解决社交语言代理在动态社交互动中缺乏灵活推理深度的问题。现有方法往往采用固定的推理深度，导致资源浪费和适应性不足。

**核心思路**：提出自适应模式学习（AML）框架，通过识别不同的思维模式并优化模式切换，使语言代理能够根据社交情境动态调整推理深度。

**技术框架**：AML框架包括两个主要模块：首先是分层思维模式的设计，涵盖从直观反应到深度思考的多种模式；其次是自适应模式策略优化（AMPO）算法，用于实现上下文感知的模式切换和推理优化。

**关键创新**：AML的核心创新在于多粒度思维模式设计和上下文感知的模式切换机制，显著区别于现有方法的固定深度推理，提升了推理的灵活性和效率。

**关键设计**：在AMPO算法中，采用了动态损失函数来平衡不同推理深度的权重，同时设计了适应性参数以优化模式切换的时机和频率。

## 📊 实验亮点

实验结果表明，AML在社交智能基准测试中比GPT-4o的任务表现提高了15.6%。此外，AMPO算法在推理链长度上减少了32.8%，相较于GRPO提升了7.0%，显示出自适应思维模式选择的优势。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、智能客服和虚拟助手等，能够提升这些系统在复杂社交场景中的交互能力和用户体验。未来，随着自适应推理能力的增强，语言代理将能够更好地理解和响应人类的情感和意图。

## 📄 摘要（原文）

> Effective social intelligence simulation requires language agents to dynamically adjust reasoning depth, a capability notably absent in current studies. Existing methods either lack this kind of reasoning capability or enforce Long Chain-of-Thought reasoning uniformly across all scenarios, resulting in excessive token usage and inflexible social simulation. To address this, we propose an $\textbf{A}$daptive $\textbf{M}$ode $\textbf{L}$earning ($\textbf{AML}$) framework in this paper, aiming to improve the adaptive thinking ability of language agents in dynamic social interactions. To this end, we first identify hierarchical thinking modes ranging from intuitive response to deep deliberation based on the cognitive control theory. We then develop the $\textbf{A}$daptive $\textbf{M}$ode $\textbf{P}$olicy $\textbf{O}$ptimization ($\textbf{AMPO}$) algorithm to optimize the context-aware mode switching and reasoning. Our framework advances existing research in three key aspects: (1) Multi-granular thinking mode design, (2) Context-aware mode switching across social interaction, and (3) Token-efficient reasoning via depth-adaptive processing. Extensive experiments on social intelligence benchmarks verify that AML achieves 15.6% higher task performance than GPT-4o. Notably, our AMPO outperforms GRPO by 7.0% with 32.8% shorter reasoning chains, demonstrating the advantage of adaptive thinking mode selection and optimization mechanism in AMPO over GRPO's fixed-depth solution.

