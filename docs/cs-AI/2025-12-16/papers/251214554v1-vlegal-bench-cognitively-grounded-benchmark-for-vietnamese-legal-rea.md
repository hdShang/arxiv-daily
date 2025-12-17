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

**提出VLegal-Bench基准以解决越南法律领域大语言模型评估的标准化与认知深度不足问题**

**关键词**: `越南法律基准` `大语言模型评估` `认知分类法` `法律推理` `专家标注系统` `检索增强生成` `多步推理` `AI辅助法律系统`

## 📋 核心要点

1. 核心问题：越南法律复杂且频繁修订，现有方法缺乏标准化基准来评估大语言模型的法律推理能力，导致模型性能评估不全面。
2. 方法要点：基于布鲁姆认知分类法设计多层次法律任务，通过专家标注和交叉验证构建包含10,450个样本的基准，确保样本基于权威法律文件。
3. 实验或效果：VLegal-Bench提供了透明评估框架，支持开发更可靠的AI法律系统，但具体模型性能提升数据未知，需后续实验验证。

## 📝 摘要（中文）

随着大语言模型（LLMs）的快速发展，人工智能在法律领域的应用展现出新的可能性。然而，越南法律的复杂性、层级结构以及频繁修订，给评估这些模型如何解释和利用法律知识带来了巨大挑战。为填补这一空白，越南法律基准（VLegal-Bench）被引入，这是首个旨在系统评估LLMs在越南法律任务上表现的综合性基准。基于布鲁姆认知分类法，VLegal-Bench通过设计反映实际使用场景的任务，涵盖了多个层次的法律理解。该基准包含10,450个样本，通过严格的标注流程生成，其中法律专家使用我们的标注系统对每个实例进行标注和交叉验证，确保每个样本都基于权威法律文件，并模拟真实世界法律助手的工作流程，包括一般法律问答、检索增强生成、多步推理以及针对越南法律的场景化问题解决。通过提供一个标准化、透明且基于认知科学的评估框架，VLegal-Bench为评估LLMs在越南法律背景下的性能奠定了坚实基础，并支持开发更可靠、可解释且符合伦理的AI辅助法律系统。

## 🔬 方法详解

VLegal-Bench的整体框架是一个基于认知科学的标准化评估基准，核心方法包括：1）以布鲁姆认知分类法为指导，设计多层次法律理解任务，如问答、检索增强生成和多步推理；2）通过严格标注流程，由法律专家使用标注系统生成和验证10,450个样本，确保样本基于权威越南法律文件并模拟真实工作流程；3）关键技术创新在于将认知理论与法律实践结合，创建透明、可复现的评估体系。与现有方法的主要区别在于其专门针对越南法律定制，强调认知深度和实际场景，而非通用法律基准。

## 📊 实验亮点

VLegal-Bench构建了首个针对越南法律的综合性基准，包含10,450个专家验证样本，基于认知分类法设计任务，为LLMs评估提供标准化框架，但具体性能提升需模型测试后确定。

## 🎯 应用场景

该研究可应用于越南法律AI助手开发、法律教育工具、自动化法律咨询系统等领域，提升法律服务的效率和准确性，支持司法和合规场景的智能化。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has enabled new possibilities for applying artificial intelligence within the legal domain. Nonetheless, the complexity, hierarchical organization, and frequent revisions of Vietnamese legislation pose considerable challenges for evaluating how well these models interpret and utilize legal knowledge. To address this gap, Vietnamese Legal Benchmark (VLegal-Bench) is introduced, the first comprehensive benchmark designed to systematically assess LLMs on Vietnamese legal tasks. Informed by Bloom's cognitive taxonomy, VLegal-Bench encompasses multiple levels of legal understanding through tasks designed to reflect practical usage scenarios. The benchmark comprises 10,450 samples generated through a rigorous annotation pipeline, where legal experts label and cross-validate each instance using our annotation system to ensure every sample is grounded in authoritative legal documents and mirrors real-world legal assistant workflows, including general legal questions and answers, retrieval-augmented generation, multi-step reasoning, and scenario-based problem solving tailored to Vietnamese law. By providing a standardized, transparent, and cognitively informed evaluation framework, VLegal-Bench establishes a solid foundation for assessing LLM performance in Vietnamese legal contexts and supports the development of more reliable, interpretable, and ethically aligned AI-assisted legal systems.

