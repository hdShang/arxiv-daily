---
layout: default
title: "The role of synthetic data in Multilingual, Multi-cultural AI systems: Lessons from Indic Languages"
---

# The role of synthetic data in Multilingual, Multi-cultural AI systems: Lessons from Indic Languages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21294" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21294v1</a>
  <a href="https://arxiv.org/pdf/2509.21294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21294v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21294v1', 'The role of synthetic data in Multilingual, Multi-cultural AI systems: Lessons from Indic Languages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pranjal A. Chitale, Varun Gumma, Sanchit Ahuja, Prashant Kodali, Manan Uppadhyay, Deepthi Sudharsan, Sunayana Sitaram

**分类**: cs.CL

**发布日期**: 2025-09-25

**备注**: Under Review

---

## 💡 一句话要点

**提出Updesh数据集，利用合成数据提升多语言、多文化AI系统在印度语言上的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据` `多语言AI` `低资源语言` `印度语言` `文化背景` `指令遵循` `大型语言模型`

## 📋 核心要点

1. 现有AI系统在低资源多语言文化环境下的表现不足，缺乏文化背景化数据。
2. 论文提出自下而上的合成数据生成策略，利用大型语言模型和维基百科内容，构建文化相关的印度语言数据集。
3. 实验表明，在Updesh数据集上训练的模型在生成任务上显著提升，尤其是在低资源语言上。

## 📝 摘要（中文）

开发在不同语言中有效运行且具有文化基础的AI系统是一项长期挑战，尤其是在低资源环境中。合成数据提供了一个有希望的途径，但其在多语言和多文化环境中的有效性仍未得到充分探索。本文研究了通过自下而上的生成策略为印度语言创建和影响合成的、文化背景化的数据集，该策略提示大型开源LLM（>= 235B参数）将数据生成建立在特定语言的维基百科内容之上。这种方法补充了从英语等高资源语言翻译合成数据集的自上而下的主导范式。我们介绍了Updesh，一个高质量的大规模合成指令遵循数据集，包含13种印度语言的950万个数据点，涵盖了多样化的推理和生成任务，重点是长上下文、多轮能力以及与印度文化背景的对齐。一项包含自动化指标和1万次人工评估的综合评估表明，生成的数据质量很高；但人工评估突出了需要进一步改进的领域。此外，我们通过在我们的数据集上微调模型并评估15个多样化的多语言数据集上的性能来进行下游评估。在Updesh上训练的模型在生成任务上始终取得显著收益，并在多项选择风格的NLU任务中保持竞争力。值得注意的是，相对改进在低资源和中等资源语言中最为明显，缩小了它们与高资源语言的差距。这些发现提供了经验证据，表明有效的多语言AI需要多方面的数据管理和生成策略，这些策略结合了上下文感知、文化基础的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决多语言、多文化AI系统在低资源印度语言环境中数据匮乏的问题。现有方法主要依赖于将高资源语言（如英语）的数据集翻译成目标语言，这种“自上而下”的方法忽略了特定文化的细微差别和语言特性，导致模型性能受限。因此，需要一种能够生成具有文化背景和语言特征的合成数据的方法。

**核心思路**：论文的核心思路是采用“自下而上”的数据生成策略，利用大型语言模型（LLM）的生成能力，并结合特定语言的维基百科内容，生成具有文化背景的合成数据。这种方法能够更好地捕捉目标语言的细微差别和文化内涵，从而提高AI系统在该语言环境下的性能。

**技术框架**：整体框架包括以下几个主要阶段：1) **数据源准备**：收集13种印度语言的维基百科内容，作为LLM生成数据的知识基础。2) **提示工程**：设计合适的提示语，引导LLM生成特定任务和文化背景的数据。3) **数据生成**：使用大型开源LLM（>= 235B参数）根据提示语生成合成数据。4) **数据清洗与过滤**：对生成的数据进行清洗和过滤，去除低质量或不相关的数据。5) **数据集构建**：将清洗后的数据整理成Updesh数据集，包含950万个数据点。

**关键创新**：最重要的技术创新点在于提出了自下而上的合成数据生成策略，该策略能够生成具有文化背景和语言特征的合成数据，从而更好地满足低资源多语言文化环境的需求。与传统的自上而下的翻译方法相比，该方法能够更好地捕捉目标语言的细微差别和文化内涵。

**关键设计**：关键设计包括：1) 使用大型开源LLM（>= 235B参数）作为数据生成器，以保证生成数据的质量和多样性。2) 利用特定语言的维基百科内容作为知识基础，以确保生成的数据具有文化背景。3) 设计多样化的提示语，引导LLM生成不同任务和风格的数据。4) 采用自动化指标和人工评估相结合的方式，对生成的数据进行质量评估。

## 📊 实验亮点

实验结果表明，在Updesh数据集上训练的模型在生成任务上取得了显著的性能提升，尤其是在低资源和中等资源语言中。例如，在下游评估中，模型在生成任务上始终取得显著收益，并在多项选择风格的NLU任务中保持竞争力。相对改进在低资源和中等资源语言中最为明显，缩小了它们与高资源语言的差距。

## 🎯 应用场景

该研究成果可应用于开发更有效的多语言、多文化AI系统，尤其是在低资源语言环境中。例如，可以用于构建更智能的印度语言聊天机器人、翻译系统和教育应用。此外，该方法还可以推广到其他低资源语言和文化环境中，促进全球AI的公平性和可访问性。

## 📄 摘要（原文）

> Developing AI systems that operate effectively across languages while remaining culturally grounded is a long-standing challenge, particularly in low-resource settings. Synthetic data provides a promising avenue, yet its effectiveness in multilingual and multicultural contexts remains underexplored. We investigate the creation and impact of synthetic, culturally contextualized datasets for Indian languages through a bottom-up generation strategy that prompts large open-source LLMs (>= 235B parameters) to ground data generation in language-specific Wikipedia content. This approach complements the dominant top-down paradigm of translating synthetic datasets from high-resource languages such as English. We introduce Updesh, a high-quality large-scale synthetic instruction-following dataset comprising 9.5M data points across 13 Indian languages, encompassing diverse reasoning and generative tasks with an emphasis on long-context, multi-turn capabilities, and alignment with Indian cultural contexts. A comprehensive evaluation incorporating both automated metrics and human annotation across 10k assessments indicates that generated data is high quality; though, human evaluation highlights areas for further improvement. Additionally, we perform downstream evaluations by fine-tuning models on our dataset and assessing the performance across 15 diverse multilingual datasets. Models trained on Updesh consistently achieve significant gains on generative tasks and remain competitive on multiple-choice style NLU tasks. Notably, relative improvements are most pronounced in low and medium-resource languages, narrowing their gap with high-resource languages. These findings provide empirical evidence that effective multilingual AI requires multi-faceted data curation and generation strategies that incorporate context-aware, culturally grounded methodologies.

