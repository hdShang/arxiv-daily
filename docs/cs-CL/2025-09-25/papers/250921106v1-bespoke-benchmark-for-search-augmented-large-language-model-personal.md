---
layout: default
title: "BESPOKE: Benchmark for Search-Augmented Large Language Model Personalization via Diagnostic Feedback"
---

# BESPOKE: Benchmark for Search-Augmented Large Language Model Personalization via Diagnostic Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21106" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21106v1</a>
  <a href="https://arxiv.org/pdf/2509.21106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21106v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21106v1', 'BESPOKE: Benchmark for Search-Augmented Large Language Model Personalization via Diagnostic Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyunseo Kim, Sangam Lee, Kwangwook Seo, Dongha Lee

**分类**: cs.CL, cs.IR

**发布日期**: 2025-09-25

**备注**: Work in progress

**🔗 代码/项目**: [PROJECT_PAGE](https://augustinlib.github.io/BESPOKE/)

---

## 💡 一句话要点

**提出BESPOKE基准，用于诊断反馈驱动的搜索增强LLM个性化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `搜索增强LLM` `个性化` `基准数据集` `诊断反馈` `信息检索`

## 📋 核心要点

1. 现有搜索增强LLM在个性化方面不足，无法充分理解不同用户相同查询背后的不同意图。
2. 提出BESPOKE基准，通过收集真实用户历史和偏好反馈，实现对个性化搜索增强LLM的诊断评估。
3. 通过BESPOKE基准的系统分析，揭示了信息检索任务中有效个性化的关键需求，为后续研究奠定基础。

## 📝 摘要（中文）

搜索增强的大型语言模型（LLMs）通过将检索集成到生成中，推进了信息检索任务，与传统的搜索系统相比，降低了用户的认知负担。然而，它们仍然不足以完全满足多样化的用户需求，这需要识别相同的查询如何在不同用户之间反映不同的意图，并以首选的形式传递信息。虽然像ChatGPT和Gemini这样的最新系统试图通过利用用户历史记录来实现个性化，但对此类个性化的系统评估仍未得到充分探索。为了解决这一差距，我们提出了BESPOKE，这是一个用于评估搜索增强LLM中个性化的真实基准。BESPOKE的设计既真实，通过直接从人类收集真实的聊天和搜索历史，又具有诊断性，通过将响应与细粒度的偏好分数和反馈配对。该基准是通过长期、深入的人工标注构建的，人工标注者贡献了自己的历史记录，撰写了带有详细信息需求的查询，并使用分数和诊断反馈评估了响应。利用BESPOKE，我们进行了系统分析，揭示了信息检索任务中有效个性化的关键要求，为个性化搜索增强LLM的细粒度评估奠定了基础。我们的代码和数据可在https://augustinlib.github.io/BESPOKE/上找到。

## 🔬 方法详解

**问题定义**：论文旨在解决搜索增强LLM在个性化信息检索任务中的不足。现有方法难以区分不同用户对相同查询的不同意图和偏好，导致无法提供真正个性化的搜索结果。缺乏一个能够真实反映用户行为和偏好的基准数据集，阻碍了对个性化搜索增强LLM的系统评估和改进。

**核心思路**：论文的核心思路是构建一个既真实又具有诊断性的基准数据集BESPOKE。通过收集真实用户的聊天和搜索历史，以及他们对搜索结果的细粒度偏好反馈，BESPOKE能够更准确地评估搜索增强LLM的个性化能力。这种诊断性的评估可以帮助研究人员识别模型在哪些方面表现良好，哪些方面需要改进。

**技术框架**：BESPOKE的构建流程主要包括以下几个阶段：1) 数据收集：招募人工标注者，贡献他们的聊天和搜索历史。2) 查询生成：标注者根据自身历史，撰写带有详细信息需求的查询。3) 响应生成：使用搜索增强LLM对查询生成响应。4) 偏好评估：标注者对响应进行评分，并提供诊断性反馈，指出响应的优点和不足。整个流程旨在模拟真实的用户搜索行为，并收集用户对搜索结果的细粒度偏好信息。

**关键创新**：BESPOKE的关键创新在于其真实性和诊断性。与以往的基准数据集相比，BESPOKE的数据来源于真实用户的历史记录，能够更准确地反映用户的实际需求和偏好。此外，BESPOKE还提供了细粒度的偏好分数和诊断性反馈，这使得研究人员能够更深入地了解模型的个性化能力，并有针对性地进行改进。

**关键设计**：BESPOKE的关键设计包括：1) 长期参与：标注者需要长期参与数据收集和评估过程，以确保数据的质量和一致性。2) 详细信息需求：标注者在撰写查询时，需要提供详细的信息需求，以便模型能够更好地理解用户的意图。3) 细粒度偏好评估：标注者需要对响应进行评分，并提供诊断性反馈，指出响应的优点和不足。这些设计旨在确保BESPOKE能够真实反映用户的搜索行为和偏好，并为个性化搜索增强LLM的评估提供有力的支持。

## 📊 实验亮点

论文构建了BESPOKE基准，包含真实的用户聊天和搜索历史，以及细粒度的偏好分数和诊断反馈。通过对现有搜索增强LLM的评估，揭示了模型在个性化方面的不足，并指出了有效个性化的关键要求。该基准为未来个性化搜索增强LLM的研究提供了重要的资源和评估工具。

## 🎯 应用场景

该研究成果可应用于个性化搜索引擎、智能助手、推荐系统等领域。通过利用用户历史和偏好反馈，可以提升搜索结果的相关性和用户满意度。未来，该研究可以推动搜索增强LLM在理解用户意图和提供个性化服务方面的进一步发展，从而改善用户的信息获取体验。

## 📄 摘要（原文）

> Search-augmented large language models (LLMs) have advanced information-seeking tasks by integrating retrieval into generation, reducing users' cognitive burden compared to traditional search systems. Yet they remain insufficient for fully addressing diverse user needs, which requires recognizing how the same query can reflect different intents across users and delivering information in preferred forms. While recent systems such as ChatGPT and Gemini attempt personalization by leveraging user histories, systematic evaluation of such personalization is under-explored. To address this gap, we propose BESPOKE, the realistic benchmark for evaluating personalization in search-augmented LLMs. BESPOKE is designed to be both realistic, by collecting authentic chat and search histories directly from humans, and diagnostic, by pairing responses with fine-grained preference scores and feedback. The benchmark is constructed through long-term, deeply engaged human annotation, where human annotators contributed their own histories, authored queries with detailed information needs, and evaluated responses with scores and diagnostic feedback. Leveraging BESPOKE, we conduct systematic analyses that reveal key requirements for effective personalization in information-seeking tasks, providing a foundation for fine-grained evaluation of personalized search-augmented LLMs. Our code and data are available at https://augustinlib.github.io/BESPOKE/.

