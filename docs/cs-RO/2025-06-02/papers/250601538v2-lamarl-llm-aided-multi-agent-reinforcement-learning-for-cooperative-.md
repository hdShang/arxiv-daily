---
layout: default
title: "LAMARL: LLM-Aided Multi-Agent Reinforcement Learning for Cooperative Policy Generation"
---

# LAMARL: LLM-Aided Multi-Agent Reinforcement Learning for Cooperative Policy Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01538" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01538v2</a>
  <a href="https://arxiv.org/pdf/2506.01538.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01538v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01538v2', 'LAMARL: LLM-Aided Multi-Agent Reinforcement Learning for Cooperative Policy Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guobin Zhu, Rui Zhou, Wenkang Ji, Shiyu Zhao

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-02 (更新: 2025-06-03)

**备注**: Accepted by IEEE Robotics and Automation Letters

**🔗 代码/项目**: [PROJECT_PAGE](https://windylab.github.io/LAMARL/)

---

## 💡 一句话要点

**提出LAMARL以解决多智能体强化学习的样本效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体强化学习` `大型语言模型` `样本效率` `自动化设计` `机器人协作`

## 📋 核心要点

1. 现有的多智能体强化学习方法在样本效率上存在显著不足，且通常需要反复手动调整奖励函数，增加了开发成本。
2. 本文提出的LAMARL方法通过结合大型语言模型，自动生成策略和奖励函数，从而提高样本效率，简化了设计过程。
3. 实验结果表明，LAMARL在形状组装任务中，样本效率提升185.9%，并且通过结构化提示显著提高了LLM的输出成功率。

## 📝 摘要（中文）

尽管多智能体强化学习（MARL）在复杂的多机器人任务中表现有效，但其样本效率低且需要手动调整奖励。大型语言模型（LLMs）在单机器人环境中展现出潜力，但在多机器人系统中的应用尚未得到充分探索。本文提出了一种新颖的LLM辅助MARL（LAMARL）方法，将MARL与LLMs结合，显著提高样本效率，无需手动设计。LAMARL由两个模块组成：第一个模块利用LLMs自动生成先验策略和奖励函数，第二个模块则使用生成的函数有效指导机器人策略训练。在形状组装基准测试中，模拟和现实世界实验均展示了LAMARL的独特优势。消融研究表明，先验策略平均提高样本效率185.9%，并增强任务完成率，而基于思维链（CoT）的结构化提示和基本API则提高了LLM输出成功率28.5%-67.5%。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体强化学习（MARL）在样本效率低和手动奖励调整方面的挑战。现有方法往往依赖于人工设计奖励函数，导致效率低下和开发复杂性增加。

**核心思路**：LAMARL通过将大型语言模型（LLMs）与MARL结合，自动生成先验策略和奖励函数，从而提高样本效率并减少人工干预。这样的设计使得系统能够更快速地适应复杂任务。

**技术框架**：LAMARL的整体架构包括两个主要模块：第一个模块利用LLMs生成先验策略和奖励函数，第二个模块则是MARL，使用这些生成的函数来指导机器人策略的训练。

**关键创新**：LAMARL的核心创新在于将LLMs引入多智能体系统，自动化生成策略和奖励函数，显著提升了样本效率和任务完成率。这一方法与传统MARL方法的本质区别在于减少了对人工设计的依赖。

**关键设计**：在设计中，采用了基于思维链（CoT）的结构化提示来优化LLM的输出，并通过消融实验验证了先验策略的有效性，确保了生成的奖励函数和策略的质量。

## 📊 实验亮点

在形状组装基准测试中，LAMARL的实验结果显示，先验策略平均提高样本效率185.9%，并且通过结构化提示，LLM的输出成功率提升了28.5%-67.5%。这些结果表明LAMARL在多智能体任务中的显著优势，展示了其在实际应用中的潜力。

## 🎯 应用场景

LAMARL的研究成果在多机器人协作任务中具有广泛的应用潜力，尤其是在需要高效学习和快速适应的场景，如自动化制造、灾害救援和智能交通系统等。通过提高样本效率，该方法能够降低开发成本并加速系统部署，未来可能推动多智能体系统的普及和应用。

## 📄 摘要（原文）

> Although Multi-Agent Reinforcement Learning (MARL) is effective for complex multi-robot tasks, it suffers from low sample efficiency and requires iterative manual reward tuning. Large Language Models (LLMs) have shown promise in single-robot settings, but their application in multi-robot systems remains largely unexplored. This paper introduces a novel LLM-Aided MARL (LAMARL) approach, which integrates MARL with LLMs, significantly enhancing sample efficiency without requiring manual design. LAMARL consists of two modules: the first module leverages LLMs to fully automate the generation of prior policy and reward functions. The second module is MARL, which uses the generated functions to guide robot policy training effectively. On a shape assembly benchmark, both simulation and real-world experiments demonstrate the unique advantages of LAMARL. Ablation studies show that the prior policy improves sample efficiency by an average of 185.9% and enhances task completion, while structured prompts based on Chain-of-Thought (CoT) and basic APIs improve LLM output success rates by 28.5%-67.5%. Videos and code are available at https://windylab.github.io/LAMARL/

