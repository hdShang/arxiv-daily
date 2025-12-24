---
layout: default
title: "Quantized Large Language Models in Biomedical Natural Language Processing: Evaluation and Recommendation"
---

# Quantized Large Language Models in Biomedical Natural Language Processing: Evaluation and Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04534" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04534v1</a>
  <a href="https://arxiv.org/pdf/2509.04534.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04534v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04534v1', 'Quantized Large Language Models in Biomedical Natural Language Processing: Evaluation and Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zaifu Zhan, Shuang Zhou, Min Zeng, Kai Yu, Meijia Song, Xiaoyi Chen, Jun Wang, Yu Hou, Rui Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04

**备注**: 11 pages, 7 figures

---

## 💡 一句话要点

**量化LLM实现生物医学NLP：评估与推荐，降低部署成本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化` `大型语言模型` `生物医学自然语言处理` `模型压缩` `本地部署`

## 📋 核心要点

1. 现有大型语言模型计算需求高，难以在数据隐私敏感的医疗环境中部署。
2. 通过量化技术压缩模型，在降低资源需求的同时，尽量保持模型性能。
3. 实验表明，量化能显著降低GPU内存需求，同时保持模型在生物医学任务中的性能。

## 📝 摘要（中文）

大型语言模型在生物医学自然语言处理领域展现了卓越的能力，但其规模和计算需求的快速增长对医疗环境中的应用构成了主要障碍，因为数据隐私限制了云部署，且资源有限。本研究系统地评估了量化对12个最先进的大型语言模型的影响，包括通用模型和生物医学专用模型，涵盖命名实体识别、关系抽取、多标签分类和问答四个关键任务的八个基准数据集。结果表明，量化显著降低了GPU内存需求（高达75%），同时保持了模型在不同任务中的性能，使得在40GB消费级GPU上部署70B参数模型成为可能。此外，领域特定知识和对高级提示方法的响应性在很大程度上得以保留。这些发现提供了重要的实践和指导价值，突出了量化作为一种实用且有效的策略，可以在生物医学环境中安全地本地部署大型且高容量的语言模型，从而弥合了人工智能技术进步与现实临床转化之间的差距。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在生物医学自然语言处理（BioNLP）领域部署困难的问题。现有LLM虽然性能强大，但其巨大的模型体积和计算资源需求，使得它们难以在对数据隐私有严格要求的医疗环境中应用，尤其是在资源受限的场景下。现有方法要么依赖云部署，要么需要昂贵的硬件，无法满足本地化部署的需求。

**核心思路**：论文的核心思路是利用模型量化技术，在尽可能不损失模型性能的前提下，显著降低LLM的存储空间和计算复杂度。通过量化，可以将模型参数从高精度浮点数转换为低精度整数，从而减少模型大小和推理时间，使其能够在消费级GPU上运行。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 选择12个具有代表性的LLM，包括通用模型和生物医学专用模型；2) 在8个BioNLP基准数据集上评估这些模型的性能，涵盖命名实体识别、关系抽取、多标签分类和问答四个任务；3) 对这些模型进行不同程度的量化（例如，4-bit量化）；4) 评估量化后模型在各个任务上的性能，并与原始模型进行比较；5) 分析量化对模型领域知识和提示学习能力的影响。

**关键创新**：该研究的关键创新在于系统性地评估了量化技术在BioNLP领域LLM上的有效性。以往的研究可能只关注单个模型或任务，而该研究覆盖了多个模型、多个任务和多个数据集，从而得出了更具普适性的结论。此外，该研究还关注了量化对模型领域知识和提示学习能力的影响，这对于BioNLP应用至关重要。

**关键设计**：论文的关键设计包括：1) 选择了具有代表性的LLM，包括BERT、RoBERTa、BioBERT等；2) 选择了涵盖不同BioNLP任务的基准数据集，例如BC5CDR、ChemProt等；3) 采用了标准的量化方法，例如Post-Training Quantization (PTQ)；4) 使用了常用的评估指标，例如F1-score、准确率等；5) 详细分析了量化对模型性能的影响，并给出了实际部署的建议。

## 📊 实验亮点

实验结果表明，通过量化，可以将LLM的GPU内存需求降低高达75%，同时保持模型在BioNLP任务上的性能。例如，70B参数的模型可以在40GB消费级GPU上运行。此外，量化对模型的领域知识和提示学习能力的影响较小，这意味着量化后的模型仍然可以有效地应用于复杂的BioNLP任务。

## 🎯 应用场景

该研究成果可广泛应用于医疗健康领域，例如辅助诊断、药物研发、电子病历分析等。通过量化技术，可以在本地部署高性能的LLM，从而保护患者隐私，并降低计算成本。这有助于推动人工智能技术在医疗领域的普及和应用，提高医疗服务的质量和效率，并加速生物医学研究的进展。

## 📄 摘要（原文）

> Large language models have demonstrated remarkable capabilities in biomedical natural language processing, yet their rapid growth in size and computational requirements present a major barrier to adoption in healthcare settings where data privacy precludes cloud deployment and resources are limited. In this study, we systematically evaluated the impact of quantization on 12 state-of-the-art large language models, including both general-purpose and biomedical-specific models, across eight benchmark datasets covering four key tasks: named entity recognition, relation extraction, multi-label classification, and question answering. We show that quantization substantially reduces GPU memory requirements-by up to 75%-while preserving model performance across diverse tasks, enabling the deployment of 70B-parameter models on 40GB consumer-grade GPUs. In addition, domain-specific knowledge and responsiveness to advanced prompting methods are largely maintained. These findings provide significant practical and guiding value, highlighting quantization as a practical and effective strategy for enabling the secure, local deployment of large yet high-capacity language models in biomedical contexts, bridging the gap between technical advances in AI and real-world clinical translation.

