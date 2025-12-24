---
layout: default
title: Explaining Large Language Models with gSMILE
---

# Explaining Large Language Models with gSMILE

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21657" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21657v5</a>
  <a href="https://arxiv.org/pdf/2505.21657.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21657v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21657v5', 'Explaining Large Language Models with gSMILE')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeinab Dehghani, Mohammed Naveed Akram, Koorosh Aslansefat, Adil Khan, Yiannis Papadopoulos

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-10-21)

---

## 💡 一句话要点

**提出gSMILE以解决大语言模型可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `可解释性` `gSMILE` `文本生成` `模型无关` `扰动方法` `Wasserstein距离` `归因分析`

## 📋 核心要点

1. 现有的大语言模型在决策过程中的不透明性限制了其在高风险应用中的信任和问责。
2. gSMILE是一种基于扰动的框架，通过控制提示扰动和Wasserstein距离度量实现令牌级可解释性。
3. 实验结果表明，gSMILE在多个大语言模型上提供了可靠的归因，Claude 2.1在注意力保真度上表现优异。

## 📝 摘要（中文）

大语言模型（LLMs）如GPT、LLaMA和Claude在文本生成方面表现出色，但其决策过程仍然不透明，限制了在高风险应用中的信任和问责。本文提出了gSMILE（生成SMILE），一种模型无关的基于扰动的框架，旨在实现LLMs的令牌级可解释性。gSMILE扩展了SMILE方法，利用受控的提示扰动、Wasserstein距离度量和加权线性替代模型，识别对输出影响最大的输入令牌。通过生成直观的热图，gSMILE能够可视化影响令牌和推理路径。我们在多个领先的LLMs上评估gSMILE，结果显示其提供了可靠的人类对齐归因，尤其在注意力保真度和输出一致性方面表现突出。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型的可解释性问题。现有方法往往缺乏透明度，导致用户对模型决策过程的信任不足。

**核心思路**：gSMILE通过控制提示扰动和Wasserstein距离度量来识别对输出影响最大的输入令牌，从而实现更高的可解释性。这样的设计使得模型的决策过程更加透明，便于用户理解。

**技术框架**：gSMILE的整体架构包括三个主要模块：受控提示扰动模块、Wasserstein距离计算模块和加权线性替代模型模块。通过这些模块，gSMILE能够生成影响令牌的热图，直观展示模型的推理路径。

**关键创新**：gSMILE的主要创新在于其模型无关性和基于扰动的归因方法，这与现有的可解释性方法形成了鲜明对比，后者往往依赖于特定模型的内部机制。

**关键设计**：在设计中，gSMILE使用了加权线性替代模型来提高归因的准确性，并通过Wasserstein距离度量来评估扰动对模型输出的影响，确保了归因结果的可靠性和一致性。

## 📊 实验亮点

实验结果显示，gSMILE在多个领先的大语言模型上表现出色，尤其是Claude 2.1在注意力保真度方面表现优异，而GPT-3.5则在输出一致性上达到最高水平。这表明gSMILE能够有效平衡模型性能与可解释性。

## 🎯 应用场景

gSMILE的潜在应用领域包括金融、医疗和法律等高风险行业，在这些领域中，模型的可解释性至关重要。通过提高大语言模型的透明度，gSMILE能够帮助决策者理解模型的推理过程，从而增强信任和问责。未来，gSMILE可能会在更多领域推广，促进AI系统的透明性和可靠性。

## 📄 摘要（原文）

> Large Language Models (LLMs) such as GPT, LLaMA, and Claude achieve remarkable performance in text generation but remain opaque in their decision-making processes, limiting trust and accountability in high-stakes applications. We present gSMILE (generative SMILE), a model-agnostic, perturbation-based framework for token-level interpretability in LLMs. Extending the SMILE methodology, gSMILE uses controlled prompt perturbations, Wasserstein distance metrics, and weighted linear surrogates to identify input tokens with the most significant impact on the output. This process enables the generation of intuitive heatmaps that visually highlight influential tokens and reasoning paths. We evaluate gSMILE across leading LLMs (OpenAI's gpt-3.5-turbo-instruct, Meta's LLaMA 3.1 Instruct Turbo, and Anthropic's Claude 2.1) using attribution fidelity, attribution consistency, attribution stability, attribution faithfulness, and attribution accuracy as metrics. Results show that gSMILE delivers reliable human-aligned attributions, with Claude 2.1 excelling in attention fidelity and GPT-3.5 achieving the highest output consistency. These findings demonstrate gSMILE's ability to balance model performance and interpretability, enabling more transparent and trustworthy AI systems.

