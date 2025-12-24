---
layout: default
title: "COCORELI: Cooperative, Compositional Reconstitution \\& Execution of Language Instructions"
---

# COCORELI: Cooperative, Compositional Reconstitution \& Execution of Language Instructions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04470" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04470v1</a>
  <a href="https://arxiv.org/pdf/2509.04470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04470v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04470v1', 'COCORELI: Cooperative, Compositional Reconstitution \& Execution of Language Instructions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Swarnadeep Bhar, Omar Naim, Eleni Metheniti, Bastien Navarri, Loïc Cabannes, Morteza Ezzabady, Nicholas Asher

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-29

**备注**: 18 pages

---

## 💡 一句话要点

**提出COCORELI以解决复杂指令执行中的局限性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `智能体系统` `复杂指令执行` `动态学习` `抽象机制` `空间推理` `自然语言处理`

## 📋 核心要点

1. 现有大型语言模型在处理复杂指令时存在幻觉、空间推理不足和信息缺失等问题。
2. COCORELI通过集成中型LLM智能体与新型抽象机制和话语模块，提升了指令解析和环境表示学习能力。
3. 实验结果显示，COCORELI在自然协作构建任务中表现优于其他基线方法，显著减少了幻觉现象。

## 📝 摘要（中文）

我们提出了COCORELI，一个混合智能体框架，旨在解决大型语言模型（LLMs）在执行复杂指令、减少幻觉和空间推理等任务中的局限性。COCORELI将中型LLM智能体与新颖的抽象机制和话语模块相结合，以解析指令并在上下文中学习动态的高层次环境表示。在自然协作构建任务上的实验表明，COCORELI的表现优于单一LLM的链式推理和智能体LLM系统，且均使用更大的LLM。它能够在很大程度上避免幻觉，识别缺失信息，提出澄清请求，并更新其学习的对象。COCORELI的抽象能力超越了环境，证明了在ToolBench API完成任务中的有效性。

## 🔬 方法详解

**问题定义**：论文要解决的问题是大型语言模型在执行复杂指令时的局限性，包括幻觉现象、空间推理能力不足和信息缺失等痛点。

**核心思路**：COCORELI的核心思路是通过结合中型LLM智能体与新颖的抽象机制和话语模块，来解析指令并动态学习环境的高层次表示，从而提升执行能力。

**技术框架**：COCORELI的整体架构包括多个模块：中型LLM智能体用于指令处理，抽象机制用于信息提取，话语模块用于上下文理解，形成一个协作的智能体系统。

**关键创新**：COCORELI的关键创新在于其抽象能力和动态学习机制，使其能够有效识别缺失信息并进行澄清请求，这与传统的单一LLM方法有本质区别。

**关键设计**：在设计中，COCORELI采用了特定的参数设置和损失函数，以优化指令解析和环境表示的学习效果，同时确保智能体能够在动态环境中适应变化。

## 📊 实验亮点

在实验中，COCORELI在自然协作构建任务中表现优于单一LLM的链式推理和其他智能体LLM系统，显著减少了幻觉现象，提升了信息识别和澄清请求的能力，展示了其在复杂任务中的有效性和可靠性。

## 🎯 应用场景

COCORELI的研究成果具有广泛的应用潜力，特别是在需要复杂指令执行的领域，如机器人协作、智能家居系统和自动化生产线等。其创新的抽象机制和动态学习能力将推动智能体在实际环境中的适应性和效率，未来可能对人机协作产生深远影响。

## 📄 摘要（原文）

> We present COCORELI, a hybrid agent framework designed to tackle the limitations of large language models (LLMs) in tasks requiring: following complex instructions, minimizing hallucination, and spatial reasoning. COCORELI integrates medium-sized LLM agents with novel abstraction mechanisms and a discourse module to parse instructions to in-context learn dynamic, high-level representations of the environment. Experiments on natural collaborative construction tasks show that COCORELI outperforms single-LLM CoT and agentic LLM systems, all using larger LLMs. It manages to largely avoid hallucinations, identify missing information, ask for clarifications, and update its learned objects. COCORELI's abstraction abilities extend beyond ENVIRONMENT, as shown in the ToolBench API completion task.

