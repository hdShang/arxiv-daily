---
layout: default
title: Confidence-Credibility Aware Weighted Ensembles of Small LLMs Outperform Large LLMs in Emotion Detection
---

# Confidence-Credibility Aware Weighted Ensembles of Small LLMs Outperform Large LLMs in Emotion Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17630" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17630v1</a>
  <a href="https://arxiv.org/pdf/2512.17630.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17630v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17630v1', 'Confidence-Credibility Aware Weighted Ensembles of Small LLMs Outperform Large LLMs in Emotion Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Menna Elgabry, Ali Hamdi

**分类**: cs.CL, cs.LG

**发布日期**: 2025-12-19

**备注**: Accepted at IRICT 2025

---

## 💡 一句话要点

**提出置信度-可信度加权的小LLM集成方法，在情感检测任务上超越大LLM**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感检测` `集成学习` `小型语言模型` `置信度加权` `可信度感知`

## 📋 核心要点

1. 现有情感检测方法依赖同构架构，且大型语言模型参数冗余，效率较低。
2. 提出一种置信度-可信度加权集成框架，结合多个小型Transformer模型，利用模型偏差。
3. 实验结果表明，该方法在情感检测任务上超越了大型语言模型，且参数效率更高。

## 📝 摘要（中文）

本文提出了一种基于Condorcet陪审团定理（CJT）的置信度加权、可信度感知的文本情感检测集成框架。与通常依赖同构架构的传统集成方法不同，我们的方法结合了架构多样的小型Transformer语言模型（sLLM），包括BERT、RoBERTa、DistilBERT、DeBERTa和ELECTRA，每个模型都经过情感分类的完全微调。为了保持误差多样性，我们在利用每个模型独特偏差的同时，最小化参数收敛。双重加权投票机制集成了全局可信度（验证F1分数）和局部置信度（实例级概率），以动态地加权模型贡献。在DAIR-AI数据集上的实验表明，我们的可信度-置信度集成方法实现了93.5%的宏F1分数，超过了最先进的基准，并显著优于大型LLM，包括Falcon、Mistral、Qwen和Phi，即使在任务特定的低秩适应（LoRA）之后也是如此。我们的小型LLM集成总共只有595M参数，证明比高达7B参数的模型更具参数效率和鲁棒性，这表明精心设计的小型、微调模型集成可以在情感检测等专门的自然语言处理（NLP）任务中优于更大的LLM。

## 🔬 方法详解

**问题定义**：论文旨在解决文本情感检测任务中，现有方法依赖于单一大型语言模型，导致参数冗余、计算成本高昂，且忽略了不同模型之间的互补性的问题。现有方法的痛点在于模型复杂度高，难以部署，且性能提升受限。

**核心思路**：论文的核心思路是利用Condorcet陪审团定理（CJT）的思想，通过集成多个小型、异构的语言模型，利用它们各自的优势和偏差，从而在整体上获得更准确的情感分类结果。这种方法旨在通过模型的多样性来提高鲁棒性和泛化能力。

**技术框架**：整体框架包含以下几个主要模块：1) 选择多个小型Transformer模型（BERT、RoBERTa、DistilBERT、DeBERTa、ELECTRA）。2) 对每个模型进行情感分类任务的微调。3) 使用双重加权投票机制，结合全局可信度（验证集F1分数）和局部置信度（实例级别的预测概率）来动态地加权每个模型的贡献。4) 将加权后的预测结果进行集成，得到最终的情感分类结果。

**关键创新**：最重要的技术创新点在于提出了置信度-可信度加权的集成方法。与传统的集成方法不同，该方法不仅考虑了模型的全局性能（可信度），还考虑了模型在特定实例上的预测置信度，从而能够更精细地控制每个模型的贡献。此外，选择异构的小型模型也有助于保持模型的多样性，避免过拟合。

**关键设计**：关键设计包括：1) 模型选择：选择具有不同架构和训练方式的小型Transformer模型，以保证模型的多样性。2) 加权机制：使用验证集F1分数作为全局可信度，使用模型输出的softmax概率作为局部置信度，并设计合理的加权公式将两者结合。3) 损失函数：使用交叉熵损失函数进行模型微调。4) 最小化参数收敛：通过不同的初始化和训练策略，避免模型参数过度相似。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17630v1/architecture1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17630v1/ar2.drawio.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在DAIR-AI数据集上实现了93.5%的宏F1分数，超过了当前最先进的基线方法，并且显著优于大型语言模型（例如Falcon、Mistral、Qwen和Phi），即使这些大型模型经过LoRA微调后也无法达到相同的性能。此外，该集成模型仅包含595M参数，远小于大型语言模型，证明了其更高的参数效率。

## 🎯 应用场景

该研究成果可应用于情感分析、舆情监控、智能客服、个性化推荐等领域。通过集成多个小型模型，可以在保证性能的同时，降低计算成本和部署难度，使得情感检测技术能够更广泛地应用于资源受限的场景。未来，该方法可以扩展到其他自然语言处理任务，例如文本分类、命名实体识别等。

## 📄 摘要（原文）

> This paper introduces a confidence-weighted, credibility-aware ensemble framework for text-based emotion detection, inspired by Condorcet's Jury Theorem (CJT). Unlike conventional ensembles that often rely on homogeneous architectures, our approach combines architecturally diverse small transformer-based large language models (sLLMs) - BERT, RoBERTa, DistilBERT, DeBERTa, and ELECTRA, each fully fine-tuned for emotion classification. To preserve error diversity, we minimize parameter convergence while taking advantage of the unique biases of each model. A dual-weighted voting mechanism integrates both global credibility (validation F1 score) and local confidence (instance-level probability) to dynamically weight model contributions. Experiments on the DAIR-AI dataset demonstrate that our credibility-confidence ensemble achieves a macro F1 score of 93.5 percent, surpassing state-of-the-art benchmarks and significantly outperforming large-scale LLMs, including Falcon, Mistral, Qwen, and Phi, even after task-specific Low-Rank Adaptation (LoRA). With only 595M parameters in total, our small LLMs ensemble proves more parameter-efficient and robust than models up to 7B parameters, establishing that carefully designed ensembles of small, fine-tuned models can outperform much larger LLMs in specialized natural language processing (NLP) tasks such as emotion detection.

