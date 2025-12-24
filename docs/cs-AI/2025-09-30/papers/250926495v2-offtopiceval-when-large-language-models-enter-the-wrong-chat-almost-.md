---
layout: default
title: "OffTopicEval: When Large Language Models Enter the Wrong Chat, Almost Always!"
---

# OffTopicEval: When Large Language Models Enter the Wrong Chat, Almost Always!

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26495" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26495v2</a>
  <a href="https://arxiv.org/pdf/2509.26495.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26495v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26495v2', 'OffTopicEval: When Large Language Models Enter the Wrong Chat, Almost Always!')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingdi Lei, Varun Gumma, Rishabh Bhardwaj, Seok Min Lim, Chuan Li, Amir Zadeh, Soujanya Poria

**分类**: cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-03)

---

## 💡 一句话要点

**OffTopicEval：评估大语言模型在错误场景下的安全性，揭示其泛化能力不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `操作安全性` `提示工程` `Out-of-Distribution检测` `LLM安全` `模型对齐` `OffTopicEval`

## 📋 核心要点

1. 现有LLM安全性研究主要关注通用危害，忽略了企业应用中LLM在特定任务下的操作安全性问题。
2. 论文提出OffTopicEval评估套件，用于衡量LLM在特定任务中接受或拒绝用户查询的操作安全性。
3. 实验表明现有LLM在操作安全性方面表现不佳，并提出Q-ground和P-ground两种prompt方法显著提升OOD拒绝能力。

## 📝 摘要（中文）

大型语言模型（LLM）的安全性是实现大规模部署面临的最紧迫挑战之一。虽然大多数研究和全球讨论都集中在通用危害上，例如模型协助用户伤害自己或他人，但企业面临着一个更根本的问题：基于LLM的代理对于其预期用例是否安全。为了解决这个问题，我们引入了操作安全性，定义为LLM在执行特定任务时适当接受或拒绝用户查询的能力。我们进一步提出了OffTopicEval，这是一个评估套件和基准，用于衡量一般和特定代理用例中的操作安全性。我们对包含20个开放权重LLM的六个模型系列的评估表明，虽然性能因模型而异，但所有模型仍然在操作上高度不安全。即使是最强大的模型，Qwen-3 (235B) 的77.77%和Mistral (24B) 的79.96%，也远未达到可靠的操作安全性，而GPT模型的性能稳定在62-73%的范围内，Phi仅达到中等水平的分数（48-70%），Gemma和Llama-3分别崩溃至39.53%和23.84%。虽然操作安全性是一个核心模型对齐问题，但为了抑制这些失败，我们提出了基于提示的引导方法：查询 grounding (Q-ground) 和系统提示 grounding (P-ground)，它们显着提高了OOD拒绝能力。Q-ground提供了高达23%的持续增益，而P-ground提供了更大的提升，将Llama-3.3 (70B) 提高了41%，将Qwen-3 (30B) 提高了27%。这些结果突出了对操作安全性干预的迫切需求，以及基于提示的引导作为迈向更可靠的基于LLM的代理的第一步的前景。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在特定应用场景下的操作安全性问题。现有方法主要关注通用安全问题，如生成有害内容，而忽略了LLM在特定任务中是否能正确判断用户查询是否相关，并拒绝处理无关查询。现有方法缺乏针对操作安全性的有效评估和干预手段。

**核心思路**：论文的核心思路是通过构建OffTopicEval评估套件，系统性地评估LLM在特定任务下的操作安全性。同时，提出基于提示的引导方法（Q-ground和P-ground）来提高LLM拒绝处理无关查询的能力。这种思路旨在提高LLM在实际应用中的可靠性和安全性。

**技术框架**：OffTopicEval评估套件包含一系列与特定任务相关的查询，其中既包含与任务相关的查询，也包含与任务无关的查询。LLM需要判断每个查询是否与任务相关，并决定是否处理该查询。论文还提出了两种基于提示的引导方法：Q-ground通过在查询中加入任务相关的上下文信息，引导LLM更好地理解查询意图；P-ground通过修改系统提示，明确告知LLM拒绝处理无关查询。

**关键创新**：论文的关键创新在于提出了操作安全性的概念，并构建了相应的评估套件OffTopicEval。此外，论文提出的基于提示的引导方法（Q-ground和P-ground）是一种简单有效的提高LLM操作安全性的方法，无需修改模型结构或训练数据。

**关键设计**：Q-ground的关键设计是在用户查询中加入任务相关的上下文信息，例如：“As an agent for [task description], answer this question: [user query]”。P-ground的关键设计是修改系统提示，明确告知LLM拒绝处理无关查询，例如：“You are an agent for [task description]. If a question is not about [task description], say you cannot answer.”

## 📊 实验亮点

实验结果表明，现有LLM在OffTopicEval评估套件上的表现不佳，操作安全性有待提高。Q-ground和P-ground两种prompt方法能够显著提高LLM的OOD拒绝能力，其中P-ground的效果更为显著，将Llama-3.3 (70B) 的性能提高了41%，将Qwen-3 (30B) 的性能提高了27%。

## 🎯 应用场景

该研究成果可应用于各种企业级LLM应用场景，例如智能客服、金融分析、医疗诊断等。通过提高LLM的操作安全性，可以降低LLM在实际应用中出错的风险，提高用户体验，并增强用户对LLM的信任。未来，该研究可以进一步扩展到更复杂的任务和场景，并探索更有效的操作安全性干预方法。

## 📄 摘要（原文）

> Large Language Model (LLM) safety is one of the most pressing challenges for enabling wide-scale deployment. While most studies and global discussions focus on generic harms, such as models assisting users in harming themselves or others, enterprises face a more fundamental concern: whether LLM-based agents are safe for their intended use case. To address this, we introduce operational safety, defined as an LLM's ability to appropriately accept or refuse user queries when tasked with a specific purpose. We further propose OffTopicEval, an evaluation suite and benchmark for measuring operational safety both in general and within specific agentic use cases. Our evaluations on six model families comprising 20 open-weight LLMs reveal that while performance varies across models, all of them remain highly operationally unsafe. Even the strongest models - Qwen-3 (235B) with 77.77% and Mistral (24B) with 79.96% - fall far short of reliable operational safety, while GPT models plateau in the 62-73% range, Phi achieves only mid-level scores (48-70%), and Gemma and Llama-3 collapse to 39.53% and 23.84%, respectively. While operational safety is a core model alignment issue, to suppress these failures, we propose prompt-based steering methods: query grounding (Q-ground) and system-prompt grounding (P-ground), which substantially improve OOD refusal. Q-ground provides consistent gains of up to 23%, while P-ground delivers even larger boosts, raising Llama-3.3 (70B) by 41% and Qwen-3 (30B) by 27%. These results highlight both the urgent need for operational safety interventions and the promise of prompt-based steering as a first step toward more reliable LLM-based agents.

