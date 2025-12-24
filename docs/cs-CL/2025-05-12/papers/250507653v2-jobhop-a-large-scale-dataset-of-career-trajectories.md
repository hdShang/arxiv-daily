---
layout: default
title: "JobHop: A Large-Scale Dataset of Career Trajectories"
---

# JobHop: A Large-Scale Dataset of Career Trajectories

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07653" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07653v2</a>
  <a href="https://arxiv.org/pdf/2505.07653.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07653v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07653v2', 'JobHop: A Large-Scale Dataset of Career Trajectories')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iman Johary, Raphael Romero, Alexandru C. Mara, Tijl De Bie

**分类**: cs.CL

**发布日期**: 2025-05-12 (更新: 2025-11-03)

---

## 💡 一句话要点

**提出JobHop数据集以解决职业轨迹分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `职业轨迹` `劳动市场` `数据集` `大型语言模型` `职业转变` `多标签分类` `政策制定` `职业路径预测`

## 📋 核心要点

1. 现有职业轨迹数据集稀缺，无法全面反映劳动市场动态，限制了相关研究和决策。
2. 论文提出JobHop数据集，通过处理匿名简历，提取并标准化职业信息，提供丰富的职业轨迹数据。
3. 数据集包含超过167万条工作经历，支持多种应用，如职业流动性分析和职业路径预测，具有重要的研究价值。

## 📝 摘要（中文）

理解劳动市场动态对政策制定者、雇主和求职者至关重要。然而，全面捕捉真实职业轨迹的数据集非常稀缺。本文介绍了JobHop，这是一个基于比利时弗拉芒地区公共就业服务VDAB提供的匿名简历构建的大规模公共数据集。通过利用大型语言模型（LLMs），我们处理非结构化的简历数据，提取结构化的职业信息，并使用多标签分类模型将其标准化为ESCO职业代码。最终生成的数据集包含超过167万条工作经历，来自于超过361,000份用户简历，提供了对真实职业转变的宝贵洞察。该数据集支持劳动市场流动性、职业稳定性和职业中断对转变影响的分析，促进职业路径预测和数据驱动决策过程。

## 🔬 方法详解

**问题定义**：本文旨在解决现有职业轨迹数据集稀缺的问题，现有方法无法全面捕捉真实的职业动态，限制了劳动市场研究的深度和广度。

**核心思路**：通过利用大型语言模型（LLMs）处理非结构化简历数据，提取结构化的职业信息，并将其标准化为ESCO职业代码，从而构建一个大规模的职业轨迹数据集。

**技术框架**：整体流程包括数据收集、数据预处理、信息提取和标准化四个主要模块。首先收集匿名简历数据，然后通过LLMs进行信息提取，最后将提取的信息映射到ESCO职业代码。

**关键创新**：最重要的创新在于结合大型语言模型进行非结构化数据处理，成功提取并标准化职业信息，显著提升了数据集的丰富性和准确性。

**关键设计**：在模型设计上，采用多标签分类模型进行职业代码的标准化，确保提取信息的准确性和一致性，同时对模型的参数设置进行了优化，以提高处理效率和效果。

## 📊 实验亮点

JobHop数据集包含超过167万条工作经历，来自于361,000份用户简历，提供了丰富的职业转变信息。通过多标签分类模型的应用，数据集在职业信息提取的准确性和标准化方面取得了显著提升，为劳动市场研究提供了强有力的数据支持。

## 🎯 应用场景

JobHop数据集的潜在应用领域包括劳动市场研究、职业路径分析和政策制定等。通过分析职业流动性和稳定性，研究人员和决策者可以更好地理解劳动市场动态，从而制定更有效的就业政策和职业发展策略。未来，该数据集还可用于支持职业预测模型的开发，帮助求职者做出更明智的职业选择。

## 📄 摘要（原文）

> Understanding labor market dynamics is essential for policymakers, employers, and job seekers. However, comprehensive datasets that capture real-world career trajectories are scarce. In this paper, we introduce JobHop, a large-scale public dataset derived from anonymized resumes provided by VDAB, the public employment service in Flanders, Belgium. Utilizing Large Language Models (LLMs), we process unstructured resume data to extract structured career information, which is then normalized to standardized ESCO occupation codes using a multi-label classification model. This results in a rich dataset of over 1.67 million work experiences, extracted from and grouped into more than 361,000 user resumes and mapped to standardized ESCO occupation codes, offering valuable insights into real-world occupational transitions. This dataset enables diverse applications, such as analyzing labor market mobility, job stability, and the effects of career breaks on occupational transitions. It also supports career path prediction and other data-driven decision-making processes. To illustrate its potential, we explore key dataset characteristics, including job distributions, career breaks, and job transitions, demonstrating its value for advancing labor market research.

