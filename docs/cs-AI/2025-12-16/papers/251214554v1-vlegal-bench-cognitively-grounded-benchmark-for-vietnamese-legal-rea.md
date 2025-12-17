---
layout: default
title: VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models
---

# VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models

**arXiv**: [2512.14554v1](https://arxiv.org/abs/2512.14554) | [PDF](https://arxiv.org/pdf/2512.14554.pdf)

**作者**: Nguyen Tien Dong, Minh-Anh Nguyen, Thanh Dat Hoang, Nguyen Tuan Ngoc, Dao Xuan Quang Minh, Phan Phi Hai, Nguyen Thi Ngoc Anh, Dang Van Tu, Binh Vu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出VLegal-Bench基准以解决越南法律领域大语言模型评估的标准化与认知深度问题**

🎯 **匹配领域**: **强化学习**

**关键词**: `法律基准` `越南法律` `大语言模型评估` `认知分类法` `法律推理` `专家标注` `检索增强生成` `场景化问题解决`

## 📋 核心要点

1. 核心问题：越南法律复杂多变，现有评估方法缺乏标准化基准，难以系统衡量大语言模型的法律推理能力。
2. 方法要点：基于布鲁姆认知分类法设计多层次任务，通过专家标注构建权威数据集，模拟真实法律工作流程。
3. 实验或效果：构建包含10,450个样本的基准，提供透明评估框架，支持AI法律系统开发，提升模型可靠性和可解释性。

## 📝 摘要（中文）

大语言模型的快速发展为人工智能在法律领域的应用开辟了新可能。然而，越南法律的复杂性、层级结构和频繁修订给评估这些模型如何解释和利用法律知识带来了巨大挑战。为填补这一空白，越南法律基准被引入，这是首个旨在系统评估大语言模型在越南法律任务上表现的综合性基准。基于布鲁姆认知分类法，VLegal-Bench通过设计反映实际使用场景的任务，涵盖了多个层次的法律理解。该基准包含10,450个样本，通过严格的标注流程生成，法律专家使用我们的标注系统对每个实例进行标注和交叉验证，确保每个样本都基于权威法律文件，并模拟真实世界法律助手的工作流程，包括一般法律问答、检索增强生成、多步推理和针对越南法律的场景化问题解决。通过提供一个标准化、透明且基于认知科学的评估框架，VLegal-Bench为评估大语言模型在越南法律环境中的表现奠定了坚实基础，并支持开发更可靠、可解释且符合伦理的AI辅助法律系统。

## 🔬 方法详解

VLegal-Bench的整体框架是一个基于认知科学的标准化评估基准，核心方法包括任务设计、数据生成和验证流程。关键技术创新点在于结合布鲁姆认知分类法，设计多层次法律理解任务，如问答、检索增强生成、多步推理和场景化问题解决，以反映实际法律应用场景。与现有方法的主要区别在于其专门针对越南法律特性，通过严格专家标注和交叉验证确保数据权威性，并模拟真实法律助手工作流程，提供更全面和实用的评估标准。

## 📊 实验亮点

构建了首个针对越南法律的综合性基准，包含10,450个专家标注样本，基于认知分类法设计多层次任务，为评估大语言模型提供标准化框架，支持开发更可靠的AI法律系统。

## 🎯 应用场景

该研究可应用于越南法律领域的AI辅助系统开发，如智能法律咨询、文档分析、案例检索和决策支持，提升法律服务的效率和准确性，促进法律科技发展。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has enabled new possibilities for applying artificial intelligence within the legal domain. Nonetheless, the complexity, hierarchical organization, and frequent revisions of Vietnamese legislation pose considerable challenges for evaluating how well these models interpret and utilize legal knowledge. To address this gap, Vietnamese Legal Benchmark (VLegal-Bench) is introduced, the first comprehensive benchmark designed to systematically assess LLMs on Vietnamese legal tasks. Informed by Bloom's cognitive taxonomy, VLegal-Bench encompasses multiple levels of legal understanding through tasks designed to reflect practical usage scenarios. The benchmark comprises 10,450 samples generated through a rigorous annotation pipeline, where legal experts label and cross-validate each instance using our annotation system to ensure every sample is grounded in authoritative legal documents and mirrors real-world legal assistant workflows, including general legal questions and answers, retrieval-augmented generation, multi-step reasoning, and scenario-based problem solving tailored to Vietnamese law. By providing a standardized, transparent, and cognitively informed evaluation framework, VLegal-Bench establishes a solid foundation for assessing LLM performance in Vietnamese legal contexts and supports the development of more reliable, interpretable, and ethically aligned AI-assisted legal systems.

