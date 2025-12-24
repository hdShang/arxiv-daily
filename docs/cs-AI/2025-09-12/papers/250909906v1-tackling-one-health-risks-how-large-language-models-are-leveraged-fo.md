---
layout: default
title: "Tackling One Health Risks: How Large Language Models are leveraged for Risk Negotiation and Consensus-building"
---

# Tackling One Health Risks: How Large Language Models are leveraged for Risk Negotiation and Consensus-building

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09906" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09906v1</a>
  <a href="https://arxiv.org/pdf/2509.09906.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09906v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09906v1', 'Tackling One Health Risks: How Large Language Models are leveraged for Risk Negotiation and Consensus-building')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexandra Fetsch, Iurii Savvateev, Racem Ben Romdhane, Martin Wiedmann, Artemiy Dimov, Maciej Durkalec, Josef Teichmann, Jakob Zinsstag, Konstantinos Koutsoumanis, Andreja Rajkovic, Jason Mann, Mauro Tonolla, Monika Ehling-Schulz, Matthias Filter, Sophia Johler

**分类**: cs.MA, cs.AI

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**利用大型语言模型进行风险协商和共识构建，应对“同一个健康”风险**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `风险协商` `共识构建` `同一个健康` `AI辅助决策`

## 📋 核心要点

1. 传统风险分析框架简化复杂性，导致跨部门协作困难，无法有效解决“同一个健康”领域的复杂问题。
2. 该研究提出一种AI辅助协商框架，利用LLM和AI代理模拟协商过程，预测妥协方案，评估解决方案影响。
3. 通过实际案例验证，证明该框架能够缓解信息过载，增强决策能力，并为跨部门合作提供有效工具。

## 📝 摘要（中文）

当前全球性挑战具有复杂的相互依赖性，需要综合性的参与式努力才能有效应对。传统的风险分析框架通常为了便于管理而简化复杂性，造成信息孤岛，阻碍了全面解决方案的形成。本文提出了一种AI辅助的协商框架，该框架将大型语言模型（LLM）和基于AI的自主代理集成到以协商为中心的风险分析工作流程中。该框架使利益相关者能够模拟协商，系统地建模动态，预测妥协，并评估解决方案的影响。通过利用LLM的语义分析能力，可以缓解信息过载，并在时间限制下增强决策过程。在两个实际场景中进行了概念验证：（i）合理使用生物农药，以及（ii）有针对性的野生动物种群控制。该研究展示了AI辅助协商在解决当前跨部门参与工具不足方面的潜力。重要的是，该解决方案的开源、基于Web的设计，适合资源有限的更广泛受众应用，并使用户能够根据自己的需求进行定制和开发。

## 🔬 方法详解

**问题定义**：论文旨在解决在“同一个健康”框架下，由于信息过载、时间限制以及不同利益相关者之间的冲突，导致跨部门协商和共识构建困难的问题。现有风险分析方法通常过于简化，无法有效处理复杂性和多方利益，阻碍了全面解决方案的制定。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的语义理解和生成能力，以及AI自主代理的模拟协商能力，构建一个AI辅助的协商框架。该框架旨在帮助利益相关者更好地理解彼此的立场，预测可能的妥协方案，并评估不同解决方案的影响，从而促进共识的达成。

**技术框架**：该框架包含以下主要模块：1) **信息收集与整理**：利用LLM从大量信息中提取关键信息，并进行语义分析；2) **利益相关者建模**：构建AI自主代理，代表不同的利益相关者，并模拟他们的行为和偏好；3) **协商模拟**：利用AI代理进行协商模拟，预测可能的妥协方案；4) **解决方案评估**：评估不同解决方案对各方利益的影响；5) **结果可视化**：将协商结果以可视化的方式呈现给用户。

**关键创新**：该研究的关键创新在于将LLM和AI自主代理集成到风险分析和协商过程中，从而能够处理更复杂的信息，模拟更真实的协商场景，并提供更全面的解决方案评估。与传统方法相比，该框架能够更好地应对信息过载、时间限制以及利益冲突等挑战。

**关键设计**：论文中没有详细描述关键参数设置、损失函数或网络结构等技术细节。但是，可以推断LLM的选择和微调、AI代理的行为建模、以及协商策略的设计是关键的设计要素。此外，框架的开源和基于Web的设计使其更易于部署和定制。

## 📊 实验亮点

该研究在生物农药的合理使用和野生动物种群控制两个实际案例中进行了概念验证。结果表明，该AI辅助协商框架能够帮助利益相关者更好地理解彼此的立场，预测可能的妥协方案，并评估不同解决方案的影响。虽然论文没有提供具体的性能数据，但强调了该框架在解决跨部门参与工具不足方面的潜力。

## 🎯 应用场景

该研究成果可应用于涉及多方利益相关者的复杂风险管理场景，例如公共卫生政策制定、环境保护、食品安全等。通过AI辅助协商，可以促进跨部门合作，提高决策效率，并制定更全面、更可持续的解决方案。该框架的开源特性使其能够被广泛应用，尤其是在资源有限的地区。

## 📄 摘要（原文）

> Key global challenges of our times are characterized by complex interdependencies and can only be effectively addressed through an integrated, participatory effort. Conventional risk analysis frameworks often reduce complexity to ensure manageability, creating silos that hinder comprehensive solutions. A fundamental shift towards holistic strategies is essential to enable effective negotiations between different sectors and to balance the competing interests of stakeholders. However, achieving this balance is often hindered by limited time, vast amounts of information, and the complexity of integrating diverse perspectives. This study presents an AI-assisted negotiation framework that incorporates large language models (LLMs) and AI-based autonomous agents into a negotiation-centered risk analysis workflow. The framework enables stakeholders to simulate negotiations, systematically model dynamics, anticipate compromises, and evaluate solution impacts. By leveraging LLMs' semantic analysis capabilities we could mitigate information overload and augment decision-making process under time constraints. Proof-of-concept implementations were conducted in two real-world scenarios: (i) prudent use of a biopesticide, and (ii) targeted wild animal population control. Our work demonstrates the potential of AI-assisted negotiation to address the current lack of tools for cross-sectoral engagement. Importantly, the solution's open source, web based design, suits for application by a broader audience with limited resources and enables users to tailor and develop it for their own needs.

