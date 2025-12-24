---
layout: default
title: "NOWJ@COLIEE 2025: A Multi-stage Framework Integrating Embedding Models and Large Language Models for Legal Retrieval and Entailment"
---

# NOWJ@COLIEE 2025: A Multi-stage Framework Integrating Embedding Models and Large Language Models for Legal Retrieval and Entailment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08025" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08025v1</a>
  <a href="https://arxiv.org/pdf/2509.08025.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08025v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08025v1', 'NOWJ@COLIEE 2025: A Multi-stage Framework Integrating Embedding Models and Large Language Models for Legal Retrieval and Entailment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hoang-Trung Nguyen, Tan-Minh Nguyen, Xuan-Bach Le, Tuan-Kiet Le, Khanh-Huyen Nguyen, Ha-Thanh Nguyen, Thi-Hai-Yen Vuong, Le-Minh Nguyen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**NOWJ团队提出多阶段框架，融合嵌入模型与大语言模型，用于法律检索和蕴含任务。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律检索` `案例蕴含` `大语言模型` `嵌入模型` `多阶段框架`

## 📋 核心要点

1. 现有法律信息处理方法在语义理解和上下文推理方面存在不足，难以准确判断案例之间的蕴含关系。
2. 论文提出一种多阶段框架，融合预排序模型、嵌入模型和大语言模型，实现更精确的法律检索和蕴含分析。
3. 在法律案例蕴含任务中，该方法取得第一名，F1值达到0.3195，证明了混合模型的有效性。

## 📝 摘要（中文）

本文介绍了NOWJ团队参与COLIEE 2025竞赛所有五个任务的方法和结果，重点介绍了法律案例蕴含任务（任务2）的进展。 我们的综合方法系统地集成了预排序模型（BM25、BERT、monoT5）、基于嵌入的语义表示（BGE-m3、LLM2Vec）和先进的大型语言模型（Qwen-2、QwQ-32B、DeepSeek-V3），用于摘要、相关性评分和上下文重排序。 特别是在任务2中，我们的两阶段检索系统将词汇语义过滤与上下文LLM分析相结合，以0.3195的F1分数获得第一名。 此外，在其他任务中——包括法律案例检索、法规检索、法律文本蕴含和法律判决预测——我们通过精心设计的集成和有效的基于提示的推理策略展示了强大的性能。 我们的研究结果突出了混合模型（将传统IR技术与当代生成模型相结合）的潜力，为法律信息处理的未来发展提供了有价值的参考。

## 🔬 方法详解

**问题定义**：论文旨在解决法律领域中案例检索和蕴含关系判断的问题。现有方法在处理复杂的法律文本时，难以准确捕捉语义信息和上下文关系，导致检索结果不准确，蕴含关系判断错误。

**核心思路**：论文的核心思路是将传统的信息检索技术（如BM25）与现代的深度学习模型（如BERT、大语言模型）相结合，利用各自的优势，实现更全面的语义理解和上下文推理。通过多阶段的处理流程，逐步提升检索和判断的准确性。

**技术框架**：该框架包含多个阶段：1) 预排序阶段：使用BM25、BERT等模型进行初步检索，筛选出候选案例；2) 嵌入表示阶段：利用BGE-m3、LLM2Vec等模型生成案例的语义嵌入表示；3) 大语言模型分析阶段：使用Qwen-2、QwQ-32B、DeepSeek-V3等大语言模型进行摘要、相关性评分和上下文重排序。对于法律案例蕴含任务，采用两阶段检索系统，首先进行词汇语义过滤，然后进行上下文LLM分析。

**关键创新**：该方法最重要的创新在于将传统的IR技术与先进的大语言模型相结合，形成一个混合模型。这种混合模型能够充分利用传统IR技术的效率和深度学习模型的语义理解能力，从而在法律信息处理任务中取得更好的效果。与现有方法相比，该方法能够更准确地捕捉法律文本的语义信息和上下文关系，提高检索和判断的准确性。

**关键设计**：在法律案例蕴含任务中，两阶段检索系统的设计是关键。第一阶段的词汇语义过滤可以快速筛选出相关案例，减少后续计算量。第二阶段的上下文LLM分析则可以对候选案例进行更深入的语义理解和上下文推理，从而提高判断的准确性。具体的参数设置和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

在COLIEE 2025法律案例蕴含任务（Task 2）中，NOWJ团队提出的方法以0.3195的F1分数获得第一名。该结果表明，融合嵌入模型和大语言模型的多阶段框架在法律信息处理任务中具有显著优势，能够有效提升检索和判断的准确性。

## 🎯 应用场景

该研究成果可应用于智能法律咨询、法律案例检索、法律文书自动生成等领域。通过提高法律信息处理的准确性和效率，可以帮助律师、法官和法律研究人员更高效地工作，并为普通民众提供更便捷的法律服务。未来，该方法有望应用于更广泛的法律人工智能领域。

## 📄 摘要（原文）

> This paper presents the methodologies and results of the NOWJ team's participation across all five tasks at the COLIEE 2025 competition, emphasizing advancements in the Legal Case Entailment task (Task 2). Our comprehensive approach systematically integrates pre-ranking models (BM25, BERT, monoT5), embedding-based semantic representations (BGE-m3, LLM2Vec), and advanced Large Language Models (Qwen-2, QwQ-32B, DeepSeek-V3) for summarization, relevance scoring, and contextual re-ranking. Specifically, in Task 2, our two-stage retrieval system combined lexical-semantic filtering with contextualized LLM analysis, achieving first place with an F1 score of 0.3195. Additionally, in other tasks--including Legal Case Retrieval, Statute Law Retrieval, Legal Textual Entailment, and Legal Judgment Prediction--we demonstrated robust performance through carefully engineered ensembles and effective prompt-based reasoning strategies. Our findings highlight the potential of hybrid models integrating traditional IR techniques with contemporary generative models, providing a valuable reference for future advancements in legal information processing.

