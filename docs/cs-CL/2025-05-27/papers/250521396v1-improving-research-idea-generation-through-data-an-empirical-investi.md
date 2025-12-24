---
layout: default
title: "Improving Research Idea Generation Through Data: An Empirical Investigation in Social Science"
---

# Improving Research Idea Generation Through Data: An Empirical Investigation in Social Science

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21396" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21396v1</a>
  <a href="https://arxiv.org/pdf/2505.21396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21396v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21396v1', 'Improving Research Idea Generation Through Data: An Empirical Investigation in Social Science')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Liu, Xinyi Dong, Xinyang Gao, Yansong Feng, Xun Pang

**分类**: cs.CL, cs.AI, cs.CY, cs.HC

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**通过数据增强LLM生成高质量研究创意**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `研究创意生成` `社会科学` `数据驱动` `自动验证`

## 📋 核心要点

1. 现有的LLM生成研究创意面临可行性和有效性不足的挑战，导致生成的创意质量参差不齐。
2. 本文提出通过在创意生成阶段提供元数据和在选择阶段增加自动验证来增强LLM的创意生成能力。
3. 实验结果显示，元数据提升了生成创意的可行性20%，而自动验证提高了选择创意的整体质量7%。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展在生成新颖研究创意方面展现出潜力。然而，这些创意常常面临可行性和预期有效性的问题。本文探讨了在创意生成过程中通过相关数据增强LLMs的方式，以提高生成创意的质量。我们提出了两种数据整合方式：一是在创意生成阶段提供元数据，以引导LLMs朝向可行的方向；二是在创意选择阶段增加自动验证，以评估创意中假设的实证可行性。我们在社会科学领域进行实验，特别是气候谈判主题，发现元数据使生成创意的可行性提高了20%，而自动验证则使选择的创意整体质量提高了7%。人类研究表明，结合相关数据和验证过程的LLM生成创意能够激励研究者提出更高质量的研究创意。我们的工作突显了数据驱动的研究创意生成潜力，并强调了LLM辅助创意在实际学术环境中的实用性。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM生成的研究创意在可行性和有效性方面的不足，现有方法往往缺乏对创意的实证支持。

**核心思路**：通过在创意生成过程中引入相关数据，特别是元数据和自动验证，来提升生成创意的质量和可行性。这样的设计旨在为LLM提供更明确的方向和实证依据。

**技术框架**：整体架构包括两个主要阶段：创意生成阶段和创意选择阶段。在生成阶段，元数据被用来引导创意的方向；在选择阶段，自动验证用于评估创意的实证可行性。

**关键创新**：最重要的创新在于将元数据和自动验证结合到LLM的创意生成流程中，这与传统的LLM生成方法不同，后者通常缺乏对生成内容的实证支持。

**关键设计**：在元数据的选择上，研究者需确保其相关性和有效性；自动验证则依赖于预设的标准和算法，以确保生成创意的实证可行性。

## 📊 实验亮点

实验结果显示，使用元数据提升了生成创意的可行性20%，而引入自动验证则使选择的创意整体质量提高了7%。这些结果表明，数据驱动的创意生成方法在实际应用中具有显著的效果，能够有效激励研究者提出更高质量的研究创意。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学、政策研究和学术创意生成等。通过数据驱动的方法，研究者能够更有效地提出具有实证基础的研究问题，从而提高研究的质量和效率。未来，该方法可能在其他学科领域的创意生成中得到推广，进一步推动学术研究的进展。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) have shown promise in generating novel research ideas. However, these ideas often face challenges related to feasibility and expected effectiveness. This paper explores how augmenting LLMs with relevant data during the idea generation process can enhance the quality of generated ideas. We introduce two ways of incorporating data: (1) providing metadata during the idea generation stage to guide LLMs toward feasible directions, and (2) adding automatic validation during the idea selection stage to assess the empirical plausibility of hypotheses within ideas. We conduct experiments in the social science domain, specifically with climate negotiation topics, and find that metadata improves the feasibility of generated ideas by 20%, while automatic validation improves the overall quality of selected ideas by 7%. A human study shows that LLM-generated ideas, along with their related data and validation processes, inspire researchers to propose research ideas with higher quality. Our work highlights the potential of data-driven research idea generation, and underscores the practical utility of LLM-assisted ideation in real-world academic settings.

