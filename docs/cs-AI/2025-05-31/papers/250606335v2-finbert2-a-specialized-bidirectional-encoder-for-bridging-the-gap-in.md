---
layout: default
title: FinBERT2: A Specialized Bidirectional Encoder for Bridging the Gap in Finance-Specific Deployment of Large Language Models
---

# FinBERT2: A Specialized Bidirectional Encoder for Bridging the Gap in Finance-Specific Deployment of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06335" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06335v2</a>
  <a href="https://arxiv.org/pdf/2506.06335.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06335v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06335v2', 'FinBERT2: A Specialized Bidirectional Encoder for Bridging the Gap in Finance-Specific Deployment of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuan Xu, Fufang Wen, Beilin Chu, Zhibing Fu, Qinhong Lin, Jiaqi Liu, Binjie Fei, Yu Li, Linna Zhou, Zhongliang Yang

**分类**: cs.IR, cs.AI, cs.CE, cs.CL

**发布日期**: 2025-05-31 (更新: 2025-07-05)

---

## 💡 一句话要点

**提出FinBERT2以解决金融领域大语言模型应用不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融文本分析` `自然语言处理` `双向编码器` `预训练模型` `市场情绪识别` `智能金融` `信息检索`

## 📋 核心要点

1. 现有大型语言模型在金融领域应用时表现不佳，尤其在判别和生成任务上存在明显不足。
2. FinBERT2是一种专门为金融领域设计的双向编码器，基于大量金融特定语料进行预训练，旨在提升模型在金融任务中的表现。
3. 实验结果表明，FinBERT2在多个金融分类和检索任务中显著优于现有的BERT和LLM模型，提升幅度可达12.3%。

## 📝 摘要（中文）

在自然语言处理领域，研究重点已从仅编码的小型语言模型（如BERT）转向仅解码的大型语言模型（如GPT-3）。然而，LLMs在金融领域的实际应用暴露出三大局限性：一是LLMs在判别任务上的表现往往不如经过微调的BERT，尽管其计算资源消耗更高；二是在生成任务中，LLMs过于依赖检索增强生成（RAG）方法，而通用检索器在领域特定检索任务中表现不佳；三是在其他特征基础场景中也存在不足。为此，本文提出了FinBERT2，这是一种专门的双向编码器，基于32亿个高质量金融特定语料进行预训练，成为已知的最大中文金融预训练语料。FinBERT2在五个金融分类任务中，微调模型（Fin-Labelers）平均超越其他（Fin）BERT变体0.4%-3.3%，超越领先的LLMs 9.7%-12.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在金融领域应用中的不足，尤其是在判别任务和生成任务中的表现不佳，以及对领域特定信息的检索能力不足。

**核心思路**：FinBERT2通过在高质量金融特定语料上进行预训练，构建一个更适合金融任务的双向编码器，以提升模型在金融领域的应用效果。

**技术框架**：FinBERT2的整体架构包括预训练阶段和微调阶段，预训练使用32亿个金融语料，微调则针对特定金融任务进行优化。

**关键创新**：FinBERT2的主要创新在于其专门针对金融领域的预训练数据集和双向编码器设计，使其在金融特定任务中表现优于传统的BERT和LLM模型。

**关键设计**：在模型设计中，FinBERT2采用了优化的损失函数和网络结构，确保在金融分类和检索任务中能够有效捕捉领域特征。

## 📊 实验亮点

FinBERT2在五个金融分类任务中，微调模型（Fin-Labelers）平均超越其他（Fin）BERT变体0.4%-3.3%，超越领先的LLMs 9.7%-12.3%。在金融检索任务中，Fin-Retrievers在开放源代码和专有嵌入器上分别提升了6.8%和4.2%。

## 🎯 应用场景

FinBERT2的研究成果在金融文本分析、市场情绪识别、投资决策支持等领域具有广泛的应用潜力。通过提升模型在金融特定任务中的表现，能够为金融机构提供更精准的分析工具，进而推动智能金融的发展。

## 📄 摘要（原文）

> In natural language processing (NLP), the focus has shifted from encoder-only tiny language models like BERT to decoder-only large language models(LLMs) such as GPT-3. However, LLMs' practical application in the financial sector has revealed three limitations: (1) LLMs often perform worse than fine-tuned BERT on discriminative tasks despite costing much higher computational resources, such as market sentiment analysis in financial reports; (2) Application on generative tasks heavily relies on retrieval augmented generation (RAG) methods to provide current and specialized information, with general retrievers showing suboptimal performance on domain-specific retrieval tasks; (3) There are additional inadequacies in other feature-based scenarios, such as topic modeling. We introduce FinBERT2, a specialized bidirectional encoder pretrained on a high-quality, financial-specific corpus of 32b tokens. This represents the largest known Chinese financial pretraining corpus for models of this parameter size. As a better backbone, FinBERT2 can bridge the gap in the financial-specific deployment of LLMs through the following achievements: (1) Discriminative fine-tuned models (Fin-Labelers) outperform other (Fin)BERT variants by 0.4%-3.3% and leading LLMs by 9.7%-12.3% on average across five financial classification tasks. (2) Contrastive fine-tuned models (Fin-Retrievers) outperform both open-source (e.g., +6.8\% avg improvement over BGE-base-zh) and proprietary (e.g., +4.2\% avg improvement over OpenAI's text-embedding-3-large) embedders across five financial retrieval tasks; (3) Building on FinBERT2 variants, we construct the Fin-TopicModel, which enables superior clustering and topic representation for financial titles. Our work revisits financial BERT models through comparative analysis with contemporary LLMs and offers practical insights for effectively utilizing FinBERT in the LLMs era.

