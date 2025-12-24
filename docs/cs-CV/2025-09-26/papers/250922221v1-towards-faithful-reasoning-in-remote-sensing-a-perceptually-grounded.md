---
layout: default
title: "Towards Faithful Reasoning in Remote Sensing: A Perceptually-Grounded GeoSpatial Chain-of-Thought for Vision-Language Models"
---

# Towards Faithful Reasoning in Remote Sensing: A Perceptually-Grounded GeoSpatial Chain-of-Thought for Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22221" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22221v1</a>
  <a href="https://arxiv.org/pdf/2509.22221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22221v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22221v1', 'Towards Faithful Reasoning in Remote Sensing: A Perceptually-Grounded GeoSpatial Chain-of-Thought for Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Liu, Lang Sun, Ronghao Fu, Bo Yang

**分类**: cs.CV

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出基于感知的地理空间思维链Geo-CoT，提升遥感视觉-语言模型推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像分析` `视觉-语言模型` `思维链` `地理空间推理` `可解释性` `群体奖励策略优化` `数据集构建`

## 📋 核心要点

1. 现有遥感VLM端到端训练忽略推理步骤，导致结果不可靠，限制了复杂分析任务的应用。
2. 提出Geo-CoT框架，将遥感分析分解为可验证的多步骤过程，模拟人类推理。
3. 构建Geo-CoT380k数据集，并使用SFT和GRPO策略训练RSThinker模型，显著提升性能。

## 📝 摘要（中文）

遥感领域的视觉-语言模型(VLMs)在复杂分析任务中表现不佳，这是由于其端到端训练范式绕过了关键的推理步骤，导致输出结果难以验证。为了解决这个问题，我们提出了基于感知的地理空间思维链(Geo-CoT)框架，该框架将遥感分析建模为一个可验证的多步骤过程。我们通过一个两阶段对齐策略来灌输这种分析过程，利用Geo-CoT380k，这是第一个大规模的结构化Geo-CoT推理数据集。该策略首先采用监督微调(SFT)来灌输基础认知架构，然后利用群体奖励策略优化(GRPO)来改进模型的推理策略，使其更符合事实。由此产生的模型RSThinker，输出最终答案及其可验证的分析轨迹。这种能力产生了卓越的性能，在各种任务中显著优于最先进的模型。Geo-CoT380k数据集和RSThinker模型的公开发布，为地球观测从不透明的感知走向结构化的、可验证的推理提供了一条具体的途径。

## 🔬 方法详解

**问题定义**：遥感领域中的视觉-语言模型(VLMs)在执行复杂的分析任务时，由于缺乏明确的推理过程，往往难以给出准确且可信的结果。现有的端到端训练方法虽然能够直接将图像映射到答案，但忽略了中间的推理步骤，导致模型成为一个“黑盒”，其输出结果难以验证，也难以解释其决策过程。这种方式在需要精确地理空间推理的遥感应用中尤其不利。

**核心思路**：论文的核心思路是将遥感分析任务分解为一系列可验证的步骤，模拟人类专家进行地理空间推理的过程。通过引入“思维链”（Chain-of-Thought, CoT）的概念，模型不再直接输出最终答案，而是逐步生成中间推理步骤，每个步骤都基于可感知的地理空间信息。这种方式使得模型的推理过程更加透明，也更容易进行调试和改进。

**技术框架**：整体框架包含两个主要阶段：首先，使用监督微调(SFT)在Geo-CoT380k数据集上训练模型，使其具备生成地理空间思维链的基本能力。Geo-CoT380k数据集包含大量的遥感图像和对应的结构化推理过程。其次，使用群体奖励策略优化(GRPO)进一步提升模型的推理能力，使其输出的推理链更符合事实，最终答案更加准确。GRPO通过对多个推理链进行评估，并根据其正确性和完整性给予不同的奖励，从而引导模型学习更有效的推理策略。

**关键创新**：最重要的技术创新点在于将思维链推理与地理空间感知相结合，提出了Perceptually-Grounded Geospatial Chain-of-Thought (Geo-CoT)框架。与传统的端到端模型相比，Geo-CoT能够生成可验证的推理过程，提高了模型的可解释性和可靠性。此外，Geo-CoT380k数据集的构建也为遥感领域的思维链研究提供了重要的数据基础。

**关键设计**：Geo-CoT380k数据集包含了38万个遥感图像和对应的结构化推理过程，涵盖了多种地理空间分析任务。在训练过程中，SFT使用交叉熵损失函数来优化模型的生成能力。GRPO则采用了一种基于群体奖励的强化学习方法，通过对多个推理链进行评估，并根据其正确性和完整性给予不同的奖励。具体的奖励函数设计需要根据任务的特点进行调整，以确保模型能够学习到正确的推理策略。

## 📊 实验亮点

RSThinker模型在多个遥感分析任务中显著优于现有模型，证明了Geo-CoT框架的有效性。具体性能提升数据在论文中给出，表明该模型在准确性和可解释性方面均有显著提升。Geo-CoT380k数据集的发布也为遥感领域的思维链研究提供了宝贵资源。

## 🎯 应用场景

该研究成果可广泛应用于遥感图像分析领域，例如土地利用分类、灾害监测、城市规划等。通过提供可验证的推理过程，可以提高决策的透明度和可靠性，为政府、企业和研究机构提供更可靠的地理空间信息支持。未来，该方法有望扩展到其他需要复杂推理的遥感应用中，例如气候变化研究、环境监测等。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) in remote sensing often fail at complex analytical tasks, a limitation stemming from their end-to-end training paradigm that bypasses crucial reasoning steps and leads to unverifiable outputs. To address this limitation, we introduce the Perceptually-Grounded Geospatial Chain-of-Thought (Geo-CoT), a framework that models remote sensing analysis as a verifiable, multi-step process. We instill this analytical process through a two-stage alignment strategy, leveraging Geo-CoT380k, the first large-scale dataset of structured Geo-CoT rationales. This strategy first employs supervised fine-tuning (SFT) to instill the foundational cognitive architecture, then leverages Group Reward Policy Optimization (GRPO) to refine the model's reasoning policy towards factual correctness. The resulting model, RSThinker, outputs both a final answer and its justifying, verifiable analytical trace. This capability yields dominant performance, significantly outperforming state-of-the-art models across a comprehensive range of tasks. The public release of our Geo-CoT380k dataset and RSThinker model upon publication serves as a concrete pathway from opaque perception towards structured, verifiable reasoning for Earth Observation.

