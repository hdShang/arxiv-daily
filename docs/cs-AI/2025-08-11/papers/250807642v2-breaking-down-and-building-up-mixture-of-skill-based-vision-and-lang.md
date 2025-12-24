---
layout: default
title: "Breaking Down and Building Up: Mixture of Skill-Based Vision-and-Language Navigation Agents"
---

# Breaking Down and Building Up: Mixture of Skill-Based Vision-and-Language Navigation Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07642" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07642v2</a>
  <a href="https://arxiv.org/pdf/2508.07642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07642v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07642v2', 'Breaking Down and Building Up: Mixture of Skill-Based Vision-and-Language Navigation Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Ma, Yue Zhang, Zehao Wang, Parisa Kordjamshidi

**分类**: cs.AI, cs.CL, cs.CV

**发布日期**: 2025-08-11 (更新: 2025-10-01)

---

## 💡 一句话要点

**提出SkillNav框架以解决视觉语言导航中的技能泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `技能学习` `模块化框架` `合成数据集` `动态路由`

## 📋 核心要点

1. 现有视觉语言导航方法在复杂空间和时间推理时，难以在未见场景中有效泛化，表现出明显的局限性。
2. 本文提出SkillNav框架，通过将导航任务分解为可解释的原子技能，提升了基于技能的推理能力，增强了模型的泛化能力。
3. SkillNav在多个基准测试中表现出色，尤其在GSA-R2R基准上，展示了对新指令风格和未见环境的强大适应性。

## 📝 摘要（中文）

视觉语言导航（VLN）面临着理解自然语言指令和在复杂3D环境中导航的重大挑战。尽管近期通过大规模预训练和数据增强取得了一定进展，但现有方法在面对复杂的空间和时间推理时，仍然难以在未见场景中进行有效泛化。本文提出了SkillNav，一个模块化框架，将结构化的基于技能的推理引入到基于Transformer的VLN代理中。该方法将导航分解为一组可解释的原子技能（如垂直移动、区域识别、停止与暂停），每项技能由专门的代理处理。为了支持有针对性的技能训练而无需手动数据标注，我们构建了一个合成数据集管道，生成多样化、语言自然的技能特定指令-轨迹对。我们还引入了一种新颖的无训练视觉-语言模型（VLM）路由器，能够在每个时间步动态选择最合适的代理，通过对齐子目标与视觉观察和历史动作来实现。SkillNav在常用基准上取得了竞争性结果，并在GSA-R2R基准上建立了最先进的泛化能力，该基准具有新颖的指令风格和未见环境。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言导航中代理在复杂场景下的泛化能力不足的问题。现有方法在处理未见场景时，尤其是涉及复杂空间和时间推理时，表现不佳。

**核心思路**：SkillNav框架通过将导航任务分解为一系列可解释的原子技能，允许每个技能由专门的代理处理，从而实现更高效的技能训练和更好的泛化能力。

**技术框架**：SkillNav的整体架构包括多个模块：首先是技能分解模块，将导航任务分解为原子技能；其次是合成数据集生成模块，自动生成技能特定的指令-轨迹对；最后是VLM路由器，根据当前状态动态选择最合适的代理。

**关键创新**：最重要的创新在于引入了无训练的VLM路由器，它能够在每个时间步根据视觉观察和历史动作动态选择代理，这一设计显著提升了模型的适应性和灵活性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化技能学习效果，同时通过合成数据集的构建，确保了训练数据的多样性和自然性。

## 📊 实验亮点

在实验中，SkillNav在多个基准测试中取得了竞争性结果，尤其在GSA-R2R基准上，展示了对新指令风格和未见环境的最先进泛化能力，显著提升了模型的适应性。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、机器人导航和增强现实等场景，能够显著提升机器在复杂环境中的自主导航能力。未来，SkillNav框架有望推动更高级的多模态交互系统的发展，使得人机协作更加高效和自然。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) poses significant challenges for agents to interpret natural language instructions and navigate complex 3D environments. While recent progress has been driven by large-scale pre-training and data augmentation, current methods still struggle to generalize to unseen scenarios, particularly when complex spatial and temporal reasoning is required. In this work, we propose SkillNav, a modular framework that introduces structured, skill-based reasoning into Transformer-based VLN agents. Our method decomposes navigation into a set of interpretable atomic skills (e.g., Vertical Movement, Area and Region Identification, Stop and Pause), each handled by a specialized agent. To support targeted skill training without manual data annotation, we construct a synthetic dataset pipeline that generates diverse, linguistically natural, skill-specific instruction-trajectory pairs. We then introduce a novel training-free Vision-Language Model (VLM)-based router, which dynamically selects the most suitable agent at each time step by aligning sub-goals with visual observations and historical actions. SkillNav obtains competitive results on commonly used benchmarks and establishes state-of-the-art generalization to the GSA-R2R, a benchmark with novel instruction styles and unseen environments.

