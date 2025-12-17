---
layout: default
title: Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting
---

# Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14288" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14288</a>
  <a href="https://arxiv.org/pdf/2512.14288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14288" onclick="toggleFavorite(this, '2512.14288', 'Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Bouchouras, Dimitrios Doumanas, Andreas Soularidis, Konstantinos Kotis, George A. Vouros

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**利用大型语言模型进行帕金森病监测和预警的协同本体工程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `本体工程` `人机协作` `帕金森病` `知识图谱` `医疗健康` `自动化`

## 📋 核心要点

1. 现有本体工程在帕金森病等复杂领域面临挑战，需要耗费大量专家知识和时间，自动化程度低。
2. 论文探索人机协作模式，利用大型语言模型（LLM）的知识推理能力，结合人工监督和迭代改进，提升本体构建效率和质量。
3. 实验表明，纯LLM生成的本体不够全面，但通过X-HCOME和SimX-HCOME+等人机协作方法，本体的完整性和准确性得到显著提升。

## 📝 摘要（中文）

本文探讨了将大型语言模型（LLM）集成到帕金森病（PD）监测和预警本体的工程中，采用了四种关键方法：One Shot（OS）提示技术、Chain of Thought（CoT）提示、X-HCOME 和 SimX-HCOME+。主要目标是确定 LLM 是否能够独立创建全面的本体，如果不能，人机协作是否能够实现这一目标。因此，本文评估了 LLM 在自动化本体开发中的有效性，以及通过人机协作实现的增强效果。初步的本体生成使用 One Shot（OS）和 Chain of Thought（CoT）提示执行，展示了 LLM 自主构建 PD 监测和预警本体的能力。然而，这些输出并不全面，需要大量的人工改进以提高其完整性和准确性。X-HCOME 是一种混合本体工程方法，结合了人类专业知识和 LLM 的能力，在本体的全面性方面显示出显著的改进。这种方法产生的本体与专家构建的本体非常相似。通过 SimX-HCOME+ 进一步实验，这是一种强调持续人工监督和迭代改进的另一种混合方法，突出了持续人工参与的重要性。这种方法能够创建更全面和准确的本体。总的来说，本文强调了人机协作在推进本体工程方面的潜力，特别是在像 PD 这样的复杂领域。结果表明了未来研究的有希望的方向，包括开发用于本体构建的专用 GPT 模型。

## 🔬 方法详解

**问题定义**：论文旨在解决帕金森病（PD）监测和预警领域本体构建的问题。现有本体构建方法依赖于领域专家，耗时且成本高昂，难以快速适应新的知识和需求。纯粹依赖LLM自动构建的本体，在完整性和准确性方面存在不足，无法满足实际应用需求。

**核心思路**：论文的核心思路是结合人类专家知识和LLM的强大能力，通过人机协作的方式进行本体工程。利用LLM进行初步的本体生成和推理，然后由人类专家进行监督、修正和迭代改进，从而构建出更全面、准确且实用的本体。这种混合方法旨在弥补纯自动化和纯人工方法的不足，充分发挥各自的优势。

**技术框架**：论文提出了两种人机协作的本体工程方法：X-HCOME 和 SimX-HCOME+。两种方法都包含以下阶段：1) 使用 One-Shot 或 Chain-of-Thought 提示 LLM 生成初始本体；2) 人类专家对 LLM 生成的本体进行评估和修正；3) 将修正后的本体反馈给 LLM，进行迭代改进。SimX-HCOME+ 强调持续的人工监督和迭代，在每次迭代后都进行更细致的评估和修正。

**关键创新**：论文的关键创新在于提出了人机协作的本体工程框架，并验证了其在帕金森病监测和预警领域的有效性。与传统的本体工程方法相比，该方法能够显著提高本体构建的效率和质量。与纯自动化方法相比，该方法通过人工监督和迭代改进，保证了本体的准确性和实用性。

**关键设计**：论文中使用的 LLM 包括通用的大型语言模型，例如 GPT 系列。关键设计在于提示工程，即如何设计合适的提示（One-Shot 或 Chain-of-Thought）来引导 LLM 生成有用的本体。此外，人工监督和迭代改进的策略也是关键设计的一部分，需要领域专家参与，并根据实际情况进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14288/LLMs_and_PD_v15-2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14288/output-9.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，纯LLM生成的本体在完整性和准确性方面存在不足，需要人工干预。通过X-HCOME和SimX-HCOME+等人机协作方法，本体的质量得到显著提升，生成的本体与专家构建的本体非常相似。SimX-HCOME+由于强调持续的人工监督和迭代，能够生成更全面和准确的本体。

## 🎯 应用场景

该研究成果可应用于医疗健康领域，特别是帕金森病等慢性疾病的监测和预警。构建的本体可以作为知识库，支持智能诊断、个性化治疗方案推荐和患者管理。此外，该方法也适用于其他需要领域知识的本体构建任务，例如金融、法律等。

## 📄 摘要（原文）

> This paper explores the integration of Large Language Models (LLMs) in the engineering of a Parkinson's Disease (PD) monitoring and alerting ontology through four key methodologies: One Shot (OS) prompt techniques, Chain of Thought (CoT) prompts, X-HCOME, and SimX-HCOME+. The primary objective is to determine whether LLMs alone can create comprehensive ontologies and, if not, whether human-LLM collaboration can achieve this goal. Consequently, the paper assesses the effectiveness of LLMs in automated ontology development and the enhancement achieved through human-LLM collaboration.Initial ontology generation was performed using One Shot (OS) and Chain of Thought (CoT) prompts, demonstrating the capability of LLMs to autonomously construct ontologies for PD monitoring and alerting. However, these outputs were not comprehensive and required substantial human refinement to enhance their completeness and accuracy.X-HCOME, a hybrid ontology engineering approach that combines human expertise with LLM capabilities, showed significant improvements in ontology comprehensiveness. This methodology resulted in ontologies that are very similar to those constructed by experts.Further experimentation with SimX-HCOME+, another hybrid methodology emphasizing continuous human supervision and iterative refinement, highlighted the importance of ongoing human involvement. This approach led to the creation of more comprehensive and accurate ontologies.Overall, the paper underscores the potential of human-LLM collaboration in advancing ontology engineering, particularly in complex domains like PD. The results suggest promising directions for future research, including the development of specialized GPT models for ontology construction.

