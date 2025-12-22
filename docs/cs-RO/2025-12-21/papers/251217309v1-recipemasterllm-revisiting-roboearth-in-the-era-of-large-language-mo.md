---
layout: default
title: RecipeMasterLLM: Revisiting RoboEarth in the Era of Large Language Models
---

# RecipeMasterLLM: Revisiting RoboEarth in the Era of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17309" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17309v1</a>
  <a href="https://arxiv.org/pdf/2512.17309.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17309v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17309v1', 'RecipeMasterLLM: Revisiting RoboEarth in the Era of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Asil Kaan Bozcuoglu, Ziyuan Liu

**分类**: cs.RO

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**RecipeMasterLLM：利用大语言模型重塑RoboEarth知识获取流程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识图谱` `机器人` `RoboEarth` `动作规划`

## 📋 核心要点

1. 现有RoboEarth知识图谱主要依赖人工构建，效率低且难以扩展，无法适应快速变化的环境。
2. RecipeMasterLLM利用微调的大语言模型自动生成OWL动作本体，显著提升知识获取效率。
3. 该方法采用检索增强生成（RAG），将环境知识融入LLM，提高生成动作描述的准确性。

## 📝 摘要（中文）

RoboEarth是云计算机器人领域的先驱项目，它通过标准化的知识图谱，为机器人共享和交换关于动作、对象和环境的知识建立了一个基础框架。最初，这些知识主要由工程师使用OWL本体中的RDF三元组手工构建，并通过机器人的控制和感知程序来更新，例如对象姿态的变化。然而，随着大型语言模型（LLM）的出现和快速发展，我们认为知识获取的过程可以显著自动化。为此，我们提出了RecipeMasterLLM，一个高级规划器，它可以根据用户提示，基于标准化的知识图谱生成OWL动作本体。该架构利用经过微调的LLM，专门训练其理解和生成与RoboEarth标准化知识图谱一致的动作描述。此外，在检索增强生成（RAG）阶段，环境知识被提供给LLM，以增强其上下文理解并提高生成的动作描述的准确性。

## 🔬 方法详解

**问题定义**：RoboEarth项目旨在构建一个机器人可以共享知识的云平台，但其知识图谱的构建和维护依赖于人工，成本高昂且难以扩展。现有方法无法充分利用自然语言处理的最新进展，特别是大型语言模型在知识获取和推理方面的潜力。因此，如何自动化RoboEarth知识图谱的构建和更新，降低人工成本，提高知识获取效率，是本文要解决的核心问题。

**核心思路**：本文的核心思路是利用大型语言模型（LLM）的强大自然语言理解和生成能力，自动生成RoboEarth所需的OWL动作本体。通过微调LLM，使其能够理解RoboEarth的知识图谱结构和动作描述规范，从而实现从用户指令到机器可理解的知识表示的自动转换。RAG的引入进一步提升了LLM的上下文理解能力，使其能够根据环境信息生成更准确的动作描述。

**技术框架**：RecipeMasterLLM的整体架构包含以下几个主要模块：1) 用户输入模块：接收用户以自然语言形式输入的任务指令。2) 检索模块：从知识库中检索与当前任务相关的环境知识。3) LLM生成模块：利用微调的LLM，结合用户指令和检索到的环境知识，生成OWL动作本体。4) 知识图谱更新模块：将生成的OWL动作本体添加到RoboEarth知识图谱中。整个流程采用检索增强生成（RAG）框架，确保LLM能够获取必要的上下文信息。

**关键创新**：本文最重要的技术创新点在于将大型语言模型应用于RoboEarth知识图谱的自动构建。与传统的手工构建方法相比，该方法能够显著降低人工成本，提高知识获取效率。此外，通过微调LLM和引入RAG，提高了生成动作描述的准确性和可靠性。

**关键设计**：LLM采用开源的预训练语言模型，并使用RoboEarth相关的动作描述数据进行微调。微调的目标是使LLM能够生成符合RoboEarth知识图谱规范的OWL动作本体。RAG模块使用基于向量相似度的检索方法，从知识库中检索与用户指令相关的环境知识。具体参数设置和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17309v1/images/idea.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17309v1/images/d1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17309v1/images/setup.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文主要提出了RecipeMasterLLM的框架和设计思路，并没有提供具体的实验结果和性能数据。因此，无法总结具体的性能数据、对比基线和提升幅度。实验亮点未知。

## 🎯 应用场景

RecipeMasterLLM可应用于各种机器人任务规划和自动化场景，例如智能家居、工业自动化、医疗机器人等。通过自动生成机器人所需的知识，可以降低机器人部署和维护的成本，提高机器人的智能化水平。未来，该技术有望促进机器人技术的普及和应用。

## 📄 摘要（原文）

> RoboEarth was a pioneering initiative in cloud robotics, establishing a foundational framework for robots to share and exchange knowledge about actions, objects, and environments through a standardized knowledge graph. Initially, this knowledge was predominantly hand-crafted by engineers using RDF triples within OWL Ontologies, with updates, such as changes in an object's pose, being asserted by the robot's control and perception routines. However, with the advent and rapid development of Large Language Models (LLMs), we believe that the process of knowledge acquisition can be significantly automated. To this end, we propose RecipeMasterLLM, a high-level planner, that generates OWL action ontologies based on a standardized knowledge graph in response to user prompts. This architecture leverages a fine-tuned LLM specifically trained to understand and produce action descriptions consistent with the RoboEarth standardized knowledge graph. Moreover, during the Retrieval-Augmented Generation (RAG) phase, environmental knowledge is supplied to the LLM to enhance its contextual understanding and improve the accuracy of the generated action descriptions.

