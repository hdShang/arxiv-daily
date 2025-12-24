---
layout: default
title: Behavioral Augmentation of UML Class Diagrams: An Empirical Study of Large Language Models for Method Generation
---

# Behavioral Augmentation of UML Class Diagrams: An Empirical Study of Large Language Models for Method Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00788" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00788v1</a>
  <a href="https://arxiv.org/pdf/2506.00788.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00788v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00788v1', 'Behavioral Augmentation of UML Class Diagrams: An Empirical Study of Large Language Models for Method Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Djaber Rouabhia, Ismail Hadjadj

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-01

---

## 💡 一句话要点

**利用大语言模型自动增强UML类图中的行为方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `UML类图` `行为建模` `大型语言模型` `自动化生成` `软件设计` `敏捷开发` `方法生成`

## 📋 核心要点

1. 现有方法在将自然语言用例转化为UML类图中的行为方法时面临挑战，尤其是在方法生成的准确性和一致性方面。
2. 本研究通过评估九种大型语言模型，探索其在增强UML类图中的方法生成能力，旨在提高自动化建模的效率和质量。
3. 实验结果显示，所有模型均生成有效的PlantUML图，部分模型在方法覆盖和注释准确性上表现突出，推动了敏捷设计的快速迭代。

## 📝 摘要（中文）

自动化将自然语言用例中的行为方法丰富到UML类图中是一项重大挑战。本研究评估了九种大型语言模型（LLMs）在使用21个结构化的废物管理用例来增强一个无方法的UML图（包含21个类和17个关系）中的表现。通过六个指标评估了90个图（共3,373个方法）：方法数量、签名丰富性、注释完整性、结构保真度、语法正确性和命名一致性。所有LLMs生成的PlantUML图均符合UML规范，部分模型在方法覆盖和注释准确性方面表现优异，而另一些则在参数化方面更为丰富但追溯性较弱。这些结果表明LLMs能够生成结构良好的方法，并推动自动化行为建模的发展。然而，注释和签名的不一致性突显了改进提示工程和模型选择的必要性。快速生成这些方法支持敏捷实践，促进更快的设计迭代。尽管具备这些能力，人类监督仍然至关重要，以确保准确性、适当性和语义一致性。所有实验文档（.puml, .png, .csv）均可公开获取以便重现。

## 🔬 方法详解

**问题定义**：本论文旨在解决如何将自然语言用例中的行为方法自动化地转化为UML类图中的方法，现有方法在准确性和一致性方面存在不足。

**核心思路**：通过评估多种大型语言模型，探索其在方法生成中的表现，旨在提高UML类图的丰富性和准确性。

**技术框架**：研究采用了一个包含21个类和17个关系的无方法UML图，结合21个结构化的废物管理用例进行评估，使用六个指标进行性能评估。

**关键创新**：本研究的创新点在于系统性地评估了不同LLMs在UML类图方法生成中的表现，揭示了模型在方法覆盖、注释准确性和参数化方面的差异。

**关键设计**：实验中使用了多种评估指标，包括方法数量、签名丰富性、注释完整性等，确保了生成方法的结构性和一致性。

## 📊 实验亮点

实验结果表明，所有评估的LLMs均生成有效的PlantUML图，且在方法覆盖和注释准确性方面表现出色。部分模型在参数化上更为丰富，但追溯性较弱，显示出不同模型在生成能力上的差异。这些发现为未来的模型选择和提示工程提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括软件设计、系统建模和敏捷开发等。通过自动化生成UML类图中的行为方法，可以显著提高设计效率，减少人工干预，促进更快速的迭代与反馈。未来，随着模型的进一步优化，可能在更广泛的领域实现更高效的自动化建模。

## 📄 摘要（原文）

> Automating the enrichment of UML class diagrams with behavioral methods from natural language use cases is a significant challenge. This study evaluates nine large language models (LLMs) in augmenting a methodless UML diagram (21 classes, 17 relationships) using 21 structured waste-management use cases. A total of 90 diagrams (3,373 methods) were assessed across six metrics: method quantity, signature richness (visibility, names, parameters, return types), annotation completeness (linking to use cases/actions), structural fidelity, syntactic correctness (PlantUML compilation), and naming convergence (across models). All LLMs produced valid PlantUML diagrams adhering to UML conventions. Some models excelled in method coverage and annotation accuracy, while others showed richer parameterization but weaker traceability. These results demonstrate that LLMs can generate well-structured methods with consistent naming, advancing automated behavioral modeling. However, inconsistencies in annotations and signatures highlight the need for improved prompt engineering and model selection. The rapid generation of these methods supports Agile practices by enabling faster design iterations. Despite their capabilities, human oversight is essential to ensure accuracy, appropriateness, and semantic alignment. This positions LLMs as collaborative partners in software design. All experimental artifacts (\texttt{.puml}, \texttt{.png}, \texttt{.csv}) are publicly available for reproducibility.

