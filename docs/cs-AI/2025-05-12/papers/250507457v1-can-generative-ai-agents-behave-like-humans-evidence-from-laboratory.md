---
layout: default
title: Can Generative AI agents behave like humans? Evidence from laboratory market experiments
---

# Can Generative AI agents behave like humans? Evidence from laboratory market experiments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07457" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07457v1</a>
  <a href="https://arxiv.org/pdf/2505.07457.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07457v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07457v1', 'Can Generative AI agents behave like humans? Evidence from laboratory market experiments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: R. Maria del Rio-Chanona, Marco Pangallo, Cars Hommes

**分类**: econ.GN, cs.AI

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**探讨大型语言模型在经济市场实验中模拟人类行为的潜力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `经济市场` `人类行为模拟` `动态反馈` `有限理性` `实验研究` `市场预测`

## 📋 核心要点

1. 现有研究未能充分考虑LLM代理之间的动态反馈，导致对市场行为的模拟不足。
2. 论文提出通过动态反馈机制和有限记忆窗口来增强LLM的决策能力，以更好地模拟人类行为。
3. 实验结果表明，LLMs在捕捉市场趋势方面表现良好，但在行为异质性上仍存在不足。

## 📝 摘要（中文）

本研究探讨了大型语言模型（LLMs）在经济市场实验中复制人类行为的潜力。与以往研究不同，我们关注LLM代理之间的动态反馈：每个LLM的决策影响当前市场价格，并在下一步影响其他LLM的决策。研究发现，LLMs并不严格遵循理性预期，而是表现出有限理性，类似于人类参与者。通过提供最小的上下文窗口（即记忆前三个时间步），结合高变异性设置，LLMs能够复制人类实验中的广泛趋势，如正负反馈市场的区别。然而，在细节层面上，LLMs的行为异质性低于人类。这些结果表明，LLMs作为模拟经济背景下人类行为的工具具有潜力，但仍需进一步研究以提高其准确性和行为多样性。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在经济市场实验中模拟人类行为的不足，尤其是缺乏动态反馈机制和行为异质性的问题。

**核心思路**：通过引入LLM代理之间的动态反馈机制，使得每个LLM的决策不仅影响当前市场价格，还影响后续决策，从而更真实地模拟人类参与者的行为。

**技术框架**：整体架构包括LLM代理的决策模块、市场价格更新模块和反馈机制模块。每个模块协同工作，形成一个动态的市场环境。

**关键创新**：论文的主要创新在于引入动态反馈机制和有限的上下文窗口，使得LLMs能够在一定程度上模拟人类的有限理性和市场反馈效应，这与传统的静态模型有本质区别。

**关键设计**：设置了最小的上下文窗口（记忆前三个时间步），并在高变异性环境中进行实验，以捕捉参与者的响应异质性。

## 📊 实验亮点

实验结果显示，LLMs能够有效模拟人类在市场中的行为趋势，尤其是在正负反馈市场的区分上表现突出。然而，LLMs在行为异质性方面的表现低于人类，提示未来研究需关注提高其行为多样性。

## 🎯 应用场景

该研究的潜在应用领域包括经济学、市场预测和决策支持系统。通过模拟人类行为，LLMs可以帮助经济学家和决策者更好地理解市场动态，从而优化策略和政策制定。未来，随着技术的不断完善，LLMs在经济领域的应用将更加广泛。

## 📄 摘要（原文）

> We explore the potential of Large Language Models (LLMs) to replicate human behavior in economic market experiments. Compared to previous studies, we focus on dynamic feedback between LLM agents: the decisions of each LLM impact the market price at the current step, and so affect the decisions of the other LLMs at the next step. We compare LLM behavior to market dynamics observed in laboratory settings and assess their alignment with human participants' behavior. Our findings indicate that LLMs do not adhere strictly to rational expectations, displaying instead bounded rationality, similarly to human participants. Providing a minimal context window i.e. memory of three previous time steps, combined with a high variability setting capturing response heterogeneity, allows LLMs to replicate broad trends seen in human experiments, such as the distinction between positive and negative feedback markets. However, differences remain at a granular level--LLMs exhibit less heterogeneity in behavior than humans. These results suggest that LLMs hold promise as tools for simulating realistic human behavior in economic contexts, though further research is needed to refine their accuracy and increase behavioral diversity.

