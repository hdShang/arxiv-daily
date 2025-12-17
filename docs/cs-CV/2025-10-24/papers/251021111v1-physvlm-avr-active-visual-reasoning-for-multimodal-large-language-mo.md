---
layout: default
title: PhysVLM-AVR: Active Visual Reasoning for Multimodal Large Language Models in Physical Environments
---

# PhysVLM-AVR: Active Visual Reasoning for Multimodal Large Language Models in Physical Environments

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.21111" target="_blank" class="toolbar-btn">arXiv: 2510.21111v1</a>
    <a href="https://arxiv.org/pdf/2510.21111.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21111v1" 
            onclick="toggleFavorite(this, '2510.21111v1', 'PhysVLM-AVR: Active Visual Reasoning for Multimodal Large Language Models in Physical Environments')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Weijie Zhou, Xuantang Xiong, Yi Peng, Manli Tao, Chaoyang Zhao, Honghui Dong, Ming Tang, Jinqiao Wang

**分类**: cs.CV

**发布日期**: 2025-10-24

**备注**: 39th Conference on Neural Information Processing Systemss (NeurIPS 2025)

---

## 💡 一句话要点

**提出PhysVLM-AVR以解决动态环境中的视觉推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `主动视觉推理` `多模态大语言模型` `信息获取` `动态环境` `推理正确性` `交互环境` `链式思维`

## 📋 核心要点

1. 现有的多模态大语言模型在静态环境中进行视觉推理，无法有效应对现实世界中的信息不完整性和动态变化。
2. 本文提出主动视觉推理（AVR）任务，要求智能体通过物理动作主动获取信息，并在多步骤中整合观察结果以进行推理。
3. PhysVLM-AVR在CLEVR-AVR等基准测试中表现出色，展示了在动态环境中进行有效推理的能力，填补了现有模型的不足。

## 📝 摘要（中文）

在多模态大语言模型（MLLMs）中，视觉推理主要集中在静态、完全可观察的环境中，这限制了其在现实世界中的有效性。人类通过主动探索和与环境互动来获取信息。为此，本文提出了主动视觉推理（AVR）任务，扩展了视觉推理至部分可观察的互动环境。我们引入了CLEVR-AVR基准，评估推理的正确性和信息获取的效率，并构建了AVR-152k数据集，提供了丰富的链式思维注释。基于此，我们开发了PhysVLM-AVR，实现在CLEVR-AVR等任务上的最先进性能，同时揭示了现有模型在主动获取和整合新信息方面的不足。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在动态、部分可观察环境中进行视觉推理的不足，现有方法无法有效处理信息的不完整性和动态变化。

**核心思路**：提出主动视觉推理（AVR）任务，智能体通过物理动作主动获取信息，并在多步骤中整合观察结果以进行推理，动态调整决策。

**技术框架**：整体架构包括信息获取模块、观察整合模块和决策调整模块，智能体在每个步骤中根据视觉反馈进行决策。

**关键创新**：引入CLEVR-AVR基准和AVR-152k数据集，提供多轮交互环境的评估标准，强调信息获取效率和推理正确性。

**关键设计**：采用链式思维注释，设计了高阶马尔可夫决策过程的训练框架，关键参数和损失函数经过精心调整以优化智能体的学习效果。

## 📊 实验亮点

PhysVLM-AVR在CLEVR-AVR基准测试中实现了最先进的性能，展示了在动态环境中有效推理的能力。与现有模型相比，性能提升幅度显著，尤其在信息获取和推理的整合方面表现突出。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、智能助手和增强现实等，能够提升智能体在复杂环境中的决策能力和交互效率。未来，随着技术的进步，PhysVLM-AVR有望在实际应用中实现更高水平的智能化和自主性。

## 📄 摘要（原文）

> Visual reasoning in multimodal large language models (MLLMs) has primarily been studied in static, fully observable settings, limiting their effectiveness in real-world environments where information is often incomplete due to occlusion or limited field of view. Humans, in contrast, actively explore and interact with their environment-moving, examining, and manipulating objects-to gather information through a closed-loop process integrating perception, reasoning, and action. Inspired by this human capability, we introduce the Active Visual Reasoning (AVR) task, extending visual reasoning to partially observable, interactive environments. AVR necessitates agents to: (1) actively acquire information via sequential physical actions, (2) integrate observations across multiple steps for coherent reasoning, and (3) dynamically adjust decisions based on evolving visual feedback. To rigorously evaluate AVR, we introduce CLEVR-AVR, a simulation benchmark featuring multi-round interactive environments designed to assess both reasoning correctness and information-gathering efficiency. We present AVR-152k, a large-scale dataset that offers rich Chain-of-Thought (CoT) annotations detailing iterative reasoning for uncertainty identification, action-conditioned information gain prediction, and information-maximizing action selection, crucial for training agents in a higher-order Markov Decision Process. Building on this, we develop PhysVLM-AVR, an MLLM achieving state-of-the-art performance on CLEVR-AVR, embodied reasoning (OpenEQA, RoboVQA), and passive visual reasoning (GeoMath, Geometry30K). Our analysis also reveals that current embodied MLLMs, despite detecting information incompleteness, struggle to actively acquire and integrate new information through interaction, highlighting a fundamental gap in active reasoning capabilities.

