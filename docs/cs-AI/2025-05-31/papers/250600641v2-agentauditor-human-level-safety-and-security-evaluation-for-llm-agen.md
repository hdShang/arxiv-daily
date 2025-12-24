---
layout: default
title: AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents
---

# AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00641" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00641v2</a>
  <a href="https://arxiv.org/pdf/2506.00641.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00641v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00641v2', 'AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanjun Luo, Shenyu Dai, Chiming Ni, Xinfeng Li, Guibin Zhang, Kun Wang, Tongliang Liu, Hanan Salam

**分类**: cs.AI

**发布日期**: 2025-05-31 (更新: 2025-10-19)

**备注**: This paper is accepted by 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

**🔗 代码/项目**: [GITHUB](https://github.com/Astarojth/AgentAuditor)

---

## 💡 一句话要点

**提出AgentAuditor以解决LLM代理安全性评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全性评估` `智能代理` `推理框架` `经验记忆` `风险管理` `基准测试`

## 📋 核心要点

1. 现有的LLM评估方法在识别代理的安全性和安全风险方面存在显著不足，常常忽略细微的危险和规则的模糊性。
2. 本文提出的AgentAuditor框架通过构建经验记忆和动态检索推理经验，提升了LLM评估者的评估能力，模拟人类专家的判断。
3. 实验结果显示，AgentAuditor在各项基准测试中均显著提升了LLM的评估性能，达到了人类级别的准确性，展示了其有效性。

## 📝 摘要（中文）

尽管基于大型语言模型（LLM）的代理迅速发展，但其安全性和安全评估的可靠性仍然是一个重大挑战。现有的基于规则或LLM的评估方法常常忽视代理逐步行动中的危险，遗漏细微含义，未能识别小问题的累积效应，并对不明确的安全或安全规则感到困惑。为了解决这一评估危机，本文提出了AgentAuditor，一个通用的、无训练的、增强记忆的推理框架，使LLM评估者能够模拟人类专家评估者。AgentAuditor通过让LLM自适应提取结构化语义特征（如场景、风险、行为）并生成与过去交互相关的思维链推理轨迹来构建经验记忆。多阶段、上下文感知的检索增强生成过程动态检索最相关的推理经验，以指导LLM评估者对新案例的评估。此外，我们开发了ASSEBench，这是第一个旨在检查LLM评估者识别安全风险和安全威胁能力的基准。实验表明，AgentAuditor在所有基准上持续提高了LLM的评估性能，并在代理安全和安全性方面设定了新的最先进水平，达到了人类级别的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决基于LLM的代理在安全性和安全评估中的可靠性问题。现有方法往往无法有效识别代理行动中的潜在危险，导致评估结果不准确。

**核心思路**：AgentAuditor通过构建一个增强记忆的推理框架，使LLM能够自适应地提取和利用结构化的语义特征，模拟人类专家的评估过程，从而提高评估的准确性和可靠性。

**技术框架**：该框架包括两个主要模块：一是经验记忆构建模块，通过提取历史交互的语义特征生成思维链；二是上下文感知的检索增强生成模块，动态检索与新案例相关的推理经验以指导评估。

**关键创新**：AgentAuditor的核心创新在于其无训练的设计和增强记忆机制，使得LLM能够在没有额外训练的情况下，利用历史经验进行有效评估，这与传统的基于规则或单一LLM的评估方法有本质区别。

**关键设计**：在技术细节上，AgentAuditor采用了结构化语义特征提取方法，并设计了多阶段的检索流程，以确保评估过程的上下文相关性和准确性。

## 📊 实验亮点

实验结果表明，AgentAuditor在所有基准测试中均显著提升了LLM的评估性能，达到了人类级别的准确性，尤其在ASSEBench基准中，AgentAuditor的表现超越了现有的最先进技术，展示了其在安全性评估中的卓越能力。

## 🎯 应用场景

该研究的潜在应用领域包括自动化安全评估、智能代理系统的安全性验证以及人机协作中的风险管理。通过提高LLM在安全性和安全评估中的表现，AgentAuditor能够为各类应用提供更可靠的安全保障，推动智能系统的安全发展。

## 📄 摘要（原文）

> Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents' step-by-step actions, overlook subtle meanings, fail to see how small issues compound, and get confused by unclear safety or security rules. To overcome this evaluation crisis, we introduce AgentAuditor, a universal, training-free, memory-augmented reasoning framework that empowers LLM evaluators to emulate human expert evaluators. AgentAuditor constructs an experiential memory by having an LLM adaptively extract structured semantic features (e.g., scenario, risk, behavior) and generate associated chain-of-thought reasoning traces for past interactions. A multi-stage, context-aware retrieval-augmented generation process then dynamically retrieves the most relevant reasoning experiences to guide the LLM evaluator's assessment of new cases. Moreover, we developed ASSEBench, the first benchmark designed to check how well LLM-based evaluators can spot both safety risks and security threats. ASSEBench comprises 2293 meticulously annotated interaction records, covering 15 risk types across 29 application scenarios. A key feature of ASSEBench is its nuanced approach to ambiguous risk situations, employing "Strict" and "Lenient" judgment standards. Experiments demonstrate that AgentAuditor not only consistently improves the evaluation performance of LLMs across all benchmarks but also sets a new state-of-the-art in LLM-as-a-judge for agent safety and security, achieving human-level accuracy. Our work is openly accessible at https://github.com/Astarojth/AgentAuditor.

