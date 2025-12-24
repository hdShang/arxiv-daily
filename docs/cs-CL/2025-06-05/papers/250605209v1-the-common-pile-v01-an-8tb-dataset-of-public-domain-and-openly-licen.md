---
layout: default
title: "The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text"
---

# The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05209" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05209v1</a>
  <a href="https://arxiv.org/pdf/2506.05209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05209v1', 'The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikhil Kandpal, Brian Lester, Colin Raffel, Sebastian Majstorovic, Stella Biderman, Baber Abbasi, Luca Soldaini, Enrico Shippole, A. Feder Cooper, Aviya Skowron, John Kirchenbauer, Shayne Longpre, Lintang Sutawika, Alon Albalak, Zhenlin Xu, Guilherme Penedo, Loubna Ben Allal, Elie Bakouch, John David Pressman, Honglu Fan, Dashiell Stander, Guangyu Song, Aaron Gokaslan, Tom Goldstein, Brian R. Bartoldson, Bhavya Kailkhura, Tyler Murray

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**发布Common Pile v0.1数据集以解决LLM训练中的版权问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `公开许可文本` `大型语言模型` `数据集构建` `知识产权` `自然语言处理` `模型训练`

## 📋 核心要点

1. 现有的LLM训练通常依赖未授权文本，导致知识产权和伦理问题，亟需解决。
2. 本文提出Common Pile v0.1数据集，包含8TB的公开许可文本，旨在为LLM训练提供高质量数据。
3. 实验结果表明，基于Common Pile训练的模型在性能上与未授权文本训练的模型相当，验证了数据集的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）通常在大量未授权文本上进行训练，这引发了知识产权和伦理问题的关注。基于公开许可文本训练LLMs是解决这些问题的第一步，但以往的数据收集工作往往导致数据集过小或质量低下，无法有效训练LLMs。为此，本文收集、整理并发布了Common Pile v0.1，这是一个8TB的公开许可文本集合，旨在为LLM预训练提供支持。Common Pile包含来自30个来源的内容，涵盖研究论文、代码、书籍、百科全书、教育材料、音频转录等多个领域。我们通过在Common Pile文本上训练两个70亿参数的LLMs（Comma v0.1-1T和Comma v0.1-2T）来验证我们的努力，结果显示这两个模型在性能上与在类似计算预算下训练的未授权文本的LLMs（如Llama 1和2 7B）具有竞争力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型训练中使用未授权文本带来的知识产权和伦理问题。现有方法往往依赖小规模或低质量的数据集，无法有效支持LLM的性能提升。

**核心思路**：通过收集和整理大量公开许可的文本数据，构建一个高质量的大型数据集Common Pile v0.1，为LLM的预训练提供支持。此举不仅解决了版权问题，还为研究者提供了丰富的训练资源。

**技术框架**：Common Pile v0.1的数据来源于30个不同领域，包括研究论文、代码、书籍等，确保了数据的多样性和覆盖面。训练过程中，使用了两个不同规模的模型（Comma v0.1-1T和Comma v0.1-2T），分别在1万亿和2万亿个token上进行训练。

**关键创新**：本研究的主要创新在于构建了一个8TB的高质量公开许可文本数据集，填补了以往数据集规模和质量不足的空白。通过在该数据集上训练的模型表现出与未授权文本训练模型相当的性能，证明了其有效性。

**关键设计**：在数据集构建过程中，注重数据的多样性和质量，确保涵盖多个领域的文本。同时，模型训练采用了先进的参数设置和优化策略，以提升训练效率和模型性能。具体的损失函数和网络结构设计也经过精心调整，以适应大规模数据的训练需求。

## 📊 实验亮点

实验结果显示，基于Common Pile v0.1训练的Comma v0.1-1T和Comma v0.1-2T模型在性能上与Llama 1和2 7B等未授权文本训练的模型相当，验证了数据集的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译、文本生成等。通过提供高质量的公开许可文本数据集，研究者和开发者可以在不侵犯知识产权的前提下，训练出更为强大的语言模型，从而推动相关技术的发展和应用。

## 📄 摘要（原文）

> Large language models (LLMs) are typically trained on enormous quantities of unlicensed text, a practice that has led to scrutiny due to possible intellectual property infringement and ethical concerns. Training LLMs on openly licensed text presents a first step towards addressing these issues, but prior data collection efforts have yielded datasets too small or low-quality to produce performant LLMs. To address this gap, we collect, curate, and release the Common Pile v0.1, an eight terabyte collection of openly licensed text designed for LLM pretraining. The Common Pile comprises content from 30 sources that span diverse domains including research papers, code, books, encyclopedias, educational materials, audio transcripts, and more. Crucially, we validate our efforts by training two 7 billion parameter LLMs on text from the Common Pile: Comma v0.1-1T and Comma v0.1-2T, trained on 1 and 2 trillion tokens respectively. Both models attain competitive performance to LLMs trained on unlicensed text with similar computational budgets, such as Llama 1 and 2 7B. In addition to releasing the Common Pile v0.1 itself, we also release the code used in its creation as well as the training mixture and checkpoints for the Comma v0.1 models.

