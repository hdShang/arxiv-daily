---
layout: default
title: Pragmatic Inference for Moral Reasoning Acquisition: Generalization via Distributional Semantics
---

# Pragmatic Inference for Moral Reasoning Acquisition: Generalization via Distributional Semantics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24102" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24102</a>
  <a href="https://arxiv.org/pdf/2509.24102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24102" onclick="toggleFavorite(this, '2509.24102', 'Pragmatic Inference for Moral Reasoning Acquisition: Generalization via Distributional Semantics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangliang Liu, Xi Chen, Bocheng Chen, Han Zi, Xitong Zhang, Kristen Johnson

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于语用推理的道德推理获取方法，提升LLM的道德推理泛化能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `道德推理` `大型语言模型` `语用推理` `道德基础理论` `泛化能力`

## 📋 核心要点

1. 大型语言模型在道德推理方面面临泛化难题，因为它们主要依赖于分布语义，而道德判断更多依赖于语用推理。
2. 论文提出基于道德基础理论的语用推理方法，通过利用上下文信息弥合分布语义和语用之间的差距。
3. 实验结果表明，该方法显著提升了大型语言模型在道德推理任务中的泛化能力，为后续研究奠定基础。

## 📝 摘要（中文）

道德推理已成为大型语言模型（LLMs）一个很有前景的研究方向，但实现泛化仍然是一个核心挑战。从语言学角度来看，这种困难的出现是因为LLMs擅长捕捉分布语义，而分布语义从根本上不同于在语用层面运作的道德。本文研究了LLMs如何在依赖分布语义的情况下实现广义的道德推理。我们提出了基于道德基础理论的语用推理方法，该方法利用每个步骤的上下文信息来弥合语用差距，并指导LLMs将道德基础与道德推理目标联系起来。实验结果表明，我们的方法显著提高了LLMs在道德推理中的泛化能力，为未来基于道德基础理论的研究奠定了基础。

## 🔬 方法详解

**问题定义**：当前大型语言模型在道德推理方面表现出一定的能力，但其泛化能力不足。主要原因是LLMs主要依赖于从大量文本数据中学习到的分布语义，而道德判断往往涉及到更深层次的语用推理，即需要结合上下文信息进行理解和判断。现有方法难以有效弥合分布语义和语用推理之间的差距，导致模型在面对新的道德场景时表现不佳。

**核心思路**：论文的核心思路是利用道德基础理论（Moral Foundations Theory）作为桥梁，将分布语义和语用推理联系起来。道德基础理论提供了一套通用的道德价值观框架，可以帮助模型更好地理解和推理不同场景下的道德含义。通过在推理过程中显式地考虑道德基础，模型可以更好地捕捉上下文信息，从而做出更合理的道德判断。

**技术框架**：该方法主要包含以下几个阶段：1) 输入道德场景描述；2) 利用道德基础理论，提取与场景相关的道德基础信息；3) 将道德基础信息与场景描述结合，作为LLM的输入；4) LLM进行道德推理，输出判断结果。整个框架的关键在于如何有效地提取和利用道德基础信息，并将其融入到LLM的推理过程中。

**关键创新**：论文的关键创新在于将道德基础理论引入到LLM的道德推理过程中，并提出了一种基于语用推理的方法，有效地弥合了分布语义和语用推理之间的差距。与现有方法相比，该方法能够更好地捕捉上下文信息，从而提高LLM在道德推理任务中的泛化能力。

**关键设计**：论文的关键设计包括：1) 如何将道德基础理论表示为可供LLM理解的向量形式；2) 如何设计损失函数，使得LLM能够更好地学习道德基础和道德判断之间的关系；3) 如何选择合适的LLM架构，以充分利用道德基础信息进行推理。具体的参数设置和网络结构细节在论文中可能有所描述，但摘要中未明确提及。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.24102/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.24102/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.24102/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法显著提高了LLMs在道德推理任务中的泛化能力。具体的性能数据、对比基线和提升幅度在摘要中未明确给出，但强调了该方法为未来基于道德基础理论的研究奠定了基础。具体提升效果未知。

## 🎯 应用场景

该研究成果可应用于开发更具道德意识的人工智能系统，例如自动驾驶汽车、医疗诊断系统和法律咨询系统。通过提升机器的道德推理能力，可以使其在复杂场景下做出更符合伦理道德的决策，从而更好地服务于人类社会。此外，该研究还可以促进人机交互的和谐发展，增强用户对人工智能系统的信任感。

## 📄 摘要（原文）

> Moral reasoning has emerged as a promising research direction for Large Language Models (LLMs), yet achieving generalization remains a central challenge. From a linguistic standpoint, this difficulty arises because LLMs are adept at capturing distributional semantics, which fundamentally differs from the morals which operate at the pragmatic level. This paper investigates how LLMs can achieve generalized moral reasoning despite their reliance on distributional semantics. We propose pragmatic inference methods grounded in moral foundations theory, which leverage contextual information at each step to bridge the pragmatic gap and guide LLMs in connecting moral foundations with moral reasoning objectives. Experimental results demonstrate that our approach significantly enhances LLMs' generalization in moral reasoning, providing a foundation for future research grounded in moral foundations theory.

