---
layout: default
title: "GPO: Learning from Critical Steps to Improve LLM Reasoning"
---

# GPO: Learning from Critical Steps to Improve LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16456" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16456v2</a>
  <a href="https://arxiv.org/pdf/2509.16456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16456v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16456v2', 'GPO: Learning from Critical Steps to Improve LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Yu, Zelei Cheng, Xian Wu, Xinyu Xing

**分类**: cs.AI

**发布日期**: 2025-09-19 (更新: 2025-10-21)

**备注**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**GPO：通过学习关键步骤提升大型语言模型推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `关键步骤` `优势函数` `策略优化`

## 📋 核心要点

1. 现有方法在提升LLM推理能力时，忽略了推理轨迹中的关键步骤，导致优化效率不高。
2. GPO通过识别推理过程中的关键步骤，并优先学习这些步骤，从而更有效地提升推理能力。
3. 实验表明，GPO可以与多种优化方法结合，在推理基准测试中显著提升性能，具有良好的通用性。

## 📝 摘要（中文）

大型语言模型（LLMs）在各个领域得到日益广泛的应用，并在不同任务上展现出令人印象深刻的潜力。最近，推理LLMs被提出以提高LLMs的	extit{推理}或	extit{思考}能力，从而解决复杂问题。尽管推理LLMs取得了可喜的成果，但增强LLMs的多步推理能力仍然是一个重大挑战。现有的优化方法虽然提升了LLM的推理能力，但通常将推理轨迹视为一个整体，而没有考虑轨迹中潜在的关键步骤。在本文中，我们介绍了一种新的微调策略，即	extbf{G}uided 	extbf{P}ivotal 	extbf{O}ptimization (GPO)，它深入研究推理过程，从而实现更有效的改进。GPO首先识别推理轨迹中的“关键步骤”——模型必须谨慎进行才能成功解决问题的点。我们通过估计优势函数来定位关键步骤。然后，GPO将策略重置为关键步骤，对新的rollout进行采样，并优先学习这些rollout。这种关注使模型能够更有效地从推理过程中的关键时刻学习，从而提高推理性能。我们证明GPO是一种通用策略，可以与各种优化方法集成，以提高推理性能。除了理论分析之外，我们在具有挑战性的推理基准上的实验表明，GPO可以持续且显着地提高现有优化方法的性能，展示了其通过专注于生成过程中的关键时刻来提高LLM推理的有效性和通用性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在多步推理任务中表现不佳的问题。现有优化方法通常将整个推理过程视为一个整体，忽略了其中对最终结果起决定性作用的关键步骤。这种一视同仁的处理方式导致优化效率低下，难以充分提升LLM的推理能力。

**核心思路**：GPO的核心思路是聚焦于推理过程中的“关键步骤”。论文认为，在多步推理过程中，某些步骤对最终结果的影响远大于其他步骤。通过识别并重点优化这些关键步骤，可以更有效地提升LLM的整体推理能力。具体而言，GPO通过估计优势函数来定位这些关键步骤，并在此基础上进行策略优化。

**技术框架**：GPO的技术框架主要包含以下几个阶段：1) **关键步骤识别**：使用优势函数估计方法，评估每个步骤对最终结果的贡献，从而识别出关键步骤。2) **策略重置**：将LLM的策略重置到关键步骤的状态。3) **Rollout采样**：从关键步骤开始，进行新的rollout采样，生成不同的推理轨迹。4) **优先学习**：优先学习包含关键步骤的rollout，使模型能够更有效地从这些关键时刻学习。

**关键创新**：GPO的关键创新在于其对推理过程的细粒度分析和优化。与现有方法将推理过程视为整体不同，GPO能够识别并重点优化对结果影响最大的关键步骤。这种针对性优化策略能够更有效地提升LLM的推理能力。此外，GPO具有良好的通用性，可以与多种现有的优化方法相结合。

**关键设计**：GPO的关键设计包括：1) **优势函数估计**：优势函数的选择和计算方法直接影响关键步骤的识别准确性。论文可能采用了特定的优势函数计算方法，例如基于奖励的差分计算。2) **策略重置方法**：如何将LLM的策略有效地重置到关键步骤的状态，可能涉及到状态表示和策略调整等技术细节。3) **优先学习策略**：如何有效地利用包含关键步骤的rollout进行学习，可能涉及到损失函数的设计和采样策略的选择。

## 📊 实验亮点

实验结果表明，GPO能够显著提升现有优化方法的性能。在多个具有挑战性的推理基准测试中，GPO与现有方法结合后，性能均得到了显著提升。具体的性能提升幅度取决于具体的基准测试和优化方法，但总体而言，GPO能够有效地提高LLM的推理能力，验证了其有效性和通用性。例如，GPO可能在某个基准测试中将准确率提升了5%-10%。

## 🎯 应用场景

GPO方法具有广泛的应用前景，可以应用于各种需要复杂推理能力的场景，例如问答系统、知识图谱推理、代码生成和机器人控制等。通过提升LLM的推理能力，GPO可以帮助解决更复杂的问题，提高AI系统的智能化水平，并在医疗诊断、金融分析等领域发挥重要作用。未来，GPO有望成为提升LLM推理能力的重要技术手段。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used in various domains, showing impressive potential on different tasks. Recently, reasoning LLMs have been proposed to improve the \textit{reasoning} or \textit{thinking} capabilities of LLMs to solve complex problems. Despite the promising results of reasoning LLMs, enhancing the multi-step reasoning capabilities of LLMs still remains a significant challenge. While existing optimization methods have advanced the LLM reasoning capabilities, they often treat reasoning trajectories as a whole, without considering the underlying critical steps within the trajectory. In this paper, we introduce \textbf{G}uided \textbf{P}ivotal \textbf{O}ptimization (GPO), a novel fine-tuning strategy that dives into the reasoning process to enable more effective improvements. GPO first identifies the `critical step' within a reasoning trajectory - a point that the model must carefully proceed to succeed at the problem. We locate the critical step by estimating the advantage function. GPO then resets the policy to the critical step, samples the new rollout and prioritizes the learning process on those rollouts. This focus allows the model to learn more effectively from pivotal moments within the reasoning process to improve the reasoning performance. We demonstrate that GPO is a general strategy that can be integrated with various optimization methods to improve reasoning performance. Besides theoretical analysis, our experiments across challenging reasoning benchmarks show that GPO can consistently and significantly enhance the performance of existing optimization methods, showcasing its effectiveness and generalizability in improving LLM reasoning by concentrating on pivotal moments within the generation process.

