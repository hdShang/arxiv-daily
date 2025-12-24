---
layout: default
title: "LoRA Users Beware: A Few Spurious Tokens Can Manipulate Your Finetuned Model"
---

# LoRA Users Beware: A Few Spurious Tokens Can Manipulate Your Finetuned Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11402" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11402v2</a>
  <a href="https://arxiv.org/pdf/2506.11402.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11402v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11402v2', 'LoRA Users Beware: A Few Spurious Tokens Can Manipulate Your Finetuned Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marcel Mateos Salles, Praney Goyal, Pradyut Sekhsaria, Hai Huang, Randall Balestriero

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-13 (更新: 2025-10-01)

**备注**: 46 pages, 17 figures, 26 tables. Submitted for publication. for associated blog post, see https://pradyut3501.github.io/lora-spur-corr/

---

## 💡 一句话要点

**揭示LoRA模型在微调中易受短路攻击的脆弱性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩适应` `短路攻击` `虚假标记注入` `模型安全性` `数据质量` `大型语言模型` `微调技术`

## 📋 核心要点

1. LoRA微调方法在高效性上表现优异，但却引入了短路攻击的脆弱性，影响模型的安全性。
2. 提出无缝虚假标记注入（SSTI）方法，专注于单个与标签虚假相关的标记，以评估模型的脆弱性。
3. 实验结果显示，现有的数据清理工具无法有效防范虚假标记的影响，提出了新的数据质量和安全性问题。

## 📝 摘要（中文）

大型语言模型（LLMs）通常用于多种应用场景，并通过低秩适应（LoRA）进行微调，以实现高效的性能。然而，本研究表明，LoRA方法实际上引入了短路脆弱性，且越是资源高效的LoRA设置，微调模型越容易受到攻击。我们提出了无缝虚假标记注入（SSTI）方法，发现LoRA在微调过程中对与下游标签虚假相关的单个标记过于敏感。通过在微调期间注入这些虚假标记，可以在测试时按需操控模型的预测。实验结果表明，现有的数据检查和预处理工具无法有效清理数据集，从而引发了对数据质量和人工智能安全的新担忧。

## 🔬 方法详解

**问题定义**：本研究旨在解决LoRA微调模型在面对短路攻击时的脆弱性。现有方法在高效性上取得了成功，但却未能考虑到模型安全性的问题，导致模型易受攻击。

**核心思路**：论文提出的无缝虚假标记注入（SSTI）方法，专注于识别和利用与下游标签虚假相关的单个标记，从而评估和展示LoRA模型的脆弱性。通过这种方式，研究者能够揭示在微调过程中潜在的安全隐患。

**技术框架**：研究首先通过LoRA微调模型进行训练，然后在微调过程中注入虚假标记，最后评估模型在测试集上的表现。主要模块包括数据集准备、模型训练、虚假标记注入和性能评估。

**关键创新**：最重要的创新点在于识别出LoRA微调模型对虚假标记的敏感性，并通过SSTI方法展示了这一现象。与现有方法相比，该研究强调了微调过程中的数据质量问题及其对模型安全性的影响。

**关键设计**：在实验中，研究者设置了不同的虚假标记注入策略，并评估了其对模型性能的影响。损失函数和网络结构的设计也经过精心调整，以确保模型在面对虚假标记时的反应被准确捕捉。实验结果表明，现有的检查和预处理工具无法有效清理数据集，进一步验证了研究的假设。

## 📊 实验亮点

实验结果表明，在LoRA微调过程中，注入虚假标记后，模型的预测准确性显著下降，且现有的数据检查工具无法有效识别和清理这些虚假标记。这一发现强调了数据质量对模型安全性的关键影响，提出了新的研究方向。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和任何依赖于大型语言模型的应用。通过提高对微调模型脆弱性的认识，研究可以推动更安全的模型设计和数据处理方法，从而提升人工智能系统的整体安全性和可靠性。

## 📄 摘要（原文）

> Large Language Models (LLMs) are commonly finetuned for a variety of use cases and domains. A common approach is to leverage Low-Rank Adaptation (LoRA) -- known to provide strong performance at low resource costs. In this study, we demonstrate that LoRA actually opens the door to short-cut vulnerabilities -- and the more resource efficient is the LoRA setup, the more vulnerable will be the finetuned model to aggressive attacks. To measure that vulnerability, we introduce Seamless Spurious Token Injection (SSTI), where we find that LoRA exclusively focuses on even just a single token that is spuriously correlated with downstream labels. In short, injection of that spurious token during finetuning ensure that the model's prediction at test-time can be manipulated on-demand. We conducted experiments across model families and datasets to evaluate the impact of SSTI during LoRA finetuning while providing possible mitigations. Our experiments conclude that none of the existing checkers and preprocessors can sanitize a dataset raising new concerns for data quality and AI safety.

