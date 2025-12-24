---
layout: default
title: "SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models"
---

# SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15174" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15174v2</a>
  <a href="https://arxiv.org/pdf/2509.15174.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15174v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15174v2', 'SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huy Nghiem, Advik Sachdeva, Hal Daumé

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-18 (更新: 2025-10-08)

**备注**: NLP, Hate speech detection, explanation, LLM. Version 2: updated experiments and analysis

---

## 💡 一句话要点

**SMARTER：利用自增强大语言模型，高效提升毒性检测能力并提供可解释性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `毒性检测` `大型语言模型` `可解释性` `自增强学习` `内容审核`

## 📋 核心要点

1. 现有毒性检测方法通常需要大量标注数据，且缺乏可解释性，限制了其在低资源场景下的应用。
2. SMARTER框架利用LLM的自增强能力，生成合成解释并进行跨模型训练，从而在数据量有限的情况下提升毒性检测性能。
3. 实验表明，SMARTER在三个基准数据集上取得了显著的性能提升，宏平均F1值最高提升了13.5%。

## 📝 摘要（中文）

为解决社交媒体上恶意内容泛滥的问题，我们提出了SMARTER，一个数据高效的两阶段框架，利用大型语言模型（LLMs）进行可解释的内容审核。在第一阶段，我们利用LLMs自身的输出来生成合成解释，用于纠正正确和不正确的标签，从而通过偏好优化实现对齐，且只需极少的人工监督。在第二阶段，我们通过跨模型训练来改进解释质量，使较弱的模型在风格和语义上与较强的模型对齐。在HateXplain、Latent Hate和Implicit Hate三个基准任务上的实验表明，SMARTER使LLMs能够在仅使用少量训练数据的情况下，比标准的小样本基线提高高达13.5%的宏平均F1值。我们的框架通过利用LLMs的自我改进能力进行分类和解释，为低资源环境提供了一种可扩展的策略。

## 🔬 方法详解

**问题定义**：论文旨在解决毒性内容检测中数据效率低和缺乏可解释性的问题。现有方法通常依赖于大量人工标注数据，这在低资源场景下是不可行的。此外，许多模型缺乏对决策过程的解释，难以进行调试和信任评估。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）的自增强能力，通过生成合成解释来提升毒性检测的性能和可解释性。通过让LLM解释其自身的预测结果，可以有效地利用LLM的知识，并减少对大量人工标注数据的依赖。

**技术框架**：SMARTER框架包含两个主要阶段：第一阶段是利用LLMs生成合成解释，并使用偏好优化进行对齐；第二阶段是通过跨模型训练来提升解释的质量。具体流程如下：
1. **阶段一：自增强解释生成**：使用LLM对数据进行预测，并要求LLM解释其预测结果。对于正确和错误的预测，都生成相应的解释。
2. **阶段二：偏好优化对齐**：使用生成的解释作为监督信号，通过偏好优化来对齐LLM的预测和解释。
3. **阶段三：跨模型训练**：使用更强大的LLM生成的解释作为目标，训练较弱的LLM，使其在风格和语义上与更强大的模型对齐。

**关键创新**：该论文的关键创新在于利用LLMs的自增强能力来生成合成解释，并将其用于提升毒性检测的性能和可解释性。与传统的监督学习方法相比，该方法可以显著减少对人工标注数据的依赖。此外，通过跨模型训练，可以将更强大的LLM的知识迁移到较弱的LLM，从而进一步提升性能。

**关键设计**：在第一阶段，使用提示工程来引导LLM生成高质量的解释。在第二阶段，使用偏好优化算法（如Direct Preference Optimization, DPO）来对齐LLM的预测和解释。在第三阶段，使用交叉熵损失函数来训练较弱的LLM，使其模仿更强大的LLM的预测和解释。

## 📊 实验亮点

实验结果表明，SMARTER框架在HateXplain、Latent Hate和Implicit Hate三个基准数据集上取得了显著的性能提升。例如，在HateXplain数据集上，SMARTER框架比标准的小样本基线提高了高达13.5%的宏平均F1值。此外，SMARTER框架在数据效率方面表现出色，仅使用少量训练数据即可达到与使用大量数据训练的模型相媲美的性能。

## 🎯 应用场景

SMARTER框架可应用于社交媒体平台、在线论坛等场景，用于自动检测和过滤有害内容，提升内容审核效率和准确性。该方法尤其适用于低资源语言或数据稀缺的场景，有助于构建更安全、更健康的网络环境。未来，该框架可扩展到其他文本分类任务，并与其他技术（如主动学习）结合，进一步提升性能。

## 📄 摘要（原文）

> WARNING: This paper contains examples of offensive materials. To address the proliferation of toxic content on social media, we introduce SMARTER, we introduce SMARTER, a data-efficient two-stage framework for explainable content moderation using Large Language Models (LLMs). In Stage 1, we leverage LLMs' own outputs to generate synthetic explanations for both correct and incorrect labels, enabling alignment via preference optimization with minimal human supervision. In Stage 2, we refine explanation quality through cross-model training, allowing weaker models to align stylistically and semantically with stronger ones. Experiments on three benchmark tasks -- HateXplain, Latent Hate, and Implicit Hate -- demonstrate that SMARTER enables LLMs to achieve up to a 13.5% macro-F1 improvement over standard few-shot baselines while using only a fraction of the full training data. Our framework offers a scalable strategy for low-resource settings by harnessing LLMs' self-improving capabilities for both classification and explanation.

