---
layout: default
title: "Text-to-CadQuery: A New Paradigm for CAD Generation with Scalable Large Model Capabilities"
---

# Text-to-CadQuery: A New Paradigm for CAD Generation with Scalable Large Model Capabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06507" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06507v1</a>
  <a href="https://arxiv.org/pdf/2505.06507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06507v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06507v1', 'Text-to-CadQuery: A New Paradigm for CAD Generation with Scalable Large Model Capabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyang Xie, Feng Ju

**分类**: cs.AI, cs.CV, cs.LG

**发布日期**: 2025-05-10

**🔗 代码/项目**: [GITHUB](https://github.com/Text-to-CadQuery/Text-to-CadQuery)

---

## 💡 一句话要点

**提出Text-to-CadQuery以解决CAD生成复杂性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CAD生成` `自然语言处理` `大规模模型` `模型微调` `CadQuery` `计算机辅助设计` `3D建模`

## 📋 核心要点

1. 现有CAD生成方法依赖于特定命令序列，无法直接利用预训练模型，增加了生成复杂性。
2. 本文提出直接从自然语言生成CadQuery代码，避免中间表示，简化CAD模型生成过程。
3. 实验结果显示，微调后的模型在top-1准确率上提升至69.3%，Chamfer距离减少48.6%。

## 📝 摘要（中文）

计算机辅助设计（CAD）是现代工程和制造的基础，但创建CAD模型仍需专业知识和专用软件。近期大型语言模型（LLMs）的进展使得自然语言直接转化为参数化3D模型成为可能。然而，现有方法通常生成特定任务的命令序列，无法直接处理，且需转换为CAD表示，增加了复杂性。为此，本文提出直接从文本生成CadQuery代码，利用预训练LLMs的优势，简化3D模型生成过程。通过对Text-to-CadQuery数据进行微调，实验表明，模型性能随着规模的增加而提升，最佳模型的top-1准确率达到69.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有CAD生成方法的复杂性问题，现有方法需将命令序列转换为CAD表示，增加了训练和生成的难度。

**核心思路**：论文提出直接从文本生成CadQuery代码，利用预训练LLMs的能力，避免中间转换步骤，从而简化生成流程。

**技术框架**：整体架构包括数据集扩展、模型微调和性能评估三个主要模块。首先，扩展Text2CAD数据集，增加170,000个CadQuery注释；其次，对六个不同规模的开源LLMs进行微调；最后，评估模型在生成任务中的表现。

**关键创新**：最重要的创新在于直接生成CadQuery代码，而非依赖于中间命令序列，这一设计显著降低了生成过程的复杂性。

**关键设计**：在微调过程中，采用了适当的损失函数和优化策略，以确保模型能够有效学习文本与CadQuery代码之间的映射关系。

## 📊 实验亮点

实验结果显示，最佳模型的top-1准确率从58.8%提升至69.3%，同时Chamfer距离减少了48.6%。这些结果表明，微调后的模型在生成3D模型的准确性和质量上有显著提升，验证了大规模模型在CAD生成中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括工程设计、产品原型开发和制造业自动化。通过简化CAD模型生成过程，能够降低对专业知识的依赖，提高设计效率，促进更广泛的用户群体参与CAD设计。未来，该技术可能推动CAD软件的普及和智能化发展。

## 📄 摘要（原文）

> Computer-aided design (CAD) is fundamental to modern engineering and manufacturing, but creating CAD models still requires expert knowledge and specialized software. Recent advances in large language models (LLMs) open up the possibility of generative CAD, where natural language is directly translated into parametric 3D models. However, most existing methods generate task-specific command sequences that pretrained models cannot directly handle. These sequences must be converted into CAD representations such as CAD vectors before a 3D model can be produced, which requires training models from scratch and adds unnecessary complexity. To tackle this issue, we propose generating CadQuery code directly from text, leveraging the strengths of pretrained LLMs to produce 3D models without intermediate representations, using this Python-based scripting language. Since LLMs already excel at Python generation and spatial reasoning, fine-tuning them on Text-to-CadQuery data proves highly effective. Given that these capabilities typically improve with scale, we hypothesize that larger models will perform better after fine-tuning. To enable this, we augment the Text2CAD dataset with 170,000 CadQuery annotations. We fine-tune six open-source LLMs of varying sizes and observe consistent improvements. Our best model achieves a top-1 exact match of 69.3%, up from 58.8%, and reduces Chamfer Distance by 48.6%. Project page: https://github.com/Text-to-CadQuery/Text-to-CadQuery.

