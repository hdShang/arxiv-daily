---
layout: default
title: "CienaLLM: Generative Climate-Impact Extraction from News Articles with Autoregressive LLMs"
---

# CienaLLM: Generative Climate-Impact Extraction from News Articles with Autoregressive LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19305" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19305v1</a>
  <a href="https://arxiv.org/pdf/2512.19305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19305v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19305v1', 'CienaLLM: Generative Climate-Impact Extraction from News Articles with Autoregressive LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Javier Vela-Tambo, Jorge Gracia, Fernando Dominguez-Castro

**分类**: cs.CL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**CienaLLM：利用自回归LLM从新闻文章中生成式提取气候影响信息**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `气候影响提取` `生成式信息提取` `大型语言模型` `零样本学习` `模式引导` `新闻文章` `自回归模型`

## 📋 核心要点

1. 现有方法难以大规模地从异构新闻文章中提取结构化的气候影响信息，阻碍了对气候灾害社会经济影响的理解和监测。
2. CienaLLM框架利用开放权重LLM进行零样本信息提取，通过可配置的提示和模式，以及多步骤流水线，实现灵活的信息抽取。
3. 实验表明，更大的模型性能更强，量化可显著提升效率，响应解析步骤有效消除格式错误，CienaLLM在干旱影响提取上与监督基线相当。

## 📝 摘要（中文）

为了理解和监测气候灾害带来的社会经济影响，需要大规模地从异构的新闻文章中提取结构化信息。为此，我们开发了CienaLLM，这是一个基于模式引导的生成式信息提取的模块化框架。CienaLLM使用开放权重的大型语言模型（LLM）从新闻文章中进行零样本信息提取，并支持可配置的提示和输出模式、多步骤流水线以及云或本地推理。为了系统地评估LLM系列、大小、精度方案和提示策略的选择如何影响性能，我们对模型、精度和提示工程技术进行了一项大型析因研究。额外的响应解析步骤几乎消除了格式错误，同时保持了准确性；较大的模型提供了最强大和最稳定的性能，而量化在精度上做出了适度的权衡，从而获得了显著的效率提升；提示策略显示出异构的、特定于模型的效果。CienaLLM在从西班牙新闻中提取干旱影响的准确性方面与监督基线相匹配或优于监督基线，尽管推理成本更高。虽然在干旱方面进行了评估，但通过编辑提示和模式而不是重新训练，这种模式驱动和模型无关的设计适合于适应相关的信息提取任务（例如，其他灾害、部门或语言）。我们发布了代码、配置和模式，以支持可重复使用。

## 🔬 方法详解

**问题定义**：论文旨在解决从大量异构新闻文章中自动提取结构化气候影响信息的问题。现有方法通常依赖于人工标注数据进行训练，成本高昂且难以适应新的灾害类型、领域或语言。此外，现有方法在处理非结构化文本时，容易产生格式错误，影响信息提取的准确性。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大生成能力，通过模式引导的生成式信息提取方法，实现零样本的信息提取。通过精心设计的提示（Prompt）和输出模式（Schema），引导LLM从新闻文章中提取所需的信息，并将其转换为结构化的格式。这种方法无需大量标注数据，具有很强的泛化能力和可扩展性。

**技术框架**：CienaLLM框架包含以下主要模块：1) **输入模块**：接收新闻文章作为输入。2) **提示生成模块**：根据预定义的模式和用户配置，生成用于引导LLM进行信息提取的提示。3) **LLM推理模块**：使用LLM对新闻文章进行推理，生成包含结构化信息的文本。4) **响应解析模块**：解析LLM的输出，提取结构化信息，并进行格式校正。5) **输出模块**：将提取的结构化信息以指定格式输出。

**关键创新**：论文的关键创新在于将模式引导的生成式信息提取方法应用于气候影响信息的提取，并利用LLM的零样本学习能力，避免了大量人工标注数据的需求。此外，论文还提出了一个响应解析模块，用于纠正LLM输出中的格式错误，提高信息提取的准确性。

**关键设计**：论文的关键设计包括：1) **提示工程**：设计有效的提示，引导LLM提取所需的信息。2) **输出模式定义**：定义清晰的输出模式，确保提取的信息具有结构化格式。3) **响应解析策略**：设计鲁棒的响应解析策略，纠正LLM输出中的格式错误。论文还对不同大小、精度和提示策略的LLM进行了大量的实验，以评估其性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19305v1/cienallm_dataflow.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19305v1/response_parsing_error_rate.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19305v1/f1_score_per_model.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CienaLLM在从西班牙新闻中提取干旱影响的准确性方面与监督基线相匹配或优于监督基线。更大的模型提供了更强大和更稳定的性能，而量化在精度上做出了适度的权衡，从而获得了显著的效率提升。响应解析步骤几乎消除了格式错误，同时保持了准确性。

## 🎯 应用场景

CienaLLM可应用于气候风险评估、灾害预警、政策制定等领域。通过自动提取新闻文章中的气候影响信息，可以帮助政府、企业和个人更好地了解气候变化带来的风险，并采取相应的应对措施。该框架具有很强的可扩展性，可以应用于其他灾害类型、领域和语言，具有广泛的应用前景。

## 📄 摘要（原文）

> Understanding and monitoring the socio-economic impacts of climate hazards requires extracting structured information from heterogeneous news articles on a large scale. To that end, we have developed CienaLLM, a modular framework based on schema-guided Generative Information Extraction. CienaLLM uses open-weight Large Language Models for zero-shot information extraction from news articles, and supports configurable prompts and output schemas, multi-step pipelines, and cloud or on-premise inference. To systematically assess how the choice of LLM family, size, precision regime, and prompting strategy affect performance, we run a large factorial study in models, precisions, and prompt engineering techniques. An additional response parsing step nearly eliminates format errors while preserving accuracy; larger models deliver the strongest and most stable performance, while quantization offers substantial efficiency gains with modest accuracy trade-offs; and prompt strategies show heterogeneous, model-specific effects. CienaLLM matches or outperforms the supervised baseline in accuracy for extracting drought impacts from Spanish news, although at a higher inference cost. While evaluated in droughts, the schema-driven and model-agnostic design is suitable for adapting to related information extraction tasks (e.g., other hazards, sectors, or languages) by editing prompts and schemas rather than retraining. We release code, configurations, and schemas to support reproducible use.

