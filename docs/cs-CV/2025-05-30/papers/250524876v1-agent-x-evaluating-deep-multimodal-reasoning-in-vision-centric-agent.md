---
layout: default
title: "Agent-X: Evaluating Deep Multimodal Reasoning in Vision-Centric Agentic Tasks"
---

# Agent-X: Evaluating Deep Multimodal Reasoning in Vision-Centric Agentic Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24876" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24876v1</a>
  <a href="https://arxiv.org/pdf/2505.24876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24876v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24876v1', 'Agent-X: Evaluating Deep Multimodal Reasoning in Vision-Centric Agentic Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tajamul Ashraf, Amal Saqib, Hanan Ghani, Muhra AlMahri, Yuhao Li, Noor Ahsan, Umair Nawaz, Jean Lahoud, Hisham Cholakkal, Mubarak Shah, Philip Torr, Fahad Shahbaz Khan, Rao Muhammad Anwer, Salman Khan

**分类**: cs.CV, cs.CL

**发布日期**: 2025-05-30

**🔗 代码/项目**: [GITHUB](https://github.com/mbzuai-oryx/Agent-X)

---

## 💡 一句话要点

**提出Agent-X以解决多步视觉推理任务评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉理解` `深度学习` `代理任务` `推理评估` `工具使用` `真实场景`

## 📋 核心要点

1. 现有基准评估方法主要依赖合成的单轮查询，缺乏对多步推理和真实场景的考量。
2. 论文提出Agent-X基准，包含828个多模态任务，强调在真实环境中进行多步推理的能力评估。
3. 实验结果显示，当前最佳模型在多步视觉任务中的成功率低于50%，揭示了推理能力的不足。

## 📝 摘要（中文）

深度推理在解决复杂任务中至关重要，尤其是在需要顺序和多模态理解的视觉中心场景中。然而，现有基准通常仅评估具有完全合成的单轮查询的代理，视觉模态有限，且缺乏评估多步骤推理质量的框架。为此，我们提出了Agent-X，这是一个大规模基准，用于评估视觉中心代理在真实多模态环境中的多步和深度推理能力。Agent-X包含828个具有真实视觉上下文的代理任务，涵盖一般视觉推理、网页浏览、安全监控、自动驾驶、体育和数学推理等六大环境。我们的基准要求代理在这些多样化的环境中结合工具使用与明确的逐步决策。此外，我们提出了一种细粒度的逐步评估框架，评估每个推理步骤的正确性和逻辑一致性，以及工具使用的有效性。实验结果显示，即使是表现最好的模型，如GPT、Gemini和Qwen系列，在解决多步视觉任务时也面临挑战，完整链成功率不足50%。这些发现突显了当前LMM推理和工具使用能力的关键瓶颈，并指明了未来研究方向。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态推理基准在真实场景中评估多步推理能力的不足。现有方法通常只关注单轮查询，无法有效评估复杂任务的推理质量。

**核心思路**：论文提出Agent-X基准，通过设计多样化的真实视觉任务，要求代理在多步推理中结合工具使用与逐步决策，提升推理能力的评估标准。

**技术框架**：Agent-X的整体架构包括任务生成模块、评估框架和数据集。任务生成模块创建多种真实场景任务，评估框架则用于分析推理步骤的正确性和逻辑一致性。

**关键创新**：最重要的创新在于引入了细粒度的逐步评估框架，能够系统性地分析每一步推理的有效性，与现有方法相比，提供了更深入的推理质量评估。

**关键设计**：在设计中，任务涵盖多种视觉模态，如图像、视频和文本，评估过程中采用了明确的工具使用标准，确保每个推理步骤的逻辑性和有效性。

## 📊 实验亮点

实验结果显示，当前最先进的模型在多步视觉任务中的完整链成功率不足50%，如GPT、Gemini和Qwen系列模型均未能有效解决这些任务。这一结果揭示了多模态推理能力的显著不足，指向了未来研究的关键方向。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶系统和安全监控等，能够提升这些系统在复杂环境中的决策能力和推理水平。未来，Agent-X基准将推动多模态推理模型的研究与发展，促进更智能的视觉中心代理的出现。

## 📄 摘要（原文）

> Deep reasoning is fundamental for solving complex tasks, especially in vision-centric scenarios that demand sequential, multimodal understanding. However, existing benchmarks typically evaluate agents with fully synthetic, single-turn queries, limited visual modalities, and lack a framework to assess reasoning quality over multiple steps as required in real-world settings. To address this, we introduce Agent-X, a large-scale benchmark for evaluating vision-centric agents multi-step and deep reasoning capabilities in real-world, multimodal settings. Agent- X features 828 agentic tasks with authentic visual contexts, including images, multi-image comparisons, videos, and instructional text. These tasks span six major agentic environments: general visual reasoning, web browsing, security and surveillance, autonomous driving, sports, and math reasoning. Our benchmark requires agents to integrate tool use with explicit, stepwise decision-making in these diverse settings. In addition, we propose a fine-grained, step-level evaluation framework that assesses the correctness and logical coherence of each reasoning step and the effectiveness of tool usage throughout the task. Our results reveal that even the best-performing models, including GPT, Gemini, and Qwen families, struggle to solve multi-step vision tasks, achieving less than 50% full-chain success. These findings highlight key bottlenecks in current LMM reasoning and tool-use capabilities and identify future research directions in vision-centric agentic reasoning models. Our data and code are publicly available at https://github.com/mbzuai-oryx/Agent-X

