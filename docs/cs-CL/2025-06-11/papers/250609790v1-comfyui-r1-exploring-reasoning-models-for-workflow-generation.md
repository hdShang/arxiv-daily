---
layout: default
title: "ComfyUI-R1: Exploring Reasoning Models for Workflow Generation"
---

# ComfyUI-R1: Exploring Reasoning Models for Workflow Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09790" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09790v1</a>
  <a href="https://arxiv.org/pdf/2506.09790.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09790v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09790v1', 'ComfyUI-R1: Exploring Reasoning Models for Workflow Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenran Xu, Yiyu Wang, Xue Yang, Longyue Wang, Weihua Luo, Kaifu Zhang, Baotian Hu, Min Zhang

**分类**: cs.CL, cs.CV, cs.SE

**发布日期**: 2025-06-11

**备注**: Work in progress. Try it out in ComfyUI-Copilot https://github.com/AIDC-AI/ComfyUI-Copilot

---

## 💡 一句话要点

**提出ComfyUI-R1以解决自动化工作流生成的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化工作流` `长链推理` `强化学习` `模块化设计` `AI艺术创作`

## 📋 核心要点

1. 现有方法在自动化工作流生成中存在高门槛，用户需要具备丰富的专业知识来有效地组合多个专用组件。
2. 论文提出ComfyUI-R1，通过构建长链推理数据和采用两阶段训练框架，自动化生成工作流，降低用户的学习曲线。
3. 实验结果显示，ComfyUI-R1模型在格式有效性上达到97%，并在节点级和图级F1分数上显著优于现有的闭源模型。

## 📝 摘要（中文）

随着AI生成内容的发展，从单一模型到模块化工作流的转变，尤其是在ComfyUI等平台上，用户在创建有效工作流时面临着高门槛的专业知识要求。为了解决这一问题，本文提出了ComfyUI-R1，这是首个用于自动化工作流生成的大型推理模型。通过构建包含4000个工作流的数据集，论文设计了长链推理数据，涵盖节点选择、工作流规划和代码级工作流表示。ComfyUI-R1采用两阶段框架进行训练：第一阶段为冷启动的推理微调，第二阶段为通过细粒度规则-度量混合奖励的强化学习，提升推理能力。实验结果表明，7B参数模型在格式有效性、节点级和图级F1分数上显著超越了现有的先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决自动化工作流生成中的高门槛问题，现有方法往往需要用户具备深厚的专业知识，导致学习曲线陡峭。

**核心思路**：论文的核心思路是构建ComfyUI-R1模型，通过长链推理（CoT）数据的生成和训练，自动化工作流的创建过程，从而降低用户的使用难度。

**技术框架**：ComfyUI-R1的整体架构包括两个主要阶段：第一阶段为冷启动的推理微调，适应ComfyUI领域；第二阶段为强化学习，通过细粒度规则-度量混合奖励来提升推理能力。

**关键创新**：最重要的技术创新在于引入长链推理数据和细粒度的混合奖励机制，这使得模型在格式有效性和结构完整性上表现优异，显著区别于现有的闭源模型。

**关键设计**：在模型设计中，采用了7B参数的架构，结合了推理微调和强化学习的双重训练策略，确保了节点级的保真度和图结构的完整性。具体的损失函数和奖励机制经过精细设计，以优化模型的推理能力。

## 📊 实验亮点

实验结果表明，ComfyUI-R1模型在格式有效性上达到了97%的高水平，同时在节点级和图级F1分数上显著优于现有的先进方法，尤其是与GPT-4o和Claude系列等闭源模型的对比中，展现出明显的性能提升，验证了长链推理在复杂工作流生成中的有效性。

## 🎯 应用场景

ComfyUI-R1的研究成果在多个领域具有潜在应用价值，包括创意内容生成、自动化设计流程和智能助手等。通过简化工作流生成过程，降低用户的技术门槛，促进AI艺术创作的普及和应用。未来，该模型可能在更多创意行业中发挥重要作用，推动智能创作工具的发展。

## 📄 摘要（原文）

> AI-generated content has evolved from monolithic models to modular workflows, particularly on platforms like ComfyUI, enabling customization in creative pipelines. However, crafting effective workflows requires great expertise to orchestrate numerous specialized components, presenting a steep learning curve for users. To address this challenge, we introduce ComfyUI-R1, the first large reasoning model for automated workflow generation. Starting with our curated dataset of 4K workflows, we construct long chain-of-thought (CoT) reasoning data, including node selection, workflow planning, and code-level workflow representation. ComfyUI-R1 is trained through a two-stage framework: (1) CoT fine-tuning for cold start, adapting models to the ComfyUI domain; (2) reinforcement learning for incentivizing reasoning capability, guided by a fine-grained rule-metric hybrid reward, ensuring format validity, structural integrity, and node-level fidelity. Experiments show that our 7B-parameter model achieves a 97\% format validity rate, along with high pass rate, node-level and graph-level F1 scores, significantly surpassing prior state-of-the-art methods that employ leading closed-source models such as GPT-4o and Claude series. Further analysis highlights the critical role of the reasoning process and the advantage of transforming workflows into code. Qualitative comparison reveals our strength in synthesizing intricate workflows with diverse nodes, underscoring the potential of long CoT reasoning in AI art creation.

