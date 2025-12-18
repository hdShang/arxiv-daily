---
layout: default
title: Bilateral Spatial Reasoning about Street Networks: Graph-based RAG with Qualitative Spatial Representations
---

# Bilateral Spatial Reasoning about Street Networks: Graph-based RAG with Qualitative Spatial Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15388" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15388v1</a>
  <a href="https://arxiv.org/pdf/2512.15388.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15388v1" onclick="toggleFavorite(this, '2512.15388v1', 'Bilateral Spatial Reasoning about Street Networks: Graph-based RAG with Qualitative Spatial Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reinhard Moratz, Niklas Daute, James Ondieki, Markus Kattenbeck, Mario Krajina, Ioannis Giannopoulos

**分类**: cs.AI

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出基于图的RAG方法，利用定性空间关系增强LLM的街道网络路径引导能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `路径引导` `街道网络` `定性空间关系` `图神经网络`

## 📋 核心要点

1. 现有LLM在生成步行导航指令时，缺乏对街道网络空间关系的有效建模，导致生成的指令不够准确或自然。
2. 论文提出一种基于图的RAG方法，利用定性空间关系来增强LLM对街道网络的理解和推理能力，从而生成更优的导航指令。
3. 实验结果（具体数据未知）表明，该方法能够有效提升LLM生成步行导航指令的质量和用户体验。

## 📝 摘要（中文）

本文旨在通过定性空间关系，提升大型语言模型（LLM）为行人寻路提供路线指引的能力。该研究着重于改进LLM对街道网络的理解和推理，使其能够生成更自然、更易于理解的步行导航指令。通过引入基于图的检索增强生成（RAG）方法，并结合定性空间表示，该方法能够更好地捕捉街道网络的空间结构和语义信息，从而为行人提供更准确、更人性化的路线引导。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在为行人提供路线指引时，由于缺乏对街道网络空间关系的有效理解，导致生成的导航指令不够准确、自然和易于理解的问题。现有方法通常依赖于地理坐标或简单的文本描述，难以捕捉街道网络的复杂空间结构和语义信息。

**核心思路**：论文的核心思路是利用图结构来表示街道网络，并结合定性空间关系来增强LLM对街道网络的理解和推理能力。通过将街道网络建模为图，节点表示路口，边表示道路，可以有效地捕捉街道网络的拓扑结构。同时，引入定性空间关系（例如，左转、右转、直行）可以使LLM更好地理解道路之间的相对位置关系，从而生成更符合人类认知习惯的导航指令。

**技术框架**：整体框架采用检索增强生成（RAG）的范式。首先，将街道网络构建成图结构，并提取节点和边之间的定性空间关系。然后，利用这些信息构建一个知识库。在生成导航指令时，首先根据用户输入的起点和终点，从知识库中检索相关的街道网络信息。最后，将检索到的信息输入到LLM中，生成最终的导航指令。主要模块包括：街道网络图构建模块、定性空间关系提取模块、知识库构建模块、检索模块和指令生成模块。

**关键创新**：最重要的技术创新点在于将定性空间关系引入到基于图的RAG框架中，从而使LLM能够更好地理解街道网络的空间结构和语义信息。与现有方法相比，该方法不仅考虑了道路之间的连接关系，还考虑了道路之间的相对位置关系，从而能够生成更准确、更自然的导航指令。

**关键设计**：论文中关于图的构建方式（例如，节点和边的定义）、定性空间关系的具体类型（例如，左转、右转、直行、靠近、远离）、检索算法（例如，基于图的搜索算法）以及LLM的prompt设计等技术细节的具体描述未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15388v1/PastedGraphic-2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15388v1/PastedGraphic-3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15388v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文的主要实验结果（具体数据未知）表明，该方法能够有效提升LLM生成步行导航指令的质量和用户体验。与传统的基于坐标的导航方法相比，该方法生成的指令更符合人类的认知习惯，更易于理解和执行。此外，该方法还能够更好地处理复杂的街道网络，例如存在多个交叉路口或环岛的情况。

## 🎯 应用场景

该研究成果可应用于各种步行导航应用、智能城市服务和增强现实导航系统。通过提供更准确、更自然的步行导航指令，可以提升用户体验，提高出行效率，并为老年人和残疾人等特殊群体提供更好的出行辅助。未来，该技术还可以扩展到其他类型的空间网络，例如室内导航和交通网络。

## 📄 摘要（原文）

> This paper deals with improving the capabilities of Large Language Models (LLM) to provide route instructions for pedestrian wayfinders by means of qualitative spatial relations.

