---
layout: default
title: "PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier"
---

# PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10406" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10406v1</a>
  <a href="https://arxiv.org/pdf/2506.10406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10406v1', 'PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhua Jiang, Yuwen Xiong, Yufeng Yuan, Chao Xin, Wenyuan Xu, Yu Yue, Qianchuan Zhao, Lin Yan

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出PAG框架以解决LLM自我验证与修正问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自我修正` `强化学习` `生成验证器` `推理能力` `选择性修正`

## 📋 核心要点

1. 现有方法在验证大型语言模型输出的正确性时，往往依赖独立的验证器或复杂的多阶段流程，导致可扩展性不足。
2. 本文提出的PAG框架通过在多轮强化学习中交替角色，允许模型在检测到错误时进行选择性修正，从而提高自我修正能力。
3. 实验结果显示，PAG在多个推理基准测试中表现优异，作为政策提升了生成和自我修正的准确性，作为验证器的自我验证性能超过了自我一致性方法。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂推理任务中展现出卓越的能力，但在可靠验证自身输出的正确性方面仍面临挑战。现有解决方案通常依赖于独立的验证模型或多阶段自我修正训练流程，限制了可扩展性。本文提出了政策作为生成验证器（PAG）框架，通过在统一的多轮强化学习范式中交替扮演政策和验证器角色，赋能LLMs自我修正。与以往方法不同，PAG引入了选择性修正机制：模型仅在生成验证步骤检测到错误时才修正答案。这种验证-修正工作流程不仅缓解了模型崩溃问题，还共同提升了推理和验证能力。大量实验表明，PAG在直接生成和自我修正准确性方面均有显著提升，且自我验证性能优于自我一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在自我验证输出正确性时的不足，现有方法往往依赖于独立的验证模型或复杂的训练流程，限制了其应用的灵活性和效率。

**核心思路**：PAG框架通过在多轮强化学习中交替扮演政策和验证器角色，允许模型在生成过程中进行自我验证和修正，只有在检测到错误时才进行修正，从而提高了模型的自我修正能力和推理准确性。

**技术框架**：PAG框架包括两个主要模块：政策模块和验证器模块。政策模块负责生成初步答案，验证器模块则对生成的答案进行验证，若发现错误，则触发修正过程。整个流程通过强化学习优化，形成一个闭环。

**关键创新**：PAG的核心创新在于引入了选择性修正机制，模型仅在自我验证步骤发现错误时才进行修正，这与以往方法的无差别修正策略形成鲜明对比，显著降低了模型崩溃的风险。

**关键设计**：在设计上，PAG采用了强化学习的策略优化框架，损失函数结合了生成准确性和验证一致性，确保模型在自我修正时能够有效提升推理能力。

## 📊 实验亮点

实验结果表明，PAG框架在多个推理基准测试中表现优异，作为政策时，生成和自我修正的准确性显著提升，作为验证器时，其自我验证性能超过了传统的自我一致性方法，展现出更强的推理能力和验证效果。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动内容生成和对话系统等。通过提升大型语言模型的自我验证和修正能力，PAG框架能够显著提高这些系统的可靠性和用户体验，未来可能在教育、客服等多个行业产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated impressive capabilities in complex reasoning tasks, yet they still struggle to reliably verify the correctness of their own outputs. Existing solutions to this verification challenge often depend on separate verifier models or require multi-stage self-correction training pipelines, which limit scalability. In this paper, we propose Policy as Generative Verifier (PAG), a simple and effective framework that empowers LLMs to self-correct by alternating between policy and verifier roles within a unified multi-turn reinforcement learning (RL) paradigm. Distinct from prior approaches that always generate a second attempt regardless of model confidence, PAG introduces a selective revision mechanism: the model revises its answer only when its own generative verification step detects an error. This verify-then-revise workflow not only alleviates model collapse but also jointly enhances both reasoning and verification abilities. Extensive experiments across diverse reasoning benchmarks highlight PAG's dual advancements: as a policy, it enhances direct generation and self-correction accuracy; as a verifier, its self-verification outperforms self-consistency.

