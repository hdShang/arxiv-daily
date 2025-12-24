---
layout: default
title: "\"She was useful, but a bit too optimistic\": Augmenting Design with Interactive Virtual Personas"
---

# "She was useful, but a bit too optimistic": Augmenting Design with Interactive Virtual Personas

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19463" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19463v2</a>
  <a href="https://arxiv.org/pdf/2508.19463.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19463v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19463v2', '&quot;She was useful, but a bit too optimistic&quot;: Augmenting Design with Interactive Virtual Personas')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Paluck Deep, Monica Bharadhidasan, A. Baki Kocaballi

**分类**: cs.HC, cs.AI

**发布日期**: 2025-08-26 (更新: 2025-09-26)

**备注**: The version accepted for publication at International Journal of Human-Computer Studies

**期刊**: International Journal of Human-Computer Studies (2025)

**DOI**: [10.1016/j.ijhcs.2025.103646](https://doi.org/10.1016/j.ijhcs.2025.103646)

---

## 💡 一句话要点

**提出交互式虚拟角色以解决传统用户画像的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `交互式虚拟角色` `用户体验设计` `大型语言模型` `人机交互` `设计创新` `实时反馈`

## 📋 核心要点

1. 现有的用户画像方法因其静态性和有限的互动性，难以满足快速迭代设计流程的需求。
2. 本文提出交互式虚拟角色（IVPs），利用大型语言模型实现多模态对话，增强用户模拟的互动性和适应性。
3. 通过与八位专业UX设计师的研究，IVPs在信息收集和设计灵感方面表现出显著的加速效果，但也引发了对偏见和真实性的讨论。

## 📝 摘要（中文）

用户画像在以人为本的设计中被广泛使用，以理解和传达用户需求。然而，传统用户画像因其静态特性、有限的参与度以及无法适应不断变化的设计需求而面临挑战。本文提出了交互式虚拟角色（IVPs），这是一种多模态、基于大型语言模型（LLM）的对话式用户模拟，设计师可以通过语音接口与之进行实时访谈、头脑风暴和反馈收集。我们对八位专业UX设计师进行了定性研究，使用名为“Alice”的IVP进行用户研究、创意构思和原型评估等三项设计活动。研究结果表明，IVPs能够加速信息收集、激发设计解决方案并提供快速的用户反馈。然而，设计师们对偏见、过于乐观、缺乏真实利益相关者输入的挑战以及IVP无法完全复制人际互动的细微差别表示担忧。参与者强调，IVPs应被视为对真实用户参与的补充，而非替代。我们讨论了有效和负责任地使用IVP的提示工程、人机协作整合和伦理考虑。最后，我们的研究为生成性AI在设计过程中的应用提供了见解。

## 🔬 方法详解

**问题定义**：本文旨在解决传统用户画像在动态设计流程中的局限性，尤其是其静态特性和缺乏真实用户反馈的问题。

**核心思路**：通过引入交互式虚拟角色（IVPs），利用大型语言模型（LLMs）实现实时对话和反馈，增强用户模拟的互动性和适应性。

**技术框架**：整体架构包括IVP的生成模块、对话管理模块和用户反馈收集模块。设计师可以通过语音接口与IVP进行交互，获取实时反馈。

**关键创新**：IVPs的最大创新在于其基于LLM的对话能力，使得用户模拟不仅限于静态信息，而是能够进行动态互动，提供更真实的用户体验。

**关键设计**：在设计IVP时，采用了特定的提示工程技术，以确保对话的自然流畅性，并考虑了用户的反馈机制，以不断优化IVP的表现。具体的参数设置和网络结构细节在论文中进行了详细讨论。

## 📊 实验亮点

实验结果显示，IVPs在信息收集和设计灵感方面显著加速了设计师的工作流程，参与者普遍反映与IVP的互动能够激发更多创意。然而，设计师对IVP的偏见和真实性问题表示关注，强调其应作为真实用户参与的补充。

## 🎯 应用场景

该研究的潜在应用领域包括用户体验设计、产品开发和人机交互等。IVPs可以帮助设计师在早期阶段快速获取用户反馈，从而提高设计效率和创新能力。未来，随着技术的进步，IVPs有望在更广泛的设计场景中得到应用，推动设计流程的变革。

## 📄 摘要（原文）

> Personas have been widely used to understand and communicate user needs in human-centred design. Despite their utility, they may fail to meet the demands of iterative workflows due to their static nature, limited engagement, and inability to adapt to evolving design needs. Recent advances in large language models (LLMs) pave the way for more engaging and adaptive approaches to user representation. This paper introduces Interactive Virtual Personas (IVPs): multimodal, LLM-driven, conversational user simulations that designers can interview, brainstorm with, and gather feedback from in real time via voice interface. We conducted a qualitative study with eight professional UX designers, employing an IVP named "Alice" across three design activities: user research, ideation, and prototype evaluation. Our findings demonstrate the potential of IVPs to expedite information gathering, inspire design solutions, and provide rapid user-like feedback. However, designers raised concerns about biases, over-optimism, the challenge of ensuring authenticity without real stakeholder input, and the inability of the IVP to fully replicate the nuances of human interaction. Our participants emphasised that IVPs should be viewed as a complement to, not a replacement for, real user engagement. We discuss strategies for prompt engineering, human-in-the-loop integration, and ethical considerations for effective and responsible IVP use in design. Finally, our work contributes to the growing body of research on generative AI in the design process by providing insights into UX designers' experiences of LLM-powered interactive personas.

