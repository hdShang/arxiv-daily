---
layout: default
title: Retrieval-augmented Prompt Learning for Pre-trained Foundation Models
---

# Retrieval-augmented Prompt Learning for Pre-trained Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20145" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20145v1</a>
  <a href="https://arxiv.org/pdf/2512.20145.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20145v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20145v1', 'Retrieval-augmented Prompt Learning for Pre-trained Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiang Chen, Yixin Ou, Quan Feng, Lei Li, Piji Li, Haibo Ye, Sheng-Jun Huang, Shuofei Qiao, Shumin Deng, Huajun Chen, Ningyu Zhang

**分类**: cs.CL, cs.AI, cs.CV, cs.IR, cs.LG

**发布日期**: 2025-12-23

**备注**: IEEE/ACM Transactions on Audio, Speech and Language Processing

**DOI**: [10.1109/TASLPRO.2025.3608936](https://doi.org/10.1109/TASLPRO.2025.3608936)

---

## 💡 一句话要点

**提出RetroPrompt，通过检索增强提示学习提升预训练模型泛化能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强学习` `提示学习` `预训练模型` `少样本学习` `知识库` `泛化能力` `自然语言处理` `计算机视觉`

## 📋 核心要点

1. 传统提示学习方法在预训练模型中存在过度依赖记忆、泛化能力不足的问题，尤其是在数据量有限的情况下。
2. RetroPrompt的核心思想是解耦知识与记忆，通过检索增强的方式，使模型能够利用外部知识库提升泛化能力。
3. 实验结果表明，RetroPrompt在零样本和少样本场景下，在NLP和CV任务上均表现出优越的性能，并有效减少了对死记硬背的依赖。

## 📝 摘要（中文）

预训练基础模型(PFMs)已成为促进大规模多模态学习的关键。研究人员通过提示学习有效地采用了“预训练、提示和预测”范式，以提高少样本性能。然而，PFM的提示学习方法仍然遵循参数学习范式，这可能会损害记忆和死记硬背的泛化稳定性。更具体地说，传统的提示学习可能难以充分利用非典型实例，并避免在完全监督训练过程中过度拟合有限数据的浅层模式。为了克服这些限制，我们提出了RetroPrompt方法，旨在通过将知识与单纯的记忆分离来实现记忆和泛化之间的平衡。与传统的提示方法不同，RetroPrompt利用从训练数据生成的公开知识库，并在输入、训练和推理阶段结合检索机制。这使得模型能够主动从语料库中检索相关的上下文信息，从而增强可用的线索。我们在自然语言处理和计算机视觉任务的各种数据集上进行了全面的实验，以证明我们提出的方法RetroPrompt在零样本和少样本场景中的优越性能。通过对记忆模式的详细分析，我们观察到RetroPrompt有效地减少了对死记硬背的依赖，从而增强了泛化能力。

## 🔬 方法详解

**问题定义**：现有预训练模型中的提示学习方法，过度依赖参数记忆，容易过拟合训练数据中的浅层模式，尤其是在少样本场景下，泛化能力受限。模型难以充分利用非典型实例，导致性能下降。

**核心思路**：RetroPrompt的核心思路是通过引入检索增强机制，将知识与单纯的记忆解耦。模型不再仅仅依赖自身参数记忆，而是能够从外部知识库中检索相关信息，从而增强上下文线索，提升泛化能力。这种方法旨在平衡记忆和泛化，使模型能够更好地适应新的、未见过的数据。

**技术框架**：RetroPrompt的整体框架包含以下几个主要阶段：1) **知识库构建**：利用训练数据构建一个公开可访问的知识库。2) **检索模块**：在输入、训练和推理阶段，模型使用检索模块从知识库中检索相关的上下文信息。3) **提示学习**：将检索到的信息融入到提示中，引导模型进行预测。整个流程旨在利用外部知识来增强模型的理解和推理能力。

**关键创新**：RetroPrompt的关键创新在于将检索机制融入到提示学习中，实现了知识与记忆的解耦。与传统的提示学习方法不同，RetroPrompt不再仅仅依赖模型自身的参数记忆，而是能够主动从外部知识库中检索相关信息，从而增强上下文线索，提升泛化能力。这种方法有效地减少了对死记硬背的依赖，使模型能够更好地适应新的、未见过的数据。

**关键设计**：RetroPrompt的关键设计包括：1) **知识库的构建方式**：知识库的构建方式会影响检索的效率和质量。论文可能采用了特定的数据结构或索引方法来优化知识库。2) **检索模块的设计**：检索模块需要能够准确地找到与输入相关的上下文信息。论文可能采用了特定的相似度度量方法或检索算法。3) **提示融合方式**：如何将检索到的信息有效地融入到提示中，也是一个关键的设计点。论文可能采用了特定的融合策略，例如注意力机制或拼接操作。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20145v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20145v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20145v1/figs/cv_results.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

RetroPrompt在多个NLP和CV数据集上进行了实验，结果表明其在零样本和少样本场景下均优于现有方法。通过对记忆模式的分析，发现RetroPrompt有效减少了对死记硬背的依赖，从而增强了泛化能力。具体性能提升数据未知，但整体表现出显著的优势。

## 🎯 应用场景

RetroPrompt方法具有广泛的应用前景，可应用于自然语言处理和计算机视觉等领域。例如，在文本分类、图像识别、机器翻译等任务中，可以利用RetroPrompt提升模型的泛化能力和鲁棒性。该方法尤其适用于少样本学习场景，能够有效解决数据稀缺问题，具有重要的实际应用价值。

## 📄 摘要（原文）

> The pre-trained foundation models (PFMs) have become essential for facilitating large-scale multimodal learning. Researchers have effectively employed the ``pre-train, prompt, and predict'' paradigm through prompt learning to induce improved few-shot performance. However, prompt learning approaches for PFMs still follow a parametric learning paradigm. As such, the stability of generalization in memorization and rote learning can be compromised. More specifically, conventional prompt learning might face difficulties in fully utilizing atypical instances and avoiding overfitting to shallow patterns with limited data during the process of fully-supervised training. To overcome these constraints, we present our approach, named RetroPrompt, which aims to achieve a balance between memorization and generalization by decoupling knowledge from mere memorization. Unlike traditional prompting methods, RetroPrompt leverages a publicly accessible knowledge base generated from the training data and incorporates a retrieval mechanism throughout the input, training, and inference stages. This enables the model to actively retrieve relevant contextual information from the corpus, thereby enhancing the available cues. We conduct comprehensive experiments on a variety of datasets across natural language processing and computer vision tasks to demonstrate the superior performance of our proposed approach, RetroPrompt, in both zero-shot and few-shot scenarios. Through detailed analysis of memorization patterns, we observe that RetroPrompt effectively reduces the reliance on rote memorization, leading to enhanced generalization.

