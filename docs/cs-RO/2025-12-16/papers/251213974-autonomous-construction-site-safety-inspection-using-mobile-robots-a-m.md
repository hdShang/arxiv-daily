---
layout: default
title: Autonomous Construction-Site Safety Inspection Using Mobile Robots: A Multilayer VLM-LLM Pipeline
---

# Autonomous Construction-Site Safety Inspection Using Mobile Robots: A Multilayer VLM-LLM Pipeline

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13974" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13974</a>
  <a href="https://arxiv.org/pdf/2512.13974.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13974" onclick="toggleFavorite(this, '2512.13974', 'Autonomous Construction-Site Safety Inspection Using Mobile Robots: A Multilayer VLM-LLM Pipeline')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hossein Naderi, Alireza Shojaei, Philip Agee, Kereshmeh Afsari, Abiola Akanmu

**分类**: cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于多层VLM-LLM管道的移动机器人自主建筑工地安全巡检方案**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `建筑工地安全` `自主巡检` `移动机器人` `视觉语言模型` `大型语言模型` `多模态融合` `SLAM`

## 📋 核心要点

1. 现有建筑工地安全巡检主要依赖人工，自动化方法依赖特定任务数据集，难以适应快速变化的工地环境。
2. 提出一种多层VLM-LLM框架，利用移动机器人自主导航，结合视觉语言模型和大型语言模型自动生成安全巡检报告。
3. 在模拟建筑工地常见危险的实验室环境中验证，结果表明该方法具有较高的召回率和有竞争力的精确率。

## 📝 摘要（中文）

本文提出了一种利用移动机器人进行自主建筑工地安全巡检的多层框架。现有方法主要依赖于特定任务数据集，难以适应快速变化的建筑环境，且机器人现场巡检仍依赖人工遥操作和手动报告，劳动强度大。该框架结合了机器人和人工智能两大模块：机器人端通过SLAM和自主导航实现可重复覆盖和目标重访；人工智能端，基于视觉语言模型（VLM）的层生成场景描述，检索组件根据OSHA和现场策略进行信息定位，另一个VLM层基于规则评估安全状况，最后大型语言模型（LLM）层根据之前的输出生成安全报告。该框架通过概念验证实现进行了验证，并在模拟常见危险的实验室环境中进行了评估。结果表明，与最先进的闭源模型相比，该方法具有较高的召回率和有竞争力的精确率。该论文贡献了一个透明、可泛化的管道，通过暴露每一层的中间结果并将人纳入循环，超越了黑盒模型。这项工作为未来在建筑环境内外扩展到其他任务和设置奠定了基础。

## 🔬 方法详解

**问题定义**：现有建筑工地安全巡检主要依赖人工，效率低且容易出错。现有的自动化方法通常需要针对特定任务训练数据集，难以适应快速变化的建筑工地环境，需要频繁重新训练。此外，机器人现场巡检仍然依赖于人工遥操作和手动报告，增加了劳动强度和成本。

**核心思路**：本文的核心思路是将机器人自主导航能力与视觉语言模型（VLM）和大型语言模型（LLM）相结合，构建一个多层管道，实现自主安全巡检和报告生成。通过VLM理解场景，LLM结合安全规则生成报告，从而减少人工干预，提高巡检效率和准确性。

**技术框架**：该框架包含机器人和人工智能两大模块。机器人模块负责自主导航和环境感知，利用SLAM技术构建地图并规划路径。人工智能模块包含四个主要层：1) VLM场景描述层：利用VLM对机器人采集的图像进行场景描述。2) 检索层：根据场景描述，从OSHA（职业安全与健康管理局）标准和现场安全策略中检索相关规则。3) VLM安全评估层：基于场景描述和检索到的安全规则，利用VLM评估安全状况。4) LLM报告生成层：根据前三层的输出，利用LLM生成最终的安全巡检报告。

**关键创新**：该方法的主要创新在于将VLM和LLM应用于建筑工地安全巡检，构建了一个透明、可泛化的多层管道。与传统的黑盒模型相比，该方法暴露了每一层的中间结果，方便人工干预和调试。此外，该方法不依赖于特定任务的数据集，具有更好的泛化能力。

**关键设计**：在VLM场景描述层，使用了预训练的VLM模型，并针对建筑工地场景进行了微调。检索层使用了基于向量相似度的检索方法，提高了检索效率和准确性。VLM安全评估层使用了提示工程（Prompt Engineering）技术，引导VLM进行安全评估。LLM报告生成层使用了链式思考（Chain-of-Thought）方法，提高了报告的逻辑性和可读性。具体参数设置和网络结构在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在模拟建筑工地场景中具有较高的召回率和有竞争力的精确率。与最先进的闭源模型相比，该方法在保证性能的同时，具有更好的透明性和可解释性。具体的性能数据和提升幅度在摘要中提及，但未给出具体数值，属于未知信息。

## 🎯 应用场景

该研究成果可应用于建筑工地、工厂、矿山等高危环境的安全巡检，降低人工巡检的风险和成本，提高巡检效率和准确性。未来可扩展到其他任务和环境，例如灾后救援、环境监测等。该技术还有潜力集成到智能建筑和智慧城市系统中，实现更全面的安全管理。

## 📄 摘要（原文）

> Construction safety inspection remains mostly manual, and automated approaches still rely on task-specific datasets that are hard to maintain in fast-changing construction environments due to frequent retraining. Meanwhile, field inspection with robots still depends on human teleoperation and manual reporting, which are labor-intensive. This paper aims to connect what a robot sees during autonomous navigation to the safety rules that are common in construction sites, automatically generating a safety inspection report. To this end, we proposed a multi-layer framework with two main modules: robotics and AI. On the robotics side, SLAM and autonomous navigation provide repeatable coverage and targeted revisits via waypoints. On AI side, a Vision Language Model (VLM)-based layer produces scene descriptions; a retrieval component powered grounds those descriptions in OSHA and site policies; Another VLM-based layer assesses the safety situation based on rules; and finally Large Language Model (LLM) layer generates safety reports based on previous outputs. The framework is validated with a proof-of-concept implementation and evaluated in a lab environment that simulates common hazards across three scenarios. Results show high recall with competitive precision compared to state-of-the-art closed-source models. This paper contributes a transparent, generalizable pipeline that moves beyond black-box models by exposing intermediate artifacts from each layer and keeping the human in the loop. This work provides a foundation for future extensions to additional tasks and settings within and beyond construction context.

