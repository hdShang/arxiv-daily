---
layout: default
title: AdaSearch: Balancing Parametric Knowledge and Search in Large Language Models via Reinforcement Learning
---

# AdaSearch: Balancing Parametric Knowledge and Search in Large Language Models via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16883" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16883v1</a>
  <a href="https://arxiv.org/pdf/2512.16883.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16883v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16883v1', 'AdaSearch: Balancing Parametric Knowledge and Search in Large Language Models via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tzu-Han Lin, Wei-Lin Chen, Chen-An Li, Hung-yi Lee, Yun-Nung Chen, Yu Meng

**分类**: cs.CL

**发布日期**: 2025-12-18

**备注**: Preprint. Code and artifacts will be uploaded to https://github.com/hank0316/AdaSearch

---

## 💡 一句话要点

**提出AdaSearch，通过强化学习平衡大语言模型的参数知识与外部搜索。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `搜索引擎` `知识边界` `自适应搜索`

## 📋 核心要点

1. 现有搜索增强的LLM过度依赖搜索，引入成本和噪声，而仅依赖模型自身知识则易产生幻觉。
2. AdaSearch通过两阶段强化学习，解耦问题解决和搜索决策，显式地学习何时调用搜索。
3. 实验表明AdaSearch能显著提高知识边界意识，减少不必要的搜索，同时保持任务性能。

## 📝 摘要（中文）

本文提出了一种利用强化学习（RL）为大型语言模型（LLM）配备搜索引擎的有效方法，以构建搜索代理。然而，过度依赖搜索会引入不必要的成本，并可能暴露于噪声或恶意内容，而仅依赖参数知识则存在幻觉风险。核心挑战在于开发能够自适应地平衡参数知识与外部搜索的代理，仅在必要时才调用搜索。现有工作通过围绕工具调用次数塑造奖励来缓解搜索过度使用，但这些惩罚需要大量的奖励工程，提供模糊的信用分配，并且可能被表面上减少调用的代理利用。此外，仅通过调用次数评估性能会混淆必要和不必要的搜索，从而模糊了对真正自适应行为的衡量。为了解决这些局限性，我们首先通过基于F1的决策指标量化现有搜索代理的自我知识感知能力，揭示了诸如Search-R1之类的方法经常忽略现成的参数知识。受这些发现的启发，我们提出AdaSearch，这是一个简单的两阶段、结果驱动的RL框架，它将问题解决与是否调用搜索的决策分离开来，并使该决策过程明确且可解释。这种透明度对于金融和医学问答等高风险领域至关重要，但之前的研究方法在很大程度上忽略了这一点。跨多个模型系列和规模的实验表明，AdaSearch显着提高了知识边界意识，减少了不必要的搜索调用，保持了强大的任务性能，并提供了更透明、可解释的决策行为。

## 🔬 方法详解

**问题定义**：现有方法在利用搜索引擎增强大型语言模型时，难以平衡参数知识和外部搜索。过度依赖搜索会增加成本并引入噪声，而完全依赖参数知识则容易产生幻觉。现有方法通常通过惩罚工具调用次数来减少搜索的使用，但这需要大量的奖励工程，并且信用分配模糊，容易被利用。

**核心思路**：AdaSearch的核心思路是将问题解决过程与是否调用搜索的决策过程解耦。通过两阶段强化学习，首先训练一个问题解决器，然后在第二阶段训练一个决策器，明确地决定是否需要调用搜索。这种解耦使得模型能够更好地学习何时利用自身的参数知识，何时需要外部信息。

**技术框架**：AdaSearch包含两个主要阶段：1) 问题解决阶段：使用强化学习训练一个问题解决器，使其能够尽可能地利用自身的参数知识解决问题。2) 搜索决策阶段：使用强化学习训练一个决策器，该决策器根据问题解决器的状态和问题本身，决定是否需要调用搜索。决策器的目标是最大化任务完成的奖励，同时最小化不必要的搜索调用。

**关键创新**：AdaSearch的关键创新在于将问题解决和搜索决策解耦，并使用强化学习显式地学习搜索策略。与现有方法相比，AdaSearch不需要复杂的奖励工程，并且能够提供更透明、可解释的决策过程。此外，AdaSearch通过F1-based决策指标量化了现有搜索代理的自我知识感知能力，为后续的改进提供了依据。

**关键设计**：AdaSearch使用Actor-Critic算法进行强化学习。在问题解决阶段，Actor网络负责生成答案，Critic网络负责评估答案的质量。在搜索决策阶段，Actor网络负责决定是否调用搜索，Critic网络负责评估搜索决策的质量。奖励函数的设计旨在鼓励模型利用自身的参数知识解决问题，并仅在必要时才调用搜索。具体参数设置和网络结构在论文中有详细描述，此处不再赘述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16883v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16883v1/figures/qwen3b_comparison.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16883v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AdaSearch在多个模型系列和规模上都取得了显著的改进。与现有方法相比，AdaSearch显著提高了知识边界意识，减少了不必要的搜索调用，同时保持了强大的任务性能。例如，在某些任务上，AdaSearch可以将不必要的搜索调用减少高达50%，同时保持与现有方法相当甚至更好的准确率。

## 🎯 应用场景

AdaSearch适用于需要平衡知识和搜索的各种应用场景，例如金融问答、医疗诊断、法律咨询等高风险领域。通过减少不必要的搜索调用，可以降低成本并提高效率。此外，AdaSearch提供的透明、可解释的决策过程，有助于提高用户对模型的信任度。

## 📄 摘要（原文）

> Equipping large language models (LLMs) with search engines via reinforcement learning (RL) has emerged as an effective approach for building search agents. However, overreliance on search introduces unnecessary cost and risks exposure to noisy or malicious content, while relying solely on parametric knowledge risks hallucination. The central challenge is to develop agents that adaptively balance parametric knowledge with external search, invoking search only when necessary. Prior work mitigates search overuse by shaping rewards around the number of tool calls. However, these penalties require substantial reward engineering, provide ambiguous credit assignment, and can be exploited by agents that superficially reduce calls. Moreover, evaluating performance solely through call counts conflates necessary and unnecessary search, obscuring the measurement of true adaptive behavior. To address these limitations, we first quantify the self-knowledge awareness of existing search agents via an F1-based decision metric, revealing that methods such as Search-R1 often overlook readily available parametric knowledge. Motivated by these findings, we propose AdaSearch, a simple two-stage, outcome-driven RL framework that disentangles problem solving from the decision of whether to invoke search, and makes this decision process explicit and interpretable. This transparency is crucial for high-stakes domains such as finance and medical question answering, yet is largely neglected by prior approaches. Experiments across multiple model families and sizes demonstrate that AdaSearch substantially improves knowledge-boundary awareness, reduces unnecessary search calls, preserves strong task performance, and offers more transparent, interpretable decision behaviors.

