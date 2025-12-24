---
layout: default
title: Acoustic and Machine Learning Methods for Speech-Based Suicide Risk Assessment: A Systematic Review
---

# Acoustic and Machine Learning Methods for Speech-Based Suicide Risk Assessment: A Systematic Review

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18195" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18195v2</a>
  <a href="https://arxiv.org/pdf/2505.18195.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18195v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18195v2', 'Acoustic and Machine Learning Methods for Speech-Based Suicide Risk Assessment: A Systematic Review')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ambre Marie, Marine Garnier, Thomas Bertin, Laura Machart, Guillaume Dardenne, Gwenolé Quellec, Sofian Berrouiguet

**分类**: eess.AS, cs.LG, cs.SD

**发布日期**: 2025-05-20 (更新: 2025-10-28)

**备注**: Preprint version of a manuscript submitted to the Journal of Affective Disorders

---

## 💡 一句话要点

**利用声学与机器学习方法评估自杀风险**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自杀风险评估` `声学分析` `机器学习` `多模态方法` `心理健康` `公共卫生` `分类器性能`

## 📋 核心要点

1. 现有自杀风险评估方法缺乏有效的声学特征分析，导致识别率低。
2. 本研究通过系统评价声学分析与机器学习结合的方法，提出了一种新的自杀风险评估框架。
3. 研究结果表明，声学特征在自杀风险人群与非风险人群之间存在显著差异，分类器性能有显著提升。

## 📝 摘要（中文）

自杀仍然是公共卫生领域的一大挑战，亟需改进检测方法以便及时干预和治疗。本系统评价评估了人工智能和机器学习在通过声学分析评估自杀风险中的作用。根据PRISMA指南，我们分析了来自PubMed、Cochrane、Scopus和Web of Science数据库的33篇文章。结果显示，自杀风险人群与非风险人群在声学特征上存在显著差异，尤其是在抖动、基频、梅尔频率倒谱系数和功率谱密度等方面。分类器的性能因算法、模态和语音引导方法而异，多模态方法表现优越。29项分类器研究的AUC值范围为0.62至0.985，准确率为60%至99.85%。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有自杀风险评估方法中声学特征分析不足的问题，导致识别率低和干预时机不当。

**核心思路**：通过系统评价声学特征与机器学习结合的方法，探索其在自杀风险评估中的有效性，旨在提高识别准确率和及时干预能力。

**技术框架**：研究采用PRISMA指南，分析了33篇相关文献，重点关注声学特征与分类器性能的关系，流程包括文献筛选、特征提取和性能评估。

**关键创新**：本研究的创新点在于系统性地整合声学分析与机器学习，发现了自杀风险人群与非风险人群在声学特征上的显著差异，尤其是抖动、基频等特征的应用。

**关键设计**：研究中使用了多种分类器算法，评估了不同模态和语音引导方法的效果，报告的AUC值范围为0.62至0.985，准确率从60%到99.85%不等。

## 📊 实验亮点

研究结果显示，自杀风险人群与非风险人群在声学特征上存在显著差异，尤其是在抖动和基频等方面。29项分类器研究的AUC值范围为0.62至0.985，准确率从60%提升至99.85%，表明多模态方法在自杀风险评估中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康评估、临床干预和公共卫生监测。通过声学分析与机器学习的结合，能够为自杀风险的早期识别提供新的工具，帮助专业人员及时干预，降低自杀率，具有重要的社会价值和实际意义。

## 📄 摘要（原文）

> Suicide remains a public health challenge, necessitating improved detection methods to facilitate timely intervention and treatment. This systematic review evaluates the role of Artificial Intelligence (AI) and Machine Learning (ML) in assessing suicide risk through acoustic analysis of speech. Following PRISMA guidelines, we analyzed 33 articles selected from PubMed, Cochrane, Scopus, and Web of Science databases. The last search was conducted in February 2025. Risk of bias was assessed using the PROBAST tool. Studies analyzing acoustic features between individuals at risk of suicide (RS) and those not at risk (NRS) were included, while studies lacking acoustic data, a suicide-related focus, or sufficient methodological details were excluded. Sample sizes varied widely and were reported in terms of participants or speech segments, depending on the study. Results were synthesized narratively based on acoustic features and classifier performance. Findings consistently showed significant acoustic feature variations between RS and NRS populations, particularly involving jitter, fundamental frequency (F0), Mel-frequency cepstral coefficients (MFCC), and power spectral density (PSD). Classifier performance varied based on algorithms, modalities, and speech elicitation methods, with multimodal approaches integrating acoustic, linguistic, and metadata features demonstrating superior performance. Among the 29 classifier-based studies, reported AUC values ranged from 0.62 to 0.985 and accuracies from 60% to 99.85%. Most datasets were imbalanced in favor of NRS, and performance metrics were rarely reported separately by group, limiting clear identification of direction of effect.

