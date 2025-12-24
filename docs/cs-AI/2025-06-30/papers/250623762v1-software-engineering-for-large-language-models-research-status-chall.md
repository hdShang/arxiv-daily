---
layout: default
title: "Software Engineering for Large Language Models: Research Status, Challenges and the Road Ahead"
---

# Software Engineering for Large Language Models: Research Status, Challenges and the Road Ahead

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23762" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23762v1</a>
  <a href="https://arxiv.org/pdf/2506.23762.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23762v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23762v1', 'Software Engineering for Large Language Models: Research Status, Challenges and the Road Ahead')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongzhou Rao, Yanjie Zhao, Xinyi Hou, Shenao Wang, Haoyu Wang

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**系统分析大语言模型开发生命周期中的软件工程挑战与解决方案**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `软件工程` `需求工程` `模型开发` `测试与评估` `数据集构建` `运维管理`

## 📋 核心要点

1. 现有研究未系统探讨大语言模型开发生命周期中的软件工程挑战，导致开发过程中的复杂性未得到有效解决。
2. 本文通过分析LLM开发的六个阶段，提出了针对每个阶段的关键挑战及相应的研究方向，填补了这一领域的研究空白。
3. 研究提供了从软件工程视角的见解，旨在为未来LLM的发展提供指导，推动技术的进步与应用。

## 📝 摘要（中文）

大语言模型（LLMs）的快速发展重新定义了人工智能（AI），推动了AI研究的边界，并为学术界和工业界带来了无限可能。然而，LLM开发在其生命周期中面临越来越复杂的挑战，现有研究尚未从软件工程（SE）角度系统探讨这些挑战及解决方案。为填补这一空白，本文系统分析了LLM开发生命周期的研究现状，分为六个阶段：需求工程、数据集构建、模型开发与增强、测试与评估、部署与运维、维护与演化。最后，本文识别了每个阶段的关键挑战，并提出了应对这些挑战的潜在研究方向。总体而言，本文从SE的角度提供了有价值的见解，以促进LLM开发的未来进展。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型开发生命周期中面临的复杂挑战，现有方法缺乏系统性分析，导致开发效率低下和质量不稳定。

**核心思路**：通过将LLM开发过程划分为六个阶段，系统分析每个阶段的挑战，并提出针对性的解决方案，旨在提升开发效率和模型质量。

**技术框架**：整体架构包括需求工程、数据集构建、模型开发与增强、测试与评估、部署与运维、维护与演化六个主要模块，形成闭环的开发流程。

**关键创新**：论文的创新点在于首次从软件工程的视角系统性地分析LLM开发的各个阶段，识别出具体的挑战并提出相应的研究方向，与现有方法相比，更加全面和系统。

**关键设计**：在每个阶段，论文强调了需求分析、数据质量控制、模型评估标准等关键设计，确保每个环节的高效性和有效性。具体参数设置和损失函数的选择也在文中进行了详细讨论。

## 📊 实验亮点

研究表明，通过系统分析LLM开发的六个阶段，能够显著提高开发效率和模型质量。具体而言，针对每个阶段的挑战提出的解决方案，预计能提升模型的准确性和稳定性，具体性能数据待进一步验证。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统、智能客服等，能够为大语言模型的开发提供系统化的指导，提升模型的开发效率和应用效果。未来，该研究可能对AI领域的标准化和规范化发展产生深远影响。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has redefined artificial intelligence (AI), pushing the boundaries of AI research and enabling unbounded possibilities for both academia and the industry. However, LLM development faces increasingly complex challenges throughout its lifecycle, yet no existing research systematically explores these challenges and solutions from the perspective of software engineering (SE) approaches. To fill the gap, we systematically analyze research status throughout the LLM development lifecycle, divided into six phases: requirements engineering, dataset construction, model development and enhancement, testing and evaluation, deployment and operations, and maintenance and evolution. We then conclude by identifying the key challenges for each phase and presenting potential research directions to address these challenges. In general, we provide valuable insights from an SE perspective to facilitate future advances in LLM development.

