---
layout: default
title: Faithful and Robust LLM-Driven Theorem Proving for NLI Explanations
---

# Faithful and Robust LLM-Driven Theorem Proving for NLI Explanations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24264" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24264v1</a>
  <a href="https://arxiv.org/pdf/2505.24264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24264v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24264v1', 'Faithful and Robust LLM-Driven Theorem Proving for NLI Explanations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Quan, Marco Valentino, Louise A. Dennis, André Freitas

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

**备注**: Camera-ready for ACL 2025

---

## 💡 一句话要点

**提出LLM驱动的定理证明方法以提升NLI解释的可靠性与稳健性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言推理` `定理证明` `大型语言模型` `自动形式化` `逻辑表达` `语义损失` `模型优化`

## 📋 核心要点

1. 现有方法在将自然语言翻译为机器可验证形式时，面临语义信息丢失和逻辑结构捕捉不精确的问题。
2. 论文提出通过多种策略来减轻语义损失、纠正语法错误，并利用逻辑表达指导LLMs生成结构化证明。
3. 实验结果显示，所提方法在e-SNLI、QASC和WorldTree数据集上，自动形式化和解释精炼的提升幅度分别达到18.46%、34.2%、39.77%和29.5%、51.5%、41.25%。

## 📝 摘要（中文）

自然语言解释在自然语言推理（NLI）中起着重要作用，揭示了前提如何逻辑上蕴含假设。近期研究表明，大型语言模型（LLMs）与定理证明器（TPs）的结合可以帮助验证和改善NLI解释的有效性。然而，TPs需要将自然语言翻译为机器可验证的形式表示，这一过程可能导致语义信息的丢失和不忠实的解释。本文探讨了几种策略，以减轻自动形式化过程中的语义损失、有效识别和纠正逻辑表示中的语法错误、利用逻辑表达指导LLMs生成结构化证明草图，并提高LLMs对TP反馈的理解能力。实验证明，所提出的策略在自动形式化和解释精炼方面显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决在自然语言推理中，如何有效地将自然语言解释转化为机器可验证的形式表示，同时避免语义信息的丢失和不准确的逻辑结构捕捉。现有方法在这方面的表现存在不足，尤其是在定理证明的严谨性和稳健性方面。

**核心思路**：论文的核心思路是通过设计一系列策略来减轻自动形式化过程中的语义损失，识别并纠正逻辑表示中的语法错误，并利用逻辑表达来指导LLMs生成结构化的证明草图。这种设计旨在提高LLMs在形式验证框架中的表现。

**技术框架**：整体架构包括四个主要模块：1) 语义损失减轻模块；2) 语法错误识别与纠正模块；3) 逻辑表达指导生成模块；4) LLM与TP反馈迭代优化模块。各模块相互协作，以提升整体性能。

**关键创新**：最重要的技术创新在于提出了一种混合LLM-TP架构，通过特定干预显著提高了验证效率，减少了成功验证所需的迭代次数。这一方法与现有技术相比，能够更有效地处理逻辑推理任务。

**关键设计**：在设计中，采用了特定的参数设置和损失函数，以确保模型在自动形式化和解释精炼中的表现。此外，网络结构经过优化，以支持逻辑表达的生成和反馈的有效利用。具体的技术细节包括对LLMs的训练策略和TP的反馈机制的调整。

## 📊 实验亮点

实验结果表明，所提出的方法在多个数据集上均显著优于现有最先进模型，自动形式化的提升幅度分别为18.46%、34.2%、39.77%，而解释精炼的提升幅度为29.5%、51.5%、41.25%。此外，混合LLM-TP架构的特定干预显著提高了验证效率，减少了迭代次数。

## 🎯 应用场景

该研究的潜在应用领域包括自动化推理系统、智能问答系统和教育技术等。通过提高NLI解释的可靠性与稳健性，能够为用户提供更准确的推理支持，促进人机交互的智能化发展。未来，该方法可能在法律、医疗等需要严谨推理的领域发挥重要作用。

## 📄 摘要（原文）

> Natural language explanations play a fundamental role in Natural Language Inference (NLI) by revealing how premises logically entail hypotheses. Recent work has shown that the interaction of large language models (LLMs) with theorem provers (TPs) can help verify and improve the validity of NLI explanations. However, TPs require translating natural language into machine-verifiable formal representations, a process that introduces the risk of semantic information loss and unfaithful interpretation, an issue compounded by LLMs' challenges in capturing critical logical structures with sufficient precision. Moreover, LLMs are still limited in their capacity for rigorous and robust proof construction within formal verification frameworks. To mitigate issues related to faithfulness and robustness, this paper investigates strategies to (1) alleviate semantic loss during autoformalisation, (2) efficiently identify and correct syntactic errors in logical representations, (3) explicitly use logical expressions to guide LLMs in generating structured proof sketches, and (4) increase LLMs' capacity of interpreting TP's feedback for iterative refinement. Our empirical results on e-SNLI, QASC and WorldTree using different LLMs demonstrate that the proposed strategies yield significant improvements in autoformalisation (+18.46%, +34.2%, +39.77%) and explanation refinement (+29.5%, +51.5%, +41.25%) over the state-of-the-art model. Moreover, we show that specific interventions on the hybrid LLM-TP architecture can substantially improve efficiency, drastically reducing the number of iterations required for successful verification.

