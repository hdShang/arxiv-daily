---
layout: default
title: "Persuasiveness and Bias in LLM: Investigating the Impact of Persuasiveness and Reinforcement of Bias in Language Models"
---

# Persuasiveness and Bias in LLM: Investigating the Impact of Persuasiveness and Reinforcement of Bias in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15798" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15798v1</a>
  <a href="https://arxiv.org/pdf/2508.15798.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15798v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15798v1', 'Persuasiveness and Bias in LLM: Investigating the Impact of Persuasiveness and Reinforcement of Bias in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saumya Roy

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出说服力与偏见强化框架以评估大型语言模型的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `说服力` `偏见强化` `社会影响` `AI安全`

## 📋 核心要点

1. 现有大型语言模型在生成文本时可能传播错误信息和社会偏见，导致潜在的滥用风险。
2. 论文提出了说服者-怀疑者框架，通过模拟角色来评估模型的说服力和偏见强化效果。
3. 实验结果表明，LLMs能够有效塑造叙事，但也可能无意中强化偏见，需加强监管和政策支持。

## 📝 摘要（中文）

本研究探讨了人工智能在说服力和偏见放大方面的潜在滥用，所有实验均用于安全评估。大型语言模型（LLMs）能够生成令人信服的人类文本，广泛应用于内容创作、决策支持和用户互动。然而，这些系统也可能在大规模传播信息或错误信息，并反映出数据、架构或训练选择所导致的社会偏见。本文研究了说服力与偏见在LLMs中的相互作用，重点关注不完美或偏颇的输出如何影响说服效果。我们引入了一个说服者-怀疑者框架，通过模拟真实态度的角色来进行实验，比较怀疑者在接触说服者模型的论点前后的信念变化。研究结果显示，LLMs在塑造叙事和适应语气方面具有潜力，但同样的能力也可能被滥用以自动化错误信息传播，强化刻板印象并扩大不平等。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在说服力和偏见放大方面的影响，现有方法未能充分评估这些模型在传播信息时的潜在风险和偏见。

**核心思路**：通过引入说服者-怀疑者框架，模拟不同角色的信念变化，量化说服力和偏见强化的程度，以评估LLMs的影响。

**技术框架**：研究包括两个主要模块：说服者模型和怀疑者模型。说服者模型生成论点，怀疑者模型作为人类代理，比较其信念变化。使用Jensen-Shannon散度量化说服效果。

**关键创新**：本研究的核心创新在于通过角色模拟来评估说服力和偏见强化，提供了一种新的视角来理解LLMs的社会影响，与传统方法相比，更加注重模型输出的社会后果。

**关键设计**：在实验中使用了对比模型和附加的对抗性提示，以探测偏见的存在，设计了特定的参数设置和损失函数来优化说服力的评估过程。实验中还考虑了种族、性别和宗教等多维度的偏见分析。

## 📊 实验亮点

实验结果显示，LLMs在说服力方面表现出显著的能力，能够有效影响怀疑者的信念变化。通过Jensen-Shannon散度量化，发现强说服者在偏见强化方面的影响力显著，提示了潜在的社会风险。

## 🎯 应用场景

该研究的潜在应用领域包括心理学、市场营销和法律援助等，能够帮助设计更具价值敏感性的AI系统，减少偏见传播的风险。未来，研究成果可为政策制定提供依据，促进可信赖的AI部署。

## 📄 摘要（原文）

> Warning: This research studies AI persuasion and bias amplification that could be misused; all experiments are for safety evaluation. Large Language Models (LLMs) now generate convincing, human-like text and are widely used in content creation, decision support, and user interactions. Yet the same systems can spread information or misinformation at scale and reflect social biases that arise from data, architecture, or training choices. This work examines how persuasion and bias interact in LLMs, focusing on how imperfect or skewed outputs affect persuasive impact. Specifically, we test whether persona-based models can persuade with fact-based claims while also, unintentionally, promoting misinformation or biased narratives.
>   We introduce a convincer-skeptic framework: LLMs adopt personas to simulate realistic attitudes. Skeptic models serve as human proxies; we compare their beliefs before and after exposure to arguments from convincer models. Persuasion is quantified with Jensen-Shannon divergence over belief distributions. We then ask how much persuaded entities go on to reinforce and amplify biased beliefs across race, gender, and religion. Strong persuaders are further probed for bias using sycophantic adversarial prompts and judged with additional models.
>   Our findings show both promise and risk. LLMs can shape narratives, adapt tone, and mirror audience values across domains such as psychology, marketing, and legal assistance. But the same capacity can be weaponized to automate misinformation or craft messages that exploit cognitive biases, reinforcing stereotypes and widening inequities. The core danger lies in misuse more than in occasional model mistakes. By measuring persuasive power and bias reinforcement, we argue for guardrails and policies that penalize deceptive use and support alignment, value-sensitive design, and trustworthy deployment.

