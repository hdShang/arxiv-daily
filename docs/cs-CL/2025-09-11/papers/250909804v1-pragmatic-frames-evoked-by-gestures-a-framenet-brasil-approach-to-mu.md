---
layout: default
title: "Pragmatic Frames Evoked by Gestures: A FrameNet Brasil Approach to Multimodality in Turn Organization"
---

# Pragmatic Frames Evoked by Gestures: A FrameNet Brasil Approach to Multimodality in Turn Organization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09804" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09804v1</a>
  <a href="https://arxiv.org/pdf/2509.09804.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09804v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09804v1', 'Pragmatic Frames Evoked by Gestures: A FrameNet Brasil Approach to Multimodality in Turn Organization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Helen de Andrade Abreu, Tiago Timponi Torrent, Ely Edison da Silva Matos

**分类**: cs.CL

**发布日期**: 2025-09-11

**备注**: Paper submitted to Language Sciences Journal

---

## 💡 一句话要点

**提出基于语用框架的多模态对话轮次组织建模方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态对话` `对话轮次组织` `语用框架` `手势识别` `人机交互`

## 📋 核心要点

1. 现有对话轮次组织研究缺乏对交流者手势策略的编码数据集，限制了机器学习的应用。
2. 论文提出基于语用框架，关联语言和交互手势，建模多模态对话轮次组织。
3. 通过Frame2数据集验证，证实手势在对话轮次中的作用，并发现新的手势变体。

## 📝 摘要（中文）

本文提出了一个框架，用于通过语言和交互手势之间的相关性来建模多模态对话轮次组织，该框架基于对语用框架如何被交流者概念化和唤起的分析。为了提供分析的证据，我们开发了一种注释方法，用语用框架来丰富一个多模态数据集（已标注语义框架），该框架对对话轮次组织进行建模。尽管对话轮次组织已被不同领域的研究人员研究过，但具体的策略，特别是交流者使用的手势，尚未被编码到一个可用于机器学习的数据集中。为了填补这一空白，我们使用用于轮次组织的手势注释丰富了Frame2数据集。Frame2数据集包含来自巴西电视剧Pedro Pelo Mundo的10集，这些剧集被注释了视频和文本中唤起的语义框架。这个数据集使我们能够密切观察交流者如何在实验室之外的场景中使用交互手势，据我们所知，这些场景以前没有在相关文献中记录过。我们的结果证实，参与面对面交流的交流者使用手势作为传递、获取和保持对话轮次的工具，并且还揭示了一些以前未被记录的手势变体。我们认为，这些手势的使用源于语用框架的概念化，包括心理空间、混合和概念隐喻。此外，我们的数据表明，语用框架的注释有助于更深入地理解人类认知和语言。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态对话中，如何利用手势理解和建模对话轮次组织的问题。现有方法主要集中在语言层面，忽略了手势等非语言信息在对话中的重要作用，缺乏可用于机器学习的手势标注数据集。

**核心思路**：论文的核心思路是将对话轮次组织与语用框架联系起来，认为手势是语用框架概念化的体现。通过分析手势如何唤起和传递语用信息，从而理解对话轮次的转移、保持和获取。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 选择Frame2数据集，该数据集包含巴西电视剧的视频和文本，并已标注语义框架。2) 设计一套新的注释方法，用于标注数据集中与对话轮次组织相关的手势。3) 分析标注后的数据，研究手势与语用框架之间的关系，以及手势在对话轮次中的作用。4) 验证手势在传递、获取和保持对话轮次中的作用，并发现新的手势变体。

**关键创新**：论文的关键创新在于：1) 提出了基于语用框架的多模态对话轮次组织建模方法，将手势纳入对话理解的范畴。2) 构建了一个包含手势标注的多模态数据集，为机器学习提供了数据基础。3) 发现了新的手势变体，丰富了对话行为的研究。

**关键设计**：论文的关键设计包括：1) 语用框架的定义和选择，需要根据具体的对话场景进行调整。2) 手势标注的细粒度，需要平衡标注的准确性和效率。3) 数据分析的方法，需要结合统计分析和案例分析，才能深入理解手势的作用。

## 📊 实验亮点

研究结果表明，交流者在面对面交流中利用手势传递、获取和保持对话轮次。通过对Frame2数据集的分析，发现了以前未被记录的手势变体，证实了语用框架注释有助于更深入地理解人类认知和语言。

## 🎯 应用场景

该研究成果可应用于智能对话系统、人机交互、虚拟助手等领域。通过理解手势在对话中的作用，可以提升对话系统的自然性和流畅性，改善用户体验。未来，该研究还可以扩展到其他非语言行为的分析，构建更完善的多模态对话模型。

## 📄 摘要（原文）

> This paper proposes a framework for modeling multimodal conversational turn organization via the proposition of correlations between language and interactive gestures, based on analysis as to how pragmatic frames are conceptualized and evoked by communicators. As a means to provide evidence for the analysis, we developed an annotation methodology to enrich a multimodal dataset (annotated for semantic frames) with pragmatic frames modeling conversational turn organization. Although conversational turn organization has been studied by researchers from diverse fields, the specific strategies, especially gestures used by communicators, had not yet been encoded in a dataset that can be used for machine learning. To fill this gap, we enriched the Frame2 dataset with annotations of gestures used for turn organization. The Frame2 dataset features 10 episodes from the Brazilian TV series Pedro Pelo Mundo annotated for semantic frames evoked in both video and text. This dataset allowed us to closely observe how communicators use interactive gestures outside a laboratory, in settings, to our knowledge, not previously recorded in related literature. Our results have confirmed that communicators involved in face-to-face conversation make use of gestures as a tool for passing, taking and keeping conversational turns, and also revealed variations of some gestures that had not been documented before. We propose that the use of these gestures arises from the conceptualization of pragmatic frames, involving mental spaces, blending and conceptual metaphors. In addition, our data demonstrate that the annotation of pragmatic frames contributes to a deeper understanding of human cognition and language.

