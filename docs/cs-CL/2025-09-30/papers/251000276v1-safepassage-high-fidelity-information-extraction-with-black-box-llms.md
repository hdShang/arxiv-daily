---
layout: default
title: "SafePassage: High-Fidelity Information Extraction with Black Box LLMs"
---

# SafePassage: High-Fidelity Information Extraction with Black Box LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00276" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00276v1</a>
  <a href="https://arxiv.org/pdf/2510.00276.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00276v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00276v1', 'SafePassage: High-Fidelity Information Extraction with Black Box LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joe Barrow, Raj Patel, Misha Kharkovski, Ben Davies, Ryan Schmitt

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**SafePassage：利用黑盒LLM实现高保真信息抽取，显著降低幻觉。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息抽取` `大型语言模型` `幻觉检测` `安全通道` `文本对齐`

## 📋 核心要点

1. 现有黑盒LLM的信息抽取结果难以信任，存在幻觉问题，抽取的信息可能并非来源于文档。
2. SafePassage方法通过生成并验证“安全通道”，确保抽取信息的上下文既基于文档又与抽取内容一致。
3. 实验表明，SafePassage能显著降低LLM信息抽取中的幻觉，且微调的Transformer编码器可有效评估安全通道。

## 📝 摘要（中文）

黑盒大型语言模型（LLM）使得信息抽取（IE）易于配置，但难以信任。与传统信息抽取流程不同，从LLM中“抽取”的信息不能保证来源于文档本身。为了防止这种情况，本文提出了“安全通道”（safe passage）的概念：由LLM生成的上下文，既要基于文档，又要与抽取的信息保持一致。这通过一个三步流程SafePassage来实现，包括：（1）LLM抽取器，从文档中生成结构化实体及其上下文；（2）基于字符串的全局对齐器；（3）评分模型。结果表明，结合使用这三个部分，可以在信息抽取任务中减少高达85%的幻觉，同时将错误标记非幻觉的风险降到最低。SafePassage流程与人类对抽取质量的判断高度一致，这意味着该流程可以双重用于评估LLM。令人惊讶的是，结果还表明，使用在少量特定任务示例上微调的Transformer编码器，在标记不安全通道方面可以优于LLM评分模型。这些注释可以在短短1-2小时内收集完成。

## 🔬 方法详解

**问题定义**：论文旨在解决黑盒大型语言模型（LLM）在信息抽取任务中产生的幻觉问题。现有方法依赖于LLM直接抽取信息，无法保证抽取的信息来源于文档本身，导致结果不可信。这种缺乏可信度的信息抽取限制了LLM在需要高精度信息的应用场景中的使用。

**核心思路**：论文的核心思路是引入“安全通道”（SafePassage）的概念，即LLM在抽取信息的同时，生成一段上下文，该上下文既要基于原始文档，又要与抽取的信息保持一致。通过验证这段上下文的真实性和一致性，可以有效降低LLM产生幻觉的风险。

**技术框架**：SafePassage方法包含三个主要步骤：（1）**LLM抽取器**：利用LLM从文档中抽取结构化实体及其上下文。（2）**字符串全局对齐器**：将LLM生成的上下文与原始文档进行对齐，判断上下文是否真实存在于文档中。（3）**评分模型**：对对齐后的上下文进行评分，判断其与抽取的信息是否一致，从而评估“安全通道”的质量。

**关键创新**：SafePassage的关键创新在于引入了“安全通道”的概念，并将幻觉检测问题转化为对“安全通道”真实性和一致性的验证。与直接评估抽取结果的真实性相比，验证上下文的真实性和一致性更容易实现，也更可靠。此外，使用微调的Transformer编码器替代LLM进行安全通道评分，在降低成本的同时，提升了性能。

**关键设计**：在字符串全局对齐器中，使用了基于字符串匹配的算法，例如编辑距离或Jaccard相似度，来衡量LLM生成的上下文与原始文档之间的相似度。评分模型可以使用预训练的LLM进行微调，也可以使用更轻量级的Transformer编码器。论文强调了使用少量任务特定示例进行微调的重要性，这可以显著提升评分模型的性能。

## 📊 实验亮点

实验结果表明，SafePassage方法能够显著降低LLM在信息抽取任务中的幻觉，最高可达85%。更令人惊讶的是，在少量任务特定示例上微调的Transformer编码器，在标记不安全通道方面，性能优于直接使用LLM进行评分。这表明，在某些情况下，轻量级模型可以通过针对性训练，超越大型LLM的性能。

## 🎯 应用场景

SafePassage可应用于需要高精度信息抽取的各种场景，例如金融报告分析、医学文献挖掘、法律文件审核等。通过降低LLM的幻觉，提高信息抽取的可靠性，SafePassage可以帮助用户更有效地利用LLM处理大量文本数据，辅助决策，提高工作效率。该方法还有助于评估不同LLM在信息抽取任务中的性能，为LLM的选型提供参考。

## 📄 摘要（原文）

> Black box large language models (LLMs) make information extraction (IE) easy to configure, but hard to trust. Unlike traditional information extraction pipelines, the information "extracted" is not guaranteed to be grounded in the document. To prevent this, this paper introduces the notion of a "safe passage": context generated by the LLM that is both grounded in the document and consistent with the extracted information. This is operationalized via a three-step pipeline, SafePassage, which consists of: (1) an LLM extractor that generates structured entities and their contexts from a document, (2) a string-based global aligner, and (3) a scoring model. Results show that using these three parts in conjunction reduces hallucinations by up to 85% on information extraction tasks with minimal risk of flagging non-hallucinations. High agreement between the SafePassage pipeline and human judgments of extraction quality mean that the pipeline can be dually used to evaluate LLMs. Surprisingly, results also show that using a transformer encoder fine-tuned on a small number of task-specific examples can outperform an LLM scoring model at flagging unsafe passages. These annotations can be collected in as little as 1-2 hours.

