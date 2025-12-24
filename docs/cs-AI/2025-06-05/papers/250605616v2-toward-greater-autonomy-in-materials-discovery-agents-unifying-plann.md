---
layout: default
title: "Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists"
---

# Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05616" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05616v2</a>
  <a href="https://arxiv.org/pdf/2506.05616.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05616v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05616v2', 'Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lianhao Zhou, Hongyi Ling, Keqiang Yan, Kaiji Zhao, Xiaoning Qian, Raymundo Arróyave, Xiaofeng Qian, Shuiwang Ji

**分类**: cs.AI, cond-mat.mtrl-sci, physics.comp-ph

**发布日期**: 2025-06-05 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出MAPPS框架以实现更高自主性的材料发现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `材料发现` `自主学习` `工作流程规划` `物理模型` `科学反馈` `人工智能` `生成模型`

## 📋 核心要点

1. 现有的材料发现方法往往局限于特定任务，缺乏灵活性和自主性，难以满足科学家的需求。
2. 论文提出的MAPPS框架通过结合工作流程规划、物理模型和科学家反馈，实现了材料发现过程的自动化和智能化。
3. 实验结果表明，MAPPS在稳定性、独特性和新颖性方面相比于传统生成模型有五倍的提升，展示了其有效性。

## 📝 摘要（中文）

本研究旨在设计具有更高自主性的语言代理，以促进晶体材料的发现。与现有研究大多限制代理在预定义工作流程内执行特定任务不同，我们的目标是根据高层次目标和科学家的直觉自动化工作流程规划。为此，我们提出了统一规划、物理和科学家的材料代理MAPPS。MAPPS由工作流程规划器、工具代码生成器和科学中介组成，能够生成结构化的多步骤工作流程，并合成可执行的Python代码。通过统一规划、物理和科学家，MAPPS在材料发现中实现了灵活性和可靠性，在MP-20数据集上相比于先前的生成模型，稳定性、独特性和新颖性率提高了五倍。我们通过广泛的实验展示了MAPPS作为自主材料发现框架的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有材料发现方法的局限性，尤其是在自主性和灵活性方面的不足。现有方法通常依赖于预定义的工作流程，无法根据科学家的直觉和高层次目标进行动态调整。

**核心思路**：MAPPS框架的核心思路是通过结合工作流程规划、物理模型和科学家反馈，实现材料发现过程的高度自动化。该设计旨在提升代理的自主性，使其能够在复杂的材料发现任务中更有效地运作。

**技术框架**：MAPPS框架主要由三个模块组成：工作流程规划器、工具代码生成器和科学中介。工作流程规划器利用大型语言模型生成结构化的多步骤工作流程；工具代码生成器则负责合成可执行的Python代码；科学中介协调科学家反馈，确保系统的鲁棒性。

**关键创新**：MAPPS的最大创新在于其将规划、物理和科学家反馈统一到一个框架中，从而实现了更高的自主性和灵活性。这一设计与传统方法的本质区别在于其动态适应能力和智能决策能力。

**关键设计**：在技术细节方面，工作流程规划器使用了先进的语言模型，工具代码生成器则采用了特定的编程接口来调用物理模型。此外，科学中介的设计确保了系统在面对错误时能够进行反思和恢复，增强了整体的稳定性。

## 📊 实验亮点

在MP-20数据集上的实验结果显示，MAPPS框架在稳定性、独特性和新颖性率方面相比于传统生成模型实现了五倍的提升。这一显著的性能改进表明，MAPPS在材料发现领域具有强大的潜力和应用价值。

## 🎯 应用场景

该研究的MAPPS框架具有广泛的应用潜力，特别是在材料科学、化学和工程等领域。通过提升材料发现的自主性和智能化水平，MAPPS能够加速新材料的研发过程，推动科学研究的进展，并为工业应用提供更高效的解决方案。未来，MAPPS可能在智能实验室和自动化科研平台中发挥重要作用。

## 📄 摘要（原文）

> We aim at designing language agents with greater autonomy for crystal materials discovery. While most of existing studies restrict the agents to perform specific tasks within predefined workflows, we aim to automate workflow planning given high-level goals and scientist intuition. To this end, we propose Materials Agent unifying Planning, Physics, and Scientists, known as MAPPS. MAPPS consists of a Workflow Planner, a Tool Code Generator, and a Scientific Mediator. The Workflow Planner uses large language models (LLMs) to generate structured and multi-step workflows. The Tool Code Generator synthesizes executable Python code for various tasks, including invoking a force field foundation model that encodes physics. The Scientific Mediator coordinates communications, facilitates scientist feedback, and ensures robustness through error reflection and recovery. By unifying planning, physics, and scientists, MAPPS enables flexible and reliable materials discovery with greater autonomy, achieving a five-fold improvement in stability, uniqueness, and novelty rates compared with prior generative models when evaluated on the MP-20 data. We provide extensive experiments across diverse tasks to show that MAPPS is a promising framework for autonomous materials discovery.

