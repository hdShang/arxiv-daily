---
layout: default
title: Effects of Theory of Mind and Prosocial Beliefs on Steering Human-Aligned Behaviors of LLMs in Ultimatum Games
---

# Effects of Theory of Mind and Prosocial Beliefs on Steering Human-Aligned Behaviors of LLMs in Ultimatum Games

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24255" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24255v1</a>
  <a href="https://arxiv.org/pdf/2505.24255.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24255v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24255v1', 'Effects of Theory of Mind and Prosocial Beliefs on Steering Human-Aligned Behaviors of LLMs in Ultimatum Games')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Neemesh Yadav, Palakorn Achananuparp, Jing Jiang, Ee-Peng Lim

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-05-30

**备注**: 17 pages, 1 figure, 6 tables

**🔗 代码/项目**: [GITHUB](https://github.com/Stealth-py/UltimatumToM)

---

## 💡 一句话要点

**探讨心智理论与利他信念对LLM人类行为对齐的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `心智理论` `利他信念` `最终通牒游戏` `人机交互` `决策一致性` `社会机器人`

## 📋 核心要点

1. 现有的LLM在复杂社会互动中缺乏有效的心智理论推理能力，导致人类行为对齐不足。
2. 本研究通过在最终通牒游戏中引入不同的利他信念和推理方法，探讨ToM推理对人类行为对齐的影响。
3. 实验结果显示，ToM推理显著提高了LLM的决策一致性和谈判效果，验证了其在人机交互中的重要性。

## 📝 摘要（中文）

大型语言模型（LLMs）在模拟人类行为和进行心智理论（ToM）推理方面展现出潜力，这是复杂社会互动的重要技能。本研究探讨了ToM推理在谈判任务中使代理行为与人类规范对齐的作用，使用最终通牒游戏作为受控环境。我们初始化了不同利他信念（包括贪婪、公平和无私）和推理方法（如链式思维和不同ToM水平）的LLM代理，并考察了它们在多种LLM模型（如o3-mini和DeepSeek-R1 Distilled Qwen 32B）中的决策过程。2700次模拟结果表明，ToM推理增强了行为对齐、决策一致性和谈判结果。与先前发现一致，推理模型的能力有限，而具备ToM推理的模型表现更佳，且不同ToM推理顺序对游戏收益的作用不同。我们的发现有助于理解ToM在增强人机交互和合作决策中的作用。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在谈判任务中与人类行为对齐的不足，尤其是在复杂的社会互动场景中，现有方法缺乏有效的心智理论推理能力。

**核心思路**：通过在最终通牒游戏中引入不同的利他信念（贪婪、公平、无私）和推理方法（链式思维和不同ToM水平），研究ToM推理如何影响LLM的决策过程和行为对齐。

**技术框架**：研究采用了多种LLM模型（如o3-mini和DeepSeek-R1 Distilled Qwen 32B），通过2700次模拟实验，分析不同ToM水平和推理方法对谈判结果的影响。

**关键创新**：本研究的创新点在于系统性地探讨了ToM推理在LLM中的应用，揭示了其在提高人类行为对齐和决策一致性方面的潜力，与传统模型相比，具备ToM推理的模型表现更佳。

**关键设计**：实验中使用了不同的利他信念初始化和推理方法，设置了多种ToM水平，采用了链式思维推理方式，以确保模型在决策过程中的一致性和有效性。实验代码可在GitHub上获取。

## 📊 实验亮点

实验结果表明，具备ToM推理的LLM在决策一致性和谈判结果上显著优于传统推理模型。具体而言，ToM推理模型在2700次模拟中表现出更高的行为对齐率和更优的谈判结果，验证了其在复杂社交任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、智能谈判系统和社会机器人等。通过增强LLM的心智理论推理能力，可以提高其在复杂社交环境中的表现，促进更自然的合作与沟通。未来，这一研究方向可能推动更智能的AI系统在社会互动中的应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown potential in simulating human behaviors and performing theory-of-mind (ToM) reasoning, a crucial skill for complex social interactions. In this study, we investigate the role of ToM reasoning in aligning agentic behaviors with human norms in negotiation tasks, using the ultimatum game as a controlled environment. We initialized LLM agents with different prosocial beliefs (including Greedy, Fair, and Selfless) and reasoning methods like chain-of-thought (CoT) and varying ToM levels, and examined their decision-making processes across diverse LLMs, including reasoning models like o3-mini and DeepSeek-R1 Distilled Qwen 32B. Results from 2,700 simulations indicated that ToM reasoning enhances behavior alignment, decision-making consistency, and negotiation outcomes. Consistent with previous findings, reasoning models exhibit limited capability compared to models with ToM reasoning, different roles of the game benefits with different orders of ToM reasoning. Our findings contribute to the understanding of ToM's role in enhancing human-AI interaction and cooperative decision-making. The code used for our experiments can be found at https://github.com/Stealth-py/UltimatumToM.

