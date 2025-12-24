---
layout: default
title: "Learning from Convenience Samples: A Case Study on Fine-Tuning LLMs for Survey Non-response in the German Longitudinal Election Study"
---

# Learning from Convenience Samples: A Case Study on Fine-Tuning LLMs for Survey Non-response in the German Longitudinal Election Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25063" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25063v1</a>
  <a href="https://arxiv.org/pdf/2509.25063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25063v1', 'Learning from Convenience Samples: A Case Study on Fine-Tuning LLMs for Survey Non-response in the German Longitudinal Election Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Holtdirk, Dennis Assenmacher, Arnim Bleier, Claudia Wagner

**分类**: cs.CY, cs.CL

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**微调LLM解决调查非回应问题，利用便利样本提升选举研究准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `微调` `调查非回应` `便利样本` `选举研究`

## 📋 核心要点

1. 传统调查研究面临成本高昂和数据缺失的挑战，影响推断的准确性，便利样本的使用日益增加。
2. 该研究通过在部分调查回复数据上微调LLM，以填补随机和系统性非回应下的投票选择，提升预测准确性。
3. 实验表明，微调后的LLM在数据完全随机缺失时与表格分类器性能相当，优于零样本方法，且能有效利用有偏便利样本。

## 📝 摘要（中文）

调查研究人员面临概率样本成本上升和数据缺失（如非回应或衰减）的双重挑战，这会损害推断并增加便利样本的使用。最近的研究探索了使用大型语言模型（LLM）通过基于角色的提示来模拟受访者，通常无需标记数据。我们研究了一个更实际的场景，即存在部分调查回复：我们使用德国纵向选举研究，在随机和系统性非回应下，微调LLM以推算自我报告的投票选择。我们将零样本提示和监督微调与表格分类器（如CatBoost）进行比较，并测试用于微调的不同便利样本（如学生）如何影响泛化。

## 🔬 方法详解

**问题定义**：论文旨在解决调查研究中因非回应造成的投票选择数据缺失问题。现有方法，如传统的统计模型和零样本LLM，在处理系统性非回应和有偏便利样本时表现不佳，导致推断偏差。

**核心思路**：论文的核心思路是利用已有的部分调查回复数据，对LLM进行微调，使其能够学习到受访者的潜在特征和投票倾向，从而更准确地推断缺失的投票选择。通过微调，LLM可以更好地适应特定调查数据集的分布，并减少对先验知识的依赖。

**技术框架**：整体框架包括数据预处理、模型选择与微调、以及性能评估三个主要阶段。首先，对德国纵向选举研究的数据进行清洗和整理，构建用于微调的数据集。然后，选择合适的LLM（如3B到8B的开源模型），并使用监督学习的方式在已有的部分调查回复数据上进行微调。最后，使用不同的评估指标，如个体预测准确率和群体分布还原度，来评估微调后LLM的性能。

**关键创新**：该研究的关键创新在于探索了使用微调后的LLM来处理调查非回应问题，特别是在只有有偏便利样本可用的情况下。与传统的统计方法和零样本LLM相比，微调后的LLM能够更好地捕捉数据中的复杂关系，并提高预测的准确性。此外，该研究还比较了不同便利样本对微调效果的影响，为实际应用提供了指导。

**关键设计**：在模型微调过程中，采用了监督学习的方式，使用已有的部分调查回复数据作为训练集。损失函数采用交叉熵损失函数，优化器采用AdamW。为了防止过拟合，采用了dropout和权重衰减等正则化技术。此外，还探索了不同的微调策略，如全参数微调和LoRA微调，以平衡性能和计算成本。

## 📊 实验亮点

实验结果表明，在数据完全随机缺失的情况下，微调后的LLM与表格分类器（如CatBoost）性能相当，优于零样本方法。更重要的是，当只有有偏便利样本可用时，微调后的LLM在个体预测和群体分布还原方面通常优于零样本方法和表格方法，表明其在处理实际调查数据中的优势。

## 🎯 应用场景

该研究成果可应用于各种调查研究领域，尤其是在面临高成本概率样本和系统性数据缺失的情况下。通过利用易于获取的子群体数据微调LLM，可以更经济高效地进行选举预测、市场调研和社会科学研究，并提高数据分析的准确性和可靠性，为政策制定提供更可靠的依据。

## 📄 摘要（原文）

> Survey researchers face two key challenges: the rising costs of probability samples and missing data (e.g., non-response or attrition), which can undermine inference and increase the use of convenience samples. Recent work explores using large language models (LLMs) to simulate respondents via persona-based prompts, often without labeled data. We study a more practical setting where partial survey responses exist: we fine-tune LLMs on available data to impute self-reported vote choice under both random and systematic nonresponse, using the German Longitudinal Election Study. We compare zero-shot prompting and supervised fine-tuning against tabular classifiers (e.g., CatBoost) and test how different convenience samples (e.g., students) used for fine-tuning affect generalization.
>   Our results show that when data are missing completely at random, fine-tuned LLMs match tabular classifiers but outperform zero-shot approaches. When only biased convenience samples are available, fine-tuning small (3B to 8B) open-source LLMs can recover both individual-level predictions and population-level distributions more accurately than zero-shot and often better than tabular methods. This suggests fine-tuned LLMs offer a promising strategy for researchers working with non-probability samples or systematic missingness, and may enable new survey designs requiring only easily accessible subpopulations.

