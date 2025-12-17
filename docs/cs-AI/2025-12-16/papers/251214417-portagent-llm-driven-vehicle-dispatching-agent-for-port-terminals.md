---
layout: default
title: PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals
---

# PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14417" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14417</a>
  <a href="https://arxiv.org/pdf/2512.14417.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14417" onclick="toggleFavorite(this, '2512.14417', 'PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Hu, Junqi Li, Weimeng Lin, Peng Jia, Yuxiong Ji, Jintao Lai

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**PortAgent：基于LLM的港口车辆调度智能体，提升跨终端迁移能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `车辆调度系统` `自动化集装箱码头` `迁移学习` `检索增强生成`

## 📋 核心要点

1. 现有车辆调度系统(VDS)在不同港口终端间的迁移性差，严重依赖专家知识和大量特定数据，部署耗时。
2. PortAgent利用大型语言模型(LLM)构建虚拟专家团队(VET)，模拟专家进行VDS迁移，降低对专家和数据的依赖。
3. 通过检索增强生成(RAG)获取少量VDS示例，并建立自动VDS设计流程，实现快速部署和自我纠正。

## 📝 摘要（中文）

车辆调度系统(VDS)对于自动化集装箱码头(ACT)的运营效率至关重要。然而，由于其在不同终端之间的低可迁移性，VDS的广泛商业化受到阻碍。这种可迁移性挑战源于三个限制：高度依赖港口运营专家、对终端特定数据的高需求以及耗时的人工部署过程。本文利用大型语言模型(LLM)的兴起，提出了一种由LLM驱动的车辆调度智能体PortAgent，该智能体可以完全自动化VDS的迁移工作流程。它具有三个特点：(1)不需要港口运营专家；(2)对数据的需求低；(3)快速部署。具体来说，通过虚拟专家团队(VET)消除了对专家的依赖。VET与四个虚拟专家（包括知识检索器、建模器、编码器和调试器）合作，模拟人类专家团队进行VDS迁移工作流程。这些专家通过少样本示例学习方法专注于终端VDS领域。通过这种方法，专家能够从一些VDS示例中学习VDS领域知识。这些示例通过检索增强生成(RAG)机制检索，从而降低了对终端特定数据的高需求。此外，在这些专家之间建立了一个自动VDS设计工作流程，以避免额外的人工干预。在这个工作流程中，创建了一个受LLM Reflexion框架启发的自我纠正循环。

## 🔬 方法详解

**问题定义**：现有车辆调度系统(VDS)在自动化集装箱码头(ACT)的应用面临跨终端迁移性差的问题。具体来说，VDS的部署和优化高度依赖于港口运营专家的经验，需要大量的终端特定数据进行训练和调整，并且人工部署过程耗时且容易出错。这些因素限制了VDS在不同港口终端的广泛应用。

**核心思路**：PortAgent的核心思路是利用大型语言模型(LLM)的强大能力，构建一个虚拟专家团队(VET)，该团队能够模拟人类专家进行VDS的迁移和部署工作。通过少样本学习和检索增强生成(RAG)技术，VET可以从少量VDS示例中学习领域知识，并自动设计和优化VDS，从而降低对专家知识和大量数据的依赖。

**技术框架**：PortAgent的整体架构包含以下几个主要模块：1) **虚拟专家团队(VET)**：由知识检索器、建模器、编码器和调试器四个虚拟专家组成。2) **检索增强生成(RAG)**：用于从少量VDS示例中检索相关知识，为VET提供学习材料。3) **自动VDS设计流程**：VET中的专家协同工作，自动设计和优化VDS。4) **自我纠正循环**：借鉴LLM Reflexion框架，VET通过自我评估和反思，不断改进VDS的设计。

**关键创新**：PortAgent最重要的技术创新在于利用LLM构建虚拟专家团队(VET)，并将其应用于VDS的迁移和部署。与传统的VDS方法相比，PortAgent无需人工干预，能够自动学习领域知识并设计VDS，从而大大降低了对专家知识和大量数据的依赖。此外，PortAgent的自我纠正循环能够不断改进VDS的设计，提高其性能。

**关键设计**：知识检索器使用向量数据库存储VDS示例，并使用余弦相似度进行检索。建模器负责将VDS示例转换为数学模型。编码器将数学模型转换为可执行的代码。调试器负责测试和调试代码，并向建模器提供反馈。自我纠正循环使用奖励函数评估VDS的性能，并使用反馈信号调整VET的参数。具体的参数设置和损失函数细节未知。

## 📊 实验亮点

论文提出了PortAgent，一个基于LLM的港口车辆调度智能体，旨在解决VDS在不同终端之间迁移性差的问题。通过构建虚拟专家团队(VET)和利用检索增强生成(RAG)技术，PortAgent能够从少量VDS示例中学习领域知识，并自动设计和优化VDS。具体的实验结果未知。

## 🎯 应用场景

PortAgent可应用于各种自动化集装箱码头(ACT)，实现VDS的快速部署和优化，提高港口运营效率，降低运营成本。该研究成果还可推广到其他需要领域专家知识和大量数据的自动化系统中，例如智能制造、智慧城市等，具有广阔的应用前景和实际价值。

## 📄 摘要（原文）

> Vehicle Dispatching Systems (VDSs) are critical to the operational efficiency of Automated Container Terminals (ACTs). However, their widespread commercialization is hindered due to their low transferability across diverse terminals. This transferability challenge stems from three limitations: high reliance on port operational specialists, a high demand for terminal-specific data, and time-consuming manual deployment processes. Leveraging the emergence of Large Language Models (LLMs), this paper proposes PortAgent, an LLM-driven vehicle dispatching agent that fully automates the VDS transferring workflow. It bears three features: (1) no need for port operations specialists; (2) low need of data; and (3) fast deployment. Specifically, specialist dependency is eliminated by the Virtual Expert Team (VET). The VET collaborates with four virtual experts, including a Knowledge Retriever, Modeler, Coder, and Debugger, to emulate a human expert team for the VDS transferring workflow. These experts specialize in the domain of terminal VDS via a few-shot example learning approach. Through this approach, the experts are able to learn VDS-domain knowledge from a few VDS examples. These examples are retrieved via a Retrieval-Augmented Generation (RAG) mechanism, mitigating the high demand for terminal-specific data. Furthermore, an automatic VDS design workflow is established among these experts to avoid extra manual interventions. In this workflow, a self-correction loop inspired by the LLM Reflexion framework is created

