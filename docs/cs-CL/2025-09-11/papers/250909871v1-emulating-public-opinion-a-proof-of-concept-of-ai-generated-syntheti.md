---
layout: default
title: "Emulating Public Opinion: A Proof-of-Concept of AI-Generated Synthetic Survey Responses for the Chilean Case"
---

# Emulating Public Opinion: A Proof-of-Concept of AI-Generated Synthetic Survey Responses for the Chilean Case

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09871" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09871v1</a>
  <a href="https://arxiv.org/pdf/2509.09871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09871v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09871v1', 'Emulating Public Opinion: A Proof-of-Concept of AI-Generated Synthetic Survey Responses for the Chilean Case')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bastián González-Bustamante, Nando Verelst, Carla Cisternas

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-11

**备注**: Working paper: 18 pages, 4 tables, 2 figures

**期刊**: Empiria Lab Method Series (2025)

**DOI**: [10.5281/zenodo.17077752](https://doi.org/10.5281/zenodo.17077752)

---

## 💡 一句话要点

**利用大型语言模型生成合成调查回复，模拟智利公众意见，验证其可行性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `合成数据` `调查研究` `公众意见` `偏差分析`

## 📋 核心要点

1. 现有调查研究存在测量和表示误差，难以准确反映公众意见。
2. 利用大型语言模型生成合成调查回复，模拟人类行为，以期降低误差。
3. 实验表明，合成回复在信任项目上表现出色，但捕捉全部细微差别仍具挑战。

## 📝 摘要（中文）

大型语言模型(LLMs)通过使用合成受访者来模拟人类的回答和行为，为调查研究中的方法论和应用创新提供了有希望的途径，有可能减轻测量和表示误差。然而，LLMs在多大程度上能够恢复聚合项目分布仍然不确定，并且下游应用可能重现从训练数据中继承的社会刻板印象和偏见。我们评估了LLM生成的合成调查回复相对于来自智利公众意见概率调查的真实人类回复的可靠性。具体来说，我们对128个提示-模型-问题三元组进行基准测试，生成189,696个合成配置文件，并在128个问题-子样本对中汇集性能指标（即，准确率、精确率、召回率和F1分数）进行元分析，以测试沿关键社会人口维度存在的偏差。评估范围涵盖OpenAI的GPT系列和o系列推理模型，以及Llama和Qwen检查点。三个结果很突出。首先，合成回复在信任项目上取得了优异的性能（F1分数和准确率>0.90）。其次，GPT-4o、GPT-4o-mini和Llama 4 Maverick在此任务上的表现相当。第三，合成-人类对齐在45-59岁的受访者中最高。总的来说，基于LLM的合成样本近似于来自概率样本的回复，尽管项目层面的异质性很大。捕捉公众意见的全部细微差别仍然具有挑战性，需要仔细校准和额外的分布测试，以确保算法的保真度并减少误差。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型（LLMs）生成合成调查回复的可靠性，并分析其在模拟公众意见方面的能力。现有方法难以准确捕捉公众意见的细微差别，并且可能存在测量和表示误差。此外，LLMs可能继承训练数据中的社会刻板印象和偏见，导致结果失真。

**核心思路**：论文的核心思路是使用LLMs生成合成的调查回复，并将其与真实的人类回复进行比较，从而评估LLMs在多大程度上能够准确地模拟公众意见。通过对不同LLM模型、不同问题类型以及不同社会人口群体进行分析，可以识别潜在的偏差和误差来源，并为未来的研究提供指导。

**技术框架**：该研究的技术框架主要包括以下几个阶段：
1.  **数据收集**：收集来自智利公众意见概率调查的真实人类回复数据。
2.  **提示工程**：设计不同的提示，用于引导LLMs生成合成回复。
3.  **模型生成**：使用不同的LLMs（例如，GPT-4o, GPT-4o-mini, Llama 4 Maverick, Qwen）生成合成的调查回复。
4.  **性能评估**：使用准确率、精确率、召回率和F1分数等指标，将合成回复与真实回复进行比较，评估LLMs的性能。
5.  **偏差分析**：分析不同社会人口群体之间的性能差异，识别潜在的偏差。
6.  **元分析**：对多个问题-子样本对的性能指标进行元分析，以获得更全面的评估结果。

**关键创新**：该研究的关键创新在于：
1.  系统地评估了多种LLMs在生成合成调查回复方面的能力。
2.  对合成回复的性能进行了全面的评估，包括准确率、精确率、召回率和F1分数等指标。
3.  深入分析了不同社会人口群体之间的性能差异，识别了潜在的偏差。
4.  提出了使用元分析方法来评估LLMs性能的思路。

**关键设计**：
1.  **提示设计**：设计了128个提示-模型-问题三元组，以探索不同提示对LLMs性能的影响。
2.  **模型选择**：选择了OpenAI的GPT系列和o系列推理模型，以及Llama和Qwen检查点，以涵盖不同的LLM架构和训练数据。
3.  **评估指标**：使用了准确率、精确率、召回率和F1分数等指标，以全面评估LLMs的性能。
4.  **偏差分析**：按年龄等社会人口维度对结果进行分组，以识别潜在的偏差。

## 📊 实验亮点

实验结果表明，合成回复在信任项目上取得了优异的性能（F1分数和准确率>0.90）。GPT-4o、GPT-4o-mini和Llama 4 Maverick在此任务上的表现相当。合成-人类对齐在45-59岁的受访者中最高。总体而言，基于LLM的合成样本近似于来自概率样本的回复，但项目层面的异质性仍然存在。

## 🎯 应用场景

该研究成果可应用于社会科学研究、市场调研、政策制定等领域。通过使用LLM生成合成调查回复，可以降低调查成本，扩大样本规模，并减轻测量和表示误差。此外，该研究还可以帮助识别和纠正LLM中的偏差，提高其在社会科学领域的应用价值。未来，该技术有望用于预测公众舆论、评估政策效果以及模拟社会行为。

## 📄 摘要（原文）

> Large Language Models (LLMs) offer promising avenues for methodological and applied innovations in survey research by using synthetic respondents to emulate human answers and behaviour, potentially mitigating measurement and representation errors. However, the extent to which LLMs recover aggregate item distributions remains uncertain and downstream applications risk reproducing social stereotypes and biases inherited from training data. We evaluate the reliability of LLM-generated synthetic survey responses against ground-truth human responses from a Chilean public opinion probabilistic survey. Specifically, we benchmark 128 prompt-model-question triplets, generating 189,696 synthetic profiles, and pool performance metrics (i.e., accuracy, precision, recall, and F1-score) in a meta-analysis across 128 question-subsample pairs to test for biases along key sociodemographic dimensions. The evaluation spans OpenAI's GPT family and o-series reasoning models, as well as Llama and Qwen checkpoints. Three results stand out. First, synthetic responses achieve excellent performance on trust items (F1-score and accuracy > 0.90). Second, GPT-4o, GPT-4o-mini and Llama 4 Maverick perform comparably on this task. Third, synthetic-human alignment is highest among respondents aged 45-59. Overall, LLM-based synthetic samples approximate responses from a probabilistic sample, though with substantial item-level heterogeneity. Capturing the full nuance of public opinion remains challenging and requires careful calibration and additional distributional tests to ensure algorithmic fidelity and reduce errors.

