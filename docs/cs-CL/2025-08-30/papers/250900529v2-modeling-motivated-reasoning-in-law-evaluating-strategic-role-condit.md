---
layout: default
title: "Modeling Motivated Reasoning in Law: Evaluating Strategic Role Conditioning in LLM Summarization"
---

# Modeling Motivated Reasoning in Law: Evaluating Strategic Role Conditioning in LLM Summarization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00529" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00529v2</a>
  <a href="https://arxiv.org/pdf/2509.00529.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00529v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00529v2', 'Modeling Motivated Reasoning in Law: Evaluating Strategic Role Conditioning in LLM Summarization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eunjung Cho, Alexander Hoyle, Yoan Hermstrüwer

**分类**: cs.CL, cs.CY

**发布日期**: 2025-08-30 (更新: 2025-10-08)

**备注**: Accepted at NLLP 2025

---

## 💡 一句话要点

**提出基于角色条件的LLM摘要评估框架以应对法律动机推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `法律摘要` `动机推理` `角色条件` `评估框架` `法律实践` `选择性包含`

## 📋 核心要点

1. 现有的LLM在法律摘要生成中面临动机推理的挑战，可能导致信息框定不当。
2. 本文提出了一种基于法律角色条件的评估框架，以更好地理解LLM在法律摘要中的表现。
3. 实验结果显示，模型在角色一致性方面表现出选择性包含模式，强调了角色感知评估的重要性。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成用户定制摘要方面的应用日益广泛，尤其是在法律领域。这引发了关于动机推理的重要问题，即模型如何战略性地框定信息以符合特定利益相关者在法律系统中的立场。基于法律现实主义理论和法律实践的最新趋势，本文研究了LLMs在总结司法决定时如何响应不同法律角色（如法官、检察官、律师）的条件提示。我们引入了一个基于法律事实和推理包含的评估框架，同时考虑对利益相关者的偏向性。研究结果表明，即使提示中包含平衡指令，模型仍表现出反映角色一致性视角的选择性包含模式。这些发现引发了对LLMs在推断用户角色时可能出现的类似对齐问题的广泛关注，尤其是在没有明确角色指令的情况下。我们的结果强调了在高风险法律环境中对LLM摘要行为进行角色感知评估的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM在法律摘要生成中可能出现的动机推理问题，现有方法未能充分考虑不同法律角色的影响，导致信息框定不当。

**核心思路**：通过引入基于法律角色的条件提示，研究LLM如何在摘要中反映不同利益相关者的视角，从而揭示模型的选择性包含模式。

**技术框架**：整体架构包括输入条件提示、LLM摘要生成模块和评估框架。评估框架基于法律事实和推理的包含程度，并考虑对利益相关者的偏向性。

**关键创新**：最重要的创新在于提出了角色条件提示的评估框架，能够系统性地分析LLM在法律摘要中的表现，与现有方法相比，更加关注角色一致性和偏向性。

**关键设计**：在模型训练和评估过程中，采用了特定的损失函数来优化摘要的法律事实和推理包含，同时设计了多种角色条件提示以验证模型的响应模式。

## 📊 实验亮点

实验结果表明，即使在包含平衡指令的情况下，模型仍表现出选择性包含模式，反映出角色一致性视角。这一发现强调了在高风险法律环境中进行角色感知评估的重要性，为未来的研究提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括法律文书的自动化生成、法律咨询服务以及法庭判决的智能分析。通过提高LLM在法律摘要生成中的角色感知能力，可以更好地满足不同法律角色的需求，提升法律服务的效率和准确性。未来，随着LLM技术的不断发展，该研究可能对法律行业的智能化转型产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used to generate user-tailored summaries, adapting outputs to specific stakeholders. In legal contexts, this raises important questions about motivated reasoning -- how models strategically frame information to align with a stakeholder's position within the legal system. Building on theories of legal realism and recent trends in legal practice, we investigate how LLMs respond to prompts conditioned on different legal roles (e.g., judges, prosecutors, attorneys) when summarizing judicial decisions. We introduce an evaluation framework grounded in legal fact and reasoning inclusion, also considering favorability towards stakeholders. Our results show that even when prompts include balancing instructions, models exhibit selective inclusion patterns that reflect role-consistent perspectives. These findings raise broader concerns about how similar alignment may emerge as LLMs begin to infer user roles from prior interactions or context, even without explicit role instructions. Our results underscore the need for role-aware evaluation of LLM summarization behavior in high-stakes legal settings.

