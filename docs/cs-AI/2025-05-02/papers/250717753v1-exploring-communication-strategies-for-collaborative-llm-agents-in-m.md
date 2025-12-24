---
layout: default
title: Exploring Communication Strategies for Collaborative LLM Agents in Mathematical Problem-Solving
---

# Exploring Communication Strategies for Collaborative LLM Agents in Mathematical Problem-Solving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.17753" class="toolbar-btn" target="_blank">📄 arXiv: 2507.17753v1</a>
  <a href="https://arxiv.org/pdf/2507.17753.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.17753v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.17753v1', 'Exploring Communication Strategies for Collaborative LLM Agents in Mathematical Problem-Solving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Zhang, Xiaoming Zhai, Jionghao Lin, Jionghao Lin, Jennifer Kleiman, Diego Zapata-Rivera, Carol Forsyth, Yang Jiang, Xiangen Hu, Arthur C. Graesser

**分类**: cs.HC, cs.AI, cs.CL, cs.CY

**发布日期**: 2025-05-02

---

## 💡 一句话要点

**探索协作LLM代理的沟通策略以提升数学问题解决效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `协作学习` `数学问题解决` `沟通策略` `教育技术` `多代理系统`

## 📋 核心要点

1. 现有研究对LLM代理的沟通策略缺乏系统性评估，影响了其在教育中的应用效果。
2. 本研究提出四种沟通模式，通过双代理设置提升数学问题解决的效率和准确性。
3. 实验结果显示，双代理设置优于单代理，同伴协作模式的准确性最高，表明沟通策略的重要性。

## 📝 摘要（中文）

大型语言模型（LLM）代理在AI辅助教育中日益受到重视，能够支持辅导和学习。有效的沟通策略能够提升LLM代理的协作问题解决效率，并促进教育中的经济适用性。然而，关于不同沟通策略对代理问题解决影响的系统性研究仍然较少。本研究考察了四种沟通模式：教师-学生互动、同伴协作、互助教学和批判性辩论，使用OpenAI的GPT-4o模型在双代理的聊天式数学问题解决环境中进行评估。结果表明，双代理设置优于单一代理，其中同伴协作模式的准确性最高。对话行为如陈述、确认和提示在协作问题解决中起着关键作用。尽管多代理框架增强了计算任务，但有效的沟通策略对于解决AI教育中的复杂问题至关重要。

## 🔬 方法详解

**问题定义**：本论文旨在解决LLM代理在数学问题解决中的沟通效率问题。现有方法缺乏对不同沟通策略的系统评估，导致协作效果不佳。

**核心思路**：论文提出通过比较四种沟通模式（教师-学生互动、同伴协作、互助教学和批判性辩论）来提升双代理的协作能力，以优化问题解决效率。

**技术框架**：研究采用双代理的聊天式环境，利用OpenAI GPT-4o模型进行实验。主要模块包括代理间的沟通策略设计、问题解决过程的协作机制以及结果评估。

**关键创新**：本研究的创新点在于系统性地比较不同的沟通模式对LLM代理协作效率的影响，填补了现有文献的空白。

**关键设计**：在实验中，设置了不同的对话行为（如陈述、确认和提示），并通过MATH数据集评估各模式的表现，确保了实验的科学性和可重复性。

## 📊 实验亮点

实验结果表明，双代理设置在数学问题解决中显著优于单一代理，尤其是同伴协作模式的准确性达到了最高水平，具体提升幅度未知。这一发现强调了有效沟通策略在多代理系统中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和在线学习平台。通过优化LLM代理的沟通策略，可以提升学生的学习体验和问题解决能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Model (LLM) agents are increasingly utilized in AI-aided education to support tutoring and learning. Effective communication strategies among LLM agents improve collaborative problem-solving efficiency and facilitate cost-effective adoption in education. However, little research has systematically evaluated the impact of different communication strategies on agents' problem-solving. Our study examines four communication modes, \textit{teacher-student interaction}, \textit{peer-to-peer collaboration}, \textit{reciprocal peer teaching}, and \textit{critical debate}, in a dual-agent, chat-based mathematical problem-solving environment using the OpenAI GPT-4o model. Evaluated on the MATH dataset, our results show that dual-agent setups outperform single agents, with \textit{peer-to-peer collaboration} achieving the highest accuracy. Dialogue acts like statements, acknowledgment, and hints play a key role in collaborative problem-solving. While multi-agent frameworks enhance computational tasks, effective communication strategies are essential for tackling complex problems in AI education.

