---
layout: default
title: "Tagging the Thought: Unlocking Personalization Reasoning via Reinforcement Learning"
---

# Tagging the Thought: Unlocking Personalization Reasoning via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23140" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23140v1</a>
  <a href="https://arxiv.org/pdf/2509.23140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23140v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23140v1', 'Tagging the Thought: Unlocking Personalization Reasoning via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Song Jin, Juntian Zhang, Yong Liu, Xun Zhang, Yufei Zhang, Fei Jiang, Guojun Yin, Wei Lin, Rui Yan

**分类**: cs.CL

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**TagPR：通过强化学习和思维标注提升LLM的个性化推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化推理` `大型语言模型` `强化学习` `思维标注` `用户偏好` `奖励模型` `监督微调`

## 📋 核心要点

1. 现有LLM在通用推理方面表现出色，但在分析用户历史、推断偏好并生成定制化响应的个性化推理方面存在不足。
2. TagPR框架通过数据驱动的推理链生成与标注，以及结合监督微调和强化学习的协同训练策略，提升LLM的个性化推理能力。
3. 实验结果表明，TagPR在LaMP基准和自建数据集上均取得了SOTA结果，相比基线模型平均提升了32.65%。

## 📝 摘要（中文）

本文提出了一种名为TagPR的训练框架，旨在显著提升大型语言模型（LLM）在个性化推理方面的能力。该框架通过“标注思维”的方法，首先开发一个数据驱动的流程，自动生成并语义标注推理链，从而创建一个结构化的数据集，促进可解释的推理。然后，提出一种协同训练策略，首先在此标注数据上进行监督微调（SFT），以建立基本的推理模式，然后进行多阶段强化学习（RL）过程。此RL阶段由独特的复合奖励信号引导，该信号集成了基于标签的约束和一个新颖的带有用户嵌入的个性化奖励模型（PRMU），以实现与用户特定逻辑的细粒度对齐。在公共LaMP基准和一个自构建数据集上的大量实验表明，该方法实现了最先进的结果，在所有任务中，相对于基础模型平均提高了32.65%。这项工作验证了结构化、可解释的推理是释放LLM中真正个性化能力的一种非常有效的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在个性化推理方面的不足。现有LLM虽然具备强大的通用推理能力，但在理解用户特定偏好、并根据这些偏好生成定制化响应方面表现欠佳。现有的方法难以有效地利用用户历史信息，缺乏对推理过程的细粒度控制和可解释性。

**核心思路**：论文的核心思路是通过“标注思维”（Tagging the Thought）的方式，显式地建模和指导LLM的推理过程。具体来说，首先构建结构化的推理链数据，并对每个推理步骤进行语义标注，然后利用这些标注信息来训练LLM，使其能够更好地理解和利用用户偏好。通过强化学习，进一步优化LLM的推理策略，使其能够生成更符合用户需求的个性化响应。

**技术框架**：TagPR框架包含以下几个主要阶段：1) **数据生成与标注**：利用数据驱动的流程自动生成推理链，并进行语义标注。2) **监督微调（SFT）**：在标注数据上对LLM进行微调，使其学习基本的推理模式。3) **多阶段强化学习（RL）**：利用复合奖励信号，对LLM进行进一步的优化，使其能够更好地适应用户特定偏好。复合奖励信号包括基于标签的约束和个性化奖励模型（PRMU）。

**关键创新**：论文的关键创新在于：1) **“标注思维”方法**：通过显式地标注推理链，提高了LLM推理过程的可解释性和可控性。2) **复合奖励信号**：结合了基于标签的约束和个性化奖励模型，实现了对LLM推理策略的细粒度优化。3) **个性化奖励模型（PRMU）**：利用用户嵌入来建模用户特定偏好，从而更准确地评估LLM生成的响应的质量。

**关键设计**：在强化学习阶段，论文设计了一个复合奖励函数，该函数由两部分组成：基于标签的约束和个性化奖励模型（PRMU）。基于标签的约束用于确保LLM生成的推理链符合预定义的语义规则。PRMU则利用用户嵌入来预测用户对LLM生成的响应的偏好。用户嵌入可以通过用户历史行为数据学习得到。损失函数的设计旨在最大化复合奖励，从而优化LLM的推理策略。

## 📊 实验亮点

实验结果表明，TagPR在LaMP基准测试和自建数据集上均取得了显著的性能提升。在所有任务中，TagPR相对于基线模型平均提高了32.65%。此外，消融实验验证了各个模块的有效性，例如，基于标签的约束和个性化奖励模型（PRMU）都对最终性能有重要贡献。

## 🎯 应用场景

该研究成果可应用于个性化推荐系统、智能对话系统、以及其他需要理解用户偏好并生成定制化内容的场景。通过提升LLM的个性化推理能力，可以显著改善用户体验，提高系统的效率和准确性。未来，该方法可以进一步扩展到其他领域，例如医疗诊断、金融风控等。

## 📄 摘要（原文）

> Recent advancements have endowed Large Language Models (LLMs) with impressive general reasoning capabilities, yet they often struggle with personalization reasoning - the crucial ability to analyze user history, infer unique preferences, and generate tailored responses. To address this limitation, we introduce TagPR, a novel training framework that significantly enhances an LLM's intrinsic capacity for personalization reasoning through a tagging the thought approach. Our method first develops a data-driven pipeline to automatically generate and semantically label reasoning chains, creating a structured dataset that fosters interpretable reasoning. We then propose a synergistic training strategy that begins with Supervised Fine-Tuning (SFT) on this tagged data to establish foundational reasoning patterns, followed by a multi-stage reinforcement learning (RL) process. This RL phase is guided by a unique composite reward signal, which integrates tag-based constraints and a novel Personalization Reward Model with User Embeddings (PRMU) to achieve fine-grained alignment with user-specific logic. Extensive experiments on the public LaMP benchmark and a self-constructed dataset demonstrate that our approach achieves state-of-the-art results, delivering an average improvement of 32.65% over the base model across all tasks. Our work validates that structured, interpretable reasoning is a highly effective pathway to unlocking genuine personalization capabilities in LLMs.

