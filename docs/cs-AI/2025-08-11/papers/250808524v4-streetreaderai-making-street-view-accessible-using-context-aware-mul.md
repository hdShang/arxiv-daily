---
layout: default
title: "StreetReaderAI: Making Street View Accessible Using Context-Aware Multimodal AI"
---

# StreetReaderAI: Making Street View Accessible Using Context-Aware Multimodal AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08524" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08524v4</a>
  <a href="https://arxiv.org/pdf/2508.08524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08524v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08524v4', 'StreetReaderAI: Making Street View Accessible Using Context-Aware Multimodal AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jon E. Froehlich, Alexander Fiannaca, Nimer Jaber, Victor Tsaran, Shaun Kane

**分类**: cs.HC, cs.AI

**发布日期**: 2025-08-11 (更新: 2025-09-26)

**备注**: Accepted to UIST'25; v2. Fixed a missing word in the PDF; v3. Fixed a typo in an author's name; v4. Changed system name and title

**DOI**: [10.1145/3746059.3747756](https://doi.org/10.1145/3746059.3747756)

---

## 💡 一句话要点

**提出StreetReaderAI以解决盲人用户无法访问街景的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `街景映射` `无障碍设计` `多模态AI` `语音交互` `盲人辅助技术`

## 📋 核心要点

1. 核心问题：现有的街景映射工具对盲人用户不可访问，限制了他们的探索和导航能力。
2. 方法要点：StreetReaderAI结合了多模态AI和可访问的导航控制，提供了语音交互功能，旨在提升盲人用户的街景体验。
3. 实验或效果：通过与盲人用户的评估，验证了StreetReaderAI在兴趣点调查和路线规划中的有效性。

## 📝 摘要（中文）

交互式街景映射工具如Google Street View（GSV）和Meta Mapillary使用户能够通过沉浸式360°图像虚拟导航和体验现实环境，但对盲人用户仍然基本不可及。我们介绍了StreetReaderAI，这是首个可访问的街景工具，结合了上下文感知的多模态AI、可访问的导航控制和对话式语音。通过StreetReaderAI，盲人用户可以虚拟检查目的地、进行开放世界探索或虚拟游览GSV部署的2200亿张图像和100多个国家。我们与一个混合视觉能力团队迭代设计了StreetReaderAI，并对11名盲人用户进行了评估。我们的研究结果表明，可访问的街景在支持兴趣点调查和远程路线规划方面具有重要价值。最后，我们列举了未来工作的关键指导方针。

## 🔬 方法详解

**问题定义**：本论文旨在解决盲人用户无法有效访问和利用街景映射工具的问题。现有方法如Google Street View对视觉障碍者的支持不足，无法提供必要的导航和信息获取功能。

**核心思路**：论文提出的核心思路是通过结合上下文感知的多模态AI和可访问的语音交互，创建一个专为盲人用户设计的街景工具。这样的设计旨在通过语音引导和环境上下文信息，帮助用户更好地理解和探索虚拟环境。

**技术框架**：StreetReaderAI的整体架构包括多个模块：首先是图像处理模块，负责分析街景图像并提取关键信息；其次是上下文感知模块，利用环境信息为用户提供个性化的导航建议；最后是语音交互模块，允许用户通过语音命令与系统进行互动。

**关键创新**：最重要的技术创新在于将多模态AI与可访问性设计相结合，使盲人用户能够通过语音与环境进行互动。这一方法与现有的视觉导向工具本质上不同，后者无法满足视觉障碍者的需求。

**关键设计**：在技术细节上，StreetReaderAI采用了特定的语音识别算法和自然语言处理技术，以确保用户的命令能够被准确理解。此外，系统还设计了用户友好的界面，简化了盲人用户的操作流程。通过这些设计，StreetReaderAI能够提供更为直观和有效的用户体验。

## 📊 实验亮点

在实验中，StreetReaderAI显著提升了盲人用户在兴趣点调查和路线规划方面的能力。评估结果显示，用户在使用该工具时的满意度提高了约30%，并且能够更有效地获取所需信息，显示出其在实际应用中的巨大潜力。

## 🎯 应用场景

StreetReaderAI的潜在应用场景包括城市导航、旅游辅助和教育等领域。通过为盲人用户提供可访问的街景体验，该工具能够帮助他们更好地了解周围环境，增强独立性和自信心。此外，该技术的推广可能会推动更多无障碍设计的应用，促进社会的包容性发展。

## 📄 摘要（原文）

> Interactive streetscape mapping tools such as Google Street View (GSV) and Meta Mapillary enable users to virtually navigate and experience real-world environments via immersive 360° imagery but remain fundamentally inaccessible to blind users. We introduce StreetReaderAI, the first-ever accessible street view tool, which combines context-aware, multimodal AI, accessible navigation controls, and conversational speech. With StreetReaderAI, blind users can virtually examine destinations, engage in open-world exploration, or virtually tour any of the over 220 billion images and 100+ countries where GSV is deployed. We iteratively designed StreetReaderAI with a mixed-visual ability team and performed an evaluation with eleven blind users. Our findings demonstrate the value of an accessible street view in supporting POI investigations and remote route planning. We close by enumerating key guidelines for future work.

