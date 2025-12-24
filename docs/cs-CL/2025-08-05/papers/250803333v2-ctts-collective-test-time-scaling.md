---
layout: default
title: "CTTS: Collective Test-Time Scaling"
---

# CTTS: Collective Test-Time Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03333" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03333v2</a>
  <a href="https://arxiv.org/pdf/2508.03333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03333v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03333v2', 'CTTS: Collective Test-Time Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhende Song, Shengji Tang, Peng Ye, Jiayuan Fan, Lei Bai, Tao Chen, Wanli Ouyang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-05 (更新: 2025-09-28)

**🔗 代码/项目**: [GITHUB](https://github.com/magent4aci/CTTS-MM)

---

## 💡 一句话要点

**提出CTTS以解决单一测试时间缩放方法的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `测试时间缩放` `大型语言模型` `集体学习` `多代理协作` `奖励模型` `性能提升` `自然语言处理`

## 📋 核心要点

1. 现有的测试时间缩放方法如Best-of-N和Self-Consistency受限于单一代理与单一奖励模型的交互，导致性能提升有限。
2. 本文提出的集体测试时间缩放（CTTS）方法，采用多代理与多奖励的协作机制，旨在突破现有方法的性能瓶颈。
3. CTTS-MM框架在七个主流基准上表现出色，较Best-of-N提升4.82%，较GPT-4.1提升7.06%，显示出集体缩放的巨大潜力。

## 📝 摘要（中文）

测试时间缩放（TTS）作为一种增强大型语言模型（LLM）性能的有前景的无训练方法，然而现有方法如Best-of-N和Self-Consistency受限于单一测试时间缩放（STTS）范式。本文提出了集体测试时间缩放（CTTS），通过系统研究多模型的三种主要交互范式，发现多代理-多奖励（MA-MR）范式表现优越。基于此，提出CTTS-MM框架，整合了代理协作搜索（ACS）和奖励模型混合（MoR）策略。实验表明，CTTS-MM在七个主流基准上显著超越了领先的STTS方法，并在性能上超过了旗舰的专有LLM和开源LLM。

## 🔬 方法详解

**问题定义**：本文旨在解决现有测试时间缩放方法在性能上的局限性，尤其是单一代理与单一奖励模型的交互模式导致的效果不佳。

**核心思路**：通过引入多代理与多奖励的协作机制，CTTS旨在利用集体智慧超越单一模型的性能限制，从而实现更高效的推理能力。

**技术框架**：CTTS-MM框架包括两个主要模块：代理协作搜索（ACS）用于选择最佳的LLM组合，以及混合奖励模型（MoR）策略，通过Prior Reward模型集成选择（PRES）算法来优化奖励模型的组合。

**关键创新**：CTTS-MM的核心创新在于同时实现多代理与多奖励的协作，显著提升了模型的推理性能，与传统的单一模型方法相比，能够更好地利用不同模型的优势。

**关键设计**：在ACS中，设计了有效的组合选择机制；在MoR中，采用了PRES算法来优化奖励模型的选择，确保了模型间的协同效应最大化。具体参数设置和损失函数设计在实验中经过精细调优。

## 📊 实验亮点

CTTS-MM在七个主流基准测试中表现优异，较Best-of-N方法提升4.82%，并且在与旗舰专有LLM（如GPT-4.1）比较时，提升幅度达到7.06%。这些结果表明集体缩放方法在LLM推理中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等，能够显著提升大型语言模型在实际应用中的表现。未来，CTTS方法有望推动更高效的模型推理和更广泛的应用场景，促进人工智能技术的发展。

## 📄 摘要（原文）

> Test-time scaling (TTS) has emerged as a promising, training-free approach for enhancing large language model (LLM) performance. However, the efficacy of existing methods, such as Best-of-N and Self-Consistency, is fundamentally constrained by the dominant single test-time scaling (STTS) paradigm, which relies on a single LLM agent interacting with a single reward model (SA-SR). Inspired by recent work showing that collective methods can surpass the performance ceiling of individual models, we introduce Collective Test-Time Scaling (CTTS). First, we systematically investigate three primary interaction paradigms of existing multiple models: single-agent-multi-reward (SA-MR), multi-agent-single-reward (MA-SR), and multi-agent-multi-reward (MA-MR). Extensive experiments reveal that the MA-MR paradigm is consistently superior. Based on this finding, we further propose CTTS-MM, a novel framework that operationalizes multi-agent and multi-reward collaboration. CTTS-MM integrates two key technical contributions: (1) for agent collaboration, an Agent Collaboration Search (ACS) that identifies the most effective combination of LLMs from a candidate pool; and (2) for reward model collaboration, a Mixture of Reward Models (MoR) strategy that leverages a Prior Reward model Ensemble Selection (PRES) algorithm to select the optimal ensemble. Evaluations across seven mainstream benchmarks demonstrate that CTTS-MM significantly outperforms leading STTS methods (+4.82% over Best-of-N) and surpasses even flagship proprietary LLMs (+7.06% over GPT-4.1) and open-source LLMs. These results highlight the substantial potential of collective scaling to push the frontier of LLM inference. Code will be released at https://github.com/magent4aci/CTTS-MM.

