---
layout: default
title: "Arce: Augmented Roberta with Contextualized Elucidations for Ner in Automated Rule Checking"
---

# Arce: Augmented Roberta with Contextualized Elucidations for Ner in Automated Rule Checking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07286" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07286v2</a>
  <a href="https://arxiv.org/pdf/2508.07286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07286v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07286v2', 'Arce: Augmented Roberta with Contextualized Elucidations for Ner in Automated Rule Checking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Chen, Jinbao Tian, Yankui Li, Yuqi Lu, Zhou Li

**分类**: cs.CL, cs.IR

**发布日期**: 2025-08-10 (更新: 2025-09-10)

**🔗 代码/项目**: [GITHUB](https://github.com/nxcc-lab/ARCE)

---

## 💡 一句话要点

**提出ARCE以解决AEC领域命名实体识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `命名实体识别` `自动化规则检查` `大型语言模型` `RoBERTa` `上下文化解释` `建筑工程` `信息提取`

## 📋 核心要点

1. 现有的命名实体识别方法在AEC领域面临领域差距，难以处理专业术语和复杂关系。
2. ARCE通过生成简单的上下文化解释来增强RoBERTa模型的预训练，优化知识生成过程。
3. 实验表明，ARCE在AEC数据集上达到了77.20%的Macro-F1分数，创下新纪录，显示出其有效性。

## 📝 摘要（中文）

从专业文本中准确提取信息是一个关键挑战，特别是在建筑、工程和施工（AEC）领域的命名实体识别（NER）中，以支持自动化规则检查（ARC）。标准预训练模型的性能常常受到领域差距的限制，难以理解AEC文本中的专业术语和复杂关系。虽然通过在大型人类策划的领域语料库上进一步预训练可以缓解这一问题，但这种方法既费力又成本高。因此，利用大型语言模型（LLMs）进行自动知识生成成为一种有前景的替代方案。为此，本文提出了ARCE（增强型RoBERTa与上下文化阐释），系统性地探索和优化这一生成过程。ARCE首先利用LLM生成简单直接的解释语料，然后逐步对RoBERTa模型进行预训练，最终在下游任务上进行微调。实验结果表明，ARCE在基准AEC数据集上达到了77.20%的Macro-F1分数，显示出简单的基于解释的知识在此任务中比复杂的基于角色的推理更有效。

## 🔬 方法详解

**问题定义**：本文旨在解决AEC领域命名实体识别中的信息提取问题，现有方法因领域差距而表现不佳，难以理解专业术语和复杂关系。

**核心思路**：ARCE的核心思路是利用大型语言模型生成简单的上下文化解释，以此增强RoBERTa模型的预训练效果，从而提高NER的准确性。

**技术框架**：ARCE的整体架构包括两个主要阶段：首先使用LLM生成解释语料（Cote），然后在此基础上对RoBERTa进行增量预训练，最后在下游任务上进行微调。

**关键创新**：ARCE的主要创新在于通过生成简单的解释知识来替代复杂的角色推理，这一方法在AEC领域的NER任务中表现出更高的有效性。

**关键设计**：在模型设计中，ARCE采用了特定的损失函数和参数设置，以确保生成的解释能够有效地支持RoBERTa的预训练过程。

## 📊 实验亮点

ARCE在基准AEC数据集上取得了77.20%的Macro-F1分数，显著优于现有方法，展示了简单解释知识的有效性，相较于复杂推理方法提升明显。

## 🎯 应用场景

该研究的潜在应用领域包括建筑、工程和施工行业的自动化规则检查，能够提高信息提取的准确性和效率。未来，该方法可能在其他专业领域的命名实体识别任务中展现出广泛的应用价值。

## 📄 摘要（原文）

> Accurate information extraction from specialized texts is a critical challenge, particularly for named entity recognition (NER) in the architecture, engineering, and construction (AEC) domain to support automated rule checking (ARC). The performance of standard pre-trained models is often constrained by the domain gap, as they struggle to interpret the specialized terminology and complex relational contexts inherent in AEC texts. Although this issue can be mitigated by further pre-training on large, human-curated domain corpora, as exemplified by methods like ARCBERT, this approach is both labor-intensive and cost-prohibitive. Consequently, leveraging large language models (LLMs) for automated knowledge generation has emerged as a promising alternative. However, the optimal strategy for generating knowledge that can genuinely enhance smaller, efficient models remains an open question. To address this, we propose ARCE (augmented RoBERTa with contextualized elucidations), a novel approach that systematically explores and optimizes this generation process. ARCE employs an LLM to first generate a corpus of simple, direct explanations, which we term Cote, and then uses this corpus to incrementally pre-train a RoBERTa model prior to its fine-tuning on the downstream task. Our extensive experiments show that ARCE establishes a new state-of-the-art on a benchmark AEC dataset, achieving a Macro-F1 score of 77.20%. This result also reveals a key finding: simple, explanation-based knowledge proves surprisingly more effective than complex, role-based rationales for this task. The code is publicly available at:https://github.com/nxcc-lab/ARCE.

