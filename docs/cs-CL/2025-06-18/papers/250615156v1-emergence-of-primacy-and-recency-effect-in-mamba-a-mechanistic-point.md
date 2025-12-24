---
layout: default
title: "Emergence of Primacy and Recency Effect in Mamba: A Mechanistic Point of View"
---

# Emergence of Primacy and Recency Effect in Mamba: A Mechanistic Point of View

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15156" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15156v1</a>
  <a href="https://arxiv.org/pdf/2506.15156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15156v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15156v1', 'Emergence of Primacy and Recency Effect in Mamba: A Mechanistic Point of View')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Cendekia Airlangga, Hilal AlQuabeh, Munachiso S Nwadike, Kentaro Inui

**分类**: cs.CL

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**研究记忆机制，揭示Mamba模型中的首因与近因效应**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `记忆机制` `首因效应` `近因效应` `状态空间模型` `Mamba架构` `自然语言处理` `信息保留` `语义规律`

## 📋 核心要点

1. 现有语言模型在记忆机制上存在不足，无法有效解释信息的保留与遗忘过程。
2. 本研究通过Mamba架构，提出了三种机制来解释首因和近因效应的形成，揭示了记忆的动态特性。
3. 实验结果显示，Mamba模型在处理输入序列时，开头和结尾的准确性显著高于中间部分，验证了提出的机制。

## 📝 摘要（中文）

本研究探讨了状态空间语言模型中的记忆机制，利用首因和近因效应作为行为工具，揭示信息如何随时间被保留和遗忘。通过对Mamba架构的结构化回忆任务，我们观察到一致的U型准确性曲线，表明输入序列的开头和结尾表现出强大的性能。我们识别出三种机制导致这一模式的形成。首先，长期记忆由模型选择性状态空间块中的稀疏通道支持，这些通道持续编码早期输入标记，并与首因效应有因果联系。其次，短期记忆受delta调制递归的控制：最近的输入由于指数衰减而获得更多权重，但当引入干扰项时，这种近因优势会崩溃，揭示了记忆深度的明显限制。最后，我们发现记忆分配受到语义规律的动态调节：输入序列中的重复关系会改变delta门控行为，增加遗忘中间项的倾向。我们通过对两个基于Mamba的大规模语言模型进行针对性消融和输入扰动验证了这些发现。

## 🔬 方法详解

**问题定义**：本论文旨在解决状态空间语言模型中记忆机制的理解，尤其是如何通过首因和近因效应揭示信息的保留与遗忘。现有方法未能充分解释这些效应的机制和影响。

**核心思路**：论文提出通过分析Mamba架构中的记忆机制，识别出长期和短期记忆的不同影响因素，进而揭示首因和近因效应的形成原因。这样的设计有助于更好地理解模型的记忆特性。

**技术框架**：研究采用结构化回忆任务，分析Mamba模型的选择性状态空间块，重点关注长期和短期记忆的相互作用。主要模块包括记忆通道、delta调制递归和语义规律调节。

**关键创新**：本研究的创新点在于识别出三种机制：稀疏通道支持长期记忆、delta调制递归影响短期记忆，以及语义规律动态调节记忆分配，这些机制共同解释了首因和近因效应的形成。

**关键设计**：在实验中，采用了针对性消融和输入扰动的方法，验证了不同参数设置对记忆效果的影响，尤其是在1.4B和7B参数的Mamba模型中，展示了模型在记忆深度和准确性方面的表现。

## 📊 实验亮点

实验结果表明，Mamba模型在输入序列的开头和结尾的准确性显著高于中间部分，形成U型曲线。通过针对性消融实验，验证了长期记忆和短期记忆机制的有效性，展示了模型在1.4B和7B参数下的优越表现。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和信息检索等。通过深入理解记忆机制，可以优化模型在处理长文本时的表现，提高信息的保留率和检索效率，进而提升用户体验和系统性能。

## 📄 摘要（原文）

> We study memory in state-space language models using primacy and recency effects as behavioral tools to uncover how information is retained and forgotten over time. Applying structured recall tasks to the Mamba architecture, we observe a consistent U-shaped accuracy profile, indicating strong performance at the beginning and end of input sequences. We identify three mechanisms that give rise to this pattern. First, long-term memory is supported by a sparse subset of channels within the model's selective state space block, which persistently encode early input tokens and are causally linked to primacy effects. Second, short-term memory is governed by delta-modulated recurrence: recent inputs receive more weight due to exponential decay, but this recency advantage collapses when distractor items are introduced, revealing a clear limit to memory depth. Third, we find that memory allocation is dynamically modulated by semantic regularity: repeated relations in the input sequence shift the delta gating behavior, increasing the tendency to forget intermediate items. We validate these findings via targeted ablations and input perturbations on two large-scale Mamba-based language models: one with 1.4B and another with 7B parameters.

