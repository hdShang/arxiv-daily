---
layout: default
title: Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting
---

# Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14288" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14288v1</a>
  <a href="https://arxiv.org/pdf/2512.14288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14288v1" onclick="toggleFavorite(this, '2512.14288v1', 'Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Bouchouras, Dimitrios Doumanas, Andreas Soularidis, Konstantinos Kotis, George A. Vouros

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**利用大型语言模型进行帕金森病监测和预警的协同本体工程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `本体工程` `大型语言模型` `帕金森病` `人机协作` `知识图谱` `医疗健康` `自然语言处理`

## 📋 核心要点

1. 现有本体工程方法在处理帕金森病等复杂领域时，构建全面、准确的本体面临挑战。
2. 论文提出结合人类专业知识与LLM能力的混合本体工程方法，提升本体的完整性和准确性。
3. 实验表明，人机协作方法（如X-HCOME和SimX-HCOME+）显著提高了本体的质量，接近专家构建的水平。

## 📝 摘要（中文）

本文探讨了将大型语言模型（LLM）集成到帕金森病（PD）监测和预警本体工程中的四种关键方法：One Shot（OS）提示技术、Chain of Thought（CoT）提示、X-HCOME和SimX-HCOME+。主要目标是确定LLM是否能够独立创建全面的本体，如果不能，人与LLM的协作是否能够实现这一目标。因此，本文评估了LLM在自动化本体开发中的有效性，以及通过人与LLM协作实现的增强效果。

## 🔬 方法详解

**问题定义**：现有本体工程方法在构建帕金森病监测和预警本体时，面临着本体不完整、准确性不足的问题。传统方法依赖于领域专家手动构建，效率低且容易遗漏关键概念和关系。因此，需要一种更高效、更全面的方法来构建高质量的本体。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的知识推理和生成能力，结合人类专家的领域知识，实现人机协同的本体工程。通过LLM自动生成本体的初始版本，然后由人类专家进行审查、修正和完善，从而提高本体的质量和构建效率。

**技术框架**：论文提出了两种人机协同的本体工程方法：X-HCOME和SimX-HCOME+。X-HCOME是一种混合方法，将人类专业知识与LLM能力相结合，用于本体构建。SimX-HCOME+进一步强调持续的人工监督和迭代改进，以创建更全面和准确的本体。整体流程包括：1) 使用One-Shot或CoT提示LLM生成初始本体；2) 人类专家审查和修改LLM生成的本体；3) 使用X-HCOME或SimX-HCOME+进行迭代改进。

**关键创新**：论文的关键创新在于提出了人机协同的本体工程框架，并验证了其在帕金森病监测和预警领域的有效性。与传统的纯人工或纯LLM方法相比，该框架能够更好地结合LLM的生成能力和人类专家的领域知识，从而构建更高质量的本体。

**关键设计**：论文使用了One-Shot和Chain-of-Thought提示技术来引导LLM生成本体。X-HCOME和SimX-HCOME+的关键设计在于强调人类专家的持续参与和迭代改进。SimX-HCOME+特别强调了持续的人工监督，确保本体的准确性和完整性。具体的参数设置和网络结构取决于所使用的LLM模型。

## 📊 实验亮点

实验结果表明，人机协同方法（X-HCOME和SimX-HCOME+）显著提高了本体的完整性和准确性，生成的本体与专家构建的本体非常相似。SimX-HCOME+通过持续的人工监督和迭代改进，进一步提升了本体的质量。这些结果验证了人机协同在本体工程中的潜力。

## 🎯 应用场景

该研究成果可应用于医疗健康领域，特别是帕金森病等慢性疾病的监测和预警。通过构建高质量的领域本体，可以支持智能诊断、个性化治疗和远程健康管理。未来，该方法还可以推广到其他复杂领域的知识图谱构建，例如金融、法律和教育等。

## 📄 摘要（原文）

> This paper explores the integration of Large Language Models (LLMs) in the engineering of a Parkinson's Disease (PD) monitoring and alerting ontology through four key methodologies: One Shot (OS) prompt techniques, Chain of Thought (CoT) prompts, X-HCOME, and SimX-HCOME+. The primary objective is to determine whether LLMs alone can create comprehensive ontologies and, if not, whether human-LLM collaboration can achieve this goal. Consequently, the paper assesses the effectiveness of LLMs in automated ontology development and the enhancement achieved through human-LLM collaboration.
>   Initial ontology generation was performed using One Shot (OS) and Chain of Thought (CoT) prompts, demonstrating the capability of LLMs to autonomously construct ontologies for PD monitoring and alerting. However, these outputs were not comprehensive and required substantial human refinement to enhance their completeness and accuracy.
>   X-HCOME, a hybrid ontology engineering approach that combines human expertise with LLM capabilities, showed significant improvements in ontology comprehensiveness. This methodology resulted in ontologies that are very similar to those constructed by experts.
>   Further experimentation with SimX-HCOME+, another hybrid methodology emphasizing continuous human supervision and iterative refinement, highlighted the importance of ongoing human involvement. This approach led to the creation of more comprehensive and accurate ontologies.
>   Overall, the paper underscores the potential of human-LLM collaboration in advancing ontology engineering, particularly in complex domains like PD. The results suggest promising directions for future research, including the development of specialized GPT models for ontology construction.

