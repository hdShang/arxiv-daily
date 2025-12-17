---
layout: default
title: OracleAgent: A Multimodal Reasoning Agent for Oracle Bone Script Research
---

# OracleAgent: A Multimodal Reasoning Agent for Oracle Bone Script Research

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.26114" target="_blank" class="toolbar-btn">arXiv: 2510.26114v1</a>
    <a href="https://arxiv.org/pdf/2510.26114.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26114v1" 
            onclick="toggleFavorite(this, '2510.26114v1', 'OracleAgent: A Multimodal Reasoning Agent for Oracle Bone Script Research')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Caoshuo Li, Zengmao Ding, Xiaobin Hu, Bang Li, Donghao Luo, Xu Peng, Taisong Jin, Yongge Liu, Shengwei Han, Jing Yang, Xiaoping He, Feng Gao, AndyPian Wu, SevenShu, Chaoyang Wang, Chengjie Wang

**分类**: cs.CV

**发布日期**: 2025-10-30

---

## 💡 一句话要点

**OracleAgent：用于甲骨文研究的多模态推理Agent系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `甲骨文研究` `多模态推理` `大型语言模型` `知识库构建` `智能Agent`

## 📋 核心要点

1. 当前甲骨文研究面临释读流程复杂、信息检索效率低下的挑战，学者需耗费大量时间整理资源。
2. OracleAgent通过集成甲骨文分析工具和构建多模态知识库，实现甲骨文信息的结构化管理和检索。
3. 实验表明，OracleAgent在多模态推理和生成任务中超越主流MLLM，并显著降低专家研究时间成本。

## 📝 摘要（中文）

甲骨文（OBS）作为最早的文字系统之一，保存了古代文明的文化和知识遗产。然而，当前的甲骨文研究面临两大挑战：（1）甲骨文的释读涉及一个复杂的流程，包含多个串行和并行的子任务；（2）甲骨文信息组织和检索的效率仍然是一个关键瓶颈，学者们经常花费大量精力搜索、编译和管理相关资源。为了应对这些挑战，我们提出了OracleAgent，这是第一个为甲骨文相关信息的结构化管理和检索而设计的Agent系统。OracleAgent无缝集成了多种甲骨文分析工具，并由大型语言模型（LLM）提供支持，可以灵活地编排这些组件。此外，我们构建了一个全面的、特定领域的多模态甲骨文知识库，该知识库是通过多年的数据收集、清洗和专家注释的严格过程构建的。该知识库包含超过140万张单字拓片图像和8万条释义文本。OracleAgent通过其多模态工具利用此资源来协助专家进行字符、文档、释义文本和拓片图像的检索任务。大量的实验表明，OracleAgent在一系列多模态推理和生成任务中取得了优异的性能，超过了领先的主流多模态大型语言模型（MLLM）（例如，GPT-4o）。此外，我们的案例研究表明，OracleAgent可以有效地帮助领域专家，从而大大降低甲骨文研究的时间成本。这些结果表明，OracleAgent是朝着甲骨文辅助研究和自动释读系统的实际部署迈出的重要一步。

## 🔬 方法详解

**问题定义**：甲骨文研究面临的主要问题是信息检索效率低下和释读流程复杂。现有方法难以有效地组织和检索甲骨文相关信息，导致研究人员需要花费大量时间进行手动搜索和整理。此外，甲骨文的释读涉及多个串行和并行的子任务，需要专业的知识和工具。

**核心思路**：OracleAgent的核心思路是构建一个集成了多种甲骨文分析工具和多模态知识库的智能Agent系统。通过利用大型语言模型（LLM）的推理能力和多模态知识库的丰富信息，OracleAgent可以自动化地完成甲骨文信息的检索、分析和释读任务，从而提高研究效率。

**技术框架**：OracleAgent的整体架构包含以下主要模块：(1) 多模态知识库：包含超过140万张单字拓片图像和8万条释义文本，通过数据收集、清洗和专家注释构建。(2) 甲骨文分析工具集成：集成多种甲骨文分析工具，例如字符识别、语义理解等。(3) 大型语言模型（LLM）：利用LLM的推理能力，协调各个模块的工作，并生成最终的释读结果。(4) 用户交互界面：提供友好的用户界面，方便用户进行查询和操作。

**关键创新**：OracleAgent的关键创新在于其将大型语言模型、多模态知识库和甲骨文分析工具集成到一个统一的Agent系统中。这种集成使得OracleAgent能够充分利用各种资源的优势，实现更高效、更准确的甲骨文研究。

**关键设计**：OracleAgent的关键设计包括：(1) 多模态知识库的构建：采用严格的数据收集、清洗和专家注释流程，保证知识库的质量。(2) LLM的选择和训练：选择合适的LLM，并针对甲骨文领域进行微调，提高其推理能力。(3) Agent的编排策略：设计合理的Agent编排策略，使得各个模块能够协同工作，完成复杂的任务。

## 📊 实验亮点

OracleAgent在多模态推理和生成任务中表现出色，超越了GPT-4o等主流MLLM。案例研究表明，OracleAgent能够显著降低领域专家在甲骨文研究中的时间成本，表明其在实际应用中具有很高的价值。具体性能数据和提升幅度在论文中有详细展示。

## 🎯 应用场景

OracleAgent可应用于甲骨文研究、古文字学、历史学等领域，为学者提供高效的甲骨文信息检索和释读工具。其潜在价值在于加速甲骨文研究进程，促进中华文明的传承和发展。未来，该系统可扩展到其他古文字的研究，构建更广泛的古文字知识库和智能分析系统。

## 📄 摘要（原文）

> As one of the earliest writing systems, Oracle Bone Script (OBS) preserves the cultural and intellectual heritage of ancient civilizations. However, current OBS research faces two major challenges: (1) the interpretation of OBS involves a complex workflow comprising multiple serial and parallel sub-tasks, and (2) the efficiency of OBS information organization and retrieval remains a critical bottleneck, as scholars often spend substantial effort searching for, compiling, and managing relevant resources. To address these challenges, we present OracleAgent, the first agent system designed for the structured management and retrieval of OBS-related information. OracleAgent seamlessly integrates multiple OBS analysis tools, empowered by large language models (LLMs), and can flexibly orchestrate these components. Additionally, we construct a comprehensive domain-specific multimodal knowledge base for OBS, which is built through a rigorous multi-year process of data collection, cleaning, and expert annotation. The knowledge base comprises over 1.4M single-character rubbing images and 80K interpretation texts. OracleAgent leverages this resource through its multimodal tools to assist experts in retrieval tasks of character, document, interpretation text, and rubbing image. Extensive experiments demonstrate that OracleAgent achieves superior performance across a range of multimodal reasoning and generation tasks, surpassing leading mainstream multimodal large language models (MLLMs) (e.g., GPT-4o). Furthermore, our case study illustrates that OracleAgent can effectively assist domain experts, significantly reducing the time cost of OBS research. These results highlight OracleAgent as a significant step toward the practical deployment of OBS-assisted research and automated interpretation systems.

