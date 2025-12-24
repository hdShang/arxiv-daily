---
layout: default
title: "BadLingual: A Novel Lingual-Backdoor Attack against Large Language Models"
---

# BadLingual: A Novel Lingual-Backdoor Attack against Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03501" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03501v1</a>
  <a href="https://arxiv.org/pdf/2505.03501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03501v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03501v1', 'BadLingual: A Novel Lingual-Backdoor Attack against Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Wang, Hongwei Li, Rui Zhang, Wenbo Jiang, Kangjie Chen, Tianwei Zhang, Qingchuan Zhao, Guowen Xu

**分类**: cs.CR, cs.CL

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出BadLingual以解决大语言模型的语言后门攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言后门攻击` `大语言模型` `对抗训练` `任务无关` `网络安全` `模型鲁棒性`

## 📋 核心要点

1. 现有的基线语言后门攻击在任务泛化能力上表现不佳，难以适应实际应用场景。
2. 论文提出的BadLingual是一种任务无关的语言后门攻击，能够在多种下游任务中有效触发。
3. 实验结果显示，BadLingual在任务无关场景下的攻击成功率（ASR）相比基线提升了37.35%。

## 📝 摘要（中文）

本文提出了一种新型的针对大语言模型的后门攻击形式：语言后门攻击。其创新之处在于语言本身作为触发器，劫持感染的大语言模型生成煽动性言论。这种攻击能够精准针对特定语言群体，助长恶意实体的种族歧视。我们首先实现了一个基线语言后门攻击，通过将特定下游任务的训练数据翻译为触发语言进行数据污染。然而，该基线攻击在任务泛化能力上表现不佳，且在实际应用中不够实用。为了解决这一挑战，我们设计了BadLingual，一种新型的任务无关语言后门，能够在聊天型大语言模型中触发任何下游任务。我们采用PPL约束的贪婪坐标梯度搜索（PGCG）进行对抗训练，扩展语言后门的决策边界，从而增强其在各种任务中的泛化能力。实验结果表明，基线攻击在特定任务上的ASR超过90%，而在任务无关场景下仅为37.61%。相比之下，BadLingual在基线之上提升了37.35%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语言后门攻击在任务泛化能力不足的问题。基线方法在实际应用中表现不佳，无法有效适应多样化的下游任务场景。

**核心思路**：BadLingual的核心思路是设计一种任务无关的语言后门攻击，通过对抗训练扩展决策边界，使其能够在不同任务中均能有效触发。

**技术框架**：整体架构包括数据污染模块、对抗训练模块和决策边界扩展模块。数据污染模块负责将训练数据翻译为触发语言，对抗训练模块使用PPL约束的贪婪坐标梯度搜索进行优化。

**关键创新**：最重要的技术创新在于提出了PGCG方法，该方法通过对抗训练增强了语言后门的泛化能力，使其能够在多种下游任务中有效触发，克服了基线方法的局限性。

**关键设计**：在设计中，采用了PPL约束来优化训练过程，确保生成的触发语言在多样性和有效性之间取得平衡，同时对抗训练的损失函数设计也考虑了任务无关性。

## 📊 实验亮点

实验结果显示，基线攻击在特定任务上的攻击成功率（ASR）超过90%，而在任务无关场景下仅为37.61%。BadLingual在此基础上提升了37.35%，显示出显著的效果改进，验证了其在多任务环境中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、社交媒体监控和内容生成等。通过揭示大语言模型的脆弱性，研究可以促进未来防御机制的开发，从而增强模型的鲁棒性，减少恶意攻击的风险。

## 📄 摘要（原文）

> In this paper, we present a new form of backdoor attack against Large Language Models (LLMs): lingual-backdoor attacks. The key novelty of lingual-backdoor attacks is that the language itself serves as the trigger to hijack the infected LLMs to generate inflammatory speech. They enable the precise targeting of a specific language-speaking group, exacerbating racial discrimination by malicious entities. We first implement a baseline lingual-backdoor attack, which is carried out by poisoning a set of training data for specific downstream tasks through translation into the trigger language. However, this baseline attack suffers from poor task generalization and is impractical in real-world settings. To address this challenge, we design BadLingual, a novel task-agnostic lingual-backdoor, capable of triggering any downstream tasks within the chat LLMs, regardless of the specific questions of these tasks. We design a new approach using PPL-constrained Greedy Coordinate Gradient-based Search (PGCG) based adversarial training to expand the decision boundary of lingual-backdoor, thereby enhancing the generalization ability of lingual-backdoor across various tasks. We perform extensive experiments to validate the effectiveness of our proposed attacks. Specifically, the baseline attack achieves an ASR of over 90% on the specified tasks. However, its ASR reaches only 37.61% across six tasks in the task-agnostic scenario. In contrast, BadLingual brings up to 37.35% improvement over the baseline. Our study sheds light on a new perspective of vulnerabilities in LLMs with multilingual capabilities and is expected to promote future research on the potential defenses to enhance the LLMs' robustness

