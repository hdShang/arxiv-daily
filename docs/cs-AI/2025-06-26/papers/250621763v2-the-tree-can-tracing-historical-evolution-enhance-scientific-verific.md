---
layout: default
title: "THE-Tree: Can Tracing Historical Evolution Enhance Scientific Verification and Reasoning?"
---

# THE-Tree: Can Tracing Historical Evolution Enhance Scientific Verification and Reasoning?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21763" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21763v2</a>
  <a href="https://arxiv.org/pdf/2506.21763.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21763v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21763v2', 'THE-Tree: Can Tracing Historical Evolution Enhance Scientific Verification and Reasoning?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Wang, Jiyao Liu, Yulong Xiao, Junzhi Ning, Lihao Liu, Junjun He, Botian Shi, Kaicheng Yu

**分类**: cs.AI

**发布日期**: 2025-06-26 (更新: 2025-07-21)

---

## 💡 一句话要点

**提出THE-Tree以解决科学验证与推理中的历史演化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `科学验证` `演化树` `大型语言模型` `数据结构` `知识管理` `自然语言推理` `图完成` `科学研究`

## 📋 核心要点

1. 现有的验证方法在评估AI生成科学提案的准确性和新颖性方面存在显著不足，手动验证速度慢且效率低下。
2. 论文提出了THE-Tree框架，通过构建领域特定的演化树，利用LLM进行科学进展的提议和验证，解决了历史数据缺乏的问题。
3. 实验结果表明，THE-Tree在图完成任务中提升了8%至14%的hit@1指标，并在预测未来科学发展方面提升了近10%。

## 📝 摘要（中文）

大型语言模型（LLMs）正在加速科学创意的生成，但对这些AI生成的提案进行严格评估以确保其新颖性和事实准确性是一个关键瓶颈，手动验证速度过慢。现有的验证方法不足：LLMs作为独立验证者可能会产生幻觉并缺乏领域知识，而传统的引用网络缺乏明确的因果关系，叙述性调查则结构不清晰。这突显了一个核心挑战：缺乏结构化、可验证和因果关联的科学演化历史数据。为此，我们提出了THE-Tree（技术历史演化树），一个从科学文献中构建领域特定演化树的计算框架。THE-Tree采用搜索算法探索演化路径，并在节点扩展过程中利用一种新颖的“思考-表达-引用-验证”过程，确保每一步都有逻辑一致性和证据支持。我们构建并验证了88个THE-Trees，并发布了一个包含71k事实验证的基准数据集，以促进进一步研究。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何有效验证AI生成的科学提案的准确性和新颖性。现有方法如LLMs和传统引用网络存在幻觉、缺乏领域知识和因果关系不明确等痛点。

**核心思路**：论文的核心思路是构建THE-Tree框架，通过从科学文献中提取结构化的演化历史数据，利用LLM进行科学进展的提议和验证，以确保每一步都有逻辑和证据支持。

**技术框架**：整体架构包括数据收集、演化树构建、节点扩展和验证四个主要模块。首先，通过文献检索构建演化树，然后在节点扩展过程中使用“思考-表达-引用-验证”流程进行科学提案和验证。

**关键创新**：最重要的技术创新点在于引入了“思考-表达-引用-验证”过程，使得每个提议的演化链接都经过逻辑一致性和证据支持的验证，这与现有方法的独立验证机制形成了鲜明对比。

**关键设计**：在关键设计上，THE-Tree使用了特定的搜索算法来探索演化路径，并结合自然语言推理机制来验证引用文献的有效性，确保每一步的科学性和准确性。

## 📊 实验亮点

实验结果显示，THE-Tree在图完成任务中相比传统引用网络提升了8%至14%的hit@1指标，在预测未来科学发展方面提升了近10%。此外，结合其他方法时，THE-Tree在评估重要科学论文的性能上提升近100%。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究、学术出版和知识管理等。通过提供一个结构化的历史演化数据框架，THE-Tree能够帮助研究人员更有效地验证和推理科学提案，从而加速科学发现的过程，提升研究的质量和效率。

## 📄 摘要（原文）

> Large Language Models (LLMs) are accelerating scientific idea generation, but rigorously evaluating these numerous, often superficial, AI-generated propositions for novelty and factual accuracy is a critical bottleneck; manual verification is too slow. Existing validation methods are inadequate: LLMs as standalone verifiers may hallucinate and lack domain knowledge (our findings show 60% unawareness of relevant papers in specific domains), while traditional citation networks lack explicit causality and narrative surveys are unstructured. This underscores a core challenge: the absence of structured, verifiable, and causally-linked historical data of scientific evolution.To address this,we introduce \textbf{THE-Tree} (\textbf{T}echnology \textbf{H}istory \textbf{E}volution Tree), a computational framework that constructs such domain-specific evolution trees from scientific literature. THE-Tree employs a search algorithm to explore evolutionary paths. During its node expansion, it utilizes a novel "Think-Verbalize-Cite-Verify" process: an LLM proposes potential advancements and cites supporting literature. Critically, each proposed evolutionary link is then validated for logical coherence and evidential support by a recovered natural language inference mechanism that interrogates the cited literature, ensuring that each step is grounded. We construct and validate 88 THE-Trees across diverse domains and release a benchmark dataset including up to 71k fact verifications covering 27k papers to foster further research. Experiments demonstrate that i) in graph completion, our THE-Tree improves hit@1 by 8% to 14% across multiple models compared to traditional citation networks; ii) for predicting future scientific developments, it improves hit@1 metric by nearly 10%; and iii) when combined with other methods, it boosts the performance of evaluating important scientific papers by almost 100%.

