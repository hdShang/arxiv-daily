---
layout: default
title: "Catalog-Native LLM: Speaking Item-ID Dialect with Less Entanglement for Recommendation"
---

# Catalog-Native LLM: Speaking Item-ID Dialect with Less Entanglement for Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05125" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05125v1</a>
  <a href="https://arxiv.org/pdf/2510.05125.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05125v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05125v1', 'Catalog-Native LLM: Speaking Item-ID Dialect with Less Entanglement for Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reza Shirkavand, Xiaokai Wei, Chen Wang, Zheng Hui, Heng Huang, Michelle Gong

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出IDIOMoE，通过Item-ID方言和MoE结构，增强LLM在推荐系统中的协同过滤能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推荐系统` `大型语言模型` `协同过滤` `混合专家模型` `Item-ID` `自然语言理解` `个性化推荐`

## 📋 核心要点

1. 现有推荐系统难以同时兼顾协同过滤的效率和LLM的语义理解能力，无法满足用户对自然语言交互的需求。
2. IDIOMoE将item交互历史视为一种“Item-ID方言”，通过MoE结构使LLM能够同时理解文本和协同信号。
3. 实验表明，IDIOMoE在多个数据集上取得了优秀的推荐性能，并保留了预训练LLM的文本理解能力。

## 📝 摘要（中文）

协同过滤在推荐系统中具有预测准确性和效率优势，而大型语言模型(LLM)则具备表达性和泛化推理能力。现代推荐系统需要结合两者的优点。然而，用户对自然语言查询和透明解释等日益增长的期望，进一步突显了统一方法的需求。实现这一目标并非易事。协同信号通常具有token效率，但在语义上不透明，而LLM在语义上丰富，但如果仅在文本输入上训练，则难以建模隐式用户偏好。本文介绍了Item-ID + Oral-language Mixture-of-Experts Language Model (IDIOMoE)，它将item交互历史视为语言空间中的一种原生方言，使协同信号能够以与自然语言相同的方式被理解。通过将预训练LLM的每个block的Feed Forward Network拆分为一个单独的文本专家和一个item专家，并使用token-type gating，我们的方法避免了文本和目录模态之间的破坏性干扰。IDIOMoE在公共和专有数据集上都表现出强大的推荐性能，同时保留了预训练模型的文本理解能力。

## 🔬 方法详解

**问题定义**：现有推荐系统面临的挑战是如何有效地融合协同过滤和大型语言模型（LLM）的优势。协同过滤虽然高效，但语义信息不足；LLM虽然语义丰富，但在建模隐式用户偏好方面存在困难。此外，用户期望推荐系统能够理解自然语言查询并提供透明的解释，这进一步增加了融合的难度。

**核心思路**：IDIOMoE的核心思路是将item交互历史视为一种“Item-ID方言”，使LLM能够像理解自然语言一样理解协同信号。通过这种方式，协同过滤的效率和LLM的语义理解能力可以更好地结合。同时，为了避免文本和item信息之间的干扰，采用了MoE结构。

**技术框架**：IDIOMoE基于预训练的LLM构建。其主要架构包括：1) 将LLM的每个block中的Feed Forward Network (FFN) 分裂为两个专家：一个文本专家和一个item专家。2) 使用token-type gating机制，根据输入token的类型（文本或item ID）来动态地选择使用哪个专家。3) 通过这种方式，文本和item信息可以并行处理，避免了相互干扰。

**关键创新**：IDIOMoE的关键创新在于将item交互历史视为一种语言，并设计了一种MoE结构来处理文本和item信息。这种方法使得LLM能够更好地理解协同信号，从而提高推荐性能。与现有方法相比，IDIOMoE避免了直接将item ID嵌入到文本序列中，从而减少了文本和item信息之间的耦合。

**关键设计**：IDIOMoE的关键设计包括：1) Token-type gating机制：根据输入token的类型（文本或item ID）来动态地选择使用哪个专家。具体来说，使用一个可学习的门控向量来控制文本专家和item专家的激活程度。2) 损失函数：IDIOMoE使用标准的语言模型损失函数进行训练，同时可以添加额外的推荐相关的损失函数，例如pairwise ranking loss。

## 📊 实验亮点

IDIOMoE在公共和专有数据集上都取得了显著的推荐性能提升。具体来说，在某些数据集上，IDIOMoE的性能超过了现有的协同过滤和LLM-based推荐方法。此外，实验结果表明，IDIOMoE在提高推荐性能的同时，保留了预训练LLM的文本理解能力。

## 🎯 应用场景

IDIOMoE可应用于各种推荐系统，尤其是在需要理解自然语言查询和提供透明解释的场景中。例如，电商平台可以使用IDIOMoE来理解用户的搜索意图，并根据用户的历史行为和偏好推荐相关的商品。此外，IDIOMoE还可以用于个性化新闻推荐、音乐推荐等领域，提升用户体验。

## 📄 摘要（原文）

> While collaborative filtering delivers predictive accuracy and efficiency, and Large Language Models (LLMs) enable expressive and generalizable reasoning, modern recommendation systems must bring these strengths together. Growing user expectations, such as natural-language queries and transparent explanations, further highlight the need for a unified approach. However, doing so is nontrivial. Collaborative signals are often token-efficient but semantically opaque, while LLMs are semantically rich but struggle to model implicit user preferences when trained only on textual inputs. This paper introduces Item-ID + Oral-language Mixture-of-Experts Language Model (IDIOMoE), which treats item interaction histories as a native dialect within the language space, enabling collaborative signals to be understood in the same way as natural language. By splitting the Feed Forward Network of each block of a pretrained LLM into a separate text expert and an item expert with token-type gating, our method avoids destructive interference between text and catalog modalities. IDIOMoE demonstrates strong recommendation performance across both public and proprietary datasets, while preserving the text understanding of the pretrained model.

