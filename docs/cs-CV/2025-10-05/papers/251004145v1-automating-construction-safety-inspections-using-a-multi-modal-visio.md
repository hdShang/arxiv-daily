---
layout: default
title: Automating construction safety inspections using a multi-modal vision-language RAG framework
---

# Automating construction safety inspections using a multi-modal vision-language RAG framework

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.04145" target="_blank" class="toolbar-btn">arXiv: 2510.04145v1</a>
    <a href="https://arxiv.org/pdf/2510.04145.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04145v1" 
            onclick="toggleFavorite(this, '2510.04145v1', 'Automating construction safety inspections using a multi-modal vision-language RAG framework')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Chenxin Wang, Elyas Asadi Shamsabadi, Zhaohui Chen, Luming Shen, Alireza Ahmadian Fard Fini, Daniel Dias-da-Costa

**分类**: cs.CV, cs.CL, cs.IR

**发布日期**: 2025-10-05

**备注**: 33 pages, 11 figures, 7 tables

---

## 💡 一句话要点

**提出SiteShield，利用多模态RAG框架自动化建筑安全检查报告生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `建筑安全` `多模态学习` `视觉语言模型` `检索增强生成` `自动化报告`

## 📋 核心要点

1. 现有建筑安全检查方法依赖人工，效率低且易出错，难以有效处理海量信息。
2. SiteShield利用多模态LVLM和RAG框架，融合视觉和音频信息，提升信息检索和报告生成能力。
3. 实验表明，SiteShield在真实数据上显著优于传统方法，F1值达到0.82，召回率高达0.96。

## 📝 摘要（中文）

传统建筑安全检查方法效率低下，需要处理大量信息。大型视觉语言模型(LVLMs)的最新进展为通过增强视觉和语言理解来自动化安全检查提供了机会。然而，现有应用面临不相关或不具体的响应、受限的模态输入和幻觉等局限性。为此目的使用大型语言模型(LLMs)受到训练数据可用性的限制，并且经常缺乏实时适应性。本研究介绍SiteShield，一个基于多模态LVLM的检索增强生成(RAG)框架，通过集成视觉和音频输入来自动化建筑安全检查报告。使用真实世界的数据，SiteShield优于没有RAG的单模态LLM，F1得分为0.82，汉明损失为0.04，精确率为0.76，召回率为0.96。研究结果表明，SiteShield为提高安全报告生成中的信息检索和效率提供了一种新途径。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑安全检查报告生成效率低下的问题。现有方法依赖人工检查和信息整理，耗时费力，且容易遗漏关键信息。此外，现有基于LLM的方法存在响应不相关、输入模态受限以及产生幻觉等问题。

**核心思路**：论文的核心思路是利用多模态信息（视觉和音频）增强LLM的理解能力，并结合RAG框架从海量数据中检索相关信息，从而生成更准确、更全面的安全检查报告。通过RAG，模型可以避免幻觉，并能适应实时变化。

**技术框架**：SiteShield框架包含以下主要模块：1) 多模态数据输入模块，用于接收视觉和音频数据；2) 特征提取模块，用于提取视觉和音频特征；3) 检索模块，基于提取的特征从知识库中检索相关信息；4) LLM生成模块，利用检索到的信息和原始输入生成安全检查报告。整体流程为：输入多模态数据 -> 提取特征 -> 检索相关信息 -> LLM生成报告。

**关键创新**：该论文的关键创新在于将多模态信息融合与RAG框架相结合，用于建筑安全检查报告的自动生成。与传统的单模态方法相比，该方法能够更全面地理解现场情况。与没有RAG的LLM相比，该方法能够减少幻觉，并能利用外部知识库进行实时更新。

**关键设计**：论文中未明确给出关键参数设置、损失函数、网络结构等技术细节。但可以推断，视觉特征提取可能使用了预训练的卷积神经网络，音频特征提取可能使用了梅尔频谱等方法。RAG框架中的检索模块可能使用了向量数据库和相似度搜索算法。LLM生成模块可能使用了Transformer架构的语言模型。

## 📊 实验亮点

SiteShield在真实世界数据集上进行了评估，实验结果表明，与没有RAG的单模态LLM相比，SiteShield在F1得分上提高了显著，达到了0.82，汉明损失降低到0.04，精确率为0.76，召回率高达0.96。这些数据表明，SiteShield能够有效地提高安全检查报告生成的准确性和完整性。

## 🎯 应用场景

该研究成果可应用于建筑行业的安全巡检、事故预防和合规性管理。通过自动化安全检查报告的生成，可以显著提高工作效率，降低人为错误，并为安全管理人员提供更及时、更全面的信息支持。未来，该技术还可扩展到其他需要多模态信息融合和实时知识更新的领域，如智能制造、智慧城市等。

## 📄 摘要（原文）

> Conventional construction safety inspection methods are often inefficient as they require navigating through large volume of information. Recent advances in large vision-language models (LVLMs) provide opportunities to automate safety inspections through enhanced visual and linguistic understanding. However, existing applications face limitations including irrelevant or unspecific responses, restricted modal inputs and hallucinations. Utilisation of Large Language Models (LLMs) for this purpose is constrained by availability of training data and frequently lack real-time adaptability. This study introduces SiteShield, a multi-modal LVLM-based Retrieval-Augmented Generation (RAG) framework for automating construction safety inspection reports by integrating visual and audio inputs. Using real-world data, SiteShield outperformed unimodal LLMs without RAG with an F1 score of 0.82, hamming loss of 0.04, precision of 0.76, and recall of 0.96. The findings indicate that SiteShield offers a novel pathway to enhance information retrieval and efficiency in generating safety reports.

