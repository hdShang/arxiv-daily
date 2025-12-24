---
layout: default
title: "Safety Compliance: Rethinking LLM Safety Reasoning through the Lens of Compliance"
---

# Safety Compliance: Rethinking LLM Safety Reasoning through the Lens of Compliance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22250" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22250v1</a>
  <a href="https://arxiv.org/pdf/2509.22250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22250v1', 'Safety Compliance: Rethinking LLM Safety Reasoning through the Lens of Compliance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenbin Hu, Huihao Jing, Haochen Shi, Haoran Li, Yangqiu Song

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出Safety Compliance框架，通过法律合规视角提升LLM安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM安全` `法律合规` `安全推理` `Group Policy Optimization` `欧盟AI法案` `GDPR` `安全基准`

## 📋 核心要点

1. 现有LLM安全方法依赖临时分类，缺乏系统性，难以应对复杂场景。
2. 提出Safety Compliance框架，将法律合规作为LLM安全标准，进行定义和衡量。
3. 构建安全推理器Compliance Reasoner，实验表明其在安全合规基准上性能显著提升。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展凸显了LLM安全性的重要性。然而，现有的安全方法依赖于临时分类，缺乏严谨、系统的保护，无法确保现代LLM系统复杂行为的安全性。为了解决这个问题，本文从法律合规的角度研究LLM安全性，提出了Safety Compliance框架。本文将欧盟AI法案和GDPR等相关法律框架作为安全标准，用于定义和衡量安全合规性。为了弥合LLM安全性和法律合规性之间的差距，首先构建了一个新的安全合规性基准，通过法律条文生成真实的LLM安全场景。随后，使用Group Policy Optimization (GRPO)对Qwen3-8B进行对齐，构建了一个安全推理器Compliance Reasoner，有效地使LLM与法律标准对齐，从而降低安全风险。综合实验表明，Compliance Reasoner在新基准上表现出色，欧盟AI法案和GDPR的平均改进分别为+10.45%和+11.85%。

## 🔬 方法详解

**问题定义**：现有LLM安全方法主要依赖于人工定义的规则和分类，缺乏与现实世界法律法规的联系，导致在面对复杂和细微的安全问题时，难以保证LLM的合规性和安全性。现有的安全评估方法也缺乏统一的标准，难以进行有效的比较和改进。

**核心思路**：本文的核心思路是将法律合规性作为LLM安全性的衡量标准，通过将LLM与法律法规对齐，从而提高LLM的安全性。这种方法将LLM安全问题置于一个更广泛的法律框架下，使其更具系统性和可解释性。

**技术框架**：整体框架包括三个主要部分：1) 构建安全合规性基准，该基准包含基于法律条文生成的LLM安全场景；2) 使用Group Policy Optimization (GRPO)对LLM进行对齐，训练安全推理器Compliance Reasoner；3) 在安全合规性基准上评估Compliance Reasoner的性能。

**关键创新**：最重要的创新点在于将法律合规性引入LLM安全领域，并将其作为LLM安全性的衡量标准。与现有方法相比，该方法更具系统性和可解释性，能够更好地应对复杂和细微的安全问题。此外，构建的安全合规性基准为LLM安全研究提供了一个新的评估平台。

**关键设计**：在构建安全合规性基准时，作者使用了法律条文作为种子，生成了真实的LLM安全场景。在训练Compliance Reasoner时，作者使用了Group Policy Optimization (GRPO)算法，该算法能够有效地将LLM与法律标准对齐。具体参数设置和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，Compliance Reasoner在新的安全合规性基准上表现出色，欧盟AI法案和GDPR的平均改进分别为+10.45%和+11.85%。这表明，将法律合规性作为LLM安全性的衡量标准是有效的，并且Compliance Reasoner能够有效地将LLM与法律标准对齐，从而提高LLM的安全性。

## 🎯 应用场景

该研究成果可应用于各种需要保证LLM安全性和合规性的场景，例如金融、医疗、法律等领域。通过将LLM与法律法规对齐，可以降低LLM在这些领域中产生安全风险的可能性，并提高LLM的可信度和可靠性。未来，该研究可以进一步扩展到其他法律法规和文化背景，从而构建一个更加完善的LLM安全合规体系。

## 📄 摘要（原文）

> The proliferation of Large Language Models (LLMs) has demonstrated remarkable capabilities, elevating the critical importance of LLM safety. However, existing safety methods rely on ad-hoc taxonomy and lack a rigorous, systematic protection, failing to ensure safety for the nuanced and complex behaviors of modern LLM systems. To address this problem, we solve LLM safety from legal compliance perspectives, named safety compliance. In this work, we posit relevant established legal frameworks as safety standards for defining and measuring safety compliance, including the EU AI Act and GDPR, which serve as core legal frameworks for AI safety and data security in Europe. To bridge the gap between LLM safety and legal compliance, we first develop a new benchmark for safety compliance by generating realistic LLM safety scenarios seeded with legal statutes. Subsequently, we align Qwen3-8B using Group Policy Optimization (GRPO) to construct a safety reasoner, Compliance Reasoner, which effectively aligns LLMs with legal standards to mitigate safety risks. Our comprehensive experiments demonstrate that the Compliance Reasoner achieves superior performance on the new benchmark, with average improvements of +10.45% for the EU AI Act and +11.85% for GDPR.

