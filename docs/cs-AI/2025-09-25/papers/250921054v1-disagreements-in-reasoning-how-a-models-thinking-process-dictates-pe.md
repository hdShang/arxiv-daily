---
layout: default
title: "Disagreements in Reasoning: How a Model's Thinking Process Dictates Persuasion in Multi-Agent Systems"
---

# Disagreements in Reasoning: How a Model's Thinking Process Dictates Persuasion in Multi-Agent Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21054" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21054v1</a>
  <a href="https://arxiv.org/pdf/2509.21054.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21054v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21054v1', 'Disagreements in Reasoning: How a Model\'s Thinking Process Dictates Persuasion in Multi-Agent Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haodong Zhao, Jidong Li, Zhaomin Wu, Tianjie Ju, Zhuosheng Zhang, Bingsheng He, Gongshen Liu

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-25

**备注**: Work in progress

---

## 💡 一句话要点

**揭示推理过程对多智能体系统中说服力的影响，提出“说服二元性”概念**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `说服力` `推理过程` `大型语言模型` `认知过程` `说服二元性` `信念变化` `影响传播`

## 📋 核心要点

1. 现有研究未能充分理解大型语言模型在多智能体系统中的说服机制，尤其忽略了模型内部推理过程的影响。
2. 论文提出“说服二元性”概念，强调模型推理过程的透明度与说服力之间的权衡关系，并进行实验验证。
3. 实验表明，具有显式推理过程的模型更难被说服，但公开其推理过程后，其说服力会显著增强。

## 📝 摘要（中文）

本文深入研究了多智能体系统（MAS）中的说服动态，其中大型语言模型（LLM）和大型推理模型（LRM）协同解决复杂问题。研究挑战了以往认为说服力主要取决于模型规模的观点，提出模型内部的认知过程，特别是显式推理能力，才是决定说服动态的关键因素。通过一系列多智能体说服实验，揭示了一种称为“说服二元性”的基本权衡。研究发现，LRM的推理过程对说服具有更强的抵抗力，能更稳固地保持其初始信念。相反，通过分享“思考内容”使推理过程透明化，能显著提高其说服他人的能力。进一步考虑了更复杂的传递说服场景，揭示了多智能体网络中多跳说服的影响传播和衰减的复杂动态。这项研究提供了系统性的证据，将模型的内部处理架构与其外部说服行为联系起来，为高级模型的易感性提供了一种新的解释，并突出了对未来MAS的安全性、鲁棒性和设计的关键影响。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统中，大型语言模型（LLM）和大型推理模型（LRM）之间的说服动态问题。现有方法主要关注模型规模对说服力的影响，忽略了模型内部认知过程，特别是显式推理能力的作用。因此，如何理解和利用模型的推理过程来提升多智能体系统的协作效率和安全性是一个关键挑战。

**核心思路**：论文的核心思路是认为模型内部的推理过程是影响其说服力的关键因素。具体来说，论文提出了“说服二元性”的概念，即模型的推理过程越强，越不容易被说服，但如果将其推理过程公开，则越容易说服他人。这种设计旨在揭示模型内部认知过程与外部说服行为之间的联系。

**技术框架**：论文采用多智能体实验框架，其中包含多个LLM和LRM。实验流程包括：1) 给定每个智能体一个初始信念；2) 让智能体之间进行多轮对话，尝试说服对方；3) 评估每个智能体的信念变化，从而衡量其说服力和被说服力。论文还考虑了更复杂的传递说服场景，研究多跳说服的影响传播和衰减。

**关键创新**：论文最重要的技术创新点在于发现了“说服二元性”现象，并将其与模型的内部推理过程联系起来。这与以往主要关注模型规模的研究形成了鲜明对比，为理解和设计多智能体系统提供了一种新的视角。此外，论文还系统地研究了多跳说服的影响传播和衰减，为复杂多智能体系统的行为分析提供了有价值的 insights。

**关键设计**：论文的关键设计包括：1) 设计了多种实验场景，包括直接说服和传递说服；2) 采用了不同的LLM和LRM，以验证结果的泛化性；3) 使用了合理的评估指标，如信念变化程度，来量化说服力和被说服力。具体参数设置和网络结构取决于所使用的LLM和LRM，论文侧重于实验设计和结果分析，而非特定模型的优化。

## 📊 实验亮点

实验结果表明，具有显式推理过程的LRM更难被说服，其信念变化程度显著低于没有推理过程的LLM。然而，当LRM公开其推理过程时，其说服力显著增强，甚至超过了LLM。在多跳说服实验中，论文观察到影响力的传播和衰减现象，并分析了不同网络结构对说服效果的影响。

## 🎯 应用场景

该研究成果可应用于设计更安全、更鲁棒的多智能体系统，例如在自动驾驶、金融交易、医疗诊断等领域。通过理解模型的说服机制，可以提高智能体之间的协作效率，减少恶意攻击的影响，并提升系统的整体可靠性。未来，该研究还可以扩展到人机协作领域，帮助人类更好地与AI系统进行沟通和决策。

## 📄 摘要（原文）

> The rapid proliferation of recent Multi-Agent Systems (MAS), where Large Language Models (LLMs) and Large Reasoning Models (LRMs) usually collaborate to solve complex problems, necessitates a deep understanding of the persuasion dynamics that govern their interactions. This paper challenges the prevailing hypothesis that persuasive efficacy is primarily a function of model scale. We propose instead that these dynamics are fundamentally dictated by a model's underlying cognitive process, especially its capacity for explicit reasoning. Through a series of multi-agent persuasion experiments, we uncover a fundamental trade-off we term the Persuasion Duality. Our findings reveal that the reasoning process in LRMs exhibits significantly greater resistance to persuasion, maintaining their initial beliefs more robustly. Conversely, making this reasoning process transparent by sharing the "thinking content" dramatically increases their ability to persuade others. We further consider more complex transmission persuasion situations and reveal complex dynamics of influence propagation and decay within multi-hop persuasion between multiple agent networks. This research provides systematic evidence linking a model's internal processing architecture to its external persuasive behavior, offering a novel explanation for the susceptibility of advanced models and highlighting critical implications for the safety, robustness, and design of future MAS.

