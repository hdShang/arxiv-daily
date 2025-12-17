---
layout: default
title: Team Xiaomi EV-AD VLA: Caption-Guided Retrieval System for Cross-Modal Drone Navigation -- Technical Report for IROS 2025 RoboSense Challenge Track 4
---

# Team Xiaomi EV-AD VLA: Caption-Guided Retrieval System for Cross-Modal Drone Navigation -- Technical Report for IROS 2025 RoboSense Challenge Track 4

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02728" target="_blank" class="toolbar-btn">arXiv: 2510.02728v2</a>
    <a href="https://arxiv.org/pdf/2510.02728.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02728v2" 
            onclick="toggleFavorite(this, '2510.02728v2', 'Team Xiaomi EV-AD VLA: Caption-Guided Retrieval System for Cross-Modal Drone Navigation -- Technical Report for IROS 2025 RoboSense Challenge Track 4')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lingfeng Zhang, Erjia Xiao, Yuchen Zhang, Haoxiang Fu, Ruibin Hu, Yanbiao Ma, Wenbo Ding, Long Chen, Hangjun Ye, Xiaoshuai Hao

**分类**: cs.RO

**发布日期**: 2025-10-03 (更新: 2025-11-06)

---

## 💡 一句话要点

**提出Caption引导的检索系统，提升跨模态无人机导航中图文检索的精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨模态检索` `无人机导航` `视觉-语言模型` `图像描述生成` `语义相似度` `图像检索` `自然语言引导`

## 📋 核心要点

1. 现有跨模态无人机导航方法难以实现文本查询和复杂航拍场景之间的细粒度语义匹配。
2. 提出Caption引导的检索系统，利用VLM生成图像描述，构建视觉内容和自然语言描述之间的语义桥梁。
3. 实验结果表明，该方法在关键指标上实现了5%的稳定提升，并在RoboSense挑战赛中获得第二名。

## 📝 摘要（中文）

本文针对跨模态无人机导航中，基于自然语言描述从大规模数据库中高效检索相关图像的挑战，提出了一个两阶段的检索优化方法：Caption引导的检索系统（CGRS）。该方法通过智能重排序来增强基线模型的粗略排序结果。首先，利用基线模型获得每个查询最相关的Top 20图像的初始粗略排序。然后，使用视觉-语言模型（VLM）为这些候选图像生成详细的描述，捕捉其丰富的语义信息。最后，在多模态相似度计算框架中使用生成的描述对原始文本查询进行细粒度的重排序，从而有效地构建视觉内容和自然语言描述之间的语义桥梁。实验结果表明，该方法在所有关键指标（Recall@1、Recall@5和Recall@10）上均实现了5%的稳定提升，并在RoboSense 2025挑战赛中获得第二名，验证了该语义优化策略在实际机器人导航场景中的价值。

## 🔬 方法详解

**问题定义**：论文旨在解决跨模态无人机导航中，自然语言引导的跨视角图像检索问题。现有方法在处理复杂航拍场景时，难以实现文本查询和视觉内容之间的细粒度语义匹配，导致检索精度不高。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM）生成图像的详细描述（Caption），从而将图像的视觉信息转化为文本信息，构建文本查询和图像之间的语义桥梁。通过比较文本查询和图像描述的相似度，实现更精确的图像检索。

**技术框架**：CGRS系统包含两个主要阶段：1) 粗略检索阶段：使用基线模型（具体模型未知）对图像数据库进行初步检索，得到Top 20的候选图像。2) 精细重排序阶段：使用VLM为每个候选图像生成详细的文本描述；然后，计算文本查询和每个图像描述之间的相似度；最后，根据相似度对候选图像进行重排序，得到最终的检索结果。

**关键创新**：该方法最重要的创新点在于利用VLM生成图像描述，从而将图像的视觉信息转化为文本信息，实现文本查询和图像之间的语义对齐。这种方法能够有效捕捉图像的细粒度语义信息，提高检索精度。与现有方法相比，该方法无需对图像进行复杂的特征提取和表示，而是直接利用VLM生成文本描述，简化了检索流程。

**关键设计**：论文中未详细说明VLM的具体选择、图像描述生成的具体方法、以及相似度计算的具体方式。这些都是影响系统性能的关键设计细节，需要在后续研究中进一步探索。基线模型的选择也可能影响最终的检索效果。

## 📊 实验亮点

实验结果表明，所提出的Caption引导的检索系统（CGRS）在所有关键指标（Recall@1、Recall@5和Recall@10）上均实现了5%的稳定提升。该方法在RoboSense 2025挑战赛中获得第二名，验证了其在实际机器人导航场景中的有效性。具体基线模型的性能数据未知，但CGRS的提升幅度明确。

## 🎯 应用场景

该研究成果可应用于无人机自主导航、智能安防、遥感图像分析等领域。通过自然语言指令，用户可以方便地控制无人机进行目标搜索和定位，提高无人机在复杂环境下的适应性和智能化水平。该技术还有潜力应用于跨模态信息检索、智能问答等领域。

## 📄 摘要（原文）

> Cross-modal drone navigation remains a challenging task in robotics, requiring efficient retrieval of relevant images from large-scale databases based on natural language descriptions. The RoboSense 2025 Track 4 challenge addresses this challenge, focusing on robust, natural language-guided cross-view image retrieval across multiple platforms (drones, satellites, and ground cameras). Current baseline methods, while effective for initial retrieval, often struggle to achieve fine-grained semantic matching between text queries and visual content, especially in complex aerial scenes. To address this challenge, we propose a two-stage retrieval refinement method: Caption-Guided Retrieval System (CGRS) that enhances the baseline coarse ranking through intelligent reranking. Our method first leverages a baseline model to obtain an initial coarse ranking of the top 20 most relevant images for each query. We then use Vision-Language-Model (VLM) to generate detailed captions for these candidate images, capturing rich semantic descriptions of their visual content. These generated captions are then used in a multimodal similarity computation framework to perform fine-grained reranking of the original text query, effectively building a semantic bridge between the visual content and natural language descriptions. Our approach significantly improves upon the baseline, achieving a consistent 5\% improvement across all key metrics (Recall@1, Recall@5, and Recall@10). Our approach win TOP-2 in the challenge, demonstrating the practical value of our semantic refinement strategy in real-world robotic navigation scenarios.

