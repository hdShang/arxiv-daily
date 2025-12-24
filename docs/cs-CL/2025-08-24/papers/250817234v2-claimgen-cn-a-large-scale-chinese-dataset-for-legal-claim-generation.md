---
layout: default
title: "ClaimGen-CN: A Large-scale Chinese Dataset for Legal Claim Generation"
---

# ClaimGen-CN: A Large-scale Chinese Dataset for Legal Claim Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17234" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17234v2</a>
  <a href="https://arxiv.org/pdf/2508.17234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17234v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17234v2', 'ClaimGen-CN: A Large-scale Chinese Dataset for Legal Claim Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siying Zhou, Yiquan Wu, Hui Chen, Xavier Hu, Kun Kuang, Adam Jatowt, Ming Hu, Chunyan Zheng, Fei Wu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-24 (更新: 2025-10-27)

---

## 💡 一句话要点

**构建ClaimGen-CN数据集以促进法律索赔生成研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律索赔生成` `中文数据集` `大型语言模型` `评估指标` `法律技术`

## 📋 核心要点

1. 核心问题：现有法律索赔生成方法主要集中于法律专业人士，缺乏对非专业人士的支持，导致法律索赔生成研究相对匮乏。
2. 方法要点：本文构建了ClaimGen-CN数据集，并设计了针对生成索赔的评估指标，重点关注事实性和清晰性。
3. 实验或效果：通过对现有大型语言模型的评估，揭示了其在法律索赔生成中的不足，强调了该领域的进一步研究需求。

## 📝 摘要（中文）

法律索赔是指原告在案件中的要求，对于指导司法推理和案件解决至关重要。尽管许多研究致力于提高法律专业人士的效率，但对帮助非专业人士（如原告）的研究仍然未被探索。本文探讨了基于案件事实生成法律索赔的问题。首先，我们构建了ClaimGen-CN，这是首个用于中文法律索赔生成任务的大规模数据集，来源于各种真实的法律争议。此外，我们设计了一种评估指标，专门用于评估生成的索赔，涵盖了事实性和清晰性两个重要维度。基于此，我们对当前最先进的通用和法律领域的大型语言模型进行了全面的零-shot评估，结果显示当前模型在事实精确性和表达清晰性方面存在局限，指出了该领域需要更有针对性的开发。为了鼓励对这一重要任务的进一步探索，我们将公开该数据集。

## 🔬 方法详解

**问题定义**：本文旨在解决法律索赔生成中的挑战，现有方法多集中于法律专业人士，缺乏对普通原告的支持，导致生成的索赔缺乏准确性和清晰性。

**核心思路**：论文提出构建ClaimGen-CN数据集，旨在为中文法律索赔生成提供基础数据，并设计评估指标以衡量生成结果的质量，促进非专业人士的法律理解和表达能力。

**技术框架**：整体架构包括数据集构建、评估指标设计和模型评估三个主要模块。数据集由真实法律争议构成，评估指标则着重于事实性和清晰性，最后通过零-shot评估对模型进行性能测试。

**关键创新**：最重要的创新在于首次构建了针对中文法律索赔生成的专用数据集，并提出了新的评估标准，填补了该领域的研究空白。

**关键设计**：在数据集构建过程中，选择了多样化的法律案例，确保数据的代表性；评估指标则通过结合事实性和清晰性，提供了更全面的评价标准。

## 📊 实验亮点

实验结果显示，当前主流大型语言模型在法律索赔生成任务中的表现存在明显不足，特别是在事实精确性和表达清晰性方面。通过零-shot评估，发现这些模型的生成结果在这两个维度上均未达到理想水平，强调了针对法律领域的模型开发需求。

## 🎯 应用场景

该研究的潜在应用领域包括法律咨询、在线法律服务平台以及法律教育等。通过提供有效的法律索赔生成工具，能够帮助非专业人士更好地理解和表达自己的法律需求，提升法律服务的可及性和效率。未来，该研究可能推动法律技术的发展，促进法律服务的普及。

## 📄 摘要（原文）

> Legal claims refer to the plaintiff's demands in a case and are essential to guiding judicial reasoning and case resolution. While many works have focused on improving the efficiency of legal professionals, the research on helping non-professionals (e.g., plaintiffs) remains unexplored. This paper explores the problem of legal claim generation based on the given case's facts. First, we construct ClaimGen-CN, the first dataset for Chinese legal claim generation task, from various real-world legal disputes. Additionally, we design an evaluation metric tailored for assessing the generated claims, which encompasses two essential dimensions: factuality and clarity. Building on this, we conduct a comprehensive zero-shot evaluation of state-of-the-art general and legal-domain large language models. Our findings highlight the limitations of the current models in factual precision and expressive clarity, pointing to the need for more targeted development in this domain. To encourage further exploration of this important task, we will make the dataset publicly available.

