---
layout: default
title: "The Open Proof Corpus: A Large-Scale Study of LLM-Generated Mathematical Proofs"
---

# The Open Proof Corpus: A Large-Scale Study of LLM-Generated Mathematical Proofs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21621" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21621v1</a>
  <a href="https://arxiv.org/pdf/2506.21621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21621v1', 'The Open Proof Corpus: A Large-Scale Study of LLM-Generated Mathematical Proofs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jasper Dekoninck, Ivo Petrov, Kristian Minchev, Mislav Balunovic, Martin Vechev, Miroslav Marinov, Maria Drencheva, Lyuba Konova, Milen Shumanov, Kaloyan Tsvetkov, Nikolay Drenchev, Lazar Todorov, Kalina Nikolova, Nikolay Georgiev, Vanesa Kalinkova, Margulan Ismoldayev

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**提出开放证明语料库以推动数学证明生成研究**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学证明生成` `大型语言模型` `开放证明语料库` `数据集构建` `自动化证明` `模型微调` `人工智能研究`

## 📋 核心要点

1. 现有的数学证明生成方法缺乏高质量的大规模数据集，限制了模型的训练和评估。
2. 本文提出开放证明语料库（OPC），包含5000多个经过人类评估的LLM生成证明，旨在推动证明生成研究。
3. 通过在OPC上微调模型，取得了与当前最佳模型相当的证明正确性评估性能。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在数学证明生成方面取得了显著进展，但缺乏高质量的人类评估证明的大规模数据集限制了进一步发展。为此，本文提出了开放证明语料库（OPC），该数据集包含5000多个由最先进的LLMs生成并经过人类评估的证明。OPC旨在广泛适用并支持证明生成研究，首次包含来自美国数学奥林匹克（USAMO）和国际数学奥林匹克（IMO）等著名数学竞赛的正确LLM生成解答。通过OPC，本文探讨了自动证明生成中的关键问题，并展示了在该数据集上微调的8B参数模型的有效性，其性能与最佳模型Gemini-2.5-Pro相当。

## 🔬 方法详解

**问题定义**：本文旨在解决缺乏高质量、经过人类评估的数学证明数据集的问题，现有方法在训练和评估上存在显著不足。

**核心思路**：提出开放证明语料库（OPC），该数据集包含5000多个LLM生成的、经过人类评估的数学证明，旨在为证明生成研究提供基础数据。

**技术框架**：OPC的构建包括数据收集、评估和整理三个主要阶段，确保数据的质量和多样性，以支持后续的研究和模型训练。

**关键创新**：OPC是首个包含大量正确LLM生成解答的数学证明数据集，特别是针对著名数学竞赛的问题，填补了现有研究的空白。

**关键设计**：在数据集构建中，采用了严格的评估标准，确保每个证明的准确性和完整性，同时在模型微调过程中使用了适当的损失函数和参数设置，以优化证明的生成质量。

## 📊 实验亮点

在使用开放证明语料库（OPC）进行微调后，8B参数模型在证明正确性评估任务上达到了与最佳模型Gemini-2.5-Pro相当的性能，展示了数据集的有效性和实用性。

## 🎯 应用场景

开放证明语料库（OPC）可广泛应用于数学教育、自动证明生成和人工智能研究等领域。其提供的高质量数据集将推动相关模型的训练和评估，促进数学证明自动化的进步，未来可能在教育和科研中发挥重要作用。

## 📄 摘要（原文）

> In recent months, large language models (LLMs) have made significant progress in mathematical proof generation, but further advancement is hindered by the lack of a large-scale, high-quality dataset of human-evaluated proofs. While expensive to create, such a dataset is essential for driving improvements in training and enabling a rigorous analysis of proof generation capabilities. In this work, we present the Open Proof Corpus (OPC), a dataset comprising over 5,000 human-evaluated proofs produced by state-of-the-art LLMs. The OPC was specifically designed for broad applicability and downstream usage in proof generation research and is the first to include a substantial number of correct, LLM-generated solutions to problems from prestigious mathematics competitions such as the USAMO and IMO. Using the OPC, we explore critical questions in automated proof generation: (1) the performance gap between natural language and formal proof generation, (2) the discrepancy between final-answer accuracy and full-proof validity, and (3) the impact of best-of-n selection on proof quality. Finally, to showcase the utility of the OPC, we finetune an 8B-parameter model on the dataset, obtaining a model that performs on par with the best model, Gemini-2.5-Pro, on the task of evaluating proof correctness.

