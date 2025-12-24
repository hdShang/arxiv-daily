---
layout: default
title: "Fact Grounded Attention: Eliminating Hallucination in Large Language Models Through Attention Level Knowledge Integration"
---

# Fact Grounded Attention: Eliminating Hallucination in Large Language Models Through Attention Level Knowledge Integration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25252" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25252v2</a>
  <a href="https://arxiv.org/pdf/2509.25252.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25252v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25252v2', 'Fact Grounded Attention: Eliminating Hallucination in Large Language Models Through Attention Level Knowledge Integration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aayush Gupta

**分类**: cs.AI

**发布日期**: 2025-09-27 (更新: 2025-10-02)

**备注**: 15 pages, 3 figures, 4 tables. Code and dataset available at https://github.com/ayushgupta4897/FGA

---

## 💡 一句话要点

**提出Fact Grounded Attention，通过知识注入注意力机制消除大语言模型的事实幻觉。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `事实幻觉` `注意力机制` `知识注入` `可信AI`

## 📋 核心要点

1. 现有大语言模型存在事实幻觉问题，即使在已知知识范围内也会自信地生成错误信息。
2. FGA通过将可验证知识直接注入到Transformer的注意力机制中，从根本上避免模型产生与知识库冲突的幻觉。
3. 实验表明，FGA在技术查询任务中显著提高了准确率，并且知识更新速度极快，无需耗时重新训练。

## 📝 摘要（中文）

大型语言模型（LLM）在自然语言处理领域取得了显著进展，但仍然存在自信地产生虚假事实的问题。本文提出了一种新颖的架构修改方法，名为Fact Grounded Attention (FGA)，通过将可验证的知识直接注入到注意力机制中，将不可靠的语言模型转变为确定性的事实陈述者。与现有在生成后修补幻觉或预先添加检索文本的方法不同，FGA直接干预Transformer的核心——pre-softmax注意力分数，从而创建一个在知识库中存在事实时不会产生幻觉的模型。在涵盖智能手机、笔记本电脑和电动汽车的1107个技术查询上的实验表明，FGA将Llama 3.2的准确率从6.3%提高到99.7%。更重要的是，知识更新在不到一秒的时间内完成，无需重新训练，而参数编辑方法则需要数小时。FGA不仅减少了幻觉，而且完全消除了可验证事实的幻觉，标志着神经语言生成从概率近似到确定性精度的根本转变。

## 🔬 方法详解

**问题定义**：大语言模型在生成文本时，经常会产生与事实不符的内容，即“幻觉”现象。现有的解决幻觉的方法，例如后处理修正或前置检索增强，要么效率较低，要么无法从根本上解决问题。这些方法无法保证模型在生成过程中始终遵循事实。

**核心思路**：FGA的核心思路是在Transformer的注意力机制中直接注入外部知识，使得模型在计算注意力权重时，能够考虑到知识库中的事实信息。通过这种方式，模型在生成文本时，会受到事实的约束，从而避免产生幻觉。

**技术框架**：FGA在Transformer的注意力层中引入了知识融合模块。该模块首先从知识库中检索与输入相关的的事实信息，然后将这些事实信息编码成向量表示。接下来，将这些向量表示与原始的注意力权重进行融合，从而得到新的、受事实约束的注意力权重。最后，使用这些新的注意力权重来计算上下文向量，并生成最终的文本。

**关键创新**：FGA最重要的创新点在于它直接在注意力机制层面进行知识融合，而不是在生成后进行修正或在生成前进行增强。这种方法能够从根本上避免模型产生与知识库冲突的幻觉，从而提高生成文本的准确性和可靠性。

**关键设计**：FGA的关键设计包括：1) 如何从知识库中高效地检索相关的事实信息；2) 如何将这些事实信息编码成向量表示；3) 如何将这些向量表示与原始的注意力权重进行融合。论文中可能详细描述了检索策略、编码方式和融合函数等具体实现细节，但具体参数设置和损失函数等细节未知。

## 📊 实验亮点

实验结果表明，FGA在1107个技术查询任务中，将Llama 3.2的准确率从6.3%大幅提升至99.7%。更重要的是，FGA的知识更新速度非常快，可以在不到一秒的时间内完成，而传统的参数编辑方法则需要数小时。这表明FGA具有很高的效率和实用性。

## 🎯 应用场景

FGA具有广泛的应用前景，例如可以应用于智能客服、问答系统、内容生成等领域。通过消除大语言模型的事实幻觉，FGA可以提高这些应用的可靠性和用户体验。此外，FGA还可以用于构建更加可信赖的AI系统，从而促进人工智能技术在各个领域的应用。

## 📄 摘要（原文）

> "The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge." Large Language Models have conquered natural language but remain prisoners of their own probabilistic nature--confidently hallucinating facts they never truly knew. We present Fact Grounded Attention (FGA), a novel architectural modification that transforms unreliable language models into deterministic truth tellers by injecting verifiable knowledge directly into the attention mechanism. Unlike existing approaches that patch hallucinations after generation or prepend retrieved text, FGA intervenes at the mathematical heart of the transformer--the pre-softmax attention scores--creating a model that cannot hallucinate when facts exist in its knowledge base. Our experiments across 1,107 technical queries spanning smartphones, laptops, and electric vehicles demonstrate a transformation from 6.3% accuracy in vanilla Llama 3.2 to 99.7% accuracy with FGA. More critically, knowledge updates occur in under one second without retraining, compared to hours for parameter editing approaches. FGA doesn't just reduce hallucination--it eliminates it entirely for verifiable facts, marking a fundamental shift from probabilistic approximation to deterministic precision in neural language generation.

