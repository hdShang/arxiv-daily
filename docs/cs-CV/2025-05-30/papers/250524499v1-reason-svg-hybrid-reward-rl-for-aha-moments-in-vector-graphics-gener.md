---
layout: default
title: "Reason-SVG: Hybrid Reward RL for Aha-Moments in Vector Graphics Generation"
---

# Reason-SVG: Hybrid Reward RL for Aha-Moments in Vector Graphics Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24499" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24499v1</a>
  <a href="https://arxiv.org/pdf/2505.24499.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24499v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24499v1', 'Reason-SVG: Hybrid Reward RL for Aha-Moments in Vector Graphics Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ximing Xing, Yandong Guan, Jing Zhang, Dong Xu, Qian Yu

**分类**: cs.CV

**发布日期**: 2025-05-30

**备注**: 17 pages, 5 figures

---

## 💡 一句话要点

**提出Reason-SVG以解决SVG生成中的推理不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可扩展矢量图形` `大型语言模型` `推理能力` `强化学习` `设计理由` `混合奖励` `监督微调` `群体相对策略优化`

## 📋 核心要点

1. 现有大型语言模型在生成SVG时面临结构有效性、语义一致性和视觉连贯性等推理能力不足的挑战。
2. 论文提出了Reason-SVG框架，通过“思考绘图”范式，结合监督微调和强化学习，提升模型的推理能力。
3. 实验结果表明，Reason-SVG在生成准确和视觉吸引的SVG方面显著优于现有方法，促进了设计中的“顿悟时刻”。

## 📝 摘要（中文）

生成高质量的可扩展矢量图形（SVG）对大型语言模型（LLMs）来说是一项挑战，因为这需要在结构有效性、语义一致性和视觉连贯性方面进行高级推理，而当前的LLMs往往无法满足这些要求。本文提出了Reason-SVG，一个旨在增强LLM推理能力的框架。Reason-SVG开创了“思考绘图”（DwT）范式，模型同时生成SVG代码和明确的设计理由，模拟人类的创造过程。该框架采用两阶段训练策略：首先，通过监督微调（SFT）激活基础推理能力；其次，利用强化学习（RL）和群体相对策略优化（GRPO），通过奖励驱动的推理生成DwT和SVG的理由。为促进推理驱动的SVG生成，设计了混合奖励函数，评估DwT推理的存在和效用，以及结构有效性、语义对齐和视觉质量。还引入了SVGX-DwT-10k数据集，包含10,000对SVG-DwT样本，显著提升了LLM在生成准确且视觉吸引的SVG方面的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成SVG时推理能力不足的问题，现有方法在结构有效性和视觉连贯性方面表现不佳。

**核心思路**：Reason-SVG框架通过“思考绘图”范式，要求模型同时生成SVG代码和设计理由，从而模拟人类的创造过程，增强推理能力。

**技术框架**：该框架采用两阶段训练策略，第一阶段为监督微调（SFT），激活基础推理能力；第二阶段为强化学习（RL），使用群体相对策略优化（GRPO），通过奖励驱动的推理生成DwT和SVG理由。

**关键创新**：最重要的创新在于引入“思考绘图”范式和混合奖励函数，前者使模型能够生成设计理由，后者评估DwT推理的有效性及其他生成质量指标。

**关键设计**：混合奖励函数设计考虑了DwT推理的存在和效用，以及SVG的结构有效性、语义对齐和视觉质量，确保模型在生成过程中能够综合考虑多方面因素。

## 📊 实验亮点

实验结果显示，Reason-SVG在SVG生成任务中相较于基线模型的性能提升显著，具体表现为生成的SVG在结构有效性和视觉质量上均有明显改善，且模型生成的设计理由有效提升了用户的理解和满意度。

## 🎯 应用场景

Reason-SVG的研究成果在多个领域具有潜在应用价值，包括图形设计、游戏开发和教育等。通过提升SVG生成的质量和效率，该框架能够帮助设计师更好地实现创意，进而推动相关行业的发展。未来，Reason-SVG可能会影响更多的创意生成任务，促进人机协作的进步。

## 📄 摘要（原文）

> Generating high-quality Scalable Vector Graphics (SVGs) is challenging for Large Language Models (LLMs), as it requires advanced reasoning for structural validity, semantic faithfulness, and visual coherence -- capabilities in which current LLMs often fall short. In this work, we introduce Reason-SVG, a novel framework designed to enhance LLM reasoning for SVG generation. Reason-SVG pioneers the "Drawing-with-Thought" (DwT) paradigm, in which models generate both SVG code and explicit design rationales, mimicking the human creative process. Reason-SVG adopts a two-stage training strategy: First, Supervised Fine-Tuning (SFT) trains the LLM on the DwT paradigm to activate foundational reasoning abilities. Second, Reinforcement Learning (RL), utilizing Group Relative Policy Optimization (GRPO), empowers the model to generate both DwT and SVGs rationales through refined, reward-driven reasoning. To facilitate reasoning-driven SVG generation, we design a Hybrid Reward function that evaluates the presence and utility of DwT reasoning, along with structural validity, semantic alignment, and visual quality. We also introduce the SVGX-DwT-10k dataset, a high-quality corpus of 10,000 SVG-DwT pairs, where each SVG code is generated based on explicit DwT reasoning. By integrating DwT, SFT, and Hybrid Reward-guided RL, Reason-SVG significantly improves LLM performance in generating accurate and visually compelling SVGs, potentially fostering "Aha moments" in design.

