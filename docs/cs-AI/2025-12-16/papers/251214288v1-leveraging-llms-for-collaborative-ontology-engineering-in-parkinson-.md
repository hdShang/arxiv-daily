---
layout: default
title: Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting
---

# Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14288" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14288v1</a>
  <a href="https://arxiv.org/pdf/2512.14288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14288v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14288v1', 'Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Bouchouras, Dimitrios Doumanas, Andreas Soularidis, Konstantinos Kotis, George A. Vouros

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**利用大型语言模型进行帕金森病监测和预警的协同本体工程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `本体工程` `大型语言模型` `人机协作` `帕金森病` `知识图谱`

## 📋 核心要点

1. 现有本体工程方法在处理帕金森病等复杂领域时，面临本体构建不全面、准确性不足的挑战。
2. 论文提出人机协作的本体工程方法，结合LLM的生成能力和人类专家的知识，迭代优化本体。
3. 实验表明，人机协作方法显著提升了本体的全面性和准确性，接近专家构建的本体水平。

## 📝 摘要（中文）

本文探讨了将大型语言模型（LLM）集成到帕金森病（PD）监测和预警本体工程中的四种关键方法：One Shot（OS）提示技术、Chain of Thought（CoT）提示、X-HCOME和SimX-HCOME+。主要目标是确定LLM是否能够独立创建全面的本体，如果不能，人机协作是否能够实现这一目标。因此，本文评估了LLM在自动化本体开发中的有效性，以及通过人机协作实现的增强效果。

## 🔬 方法详解

**问题定义**：论文旨在解决帕金森病（PD）监测和预警领域本体构建的问题。现有本体构建方法，特别是完全依赖人工构建的方法，耗时且容易出错，难以保证本体的全面性和准确性。而完全依赖LLM自动构建本体，又面临LLM知识的局限性和幻觉问题，导致生成的本体不够完善。

**核心思路**：论文的核心思路是结合人类专家知识和LLM的生成能力，通过人机协作的方式迭代构建本体。利用LLM的快速生成能力，生成初步的本体结构和概念，然后由人类专家进行审核、修正和补充，再将修正后的本体反馈给LLM，进行下一轮的迭代优化。

**技术框架**：论文提出了两种人机协作的本体工程方法：X-HCOME和SimX-HCOME+。X-HCOME是一种混合本体工程方法，强调人类专家和LLM的协同工作。SimX-HCOME+则进一步强调持续的人工监督和迭代优化。两种方法都包含以下主要阶段：1) 使用One Shot或Chain of Thought提示LLM生成初始本体；2) 人类专家审核和修改LLM生成的本体；3) 将修改后的本体反馈给LLM，进行迭代优化。

**关键创新**：论文的关键创新在于提出了人机协作的本体工程框架，并验证了该框架在帕金森病监测和预警领域的有效性。与完全依赖人工或LLM的方法相比，人机协作方法能够更好地平衡本体的全面性和准确性，并显著提高本体构建的效率。

**关键设计**：论文中，提示工程（Prompt Engineering）是关键设计之一。通过设计合适的One Shot和Chain of Thought提示，引导LLM生成高质量的初始本体。此外，迭代优化的次数和人类专家参与的程度也是影响本体质量的关键参数。SimX-HCOME+方法中，人类专家需要对LLM生成的本体进行细致的审核和修改，并提供详细的反馈，以便LLM能够更好地学习和改进。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14288v1/LLMs_and_PD_v15-2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14288v1/output-9.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，X-HCOME和SimX-HCOME+等人机协作方法显著提高了本体的全面性和准确性，生成的本体与专家构建的本体非常相似。SimX-HCOME+通过持续的人工监督和迭代优化，进一步提升了本体的质量，验证了人机协作在本体工程中的重要性。

## 🎯 应用场景

该研究成果可应用于医疗健康领域，特别是帕金森病等慢性疾病的监测和预警。构建的本体可以作为知识库，支持智能诊断、个性化治疗方案推荐和患者管理。此外，该研究提出的协同本体工程方法也可以推广到其他复杂领域，如金融、法律等。

## 📄 摘要（原文）

> This paper explores the integration of Large Language Models (LLMs) in the engineering of a Parkinson's Disease (PD) monitoring and alerting ontology through four key methodologies: One Shot (OS) prompt techniques, Chain of Thought (CoT) prompts, X-HCOME, and SimX-HCOME+. The primary objective is to determine whether LLMs alone can create comprehensive ontologies and, if not, whether human-LLM collaboration can achieve this goal. Consequently, the paper assesses the effectiveness of LLMs in automated ontology development and the enhancement achieved through human-LLM collaboration.
>   Initial ontology generation was performed using One Shot (OS) and Chain of Thought (CoT) prompts, demonstrating the capability of LLMs to autonomously construct ontologies for PD monitoring and alerting. However, these outputs were not comprehensive and required substantial human refinement to enhance their completeness and accuracy.
>   X-HCOME, a hybrid ontology engineering approach that combines human expertise with LLM capabilities, showed significant improvements in ontology comprehensiveness. This methodology resulted in ontologies that are very similar to those constructed by experts.
>   Further experimentation with SimX-HCOME+, another hybrid methodology emphasizing continuous human supervision and iterative refinement, highlighted the importance of ongoing human involvement. This approach led to the creation of more comprehensive and accurate ontologies.
>   Overall, the paper underscores the potential of human-LLM collaboration in advancing ontology engineering, particularly in complex domains like PD. The results suggest promising directions for future research, including the development of specialized GPT models for ontology construction.

