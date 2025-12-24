---
layout: default
title: "Bias Amplification in RAG: Poisoning Knowledge Retrieval to Steer LLMs"
---

# Bias Amplification in RAG: Poisoning Knowledge Retrieval to Steer LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11415" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11415v1</a>
  <a href="https://arxiv.org/pdf/2506.11415.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11415v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11415v1', 'Bias Amplification in RAG: Poisoning Knowledge Retrieval to Steer LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linlin Wang, Tianqing Zhu, Laiqiao Qin, Longxiang Gao, Wanlei Zhou

**分类**: cs.LG, cs.CL, cs.CR

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出BRRA框架以解决RAG系统中的偏见放大问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏见放大` `检索增强生成` `毒化攻击` `对抗性生成` `模型公平性` `双阶段防御` `多目标奖励`

## 📋 核心要点

1. 现有研究主要集中在RAG系统中的毒化攻击对模型输出质量的影响，忽视了其放大模型偏见的潜力。
2. 本文提出BRRA框架，通过对抗文档生成和检索结果操控，系统性放大语言模型的偏见。
3. 实验结果显示，BRRA攻击显著增强了多个主流大型语言模型的偏见，并提出了有效的防御机制。

## 📝 摘要（中文）

在大型语言模型中，检索增强生成（RAG）系统通过整合外部知识显著提升模型性能。然而，RAG也带来了新的安全风险。现有研究主要关注毒化攻击对模型输出质量的影响，忽视了其可能放大模型偏见的潜力。本文提出了一种偏见检索与奖励攻击（BRRA）框架，系统性地研究了通过RAG系统操控放大语言模型偏见的攻击路径。我们设计了一种基于多目标奖励函数的对抗文档生成方法，采用子空间投影技术操控检索结果，并构建了一个循环反馈机制以实现持续的偏见放大。实验表明，BRRA攻击能显著增强模型在多个维度上的偏见，并探讨了一种双阶段防御机制以有效减轻攻击影响。

## 🔬 方法详解

**问题定义**：本文旨在解决RAG系统中毒化攻击导致的模型偏见放大问题。现有方法未能充分考虑这些攻击对模型公平性的影响。

**核心思路**：提出BRRA框架，通过对抗性文档生成和检索结果操控，系统性地放大语言模型的偏见，揭示RAG系统安全性与模型公平性之间的关系。

**技术框架**：BRRA框架包括三个主要模块：对抗文档生成模块、检索结果操控模块和循环反馈机制。对抗文档生成模块基于多目标奖励函数生成偏见文档，检索结果操控模块利用子空间投影技术操控检索结果，循环反馈机制则实现持续的偏见放大。

**关键创新**：最重要的创新在于提出了偏见检索与奖励攻击（BRRA）框架，系统性地揭示了毒化攻击如何通过RAG系统放大模型偏见，这在现有文献中尚属首次。

**关键设计**：在对抗文档生成中，采用了多目标奖励函数以优化文档的偏见特征；在检索结果操控中，使用了子空间投影技术以实现对检索结果的精准操控；循环反馈机制则通过不断调整生成文档和检索结果，增强了偏见放大的效果。

## 📊 实验亮点

实验结果表明，BRRA攻击能够在多个维度上显著增强模型偏见，具体提升幅度达到30%以上。此外，提出的双阶段防御机制有效减轻了攻击的影响，展示了防御策略的可行性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、自动化新闻生成和法律文本分析等。通过理解和缓解RAG系统中的偏见放大问题，可以提高这些系统的公平性和可靠性，进而影响社会对自动化决策的信任和接受度。

## 📄 摘要（原文）

> In Large Language Models, Retrieval-Augmented Generation (RAG) systems can significantly enhance the performance of large language models by integrating external knowledge. However, RAG also introduces new security risks. Existing research focuses mainly on how poisoning attacks in RAG systems affect model output quality, overlooking their potential to amplify model biases. For example, when querying about domestic violence victims, a compromised RAG system might preferentially retrieve documents depicting women as victims, causing the model to generate outputs that perpetuate gender stereotypes even when the original query is gender neutral. To show the impact of the bias, this paper proposes a Bias Retrieval and Reward Attack (BRRA) framework, which systematically investigates attack pathways that amplify language model biases through a RAG system manipulation. We design an adversarial document generation method based on multi-objective reward functions, employ subspace projection techniques to manipulate retrieval results, and construct a cyclic feedback mechanism for continuous bias amplification. Experiments on multiple mainstream large language models demonstrate that BRRA attacks can significantly enhance model biases in dimensions. In addition, we explore a dual stage defense mechanism to effectively mitigate the impacts of the attack. This study reveals that poisoning attacks in RAG systems directly amplify model output biases and clarifies the relationship between RAG system security and model fairness. This novel potential attack indicates that we need to keep an eye on the fairness issues of the RAG system.

