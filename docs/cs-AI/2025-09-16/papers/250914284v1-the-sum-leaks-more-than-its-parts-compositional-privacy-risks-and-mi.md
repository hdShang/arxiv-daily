---
layout: default
title: "The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration"
---

# The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14284" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14284v1</a>
  <a href="https://arxiv.org/pdf/2509.14284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14284v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14284v1', 'The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vaidehi Patil, Elias Stengel-Eskin, Mohit Bansal

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-09-16

**备注**: Code: https://github.com/Vaidehi99/MultiAgentPrivacy

---

## 💡 一句话要点

**揭示多智能体协作中组合隐私泄露风险，并提出ToM和CoDef防御机制。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `隐私泄露` `大型语言模型` `心智理论` `协作防御` `组合隐私` `隐私保护`

## 📋 核心要点

1. 现有方法难以应对多智能体系统中，交互组合带来的隐私泄露风险，单轮评估无法有效识别。
2. 提出心智理论防御（ToM）和协作共识防御（CoDef），分别从个体推理和群体协作角度防御。
3. 实验表明，ToM可显著提高敏感查询阻止率，CoDef在隐私保护和任务成功率之间取得最佳平衡。

## 📝 摘要（中文）

随着大型语言模型（LLM）在多智能体系统中变得不可或缺，新的隐私风险开始出现，这些风险超越了记忆、直接推理或单轮评估。特别地，看似无害的响应在交互中组合起来时，会累积地使攻击者能够恢复敏感信息，我们称之为组合隐私泄露。我们首次系统地研究了多智能体LLM系统中这种组合隐私泄露以及可能的缓解方法。首先，我们开发了一个框架，该框架模拟了辅助知识和智能体交互如何共同放大隐私风险，即使每个响应本身是良性的。接下来，为了缓解这种情况，我们提出并评估了两种防御策略：（1）心智理论防御（ToM），防御者智能体通过预测其输出可能被攻击者利用的方式来推断提问者的意图；（2）协作共识防御（CoDef），响应者智能体与基于共享聚合状态进行投票的同伴协作，以限制敏感信息的传播。至关重要的是，我们在暴露敏感信息的组合和产生良性推论的组合之间平衡了我们的评估。我们的实验量化了这些防御策略在平衡隐私-效用权衡方面的差异。我们发现，仅凭思维链（Chain-of-Thought）对泄露的保护有限（~39%的敏感信息阻止率），而我们的ToM防御显着提高了敏感查询阻止率（高达97%），但可能会降低良性任务的成功率。CoDef实现了最佳平衡，产生了最高的平衡结果（79.8%），突出了将显式推理与防御者协作相结合的好处。总之，我们的结果揭示了协作LLM部署中的一类新风险，并为设计针对组合的、上下文驱动的隐私泄露的保护措施提供了可操作的见解。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统中，由于大型语言模型（LLM）的交互组合而产生的隐私泄露问题。现有方法主要关注单轮交互的隐私保护，忽略了多轮交互中信息累积带来的风险。攻击者可以通过组合看似无害的响应，推断出敏感信息，这给隐私保护带来了新的挑战。

**核心思路**：论文的核心思路是设计防御机制，使智能体能够意识到自身行为可能导致的隐私泄露，并采取措施进行缓解。具体而言，论文提出了两种防御策略：心智理论防御（ToM）和协作共识防御（CoDef）。ToM使智能体能够推断提问者的意图，预测其输出可能被利用的方式，从而避免泄露敏感信息。CoDef则通过智能体之间的协作，共同评估响应的安全性，限制敏感信息的传播。

**技术框架**：论文构建了一个多智能体交互框架，其中包含提问者和响应者。提问者向响应者提出问题，响应者根据问题生成回答。攻击者通过观察提问者和响应者的交互，试图推断出敏感信息。论文提出的防御机制主要作用于响应者。ToM防御通过在响应者中引入一个心智模型，使其能够预测提问者的意图。CoDef防御则通过在响应者之间建立协作机制，共同评估响应的安全性。

**关键创新**：论文的关键创新在于首次系统地研究了多智能体LLM系统中组合隐私泄露问题，并提出了两种有效的防御策略。ToM防御通过引入心智模型，使智能体能够进行隐私感知的推理。CoDef防御则通过智能体之间的协作，提高了隐私保护的鲁棒性。与现有方法相比，论文提出的方法能够更好地应对多轮交互中信息累积带来的隐私风险。

**关键设计**：ToM防御的关键设计在于心智模型的构建。论文使用LLM来模拟提问者的意图，并根据心智模型的预测结果，调整响应者的输出。CoDef防御的关键设计在于协作机制的建立。论文使用投票机制来评估响应的安全性，并根据投票结果决定是否发送响应。具体参数设置和损失函数等技术细节在论文中有详细描述，此处不再赘述。

## 📊 实验亮点

实验结果表明，仅使用思维链（Chain-of-Thought）的敏感信息阻止率约为39%，而ToM防御可将阻止率提高到97%。CoDef防御在隐私保护和任务成功率之间取得了最佳平衡，实现了79.8%的平衡结果。这些结果表明，论文提出的防御策略能够有效缓解多智能体系统中的组合隐私泄露风险。

## 🎯 应用场景

该研究成果可应用于各种多智能体协作场景，例如医疗诊断、金融分析、法律咨询等。通过部署相应的防御机制，可以有效保护用户隐私，防止敏感信息泄露。此外，该研究也为设计更安全的LLM应用提供了新的思路，有助于推动人工智能技术的健康发展。

## 📄 摘要（原文）

> As large language models (LLMs) become integral to multi-agent systems, new privacy risks emerge that extend beyond memorization, direct inference, or single-turn evaluations. In particular, seemingly innocuous responses, when composed across interactions, can cumulatively enable adversaries to recover sensitive information, a phenomenon we term compositional privacy leakage. We present the first systematic study of such compositional privacy leaks and possible mitigation methods in multi-agent LLM systems. First, we develop a framework that models how auxiliary knowledge and agent interactions jointly amplify privacy risks, even when each response is benign in isolation. Next, to mitigate this, we propose and evaluate two defense strategies: (1) Theory-of-Mind defense (ToM), where defender agents infer a questioner's intent by anticipating how their outputs may be exploited by adversaries, and (2) Collaborative Consensus Defense (CoDef), where responder agents collaborate with peers who vote based on a shared aggregated state to restrict sensitive information spread. Crucially, we balance our evaluation across compositions that expose sensitive information and compositions that yield benign inferences. Our experiments quantify how these defense strategies differ in balancing the privacy-utility trade-off. We find that while chain-of-thought alone offers limited protection to leakage (~39% sensitive blocking rate), our ToM defense substantially improves sensitive query blocking (up to 97%) but can reduce benign task success. CoDef achieves the best balance, yielding the highest Balanced Outcome (79.8%), highlighting the benefit of combining explicit reasoning with defender collaboration. Together, our results expose a new class of risks in collaborative LLM deployments and provide actionable insights for designing safeguards against compositional, context-driven privacy leakage.

