---
layout: default
title: "90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development"
---

# 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26161" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26161v1</a>
  <a href="https://arxiv.org/pdf/2509.26161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26161v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26161v1', '90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runxin Yang, Yuxuan Wan, Shuqing Li, Michael R. Lyu

**分类**: cs.AI, cs.SE

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/yxwan123/UniGen)

---

## 💡 一句话要点

**UniGen：基于MLLM的零代码3D游戏开发框架，开发速度提升90%。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D游戏开发` `零代码` `多模态大语言模型` `自动化` `多智能体系统` `游戏引擎` `自然语言处理`

## 📋 核心要点

1. 现有游戏自动化开发方法局限于2D或孤立代码，需手动集成，且交互逻辑处理性能差。
2. UniGen提出端到端多智能体框架，将自然语言需求转化为可运行的3D游戏，无需编码。
3. 实验表明，UniGen显著降低了游戏开发时间，无需编码即可实现游戏创建，提速91.4%。

## 📝 摘要（中文）

开发3D游戏需要编程、3D建模和引擎配置等多领域的专业知识，这限制了潜在创作者的数量。最近，研究人员开始探索自动化游戏开发。然而，现有方法面临三个主要挑战：(1)范围局限于2D内容生成或孤立的代码片段；(2)需要手动将生成的组件集成到游戏引擎中；(3)在处理交互式游戏逻辑和状态管理方面的性能较差。多模态大型语言模型(MLLM)展示了简化游戏生成任务的潜力，但如何将这些输出转化为基于Unity和Unreal Engine等游戏引擎的、可用于生产的、可执行的游戏项目仍然是一个关键缺口。为了弥合这一差距，本文介绍UniGen，这是第一个端到端协调的多智能体框架，可从自然语言需求中自动进行零代码可运行3D游戏开发。具体来说，UniGen使用规划代理将用户需求解释为结构化蓝图和工程化的逻辑描述；然后，生成代理生成可执行的C#脚本；然后，自动化代理处理特定于引擎的组件绑定和场景构建；最后，调试代理通过对话交互提供实时错误纠正。我们在三个不同的游戏原型上评估了UniGen。结果表明，UniGen不仅通过不需要用户进行编码来实现游戏创建的民主化，而且还将开发时间缩短了91.4%。

## 🔬 方法详解

**问题定义**：现有3D游戏开发高度依赖专业技能，包括编程、建模和引擎配置，阻碍了非专业人士参与。现有的自动化方法要么局限于2D内容，要么生成孤立的代码片段，需要手动集成到游戏引擎中，并且在处理复杂的交互逻辑和状态管理方面表现不佳。

**核心思路**：UniGen的核心思路是利用多模态大型语言模型（MLLM）的强大能力，构建一个端到端的自动化框架，将自然语言描述的游戏需求转化为可执行的3D游戏。通过多智能体协作，实现需求理解、代码生成、引擎集成和错误调试的自动化，从而降低游戏开发的门槛。

**技术框架**：UniGen采用一个包含四个主要智能体的框架：规划代理（Planning Agent）、生成代理（Generation Agent）、自动化代理（Automation Agent）和调试代理（Debugging Agent）。规划代理负责将用户输入的自然语言需求解析为结构化的蓝图和逻辑描述。生成代理根据蓝图生成可执行的C#脚本。自动化代理负责将生成的脚本和资源绑定到游戏引擎（如Unity或Unreal Engine）中的相应组件，并构建游戏场景。调试代理通过对话交互，实时检测和修复错误。

**关键创新**：UniGen的关键创新在于其端到端的自动化流程和多智能体协作框架。它首次实现了从自然语言需求到可运行3D游戏的零代码转换，无需人工干预。通过多智能体的协同工作，实现了游戏开发的各个环节的自动化，包括需求理解、代码生成、引擎集成和错误调试。

**关键设计**：UniGen的关键设计包括：(1)规划代理使用MLLM将自然语言需求分解为结构化蓝图，蓝图包含游戏对象、属性、行为和交互关系等信息。(2)生成代理利用代码生成模型，根据蓝图生成高质量的C#脚本，脚本实现了游戏逻辑和交互。(3)自动化代理使用引擎API，自动将生成的脚本和资源绑定到游戏引擎中的相应组件，并构建游戏场景。(4)调试代理通过分析游戏运行时的日志和错误信息，与用户进行对话交互，帮助用户定位和修复错误。

## 📊 实验亮点

UniGen在三个不同的游戏原型上进行了评估，实验结果表明，UniGen能够显著降低游戏开发时间，平均降低91.4%。此外，UniGen实现了零代码游戏开发，无需用户编写任何代码即可创建可运行的3D游戏。这表明UniGen在游戏自动化开发方面具有显著的优势。

## 🎯 应用场景

UniGen具有广泛的应用前景，可用于游戏原型设计、教育游戏开发、虚拟现实/增强现实应用开发等领域。它降低了游戏开发的门槛，使非专业人士也能参与游戏创作，促进了游戏开发的民主化。未来，UniGen可以扩展到支持更复杂的游戏类型和更丰富的交互方式，并与其他AI技术（如强化学习）相结合，实现更智能化的游戏开发。

## 📄 摘要（原文）

> Developing 3D games requires specialized expertise across multiple domains, including programming, 3D modeling, and engine configuration, which limits access to millions of potential creators. Recently, researchers have begun to explore automated game development. However, existing approaches face three primary challenges: (1) limited scope to 2D content generation or isolated code snippets; (2) requirement for manual integration of generated components into game engines; and (3) poor performance on handling interactive game logic and state management. While Multimodal Large Language Models (MLLMs) demonstrate potential capabilities to ease the game generation task, a critical gap still remains in translating these outputs into production-ready, executable game projects based on game engines such as Unity and Unreal Engine.
>   To bridge the gap, this paper introduces UniGen, the first end-to-end coordinated multi-agent framework that automates zero-coding development of runnable 3D games from natural language requirements. Specifically, UniGen uses a Planning Agent that interprets user requirements into structured blueprints and engineered logic descriptions; after which a Generation Agent produces executable C# scripts; then an Automation Agent handles engine-specific component binding and scene construction; and lastly a Debugging Agent provides real-time error correction through conversational interaction. We evaluated UniGen on three distinct game prototypes. Results demonstrate that UniGen not only democratizes game creation by requiring no coding from the user, but also reduces development time by 91.4%. We release UniGen at https://github.com/yxwan123/UniGen. A video demonstration is available at https://www.youtube.com/watch?v=xyJjFfnxUx0.

