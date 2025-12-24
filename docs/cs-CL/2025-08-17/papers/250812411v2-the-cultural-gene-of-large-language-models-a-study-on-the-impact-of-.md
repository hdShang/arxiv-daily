---
layout: default
title: "The Cultural Gene of Large Language Models: A Study on the Impact of Cross-Corpus Training on Model Values and Biases"
---

# The Cultural Gene of Large Language Models: A Study on the Impact of Cross-Corpus Training on Model Values and Biases

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12411" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12411v2</a>
  <a href="https://arxiv.org/pdf/2508.12411.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12411v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12411v2', 'The Cultural Gene of Large Language Models: A Study on the Impact of Cross-Corpus Training on Model Values and Biases')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Emanuel Z. Fenech-Borg, Tilen P. Meznaric-Kos, Milica D. Lekovic-Bojovic, Arni J. Hentze-Djurhuus

**分类**: cs.CL

**发布日期**: 2025-08-17 (更新: 2025-10-14)

**备注**: 10 pages, 5 figures, IEEE conference format, submitted to [Conference Name]

---

## 💡 一句话要点

**提出文化基因概念以探讨大语言模型的文化偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `文化基因` `文化偏见` `跨文化研究` `算法伦理` `自然语言处理` `文化对齐指数`

## 📋 核心要点

1. 现有的大语言模型在文化和伦理假设方面的研究相对不足，导致模型可能存在文化偏见。
2. 本文提出了“文化基因”概念，利用文化探测数据集（CPD）对模型的文化价值取向进行系统性分析。
3. 实验结果表明，GPT-4与美国文化更为一致，而ERNIE Bot则与中国文化更为一致，差异具有统计学意义。

## 📝 摘要（中文）

大语言模型（LLMs）在全球范围内被广泛应用，但其潜在的文化和伦理假设尚未得到充分探讨。本文提出了“文化基因”这一概念，指LLMs从训练语料中继承的系统性价值取向，并引入了一个包含200个提示的文化探测数据集（CPD），针对个人主义-集体主义（IDV）和权力距离（PDI）两个经典跨文化维度进行研究。通过标准化的零样本提示，比较了以西方为中心的模型（GPT-4）和以东方为中心的模型（ERNIE Bot），结果显示两者在这两个维度上存在显著差异。GPT-4表现出个人主义和低权力距离的倾向，而ERNIE Bot则表现出集体主义和高权力距离的倾向。我们的研究结果支持LLMs作为其文化语料的统计镜像的观点，并强调在评估和部署时需考虑文化因素，以避免算法文化霸权。

## 🔬 方法详解

**问题定义**：本文旨在探讨大语言模型在训练过程中如何继承文化价值观及其对模型输出的影响。现有方法未能充分揭示模型的文化偏见，导致其在不同文化背景下的表现不一致。

**核心思路**：论文提出“文化基因”概念，认为LLMs的价值取向源于其训练语料的文化背景，并通过文化探测数据集（CPD）对不同文化背景下的模型进行比较分析。

**技术框架**：研究采用标准化的零样本提示，通过对比分析西方模型（GPT-4）和东方模型（ERNIE Bot）在个人主义-集体主义和权力距离两个维度上的表现，构建文化对齐指数（CAI）进行量化评估。

**关键创新**：本文的创新在于引入“文化基因”这一概念，并通过系统性的方法评估模型的文化偏见，填补了现有研究的空白。

**关键设计**：研究中使用了200个提示的文化探测数据集，采用标准化的评分方法进行人类注释，并计算文化对齐指数（CAI）与霍夫斯泰德国家评分进行比较。

## 📊 实验亮点

实验结果显示，GPT-4在个人主义（IDV）和低权力距离（PDI）方面的得分分别为约1.21和-1.05，而ERNIE Bot则在这两个维度上得分分别为约-0.89和0.76，差异具有统计学意义（p < 0.001）。这表明两种模型在文化价值取向上存在显著差异。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、跨文化交流和人工智能伦理等。通过理解和评估大语言模型的文化偏见，开发者可以在模型设计和应用中更加注重文化敏感性，从而提高模型在不同文化背景下的适用性和公平性。

## 📄 摘要（原文）

> Large language models (LLMs) are deployed globally, yet their underlying cultural and ethical assumptions remain underexplored. We propose the notion of a "cultural gene" -- a systematic value orientation that LLMs inherit from their training corpora -- and introduce a Cultural Probe Dataset (CPD) of 200 prompts targeting two classic cross-cultural dimensions: Individualism-Collectivism (IDV) and Power Distance (PDI). Using standardized zero-shot prompts, we compare a Western-centric model (GPT-4) and an Eastern-centric model (ERNIE Bot). Human annotation shows significant and consistent divergence across both dimensions. GPT-4 exhibits individualistic and low-power-distance tendencies (IDV score approx 1.21; PDI score approx -1.05), while ERNIE Bot shows collectivistic and higher-power-distance tendencies (IDV approx -0.89; PDI approx 0.76); differences are statistically significant (p < 0.001). We further compute a Cultural Alignment Index (CAI) against Hofstede's national scores and find GPT-4 aligns more closely with the USA (e.g., IDV CAI approx 0.91; PDI CAI approx 0.88) whereas ERNIE Bot aligns more closely with China (IDV CAI approx 0.85; PDI CAI approx 0.81). Qualitative analyses of dilemma resolution and authority-related judgments illustrate how these orientations surface in reasoning. Our results support the view that LLMs function as statistical mirrors of their cultural corpora and motivate culturally aware evaluation and deployment to avoid algorithmic cultural hegemony.

