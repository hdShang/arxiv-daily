---
layout: default
title: PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals
---

# PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals

**arXiv**: [2512.14417v1](https://arxiv.org/abs/2512.14417) | [PDF](https://arxiv.org/pdf/2512.14417.pdf)

**作者**: Jia Hu, Junqi Li, Weimeng Lin, Peng Jia, Yuxiong Ji, Jintao Lai

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出PortAgent：基于大语言模型的自动化车辆调度代理，解决自动化集装箱码头系统跨终端迁移难题**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `大语言模型` `车辆调度系统` `自动化集装箱码头` `虚拟专家团队` `少样本学习` `检索增强生成` `系统迁移` `自校正循环`

## 📋 核心要点

1. 现有车辆调度系统跨终端迁移困难，依赖专家、数据需求高且部署耗时，阻碍商业化应用。
2. 提出PortAgent，利用大语言模型构建虚拟专家团队，通过少样本学习和检索增强生成实现自动化迁移。
3. 实验表明PortAgent能显著降低专家依赖和数据需求，实现快速部署，提升系统可迁移性和效率。

## 📝 摘要（中文）

车辆调度系统对自动化集装箱码头的运营效率至关重要，但其广泛商业化受到跨终端可迁移性低的限制。这一挑战源于三个局限：高度依赖港口运营专家、对终端特定数据需求高以及部署过程耗时。本文利用大语言模型的兴起，提出PortAgent，一个基于大语言模型的车辆调度代理，完全自动化车辆调度系统的迁移工作流。它具有三个特点：（1）无需港口运营专家；（2）数据需求低；（3）部署快速。具体而言，通过虚拟专家团队消除专家依赖。该团队由知识检索器、建模器、编码器和调试器四个虚拟专家组成，模拟人类专家团队执行车辆调度系统迁移工作流。这些专家通过少样本示例学习方法专门化于终端车辆调度系统领域。通过这种方法，专家能够从少量车辆调度系统示例中学习领域知识。这些示例通过检索增强生成机制检索，减轻了对终端特定数据的高需求。此外，在这些专家之间建立了自动车辆调度系统设计工作流，以避免额外的人工干预。在该工作流中，创建了一个受大语言模型反思框架启发的自校正循环。

## 🔬 方法详解

PortAgent的核心方法基于大语言模型驱动的虚拟专家团队框架。整体框架包括知识检索器、建模器、编码器和调试器四个虚拟专家，它们通过协作模拟人类专家团队，执行车辆调度系统的自动化迁移工作流。关键技术创新点在于采用少样本示例学习方法，使专家从少量车辆调度示例中学习领域知识，并结合检索增强生成机制动态检索相关示例，以降低数据需求。此外，引入受LLM Reflexion框架启发的自校正循环，实现工作流的自动优化和错误修正。与现有方法的主要区别在于完全自动化迁移过程，无需人工干预，显著减少了对专家和大量终端特定数据的依赖。

## 📊 实验亮点

PortAgent在实验中展示了高效迁移能力，无需港口运营专家参与，仅需少量示例数据即可实现快速部署。性能提升体现在迁移工作流的自动化程度高，减少了人工干预，同时通过自校正机制提高了系统设计的准确性和鲁棒性。

## 🎯 应用场景

该研究主要应用于自动化集装箱码头的车辆调度系统迁移和部署，可扩展到其他工业自动化场景，如物流中心或制造工厂的调度优化。实际价值在于提升系统跨终端可迁移性，降低部署成本和时间，促进智能调度技术的商业化应用。

## 📄 摘要（原文）

> Vehicle Dispatching Systems (VDSs) are critical to the operational efficiency of Automated Container Terminals (ACTs). However, their widespread commercialization is hindered due to their low transferability across diverse terminals. This transferability challenge stems from three limitations: high reliance on port operational specialists, a high demand for terminal-specific data, and time-consuming manual deployment processes. Leveraging the emergence of Large Language Models (LLMs), this paper proposes PortAgent, an LLM-driven vehicle dispatching agent that fully automates the VDS transferring workflow. It bears three features: (1) no need for port operations specialists; (2) low need of data; and (3) fast deployment. Specifically, specialist dependency is eliminated by the Virtual Expert Team (VET). The VET collaborates with four virtual experts, including a Knowledge Retriever, Modeler, Coder, and Debugger, to emulate a human expert team for the VDS transferring workflow. These experts specialize in the domain of terminal VDS via a few-shot example learning approach. Through this approach, the experts are able to learn VDS-domain knowledge from a few VDS examples. These examples are retrieved via a Retrieval-Augmented Generation (RAG) mechanism, mitigating the high demand for terminal-specific data. Furthermore, an automatic VDS design workflow is established among these experts to avoid extra manual interventions. In this workflow, a self-correction loop inspired by the LLM Reflexion framework is created

