---
layout: default
title: "Readme_AI: Dynamic Context Construction for Large Language Models"
---

# Readme_AI: Dynamic Context Construction for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19322" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19322v1</a>
  <a href="https://arxiv.org/pdf/2509.19322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19322v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19322v1', 'Readme_AI: Dynamic Context Construction for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Millie Vyas, Timothy Blattner, Alden Dima

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-12

**🔗 代码/项目**: [GITHUB](https://github.com/usnistgov/readme_ai)

---

## 💡 一句话要点

**Readme_AI：提出动态上下文构建方法，提升大语言模型在特定查询下的准确性和可靠性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `动态上下文构建` `元数据驱动` `知识库问答` `信息检索`

## 📋 核心要点

1. 大语言模型在特定领域或数据集上，由于缺乏针对性上下文，容易产生不准确或幻觉信息。
2. Readme_AI通过构建动态上下文，让LLM能够基于数据源所有者提供的元数据进行推理，从而提升响应质量。
3. 实验表明，Readme_AI能够使LLM更准确地理解NIST的Hedgehog库，并生成相关的代码示例。

## 📝 摘要（中文）

尽管大语言模型(LLMs)经过大量数据训练，但在用户特定查询的上下文中，它们可能会提供不准确或不可靠的信息。提供特定于查询的上下文可以显著提高其响应的有效性。本文提出了一种规范，可用于为数据源动态构建上下文。数据源所有者创建包含元数据的文件，供LLMs在推理与数据集相关的查询时使用。为了演示我们提出的规范，我们创建了一个原型Readme_AI模型上下文协议(MCP)服务器，该服务器从数据源检索元数据，并使用它来动态构建上下文。该规范的一些动态特性是可扩展的类型，这些类型表示爬取网页、从数据存储库获取数据、下载和解析出版物以及通用文本。上下文使用用户指定的标签进行格式化和分组，这些标签为LLM提供清晰的上下文信息以进行推理。我们通过询问LLM关于NIST开发的Hedgehog库来演示这个早期原型的能力，对于该库，常见的LLM通常提供包含幻觉的不准确和不相关的响应。借助Readme_AI，LLM接收到足够的上下文，现在能够推理该库及其使用，甚至可以生成从Hedgehog开发人员提供的Readme_AI文件中包含的示例中插入的代码。我们的主要贡献是一种可扩展的协议，用于在专门的、所有者提供的数据中动态地 grounding LLM，从而增强LLM的响应并减少幻觉。

## 🔬 方法详解

**问题定义**：大语言模型虽然拥有强大的知识储备，但在面对特定领域或数据集的查询时，由于缺乏针对性的上下文信息，容易产生不准确、不相关甚至虚假的回答（即幻觉）。现有方法难以动态地为LLM提供所需的上下文信息，从而限制了其在特定场景下的应用效果。

**核心思路**：Readme_AI的核心思路是构建一个动态上下文构建协议，允许数据源所有者提供关于其数据集的元数据，并利用这些元数据为LLM构建特定于查询的上下文。这样，LLM就可以在更充分的背景信息下进行推理，从而提高回答的准确性和可靠性。

**技术框架**：Readme_AI的技术框架主要包括以下几个部分：1) 数据源元数据规范：定义了数据源所有者如何提供关于其数据集的元数据，包括数据描述、使用示例、相关文档等。2) 模型上下文协议(MCP)服务器：负责从数据源检索元数据，并根据用户查询动态构建上下文。3) 上下文格式化和分组：使用用户指定的标签对上下文进行格式化和分组，以便LLM更好地理解和利用上下文信息。

**关键创新**：Readme_AI的关键创新在于其动态上下文构建协议，该协议允许数据源所有者以标准化的方式提供元数据，并利用这些元数据为LLM构建特定于查询的上下文。这种动态构建上下文的方法可以有效地减少LLM的幻觉，并提高其在特定场景下的应用效果。

**关键设计**：Readme_AI的关键设计包括：1) 可扩展的元数据类型：支持多种元数据类型，包括网页爬取、数据仓库访问、文档解析等。2) 用户可配置的上下文标签：允许用户自定义上下文标签，以便更好地组织和利用上下文信息。3) 基于查询的上下文检索：根据用户查询动态检索相关的元数据，并构建上下文。

## 📊 实验亮点

实验结果表明，Readme_AI能够显著提升LLM在理解NIST开发的Hedgehog库方面的能力。在没有Readme_AI的情况下，LLM通常会给出不准确或不相关的回答。而借助Readme_AI提供的上下文，LLM能够更准确地理解Hedgehog库，并生成相关的代码示例，有效减少了幻觉现象。

## 🎯 应用场景

Readme_AI可应用于各种需要大语言模型提供专业领域知识的场景，例如软件开发文档理解、科学研究数据分析、企业内部知识库问答等。通过提供动态上下文，Readme_AI可以显著提升LLM在这些场景下的应用效果，并降低幻觉风险。未来，该技术有望成为LLM在专业领域应用的重要基础设施。

## 📄 摘要（原文）

> Despite being trained on significant amounts of data, Large Language Models (LLMs) can provide inaccurate or unreliable information in the context of a user's specific query. Given query-specific context significantly improves the usefulness of its responses. In this paper, we present a specification that can be used to dynamically build context for data sources. The data source owner creates the file containing metadata for LLMs to use when reasoning about dataset-related queries. To demonstrate our proposed specification, we created a prototype Readme_AI Model Context Protocol (MCP) server that retrieves the metadata from the data source and uses it to dynamically build context. Some features that make this specification dynamic are the extensible types that represent crawling web-pages, fetching data from data repositories, downloading and parsing publications, and general text. The context is formatted and grouped using user-specified tags that provide clear contextual information for the LLM to reason about the content. We demonstrate the capabilities of this early prototype by asking the LLM about the NIST-developed Hedgehog library, for which common LLMs often provides inaccurate and irrelevant responses containing hallucinations. With Readme_AI, the LLM receives enough context that it is now able to reason about the library and its use, and even generate code interpolated from examples that were included in the Readme_AI file provided by Hedgehog's developer. Our primary contribution is a extensible protocol for dynamically grounding LLMs in specialized, owner-provided data, enhancing responses from LLMs and reducing hallucinations. The source code for the Readme_AI tool is posted here: https://github.com/usnistgov/readme_ai .

