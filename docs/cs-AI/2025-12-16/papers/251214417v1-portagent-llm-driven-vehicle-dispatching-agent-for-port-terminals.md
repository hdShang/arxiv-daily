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

**提出PortAgent，一种基于大语言模型的车辆调度代理，以解决自动化集装箱码头中车辆调度系统跨码头可移植性低的问题。**

**关键词**: `大语言模型` `车辆调度系统` `自动化码头` `少样本学习` `检索增强生成` `虚拟专家团队` `系统迁移` `自校正循环`

## 📋 核心要点

1. 核心问题：现有车辆调度系统跨码头可移植性低，主要受限于专家依赖、数据需求高和手动部署耗时。
2. 方法要点：提出PortAgent，基于大语言模型构建虚拟专家团队，通过少样本学习和检索增强生成自动化迁移工作流。
3. 实验或效果：PortAgent实现了快速部署，减少数据需求，提升系统可移植性，具体性能提升未知。

## 📝 摘要（中文）

车辆调度系统对自动化集装箱码头的运营效率至关重要，但其广泛商业化受到跨码头可移植性低的阻碍。这一挑战源于三个限制：高度依赖港口运营专家、对码头特定数据的高需求以及耗时的手动部署过程。利用大语言模型的兴起，本文提出PortAgent，一种基于大语言模型的车辆调度代理，完全自动化车辆调度系统的迁移工作流。它具有三个特点：（1）无需港口运营专家；（2）数据需求低；（3）部署快速。具体而言，通过虚拟专家团队消除专家依赖。该团队与知识检索器、建模师、编码器和调试器四个虚拟专家协作，模拟人类专家团队进行车辆调度系统迁移工作流。这些专家通过少样本示例学习方法专门化于码头车辆调度系统领域。通过这种方法，专家能够从少量车辆调度系统示例中学习领域知识。这些示例通过检索增强生成机制检索，减轻了对码头特定数据的高需求。此外，在这些专家之间建立了自动车辆调度系统设计工作流，以避免额外的手动干预。在该工作流中，创建了一个受大语言模型反射框架启发的自校正循环。

## 🔬 方法详解

PortAgent的核心方法基于大语言模型驱动的虚拟专家团队框架。整体框架包括知识检索器、建模师、编码器和调试器四个虚拟专家，它们通过协作模拟人类专家团队进行车辆调度系统迁移。关键技术创新点在于结合少样本示例学习和检索增强生成机制，使专家能从少量示例中学习领域知识，并自动检索相关数据以降低数据需求。与现有方法的主要区别在于完全自动化迁移过程，无需专家干预，通过自校正循环优化工作流，显著提高可移植性和部署效率。

## 📊 实验亮点

PortAgent通过虚拟专家团队和少样本学习，实现了车辆调度系统的快速自动化迁移，减少专家依赖和数据需求，具体性能指标未知，但显著提升了可移植性和部署速度。

## 🎯 应用场景

该研究主要应用于自动化集装箱码头的车辆调度系统迁移和部署，可扩展到其他物流和工业自动化场景，提升运营效率和系统适应性，具有实际商业价值。

## 📄 摘要（原文）

> Vehicle Dispatching Systems (VDSs) are critical to the operational efficiency of Automated Container Terminals (ACTs). However, their widespread commercialization is hindered due to their low transferability across diverse terminals. This transferability challenge stems from three limitations: high reliance on port operational specialists, a high demand for terminal-specific data, and time-consuming manual deployment processes. Leveraging the emergence of Large Language Models (LLMs), this paper proposes PortAgent, an LLM-driven vehicle dispatching agent that fully automates the VDS transferring workflow. It bears three features: (1) no need for port operations specialists; (2) low need of data; and (3) fast deployment. Specifically, specialist dependency is eliminated by the Virtual Expert Team (VET). The VET collaborates with four virtual experts, including a Knowledge Retriever, Modeler, Coder, and Debugger, to emulate a human expert team for the VDS transferring workflow. These experts specialize in the domain of terminal VDS via a few-shot example learning approach. Through this approach, the experts are able to learn VDS-domain knowledge from a few VDS examples. These examples are retrieved via a Retrieval-Augmented Generation (RAG) mechanism, mitigating the high demand for terminal-specific data. Furthermore, an automatic VDS design workflow is established among these experts to avoid extra manual interventions. In this workflow, a self-correction loop inspired by the LLM Reflexion framework is created

