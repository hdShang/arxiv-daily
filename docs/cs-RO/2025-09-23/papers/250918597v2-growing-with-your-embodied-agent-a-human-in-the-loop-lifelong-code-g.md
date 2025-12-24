---
layout: default
title: "Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills"
---

# Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18597" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18597v2</a>
  <a href="https://arxiv.org/pdf/2509.18597.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18597v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18597v2', 'Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuan Meng, Zhenguo Sun, Max Fest, Xukun Li, Zhenshan Bing, Alois Knoll

**分类**: cs.RO

**发布日期**: 2025-09-23 (更新: 2025-09-25)

**备注**: update fig 1, typo correction - v2

---

## 💡 一句话要点

**提出人机协作的终身代码生成框架，提升长时程操作技能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机协作` `终身学习` `代码生成` `机器人操作` `长时程任务`

## 📋 核心要点

1. 现有基于LLM的机器人操作代码生成方法存在噪声大、泛化性差、难以处理长时程任务等问题。
2. 该论文提出人机协作框架，将人类修正编码为可重用技能，并利用外部记忆和RAG提升模型能力。
3. 实验表明，该框架在多个机器人操作任务中显著提升了成功率和效率，尤其擅长超长时程任务。

## 📝 摘要（中文）

本文提出了一种基于大型语言模型（LLMs）的人机协作框架，用于机器人操作的代码生成，旨在解决现有方法噪声大、受限于固定原语和上下文窗口、难以处理长时程任务等问题。该框架将人类的修正编码为可重用的技能，并利用外部记忆和检索增强生成（RAG）以及提示机制来实现动态重用。在Ravens、Franka Kitchen、MetaWorld以及真实世界环境中的实验表明，该框架的成功率达到了0.93（比基线方法高出27%），并且修正效率提高了42%。该框架能够稳健地解决“建造房屋”等需要规划超过20个原语的超长时程任务。

## 🔬 方法详解

**问题定义**：现有基于大型语言模型的机器人操作代码生成方法，在长时程任务中面临诸多挑战。这些方法通常存在噪声较大、受限于预定义的固定原语、上下文窗口有限等问题，导致难以处理复杂的、需要长期规划的任务。此外，单纯依赖LLM的推理能力在机器人领域往往不足，尤其是在人类可以轻松识别问题的情况下。

**核心思路**：该论文的核心思路是构建一个人机协作的终身学习框架，通过将人类的修正反馈融入到可重用的技能中，并利用外部记忆和检索增强生成（RAG）机制，实现技能的动态重用和知识的持续积累。这种方法旨在结合人类的领域知识和LLM的代码生成能力，从而更有效地解决长时程机器人操作任务。

**技术框架**：该框架主要包含以下几个核心模块：1) 基于LLM的代码生成器，用于将人类指令转化为初始的机器人操作代码；2) 人机交互界面，允许人类对生成的代码进行修正和反馈；3) 外部记忆模块，用于存储和管理可重用的技能；4) 检索增强生成（RAG）模块，利用外部记忆中的技能来指导代码生成，并结合提示机制实现动态重用。整个流程是一个迭代的过程，通过不断的人机协作和技能积累，逐步提升机器人的操作能力。

**关键创新**：该论文的关键创新在于提出了一种人机协作的终身学习框架，该框架能够将人类的修正反馈转化为可重用的技能，并利用外部记忆和RAG机制实现技能的动态重用。与传统的闭环反馈方法不同，该框架能够更好地泛化知识，避免灾难性遗忘，并结合人类的领域知识来提升LLM在机器人领域的推理能力。

**关键设计**：该框架的关键设计包括：1) 技能的编码方式，如何将人类的修正反馈有效地转化为可重用的技能；2) 外部记忆的组织和管理，如何高效地存储和检索技能；3) RAG模块的实现，如何利用外部记忆中的技能来指导代码生成，并结合提示机制实现动态重用；4) 人机交互界面的设计，如何方便人类进行修正和反馈。

## 📊 实验亮点

实验结果表明，该框架在Ravens、Franka Kitchen、MetaWorld以及真实世界环境中的成功率达到了0.93，比基线方法高出27%。同时，修正效率提高了42%，显著减少了人机交互的次数。该框架能够成功解决“建造房屋”等需要规划超过20个原语的超长时程任务，充分展示了其在长时程任务中的优势。

## 🎯 应用场景

该研究成果可应用于各种需要长时程规划和复杂操作的机器人任务，例如家庭服务机器人、工业自动化、医疗辅助机器人等。通过人机协作和终身学习，机器人能够不断提升其操作技能，更好地适应复杂多变的环境，并完成更加复杂的任务。该研究对于推动机器人智能化和人机协作技术的发展具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs)-based code generation for robotic manipulation has recently shown promise by directly translating human instructions into executable code, but existing methods remain noisy, constrained by fixed primitives and limited context windows, and struggle with long-horizon tasks. While closed-loop feedback has been explored, corrected knowledge is often stored in improper formats, restricting generalization and causing catastrophic forgetting, which highlights the need for learning reusable skills. Moreover, approaches that rely solely on LLM guidance frequently fail in extremely long-horizon scenarios due to LLMs' limited reasoning capability in the robotic domain, where such issues are often straightforward for humans to identify. To address these challenges, we propose a human-in-the-loop framework that encodes corrections into reusable skills, supported by external memory and Retrieval-Augmented Generation with a hint mechanism for dynamic reuse. Experiments on Ravens, Franka Kitchen, and MetaWorld, as well as real-world settings, show that our framework achieves a 0.93 success rate (up to 27% higher than baselines) and a 42% efficiency improvement in correction rounds. It can robustly solve extremely long-horizon tasks such as "build a house", which requires planning over 20 primitives.

