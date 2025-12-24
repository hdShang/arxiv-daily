---
layout: default
title: LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey
---

# LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00753" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00753v4</a>
  <a href="https://arxiv.org/pdf/2505.00753.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00753v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00753v4', 'LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henry Peng Zou, Wei-Chieh Huang, Yaozu Wu, Yankai Chen, Chunyu Miao, Hoang Nguyen, Yue Zhou, Weizhi Zhang, Liancheng Fang, Langzhou He, Yangning Li, Dongyuan Li, Renhe Jiang, Xue Liu, Philip S. Yu

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-01 (更新: 2025-06-26)

**备注**: Paper lists and resources are available at https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems

**🔗 代码/项目**: [GITHUB](https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems)

---

## 💡 一句话要点

**提出LLM-HAS以解决自主代理的可靠性与安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `人机协作` `自主代理` `系统调查` `反馈机制` `安全性` `可靠性` `复杂任务处理`

## 📋 核心要点

1. 现有的完全自主LLM代理面临幻觉、复杂任务处理困难及安全伦理风险等重大挑战，限制了其实际应用。
2. 论文提出通过人机协作系统（LLM-HAS），将人类反馈和控制融入代理系统，以提升其性能和可靠性。
3. 通过系统性调查，论文为LLM-HAS提供了结构化的概述，促进了该领域的进一步研究与创新。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展激发了对构建完全自主代理的兴趣。然而，基于LLM的完全自主代理仍面临重大挑战，包括由于幻觉导致的可靠性有限、处理复杂任务的困难以及显著的安全和伦理风险，这些都限制了其在实际应用中的可行性和可信度。为克服这些局限，LLM-HAS将人类提供的信息、反馈或控制纳入代理系统，以增强系统性能、可靠性和安全性。本文首次全面系统地调查了LLM-HAS，阐明了基本概念，系统呈现了塑造这些系统的核心组件，探讨了新兴应用，并讨论了人机协作带来的独特挑战和机遇。

## 🔬 方法详解

**问题定义**：本文旨在解决基于LLM的自主代理在可靠性、任务处理能力及安全性方面的不足，现有方法在这些方面存在显著挑战。

**核心思路**：论文提出通过人机协作系统（LLM-HAS）来增强代理的性能，利用人类的反馈和控制来弥补LLM的局限性，从而提高系统的可靠性和安全性。

**技术框架**：LLM-HAS的整体架构包括环境与用户画像、反馈机制、交互类型、协调与通信等主要模块，形成一个完整的人机协作流程。

**关键创新**：论文的主要创新在于系统化地整合人类反馈与控制机制，形成一种新的人机协作模式，这与传统的完全自主代理方法有本质区别。

**关键设计**：在设计中，重点关注反馈机制的有效性、交互类型的多样性以及环境适应性，确保系统能够在复杂场景中有效运作。具体的参数设置和损失函数设计尚未详细披露。

## 📊 实验亮点

论文通过系统性调查和分析，明确了LLM-HAS的核心组件和应用场景，促进了该领域的研究进展。尽管具体的实验结果和性能数据未在摘要中提供，但该研究为未来的实验设计和应用提供了重要的理论基础。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、虚拟助手、教育辅导等，能够通过人机协作提升代理的智能水平和用户体验。未来，随着技术的进步，LLM-HAS有望在更多行业中得到广泛应用，推动人机协作的深入发展。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have sparked growing interest in building fully autonomous agents. However, fully autonomous LLM-based agents still face significant challenges, including limited reliability due to hallucinations, difficulty in handling complex tasks, and substantial safety and ethical risks, all of which limit their feasibility and trustworthiness in real-world applications. To overcome these limitations, LLM-based human-agent systems (LLM-HAS) incorporate human-provided information, feedback, or control into the agent system to enhance system performance, reliability and safety. These human-agent collaboration systems enable humans and LLM-based agents to collaborate effectively by leveraging their complementary strengths. This paper provides the first comprehensive and structured survey of LLM-HAS. It clarifies fundamental concepts, systematically presents core components shaping these systems, including environment & profiling, human feedback, interaction types, orchestration and communication, explores emerging applications, and discusses unique challenges and opportunities arising from human-AI collaboration. By consolidating current knowledge and offering a structured overview, we aim to foster further research and innovation in this rapidly evolving interdisciplinary field. Paper lists and resources are available at https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems.

