---
layout: default
title: "CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning"
---

# CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19282" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19282v3</a>
  <a href="https://arxiv.org/pdf/2508.19282.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19282v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19282v3', 'CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqiang Cui, Yunpeng Weng, Xing Tang, Peiyang Liu, Shiwei Li, Bowei He, Jiamin Chen, Yansen Zhang, Xiuqiang He, Chen Ma

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-24 (更新: 2025-09-28)

**备注**: This paper is under continuous improvement

---

## 💡 一句话要点

**提出CORE以解决RAG文档压缩效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `文档压缩` `强化学习` `无损压缩` `任务性能优化`

## 📋 核心要点

1. 现有的文档压缩方法在RAG中往往依赖于启发式规则，导致任务性能下降。
2. CORE方法通过端到端优化，利用下游任务性能反馈，迭代改进压缩策略。
3. 实验结果显示，CORE在高压缩比下有效提升了任务性能，EM得分提高了3.3分。

## 📝 摘要（中文）

检索增强生成（RAG）已成为提高大型语言模型知识更新及时性和响应准确性的有效方法。然而，检索到的大量文档显著增加了输入长度，导致计算成本上升。现有的文档压缩方法往往依赖于预定义的启发式规则，缺乏明确的压缩指导，且可能降低任务性能。为了解决这些问题，本文提出了CORE，一种新颖的无损上下文压缩方法，能够端到端优化，并不依赖于难以获得的预定义压缩标签，而是利用下游任务性能作为反馈信号，迭代改进压缩策略。通过在四个数据集上的广泛实验，CORE实现了3%的高压缩比，不仅避免了与完整文档相比的性能下降，还将平均准确匹配（EM）得分提高了3.3分。

## 🔬 方法详解

**问题定义**：本文旨在解决在检索增强生成（RAG）中，文档压缩效率低下的问题。现有方法通常依赖于预定义的启发式规则，导致压缩后的内容无法有效支持下游任务，进而影响性能。

**核心思路**：CORE方法的核心思想是通过端到端的优化，不依赖于难以获得的压缩标签，而是利用下游任务的性能作为反馈信号，迭代改进压缩策略，以确保压缩内容对任务的有效性。

**技术框架**：CORE的整体架构包括数据预处理、压缩策略生成和性能反馈三个主要模块。首先，对输入文档进行预处理，然后生成压缩策略，最后通过下游任务的性能反馈来优化策略。

**关键创新**：CORE的主要创新在于其无损压缩能力和端到端优化机制，与现有方法的本质区别在于不依赖于固定的压缩标签，而是动态调整压缩策略以适应具体任务需求。

**关键设计**：在设计中，CORE采用了强化学习框架，通过定义合适的奖励函数来引导压缩策略的优化，确保压缩后的内容能够有效支持下游任务。

## 📊 实验亮点

实验结果表明，CORE在压缩比达到3%的情况下，避免了与完整文档相比的性能下降，并且平均准确匹配（EM）得分提高了3.3分，显示出其在提升任务性能方面的显著优势。

## 🎯 应用场景

CORE方法具有广泛的应用潜力，尤其在需要快速更新知识库的对话系统、信息检索和问答系统中，能够显著提高响应速度和准确性。未来，CORE的设计理念也可以扩展到其他需要高效信息处理的领域，如智能助手和自动摘要生成等。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) has emerged as a promising approach to enhance the timeliness of knowledge updates and the factual accuracy of responses in large language models. However, incorporating a large number of retrieved documents significantly increases input length, leading to higher computational costs. Existing approaches to document compression tailored for RAG often degrade task performance, as they typically rely on predefined heuristics in the absence of clear compression guidelines. These heuristics fail to ensure that the compressed content effectively supports downstream tasks. To address these limitations, we propose CORE, a novel method for lossless context compression in RAG. CORE is optimized end-to-end and does not depend on predefined compression labels, which are often impractical to obtain. Instead, it leverages downstream task performance as a feedback signal, iteratively refining the compression policy to enhance task effectiveness. Extensive experiments across four datasets demonstrate the effectiveness of CORE. With a high compression ratio of 3%, CORE not only prevents performance degradation compared to including full documents (i.e., without compression) but also improves the average Exact Match (EM) score by 3.3 points. The code for CORE will be released soon.

