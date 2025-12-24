---
layout: default
title: "GEM: Empowering LLM for both Embedding Generation and Language Understanding"
---

# GEM: Empowering LLM for both Embedding Generation and Language Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04344" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04344v1</a>
  <a href="https://arxiv.org/pdf/2506.04344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04344v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04344v1', 'GEM: Empowering LLM for both Embedding Generation and Language Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Caojin Zhang, Qiang Zhang, Ke Li, Sai Vidyaranya Nuthalapati, Benyu Zhang, Jason Liu, Serena Li, Lizhu Zhang, Xiangjun Fan

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出GEM以解决LLM嵌入生成与语言理解的矛盾问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `嵌入生成` `自监督学习` `文本生成` `自然语言处理` `检索增强生成`

## 📋 核心要点

1. 现有的LLM在生成和推理任务中表现优异，但在嵌入生成方面仍依赖于独立模型，导致系统复杂性和理解差异。
2. 本文提出GEM方法，通过自监督学习使LLM能够生成高质量文本嵌入，保持其生成和推理能力。
3. 实验表明，GEM在MTEB基准上显著提升了LLM的性能，而对MMLU的影响微乎其微，展示了其有效性。

## 📝 摘要（中文）

大型解码器语言模型（LLMs）在生成和推理任务中取得了显著成功，但许多应用（如检索增强生成）仍依赖于单独的嵌入模型，这导致系统复杂性增加，并可能在查询理解上产生差异。为了解决这一问题，本文提出了一种简单的自监督方法——生成嵌入大型语言模型（GEM），使任何大型解码器LLM能够生成高质量的文本嵌入，同时保持其原有的文本生成和推理能力。该方法通过在文本中插入新的特殊标记，并操控注意力掩码生成文本的摘要嵌入，能够轻松集成到现有LLMs的后训练或微调阶段。实验结果表明，该方法在文本嵌入基准（MTEB）上显著提升了原有LLMs的性能，同时对自然语言处理基准（MMLU）的影响最小。

## 🔬 方法详解

**问题定义**：本文旨在解决大型解码器语言模型在文本嵌入生成中的局限性，现有方法通常依赖于独立的嵌入模型，导致系统复杂且可能产生理解上的不一致。

**核心思路**：GEM方法通过在文本中插入特殊标记并操控注意力掩码，使LLM能够自生成高质量的文本嵌入，从而消除对独立嵌入模型的依赖。

**技术框架**：GEM的整体架构包括两个主要阶段：首先，在文本中插入特殊标记；其次，通过调整注意力掩码生成文本的摘要嵌入。该方法可以无缝集成到现有LLMs的后训练或微调过程中。

**关键创新**：GEM的核心创新在于将嵌入生成与文本生成能力结合，使得LLM不仅能生成文本，还能有效地生成其嵌入表示，这与传统方法截然不同。

**关键设计**：在实现过程中，GEM采用了特定的损失函数来优化嵌入质量，同时在网络结构上进行了适当的调整，以确保生成的嵌入与文本生成能力的兼容性。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，GEM在文本嵌入基准（MTEB）上显著提升了原有LLMs的性能，具体提升幅度达到XX%（具体数据需参考原文），而对自然语言处理基准（MMLU）的影响则保持在最小范围内，证明了其有效性和实用性。

## 🎯 应用场景

GEM方法的潜在应用领域包括检索增强生成、对话系统和信息检索等。通过将嵌入生成与语言理解能力结合，GEM能够提升系统的整体性能，简化架构，降低复杂性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large decoder-only language models (LLMs) have achieved remarkable success in generation and reasoning tasks, where they generate text responses given instructions. However, many applications, e.g., retrieval augmented generation (RAG), still rely on separate embedding models to generate text embeddings, which can complicate the system and introduce discrepancies in understanding of the query between the embedding model and LLMs. To address this limitation, we propose a simple self-supervised approach, Generative Embedding large language Model (GEM), that enables any large decoder-only LLM to generate high-quality text embeddings while maintaining its original text generation and reasoning capabilities. Our method inserts new special token(s) into a text body, and generates summarization embedding of the text by manipulating the attention mask. This method could be easily integrated into post-training or fine tuning stages of any existing LLMs. We demonstrate the effectiveness of our approach by applying it to two popular LLM families, ranging from 1B to 8B parameters, and evaluating the transformed models on both text embedding benchmarks (MTEB) and NLP benchmarks (MMLU). The results show that our proposed method significantly improves the original LLMs on MTEB while having a minimal impact on MMLU. Our strong results indicate that our approach can empower LLMs with state-of-the-art text embedding capabilities while maintaining their original NLP performance

