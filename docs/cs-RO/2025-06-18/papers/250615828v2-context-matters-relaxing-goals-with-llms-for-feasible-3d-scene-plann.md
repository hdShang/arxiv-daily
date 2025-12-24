---
layout: default
title: "Context Matters! Relaxing Goals with LLMs for Feasible 3D Scene Planning"
---

# Context Matters! Relaxing Goals with LLMs for Feasible 3D Scene Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15828" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15828v2</a>
  <a href="https://arxiv.org/pdf/2506.15828.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15828v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15828v2', 'Context Matters! Relaxing Goals with LLMs for Feasible 3D Scene Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Emanuele Musumeci, Michele Brienza, Francesco Argenziano, Abdel Hakim Drid, Vincenzo Suriani, Daniele Nardi, Domenico D. Bloisi

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-18 (更新: 2025-10-08)

**🔗 代码/项目**: [PROJECT_PAGE](https://lab-rococo-sapienza.github.io/context-matters/)

---

## 💡 一句话要点

**提出ContextMatters框架以解决3D场景规划中的可行性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景规划` `具身智能体` `大型语言模型` `目标放宽` `环境适应性` `机器人技术` `常识推理`

## 📋 核心要点

1. 现有方法在复杂3D环境中规划时，容易受到噪声感知和不准确谓词的影响，导致不可行的行动建议。
2. 本文提出ContextMatters框架，通过结合LLMs与经典规划，实现层次化目标放宽，适应环境上下文。
3. 实验结果表明，ContextMatters在成功率上较现有基线提升了52.45%，并在真实场景中验证了其有效性。

## 📝 摘要（中文）

具身智能体需要在复杂的3D环境中可靠地规划和行动。传统规划方法（如PDDL）提供了结构和保证，但在噪声感知和不正确的谓词基础上往往失败。另一方面，基于大型语言模型（LLMs）的规划者利用常识推理，但常常提出不可行或不安全的行动。本文提出ContextMatters框架，融合LLMs与经典规划，通过层次化目标放宽机制，帮助将符号与场景结合，并在目标不可达时提出功能等效的目标，逐步放宽约束，适应智能体环境的上下文。实验结果显示，相较于最先进的LLMs+PDDL基线，成功率提高了52.45%。

## 🔬 方法详解

**问题定义**：本文旨在解决具身智能体在复杂3D环境中进行有效规划时面临的可行性问题，现有方法在噪声感知和不准确谓词基础上往往导致不可行的行动建议。

**核心思路**：ContextMatters框架通过结合LLMs与经典规划，利用LLMs的常识推理能力来帮助智能体将符号与环境场景结合，并在目标不可达时提出功能等效的替代目标，从而逐步放宽约束，适应环境上下文。

**技术框架**：该框架主要包括三个模块：首先，LLM负责将符号与3D场景图进行结合；其次，当目标不可达时，LLM提出功能等效的替代目标；最后，系统根据环境上下文逐步放宽约束，生成可行的行动计划。

**关键创新**：最重要的创新在于层次化目标放宽机制，该机制使得许多名义上不可行的任务转变为可处理的计划，与传统方法相比，能够更好地适应复杂环境中的变化。

**关键设计**：在设计中，框架对LLMs的输入进行了优化，以确保符号与场景的准确结合，同时采用了适应性约束放宽策略，以便在目标不可达时能够有效地生成替代目标。

## 📊 实验亮点

实验结果显示，ContextMatters框架在成功率上较最先进的LLMs+PDDL基线提升了52.45%。此外，框架在真实场景中的有效执行验证了其实际应用潜力，展示了其在复杂环境中进行有效规划的能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟现实等，能够帮助具身智能体在复杂环境中进行更为灵活和安全的规划与决策。未来，ContextMatters框架有望推动智能体在动态环境中的自主学习与适应能力，提升其在实际应用中的表现。

## 📄 摘要（原文）

> Embodied agents need to plan and act reliably in real and complex 3D environments. Classical planning (e.g., PDDL) offers structure and guarantees, but in practice it fails under noisy perception and incorrect predicate grounding. On the other hand, Large Language Models (LLMs)-based planners leverage commonsense reasoning, yet frequently propose actions that are unfeasible or unsafe. Following recent works that combine the two approaches, we introduce ContextMatters, a framework that fuses LLMs and classical planning to perform hierarchical goal relaxation: the LLM helps ground symbols to the scene and, when the target is unreachable, it proposes functionally equivalent goals that progressively relax constraints, adapting the goal to the context of the agent's environment. Operating on 3D Scene Graphs, this mechanism turns many nominally unfeasible tasks into tractable plans and enables context-aware partial achievement when full completion is not achievable. Our experimental results show a +52.45% Success Rate improvement over state-of-the-art LLMs+PDDL baseline, demonstrating the effectiveness of our approach. Moreover, we validate the execution of ContextMatter in a real world scenario by deploying it on a TIAGo robot. Code, dataset, and supplementary materials are available to the community at https://lab-rococo-sapienza.github.io/context-matters/.

