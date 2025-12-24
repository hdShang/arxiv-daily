---
layout: default
title: "DeKeyNLU: Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction"
---

# DeKeyNLU: Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14507" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14507v1</a>
  <a href="https://arxiv.org/pdf/2509.14507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14507v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14507v1', 'DeKeyNLU: Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Chen, Zhenyan Chen, Xuming Hu, Peilin Zhou, Yining Hua, Han Fang, Cissy Hing Yee Choy, Xinmei Ke, Jingfeng Luo, Zixuan Yuan

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**DeKeyNLU：通过任务分解和关键词提取增强自然语言到SQL的生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言到SQL` `NL2SQL` `检索增强生成` `RAG` `任务分解` `关键词提取` `数据集` `微调`

## 📋 核心要点

1. 现有NL2SQL方法在任务分解和关键词提取方面存在不足，导致SQL生成错误，数据集缺乏领域特定关键词注释。
2. 提出DeKeyNLU数据集，包含1500个QA对，用于改进RAG管道的任务分解和关键词提取精度。
3. DeKeySQL通过用户问题理解、实体检索和生成三个模块，显著提升了BIRD和Spider数据集上的SQL生成准确性。

## 📝 摘要（中文）

自然语言到SQL (NL2SQL) 提供了一种以模型为中心的新范式，通过将自然语言查询转换为SQL命令，简化了非技术用户对数据库的访问。最近的进展，特别是那些整合了检索增强生成 (RAG) 和思维链 (CoT) 推理的进展，在提高 NL2SQL 性能方面取得了显著进步。然而，LLM 在任务分解和关键词提取方面的不准确仍然是主要的瓶颈，经常导致 SQL 生成错误。现有的数据集旨在通过微调模型来缓解这些问题，但它们在任务过度碎片化和缺乏领域特定关键词注释方面存在不足，限制了其有效性。为了解决这些限制，我们提出了 DeKeyNLU，这是一个包含 1,500 个精心注释的 QA 对的新数据集，旨在改进 RAG 管道的任务分解并提高关键词提取精度。通过 DeKeyNLU 进行微调，我们提出了 DeKeySQL，这是一个基于 RAG 的 NL2SQL 管道，它采用三个不同的模块进行用户问题理解、实体检索和生成，以提高 SQL 生成的准确性。我们对 DeKeySQL RAG 管道中的多个模型配置进行了基准测试。实验结果表明，使用 DeKeyNLU 进行微调可以显著提高 BIRD（62.31% 到 69.10%）和 Spider（84.2% 到 88.7%）开发数据集上的 SQL 生成准确性。

## 🔬 方法详解

**问题定义**：论文旨在解决自然语言到SQL生成任务中，大型语言模型（LLM）在任务分解和关键词提取方面表现不佳的问题。现有方法在处理复杂查询时，容易出现任务分解不准确和关键词提取遗漏，导致生成的SQL语句错误率较高。此外，现有数据集在任务标注上存在过度碎片化的问题，并且缺乏针对特定领域的关键词标注，限制了模型的泛化能力。

**核心思路**：论文的核心思路是通过构建高质量的标注数据集DeKeyNLU，并基于此微调RAG（Retrieval-Augmented Generation）模型，从而提升模型在任务分解和关键词提取方面的能力。DeKeyNLU数据集专注于提供更准确的任务分解和领域相关的关键词标注，从而引导模型学习更有效的SQL生成策略。

**技术框架**：DeKeySQL是一个基于RAG的NL2SQL流水线，包含三个主要模块：用户问题理解模块、实体检索模块和SQL生成模块。用户问题理解模块负责解析用户输入的自然语言查询，提取关键信息。实体检索模块根据提取的信息，从数据库模式中检索相关的表、列等实体。SQL生成模块则利用检索到的实体和用户查询，生成最终的SQL语句。

**关键创新**：论文的关键创新在于DeKeyNLU数据集的构建，它提供了更细粒度、更准确的任务分解和关键词标注，能够有效提升RAG模型在NL2SQL任务中的性能。此外，DeKeySQL流水线通过模块化的设计，将NL2SQL任务分解为更小的子任务，从而降低了模型的学习难度。

**关键设计**：DeKeyNLU数据集的标注过程经过精心设计，确保标注的准确性和一致性。具体来说，标注人员需要对每个QA对进行任务分解，并标注出与SQL生成相关的关键词。在模型训练方面，论文采用了微调策略，使用DeKeyNLU数据集对预训练的RAG模型进行微调，从而使其更好地适应NL2SQL任务。论文中没有提及具体的损失函数或网络结构等技术细节。

## 📊 实验亮点

实验结果表明，使用DeKeyNLU数据集进行微调后，DeKeySQL在BIRD数据集上的SQL生成准确率从62.31%提升至69.10%，在Spider数据集上的准确率从84.2%提升至88.7%。这些结果表明，DeKeyNLU数据集能够显著提升RAG模型在NL2SQL任务中的性能。

## 🎯 应用场景

该研究成果可应用于智能数据库助手、自然语言查询接口等领域，使用户能够通过自然语言与数据库进行交互，无需掌握复杂的SQL语法。这对于非技术人员访问和分析数据具有重要意义，可以降低数据分析的门槛，提高工作效率，并促进数据驱动的决策。

## 📄 摘要（原文）

> Natural Language to SQL (NL2SQL) provides a new model-centric paradigm that simplifies database access for non-technical users by converting natural language queries into SQL commands. Recent advancements, particularly those integrating Retrieval-Augmented Generation (RAG) and Chain-of-Thought (CoT) reasoning, have made significant strides in enhancing NL2SQL performance. However, challenges such as inaccurate task decomposition and keyword extraction by LLMs remain major bottlenecks, often leading to errors in SQL generation. While existing datasets aim to mitigate these issues by fine-tuning models, they struggle with over-fragmentation of tasks and lack of domain-specific keyword annotations, limiting their effectiveness. To address these limitations, we present DeKeyNLU, a novel dataset which contains 1,500 meticulously annotated QA pairs aimed at refining task decomposition and enhancing keyword extraction precision for the RAG pipeline. Fine-tuned with DeKeyNLU, we propose DeKeySQL, a RAG-based NL2SQL pipeline that employs three distinct modules for user question understanding, entity retrieval, and generation to improve SQL generation accuracy. We benchmarked multiple model configurations within DeKeySQL RAG pipeline. Experimental results demonstrate that fine-tuning with DeKeyNLU significantly improves SQL generation accuracy on both BIRD (62.31% to 69.10%) and Spider (84.2% to 88.7%) dev datasets.

