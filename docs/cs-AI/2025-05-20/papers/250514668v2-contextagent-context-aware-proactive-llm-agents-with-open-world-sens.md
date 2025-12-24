---
layout: default
title: ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions
---

# ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14668" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14668v2</a>
  <a href="https://arxiv.org/pdf/2505.14668.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14668v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14668v2', 'ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bufang Yang, Lilin Xu, Liekang Zeng, Kaiwei Liu, Siyang Jiang, Wenrui Lu, Hongkai Chen, Xiaofan Jiang, Guoliang Xing, Zhenyu Yan

**分类**: cs.AI, cs.CL, cs.HC

**发布日期**: 2025-05-20 (更新: 2025-10-27)

**备注**: Accepted by NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/openaiotlab/ContextAgent)

---

## 💡 一句话要点

**提出ContextAgent以解决现有主动智能体的局限性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文感知` `主动智能体` `多模态融合` `用户意图理解` `可穿戴设备`

## 📋 核心要点

1. 现有主动智能体依赖封闭环境的观察，导致用户意图理解不足和功能受限。
2. ContextAgent通过提取多维感知上下文，结合历史数据，增强LLM智能体的主动性。
3. 在ContextAgentBench上，ContextAgent在主动预测和工具调用的准确性上分别提高了8.5%和6.0%。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展使得智能体从被动响应转向主动支持。然而，现有的主动智能体要么仅依赖封闭环境中的观察（如桌面用户界面）进行直接推理，要么采用基于规则的主动通知，导致用户意图理解不足和功能有限。本文提出了ContextAgent，这是首个结合人类周围广泛感知上下文的上下文感知主动智能体，以增强LLM智能体的主动性。ContextAgent首先从可穿戴设备的多维感知中提取上下文，以理解用户意图。然后，它利用感知上下文和历史数据中的个性化信息来预测主动服务的必要性。当需要主动协助时，ContextAgent会自动调用必要的工具，以不打扰用户的方式提供帮助。我们还构建了ContextAgentBench，这是评估上下文感知主动LLM智能体的首个基准，涵盖1000个样本和20种工具。实验结果显示，ContextAgent在主动预测和工具调用的准确性上分别比基线提高了8.5%和6.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有主动智能体在用户意图理解和功能上的局限性，现有方法往往依赖封闭环境的观察，导致主动服务效果不佳。

**核心思路**：ContextAgent的核心思路是通过提取来自可穿戴设备的多维感知上下文，结合历史数据中的个性化信息，来更准确地理解用户意图并预测主动服务的需求。

**技术框架**：ContextAgent的整体架构包括上下文提取模块、意图理解模块和工具调用模块。首先，通过可穿戴设备收集视频和音频等多维感知数据；其次，分析这些数据以理解用户意图；最后，根据预测的需求自动调用相应工具提供帮助。

**关键创新**：ContextAgent的主要创新在于其上下文感知能力，能够从多种感知数据中提取信息，从而超越传统的基于规则的主动通知方法，提供更为精准的用户服务。

**关键设计**：在设计上，ContextAgent使用了多模态融合技术来处理不同类型的感知数据，并通过深度学习模型优化用户意图的预测。此外，损失函数的设计考虑了主动服务的准确性和用户体验的平衡。

## 📊 实验亮点

在ContextAgentBench的实验中，ContextAgent在主动预测的准确性上比基线提高了8.5%，在工具调用的准确性上提高了6.0%。这些结果表明，ContextAgent在理解用户意图和提供主动服务方面具有显著优势，展示了其在实际应用中的潜力。

## 🎯 应用场景

ContextAgent的研究成果具有广泛的应用潜力，尤其在智能家居、个人助理和健康监测等领域。通过提供更为精准和人性化的主动服务，ContextAgent能够显著提升用户体验，并推动智能助手向更高层次的发展。未来，该技术可能会在更多人机交互场景中得到应用，促进智能体的普及与发展。

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) have propelled intelligent agents from reactive responses to proactive support. While promising, existing proactive agents either rely exclusively on observations from enclosed environments (e.g., desktop UIs) with direct LLM inference or employ rule-based proactive notifications, leading to suboptimal user intent understanding and limited functionality for proactive service. In this paper, we introduce ContextAgent, the first context-aware proactive agent that incorporates extensive sensory contexts surrounding humans to enhance the proactivity of LLM agents. ContextAgent first extracts multi-dimensional contexts from massive sensory perceptions on wearables (e.g., video and audio) to understand user intentions. ContextAgent then leverages the sensory contexts and personas from historical data to predict the necessity for proactive services. When proactive assistance is needed, ContextAgent further automatically calls the necessary tools to assist users unobtrusively. To evaluate this new task, we curate ContextAgentBench, the first benchmark for evaluating context-aware proactive LLM agents, covering 1,000 samples across nine daily scenarios and twenty tools. Experiments on ContextAgentBench show that ContextAgent outperforms baselines by achieving up to 8.5% and 6.0% higher accuracy in proactive predictions and tool calling, respectively. We hope our research can inspire the development of more advanced, human-centric, proactive AI assistants. The code and dataset are publicly available at https://github.com/openaiotlab/ContextAgent.

