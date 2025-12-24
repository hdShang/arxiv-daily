---
layout: default
title: "GradeSQL: Test-Time Inference with Outcome Reward Models for Text-to-SQL Generation from Large Language Models"
---

# GradeSQL: Test-Time Inference with Outcome Reward Models for Text-to-SQL Generation from Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01308" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01308v2</a>
  <a href="https://arxiv.org/pdf/2509.01308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01308v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01308v2', 'GradeSQL: Test-Time Inference with Outcome Reward Models for Text-to-SQL Generation from Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mattia Tritto, Giuseppe Farano, Dario Di Palma, Gaetano Rossiello, Fedelucio Narducci, Dharmashankar Subramanian, Tommaso Di Noia

**分类**: cs.AI, cs.CL, cs.DB

**发布日期**: 2025-09-01 (更新: 2025-10-29)

---

## 💡 一句话要点

**提出GradeSQL：利用Outcome Reward Models提升大语言模型Text-to-SQL生成性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Text-to-SQL` `大语言模型` `Outcome Reward Model` `测试时推理` `语义正确性`

## 📋 核心要点

1. 现有Text-to-SQL方法在处理复杂查询时存在困难，传统的Best-of-N和Majority Voting等方法依赖于表面启发式，效果有限。
2. 本文提出利用Outcome Reward Models (ORMs) 作为测试时启发式方法，通过语义正确性评估生成SQL的效用，提升模型对齐。
3. 实验结果表明，ORMs在BIRD和Spider数据集上优于现有方法，执行准确率分别提升了+4.33%和+2.10%。

## 📝 摘要（中文）

本文针对大语言模型(LLMs)在Text-to-SQL任务中处理复杂查询时表现不佳的问题，提出了一种基于Outcome Reward Models (ORMs)的测试时推理框架GradeSQL。尽管LLMs在生成有效SQL方面取得了显著进展，但现有方法如Best-of-N (BoN)和Majority Voting (Maj)依赖于表面启发式方法。本文提出将ORMs作为一种新的测试时启发式方法，并构建了一个统一的框架来训练针对Text-to-SQL任务定制的ORMs。实验结果表明，ORMs在BIRD和Spider数据集上优于ex-BoN和Maj，在执行准确率方面分别提升了+4.33%和+2.10%。此外，对OmniSQL等已对齐SQL生成的模型进行微调，可获得更优的ORM性能。ORMs在简单查询上表现出色，并且相比ex-BoN和Maj，能从更多的候选查询中获益。

## 🔬 方法详解

**问题定义**：Text-to-SQL任务旨在将自然语言问题转换为SQL查询。现有的大语言模型在处理复杂查询时，生成的SQL查询的准确率仍然较低。传统的Best-of-N (BoN) 和 Majority Voting (Maj) 等测试时策略，依赖于语法正确性或频率等表面信息，无法有效区分语义上正确的查询。

**核心思路**：本文的核心思路是利用Outcome Reward Models (ORMs) 来评估生成的SQL查询的语义正确性，并将其作为一种新的测试时启发式方法。通过训练ORMs，使其能够根据SQL查询的执行结果（outcome）来预测其奖励（reward），从而选择更优的查询。

**技术框架**：该框架包含以下主要步骤：1) 使用大语言模型生成N个候选SQL查询；2) 使用数据库执行这些查询，获取执行结果；3) 使用训练好的ORM模型对每个查询的执行结果进行评分；4) 选择得分最高的查询作为最终结果。该框架可以与不同的基础大语言模型相结合，并利用Best-of-N策略进行测试时推理。

**关键创新**：本文最重要的技术创新点在于将Outcome Reward Models应用于Text-to-SQL任务的测试时推理。与传统的基于表面信息的启发式方法不同，ORM能够学习SQL查询的语义信息，从而更准确地评估查询的正确性。此外，本文还提出了一个统一的框架来训练针对Text-to-SQL任务定制的ORMs。

**关键设计**：ORM模型的训练需要构造正负样本。正样本通常是与自然语言问题对应的正确SQL查询及其执行结果，负样本可以是随机生成的SQL查询或由大语言模型生成的错误查询及其执行结果。损失函数可以使用二元交叉熵损失或排序损失等。模型的输入可以是SQL查询的执行结果的向量化表示，输出是该查询的奖励得分。关键参数包括ORM模型的结构（例如，Transformer模型）和训练数据规模。

## 📊 实验亮点

实验结果表明，本文提出的基于ORMs的测试时推理方法在BIRD和Spider数据集上均优于现有的ex-BoN和Maj方法。在BIRD数据集上，ORMs的执行准确率比ex-BoN提高了4.33%，比Maj提高了2.91%。在Spider数据集上，ORMs的执行准确率比ex-BoN提高了2.10%，比Maj提高了0.93%。此外，对OmniSQL等已对齐SQL生成的模型进行微调，可获得更优的ORM性能。

## 🎯 应用场景

该研究成果可应用于各种需要将自然语言转换为SQL查询的场景，例如智能数据库助手、数据分析平台等。通过提高Text-to-SQL的准确率，可以降低用户使用数据库的门槛，使更多用户能够方便地访问和分析数据。未来，该方法可以进一步扩展到其他自然语言生成任务中。

## 📄 摘要（原文）

> Text-to-SQL, the task of translating natural language questions into SQL queries, has significantly advanced with the introduction of Large Language Models (LLMs), broadening database accessibility for a wide range of users. Despite substantial progress in generating valid SQL, current LLMs still struggle with complex queries. To address this limitation, test-time strategies such as Best-of-N (BoN) and Majority Voting (Maj) are often employed, based on the assumption that LLMs can produce correct answers after multiple attempts. However, these methods rely on surface-level heuristics, selecting the syntactically correct query through execution-based BoN (ex-BoN) or the most frequently generated one through Majority Voting. Recently, Outcome Reward Models (ORMs), which assign utility scores to generated outputs based on semantic correctness, have emerged as a promising reinforcement learning approach for improving model alignment. We argue that ORMs could serve as an effective new test-time heuristic, although their application in this context remains largely underexplored.
>   In this work, we propose a unified framework for training ORMs tailored to the Text-to-SQL task and assess their effectiveness as a test-time heuristic within the BoN strategy. We benchmark ORMs against ex-BoN and Maj across the BIRD and Spider datasets, fine-tuning diverse open-source LLMs from the Qwen2, Granite3, and Llama3 families. Results show that ORMs outperform ex-BoN and Maj, achieving execution accuracy gains of +4.33% (BIRD) and +2.10% (Spider) over ex-BoN, and +2.91% (BIRD) and +0.93% (Spider) over Maj. We further demonstrate that finetuning models already aligned with SQL generation, such as OmniSQL, yields superior ORM performance. Additionally, we observe that ORMs achieve competitive results on simple queries and benefit more from an increased number of candidates compared to ex-BoN and Maj.

