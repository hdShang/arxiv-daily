---
layout: default
title: TCM-Ladder: A Benchmark for Multimodal Question Answering on Traditional Chinese Medicine
---

# TCM-Ladder: A Benchmark for Multimodal Question Answering on Traditional Chinese Medicine

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24063" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24063v2</a>
  <a href="https://arxiv.org/pdf/2505.24063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24063v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24063v2', 'TCM-Ladder: A Benchmark for Multimodal Question Answering on Traditional Chinese Medicine')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Xie, Yang Yu, Ziyang Zhang, Shuai Zeng, Jiaxuan He, Ayush Vasireddy, Xiaoting Tang, Congyu Guo, Lening Zhao, Congcong Jing, Guanghui An, Dong Xu

**分类**: cs.CL, cs.DB

**发布日期**: 2025-05-29 (更新: 2025-10-24)

---

## 💡 一句话要点

**提出TCM-Ladder以解决中医多模态问答评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态问答` `传统中医` `大型语言模型` `数据集构建` `评估方法` `智能问答` `医疗辅助决策`

## 📋 核心要点

1. 现有的中医问答评估数据集主要基于文本，缺乏多模态支持，无法全面评估大型语言模型的能力。
2. TCM-Ladder数据集结合了文本、图像和视频，涵盖多个中医学科，提供了一个统一的多模态问答基准。
3. 通过与九个通用领域和五个中医特定的LLMs进行比较实验，验证了TCM-Ladder的有效性和Ladder-Score的评估能力。

## 📝 摘要（中文）

传统中医（TCM）作为一种有效的替代医学，近年来受到越来越多的关注。随着针对TCM的大型语言模型（LLMs）的快速发展，迫切需要一个客观且全面的评估框架来评估其在实际任务中的表现。现有的评估数据集范围有限，主要基于文本，缺乏统一和标准化的多模态问答基准。为了解决这一问题，本文提出了TCM-Ladder，这是第一个专门为评估大型TCM语言模型而设计的综合多模态问答数据集。该数据集涵盖了TCM的多个核心学科，并结合文本、图像和视频等多种模态，构建了超过52,000个问题。我们还提出了Ladder-Score评估方法，专门用于TCM问答的质量评估。

## 🔬 方法详解

**问题定义**：本文旨在解决现有中医问答评估数据集缺乏多模态支持和统一标准的问题，现有方法无法全面评估大型语言模型在实际应用中的表现。

**核心思路**：提出TCM-Ladder数据集，结合文本、图像和视频等多种模态，涵盖中医的多个核心学科，以提供全面的评估框架。

**技术框架**：TCM-Ladder数据集由自动化和手动过滤过程构建，包含超过52,000个问题，涵盖单选、多选、填空、诊断对话和视觉理解任务。评估方法Ladder-Score专门设计用于评估答案质量。

**关键创新**：这是首次系统性地在统一的多模态基准上评估主流通用领域和中医特定的LLMs，填补了现有研究的空白。

**关键设计**：数据集构建过程中采用了自动化和手动过滤相结合的方法，确保问题的多样性和质量，同时Ladder-Score评估方法关注术语使用和语义表达的准确性。

## 📊 实验亮点

在与九个通用领域和五个中医特定的LLMs的比较实验中，TCM-Ladder显示出显著的评估能力，Ladder-Score有效地评估了答案的质量，提升了中医问答系统的准确性和实用性。

## 🎯 应用场景

TCM-Ladder的研究成果可广泛应用于中医领域的智能问答系统、医疗辅助决策和教育培训等场景。通过提供一个标准化的评估框架，能够推动中医相关大型语言模型的进一步发展与应用，提升中医知识的传播与应用效率。

## 📄 摘要（原文）

> Traditional Chinese Medicine (TCM), as an effective alternative medicine, has been receiving increasing attention. In recent years, the rapid development of large language models (LLMs) tailored for TCM has highlighted the urgent need for an objective and comprehensive evaluation framework to assess their performance on real-world tasks. However, existing evaluation datasets are limited in scope and primarily text-based, lacking a unified and standardized multimodal question-answering (QA) benchmark. To address this issue, we introduce TCM-Ladder, the first comprehensive multimodal QA dataset specifically designed for evaluating large TCM language models. The dataset covers multiple core disciplines of TCM, including fundamental theory, diagnostics, herbal formulas, internal medicine, surgery, pharmacognosy, and pediatrics. In addition to textual content, TCM-Ladder incorporates various modalities such as images and videos. The dataset was constructed using a combination of automated and manual filtering processes and comprises over 52,000 questions. These questions include single-choice, multiple-choice, fill-in-the-blank, diagnostic dialogue, and visual comprehension tasks. We trained a reasoning model on TCM-Ladder and conducted comparative experiments against nine state-of-the-art general domain and five leading TCM-specific LLMs to evaluate their performance on the dataset. Moreover, we propose Ladder-Score, an evaluation method specifically designed for TCM question answering that effectively assesses answer quality in terms of terminology usage and semantic expression. To the best of our knowledge, this is the first work to systematically evaluate mainstream general domain and TCM-specific LLMs on a unified multimodal benchmark. The datasets and leaderboard are publicly available at https://tcmladder.com and will be continuously updated.

