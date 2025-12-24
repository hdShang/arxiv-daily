---
layout: default
title: "LLMSQL: Upgrading WikiSQL for the LLM Era of Text-to-SQL"
---

# LLMSQL: Upgrading WikiSQL for the LLM Era of Text-to-SQL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02350" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02350v2</a>
  <a href="https://arxiv.org/pdf/2510.02350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02350v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02350v2', 'LLMSQL: Upgrading WikiSQL for the LLM Era of Text-to-SQL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dzmitry Pihulski, Karol Charchut, Viktoria Novogrodskaia, Jan Kocoń

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27 (更新: 2025-12-09)

**备注**: To appear in the Proceedings of the IEEE International Conference on Data Mining Workshops (ICDMW)

---

## 💡 一句话要点

**LLMSQL：为大语言模型时代升级WikiSQL文本到SQL数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到SQL` `大型语言模型` `数据集清洗` `数据标注` `自然语言处理`

## 📋 核心要点

1. 现有WikiSQL数据集存在大小写敏感、数据类型不匹配等问题，限制了大语言模型在文本到SQL任务上的应用。
2. LLMSQL通过自动化方法清理和重新标注WikiSQL数据集，提供更干净的自然语言问题和完整的SQL查询。
3. 实验表明，DeepSeek-R1在LLMSQL上零样本准确率达88.40%，小参数模型微调后准确率超过90%。

## 📝 摘要（中文）

本文提出了LLMSQL，一个为大语言模型时代设计的WikiSQL数据集的系统性修订和转换版本。原始WikiSQL数据集在早期的文本到SQL研究中发挥了关键作用，但由于结构和标注问题（包括大小写敏感性不一致、数据类型不匹配、语法错误和未回答的问题）而逐渐不再被使用。本文对这些错误进行了分类，并实现了自动化的清理和重新标注方法。为了评估这些改进的影响，本文评估了多个大型语言模型，包括Gemma 3、LLaMA 3.2、Mistral 7B、gpt-oss 20B、Phi-3.5 Mini、Qwen 2.5、OpenAI o4-mini、DeepSeek-R1等。结果表明，DeepSeek-R1在零样本设置下达到了88.40%的准确率，而参数量小于10B的模型在微调后超过了90%的准确率。LLMSQL并非简单地作为更新，而是作为LLM-ready的基准被引入。与最初为指针网络模型量身定制的WikiSQL不同，LLMSQL提供了干净的自然语言问题和完整的SQL查询作为纯文本，从而能够为现代自然语言到SQL模型提供直接的生成和评估。

## 🔬 方法详解

**问题定义**：论文旨在解决现有WikiSQL数据集质量不高的问题，这些问题包括大小写敏感性不一致、数据类型不匹配、SQL语法错误以及存在无法回答的问题。这些问题阻碍了大语言模型在文本到SQL任务上的有效应用，使得模型难以学习到正确的映射关系。现有方法通常直接使用原始WikiSQL数据集，忽略了这些内在缺陷，导致模型性能受限。

**核心思路**：论文的核心思路是对WikiSQL数据集进行系统性的清洗和重新标注，以消除数据集中的错误和不一致性。通过自动化方法，尽可能地减少人工干预，保证数据集的客观性和一致性。同时，将数据集格式转换为纯文本，方便大语言模型直接生成和评估SQL查询。

**技术框架**：LLMSQL的构建主要包含以下几个阶段：1) 错误分类：对WikiSQL中存在的错误类型进行详细分类，包括大小写问题、数据类型问题、语法错误等。2) 自动化清洗：针对不同类型的错误，设计相应的自动化清洗方法，例如使用正则表达式进行大小写转换，使用数据类型推断工具进行数据类型校正。3) 重新标注：对于无法自动修复的问题，进行人工重新标注，确保数据集的正确性。4) 格式转换：将数据集转换为纯文本格式，方便大语言模型直接使用。

**关键创新**：LLMSQL的关键创新在于其系统性的数据清洗和重新标注流程，以及将数据集转换为纯文本格式。与以往的研究不同，LLMSQL不仅仅是对数据集进行简单的更新，而是从根本上解决了数据集质量问题，使其更适合大语言模型的使用。此外，纯文本格式的转换使得模型可以直接生成SQL查询，避免了以往需要使用指针网络选择token的限制。

**关键设计**：论文中使用了多种自动化清洗方法，例如使用正则表达式进行大小写转换，使用数据类型推断工具进行数据类型校正。对于无法自动修复的问题，采用了人工重新标注的方式。在格式转换方面，将原始的JSON格式转换为纯文本格式，并对SQL查询进行了标准化处理，例如统一使用大写关键字，添加必要的空格等。

## 📊 实验亮点

实验结果表明，经过LLMSQL清洗和重新标注后的数据集，能够显著提升大语言模型在文本到SQL任务上的性能。DeepSeek-R1模型在零样本设置下达到了88.40%的准确率，而参数量小于10B的模型在微调后超过了90%的准确率。这些结果表明，LLMSQL数据集的质量得到了显著提升，为大语言模型在文本到SQL任务上的应用奠定了基础。

## 🎯 应用场景

LLMSQL数据集的发布，能够促进大语言模型在文本到SQL任务上的研究和应用。该数据集可以用于训练和评估各种文本到SQL模型，提高模型在实际应用中的准确性和鲁棒性。潜在的应用领域包括智能客服、数据分析、商业智能等，使得非专业用户可以通过自然语言与数据库进行交互，获取所需信息。

## 📄 摘要（原文）

> Converting natural language questions into SQL queries enables non-expert users to interact with relational databases and has long been a central task for natural language interfaces to data. While the WikiSQL dataset played a key role in early text-to-SQL research, its usage has declined due to structural and annotation issues, including case sensitivity inconsistencies, data type mismatches, syntax errors, and unanswered questions. We present LLMSQL, a systematic revision and transformation of WikiSQL designed for the large language model era. We classify these errors and implement automated methods for cleaning and re-annotation. To assess the impact of these improvements, we evaluated multiple large language models, including Gemma 3, LLaMA 3.2, Mistral 7B, gpt-oss 20B, Phi-3.5 Mini, Qwen 2.5, OpenAI o4-mini, DeepSeek-R1, and others. Notably, DeepSeek-R1 achieves 88.40% accuracy in a zero-shot setting, and models under 10B parameters surpass 90% accuracy after fine-tuning. Rather than serving as an update, LLMSQL is introduced as an LLM-ready benchmark. Unlike the original WikiSQL, which was tailored for pointer-network models selecting tokens from input, LLMSQL provides clean natural language questions and full SQL queries as plain text, enabling straightforward generation and evaluation for modern natural-language-to-SQL models.

