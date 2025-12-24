---
layout: default
title: "TransLLM: A Unified Multi-Task Foundation Framework for Urban Transportation via Learnable Prompting"
---

# TransLLM: A Unified Multi-Task Foundation Framework for Urban Transportation via Learnable Prompting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14782" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14782v1</a>
  <a href="https://arxiv.org/pdf/2508.14782.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14782v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14782v1', 'TransLLM: A Unified Multi-Task Foundation Framework for Urban Transportation via Learnable Prompting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaming Leng, Yunying Bi, Chuan Qin, Bing Yin, Yanyong Zhang, Chao Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-20

**🔗 代码/项目**: [GITHUB](https://github.com/BiYunying/TransLLM)

---

## 💡 一句话要点

**提出TransLLM以解决城市交通多任务问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市交通` `多任务学习` `大型语言模型` `时空建模` `强化学习` `提示机制` `电动车充电预测`

## 📋 核心要点

1. 现有方法在城市交通多任务中存在任务特定和数据需求高的局限性，影响了模型的泛化能力。
2. TransLLM通过可学习的提示组合，将时空建模与大型语言模型整合，提供了一种统一的解决方案。
3. 在七个数据集和三个任务上的实验表明，TransLLM在回归和规划问题上表现优异，具有强大的跨任务适应性。

## 📝 摘要（中文）

城市交通系统面临多种挑战，如交通预测、电动车充电需求预测和出租车调度。现有方法存在两个主要局限：小规模深度学习模型任务特定且数据需求高，限制了其在多场景下的泛化能力；而大型语言模型在处理结构化时空数据和数值推理时表现不佳。为了解决这些问题，本文提出了TransLLM，一个统一的基础框架，通过可学习的提示组合将时空建模与大型语言模型整合。该方法采用轻量级的时空编码器，通过扩张卷积和双邻接图注意力网络捕捉复杂依赖关系，并通过结构化嵌入与LLM无缝对接。新颖的实例级提示路由机制通过强化学习训练，基于输入特征动态个性化提示，超越了固定的任务特定模板。实验结果表明，TransLLM在七个数据集和三个任务上表现出色，展现了强大的泛化能力和跨任务适应性。

## 🔬 方法详解

**问题定义**：本文旨在解决城市交通系统中多任务的挑战，现有方法因任务特定和数据需求高而限制了泛化能力。

**核心思路**：TransLLM通过可学习的提示组合，将时空建模与大型语言模型结合，旨在提升模型在多任务场景下的表现。

**技术框架**：该框架包括轻量级的时空编码器、结构化嵌入与LLM的接口，以及通过强化学习训练的动态提示路由机制，整体流程为编码时空模式、动态组合个性化提示、生成任务特定预测。

**关键创新**：最重要的创新在于实例级提示路由机制，能够根据输入特征动态调整提示，超越了传统的固定模板方法。

**关键设计**：采用扩张卷积和双邻接图注意力网络来捕捉复杂的时空依赖关系，设计了专门的输出层以生成任务特定的预测。损失函数和网络结构经过精心调整，以确保模型的高效性和准确性。

## 📊 实验亮点

在七个数据集和三个任务的实验中，TransLLM在回归和规划问题上相较于十个基线模型表现出色，展现了强大的泛化能力和跨任务适应性，具体性能数据未详述。

## 🎯 应用场景

TransLLM的潜在应用领域包括城市交通管理、智能出行服务和电动车充电网络优化等。其统一框架能够有效整合多种交通任务，提高决策效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Urban transportation systems encounter diverse challenges across multiple tasks, such as traffic forecasting, electric vehicle (EV) charging demand prediction, and taxi dispatch. Existing approaches suffer from two key limitations: small-scale deep learning models are task-specific and data-hungry, limiting their generalizability across diverse scenarios, while large language models (LLMs), despite offering flexibility through natural language interfaces, struggle with structured spatiotemporal data and numerical reasoning in transportation domains. To address these limitations, we propose TransLLM, a unified foundation framework that integrates spatiotemporal modeling with large language models through learnable prompt composition. Our approach features a lightweight spatiotemporal encoder that captures complex dependencies via dilated temporal convolutions and dual-adjacency graph attention networks, seamlessly interfacing with LLMs through structured embeddings. A novel instance-level prompt routing mechanism, trained via reinforcement learning, dynamically personalizes prompts based on input characteristics, moving beyond fixed task-specific templates. The framework operates by encoding spatiotemporal patterns into contextual representations, dynamically composing personalized prompts to guide LLM reasoning, and projecting the resulting representations through specialized output layers to generate task-specific predictions. Experiments across seven datasets and three tasks demonstrate the exceptional effectiveness of TransLLM in both supervised and zero-shot settings. Compared to ten baseline models, it delivers competitive performance on both regression and planning problems, showing strong generalization and cross-task adaptability. Our code is available at https://github.com/BiYunying/TransLLM.

