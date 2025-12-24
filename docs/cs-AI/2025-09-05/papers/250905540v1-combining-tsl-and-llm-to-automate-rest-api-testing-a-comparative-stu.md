---
layout: default
title: "Combining TSL and LLM to Automate REST API Testing: A Comparative Study"
---

# Combining TSL and LLM to Automate REST API Testing: A Comparative Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05540" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05540v1</a>
  <a href="https://arxiv.org/pdf/2509.05540.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05540v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05540v1', 'Combining TSL and LLM to Automate REST API Testing: A Comparative Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thiago Barradas, Aline Paes, Vânia de Oliveira Neves

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-05

**备注**: 10 pages, article computer science, software engineering, software testing, ia, llm

**期刊**: SBES 2025 39th Brazilian Symposium on Software Engineering

---

## 💡 一句话要点

**提出RestTSLLM，结合TSL与LLM自动化REST API测试用例生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `REST API测试` `自动化测试` `大型语言模型` `测试用例生成` `提示工程`

## 📋 核心要点

1. REST API测试面临分布式系统复杂、测试场景多样和时间有限等挑战，导致测试不充分和人工成本高。
2. RestTSLLM结合TSL和LLM，通过提示工程和自动化流程，从OpenAPI规范生成测试用例，解决测试场景和输入数据定义问题。
3. 实验表明，Claude 3.5 Sonnet等LLM能有效生成REST API测试，Claude 3.5 Sonnet在成功率、覆盖率和变异得分上表现最佳。

## 📝 摘要（中文）

针对REST API测试中分布式系统复杂性、场景多样性和测试时间有限等挑战，本文提出RestTSLLM方法，该方法结合测试规约语言（TSL）和大型语言模型（LLM）来自动化生成REST API的测试用例。该方法主要解决两个核心问题：测试场景的创建和适当输入数据的定义。提出的解决方案集成了提示工程技术和一个自动化流程，以评估各种LLM从OpenAPI规范生成测试的能力。评估侧重于成功率、测试覆盖率和变异得分等指标，从而系统地比较模型性能。结果表明，表现最佳的LLM（Claude 3.5 Sonnet、Deepseek R1、Qwen 2.5 32b和Sabia 3）能够持续生成稳健且上下文连贯的REST API测试。其中，Claude 3.5 Sonnet在所有指标上均优于其他模型，成为本研究中最适合此任务的模型。这些发现突显了LLM在基于API规范自动化生成测试方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决REST API测试自动化程度低的问题。现有方法难以应对分布式系统的复杂性，无法覆盖所有可能的输入组合，导致测试覆盖率低，需要大量的人工干预，并且容易遗漏潜在的故障。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的生成能力，结合测试规约语言（TSL）的规范性，自动化生成REST API的测试用例。通过提示工程，引导LLM理解API规范，并生成符合规范的测试场景和输入数据。

**技术框架**：RestTSLLM方法包含以下主要阶段：1) 输入OpenAPI规范；2) 使用提示工程技术，设计合适的prompt，引导LLM生成测试用例；3) 利用TSL对生成的测试用例进行规范化和验证；4) 执行测试用例，并评估测试结果，包括成功率、测试覆盖率和变异得分；5) 对比不同LLM的性能，选择最适合该任务的模型。

**关键创新**：该方法最重要的创新点在于将LLM应用于REST API测试用例的自动化生成。与传统的基于规则或模板的测试生成方法相比，LLM能够更好地理解API的语义，生成更复杂、更具上下文相关性的测试用例，从而提高测试覆盖率和发现潜在缺陷的能力。

**关键设计**：关键设计包括：1) Prompt工程：设计有效的prompt，引导LLM生成高质量的测试用例。Prompt需要包含API的描述、输入参数的类型和范围、以及期望的输出结果等信息。2) TSL规范：使用TSL对生成的测试用例进行规范化，确保测试用例的格式正确、语义清晰。3) 评估指标：使用成功率、测试覆盖率和变异得分等指标，全面评估LLM生成的测试用例的质量。

## 📊 实验亮点

实验结果表明，Claude 3.5 Sonnet在所有评估指标上均优于其他LLM，包括Deepseek R1、Qwen 2.5 32b和Sabia 3。Claude 3.5 Sonnet能够生成更稳健、更具上下文连贯性的REST API测试用例，证明了LLM在自动化API测试方面的巨大潜力。

## 🎯 应用场景

该研究成果可应用于软件开发和测试领域，帮助开发团队自动化生成REST API的测试用例，提高测试效率和覆盖率，降低人工测试成本，并尽早发现潜在的缺陷。未来可扩展到其他类型的API测试，并集成到持续集成/持续交付（CI/CD）流程中。

## 📄 摘要（原文）

> The effective execution of tests for REST APIs remains a considerable challenge for development teams, driven by the inherent complexity of distributed systems, the multitude of possible scenarios, and the limited time available for test design. Exhaustive testing of all input combinations is impractical, often resulting in undetected failures, high manual effort, and limited test coverage. To address these issues, we introduce RestTSLLM, an approach that uses Test Specification Language (TSL) in conjunction with Large Language Models (LLMs) to automate the generation of test cases for REST APIs. The approach targets two core challenges: the creation of test scenarios and the definition of appropriate input data. The proposed solution integrates prompt engineering techniques with an automated pipeline to evaluate various LLMs on their ability to generate tests from OpenAPI specifications. The evaluation focused on metrics such as success rate, test coverage, and mutation score, enabling a systematic comparison of model performance. The results indicate that the best-performing LLMs - Claude 3.5 Sonnet (Anthropic), Deepseek R1 (Deepseek), Qwen 2.5 32b (Alibaba), and Sabia 3 (Maritaca) - consistently produced robust and contextually coherent REST API tests. Among them, Claude 3.5 Sonnet outperformed all other models across every metric, emerging in this study as the most suitable model for this task. These findings highlight the potential of LLMs to automate the generation of tests based on API specifications.

