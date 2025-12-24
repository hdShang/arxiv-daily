---
layout: default
title: "An Auditable Pipeline for Fuzzy Full-Text Screening in Systematic Reviews: Integrating Contrastive Semantic Highlighting and LLM Judgment"
---

# An Auditable Pipeline for Fuzzy Full-Text Screening in Systematic Reviews: Integrating Contrastive Semantic Highlighting and LLM Judgment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15822" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15822v1</a>
  <a href="https://arxiv.org/pdf/2508.15822.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15822v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15822v1', 'An Auditable Pipeline for Fuzzy Full-Text Screening in Systematic Reviews: Integrating Contrastive Semantic Highlighting and LLM Judgment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pouria Mortezaagha, Arya Rahgozar

**分类**: cs.CL, cs.AI, cs.ET, cs.IR

**发布日期**: 2025-08-17

---

## 💡 一句话要点

**提出模糊全文本筛选管道以解决系统评价中的文献筛选问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模糊逻辑` `系统评价` `文献筛选` `大型语言模型` `对比相似度` `多标签设置` `医学研究`

## 📋 核心要点

1. 现有的全文本筛选方法在处理长文档时效率低下，难以有效捕捉分散的证据，导致系统评价的瓶颈。
2. 本文提出了一种模糊决策框架，通过对比语义高亮和大型语言模型的判断，提升文献筛选的准确性和效率。
3. 实验结果表明，模糊系统在多个标准上召回率显著高于传统方法，且筛选时间从20分钟缩短至1分钟，具有较高的实用价值。

## 📝 摘要（中文）

全文本筛选是系统评价中的主要瓶颈，因为重要证据分散在长且异质的文档中，难以应用静态的二元规则。本文提出了一种可扩展、可审计的管道，将纳入/排除重构为模糊决策问题，并在非传染性疾病的群体健康建模共识报告网络（POPCORN）中进行基准测试。文章将文献解析为重叠块，并使用领域适应模型进行嵌入；针对每个标准（人群、干预、结果、研究方法），计算对比相似度和模糊边际，利用Mamdani模糊控制器映射为动态阈值下的分级纳入度。大型语言模型（LLM）对高亮的文本片段进行评判，提供三级标签、置信度评分和标准相关的理由。结果显示，模糊系统在召回率上显著优于统计和清晰基线，且筛选时间大幅缩短。

## 🔬 方法详解

**问题定义**：本文旨在解决系统评价中全文本筛选的效率和准确性问题。现有方法在处理长且异质的文献时，往往无法有效捕捉分散的证据，导致筛选过程缓慢且不准确。

**核心思路**：论文的核心思路是将纳入/排除问题重构为模糊决策问题，通过对比相似度和模糊控制器来动态评估文献的纳入程度，以适应文献的复杂性。

**技术框架**：整体架构包括文献解析、特征嵌入、模糊控制和LLM评判四个主要模块。文献首先被解析为重叠块，然后通过领域适应模型进行嵌入，接着计算对比相似度，最后由LLM进行判断和标注。

**关键创新**：最重要的技术创新在于将模糊逻辑与对比高亮结合，利用LLM进行高效的判断和理由生成，显著提升了筛选的准确性和可审计性。

**关键设计**：在设计中，使用了Mamdani模糊控制器来映射模糊边际，并设定动态阈值以适应多标签设置。此外，LLM的使用提供了三级标签和置信度评分，确保了评判的稳定性和可靠性。

## 📊 实验亮点

实验结果显示，模糊系统在召回率上达到了81.3%（人群）、87.5%（干预）、87.5%（结果）和75.0%（研究方法），显著高于统计基线（56.3-75.0%）和清晰基线（43.8-81.3%）。此外，筛选时间从约20分钟减少到不足1分钟，且人机一致性达到96.1%。

## 🎯 应用场景

该研究的潜在应用领域包括医学文献筛选、系统评价和临床研究等。通过提高文献筛选的效率和准确性，能够加速研究进程，降低成本，提升决策质量，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Full-text screening is the major bottleneck of systematic reviews (SRs), as decisive evidence is dispersed across long, heterogeneous documents and rarely admits static, binary rules. We present a scalable, auditable pipeline that reframes inclusion/exclusion as a fuzzy decision problem and benchmark it against statistical and crisp baselines in the context of the Population Health Modelling Consensus Reporting Network for noncommunicable diseases (POPCORN). Articles are parsed into overlapping chunks and embedded with a domain-adapted model; for each criterion (Population, Intervention, Outcome, Study Approach), we compute contrastive similarity (inclusion-exclusion cosine) and a vagueness margin, which a Mamdani fuzzy controller maps into graded inclusion degrees with dynamic thresholds in a multi-label setting. A large language model (LLM) judge adjudicates highlighted spans with tertiary labels, confidence scores, and criterion-referenced rationales; when evidence is insufficient, fuzzy membership is attenuated rather than excluded. In a pilot on an all-positive gold set (16 full texts; 3,208 chunks), the fuzzy system achieved recall of 81.3% (Population), 87.5% (Intervention), 87.5% (Outcome), and 75.0% (Study Approach), surpassing statistical (56.3-75.0%) and crisp baselines (43.8-81.3%). Strict "all-criteria" inclusion was reached for 50.0% of articles, compared to 25.0% and 12.5% under the baselines. Cross-model agreement on justifications was 98.3%, human-machine agreement 96.1%, and a pilot review showed 91% inter-rater agreement (kappa = 0.82), with screening time reduced from about 20 minutes to under 1 minute per article at significantly lower cost. These results show that fuzzy logic with contrastive highlighting and LLM adjudication yields high recall, stable rationale, and end-to-end traceability.

