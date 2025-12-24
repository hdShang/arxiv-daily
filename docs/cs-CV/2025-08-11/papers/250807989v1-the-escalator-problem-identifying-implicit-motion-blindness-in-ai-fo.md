---
layout: default
title: "The Escalator Problem: Identifying Implicit Motion Blindness in AI for Accessibility"
---

# The Escalator Problem: Identifying Implicit Motion Blindness in AI for Accessibility

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07989" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07989v1</a>
  <a href="https://arxiv.org/pdf/2508.07989.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07989v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07989v1', 'The Escalator Problem: Identifying Implicit Motion Blindness in AI for Accessibility')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiantao Zhang

**分类**: cs.CV, cs.HC

**发布日期**: 2025-08-11

**备注**: 9 pages, 3 figures, 2 tables. Accepted at CV4A11y, ICCV 2025

---

## 💡 一句话要点

**提出隐性运动失明问题以提升辅助技术的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `隐性运动失明` `自动扶梯问题` `动态环境感知` `用户信任` `辅助技术` `物理感知` `基准测试`

## 📋 核心要点

1. 现有的多模态大型语言模型在处理动态场景时存在隐性运动失明问题，无法准确感知自动扶梯的运动方向。
2. 论文提出通过转变研究范式，强调从语义识别向物理感知的转变，以解决现有模型的局限性。
3. 作为立场论文，未提供新模型，而是分析了隐性运动失明对用户信任的影响，并呼吁开发新的基准测试。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在为盲人和视障人士提供辅助技术方面具有巨大潜力。然而，本文指出了一个关键的失效模式，即无法感知自动扶梯的运动方向，这被称为“自动扶梯问题”。这种失明源于视频理解中的主流帧采样范式，导致模型在感知连续、低信号运动时存在根本性困难。作为一篇立场论文，我们的贡献在于正式阐述这一盲点，分析其对用户信任的影响，并呼吁采取行动，倡导从纯语义识别转向稳健的物理感知，发展以人为本的基准，优先考虑动态环境中的安全性、可靠性和用户的真实需求。

## 🔬 方法详解

**问题定义**：本文要解决的问题是现有多模态大型语言模型在动态场景下的隐性运动失明，特别是无法感知自动扶梯的运动方向。现有方法主要依赖于帧采样，导致对连续运动的感知能力不足。

**核心思路**：论文的核心思路是提出“隐性运动失明”这一概念，强调需要从语义识别转向物理感知，以提高模型在动态环境中的可靠性和安全性。

**技术框架**：整体架构包括对现有模型的分析、用户信任的影响评估以及对未来研究方向的建议。主要模块包括对隐性运动失明的定义、影响分析和基准测试的呼吁。

**关键创新**：最重要的技术创新点在于提出了隐性运动失明这一新概念，并系统性地分析了其对用户信任的影响，这与现有方法的关注点有本质区别。

**关键设计**：论文中没有具体的模型设计或参数设置，而是提出了对现有研究方法的批判性分析，强调需要建立新的以人为本的基准测试。通过这种方式，推动研究者关注动态环境中的安全性和可靠性。

## 📊 实验亮点

论文通过分析隐性运动失明问题，强调了现有多模态大型语言模型在动态场景中的局限性。虽然未提供具体实验数据，但提出的概念和分析为未来研究指明了方向，呼吁开发新的基准测试以提高模型的可靠性和安全性。

## 🎯 应用场景

该研究的潜在应用领域包括辅助技术、智能交通系统和机器人导航等。通过提升模型对动态环境的感知能力，可以为盲人和视障人士提供更安全、可靠的辅助工具，改善他们的生活质量。未来，随着技术的进步，这一研究可能会影响更广泛的智能系统设计，确保其在复杂环境中的有效性和安全性。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) hold immense promise as assistive technologies for the blind and visually impaired (BVI) community. However, we identify a critical failure mode that undermines their trustworthiness in real-world applications. We introduce the Escalator Problem -- the inability of state-of-the-art models to perceive an escalator's direction of travel -- as a canonical example of a deeper limitation we term Implicit Motion Blindness. This blindness stems from the dominant frame-sampling paradigm in video understanding, which, by treating videos as discrete sequences of static images, fundamentally struggles to perceive continuous, low-signal motion. As a position paper, our contribution is not a new model but rather to: (I) formally articulate this blind spot, (II) analyze its implications for user trust, and (III) issue a call to action. We advocate for a paradigm shift from purely semantic recognition towards robust physical perception and urge the development of new, human-centered benchmarks that prioritize safety, reliability, and the genuine needs of users in dynamic environments.

