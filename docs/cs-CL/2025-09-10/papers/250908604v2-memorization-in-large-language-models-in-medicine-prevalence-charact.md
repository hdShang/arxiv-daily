---
layout: default
title: "Memorization in Large Language Models in Medicine: Prevalence, Characteristics, and Implications"
---

# Memorization in Large Language Models in Medicine: Prevalence, Characteristics, and Implications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08604" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08604v2</a>
  <a href="https://arxiv.org/pdf/2509.08604.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08604v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08604v2', 'Memorization in Large Language Models in Medicine: Prevalence, Characteristics, and Implications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anran Li, Lingfei Qian, Mengmeng Du, Yu Yin, Yan Hu, Zihao Sun, Yihang Fu, Erica Stutz, Xuguang Ai, Qianqian Xie, Rui Zhu, Jimin Huang, Yifan Yang, Siru Liu, Yih-Chung Tham, Lucila Ohno-Machado, Hyunghoon Cho, Zhiyong Lu, Hua Xu, Qingyu Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-10 (更新: 2025-11-06)

---

## 💡 一句话要点

**首个医学LLM记忆能力综合评估：揭示记忆普遍性、特征及影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学LLM` `记忆能力` `数据泄露` `临床应用` `模型评估`

## 📋 核心要点

1. 医学LLM面临记忆训练数据的问题，可能导致信息泄露或不当应用。
2. 论文全面评估医学LLM的记忆能力，分析其普遍性、特征和影响。
3. 实验表明医学LLM记忆普遍且高于通用领域，并提出改进建议。

## 📝 摘要（中文）

大型语言模型（LLM）在医学领域展现出巨大潜力。目前，LLM已广泛应用于诊断辅助、医学问答和临床信息综合等任务。然而，一个关键的开放性问题仍然存在：LLM在多大程度上记忆了医学训练数据？本研究首次对医学LLM的记忆能力进行了全面评估，评估其普遍性（发生频率）、特征（记忆内容）、容量（记忆内容量）以及潜在的下游影响（记忆如何影响医学应用）。我们系统地分析了常见的适应场景：（1）在医学语料库上持续预训练，（2）在标准医学基准上进行微调，以及（3）在真实临床数据上进行微调，包括来自耶鲁纽黑文医疗系统的超过13,000份独特的住院记录。结果表明，记忆在所有适应场景中都很普遍，并且明显高于在通用领域中报告的水平。记忆影响了医学LLM的开发和采用，并且可以分为三种类型：有益的（例如，准确回忆临床指南和生物医学参考文献），无信息的（例如，重复的免责声明或模板化的医学文档语言）和有害的（例如，数据集特定的或敏感的临床内容的再生）。基于这些发现，我们提出了实用的建议，以促进有益的记忆，从而增强领域特定的推理和事实准确性，最大限度地减少无信息的记忆，以促进超越表面模式的更深层次的学习，并减轻有害的记忆，以防止敏感或可识别的患者信息的泄露。

## 🔬 方法详解

**问题定义**：论文旨在解决医学领域大型语言模型（LLM）过度记忆训练数据的问题。现有方法缺乏对医学LLM记忆能力的系统性评估，无法有效区分有益、无信息和有害的记忆，从而可能导致敏感患者信息泄露、临床指南的错误应用等问题。

**核心思路**：论文的核心思路是通过系统性的实验评估，量化医学LLM在不同训练场景下的记忆水平，并分析记忆内容的特征。通过识别不同类型的记忆，为后续的优化和改进提供依据，最终目标是促进有益记忆，抑制有害记忆。

**技术框架**：论文的整体框架包括三个主要阶段：1) 数据准备：构建包含医学语料库、标准医学基准和真实临床数据的综合数据集；2) 模型训练：在不同数据集上对LLM进行持续预训练和微调，模拟常见的医学LLM应用场景；3) 记忆评估：设计特定的评估指标和方法，量化LLM在不同场景下的记忆水平，并分析记忆内容的特征。

**关键创新**：论文最重要的创新点在于首次对医学LLM的记忆能力进行全面而系统的评估。与以往研究主要关注通用领域LLM的记忆不同，该研究深入分析了医学LLM在特定领域的记忆特征，并提出了针对性的改进建议。此外，该研究还首次区分了有益、无信息和有害三种类型的记忆，为后续研究提供了新的视角。

**关键设计**：论文的关键设计包括：1) 针对不同类型记忆的评估指标，例如，使用精确匹配率评估对临床指南的记忆，使用信息熵评估记忆内容的多样性；2) 针对不同训练场景的实验设置，例如，分别在医学语料库、标准医学基准和真实临床数据上进行训练，以模拟不同的应用场景；3) 对记忆内容进行人工分析，识别有益、无信息和有害三种类型，并分析其产生的原因。

## 📊 实验亮点

研究结果表明，医学LLM的记忆水平显著高于通用领域LLM。在真实临床数据上微调的LLM，其记忆水平最高，表明临床数据更容易被模型记忆。此外，研究还发现，LLM更容易记忆数据集中的高频信息，例如免责声明和模板化的医学文档语言。

## 🎯 应用场景

该研究成果可应用于医学LLM的开发和部署，帮助开发者更好地控制模型的记忆行为，避免敏感信息泄露，提高模型的安全性和可靠性。同时，该研究也为医学领域的知识管理和信息检索提供了新的思路，有助于构建更加智能和高效的医疗信息系统。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated significant potential in medicine. To date, LLMs have been widely applied to tasks such as diagnostic assistance, medical question answering, and clinical information synthesis. However, a key open question remains: to what extent do LLMs memorize medical training data. In this study, we present the first comprehensive evaluation of memorization of LLMs in medicine, assessing its prevalence (how frequently it occurs), characteristics (what is memorized), volume (how much content is memorized), and potential downstream impacts (how memorization may affect medical applications). We systematically analyze common adaptation scenarios: (1) continued pretraining on medical corpora, (2) fine-tuning on standard medical benchmarks, and (3) fine-tuning on real-world clinical data, including over 13,000 unique inpatient records from Yale New Haven Health System. The results demonstrate that memorization is prevalent across all adaptation scenarios and significantly higher than reported in the general domain. Memorization affects both the development and adoption of LLMs in medicine and can be categorized into three types: beneficial (e.g., accurate recall of clinical guidelines and biomedical references), uninformative (e.g., repeated disclaimers or templated medical document language), and harmful (e.g., regeneration of dataset-specific or sensitive clinical content). Based on these findings, we offer practical recommendations to facilitate beneficial memorization that enhances domain-specific reasoning and factual accuracy, minimize uninformative memorization to promote deeper learning beyond surface-level patterns, and mitigate harmful memorization to prevent the leakage of sensitive or identifiable patient information.

