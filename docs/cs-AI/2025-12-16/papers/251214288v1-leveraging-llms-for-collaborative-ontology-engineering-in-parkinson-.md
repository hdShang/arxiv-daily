---
layout: default
title: Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting
---

# Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting

**arXiv**: [2512.14288v1](https://arxiv.org/abs/2512.14288) | [PDF](https://arxiv.org/pdf/2512.14288.pdf)

**作者**: Georgios Bouchouras, Dimitrios Doumanas, Andreas Soularidis, Konstantinos Kotis, George A. Vouros

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出人机协作本体工程方法，以提升帕金森病监测与警报领域的本体构建效果。**

**关键词**: `本体工程` `大型语言模型` `帕金森病监测` `人机协作` `思维链提示` `混合方法` `知识表示` `医疗人工智能`

## 📋 核心要点

1. 核心问题：LLMs在自动化本体构建中难以独立生成全面且准确的本体，尤其在复杂医学领域如帕金森病监测与警报。
2. 方法要点：提出混合本体工程方法，如X-HCOME和SimX-HCOME+，结合人类专业知识和LLM能力，通过迭代协作提升本体质量。
3. 实验或效果：人机协作方法显著提高了本体的全面性和准确性，接近专家构建水平，验证了协作的有效性。

## 📝 摘要（中文）

本文探讨了将大型语言模型（LLMs）集成到帕金森病（PD）监测与警报本体工程中的四种关键方法：单次提示（OS）、思维链（CoT）提示、X-HCOME和SimX-HCOME+。主要目标是确定LLMs是否能独立创建全面本体，以及人机协作是否能实现这一目标。因此，本文评估了LLMs在自动化本体开发中的有效性，以及通过人机协作实现的提升。初始本体生成使用OS和CoT提示进行，展示了LLMs自主构建PD监测与警报本体的能力，但这些输出不够全面，需要大量人工细化以提高完整性和准确性。X-HCOME是一种结合人类专业知识和LLM能力的混合本体工程方法，显著提高了本体的全面性，结果与专家构建的本体非常相似。进一步实验使用SimX-HCOME+，另一种强调持续人类监督和迭代细化的混合方法，突出了持续人类参与的重要性，该方法创建了更全面和准确的本体。总体而言，本文强调了人机协作在推进本体工程中的潜力，特别是在PD等复杂领域。结果为未来研究指明了有前景的方向，包括开发专门用于本体构建的GPT模型。

## 🔬 方法详解

论文的核心方法包括四种本体工程方法：单次提示（OS）和思维链（CoT）提示用于初始LLM自主本体生成，X-HCOME作为混合方法结合人类输入和LLM输出进行协作构建，SimX-HCOME+则强调持续人类监督和迭代细化。整体框架基于人机协作，关键技术创新点在于将LLMs的自动化能力与人类专家的领域知识相结合，通过结构化流程优化本体开发。与现有方法的主要区别在于，传统方法可能依赖纯人工或纯自动化，而本文方法通过混合策略平衡效率和准确性，特别针对复杂医学领域设计。

## 📊 实验亮点

实验结果显示，人机协作方法（如X-HCOME和SimX-HCOME+）相比纯LLM方法（OS和CoT）显著提升了本体的全面性和准确性，接近专家构建标准，验证了协作在复杂领域本体工程中的优势。

## 🎯 应用场景

该研究可应用于帕金森病等慢性疾病的智能监测与警报系统，通过构建高质量本体支持知识表示和推理，提升医疗诊断、患者管理和远程护理的自动化水平，具有实际医疗价值。

## 📄 摘要（原文）

> This paper explores the integration of Large Language Models (LLMs) in the engineering of a Parkinson's Disease (PD) monitoring and alerting ontology through four key methodologies: One Shot (OS) prompt techniques, Chain of Thought (CoT) prompts, X-HCOME, and SimX-HCOME+. The primary objective is to determine whether LLMs alone can create comprehensive ontologies and, if not, whether human-LLM collaboration can achieve this goal. Consequently, the paper assesses the effectiveness of LLMs in automated ontology development and the enhancement achieved through human-LLM collaboration.
>   Initial ontology generation was performed using One Shot (OS) and Chain of Thought (CoT) prompts, demonstrating the capability of LLMs to autonomously construct ontologies for PD monitoring and alerting. However, these outputs were not comprehensive and required substantial human refinement to enhance their completeness and accuracy.
>   X-HCOME, a hybrid ontology engineering approach that combines human expertise with LLM capabilities, showed significant improvements in ontology comprehensiveness. This methodology resulted in ontologies that are very similar to those constructed by experts.
>   Further experimentation with SimX-HCOME+, another hybrid methodology emphasizing continuous human supervision and iterative refinement, highlighted the importance of ongoing human involvement. This approach led to the creation of more comprehensive and accurate ontologies.
>   Overall, the paper underscores the potential of human-LLM collaboration in advancing ontology engineering, particularly in complex domains like PD. The results suggest promising directions for future research, including the development of specialized GPT models for ontology construction.

