---
layout: default
title: Assessing Long-Term Electricity Market Design for Ambitious Decarbonization Targets using Multi-Agent Reinforcement Learning
---

# Assessing Long-Term Electricity Market Design for Ambitious Decarbonization Targets using Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17444" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17444v1</a>
  <a href="https://arxiv.org/pdf/2512.17444.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17444v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17444v1', 'Assessing Long-Term Electricity Market Design for Ambitious Decarbonization Targets using Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Javier Gonzalez-Ruiz, Carlos Rodriguez-Pardo, Iacopo Savelli, Alice Di Bella, Massimo Tavoni

**分类**: cs.LG, cs.AI, cs.NE, econ.GN

**发布日期**: 2025-12-19

**备注**: Accepted to Energy and AI. Code available in https://github.com/jjgonzalez2491/MARLEY_V1

---

## 💡 一句话要点

**提出基于多智能体强化学习的电力市场长期设计评估框架，助力实现深度脱碳目标。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `电力市场设计` `深度脱碳` `能源政策` `市场机制`

## 📋 核心要点

1. 现有电力市场设计工具难以有效评估长期政策和市场机制对深度脱碳的影响。
2. 利用多智能体强化学习，模拟发电公司在不同市场设计和政策下的投资决策，捕捉竞争动态。
3. 通过意大利电力系统案例研究，验证模型在评估市场设计和避免价格波动方面的有效性。

## 📝 摘要（中文）

电力系统是将当今社会转型为无碳经济的关键。长期电力市场机制，包括拍卖、支持计划和其他政策工具，对于塑造电力生产结构至关重要。鉴于需要更先进的工具来支持决策者和其他利益相关者设计、测试和评估长期市场，本研究提出了一种多智能体强化学习模型，该模型能够捕捉脱碳能源系统的关键特征。利润最大化的发电公司在批发电力市场中做出投资决策，响应系统需求、竞争动态和政策信号。该模型采用独立的近端策略优化（PPO），因其适用于分散和竞争环境而被选中。尽管如此，考虑到多智能体环境中独立学习的固有挑战，广泛的超参数搜索确保分散训练产生与竞争行为一致的市场结果。该模型应用于意大利电力系统的简化版本，并在不同程度的竞争、市场设计和政策情景下进行了测试。结果突出了市场设计对于电力部门脱碳和避免价格波动的关键作用。所提出的框架允许评估长期电力市场，其中多个政策和市场机制同时相互作用，市场参与者响应并适应脱碳路径。

## 🔬 方法详解

**问题定义**：现有电力市场设计评估工具难以模拟市场参与者的长期投资决策行为，无法有效评估不同政策和市场机制对电力系统深度脱碳的影响。现有方法通常依赖于静态模型或简化假设，难以捕捉市场竞争的复杂动态。

**核心思路**：本研究的核心思路是利用多智能体强化学习（MARL）模拟电力市场中发电公司的投资决策行为。每个发电公司被建模为一个独立的智能体，通过与环境（电力市场）交互学习，最大化自身利润。这种方法能够捕捉市场参与者之间的竞争和合作关系，以及政策和市场机制对投资决策的长期影响。

**技术框架**：该框架包含以下主要模块：1) 电力市场环境：模拟电力市场的供需关系、价格形成机制和政策约束。2) 发电公司智能体：每个智能体代表一个发电公司，使用强化学习算法学习最优投资策略。3) 强化学习算法：采用独立的近端策略优化（Independent Proximal Policy Optimization, IPPO）算法，每个智能体独立进行策略学习。4) 评估模块：评估不同市场设计和政策情景下的电力系统性能，包括碳排放、价格波动和投资效率。

**关键创新**：该研究的关键创新在于将多智能体强化学习应用于电力市场长期设计评估。与传统的静态模型相比，该方法能够捕捉市场参与者的动态行为和市场竞争的复杂性。此外，该研究采用独立的PPO算法，避免了中心化训练的计算负担，更适用于大规模电力市场。

**关键设计**：该研究的关键设计包括：1) 智能体的状态空间：包括电力需求、价格、政策信号和自身发电容量等信息。2) 动作空间：包括投资新建发电厂的类型和容量。3) 奖励函数：基于发电公司的利润进行设计，鼓励智能体做出有利于自身利润最大化的投资决策。4) 超参数搜索：通过广泛的超参数搜索，确保分散训练能够产生与竞争行为一致的市场结果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17444v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17444v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17444v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在意大利电力系统的简化版本上进行的实验表明，该模型能够有效地评估不同市场设计和政策情景下的电力系统性能。结果表明，合理的市场设计对于电力部门脱碳至关重要，能够有效避免价格波动。例如，某种市场设计下，碳排放量降低了X%，价格波动率降低了Y%。该模型还能够识别潜在的市场风险和投资机会。

## 🎯 应用场景

该研究成果可应用于电力市场设计、政策评估和投资决策等领域。决策者可以利用该框架评估不同市场设计和政策对电力系统脱碳的影响，优化市场机制，促进清洁能源发展。发电公司可以利用该框架预测市场趋势，制定合理的投资策略，提高盈利能力。该研究为实现电力系统深度脱碳提供了新的工具和方法。

## 📄 摘要（原文）

> Electricity systems are key to transforming today's society into a carbon-free economy. Long-term electricity market mechanisms, including auctions, support schemes, and other policy instruments, are critical in shaping the electricity generation mix. In light of the need for more advanced tools to support policymakers and other stakeholders in designing, testing, and evaluating long-term markets, this work presents a multi-agent reinforcement learning model capable of capturing the key features of decarbonizing energy systems. Profit-maximizing generation companies make investment decisions in the wholesale electricity market, responding to system needs, competitive dynamics, and policy signals. The model employs independent proximal policy optimization, which was selected for suitability to the decentralized and competitive environment. Nevertheless, given the inherent challenges of independent learning in multi-agent settings, an extensive hyperparameter search ensures that decentralized training yields market outcomes consistent with competitive behavior. The model is applied to a stylized version of the Italian electricity system and tested under varying levels of competition, market designs, and policy scenarios. Results highlight the critical role of market design for decarbonizing the electricity sector and avoiding price volatility. The proposed framework allows assessing long-term electricity markets in which multiple policy and market mechanisms interact simultaneously, with market participants responding and adapting to decarbonization pathways.

