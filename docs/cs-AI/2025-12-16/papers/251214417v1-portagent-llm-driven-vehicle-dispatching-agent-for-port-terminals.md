---
layout: default
title: PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals
---

# PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14417" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14417v1</a>
  <a href="https://arxiv.org/pdf/2512.14417.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14417v1" onclick="toggleFavorite(this, '2512.14417v1', 'PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Hu, Junqi Li, Weimeng Lin, Peng Jia, Yuxiong Ji, Jintao Lai

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出PortAgent，一种基于LLM的港口车辆调度智能体，提升跨港口适应性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `车辆调度系统` `自动化集装箱码头` `少样本学习` `检索增强生成`

## 📋 核心要点

1. 现有车辆调度系统(VDS)在不同港口间迁移性差，依赖专家知识、数据量大且部署耗时。
2. PortAgent利用LLM构建虚拟专家团队(VET)，通过少样本学习和RAG降低数据需求，实现自动VDS设计。
3. PortAgent通过VET模拟专家团队，无需人工干预，实现快速部署和跨港口迁移，提升VDS应用效率。

## 📝 摘要（中文）

车辆调度系统(VDS)对于自动化集装箱码头(ACT)的运营效率至关重要。然而，由于其在不同码头之间的低可迁移性，VDS的广泛商业化受到阻碍。这种可迁移性挑战源于三个限制：高度依赖港口运营专家、对特定码头数据的高需求以及耗时的人工部署过程。本文利用大型语言模型(LLM)的出现，提出了一种由LLM驱动的车辆调度智能体PortAgent，该智能体可以完全自动化VDS的迁移工作流程。它具有三个特点：(1)不需要港口运营专家；(2)对数据的需求低；(3)部署速度快。具体来说，通过虚拟专家团队(VET)消除了对专家的依赖。VET与四个虚拟专家（包括知识检索器、建模器、编码器和调试器）合作，模拟人类专家团队进行VDS迁移工作流程。这些专家通过少样本示例学习方法专注于终端VDS领域。通过这种方法，专家能够从一些VDS示例中学习VDS领域知识。这些示例通过检索增强生成(RAG)机制检索，从而降低了对特定码头数据的高需求。此外，在这些专家之间建立了一个自动VDS设计工作流程，以避免额外的人工干预。在这个工作流程中，创建了一个受LLM Reflexion框架启发的自我纠正循环。

## 🔬 方法详解

**问题定义**：现有自动化集装箱码头的车辆调度系统(VDS)难以在不同港口之间迁移。主要痛点在于：1)高度依赖港口运营专家进行定制化配置；2)需要大量的特定港口数据进行训练和优化；3)人工部署过程耗时且容易出错。这些因素限制了VDS的广泛应用和商业化。

**核心思路**：利用大型语言模型(LLM)的强大能力，模拟人类专家团队进行VDS的迁移和部署。通过构建一个虚拟专家团队(VET)，每个专家负责不同的任务，例如知识检索、模型构建、代码生成和调试。VET通过协作完成VDS的设计和部署，从而降低对人工干预和特定港口数据的依赖。这样设计的目的是为了实现VDS的自动化迁移，提高其在不同港口之间的适应性。

**技术框架**：PortAgent的核心是虚拟专家团队(VET)，它包含四个主要模块：1)知识检索器(Knowledge Retriever)：负责从少量示例中检索相关的VDS领域知识；2)建模器(Modeler)：基于检索到的知识构建VDS模型；3)编码器(Coder)：将VDS模型转化为可执行的代码；4)调试器(Debugger)：负责调试代码并进行自我纠正。这些模块通过一个自动VDS设计工作流程进行协作，该流程包含一个受LLM Reflexion框架启发的自我纠正循环，以提高VDS的性能。

**关键创新**：PortAgent的关键创新在于利用LLM构建虚拟专家团队(VET)，从而模拟人类专家进行VDS的迁移和部署。与传统的VDS方法相比，PortAgent不需要大量的特定港口数据，也不需要人工干预。此外，PortAgent的自我纠正循环可以不断优化VDS的性能，从而提高其在不同港口之间的适应性。本质区别在于，传统方法依赖人工和大量数据，而PortAgent依赖LLM的推理和生成能力。

**关键设计**：PortAgent的关键设计包括：1)少样本学习方法：用于训练虚拟专家，使其能够从少量示例中学习VDS领域知识；2)检索增强生成(RAG)机制：用于检索相关的VDS示例，从而降低对特定港口数据的需求；3)自我纠正循环：用于不断优化VDS的性能。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

论文提出了PortAgent，一个基于LLM的车辆调度智能体，旨在解决VDS在不同港口间迁移性差的问题。通过构建虚拟专家团队(VET)和采用少样本学习方法，PortAgent降低了对特定港口数据的需求，并实现了自动VDS设计。具体的性能数据和对比基线在摘要中未提及，属于未知信息。

## 🎯 应用场景

PortAgent可应用于自动化集装箱码头(ACT)，实现车辆调度系统的快速部署和迁移，降低对人工和数据的依赖，提高港口运营效率。该研究具有重要的实际价值，有望推动VDS在不同港口的广泛应用，并为其他领域的自动化系统设计提供借鉴。

## 📄 摘要（原文）

> Vehicle Dispatching Systems (VDSs) are critical to the operational efficiency of Automated Container Terminals (ACTs). However, their widespread commercialization is hindered due to their low transferability across diverse terminals. This transferability challenge stems from three limitations: high reliance on port operational specialists, a high demand for terminal-specific data, and time-consuming manual deployment processes. Leveraging the emergence of Large Language Models (LLMs), this paper proposes PortAgent, an LLM-driven vehicle dispatching agent that fully automates the VDS transferring workflow. It bears three features: (1) no need for port operations specialists; (2) low need of data; and (3) fast deployment. Specifically, specialist dependency is eliminated by the Virtual Expert Team (VET). The VET collaborates with four virtual experts, including a Knowledge Retriever, Modeler, Coder, and Debugger, to emulate a human expert team for the VDS transferring workflow. These experts specialize in the domain of terminal VDS via a few-shot example learning approach. Through this approach, the experts are able to learn VDS-domain knowledge from a few VDS examples. These examples are retrieved via a Retrieval-Augmented Generation (RAG) mechanism, mitigating the high demand for terminal-specific data. Furthermore, an automatic VDS design workflow is established among these experts to avoid extra manual interventions. In this workflow, a self-correction loop inspired by the LLM Reflexion framework is created

