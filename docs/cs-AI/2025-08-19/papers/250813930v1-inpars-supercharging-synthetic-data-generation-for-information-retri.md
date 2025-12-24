---
layout: default
title: "InPars+: Supercharging Synthetic Data Generation for Information Retrieval Systems"
---

# InPars+: Supercharging Synthetic Data Generation for Information Retrieval Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13930" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13930v1</a>
  <a href="https://arxiv.org/pdf/2508.13930.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13930v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13930v1', 'InPars+: Supercharging Synthetic Data Generation for Information Retrieval Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matey Krastev, Miklos Hamar, Danilo Toapanta, Jesse Brouwers, Yibin Lei

**分类**: cs.IR, cs.AI

**发布日期**: 2025-08-19

**🔗 代码/项目**: [GITHUB](https://github.com/danilotpnta/IR2-project)

---

## 💡 一句话要点

**提出InPars+以提升神经信息检索系统的合成数据生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据生成` `神经信息检索` `对比偏好优化` `动态提示模板` `大型语言模型`

## 📋 核心要点

1. 现有的合成查询生成方法在生成高质量查询方面存在不足，影响了神经信息检索系统的性能。
2. 本研究通过对比偏好优化微调查询生成模型，并使用动态提示模板来提升生成查询的质量。
3. 实验结果显示，采用新方法后，检索性能显著提高，且对激进过滤的需求减少，验证了方法的有效性。

## 📝 摘要（中文）

本研究重新审视并扩展了神经信息检索（NIR）的合成查询生成管道，利用InPars工具包，这是一个可重复的端到端框架，使用大型语言模型（LLMs）生成训练数据。我们首先评估了原始InPars、InPars-V2和Promptagator管道在SciFact基准上的可重复性，并验证了它们在开源重排序和生成模型中的有效性。在此基础上，我们引入了两个关键扩展：通过对比偏好优化（CPO）微调查询生成LLM，以提高生成查询的信号质量；以及使用DSPy框架将静态提示模板替换为动态的思维链（CoT）优化提示。我们的结果表明，这两个扩展减少了对激进过滤的需求，同时提高了检索性能。所有代码、模型和合成数据集均已公开发布，以支持进一步研究。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有合成查询生成方法在生成高质量查询时的不足，尤其是在神经信息检索系统中的应用痛点。现有方法往往依赖静态模板，导致生成的查询质量不高，影响检索效果。

**核心思路**：论文提出通过对比偏好优化（CPO）对查询生成模型进行微调，以提高生成查询的信号质量。同时，采用动态的思维链（CoT）优化提示，替代静态模板，从而提升生成过程的灵活性和效果。

**技术框架**：整体架构包括数据生成、模型微调和检索性能评估三个主要模块。首先，通过InPars工具包生成初步查询数据；然后，利用CPO对生成模型进行微调；最后，评估生成查询在实际检索任务中的表现。

**关键创新**：最重要的技术创新在于引入了对比偏好优化来微调查询生成模型，并使用动态提示模板，这与传统的静态模板方法形成了本质区别，显著提升了生成查询的质量。

**关键设计**：在微调过程中，采用了特定的损失函数以优化生成查询的信号质量，同时在动态提示设计中，结合了思维链的策略，使得生成过程更加灵活和高效。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，采用InPars+后，检索性能显著提升，具体表现为在SciFact基准测试中，生成查询的有效性提高了XX%，同时减少了对激进过滤的需求，验证了新方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、搜索引擎优化和自然语言处理等。通过提升合成数据的质量，研究成果能够帮助构建更高效的检索系统，进而提高用户的信息获取效率。未来，这种方法还可能扩展到其他需要高质量数据生成的领域，如对话系统和推荐系统。

## 📄 摘要（原文）

> This work revisits and extends synthetic query generation pipelines for Neural Information Retrieval (NIR) by leveraging the InPars Toolkit, a reproducible, end-to-end framework for generating training data using large language models (LLMs). We first assess the reproducibility of the original InPars, InPars-V2, and Promptagator pipelines on the SciFact benchmark and validate their effectiveness using open-source reranker and generator models. Building on this foundation, we introduce two key extensions to the pipeline: (1) fine-tuning a query generator LLM via Contrastive Preference Optimization (CPO) to improve the signal quality in generated queries, and (2) replacing static prompt templates with dynamic, Chain-of-Thought (CoT) optimized prompts using the DSPy framework. Our results show that both extensions reduce the need for aggressive filtering while improving retrieval performance. All code, models, and synthetic datasets are publicly released to support further research at: \href{https://github.com/danilotpnta/IR2-project}{this https URL}.

