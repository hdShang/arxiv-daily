---
layout: default
title: "ProRefine: Inference-Time Prompt Refinement with Textual Feedback"
---

# ProRefine: Inference-Time Prompt Refinement with Textual Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05305" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05305v3</a>
  <a href="https://arxiv.org/pdf/2506.05305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05305v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05305v3', 'ProRefine: Inference-Time Prompt Refinement with Textual Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Deepak Pandita, Tharindu Cyril Weerasooriya, Ankit Parag Shah, Isabelle Diana May-Xin Ng, Christopher M. Homan, Wei Wei

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-05 (更新: 2025-11-06)

**备注**: Workshop on Efficient Reasoning at NeurIPS 2025

---

## 💡 一句话要点

**提出ProRefine以解决推理时提示优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理优化` `代理工作流` `文本反馈` `动态提示` `多步骤推理` `人工智能` `大型语言模型`

## 📋 核心要点

1. 现有方法在多代理协作中，提示设计不当会导致性能下降，影响系统的可靠性与可扩展性。
2. ProRefine通过代理循环生成文本反馈，动态优化推理任务中的提示，无需额外训练。
3. 在五个数学推理基准数据集上，ProRefine的表现显著优于零-shot Chain-of-Thought基线，提升幅度达3至37个百分点。

## 📝 摘要（中文）

代理工作流中，多个AI代理协作完成复杂任务，依赖于有效的提示设计。若提示设计不当，可能导致代理性能下降，影响系统的可靠性和可扩展性。为了解决推理时提示优化的问题，本文提出了ProRefine，这是一种创新的推理时优化方法，利用大型语言模型的代理循环生成和应用文本反馈。ProRefine在多步骤推理任务中动态优化提示，无需额外训练或真实标签。在五个基准数学推理数据集上的评估结果显示，ProRefine的表现显著超过零-shot Chain-of-Thought基线，提升幅度在3到37个百分点之间。这种方法不仅提高了准确性，还使得较小的模型能够接近较大模型的性能，展示了其在构建更具成本效益和强大混合AI系统中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决推理时提示优化的问题。现有方法在多代理系统中，提示设计不当会导致个体代理性能下降，进而影响整个系统的表现和可靠性。

**核心思路**：ProRefine的核心思路是利用大型语言模型的代理循环生成和应用文本反馈，动态优化提示。这种方法避免了额外的训练过程，能够在推理过程中实时调整提示，提高任务的完成效果。

**技术框架**：ProRefine的整体架构包括多个阶段：首先，系统接收初始提示；然后，利用代理循环生成反馈；接着，基于反馈动态调整提示；最后，执行推理任务并输出结果。

**关键创新**：ProRefine的主要创新在于其动态提示优化机制，通过实时反馈调整提示，与传统静态提示方法形成鲜明对比。这种方法显著提升了多步骤推理任务的准确性和效率。

**关键设计**：在设计中，ProRefine不依赖于额外的训练数据或真实标签，利用现有的模型能力进行推理。同时，反馈生成的机制确保了提示的实时更新，增强了系统的灵活性和适应性。

## 📊 实验亮点

ProRefine在五个数学推理基准数据集上的评估结果显示，其性能显著优于零-shot Chain-of-Thought基线，提升幅度在3至37个百分点之间。这一结果不仅提高了模型的准确性，还使得较小模型的性能接近较大模型，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

ProRefine的研究成果在多个领域具有广泛的应用潜力，尤其是在需要多代理协作的复杂任务中，如自动化决策、智能助手和复杂系统的规划与执行。其动态优化提示的能力可以提升AI系统的整体性能，降低开发成本，推动高效能AI的普及与应用。

## 📄 摘要（原文）

> Agentic workflows, where multiple AI agents collaborate to accomplish complex tasks like reasoning or planning, play a substantial role in many cutting-edge commercial applications, and continue to fascinate researchers across fields for their potential to accomplish expensive, complex tasks that, until recently, only humans have been trusted to do. These workflows depend critically on the prompts used to provide the roles models play in such workflows. Poorly designed prompts that fail even slightly to guide individual agents can lead to sub-optimal performance that may snowball within a system of agents, limiting their reliability and scalability. To address this important problem of inference-time prompt optimization, we introduce ProRefine, an innovative inference-time optimization method that uses an agentic loop of LLMs to generate and apply textual feedback. ProRefine dynamically refines prompts for multi-step reasoning tasks without additional training or ground truth labels. Evaluated on five benchmark mathematical reasoning datasets, ProRefine significantly surpasses zero-shot Chain-of-Thought baselines by 3 to 37 percentage points. This approach not only boosts accuracy but also allows smaller models to approach the performance of their larger counterparts. This highlights its potential for building more cost-effective and powerful hybrid AI systems, thereby democratizing access to high-performing AI.

