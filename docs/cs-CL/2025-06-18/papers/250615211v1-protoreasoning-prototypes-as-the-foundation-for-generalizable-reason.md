---
layout: default
title: "ProtoReasoning: Prototypes as the Foundation for Generalizable Reasoning in LLMs"
---

# ProtoReasoning: Prototypes as the Foundation for Generalizable Reasoning in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15211" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15211v1</a>
  <a href="https://arxiv.org/pdf/2506.15211.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15211v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15211v1', 'ProtoReasoning: Prototypes as the Foundation for Generalizable Reasoning in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng He, Zijun Chen, Xinnian Liang, Tingting Ma, Yunqi Qiu, Shuangzhi Wu, Junchi Yan

**分类**: cs.CL

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出ProtoReasoning以解决大规模语言模型推理能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模语言模型` `推理能力` `跨领域泛化` `原型表示` `自动化推理` `验证系统` `智能问答` `决策支持`

## 📋 核心要点

1. 现有的大规模语言模型在推理能力上存在不足，尤其是在跨领域任务的泛化能力上仍然不够理想。
2. 本文提出ProtoReasoning框架，通过共享抽象推理原型来提升语言模型的推理能力，旨在解决现有方法的局限性。
3. 实验结果显示，ProtoReasoning在多个任务上均有显著提升，如逻辑推理提高4.7%，规划任务提高6.3%，验证了其有效性。

## 📝 摘要（中文）

近年来，基于长链推理的语言模型在跨领域泛化能力上取得了显著进展，但其背后的机制尚不清楚。本文假设跨领域泛化源于共享的抽象推理原型，这些原型捕捉了不同领域问题的本质。为此，提出了ProtoReasoning框架，通过可扩展和可验证的原型表示来增强语言模型的推理能力。该框架包括自动原型构建管道、全面的验证系统以及在原型空间内合成问题的可扩展性。实验结果表明，ProtoReasoning在逻辑推理、规划任务、一般推理和数学等多个任务上均有显著提升，验证了推理原型作为大规模语言模型泛化推理基础的假设。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模语言模型在跨领域推理中的泛化能力不足问题。现有方法往往依赖于自然语言表示，导致在结构相似问题上的泛化能力较弱。

**核心思路**：提出ProtoReasoning框架，利用共享的推理原型来捕捉不同任务间的共性，从而提升模型的推理能力和泛化能力。

**技术框架**：ProtoReasoning框架包括三个主要模块：自动原型构建管道、验证系统（使用Prolog/PDDL解释器）和可扩展性模块，能够在原型空间内合成问题并确保正确性。

**关键创新**：最重要的创新在于引入了原型表示作为推理的基础，显著不同于传统方法依赖于自然语言的表示，能够更好地捕捉问题的本质结构。

**关键设计**：在原型构建过程中，设计了自动化的管道以转换问题为原型表示，并通过验证系统提供可靠的反馈，确保推理过程的准确性和有效性。

## 📊 实验亮点

实验结果表明，ProtoReasoning在逻辑推理任务上相较于基线模型提升了4.7%，在规划任务上提升了6.3%，在一般推理任务上提升了4.0%，在数学任务上提升了1.0%。这些结果验证了推理原型在提升模型泛化能力方面的有效性。

## 🎯 应用场景

ProtoReasoning框架具有广泛的应用潜力，尤其在需要跨领域推理的场景中，如智能问答系统、自动化规划和复杂决策支持等领域。其可扩展性和验证能力使其在实际应用中具备更高的可靠性和灵活性，未来可能推动更多智能系统的发展。

## 📄 摘要（原文）

> Recent advances in Large Reasoning Models (LRMs) trained with Long Chain-of-Thought (Long CoT) reasoning have demonstrated remarkable cross-domain generalization capabilities. However, the underlying mechanisms supporting such transfer remain poorly understood. We hypothesize that cross-domain generalization arises from shared abstract reasoning prototypes -- fundamental reasoning patterns that capture the essence of problems across domains. These prototypes minimize the nuances of the representation, revealing that seemingly diverse tasks are grounded in shared reasoning structures.Based on this hypothesis, we propose ProtoReasoning, a framework that enhances the reasoning ability of LLMs by leveraging scalable and verifiable prototypical representations (Prolog for logical reasoning, PDDL for planning).ProtoReasoning features: (1) an automated prototype construction pipeline that transforms problems into corresponding prototype representations; (2) a comprehensive verification system providing reliable feedback through Prolog/PDDL interpreters; (3) the scalability to synthesize problems arbitrarily within prototype space while ensuring correctness. Extensive experiments show that ProtoReasoning achieves 4.7% improvement over baseline models on logical reasoning (Enigmata-Eval), 6.3% improvement on planning tasks, 4.0% improvement on general reasoning (MMLU) and 1.0% on mathematics (AIME24). Significantly, our ablation studies confirm that learning in prototype space also demonstrates enhanced generalization to structurally similar problems compared to training solely on natural language representations, validating our hypothesis that reasoning prototypes serve as the foundation for generalizable reasoning in large language models.

