---
layout: default
title: "FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models"
---

# FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21563" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21563v1</a>
  <a href="https://arxiv.org/pdf/2506.21563.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21563v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21563v1', 'FormosanBench: Benchmarking Low-Resource Austronesian Languages in the Era of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiying Kevin Lin, Hsiyu Chen, Haopeng Zhang

**分类**: cs.CL

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出FORMOSANBENCH以评估低资源南岛语言的LLM表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源语言` `南岛语言` `大型语言模型` `自然语言处理` `语言评估` `机器翻译` `自动语音识别` `文本摘要`

## 📋 核心要点

1. 现有大型语言模型在低资源和少数语言的表现显著不足，尤其是在福尔摩沙语言中。
2. 本文提出FORMOSANBENCH基准，专门用于评估低资源南岛语言的LLM性能，涵盖多项NLP任务。
3. 实验结果显示，现有LLMs在福尔摩沙语言上的表现普遍较差，强调了对包容性NLP技术的需求。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在高资源语言的自然语言处理任务中表现出色，但在低资源和少数语言中的能力仍未得到充分探索。本文介绍了FORMOSANBENCH，这是第一个用于评估低资源南岛语言的基准，涵盖了三种濒危的福尔摩沙语言：阿美语、排湾语和泰雅语，涉及机器翻译、自动语音识别和文本摘要等三项核心NLP任务。通过零样本、10样本和微调设置评估模型性能，结果显示高资源语言与福尔摩沙语言之间存在显著的性能差距，现有LLMs在所有任务中表现不佳，10样本学习和微调仅提供有限改进。这些发现强调了开发更具包容性的NLP技术以有效支持濒危和被忽视语言的紧迫性。我们发布了数据集和代码，以促进未来的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在低资源南岛语言（如福尔摩沙语言）中的评估问题。现有方法在这些语言上表现不佳，缺乏有效的基准和评估工具。

**核心思路**：提出FORMOSANBENCH基准，通过涵盖多种NLP任务，系统性地评估LLMs在低资源语言上的表现，旨在填补这一研究空白。

**技术框架**：FORMOSANBENCH包括三个主要模块：机器翻译、自动语音识别（ASR）和文本摘要，针对三种福尔摩沙语言进行评估，采用零样本、10样本和微调三种设置。

**关键创新**：FORMOSANBENCH是首个专门针对低资源南岛语言的评估基准，填补了现有LLMs评估的空白，强调了对濒危语言的关注。

**关键设计**：在实验中，使用了多种评估指标来衡量模型性能，特别关注在不同样本设置下的表现差异，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，现有LLMs在福尔摩沙语言的所有任务中均表现不佳，尤其是在机器翻译和文本摘要任务中，性能差距显著。10样本学习和微调仅带来有限的性能提升，进一步验证了对低资源语言技术支持的迫切需求。

## 🎯 应用场景

该研究的潜在应用领域包括语言保护、教育和文化传承等。通过提升对福尔摩沙语言的支持，能够促进这些濒危语言的复兴和使用，推动多样性和包容性的发展。未来，FORMOSANBENCH可作为其他低资源语言评估的参考框架，推动相关技术的进步。

## 📄 摘要（原文）

> While large language models (LLMs) have demonstrated impressive performance across a wide range of natural language processing (NLP) tasks in high-resource languages, their capabilities in low-resource and minority languages remain significantly underexplored. Formosan languages -- a subgroup of Austronesian languages spoken in Taiwan -- are both linguistically rich and endangered, largely due to the sociolinguistic dominance of Mandarin. In this work, we introduce FORMOSANBENCH, the first benchmark for evaluating LLMs on low-resource Austronesian languages. It covers three endangered Formosan languages: Atayal, Amis, and Paiwan, across three core NLP tasks: machine translation, automatic speech recognition (ASR), and text summarization. We assess model performance in zero-shot, 10-shot, and fine-tuned settings using FORMOSANBENCH. Our results reveal a substantial performance gap between high-resource and Formosan languages. Existing LLMs consistently underperform across all tasks, with 10-shot learning and fine-tuning offering only limited improvements. These findings underscore the urgent need for more inclusive NLP technologies that can effectively support endangered and underrepresented languages. We release our datasets and code to facilitate future research in this direction.

