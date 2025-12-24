---
layout: default
title: Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents
---

# Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14418" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14418v2</a>
  <a href="https://arxiv.org/pdf/2505.14418.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14418v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14418v2', 'Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengzhou Cheng, Haowen Hu, Zheng Wu, Zongru Wu, Tianjie Ju, Zhuosheng Zhang, Gongshen Liu

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-23)

**备注**: 25 pages, 10 figures, 12 Tables

---

## 💡 一句话要点

**提出AgentGhost以解决MLLM驱动的GUI代理后门攻击问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门攻击` `多模态大型语言模型` `图形用户界面` `安全性评估` `监督对比学习`

## 📋 核心要点

1. 现有的MLLM驱动GUI代理在安全性方面存在严重的后门攻击风险，尤其是依赖开源解决方案时。
2. 提出AgentGhost框架，通过构建复合触发器和最小-最大优化问题，有效实现后门攻击，同时保持任务效用。
3. 在两个移动基准测试中，AgentGhost在三项攻击目标上达到了99.7%的攻击准确率，且仅有1%的效用下降，显示出良好的隐蔽性。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）驱动的图形用户界面（GUI）代理在与人类交互中展现出更大的潜力。然而，由于高昂的微调成本，用户往往依赖开源的GUI代理或AI提供商的API，这引入了一种关键但尚未充分探讨的供应链威胁：后门攻击。本文首次揭示了MLLM驱动的GUI代理自然暴露出多种交互级触发器。基于这一观察，我们提出了AgentGhost，一个有效且隐蔽的后门攻击框架。通过构建复合触发器并将后门注入形式化为最小-最大优化问题，我们显著提高了后门的灵活性和有效性。实验结果表明，AgentGhost在多个代理模型上表现出99.7%的攻击准确率，且仅有1%的效用下降。

## 🔬 方法详解

**问题定义**：本文旨在解决MLLM驱动的GUI代理中存在的后门攻击问题。现有方法在安全性方面存在不足，尤其是依赖开源解决方案时，容易受到供应链攻击的威胁。

**核心思路**：我们提出AgentGhost框架，利用复合触发器的构建和最小-最大优化，将后门注入过程形式化，以提高后门的灵活性和有效性，同时确保任务的实用性。

**技术框架**：AgentGhost的整体架构包括两个主要模块：复合触发器构建模块和后门注入优化模块。复合触发器通过结合目标和交互级别来设计，后门注入则通过监督对比学习和监督微调来实现。

**关键创新**：最重要的技术创新在于将后门注入问题转化为最小-最大优化问题，并通过监督对比学习最大化样本类别间的特征差异。这一方法显著提升了后门的灵活性和隐蔽性。

**关键设计**：在参数设置上，采用了监督对比学习的损失函数，以确保不同类别之间的特征差异最大化。同时，使用监督微调来最小化后门行为与正常行为之间的差异，从而提高了后门的有效性和实用性。

## 📊 实验亮点

实验结果显示，AgentGhost在三项攻击目标上达到了99.7%的攻击准确率，且仅有1%的效用下降，表现出极高的隐蔽性。此外，针对AgentGhost的防御方法将攻击准确率降低至22.1%，显示出良好的防御效果。

## 🎯 应用场景

该研究的潜在应用领域包括移动应用程序的安全性评估和AI驱动的用户界面设计。通过识别和防御后门攻击，开发者可以增强其应用的安全性，保护用户数据和隐私。未来，该研究可能推动更安全的AI代理开发和更严格的供应链安全标准。

## 📄 摘要（原文）

> Graphical user interface (GUI) agents powered by multimodal large language models (MLLMs) have shown greater promise for human-interaction. However, due to the high fine-tuning cost, users often rely on open-source GUI agents or APIs offered by AI providers, which introduces a critical but underexplored supply chain threat: backdoor attacks. In this work, we first unveil that MLLM-powered GUI agents naturally expose multiple interaction-level triggers, such as historical steps, environment states, and task progress. Based on this observation, we introduce AgentGhost, an effective and stealthy framework for red-teaming backdoor attacks. Specifically, we first construct composite triggers by combining goal and interaction levels, allowing GUI agents to unintentionally activate backdoors while ensuring task utility. Then, we formulate backdoor injection as a Min-Max optimization problem that uses supervised contrastive learning to maximize the feature difference across sample classes at the representation space, improving flexibility of the backdoor. Meanwhile, it adopts supervised fine-tuning to minimize the discrepancy between backdoor and clean behavior generation, enhancing effectiveness and utility. Extensive evaluations of various agent models in two established mobile benchmarks show that AgentGhost is effective and generic, with attack accuracy that reaches 99.7\% on three attack objectives, and shows stealthiness with only 1\% utility degradation. Furthermore, we tailor a defense method against AgentGhost that reduces the attack accuracy to 22.1\%. Our code is available at \texttt{anonymous}.

