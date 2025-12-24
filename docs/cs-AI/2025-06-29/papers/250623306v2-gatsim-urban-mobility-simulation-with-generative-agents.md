---
layout: default
title: "GATSim: Urban Mobility Simulation with Generative Agents"
---

# GATSim: Urban Mobility Simulation with Generative Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23306" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23306v2</a>
  <a href="https://arxiv.org/pdf/2506.23306.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23306v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23306v2', 'GATSim: Urban Mobility Simulation with Generative Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Liu, Can Li, Wanjing Ma

**分类**: cs.AI

**发布日期**: 2025-06-29 (更新: 2025-07-18)

**🔗 代码/项目**: [GITHUB](https://github.com/qiliuchn/gatsim)

---

## 💡 一句话要点

**提出GATSim以解决城市交通模拟中的行为多样性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市交通模拟` `生成代理` `适应性学习` `层次记忆` `行为多样性` `智能交通系统` `出行决策`

## 📋 核心要点

1. 现有的城市交通模拟方法往往依赖于固定规则，无法有效捕捉人类出行决策的复杂性和适应性。
2. GATSim框架通过生成代理模拟城市交通，具备多样的社会经济特征和心理学启发的记忆系统，能够适应性学习和演变。
3. 实验结果显示，生成代理的表现与人类标注者相当，具有92%的后验概率，并自然生成现实的交通模式。

## 📝 摘要（中文）

传统的基于代理的城市交通模拟往往依赖于僵化的规则系统，难以捕捉人类出行决策中的复杂性和适应性。GATSim（生成代理交通模拟）框架利用大型语言模型和AI代理技术，模拟具有丰富人类行为的城市交通。GATSim代理具备多样的社会经济特征、个体生活方式和通过心理学启发的记忆系统塑造的不断演变的偏好。本文的主要贡献包括：综合架构、层次记忆设计以及创新的规划和反应机制。实验结果表明，生成代理的表现至少与人类标注者相当，且自然生成现实的宏观交通模式。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统城市交通模拟中代理行为缺乏多样性和适应性的问题。现有方法通常依赖于固定规则，无法有效模拟人类的复杂出行决策。

**核心思路**：GATSim框架的核心思想是利用生成代理技术，结合心理学启发的记忆系统和适应性学习，模拟具有丰富人类行为的城市交通。这样的设计使得代理能够根据个体特征和环境变化进行动态调整。

**技术框架**：GATSim的整体架构包括三个主要模块：城市交通基础模型、代理认知系统和交通模拟环境。代理通过层次记忆系统高效检索与上下文相关的信息，并在此基础上进行出行决策。

**关键创新**：本研究的关键创新在于引入了层次记忆设计和多尺度反思过程，使得代理能够将具体的出行经验转化为一般化的行为洞察。这与传统方法的静态规则系统形成鲜明对比。

**关键设计**：在技术细节上，层次记忆系统结合空间和时间关联性、关键词匹配和语义相关性，以提高信息检索效率。此外，规划和反应机制的创新设计使得代理能够灵活应对复杂的交通环境。

## 📊 实验亮点

实验结果表明，GATSim生成的代理在出行行为模拟中表现出92%的后验概率，且其生成的宏观交通模式与真实情况高度一致。这一结果表明，生成代理在模拟复杂交通环境中的有效性和可靠性，超越了传统的规则基础模型。

## 🎯 应用场景

GATSim框架具有广泛的应用潜力，能够用于城市交通规划、智能交通系统设计以及出行行为研究等领域。通过模拟真实的交通行为，相关部门可以更好地理解和优化城市交通流，提高出行效率，减少交通拥堵。

## 📄 摘要（原文）

> Traditional agent-based urban mobility simulations often rely on rigid rule-based systems that struggle to capture the complexity, adaptability, and behavioral diversity inherent in human travel decision making. Recent advancements in large language models and AI agent technologies present new opportunities to develop agents with enhanced reasoning capabilities, persistent memory, and adaptive learning. We introduce GATSim (Generative-Agent Transport Simulation), a novel framework that leverages these advancements to simulate urban mobility using generative agents with rich, human-like behaviors. Unlike conventional approaches, GATSim agents are characterized by diverse socioeconomic profiles, individual lifestyles, and evolving preferences shaped through psychologically informed memory systems, tool usage, and lifelong learning. The main contributions of this work are: (1) a comprehensive architecture that integrates an urban mobility foundation model with agent cognitive systems and a transport simulation environment; (2) a hierarchical memory designed for efficient retrieval of contextually relevant information, incorporating spatial and temporal associations, keyword matching, and semantic relevance; (3) innovative planning and reactive mechanisms for modeling adaptive mobility behaviors which integrate a multi-scale reflection process to transform specific travel experiences into generalized behavioral insights. We implement a prototype system and conduct systematic validation, demonstrating that generative agents produce believable and coherent travel behaviors. Experimental results indicate that generative agents perform at least as well as human annotators with 92\% posterior probability, while naturally producing realistic macroscopic traffic patterns. The code for the prototype implementation is publicly available at https://github.com/qiliuchn/gatsim.

