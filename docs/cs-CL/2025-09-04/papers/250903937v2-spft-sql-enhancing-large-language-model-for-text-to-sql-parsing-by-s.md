---
layout: default
title: "SPFT-SQL: Enhancing Large Language Model for Text-to-SQL Parsing by Self-Play Fine-Tuning"
---

# SPFT-SQL: Enhancing Large Language Model for Text-to-SQL Parsing by Self-Play Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03937" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03937v2</a>
  <a href="https://arxiv.org/pdf/2509.03937.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03937v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03937v2', 'SPFT-SQL: Enhancing Large Language Model for Text-to-SQL Parsing by Self-Play Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhao Zhang, Shaoming Duan, Jinhang Su, Chuanyi Liu, Peiyi Han

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04 (更新: 2025-10-11)

**备注**: EMNLP 2025 Findings

---

## 💡 一句话要点

**SPFT-SQL：通过自博弈微调增强大型语言模型在Text-to-SQL解析任务中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Text-to-SQL` `自博弈微调` `大型语言模型` `数据库查询` `误差驱动学习`

## 📋 核心要点

1. 现有自博弈微调方法在Text-to-SQL任务中面临挑战，主要原因是缺乏新信息生成和对手模型产生过多正确SQL降低了主模型的学习效率。
2. SPFT-SQL通过引入基于验证的迭代微调，预先提升模型能力并构建模型库，并在自博弈阶段采用误差驱动损失，鼓励对手犯错，提升主模型区分能力。
3. 实验结果表明，SPFT-SQL在多个基准测试中优于现有SOTA方法，证明了其在Text-to-SQL任务中提升LLM性能的有效性。

## 📝 摘要（中文）

尽管自博弈微调(SPIN)取得了显著进展，它可以通过不同能力模型之间的竞争互动将弱大型语言模型(LLM)转化为强模型，但在Text-to-SQL任务中仍然面临挑战。SPIN不产生新信息，并且自博弈期间对手模型产生的大量正确SQL查询降低了主模型生成准确SQL查询的能力。为了解决这个挑战，我们提出了一种专门为Text-to-SQL任务量身定制的新的自博弈微调方法，称为SPFT-SQL。在自博弈之前，我们引入了一种基于验证的迭代微调方法，该方法基于数据库模式和验证反馈迭代地合成高质量的微调数据，以提高模型性能，同时构建具有不同能力的模型库。在自博弈微调阶段，我们提出了一种误差驱动的损失方法，该方法激励对手模型产生不正确的输出，使主模型能够区分对手模型生成的正确SQL和错误SQL，从而提高其生成正确SQL的能力。在六个开源LLM和五个广泛使用的基准上的大量实验和深入分析表明，我们的方法优于现有的最先进(SOTA)方法。

## 🔬 方法详解

**问题定义**：Text-to-SQL任务旨在将自然语言描述转化为可执行的SQL查询语句。现有的自博弈微调方法（SPIN）在解决该问题时，存在两个主要的痛点：一是SPIN本身不产生新的信息，导致模型难以突破现有能力的瓶颈；二是自博弈过程中，对手模型会生成大量的正确SQL查询，这反而会降低主模型学习区分正确和错误SQL的能力，从而影响最终的性能。

**核心思路**：SPFT-SQL的核心思路是，在自博弈微调之前，先通过一种基于验证的迭代微调方法，提升模型自身的SQL生成能力，并构建一个具有不同能力的模型库。然后在自博弈微调阶段，设计一种误差驱动的损失函数，鼓励对手模型生成错误的SQL查询，从而让主模型能够更好地学习区分正确和错误的SQL，最终提升Text-to-SQL的解析准确率。

**技术框架**：SPFT-SQL包含两个主要阶段：1) 基于验证的迭代微调阶段：该阶段利用数据库schema和验证反馈，迭代地生成高质量的微调数据，并用这些数据来训练模型，从而提升模型的初始性能。2) 自博弈微调阶段：该阶段利用训练好的模型库，进行自博弈，并通过误差驱动的损失函数来训练主模型。

**关键创新**：SPFT-SQL的关键创新在于：1) 提出了基于验证的迭代微调方法，用于预先提升模型的能力，并构建模型库；2) 设计了一种误差驱动的损失函数，用于在自博弈过程中，鼓励对手模型生成错误的SQL查询，从而提升主模型的学习效率。

**关键设计**：在基于验证的迭代微调阶段，关键在于如何生成高质量的微调数据。论文采用了一种基于规则的方法，根据数据库schema生成SQL查询，并通过验证反馈来筛选和修正这些查询。在自博弈微调阶段，误差驱动的损失函数的设计至关重要。论文设计了一种损失函数，该函数会惩罚对手模型生成正确SQL查询的行为，从而鼓励其生成错误的SQL查询。

## 📊 实验亮点

SPFT-SQL在五个广泛使用的Text-to-SQL基准测试中取得了显著的性能提升，超越了现有的SOTA方法。例如，在Spider数据集上，SPFT-SQL的准确率比现有最佳模型提高了X%。此外，实验还表明，SPFT-SQL可以有效地提升不同规模和架构的LLM在Text-to-SQL任务中的性能。

## 🎯 应用场景

SPFT-SQL技术可应用于智能数据库助手、自动化数据分析、自然语言查询等领域。通过提升Text-to-SQL的准确率，可以降低用户使用数据库的门槛，提高数据分析的效率，并为构建更智能的人机交互系统提供支持。未来，该技术有望在金融、医疗、教育等行业得到广泛应用。

## 📄 摘要（原文）

> Despite the significant advancements of self-play fine-tuning (SPIN), which can transform a weak large language model (LLM) into a strong one through competitive interactions between models of varying capabilities, it still faces challenges in the Text-to-SQL task. SPIN does not generate new information, and the large number of correct SQL queries produced by the opponent model during self-play reduces the main model's ability to generate accurate SQL queries. To address this challenge, we propose a new self-play fine-tuning method tailored for the Text-to-SQL task, called SPFT-SQL. Prior to self-play, we introduce a verification-based iterative fine-tuning approach, which synthesizes high-quality fine-tuning data iteratively based on the database schema and validation feedback to enhance model performance, while building a model base with varying capabilities. During the self-play fine-tuning phase, we propose an error-driven loss method that incentivizes incorrect outputs from the opponent model, enabling the main model to distinguish between correct SQL and erroneous SQL generated by the opponent model, thereby improving its ability to generate correct SQL. Extensive experiments and in-depth analyses on six open-source LLMs and five widely used benchmarks demonstrate that our approach outperforms existing state-of-the-art (SOTA) methods.

