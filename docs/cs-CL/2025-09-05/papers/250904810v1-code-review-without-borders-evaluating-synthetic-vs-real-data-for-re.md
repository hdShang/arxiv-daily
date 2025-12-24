---
layout: default
title: "Code Review Without Borders: Evaluating Synthetic vs. Real Data for Review Recommendation"
---

# Code Review Without Borders: Evaluating Synthetic vs. Real Data for Review Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04810" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04810v1</a>
  <a href="https://arxiv.org/pdf/2509.04810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04810v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04810v1', 'Code Review Without Borders: Evaluating Synthetic vs. Real Data for Review Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yogev Cohen, Dudi Ohayon, Romy Somkin, Yehudit Aperstein, Alexander Apartsin

**分类**: cs.SE, cs.CL, cs.LG

**发布日期**: 2025-09-05

**备注**: 4 pages, 1 figure

---

## 💡 一句话要点

**利用LLM生成合成数据，解决新兴语言代码审查推荐系统训练数据不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码审查` `代码推荐` `大型语言模型` `合成数据` `低资源学习`

## 📋 核心要点

1. 现有代码审查推荐系统在新兴语言中面临标注数据稀缺的挑战，阻碍了其应用。
2. 利用大型语言模型将资源丰富的语言的代码变更翻译为新兴语言的等效变更，生成合成训练数据。
3. 实验表明，使用LLM生成的合成数据训练的模型，能够有效提升新兴语言的代码审查推荐性能。

## 📝 摘要（中文）

在现代软件开发流程中，自动判断代码变更是否需要人工审查至关重要。然而，新兴编程语言和框架的出现带来了一个关键瓶颈：虽然大量未标记的代码唾手可得，但用于训练有监督的审查分类模型的已标记数据却不足。为了解决这个问题，我们利用大型语言模型（LLM）将来自资源丰富的语言的代码变更翻译成代表性不足或新兴语言中的等效变更，从而在标记示例稀缺的情况下生成合成训练数据。我们假设，虽然LLM已经从可用的未标记代码中学习了新语言的语法和语义，但它们尚未完全掌握哪些代码变更在新兴生态系统中被认为是重要的或值得审查的。为了克服这一点，我们使用LLM生成合成变更示例，并用它们训练有监督的分类器。我们系统地将这些分类器的性能与在真实标记数据上训练的模型进行了比较。我们在多个GitHub存储库和语言对上的实验表明，LLM生成的合成数据可以有效地引导审查推荐系统，即使在低资源环境中也能缩小性能差距。这种方法为将自动代码审查能力扩展到快速发展的技术堆栈提供了一条可扩展的途径，即使在没有注释数据的情况下也是如此。

## 🔬 方法详解

**问题定义**：论文旨在解决新兴编程语言和框架中，由于缺乏足够的标注数据，导致无法有效训练代码审查推荐系统的问题。现有方法依赖于大量标注数据，但在新兴语言中，获取这些数据成本高昂且耗时，限制了自动化代码审查的推广应用。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的跨语言代码理解和生成能力，将已有的、资源丰富的语言的代码变更翻译成新兴语言的等效变更，从而生成合成的训练数据。这种方法避免了人工标注的成本，并能够快速生成大量训练数据。

**技术框架**：整体框架包含以下几个主要阶段：1) 选择资源丰富的源语言和资源匮乏的目标语言；2) 从源语言的代码仓库中提取代码变更；3) 使用LLM将源语言的代码变更翻译成目标语言的等效变更，生成合成数据；4) 使用合成数据训练代码审查分类器；5) 在真实的目标语言数据集上评估分类器的性能。

**关键创新**：论文的关键创新在于利用LLM进行跨语言的代码变更翻译，从而生成用于训练代码审查推荐系统的合成数据。与以往依赖人工标注或简单数据增强的方法相比，该方法能够更有效地利用LLM的语义理解能力，生成更具代表性的训练数据。

**关键设计**：论文中，LLM的选择和使用是关键。具体来说，需要选择具有较强跨语言代码理解和生成能力的LLM，例如基于Transformer的模型。此外，如何设计合适的prompt，引导LLM生成高质量的合成数据也是一个重要的技术细节。论文可能还涉及了对合成数据进行过滤和清洗，以提高训练数据的质量。

## 📊 实验亮点

实验结果表明，使用LLM生成的合成数据训练的代码审查分类器，在多个GitHub仓库和语言对上取得了显著的性能提升。即使在低资源环境下，该方法也能有效缩小与使用真实标注数据训练的模型之间的性能差距，证明了LLM生成合成数据在代码审查推荐系统中的有效性。具体的性能数据和提升幅度在论文正文中给出。

## 🎯 应用场景

该研究成果可应用于各种新兴编程语言和框架的代码审查自动化，提高软件开发效率和质量。通过降低对标注数据的依赖，可以加速自动化代码审查技术在新兴技术栈中的普及，并支持更快速的软件迭代和创新。此外，该方法还可扩展到其他低资源场景，例如自然语言处理中的低资源语言翻译。

## 📄 摘要（原文）

> Automating the decision of whether a code change requires manual review is vital for maintaining software quality in modern development workflows. However, the emergence of new programming languages and frameworks creates a critical bottleneck: while large volumes of unlabelled code are readily available, there is an insufficient amount of labelled data to train supervised models for review classification. We address this challenge by leveraging Large Language Models (LLMs) to translate code changes from well-resourced languages into equivalent changes in underrepresented or emerging languages, generating synthetic training data where labelled examples are scarce. We assume that although LLMs have learned the syntax and semantics of new languages from available unlabelled code, they have yet to fully grasp which code changes are considered significant or review-worthy within these emerging ecosystems. To overcome this, we use LLMs to generate synthetic change examples and train supervised classifiers on them. We systematically compare the performance of these classifiers against models trained on real labelled data. Our experiments across multiple GitHub repositories and language pairs demonstrate that LLM-generated synthetic data can effectively bootstrap review recommendation systems, narrowing the performance gap even in low-resource settings. This approach provides a scalable pathway to extend automated code review capabilities to rapidly evolving technology stacks, even in the absence of annotated data.

