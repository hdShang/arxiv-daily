---
layout: default
title: DEER: A Comprehensive and Reliable Benchmark for Deep-Research Expert Reports
---

# DEER: A Comprehensive and Reliable Benchmark for Deep-Research Expert Reports

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17776" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17776v1</a>
  <a href="https://arxiv.org/pdf/2512.17776.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17776v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17776v1', 'DEER: A Comprehensive and Reliable Benchmark for Deep-Research Expert Reports')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Janghoon Han, Heegyu Kim, Changho Lee, Dahm Lee, Min Hyung Park, Hosung Song, Stanley Jungkyu Choi, Moontae Lee, Honglak Lee

**分类**: cs.CL

**发布日期**: 2025-12-19

**备注**: Work in progress

---

## 💡 一句话要点

**DEER：一个全面可靠的深度研究专家报告评估基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度研究报告` `评估基准` `大型语言模型` `事实核查` `专家评估` `自然语言处理` `信息抽取`

## 📋 核心要点

1. 现有专家报告评估基准缺乏系统性标准，且过度依赖LLM评判，难以捕捉需要专家知识的问题。
2. DEER基准通过构建专家基础的评估体系，并提供任务相关的专家指导，提升LLM评判的一致性。
3. DEER引入文档级事实核查架构，验证报告中所有声明，并量化外部证据质量，更全面评估报告可靠性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的进步，深度研究系统能够通过多步骤推理和基于证据的综合生成专家级报告，但评估此类报告仍然具有挑战性。现有的基准通常缺乏针对专家报告的系统性标准，严重依赖LLM评判的评估可能无法捕捉到需要专家判断的问题，并且源验证通常仅涵盖显式引用的语句的有限子集，而不是报告范围内的事实可靠性。我们引入了DEER，这是一个用于评估专家级深度研究报告的基准。DEER包含跨越13个领域的50个报告撰写任务，以及一个专家基础的评估分类法（7个维度，25个子维度），并将其操作化为130个细粒度的评分标准项。DEER还提供特定于任务的专家指导，以帮助LLM评判更一致地评估专家级报告质量。作为基于评分标准的评估的补充，我们提出了一种文档级事实检查架构，该架构提取并验证整个报告中的所有声明，包括引用的和未引用的声明，并量化外部证据质量。DEER与人类专家的判断密切相关，并产生对系统优势和劣势的可解释诊断。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在生成专家级别的研究报告时，缺乏一个全面且可靠的评估基准。现有的基准要么缺乏针对专家报告的系统性评估标准，要么过度依赖LLM进行评估，而LLM本身可能无法准确捕捉到需要专业知识才能判断的问题。此外，现有的事实核查方法通常只关注报告中显式引用的部分，而忽略了未引用的声明，导致无法全面评估报告的可靠性。

**核心思路**：DEER的核心思路是构建一个专家基础的评估体系，并提供任务相关的专家指导，以提升LLM评判的一致性和准确性。同时，引入一种文档级别的全面事实核查架构，以验证报告中的所有声明，包括引用的和未引用的部分，从而更全面地评估报告的可靠性。

**技术框架**：DEER基准包含以下几个主要组成部分：1) 50个报告撰写任务，涵盖13个不同的领域；2) 一个专家基础的评估分类法，包含7个维度和25个子维度，并将其转化为130个细粒度的评分标准项；3) 任务相关的专家指导，用于帮助LLM评判更一致地评估报告质量；4) 一个文档级别的全面事实核查架构，用于提取和验证报告中的所有声明，并量化外部证据的质量。

**关键创新**：DEER的关键创新在于：1) 构建了一个专家基础的评估体系，该体系能够更准确地评估专家级别的研究报告；2) 引入了任务相关的专家指导，从而提升了LLM评判的一致性和准确性；3) 提出了一种文档级别的全面事实核查架构，该架构能够验证报告中的所有声明，包括引用的和未引用的部分，从而更全面地评估报告的可靠性。

**关键设计**：DEER的评估分类法包含7个维度，分别是：正确性、完整性、相关性、一致性、清晰性、可信度和有用性。每个维度又包含若干个子维度，例如，正确性维度包含事实正确性、逻辑正确性和计算正确性等子维度。每个子维度都对应若干个细粒度的评分标准项，例如，事实正确性子维度对应“报告中的所有事实陈述是否都得到了可靠来源的支持”等评分标准项。文档级事实核查架构使用信息抽取技术从报告中提取所有声明，然后使用搜索引擎和知识图谱等外部资源验证这些声明的真实性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17776v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17776v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17776v1/latex/figures/heatmap_criteria.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DEER基准与人类专家的判断具有很高的相关性，表明该基准能够有效地评估专家级研究报告的质量。实验结果表明，使用DEER基准可以对深度研究系统的优势和劣势进行可解释的诊断，从而帮助研究人员更好地理解系统的行为。文档级事实核查架构能够有效地识别报告中的错误声明，并量化外部证据的质量。

## 🎯 应用场景

DEER基准可用于评估和比较不同深度研究系统的性能，帮助研究人员了解系统的优势和劣势，并指导系统改进。此外，DEER还可以用于训练和微调LLM，使其能够更好地生成高质量的专家级研究报告。该基准的实际价值在于推动深度研究系统的发展，提高研究报告的质量和可靠性，从而促进科学研究和知识传播。

## 📄 摘要（原文）

> As large language models (LLMs) advance, deep research systems can generate expert-level reports via multi-step reasoning and evidence-based synthesis, but evaluating such reports remains challenging. Existing benchmarks often lack systematic criteria for expert reporting, evaluations that rely heavily on LLM judges can fail to capture issues that require expert judgment, and source verification typically covers only a limited subset of explicitly cited statements rather than report-wide factual reliability. We introduce DEER, a benchmark for evaluating expert-level deep research reports. DEER comprises 50 report-writing tasks spanning 13 domains and an expert-grounded evaluation taxonomy (7 dimensions, 25 sub-dimension) operationalized into 130 fine-grained rubric items. DEER further provides task-specific expert guidance to help LLM judges assess expert-level report quality more consistently. Complementing rubric-based assessment, we propose a document-level fact-checking architecture that extracts and verifies all claims across the entire report, including both cited and uncited ones, and quantifies external-evidence quality. DEER correlates closely with human expert judgments and yields interpretable diagnostics of system strengths and weaknesses.

