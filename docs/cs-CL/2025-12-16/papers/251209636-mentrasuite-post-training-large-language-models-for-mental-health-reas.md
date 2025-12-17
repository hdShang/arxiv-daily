---
layout: default
title: MentraSuite: Post-Training Large Language Models for Mental Health Reasoning and Assessment
---

# MentraSuite: Post-Training Large Language Models for Mental Health Reasoning and Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09636" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09636</a>
  <a href="https://arxiv.org/pdf/2512.09636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09636" onclick="toggleFavorite(this, '2512.09636', 'MentraSuite: Post-Training Large Language Models for Mental Health Reasoning and Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengxi Xiao, Kailai Yang, Pengde Zhao, Enze Zhang, Ziyan Kuang, Zhiwei Liu, Weiguang Han, Shu Liao, Lianting Huang, Jinpeng Hu, Min Peng, Qianqian Xie, Sophia Ananiadou

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**MentraSuite：通过后训练大语言模型提升心理健康推理与评估能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理健康` `大语言模型` `推理能力` `后训练` `强化学习` `基准测试` `一致性` `评估诊断`

## 📋 核心要点

1. 现有心理健康领域的大语言模型缺乏临床对齐的逐步推理能力，限制了其在评估、诊断等任务中的应用。
2. MentraSuite框架通过构建高质量推理轨迹和混合SFT-RL训练，优化模型推理的连贯性和可靠性。
3. Mindora模型在MentraBench基准测试中表现最佳，尤其在推理可靠性方面，验证了其在复杂心理健康场景中的有效性。

## 📝 摘要（中文）

心理健康问题影响着全球数亿人，网络已成为获取支持、信息和评估的主要渠道。大型语言模型（LLMs）提供了可扩展且易于访问的帮助，但当其推理不完整、不一致或缺乏依据时，在心理健康环境中的部署仍然存在风险。现有的心理学LLM强调情感理解或知识回忆，但忽略了评估、诊断、干预计划、抽象和验证所需的逐步、临床对齐的推理。为了解决这些问题，我们引入了MentraSuite，一个用于推进可靠心理健康推理的统一框架。我们提出了MentraBench，一个全面的基准，涵盖五个核心推理方面、六个任务和13个数据集，评估任务性能和推理质量的五个维度：简洁性、连贯性、避免幻觉、任务理解和内部一致性。我们进一步提出了Mindora，一个通过混合SFT-RL框架优化的后训练模型，具有不一致性检测奖励，以强制执行忠实和连贯的推理。为了支持训练，我们使用一种新颖的推理轨迹生成策略构建高质量的轨迹，该策略策略性地过滤困难样本，并应用结构化的、面向一致性的重写过程来生成简洁、可读且平衡良好的轨迹。在评估的20个LLM中，Mindora在MentraBench上实现了最高的平均性能，并在推理可靠性方面表现出色，证明了其在复杂心理健康场景中的有效性。

## 🔬 方法详解

**问题定义**：现有心理健康领域的大语言模型（LLMs）虽然在情感理解和知识回忆方面表现良好，但在进行心理评估、诊断和干预计划等任务时，缺乏临床专家所具备的逐步、连贯且可靠的推理能力。这些模型容易产生不一致、不完整甚至幻觉性的推理结果，限制了它们在实际临床环境中的应用。因此，如何提升LLMs在心理健康领域的推理能力，使其能够进行更准确、更可靠的评估和诊断，是本研究要解决的核心问题。

**核心思路**：本研究的核心思路是通过后训练的方式，利用高质量的推理轨迹数据，提升LLMs在心理健康领域的推理能力。具体来说，首先构建一个全面的基准测试集MentraBench，用于评估模型在多个推理维度上的性能。然后，通过一种新颖的推理轨迹生成策略，生成高质量的训练数据，并采用混合的SFT（监督微调）和RL（强化学习）框架，训练一个名为Mindora的模型。通过不一致性检测奖励，鼓励模型生成更忠实和连贯的推理过程。

**技术框架**：MentraSuite框架主要包含以下几个关键组成部分：1) MentraBench基准测试集，用于评估模型在心理健康推理方面的性能；2) 推理轨迹生成策略，用于生成高质量的训练数据；3) Mindora模型，通过混合SFT-RL框架进行训练，并采用不一致性检测奖励；4) 评估流程，用于评估Mindora模型在MentraBench上的性能。整个流程首先利用推理轨迹生成策略构建训练数据，然后使用SFT进行初步微调，接着使用RL进一步优化，最后在MentraBench上进行评估。

**关键创新**：本研究的关键创新点在于：1) 提出了MentraBench基准测试集，该基准全面评估了模型在心理健康推理方面的多个维度；2) 提出了一种新颖的推理轨迹生成策略，能够生成高质量、简洁、可读且平衡良好的训练数据；3) 采用了混合SFT-RL框架，并引入了不一致性检测奖励，有效提升了模型的推理连贯性和可靠性。与现有方法相比，本研究更注重模型的推理过程，而非仅仅关注最终的预测结果。

**关键设计**：在推理轨迹生成策略中，采用了策略性地过滤困难样本，并应用结构化的、面向一致性的重写过程。在混合SFT-RL框架中，SFT用于初始化模型参数，RL用于进一步优化推理过程。不一致性检测奖励基于模型生成的推理轨迹，检测其中是否存在矛盾或不一致之处，并给予相应的惩罚。具体的奖励函数设计和超参数设置在论文中有详细描述，但此处未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.09636/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.09636/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.09636/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Mindora模型在MentraBench基准测试中取得了最佳的平均性能，显著优于其他20个评估的LLM。尤其在推理可靠性方面，Mindora表现出色，证明了其在复杂心理健康场景中的有效性。具体的性能提升幅度未知，但整体结果表明Mindora在心理健康推理方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于开发智能心理健康助手，辅助心理咨询师进行初步评估和诊断，提供个性化的干预建议。此外，该技术还可用于构建在线心理健康教育平台，提供高质量的心理健康知识和资源，提升公众的心理健康素养。未来，该研究有望推动心理健康服务的普及和智能化。

## 📄 摘要（原文）

> Mental health disorders affect hundreds of millions globally, and the Web now serves as a primary medium for accessing support, information, and assessment. Large language models (LLMs) offer scalable and accessible assistance, yet their deployment in mental-health settings remains risky when their reasoning is incomplete, inconsistent, or ungrounded. Existing psychological LLMs emphasize emotional understanding or knowledge recall but overlook the step-wise, clinically aligned reasoning required for appraisal, diagnosis, intervention planning, abstraction, and verification. To address these issues, we introduce MentraSuite, a unified framework for advancing reliable mental-health reasoning. We propose MentraBench, a comprehensive benchmark spanning five core reasoning aspects, six tasks, and 13 datasets, evaluating both task performance and reasoning quality across five dimensions: conciseness, coherence, hallucination avoidance, task understanding, and internal consistency. We further present Mindora, a post-trained model optimized through a hybrid SFT-RL framework with an inconsistency-detection reward to enforce faithful and coherent reasoning. To support training, we construct high-quality trajectories using a novel reasoning trajectory generation strategy, that strategically filters difficult samples and applies a structured, consistency-oriented rewriting process to produce concise, readable, and well-balanced trajectories. Across 20 evaluated LLMs, Mindora achieves the highest average performance on MentraBench and shows remarkable performances in reasoning reliability, demonstrating its effectiveness for complex mental-health scenarios.

