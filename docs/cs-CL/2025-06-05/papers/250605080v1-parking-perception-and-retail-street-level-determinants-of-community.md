---
layout: default
title: "Parking, Perception, and Retail: Street-Level Determinants of Community Vitality in Harbin"
---

# Parking, Perception, and Retail: Street-Level Determinants of Community Vitality in Harbin

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05080" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05080v1</a>
  <a href="https://arxiv.org/pdf/2506.05080.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05080v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05080v1', 'Parking, Perception, and Retail: Street-Level Determinants of Community Vitality in Harbin')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: HaoTian Lan

**分类**: cs.CL, cs.CV

**发布日期**: 2025-06-05

**备注**: 22 pages,5 figures

---

## 💡 一句话要点

**提出图像基础框架以分析哈尔滨社区商业活力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社区商业活力` `街道特征` `多模态AI` `环境质量` `车辆可达性` `用户满意度` `空间配置` `城市设计`

## 📋 核心要点

1. 现有研究未能充分揭示街道特征与社区商业活力之间的复杂关系，尤其是在中国城市背景下。
2. 本研究提出了一种可解释的图像基础框架，结合多模态AI技术，分析街道特征对商业活力的影响。
3. 研究结果表明，适度的车辆存在有助于商业发展，而过多的停车则会降低用户满意度，强调了空间配置的重要性。

## 📝 摘要（中文）

本研究探讨了中国城市社区街道商业活力的复杂影响因素，包括车辆可达性、环境质量和行人感知。通过图像基础框架，分析了停车车辆密度、绿化、清洁度和街道宽度等街道特征对零售表现和用户满意度的影响。利用街景图像和多模态大语言模型（VisualGLM-6B），构建了社区商业活力指数（CCVI），并分析其与通过GPT-4感知建模提取的空间属性的关系。研究发现，适度的车辆存在可能增强商业可达性，但过多的路边停车会降低步行性和用户满意度。相反，绿化和清洁度较高的街道则显示出显著的满意度评分，但与定价的关联较弱。街道宽度在车辆存在的影响中起到调节作用，强调了空间配置的重要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决街道特征如何影响社区商业活力的具体问题，现有方法未能有效捕捉这些复杂的非线性关系。

**核心思路**：通过构建一个图像基础框架，结合多模态大语言模型，分析街道特征与商业活力之间的关系，以提供更直观的理解和解释。

**技术框架**：整体架构包括数据收集（街景图像和商业数据）、特征提取（使用GPT-4进行空间属性建模）、CCVI构建和数据分析等主要模块。

**关键创新**：最重要的技术创新在于将AI辅助感知与城市形态分析相结合，揭示了车辆活动在社区商业中的条件性作用，与传统方法相比，提供了更深层次的洞察。

**关键设计**：研究中使用了多模态模型VisualGLM-6B进行图像分析，CCVI的构建依赖于Meituan和Dianping的数据，特征提取过程中采用了GPT-4的感知建模技术。

## 📊 实验亮点

研究发现，适度的车辆存在能够提高商业可达性，但过多的路边停车会显著降低用户满意度和商店定价。街道宽度在车辆影响中起到调节作用，强调了空间配置的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括城市设计、停车管理和社区复兴的可扩展规划工具。通过理解街道特征对商业活力的影响，城市规划者可以更有效地设计街道环境，以促进社区经济发展。

## 📄 摘要（原文）

> The commercial vitality of community-scale streets in Chinese cities is shaped by complex interactions between vehicular accessibility, environmental quality, and pedestrian perception. This study proposes an interpretable, image-based framework to examine how street-level features -- including parked vehicle density, greenery, cleanliness, and street width -- impact retail performance and user satisfaction in Harbin, China. Leveraging street view imagery and a multimodal large language model (VisualGLM-6B), we construct a Community Commercial Vitality Index (CCVI) from Meituan and Dianping data and analyze its relationship with spatial attributes extracted via GPT-4-based perception modeling. Our findings reveal that while moderate vehicle presence may enhance commercial access, excessive on-street parking -- especially in narrow streets -- erodes walkability and reduces both satisfaction and shop-level pricing. In contrast, streets with higher perceived greenery and cleanliness show significantly greater satisfaction scores but only weak associations with pricing. Street width moderates the effects of vehicle presence, underscoring the importance of spatial configuration. These results demonstrate the value of integrating AI-assisted perception with urban morphological analysis to capture non-linear and context-sensitive drivers of commercial success. This study advances both theoretical and methodological frontiers by highlighting the conditional role of vehicle activity in neighborhood commerce and demonstrating the feasibility of multimodal AI for perceptual urban diagnostics. The implications extend to urban design, parking management, and scalable planning tools for community revitalization.

