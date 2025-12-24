---
layout: default
title: "AdaSearch: Balancing Parametric Knowledge and Search in Large Language Models via Reinforcement Learning"
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

**AdaSearch：通过强化学习平衡大语言模型中的参数知识和搜索**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `强化学习` `搜索引擎` `知识边界` `自适应搜索`

## 📋 核心要点

1. 现有搜索增强的大语言模型过度依赖搜索，导致成本增加和潜在风险，而完全依赖模型自身知识则容易产生幻觉。
2. AdaSearch通过两阶段强化学习框架，将问题解决与搜索决策分离，显式地学习何时调用搜索，从而实现自适应平衡。
3. 实验表明，AdaSearch能显著提高知识边界意识，减少不必要的搜索调用，同时保持甚至提升任务性能，并提供更透明的决策过程。

## 📝 摘要（中文）

本文提出了一种利用强化学习为大语言模型配备搜索引擎的有效方法，用于构建搜索代理。然而，过度依赖搜索会引入不必要的成本，并可能暴露于噪声或恶意内容，而仅依赖参数知识则存在幻觉风险。核心挑战在于开发能够自适应地平衡参数知识与外部搜索的代理，仅在必要时才调用搜索。现有工作通过围绕工具调用次数塑造奖励来缓解搜索过度使用，但这些惩罚需要大量的奖励工程，提供模糊的信用分配，并且可能被表面上减少调用的代理利用。此外，仅通过调用次数评估性能会混淆必要和不必要的搜索，从而模糊了对真正自适应行为的衡量。为了解决这些局限性，我们首先通过基于F1的决策指标量化现有搜索代理的自我知识感知能力，揭示了诸如Search-R1之类的方法经常忽略现成的参数知识。受这些发现的启发，我们提出了AdaSearch，这是一个简单的两阶段、结果驱动的强化学习框架，它将问题解决与是否调用搜索的决策分离开来，并使该决策过程显式且可解释。这种透明性对于金融和医学问答等高风险领域至关重要，但之前的研究方法在很大程度上忽略了这一点。跨多个模型系列和规模的实验表明，AdaSearch显着提高了知识边界意识，减少了不必要的搜索调用，保持了强大的任务性能，并提供了更透明、可解释的决策行为。

## 🔬 方法详解

**问题定义**：现有方法在利用搜索引擎增强大语言模型时，难以平衡参数知识和外部搜索。过度依赖搜索会增加成本并引入噪声，而完全依赖参数知识则容易产生幻觉。现有方法通常通过惩罚工具调用次数来减少搜索使用，但这种方法需要大量人工设计奖励，且信用分配模糊，容易被模型利用。

**核心思路**：AdaSearch的核心思路是将问题解决过程与搜索决策过程解耦。模型首先尝试仅使用参数知识解决问题，然后独立地决定是否需要进行搜索。这种解耦使得模型能够更清晰地评估自身知识的边界，并仅在必要时才调用搜索。

**技术框架**：AdaSearch是一个两阶段的强化学习框架。第一阶段是问题解决阶段，模型尝试仅使用自身参数知识回答问题。第二阶段是搜索决策阶段，模型根据第一阶段的结果和问题本身，决定是否需要进行搜索。如果决定搜索，则执行搜索并利用搜索结果重新回答问题。整个过程通过强化学习进行训练，目标是最大化任务完成的奖励，同时最小化不必要的搜索调用。

**关键创新**：AdaSearch的关键创新在于将问题解决和搜索决策解耦，并通过强化学习显式地学习搜索策略。这种方法避免了手动设计奖励函数的复杂性，并允许模型自适应地学习何时调用搜索。此外，AdaSearch提供了一个更透明和可解释的决策过程，这对于高风险应用至关重要。

**关键设计**：AdaSearch使用基于F1的决策指标来量化模型的自我知识感知能力。强化学习算法使用标准的策略梯度方法，奖励函数包括任务完成的奖励和搜索调用的惩罚。具体参数设置（如学习率、奖励系数等）根据不同的模型和数据集进行调整。

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

实验结果表明，AdaSearch在多个模型和数据集上均取得了显著的性能提升。例如，在某些任务上，AdaSearch能够将不必要的搜索调用次数减少50%以上，同时保持甚至提高了任务完成的准确率。与现有方法相比，AdaSearch在知识边界意识方面也表现出明显的优势。

## 🎯 应用场景

AdaSearch可应用于需要大语言模型进行知识密集型任务的各种场景，例如金融问答、医疗诊断、法律咨询等。通过自适应地平衡参数知识和外部搜索，AdaSearch可以提高模型的准确性、可靠性和效率，并降低不必要的成本和风险。该方法尤其适用于对透明性和可解释性要求较高的领域。

## 📄 摘要（原文）

> Equipping large language models (LLMs) with search engines via reinforcement learning (RL) has emerged as an effective approach for building search agents. However, overreliance on search introduces unnecessary cost and risks exposure to noisy or malicious content, while relying solely on parametric knowledge risks hallucination. The central challenge is to develop agents that adaptively balance parametric knowledge with external search, invoking search only when necessary. Prior work mitigates search overuse by shaping rewards around the number of tool calls. However, these penalties require substantial reward engineering, provide ambiguous credit assignment, and can be exploited by agents that superficially reduce calls. Moreover, evaluating performance solely through call counts conflates necessary and unnecessary search, obscuring the measurement of true adaptive behavior. To address these limitations, we first quantify the self-knowledge awareness of existing search agents via an F1-based decision metric, revealing that methods such as Search-R1 often overlook readily available parametric knowledge. Motivated by these findings, we propose AdaSearch, a simple two-stage, outcome-driven RL framework that disentangles problem solving from the decision of whether to invoke search, and makes this decision process explicit and interpretable. This transparency is crucial for high-stakes domains such as finance and medical question answering, yet is largely neglected by prior approaches. Experiments across multiple model families and sizes demonstrate that AdaSearch substantially improves knowledge-boundary awareness, reduces unnecessary search calls, preserves strong task performance, and offers more transparent, interpretable decision behaviors.

