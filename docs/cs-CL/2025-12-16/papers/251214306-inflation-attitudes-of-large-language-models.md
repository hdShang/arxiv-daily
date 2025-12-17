---
layout: default
title: Inflation Attitudes of Large Language Models
---

# Inflation Attitudes of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14306" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14306</a>
  <a href="https://arxiv.org/pdf/2512.14306.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14306" onclick="toggleFavorite(this, '2512.14306', 'Inflation Attitudes of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikoleta Anesti, Edward Hill, Andreas Joseph

**分类**: cs.CL, econ.EM

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**利用大型语言模型GPT-3.5研究通货膨胀感知与预期，并与人类调查数据对比。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `通货膨胀感知` `通货膨胀预期` `社会科学` `Shapley值` `GPT-3.5` `调查模拟`

## 📋 核心要点

1. 现有方法难以有效模拟和预测个体对通货膨胀的感知和预期，缺乏细粒度分析。
2. 利用GPT-3.5，通过模拟调查环境，研究LLM对宏观经济信号的反应，并与人类数据对比。
3. 实验表明，GPT在短期内能跟踪总体预测，并在收入、住房等方面重现人类通胀感知的规律。

## 📝 摘要（中文）

本文研究了大型语言模型（LLM），特别是GPT-3.5-turbo（GPT），基于宏观经济价格信号形成通货膨胀感知和期望的能力。我们将LLM的输出与家庭调查数据和官方统计数据进行比较，模拟英国央行通货膨胀态度调查（IAS）的信息集和人口特征。我们的准实验设计利用了GPT在2021年9月的训练截止时间，这意味着它不了解随后的英国通货膨胀飙升。我们发现GPT在短期内跟踪总体调查预测和官方统计数据。在分解层面，GPT复制了家庭通货膨胀感知的关键经验规律，特别是在收入、住房保有权和社会阶层方面。一种新颖的Shapley值分解方法适用于合成调查环境，为与提示内容相关的模型输出驱动因素提供了明确的见解。我们发现GPT表现出对食品通货膨胀信息的高度敏感性，类似于人类受访者。然而，我们也发现它缺乏一致的消费者价格通货膨胀模型。更广泛地说，我们的方法可以用于评估LLM在社会科学中的行为，比较不同的模型，或协助调查设计。

## 🔬 方法详解

**问题定义**：论文旨在研究大型语言模型（LLM）是否能够像人类一样，基于宏观经济数据形成对通货膨胀的感知和预期。现有方法主要依赖于传统的经济模型和调查数据，难以捕捉个体差异，且成本较高。此外，缺乏对LLM在社会科学领域应用的系统性评估。

**核心思路**：核心思路是将LLM（GPT-3.5）视为一个“合成受访者”，通过向其输入类似人类调查问卷的提示，模拟人类在通货膨胀态度调查中的行为。通过对比LLM的输出与真实调查数据和官方统计数据，评估LLM在通货膨胀感知和预期方面的能力。利用GPT训练截止日期（2021年9月）的天然分割，模拟LLM对未知通胀事件的反应。

**技术框架**：整体框架包括以下几个阶段：1) 数据准备：收集英国央行通货膨胀态度调查（IAS）数据和官方统计数据。2) 提示工程：设计针对GPT-3.5的提示，模拟IAS问卷，并考虑不同的信息集和人口特征。3) 模型推理：使用GPT-3.5生成通货膨胀感知和预期数据。4) 结果分析：对比GPT-3.5的输出与真实调查数据和官方统计数据，评估其性能。5) Shapley值分解：使用Shapley值分解方法，分析提示内容对模型输出的影响。

**关键创新**：主要创新点在于：1) 将LLM应用于通货膨胀感知和预期研究，开辟了新的研究方向。2) 提出了一个基于Shapley值分解的分析框架，用于理解LLM在合成调查环境中的行为。3) 利用GPT的训练截止日期，进行了一个准实验设计，评估LLM对未知事件的反应。

**关键设计**：关键设计包括：1) 提示的设计，需要尽可能模拟真实调查问卷，并考虑不同的信息集和人口特征。2) Shapley值分解方法的应用，需要针对合成调查环境进行调整，以获得对模型输出驱动因素的有效解释。3) 对比指标的选择，需要选择合适的指标来评估LLM的性能，例如均方误差、相关系数等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14306/inflation_time_series.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14306/temp-0.0_CV_hist_negative-True.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14306/question-present_T-0_hist_negative-True.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GPT-3.5在短期内能够跟踪总体调查预测和官方统计数据。在分解层面，GPT-3.5能够重现人类通货膨胀感知的关键经验规律，特别是在收入、住房保有权和社会阶层方面。Shapley值分解结果表明，GPT-3.5对食品通货膨胀信息表现出高度敏感性，与人类受访者相似。但GPT-3.5缺乏一致的消费者价格通货膨胀模型。

## 🎯 应用场景

该研究具有广泛的应用前景，可用于：1) 评估LLM在社会科学领域的应用潜力。2) 比较不同LLM的性能。3) 辅助调查设计，例如优化问卷内容和抽样策略。4) 构建更准确的通货膨胀预测模型，为政策制定提供参考。5) 模拟和预测其他社会经济现象，例如消费者行为、市场情绪等。

## 📄 摘要（原文）

> This paper investigates the ability of Large Language Models (LLMs), specifically GPT-3.5-turbo (GPT), to form inflation perceptions and expectations based on macroeconomic price signals. We compare the LLM's output to household survey data and official statistics, mimicking the information set and demographic characteristics of the Bank of England's Inflation Attitudes Survey (IAS). Our quasi-experimental design exploits the timing of GPT's training cut-off in September 2021 which means it has no knowledge of the subsequent UK inflation surge. We find that GPT tracks aggregate survey projections and official statistics at short horizons. At a disaggregated level, GPT replicates key empirical regularities of households' inflation perceptions, particularly for income, housing tenure, and social class. A novel Shapley value decomposition of LLM outputs suited for the synthetic survey setting provides well-defined insights into the drivers of model outputs linked to prompt content. We find that GPT demonstrates a heightened sensitivity to food inflation information similar to that of human respondents. However, we also find that it lacks a consistent model of consumer price inflation. More generally, our approach could be used to evaluate the behaviour of LLMs for use in the social sciences, to compare different models, or to assist in survey design.

