---
layout: default
title: "Spelling-out is not Straightforward: LLMs' Capability of Tokenization from Token to Characters"
---

# Spelling-out is not Straightforward: LLMs' Capability of Tokenization from Token to Characters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10641" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10641v1</a>
  <a href="https://arxiv.org/pdf/2506.10641.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10641v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10641v1', 'Spelling-out is not Straightforward: LLMs\' Capability of Tokenization from Token to Characters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tatsuya Hiraoka, Kentaro Inui

**分类**: cs.CL

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**揭示LLMs在字符拼写中的复杂性与内部表征**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `字符拼写` `Transformer` `知识表示` `自然语言处理`

## 📋 核心要点

1. 现有的LLMs在处理字符拼写时表现出色，但在识别标记的复杂组成部分时却存在明显不足。
2. 本研究通过分析LLMs的内部表征，揭示了其在拼写过程中对字符级信息的依赖及处理方式。
3. 实验结果显示，LLMs在中间和高层Transformer层的拼写行为中出现显著改善，验证了我们提出的机制。

## 📝 摘要（中文）

大型语言模型（LLMs）能够以高准确率逐字符拼写出标记，但在更复杂的字符级任务中，如识别标记内的组成子组件时却表现不佳。本研究探讨了LLMs在拼写过程中如何内部表示和利用字符级信息。分析表明，尽管拼写对人类而言是简单任务，但LLMs并未以直接方式处理此任务。具体而言，嵌入层未能充分编码字符级信息，尤其是超出第一个字符的部分。因此，LLMs依赖中间和更高层的Transformer层来重构字符级知识，并在拼写行为中观察到明显的“突破”。我们通过三种互补分析验证了这一机制：探测分类器、知识神经元识别和注意力权重检查。

## 🔬 方法详解

**问题定义**：本论文旨在解决LLMs在字符拼写过程中对字符级信息处理不充分的问题，现有方法在识别复杂标记组成部分时存在困难。

**核心思路**：通过分析LLMs的嵌入层和Transformer层，揭示其在拼写过程中如何重构字符级知识，强调中间层的重要性。

**技术框架**：研究采用了探测分类器、知识神经元识别和注意力权重检查三种分析方法，系统性地评估LLMs的拼写能力与内部机制。

**关键创新**：本研究的创新点在于揭示了嵌入层未能充分编码字符信息的现象，并指出中间层在拼写行为中的关键作用，与现有方法相比，提供了更深入的理解。

**关键设计**：研究中使用了多种探测分类器来分析模型的知识表示，并通过注意力权重的检查来识别影响拼写行为的关键神经元。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，LLMs在拼写任务中的表现显著提升，尤其是在中间层的拼写行为中观察到明显的“突破”。通过三种分析方法的验证，模型在字符级知识重构方面的能力得到了有效提升，具体性能数据和对比基线将在论文中详细列出。

## 🎯 应用场景

该研究为改进LLMs在字符级任务中的表现提供了理论基础，潜在应用包括自然语言处理中的拼写纠错、文本生成和信息提取等领域。通过优化模型的内部表征，未来可能提升LLMs在复杂语言任务中的整体性能。

## 📄 摘要（原文）

> Large language models (LLMs) can spell out tokens character by character with high accuracy, yet they struggle with more complex character-level tasks, such as identifying compositional subcomponents within tokens. In this work, we investigate how LLMs internally represent and utilize character-level information during the spelling-out process. Our analysis reveals that, although spelling out is a simple task for humans, it is not handled in a straightforward manner by LLMs. Specifically, we show that the embedding layer does not fully encode character-level information, particularly beyond the first character. As a result, LLMs rely on intermediate and higher Transformer layers to reconstruct character-level knowledge, where we observe a distinct "breakthrough" in their spelling behavior. We validate this mechanism through three complementary analyses: probing classifiers, identification of knowledge neurons, and inspection of attention weights.

