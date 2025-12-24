---
layout: default
title: "The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology"
---

# The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16765" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16765v2</a>
  <a href="https://arxiv.org/pdf/2509.16765.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16765v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16765v2', 'The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fagun Patel, Duc Q. Nguyen, Sang T. Truong, Jody Vaynshtok, Sanmi Koyejo, Nick Haber

**分类**: cs.CL, cs.AI, cs.SD, eess.AS

**发布日期**: 2025-09-20 (更新: 2025-10-08)

**备注**: EMNLP 2025 Oral Presentation

---

## 💡 一句话要点

**针对语音病理学，提出微调语言模型并进行全面评估，填补临床应用空白。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态语言模型` `言语病理学` `临床应用` `评估基准` `微调` `鲁棒性测试` `领域自适应`

## 📋 核心要点

1. 现有MLM在言语病理学领域应用不足，缺乏对其在高风险临床环境中性能的全面理解。
2. 构建了言语病理学中MLM用例分类，并设计了包含鲁棒性和敏感性测试的综合评估基准。
3. 实验表明，没有单一模型在所有任务中表现最佳，微调领域数据可显著提升模型性能。

## 📝 摘要（中文）

美国国立卫生研究院数据显示，超过340万儿童患有需要临床干预的言语障碍。言语病理学家（SLP）的数量远少于受影响的儿童，凸显了儿童护理方面的巨大差距以及对提高SLP工作效率的技术支持的迫切需求。目前先进的多模态语言模型（MLM）在支持SLP方面显示出潜力，但由于对其在高风险临床环境中的性能理解有限，其应用仍未得到充分探索。为了解决这个问题，我们与领域专家合作，开发了MLM在言语病理学中实际用例的分类。在此基础上，我们引入了第一个综合基准，用于评估MLM在五个核心用例中的表现，每个用例包含1000个手动标注的数据点。该基准包括在各种设置下的鲁棒性和敏感性测试，包括背景噪声、说话者性别和口音。对15个最先进的MLM的评估表明，没有一个模型在所有任务中始终优于其他模型。值得注意的是，我们发现系统性差异，模型在男性说话者上的表现更好，并且观察到思维链提示会降低标签空间大且决策边界窄的分类任务的性能。此外，我们研究了在领域特定数据上微调MLM，与基础模型相比，性能提高了10％以上。这些发现突出了当前MLM在言语病理学应用中的潜力和局限性，强调了进一步研究和有针对性的开发的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态语言模型（MLM）在言语病理学领域应用不足的问题。现有方法缺乏对MLM在高风险临床环境中性能的全面评估，阻碍了其在该领域的实际应用。此外，现有模型在不同性别、口音等因素下表现存在差异，需要更细致的分析和优化。

**核心思路**：论文的核心思路是构建一个全面的评估基准，用于评估MLM在言语病理学中的性能。通过与领域专家合作，定义了MLM在该领域的五个核心用例，并针对每个用例构建了包含1000个手动标注数据点的测试集。此外，论文还研究了在领域特定数据上微调MLM的效果，以提升其在该领域的性能。

**技术框架**：论文的技术框架主要包括以下几个部分：1）与领域专家合作，定义MLM在言语病理学中的五个核心用例；2）针对每个用例，构建包含1000个手动标注数据点的测试集；3）设计鲁棒性和敏感性测试，评估MLM在不同设置下的性能，包括背景噪声、说话者性别和口音；4）评估15个最先进的MLM在基准测试上的性能；5）研究在领域特定数据上微调MLM的效果。

**关键创新**：论文的关键创新在于构建了第一个针对言语病理学领域的MLM综合评估基准。该基准覆盖了该领域的五个核心用例，并包含了鲁棒性和敏感性测试，可以全面评估MLM在该领域的性能。此外，论文还发现了现有MLM在不同性别、口音等因素下表现存在差异，并提出了通过微调领域数据来提升模型性能的方法。

**关键设计**：论文的关键设计包括：1）与领域专家合作，确保用例定义的准确性和代表性；2）手动标注数据，保证测试集的质量；3）设计鲁棒性和敏感性测试，全面评估模型的性能；4）选择15个最先进的MLM进行评估，保证评估结果的可靠性；5）使用领域特定数据进行微调，提升模型在该领域的性能。具体参数设置、损失函数和网络结构等细节未在摘要中提及，属于未知信息。

## 📊 实验亮点

实验结果表明，没有单一MLM在所有任务中表现最佳，模型在男性说话者上的表现优于女性。通过在领域特定数据上微调MLM，性能提升超过10%。思维链提示在某些分类任务中反而会降低性能。这些发现为MLM在言语病理学领域的应用提供了重要的参考。

## 🎯 应用场景

该研究成果可应用于开发辅助言语病理学家（SLP）的智能工具，提高SLP的工作效率，并为更多患有言语障碍的儿童提供及时的诊断和治疗。未来，该研究可扩展到其他医疗领域，为构建更智能、更个性化的医疗服务提供技术支持。

## 📄 摘要（原文）

> According to the U.S. National Institutes of Health, more than 3.4 million children experience speech disorders that require clinical intervention. The number of speech-language pathologists (SLPs) is roughly 20 times fewer than the number of affected children, highlighting a significant gap in children's care and a pressing need for technological support that improves the productivity of SLPs. State-of-the-art multimodal language models (MLMs) show promise for supporting SLPs, but their use remains underexplored largely due to a limited understanding of their performance in high-stakes clinical settings. To address this gap, we collaborate with domain experts to develop a taxonomy of real-world use cases of MLMs in speech-language pathologies. Building on this taxonomy, we introduce the first comprehensive benchmark for evaluating MLM across five core use cases, each containing 1,000 manually annotated data points. This benchmark includes robustness and sensitivity tests under various settings, including background noise, speaker gender, and accent. Our evaluation of 15 state-of-the-art MLMs reveals that no single model consistently outperforms others across all tasks. Notably, we find systematic disparities, with models performing better on male speakers, and observe that chain-of-thought prompting can degrade performance on classification tasks with large label spaces and narrow decision boundaries. Furthermore, we study fine-tuning MLMs on domain-specific data, achieving improvements of over 10\% compared to base models. These findings highlight both the potential and limitations of current MLMs for speech-language pathology applications, underscoring the need for further research and targeted development.

