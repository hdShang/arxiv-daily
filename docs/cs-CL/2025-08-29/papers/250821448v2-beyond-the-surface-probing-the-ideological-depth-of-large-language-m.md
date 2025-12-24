---
layout: default
title: "Beyond the Surface: Probing the Ideological Depth of Large Language Models"
---

# Beyond the Surface: Probing the Ideological Depth of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21448" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21448v2</a>
  <a href="https://arxiv.org/pdf/2508.21448.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21448v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21448v2', 'Beyond the Surface: Probing the Ideological Depth of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shariar Kabir, Kevin Esterling, Yue Dong

**分类**: cs.CL

**发布日期**: 2025-08-29 (更新: 2025-11-14)

---

## 💡 一句话要点

**提出意识深度概念以分析大型语言模型的政治倾向**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `意识深度` `政治倾向` `可操控性` `稀疏自编码器` `特征分析` `因果消融实验`

## 📋 核心要点

1. 现有大型语言模型在表现政治倾向时存在一致性不足的问题，影响其在特定指令下的响应能力。
2. 本文提出意识深度的概念，通过可操控性和内部特征丰富性来评估模型的政治表现，采用稀疏自编码器进行分析。
3. 实验结果显示，Gemma在可操控性和激活的政治特征数量上均显著优于Llama，且特征消融实验揭示了拒绝响应的潜在原因。

## 📝 摘要（中文）

大型语言模型（LLMs）表现出明显的政治倾向，但在一致性表现上存在显著差异。本文定义了意识深度，包含模型在无失败地遵循政治指令的能力（可操控性）和其内部政治表示的特征丰富性。通过对Llama-3.1-8B-Instruct和Gemma-2-9B-IT的比较，发现Gemma在可操控性和激活的政治特征数量上均优于Llama。此外，针对Gemma的特定政治特征进行因果消融实验，表明拒绝响应的原因可能源于能力不足，而非安全防护。这些结果表明意识深度是LLMs的可测量属性，可操控性则为其潜在政治架构提供了视角。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在遵循政治指令时表现不一致的问题，现有方法未能有效量化模型的政治倾向和可操控性。

**核心思路**：通过定义意识深度，结合可操控性和内部特征丰富性，利用稀疏自编码器（SAEs）对模型的政治表示进行深入分析，以揭示其潜在的政治架构。

**技术框架**：研究采用Llama-3.1-8B-Instruct和Gemma-2-9B-IT作为实验对象，比较基于提示和激活的干预方法，分析其政治特征的激活情况。主要模块包括模型选择、干预方法、特征提取和行为分析。

**关键创新**：意识深度作为LLMs的新测量属性，提供了一种新的视角来理解模型的政治倾向，尤其是可操控性与内部特征的关系。

**关键设计**：采用稀疏自编码器进行特征提取，设计了特定的因果消融实验，以验证不同政治特征对模型行为的影响，确保实验的可重复性和结果的可靠性。

## 📊 实验亮点

实验结果显示，Gemma在可操控性方面优于Llama，激活的政治特征数量约为Llama的7.3倍。此外，特征消融实验表明，Gemma在特定政治特征缺失时，拒绝响应的频率显著增加，揭示了能力不足的影响。

## 🎯 应用场景

该研究为理解大型语言模型的政治倾向提供了新的框架，潜在应用于政治分析、舆情监测和社会科学研究等领域。通过量化模型的意识深度，可以为模型的设计和优化提供指导，提升其在特定任务中的表现。

## 📄 摘要（原文）

> Large language models (LLMs) display recognizable political leanings, yet they vary significantly in their ability to represent a political orientation consistently. In this paper, we define ideological depth as (i) a model's ability to follow political instructions without failure (steerability), and (ii) the feature richness of its internal political representations measured with sparse autoencoders (SAEs), an unsupervised sparse dictionary learning (SDL) approach. Using Llama-3.1-8B-Instruct and Gemma-2-9B-IT as candidates, we compare prompt-based and activation-steering interventions and probe political features with publicly available SAEs. We find large, systematic differences: Gemma is more steerable in both directions and activates approximately 7.3x more distinct political features than Llama. Furthermore, causal ablations of a small targeted set of Gemma's political features to create a similar feature-poor setting induce consistent shifts in its behavior, with increased rates of refusals across topics. Together, these results indicate that refusals on benign political instructions or prompts can arise from capability deficits rather than safety guardrails. Ideological depth thus emerges as a measurable property of LLMs, and steerability serves as a window into their latent political architecture.

