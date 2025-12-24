---
layout: default
title: "Think Less, Label Better: Multi-Stage Domain-Grounded Synthetic Data Generation for Fine-Tuning Large Language Models in Telecommunications"
---

# Think Less, Label Better: Multi-Stage Domain-Grounded Synthetic Data Generation for Fine-Tuning Large Language Models in Telecommunications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25736" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25736v1</a>
  <a href="https://arxiv.org/pdf/2509.25736.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25736v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25736v1', 'Think Less, Label Better: Multi-Stage Domain-Grounded Synthetic Data Generation for Fine-Tuning Large Language Models in Telecommunications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenhua Shi, Gregor Macdonald, Bhavika Jalli, Wanlu Lei, John Zou, Mridul Jain, Joji Philip

**分类**: cs.CL, cs.AI, cs.IT, cs.NI

**发布日期**: 2025-09-30

**备注**: 6 pages, 6 figures, 5 tables

---

## 💡 一句话要点

**提出基于领域知识图谱的多阶段合成数据生成方法，用于电信领域大语言模型微调。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据生成` `大语言模型微调` `领域知识图谱` `检索增强生成` `电信网络故障排除`

## 📋 核心要点

1. 人工标注领域特定数据成本高昂，尤其是在电信等需要专业知识的场景。
2. 提出一种全自动的检索增强流水线，基于领域知识图谱生成高质量合成问答数据。
3. 通过定制的RAGAS评分过滤低质量样本，生成的数据适用于强化微调，提升模型性能。

## 📝 摘要（中文）

大型语言模型（LLM）的成功很大程度上依赖于大规模、高质量的指令遵循和强化学习数据集。然而，通过人工标注生成此类数据非常耗时，尤其是在电信网络故障排除等特定领域任务中，准确的响应需要深厚的技术专业知识和上下文理解。本文提出了一种全自动、检索增强的流水线，用于生成基于结构化领域知识的合成问答（QA）对。我们的多阶段框架集成了检索器、基础生成器和精炼模型，利用从领域特定知识图谱中检索到的文档来合成和增强QA对。为了确保数据质量，我们采用定制的基于RAGAS的评分来过滤低质量样本，从而生成适用于强化微调（RFT）的高质量数据集。我们在一个真实的电信场景中，重点关注无线接入网（RAN）故障排除，验证了我们的方法。结果表明，该流水线无需人工干预即可生成复杂的、上下文丰富的故障排除解决方案计划。这项工作为在专业领域构建指令和强化数据集提供了一种可扩展的解决方案，显著降低了对人工标注的依赖，同时保持了较高的技术保真度。

## 🔬 方法详解

**问题定义**：论文旨在解决电信领域，特别是无线接入网（RAN）故障排除中，缺乏高质量、大规模的指令遵循和强化学习数据集的问题。现有方法依赖于人工标注，成本高、耗时，且需要领域专家参与，难以扩展。

**核心思路**：核心思路是利用领域知识图谱，通过检索增强生成（RAG）技术，自动生成合成问答数据。通过多阶段的生成和精炼过程，以及基于RAGAS的质量评估和过滤，保证生成数据的质量，从而降低对人工标注的依赖。

**技术框架**：该框架包含三个主要阶段：1) **检索器**：从领域知识图谱中检索相关文档；2) **基础生成器**：基于检索到的文档生成初始的问答对；3) **精炼模型**：对生成的问答对进行优化和改进，提升质量和一致性。此外，还包括一个基于RAGAS的**质量评估模块**，用于过滤低质量的样本。

**关键创新**：关键创新在于将检索增强生成技术与领域知识图谱相结合，并采用多阶段的生成和精炼流程，以及定制的RAGAS评分机制。这种方法能够有效地生成高质量的合成数据，显著降低了对人工标注的需求。与传统的纯人工标注方法相比，该方法更具可扩展性和效率。

**关键设计**：论文中定制了基于RAGAS的评分指标，用于评估生成数据的质量，包括上下文相关性、答案的准确性和一致性等。具体的参数设置和模型选择（例如，检索器、生成器和精炼模型的具体架构）在论文中可能有所描述，但摘要中未明确提及。损失函数和网络结构等细节也需要参考原文。

## 📊 实验亮点

该研究在真实的电信场景中进行了验证，证明了该方法能够生成复杂的、上下文丰富的故障排除解决方案计划，且无需人工干预。通过定制的RAGAS评分过滤低质量样本，保证了生成数据的质量，从而提升了微调后模型的性能。具体的性能数据和提升幅度需要在论文中查找。

## 🎯 应用场景

该研究成果可广泛应用于电信、金融、医疗等专业领域，为这些领域的大语言模型微调提供高质量的训练数据。通过降低对人工标注的依赖，可以加速领域模型的开发和部署，提升模型在特定任务上的性能，例如故障诊断、客户服务、知识问答等。该方法还可用于构建智能助手和自动化解决方案，提高工作效率。

## 📄 摘要（原文）

> The success of large language models (LLMs) depends heavily on large-scale, high-quality instruction-following and reinforcement datasets. However, generating such data through human annotation is prohibitively time-consuming particularly for domain-specific tasks like telecom network troubleshooting, where accurate responses require deep technical expertise and contextual understanding. In this paper, we present a fully automated, retrieval-augmented pipeline for generating synthetic question-answer (QA) pairs grounded in structured domain knowledge. Our multi-stage framework integrates a retriever, base generator, and refinement model to synthesize and enhance QA pairs using documents retrieved from a domain-specific knowledge graph. To ensure data quality, we employ customized RAGAS-based scoring to filter low-quality samples, producing a high-quality dataset suitable for reinforcement fine-tuning (RFT). We demonstrate our approach in a real-world telecom scenario focused on radio access network (RAN) troubleshooting. The resulting pipeline generates complex, context-rich troubleshooting solution plans without human intervention. This work offers a scalable solution for building instruction and reinforcement datasets in specialized domains, significantly reducing dependence on manual labeling while maintaining high technical fidelity.

