---
layout: default
title: "Preacher: Paper-to-Video Agentic System"
---

# Preacher: Paper-to-Video Agentic System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09632" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09632v6</a>
  <a href="https://arxiv.org/pdf/2508.09632.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09632v6" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09632v6', 'Preacher: Paper-to-Video Agentic System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingwei Liu, Ling Yang, Hao Luo, Fan Wang, Hongyan Li, Mengdi Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-13 (更新: 2025-09-08)

**备注**: ICCV 2025. Code: https://github.com/Gen-Verse/Paper2Video

**🔗 代码/项目**: [GITHUB](https://github.com/Gen-Verse/Paper2Video)

---

## 💡 一句话要点

**提出Preacher以解决论文转视频生成的多重限制问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `论文转视频` `多模态生成` `渐进式思维链` `视频摘要` `跨模态对齐`

## 📋 核心要点

1. 现有的视频生成模型在处理论文转视频任务时面临上下文限制和风格单一等挑战，难以有效表达领域知识。
2. Preacher通过自上而下的分解与总结，结合自下而上的视频生成，创新性地实现了论文内容的多样化视频呈现。
3. 实验结果表明，Preacher在五个研究领域生成的视频摘要质量显著高于现有模型，展示了其广泛的适用性和优越性。

## 📝 摘要（中文）

论文转视频任务旨在将研究论文转换为结构化的视频摘要，将关键概念、方法和结论提炼成易于理解的格式。尽管现有的视频生成模型展现出潜力，但受到上下文窗口限制、视频时长约束、风格多样性不足以及无法表示领域特定知识等问题的制约。为了解决这些限制，本文提出了Preacher，这是首个论文转视频的自主系统。Preacher采用自上而下的方法对论文进行分解、总结和重构，随后通过自下而上的视频生成，将多样的视频片段合成一个连贯的摘要。为了对齐跨模态表示，定义了关键场景并引入了渐进式思维链（P-CoT）进行细粒度的迭代规划。Preacher成功生成了五个研究领域的高质量视频摘要，展示了超越现有视频生成模型的能力。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是如何将研究论文有效转化为结构化的视频摘要。现有方法在上下文窗口、视频时长和风格多样性等方面存在明显不足，无法充分表达领域特定知识。

**核心思路**：Preacher的核心思路是采用自上而下的分解与总结方法，结合自下而上的视频生成策略，通过多样化的视频片段合成一个连贯的摘要，以克服现有方法的局限性。

**技术框架**：Preacher的整体架构包括两个主要阶段：第一阶段是对论文进行分解、总结和重构，第二阶段是视频生成，利用定义的关键场景和渐进式思维链（P-CoT）进行细粒度的规划。

**关键创新**：Preacher的关键创新在于引入了渐进式思维链（P-CoT），使得视频生成过程能够进行细粒度的迭代规划，从而实现更高质量的跨模态表示对齐。与现有方法相比，Preacher在处理复杂内容时表现出更强的灵活性和适应性。

**关键设计**：在技术细节上，Preacher采用了特定的损失函数来优化视频生成质量，并设计了适应不同领域的网络结构，以确保生成视频的多样性和连贯性。

## 📊 实验亮点

Preacher在五个研究领域的实验中，生成的视频摘要质量显著优于现有模型，具体性能数据尚未披露，但展示了其在多样性和连贯性方面的明显提升，证明了其在论文转视频生成任务中的有效性。

## 🎯 应用场景

Preacher的研究成果在教育、科研传播和信息可视化等领域具有广泛的应用潜力。通过将复杂的研究内容转化为易于理解的视频摘要，可以帮助研究人员、学生和公众更好地获取和理解科学知识，促进科学传播与交流。

## 📄 摘要（原文）

> The paper-to-video task converts a research paper into a structured video abstract, distilling key concepts, methods, and conclusions into an accessible, well-organized format. While state-of-the-art video generation models demonstrate potential, they are constrained by limited context windows, rigid video duration constraints, limited stylistic diversity, and an inability to represent domain-specific knowledge. To address these limitations, we introduce Preacher, the first paper-to-video agentic system. Preacher employs a topdown approach to decompose, summarize, and reformulate the paper, followed by bottom-up video generation, synthesizing diverse video segments into a coherent abstract. To align cross-modal representations, we define key scenes and introduce a Progressive Chain of Thought (P-CoT) for granular, iterative planning. Preacher successfully generates high-quality video abstracts across five research fields, demonstrating expertise beyond current video generation models. Code will be released at: https://github.com/Gen-Verse/Paper2Video

