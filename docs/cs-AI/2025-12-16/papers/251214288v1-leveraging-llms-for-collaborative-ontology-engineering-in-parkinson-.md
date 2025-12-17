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

**提出人机协作本体工程方法，利用LLMs增强帕金森病监测与警报本体构建的完整性与准确性。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `大型语言模型` `本体工程` `人机协作` `帕金森病监测` `医疗本体` `智能提示` `知识表示` `混合方法`

## 📋 核心要点

1. 核心问题：LLMs在自动化本体工程中难以独立生成全面且准确的本体，尤其在复杂医学领域如帕金森病监测与警报。
2. 方法要点：提出X-HCOME和SimX-HCOME+混合方法，结合人类专业知识与LLMs能力，通过迭代协作提升本体质量。
3. 实验或效果：人机协作方法显著提高本体完整性和准确性，SimX-HCOME+在持续监督下实现最优性能，接近专家水平。

## 📝 摘要（中文）

本文探讨了将大型语言模型（LLMs）集成到帕金森病（PD）监测与警报本体工程中的四种关键方法：单次提示（OS）、思维链（CoT）提示、X-HCOME和SimX-HCOME+。主要目标是确定LLMs能否独立创建全面本体，若不能，人机协作是否能实现此目标。因此，本文评估了LLMs在自动化本体开发中的有效性以及通过人机协作实现的改进。初始本体生成使用OS和CoT提示进行，展示了LLMs自主构建PD监测与警报本体的能力，但这些输出不够全面，需要大量人工细化以提升完整性和准确性。X-HCOME是一种结合人类专业知识与LLM能力的混合本体工程方法，显著提高了本体全面性，产生的本体与专家构建的非常相似。进一步实验使用SimX-HCOME+，另一种强调持续人工监督和迭代细化的混合方法，突出了持续人工参与的重要性，该方法创建了更全面和准确的本体。总体而言，本文强调了人机协作在推进本体工程中的潜力，特别是在PD等复杂领域。结果指出了未来研究的有前景方向，包括开发用于本体构建的专用GPT模型。

## 🔬 方法详解

论文提出一个基于人机协作的本体工程框架，核心包括四种方法：单次提示（OS）和思维链（CoT）提示用于初始LLMs自主本体生成；X-HCOME作为混合方法，整合人类专家输入与LLMs输出进行协同构建；SimX-HCOME+进一步强调持续人工监督和迭代细化过程。关键创新点在于系统化评估LLMs在复杂领域本体工程中的能力，并设计结构化协作流程以弥补LLMs的不足。与现有方法的主要区别在于，传统本体工程多依赖专家手动构建或自动化工具，而本文首次系统探索LLMs与人力的协同作用，通过实验验证协作模式的有效性，为智能本体开发提供新范式。

## 📊 实验亮点

实验显示，纯LLMs方法（OS和CoT）生成的本体不全面，需人工细化；X-HCOME混合方法使本体接近专家构建水平；SimX-HCOME+在持续监督下实现最高完整性和准确性，验证了人机协作在复杂本体工程中的关键作用。

## 🎯 应用场景

该研究可应用于医学信息学领域，特别是慢性病如帕金森病的智能监测与警报系统开发，通过构建高质量本体支持数据集成、知识推理和临床决策辅助，提升医疗服务的个性化和实时性。

## 📄 摘要（原文）

> This paper explores the integration of Large Language Models (LLMs) in the engineering of a Parkinson's Disease (PD) monitoring and alerting ontology through four key methodologies: One Shot (OS) prompt techniques, Chain of Thought (CoT) prompts, X-HCOME, and SimX-HCOME+. The primary objective is to determine whether LLMs alone can create comprehensive ontologies and, if not, whether human-LLM collaboration can achieve this goal. Consequently, the paper assesses the effectiveness of LLMs in automated ontology development and the enhancement achieved through human-LLM collaboration.
>   Initial ontology generation was performed using One Shot (OS) and Chain of Thought (CoT) prompts, demonstrating the capability of LLMs to autonomously construct ontologies for PD monitoring and alerting. However, these outputs were not comprehensive and required substantial human refinement to enhance their completeness and accuracy.
>   X-HCOME, a hybrid ontology engineering approach that combines human expertise with LLM capabilities, showed significant improvements in ontology comprehensiveness. This methodology resulted in ontologies that are very similar to those constructed by experts.
>   Further experimentation with SimX-HCOME+, another hybrid methodology emphasizing continuous human supervision and iterative refinement, highlighted the importance of ongoing human involvement. This approach led to the creation of more comprehensive and accurate ontologies.
>   Overall, the paper underscores the potential of human-LLM collaboration in advancing ontology engineering, particularly in complex domains like PD. The results suggest promising directions for future research, including the development of specialized GPT models for ontology construction.

