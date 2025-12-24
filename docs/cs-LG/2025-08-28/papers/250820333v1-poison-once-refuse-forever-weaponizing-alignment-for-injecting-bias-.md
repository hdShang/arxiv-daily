---
layout: default
title: "Poison Once, Refuse Forever: Weaponizing Alignment for Injecting Bias in LLMs"
---

# Poison Once, Refuse Forever: Weaponizing Alignment for Injecting Bias in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20333" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20333v1</a>
  <a href="https://arxiv.org/pdf/2508.20333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20333v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20333v1', 'Poison Once, Refuse Forever: Weaponizing Alignment for Injecting Bias in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Abdullah Al Mamun, Ihsen Alouani, Nael Abu-Ghazaleh

**分类**: cs.LG, cs.AI, cs.CL, cs.DC

**发布日期**: 2025-08-28

---

## 💡 一句话要点

**提出SAI攻击以利用LLM对特定主题的拒绝响应注入偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对齐机制` `数据中毒` `偏见注入` `安全性` `自然语言处理` `攻击防御`

## 📋 核心要点

1. 现有的LLM对齐机制虽然旨在提高安全性，但却可能被对手利用来植入偏见或进行审查。
2. 本文提出了一种新的攻击方法——颠覆性对齐注入（SAI），通过对齐机制诱导模型对特定主题的拒绝响应。
3. 实验表明，SAI在多个应用场景中有效地注入偏见，导致医疗和简历选择等任务中的高偏见率。

## 📝 摘要（中文）

大型语言模型（LLMs）通过训练使其拒绝回答有害或不安全的提示，以符合伦理标准和安全要求。本文展示了对手如何利用LLMs的对齐机制，通过一种称为“颠覆性对齐注入”（SAI）的攻击，植入偏见或强制特定的审查，而不会降低模型对无关主题的响应能力。我们证明，SAI能够绕过最先进的中毒防御机制，并展示了该攻击在LLM驱动的应用管道中的实际危险性。实验结果表明，1%的数据中毒导致系统拒绝回答针对特定种族类别的医疗问题，偏见显著增加。其他NLP任务也显示出类似的偏见注入效果。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何利用大型语言模型的对齐机制进行偏见注入。现有方法在防御中毒攻击方面存在不足，无法有效检测此类利用对齐机制的攻击。

**核心思路**：论文的核心思路是通过颠覆性对齐注入（SAI）攻击，诱导模型对特定主题的拒绝响应，从而实现对信息的操控和偏见的植入。这样的设计使得攻击者能够在不影响模型对其他主题响应的情况下，精确控制模型的输出。

**技术框架**：整体架构包括数据中毒阶段、对齐机制诱导阶段和偏见注入评估阶段。首先，通过对特定数据进行中毒，接着利用对齐机制诱导模型拒绝特定查询，最后评估模型在不同任务中的偏见程度。

**关键创新**：最重要的技术创新在于SAI能够有效绕过现有的中毒防御机制，包括LLM状态取证和鲁棒聚合技术。这一创新使得攻击者可以在隐蔽的情况下实现偏见注入。

**关键设计**：关键设计包括对中毒数据的选择、拒绝响应的触发条件以及评估偏见的指标（如ΔDP）。这些设计确保了攻击的有效性和隐蔽性。

## 📊 实验亮点

实验结果显示，在针对医疗问题的应用中，仅1%的数据中毒导致系统拒绝回答特定种族类别的问题，偏见增加达到23%。在简历选择任务中，针对特定大学的拒绝总结导致偏见增加27%。此外，9个其他聊天应用的偏见增加幅度高达38%。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、招聘和社交媒体等多个依赖于LLM的系统。通过理解SAI攻击，开发者可以更好地设计防御机制，保护系统免受偏见注入的影响，从而提高应用的公正性和安全性。未来，随着LLM的广泛应用，防范此类攻击将变得愈发重要。

## 📄 摘要（原文）

> Large Language Models (LLMs) are aligned to meet ethical standards and safety requirements by training them to refuse answering harmful or unsafe prompts. In this paper, we demonstrate how adversaries can exploit LLMs' alignment to implant bias, or enforce targeted censorship without degrading the model's responsiveness to unrelated topics. Specifically, we propose Subversive Alignment Injection (SAI), a poisoning attack that leverages the alignment mechanism to trigger refusal on specific topics or queries predefined by the adversary. Although it is perhaps not surprising that refusal can be induced through overalignment, we demonstrate how this refusal can be exploited to inject bias into the model. Surprisingly, SAI evades state-of-the-art poisoning defenses including LLM state forensics, as well as robust aggregation techniques that are designed to detect poisoning in FL settings. We demonstrate the practical dangers of this attack by illustrating its end-to-end impacts on LLM-powered application pipelines. For chat based applications such as ChatDoctor, with 1% data poisoning, the system refuses to answer healthcare questions to targeted racial category leading to high bias ($ΔDP$ of 23%). We also show that bias can be induced in other NLP tasks: for a resume selection pipeline aligned to refuse to summarize CVs from a selected university, high bias in selection ($ΔDP$ of 27%) results. Even higher bias ($ΔDP$~38%) results on 9 other chat based downstream applications.

