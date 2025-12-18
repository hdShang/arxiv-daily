---
layout: default
title: Inflation Attitudes of Large Language Models
---

# Inflation Attitudes of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14306" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14306v1</a>
  <a href="https://arxiv.org/pdf/2512.14306.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14306v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14306v1', 'Inflation Attitudes of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikoleta Anesti, Edward Hill, Andreas Joseph

**分类**: cs.CL, econ.EM

**发布日期**: 2025-12-16

**备注**: 41 pages, 11 figures

---

## 💡 一句话要点

**利用大型语言模型GPT-3.5研究通货膨胀感知与预期，模拟人类调查并分析影响因素。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `通货膨胀感知` `经济行为模拟` `Shapley值分解` `准实验设计`

## 📋 核心要点

1. 现有方法难以有效利用LLM模拟人类经济行为，尤其是在通货膨胀感知方面，缺乏细粒度分析。
2. 论文提出一种准实验设计，模拟英国央行调查，利用GPT-3.5的知识截止点，研究其对通胀的感知和预期。
3. 实验表明，GPT在短期内能跟踪调查预测和官方数据，并复现人类在收入、住房等方面的通胀感知规律。

## 📝 摘要（中文）

本文研究了大型语言模型（LLM），特别是GPT-3.5-turbo（GPT），基于宏观经济价格信号形成通货膨胀感知和期望的能力。我们将LLM的输出与家庭调查数据和官方统计数据进行比较，模拟英国央行通货膨胀态度调查（IAS）的信息集和人口特征。我们的准实验设计利用了GPT在2021年9月的训练截止时间，这意味着它不了解随后的英国通货膨胀飙升。我们发现GPT在短期内跟踪总体调查预测和官方统计数据。在分解层面，GPT复制了家庭通货膨胀感知的关键经验规律，特别是在收入、住房保有权和社会阶层方面。一种新颖的Shapley值分解方法适用于合成调查环境，为与提示内容相关的模型输出驱动因素提供了明确的见解。我们发现GPT表现出对食品通货膨胀信息的高度敏感性，类似于人类受访者。然而，我们也发现它缺乏一致的消费者价格通货膨胀模型。更一般地说，我们的方法可以用于评估LLM在社会科学中的行为，比较不同的模型，或协助调查设计。

## 🔬 方法详解

**问题定义**：论文旨在研究大型语言模型（LLM）是否能够像人类一样，基于宏观经济数据形成对通货膨胀的感知和预期。现有方法难以直接评估LLM在经济行为模拟方面的能力，尤其是在缺乏真实世界数据的情况下，难以进行细粒度的分析和验证。

**核心思路**：论文的核心思路是构建一个准实验环境，模拟英国央行的通货膨胀态度调查（IAS）。通过向GPT-3.5输入类似调查问题和宏观经济数据，观察其输出结果与真实调查数据和官方统计数据的匹配程度。利用GPT-3.5的训练截止时间（2021年9月）作为天然的实验控制，评估其对后续通货膨胀飙升的反应。

**技术框架**：整体框架包括以下几个主要阶段：
1. **数据准备**：收集英国央行IAS的调查数据、官方统计数据以及宏观经济指标。
2. **提示工程**：设计合适的提示语，模拟调查问卷，向GPT-3.5提问。
3. **模型推理**：使用GPT-3.5生成通货膨胀感知和预期。
4. **结果分析**：将GPT-3.5的输出与真实调查数据和官方统计数据进行比较，评估其性能。
5. **Shapley值分解**：使用Shapley值分解方法，分析提示内容对模型输出的影响。

**关键创新**：论文的关键创新在于：
1. **准实验设计**：巧妙利用GPT-3.5的知识截止点，构建了一个准实验环境，避免了直接使用真实世界数据带来的偏差。
2. **合成调查环境**：通过提示工程模拟调查问卷，使得能够控制输入信息，进行细粒度的分析。
3. **Shapley值分解**：将Shapley值分解方法应用于LLM的输出分析，揭示了提示内容对模型输出的影响，为理解LLM的决策过程提供了新的视角。

**关键设计**：论文的关键设计包括：
1. **提示语设计**：提示语的设计需要尽可能贴近真实调查问卷，同时包含相关的宏观经济数据。
2. **Shapley值计算**：选择合适的Shapley值计算方法，并针对合成调查环境进行调整。
3. **对比分析**：选择合适的基线方法，例如简单的统计模型，与GPT-3.5的输出进行对比。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14306v1/inflation_time_series.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14306v1/temp-0.0_CV_hist_negative-True.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14306v1/question-present_T-0_hist_negative-True.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GPT-3.5在短期内能够跟踪总体调查预测和官方统计数据，并在收入、住房保有权和社会阶层等维度上复现人类的通货膨胀感知规律。Shapley值分解结果显示，GPT-3.5对食品通货膨胀信息表现出高度敏感性，与人类受访者相似。但同时也发现，GPT-3.5缺乏一致的消费者价格通货膨胀模型。

## 🎯 应用场景

该研究方法可应用于评估LLM在社会科学领域的应用潜力，例如预测消费者行为、分析市场趋势等。此外，该方法还可以用于比较不同LLM的性能，辅助调查问卷设计，提高调查效率和准确性。未来，该研究可以扩展到其他经济指标的预测和分析，为政策制定提供参考。

## 📄 摘要（原文）

> This paper investigates the ability of Large Language Models (LLMs), specifically GPT-3.5-turbo (GPT), to form inflation perceptions and expectations based on macroeconomic price signals. We compare the LLM's output to household survey data and official statistics, mimicking the information set and demographic characteristics of the Bank of England's Inflation Attitudes Survey (IAS). Our quasi-experimental design exploits the timing of GPT's training cut-off in September 2021 which means it has no knowledge of the subsequent UK inflation surge. We find that GPT tracks aggregate survey projections and official statistics at short horizons. At a disaggregated level, GPT replicates key empirical regularities of households' inflation perceptions, particularly for income, housing tenure, and social class. A novel Shapley value decomposition of LLM outputs suited for the synthetic survey setting provides well-defined insights into the drivers of model outputs linked to prompt content. We find that GPT demonstrates a heightened sensitivity to food inflation information similar to that of human respondents. However, we also find that it lacks a consistent model of consumer price inflation. More generally, our approach could be used to evaluate the behaviour of LLMs for use in the social sciences, to compare different models, or to assist in survey design.

