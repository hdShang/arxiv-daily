---
layout: default
title: "RefTool: Enhancing Model Reasoning with Reference-Guided Tool Creation"
---

# RefTool: Enhancing Model Reasoning with Reference-Guided Tool Creation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21413" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21413v1</a>
  <a href="https://arxiv.org/pdf/2505.21413.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21413v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21413v1', 'RefTool: Enhancing Model Reasoning with Reference-Guided Tool Creation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Liu, Da Yin, Zirui Wu, Yansong Feng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27

**备注**: Code is available at https://github.com/xxxiaol/RefTool

---

## 💡 一句话要点

**提出RefTool以解决工具生成不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工具生成` `大型语言模型` `推理能力` `外部参考` `层次化结构` `自动化系统` `科学研究`

## 📋 核心要点

1. 现有方法在工具生成方面依赖模型内部知识，导致在知识范围外的任务中表现不佳。
2. RefTool通过参考材料指导工具创建，分为工具创建和工具利用两个模块，提升了模型的推理能力。
3. 实验结果显示，RefTool在多个基准测试中平均准确率提高了11.3%，且具有成本效益和广泛的适用性。

## 📝 摘要（中文）

工具增强了大型语言模型（LLMs）在复杂问题解决任务中的推理能力，但并非所有任务都有现成的工具可用。以往的研究尝试指导LLMs自行生成工具，但这些方法过于依赖模型的内部知识，容易在知识范围之外的领域失效。为了解决这一局限性，本文提出了RefTool，一个基于参考的自动工具创建框架，利用结构化的外部材料（如教科书）。RefTool由两个模块组成：工具创建和工具利用。实验表明，RefTool在因果关系、物理和化学基准测试中，平均准确率比现有工具创建和领域特定推理方法提高了11.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决在缺乏预定义工具时，LLMs在复杂任务中推理能力不足的问题。现有方法过于依赖模型的内部知识，导致在知识范围外的领域表现不佳。

**核心思路**：RefTool的核心思路是利用结构化的外部参考材料（如教科书）来指导工具的生成，从而克服模型知识的局限性。通过这种方式，LLMs能够生成更准确和可靠的工具。

**技术框架**：RefTool的整体架构包括两个主要模块：工具创建模块和工具利用模块。工具创建模块负责从参考内容生成可执行工具，并通过示例进行验证，最后将工具组织成层次化的工具箱；工具利用模块则负责在工具箱中导航，选择并应用合适的工具来解决问题。

**关键创新**：RefTool的主要创新在于将工具创建过程与外部参考材料相结合，从而生成准确且可信的工具。这一方法与以往仅依赖模型内部知识的工具生成方法本质上不同。

**关键设计**：在工具创建过程中，模型需要对参考内容进行解析和理解，生成的工具需经过示例验证以确保其有效性。此外，工具的层次化结构设计使得工具选择过程更加高效，提升了整体推理能力。

## 📊 实验亮点

实验结果表明，RefTool在因果关系、物理和化学基准测试中，平均准确率比现有工具创建和领域特定推理方法提高了11.3%。这一显著提升展示了RefTool在工具生成和推理能力方面的有效性，且其成本效益和广泛适用性使其成为一个有前景的解决方案。

## 🎯 应用场景

RefTool的研究成果在教育、科学研究和工程等领域具有广泛的应用潜力。通过提供可靠的工具生成机制，LLMs能够在更广泛的知识领域内进行有效推理，帮助用户解决复杂问题，提升决策支持的能力。未来，RefTool可能会推动智能助手和自动化系统的发展，使其在多种应用场景中更具实用性和可靠性。

## 📄 摘要（原文）

> Tools enhance the reasoning capabilities of large language models (LLMs) in complex problem-solving tasks, but not all tasks have available tools. In the absence of predefined tools, prior works have explored instructing LLMs to generate tools on their own. However, such approaches rely heavily on the models' internal knowledge and would fail in domains beyond the LLMs' knowledge scope. To address this limitation, we propose RefTool, a reference-guided framework for automatic tool creation that leverages structured external materials such as textbooks. RefTool consists of two modules: (1) tool creation, where LLMs generate executable tools from reference content, validate them using illustrative examples, and organize them hierarchically into a toolbox; and (2) tool utilization, where LLMs navigate the toolbox structure to select and apply the appropriate tools to solve problems. Experiments on causality, physics, and chemistry benchmarks demonstrate that RefTool outperforms existing tool-creation and domain-specific reasoning methods by 11.3% on average accuracy, while being cost-efficient and broadly generalizable. Analyses reveal that grounding tool creation in references produces accurate and faithful tools, and that the hierarchical structure facilitates effective tool selection. RefTool enables LLMs to overcome knowledge limitations, demonstrating the value of grounding tool creation in external references for enhanced and generalizable reasoning.

