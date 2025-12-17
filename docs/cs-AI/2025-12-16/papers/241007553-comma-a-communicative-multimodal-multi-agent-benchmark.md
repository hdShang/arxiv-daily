---
layout: default
title: COMMA: A Communicative Multimodal Multi-Agent Benchmark
---

# COMMA: A Communicative Multimodal Multi-Agent Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2410.07553" class="toolbar-btn" target="_blank">📄 arXiv: 2410.07553</a>
  <a href="https://arxiv.org/pdf/2410.07553.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2410.07553" onclick="toggleFavorite(this, '2410.07553', 'COMMA: A Communicative Multimodal Multi-Agent Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timothy Ossowski, Danyal Maqbool, Jixuan Chen, Zefan Cai, Tyler Bradshaw, Junjie Hu

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出COMMA：一个用于评估多模态多智能体语言交流协作的新基准。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `多模态学习` `语言交流` `协作基准` `智能体评估`

## 📋 核心要点

1. 现有智能体基准在评估多智能体语言交流协作方面存在不足，无法有效衡量智能体在信息不对称情况下的协同能力。
2. COMMA基准通过设计多模态谜题，模拟真实协作场景，考察智能体在语言沟通下的问题解决、信息共享和协同推理能力。
3. 实验结果表明，即使是GPT-4o等先进模型在COMMA基准上表现不佳，表明多智能体交流协作仍是当前模型的薄弱环节。

## 📝 摘要（中文）

本文介绍了一个名为COMMA的新型谜题基准，旨在评估多模态多智能体系统通过语言交流进行协作的性能。现有基于大型模型的多模态智能体在语言交流协作方面潜力被忽视，这导致对它们在真实场景中有效性的理解存在关键差距，尤其是在与人类交流时。现有智能体基准未能解决智能体间交流和协作的关键方面，特别是在智能体对信息的访问不平等，且必须协同完成超出个体能力的任务时。COMMA包含各种多模态谜题，对智能体在交流协作环境中的四类关键能力进行全面评估。研究结果揭示了现有模型（包括GPT-4o和o4-mini等强大专有模型，以及R1-Onevision和LLaVA-CoT等推理模型）的弱点，许多思维链推理模型在智能体间协作中的表现甚至不如随机基线，表明其交流能力有待提高。

## 🔬 方法详解

**问题定义**：现有的大型多模态模型在单智能体任务上取得了显著进展，但在多智能体协作，特别是需要语言交流的协作场景中，其能力尚未得到充分评估。现有的智能体基准测试未能充分考虑智能体之间信息不对称、任务复杂性以及交流策略等关键因素，导致无法准确评估智能体在真实协作环境中的表现。

**核心思路**：COMMA基准的核心思路是设计一系列多模态谜题，这些谜题需要多个智能体通过语言交流，共享信息、协商策略并协同解决。通过控制每个智能体所能访问的信息，并增加谜题的复杂性，COMMA能够更全面地评估智能体在协作过程中的推理、沟通和决策能力。

**技术框架**：COMMA基准包含一个谜题生成器，用于创建各种多模态谜题。每个谜题都包含视觉信息（例如图像）和文本描述，并分配给多个智能体。智能体之间可以通过语言进行交流，但每个智能体只能访问部分信息。智能体需要通过交流，整合信息，推理出谜题的答案。评估指标包括谜题解决率、交流效率和协作质量。

**关键创新**：COMMA基准的关键创新在于其对多智能体协作场景的模拟，以及对语言交流在协作过程中的作用的强调。与传统的单智能体基准测试相比，COMMA更贴近真实世界的应用场景，能够更有效地评估智能体的协作能力。此外，COMMA还提供了一个可扩展的谜题生成框架，可以根据需要生成不同难度和类型的谜题。

**关键设计**：COMMA基准中的谜题设计考虑了以下关键因素：信息不对称程度、谜题复杂性、交流成本和协作策略。谜题的难度可以通过调整视觉信息的清晰度、文本描述的详细程度以及智能体之间的交流限制来控制。评估指标的设计旨在衡量智能体的协作效率和质量，包括谜题解决率、交流轮数、交流内容的相关性和准确性等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2410.07553/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2410.07553/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2410.07553/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，即使是像GPT-4o这样强大的专有模型，在COMMA基准上的表现也远未达到理想水平。许多思维链推理模型，如R1-Onevision和LLaVA-CoT，在智能体间协作中的表现甚至不如随机基线。这表明当前的多模态模型在多智能体交流协作方面仍存在显著的不足，需要进一步的研究和改进。

## 🎯 应用场景

COMMA基准的潜在应用领域包括：多智能体机器人协作、人机协作、智能交通系统、分布式决策系统等。通过COMMA基准，可以更好地评估和改进多智能体系统的协作能力，提高其在复杂环境中的适应性和可靠性。此外，COMMA还可以用于研究人类协作行为，为设计更有效的人机协作系统提供理论基础。

## 📄 摘要（原文）

> The rapid advances of multimodal agents built on large foundation models have largely overlooked their potential for language-based communication between agents in collaborative tasks. This oversight presents a critical gap in understanding their effectiveness in real-world deployments, particularly when communicating with humans. Existing agentic benchmarks fail to address key aspects of inter-agent communication and collaboration, particularly in scenarios where agents have unequal access to information and must work together to achieve tasks beyond the scope of individual capabilities. To fill this gap, we introduce COMMA: a novel puzzle benchmark designed to evaluate the collaborative performance of multimodal multi-agent systems through language communication. Our benchmark features a variety of multimodal puzzles, providing a comprehensive evaluation across four key categories of agentic capability in a communicative collaboration setting. Our findings reveal surprising weaknesses in state-of-the-art models, including strong proprietary models like GPT-4o and reasoning models like o4-mini. Many chain of thought reasoning models such as R1-Onevision and LLaVA-CoT struggle to outperform even a random baseline in agent-agent collaboration, indicating a potential growth area in their communication abilities.

