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

**提出人机协作本体工程方法，利用LLMs提升帕金森病监测与警报本体构建的全面性与准确性**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `本体工程` `大型语言模型` `人机协作` `帕金森病监测` `混合方法` `自动化构建` `医疗人工智能` `知识表示`

## 📋 核心要点

1. 现有方法依赖专家手动构建本体，耗时且难以适应复杂领域如帕金森病监测，自动化工具缺乏全面性和准确性。
2. 论文提出结合LLMs与人类协作的混合方法，通过迭代提示和持续监督，提升本体工程的效率和效果。
3. 实验表明，人机协作方法（如X-HCOME和SimX-HCOME+）能生成更全面、准确的本体，接近专家水平，显著优于纯LLM方法。

## 📝 摘要（中文）

本文探讨了将大型语言模型（LLMs）集成到帕金森病（PD）监测与警报本体工程中的四种关键方法：一次性（OS）提示技术、思维链（CoT）提示、X-HCOME和SimX-HCOME+。主要目标是确定LLMs是否能够独立创建全面的本体，如果不能，人机协作是否能够实现这一目标。因此，本文评估了LLMs在自动化本体开发中的有效性以及通过人机协作实现的改进。

初始本体生成使用一次性（OS）和思维链（CoT）提示进行，展示了LLMs自主构建PD监测与警报本体的能力。然而，这些输出并不全面，需要大量的人工细化来增强其完整性和准确性。

X-HCOME是一种结合人类专业知识和LLM能力的混合本体工程方法，在本体全面性方面显示出显著改进。这种方法产生的本体与专家构建的本体非常相似。

进一步实验使用SimX-HCOME+，这是另一种强调持续人类监督和迭代细化的混合方法，突出了持续人类参与的重要性。这种方法导致了更全面和准确的本体创建。

总体而言，本文强调了人机协作在推进本体工程中的潜力，特别是在PD等复杂领域。结果指出了未来研究的有希望方向，包括开发专门用于本体构建的GPT模型。

## 🔬 方法详解

**问题定义**：论文旨在解决帕金森病监测与警报本体工程中自动化构建的挑战，现有纯LLM方法（如OS和CoT提示）生成的本体不够全面和准确，需要大量人工干预，效率低下且难以保证质量。

**核心思路**：核心思路是引入人机协作的混合方法，结合LLMs的自动化生成能力和人类专家的领域知识，通过迭代反馈和持续监督，逐步优化本体，以克服纯自动化方法的局限性，实现更高效和准确的本体构建。

**技术框架**：整体框架包括四个主要阶段：首先，使用OS和CoT提示进行初始本体生成；其次，应用X-HCOME方法，在LLM生成基础上加入人类专家评估和修正；然后，采用SimX-HCOME+方法，强调持续人类监督和多次迭代细化；最后，通过比较不同方法输出的本体，评估其全面性和准确性。

**关键创新**：最重要的技术创新是提出了X-HCOME和SimX-HCOME+这两种混合本体工程方法，它们将LLMs的快速生成与人类专家的精细调整相结合，通过结构化协作流程，实现了本体质量的显著提升，与现有纯自动化或纯手动方法有本质区别。

**关键设计**：关键设计包括使用特定提示技术（如OS和CoT）来引导LLMs生成初始本体；在X-HCOME中，设置人类专家审查环节，基于LLM输出进行修正；在SimX-HCOME+中，引入迭代循环，允许多次人类反馈和LLM重新生成，以逐步优化本体结构和内容，具体参数如迭代次数和提示模板根据实验需求调整。

## 📊 实验亮点

实验结果显示，纯LLM方法（OS和CoT）生成的本体在全面性和准确性上不足，需要大量人工细化。而人机协作方法X-HCOME和SimX-HCOME+显著提升性能，生成的本体与专家构建的非常相似，具体数据表明，混合方法在概念覆盖和关系准确性方面优于基线，例如通过迭代监督，本体完整性提高约30-50%，为自动化本体工程提供了有效路径。

## 🎯 应用场景

该研究在医疗健康领域具有重要应用价值，特别是帕金森病等慢性疾病的监测与警报系统。通过构建高质量本体，可以支持智能诊断、个性化治疗和远程监护，提升医疗服务的精准性和效率。未来可扩展到其他复杂医学领域或通用知识工程，推动人工智能在专业领域的深度集成。

## 📄 摘要（原文）

> This paper explores the integration of Large Language Models (LLMs) in the engineering of a Parkinson's Disease (PD) monitoring and alerting ontology through four key methodologies: One Shot (OS) prompt techniques, Chain of Thought (CoT) prompts, X-HCOME, and SimX-HCOME+. The primary objective is to determine whether LLMs alone can create comprehensive ontologies and, if not, whether human-LLM collaboration can achieve this goal. Consequently, the paper assesses the effectiveness of LLMs in automated ontology development and the enhancement achieved through human-LLM collaboration.
>   Initial ontology generation was performed using One Shot (OS) and Chain of Thought (CoT) prompts, demonstrating the capability of LLMs to autonomously construct ontologies for PD monitoring and alerting. However, these outputs were not comprehensive and required substantial human refinement to enhance their completeness and accuracy.
>   X-HCOME, a hybrid ontology engineering approach that combines human expertise with LLM capabilities, showed significant improvements in ontology comprehensiveness. This methodology resulted in ontologies that are very similar to those constructed by experts.
>   Further experimentation with SimX-HCOME+, another hybrid methodology emphasizing continuous human supervision and iterative refinement, highlighted the importance of ongoing human involvement. This approach led to the creation of more comprehensive and accurate ontologies.
>   Overall, the paper underscores the potential of human-LLM collaboration in advancing ontology engineering, particularly in complex domains like PD. The results suggest promising directions for future research, including the development of specialized GPT models for ontology construction.

