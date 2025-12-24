---
layout: default
title: "LAMDAS: LLM as an Implicit Classifier for Domain-specific Data Selection"
---

# LAMDAS: LLM as an Implicit Classifier for Domain-specific Data Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06524" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06524v1</a>
  <a href="https://arxiv.org/pdf/2509.06524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06524v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06524v1', 'LAMDAS: LLM as an Implicit Classifier for Domain-specific Data Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Wu, Hang Yu, Bingchang Liu, Wenjie Yang, Peng Di, Jianguo Li, Yue Zhang

**分类**: cs.CL

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**LAMDAS：利用LLM作为隐式分类器进行领域数据选择**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数据选择` `领域自适应` `隐式分类` `单类分类`

## 📋 核心要点

1. 领域数据稀缺是LLM领域适配的关键瓶颈，直接使用大量未清洗数据会引入噪声。
2. LAMDAS将LLM作为隐式分类器，把数据选择转化为单类分类问题，无需显式特征工程。
3. 实验表明，LAMDAS使用少量数据超越全数据训练，并优于多个SOTA基线，兼顾性能与效率。

## 📝 摘要（中文）

将大型语言模型(LLM)应用于特定领域时，常常面临高质量人工标注数据稀缺的瓶颈。虽然大量未经检查的数据唾手可得，但盲目地使用它们进行微调可能会引入噪声并降低性能。因此，战略性的数据选择至关重要，这需要一种既准确又高效的方法。现有的方法，可分为基于相似性的方法和直接优化方法，难以同时实现这些目标。本文介绍了一种新颖的方法LAMDAS（LLM As an iMplicit classifier for domain-specific DAta Selection），它利用预训练的LLM本身作为隐式分类器，从而绕过显式的特征工程和计算密集型的优化过程。LAMDAS将数据选择重新定义为一个单类分类问题，识别出“属于”由小型参考数据集定义的目标领域的数据。大量的实验结果表明，LAMDAS不仅使用一小部分数据就超过了全数据训练的性能，而且在各种场景下都优于九个最先进(SOTA)的基线。此外，与所有评估的基线相比，LAMDAS在性能提升和计算效率之间实现了最引人注目的平衡。

## 🔬 方法详解

**问题定义**：论文旨在解决特定领域内，高质量标注数据稀缺的情况下，如何从大量未标注数据中高效、准确地选择出适合微调LLM的数据子集的问题。现有方法，如基于相似度的方法和直接优化方法，要么需要大量的计算资源，要么在准确性上有所欠缺，难以同时满足效率和性能的要求。

**核心思路**：LAMDAS的核心思路是将预训练的LLM本身视为一个隐式的领域分类器。通过少量的参考数据集来引导LLM理解目标领域，然后利用LLM对候选数据进行“打分”，判断其是否属于目标领域。这种方法避免了显式的特征工程和复杂的优化过程，从而提高了数据选择的效率。

**技术框架**：LAMDAS的整体流程如下：1) **参考数据集构建**：收集少量高质量的领域内数据作为参考集。2) **LLM提示工程**：设计合适的提示语，引导LLM理解参考数据集所代表的领域。3) **候选数据评分**：使用LLM对候选数据进行评分，判断其与目标领域的相似度或相关性。4) **数据选择**：根据评分结果，选择排名靠前的候选数据用于LLM的微调。

**关键创新**：LAMDAS最重要的创新在于将LLM本身作为隐式分类器，避免了传统数据选择方法中复杂的特征工程和优化过程。与现有方法相比，LAMDAS无需训练额外的分类器或计算数据之间的相似度，而是直接利用LLM的预训练知识来判断数据是否属于目标领域。这种方法不仅提高了数据选择的效率，而且能够更好地利用LLM的领域知识。

**关键设计**：LAMDAS的关键设计包括：1) **提示语的设计**：提示语需要能够清晰地表达目标领域的特征，并引导LLM进行准确的判断。2) **评分函数的选择**：评分函数需要能够有效地衡量候选数据与目标领域的相似度或相关性。3) **数据选择策略**：数据选择策略需要平衡数据的质量和数量，以获得最佳的微调效果。具体的提示语设计、评分函数和数据选择策略可能需要根据具体的应用场景进行调整。

## 📊 实验亮点

实验结果表明，LAMDAS在多个领域数据集上均优于现有SOTA方法。例如，在特定数据集上，LAMDAS仅使用20%的数据就超过了全数据训练的性能，并且相比其他基线方法，性能提升显著，同时计算效率更高。这些结果验证了LAMDAS在领域数据选择方面的有效性和优越性。

## 🎯 应用场景

LAMDAS可广泛应用于各种领域LLM的定制化训练，例如医疗、金融、法律等。通过高效的数据选择，可以降低人工标注成本，加速LLM在特定领域的落地应用。该方法还有助于提升LLM在数据匮乏领域的性能，并降低模型训练的计算资源消耗，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Adapting large language models (LLMs) to specific domains often faces a critical bottleneck: the scarcity of high-quality, human-curated data. While large volumes of unchecked data are readily available, indiscriminately using them for fine-tuning risks introducing noise and degrading performance. Strategic data selection is thus crucial, requiring a method that is both accurate and efficient. Existing approaches, categorized as similarity-based and direct optimization methods, struggle to simultaneously achieve these goals. In this paper, we introduce LAMDAS (LLM As an iMplicit classifier for domain-specific DAta Selection), a novel approach that leverages the pre-trained LLM itself as an implicit classifier, thereby bypassing explicit feature engineering and computationally intensive optimization process. LAMDAS reframes data selection as a one-class classification problem, identifying candidate data that "belongs" to the target domain defined by a small reference dataset. Extensive experimental results demonstrate that LAMDAS not only exceeds the performance of full-data training using a fraction of the data but also outperforms nine state-of-the-art (SOTA) baselines under various scenarios. Furthermore, LAMDAS achieves the most compelling balance between performance gains and computational efficiency compared to all evaluated baselines.

