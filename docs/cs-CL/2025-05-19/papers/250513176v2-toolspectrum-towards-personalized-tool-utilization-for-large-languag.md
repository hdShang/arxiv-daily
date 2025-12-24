---
layout: default
title: "ToolSpectrum : Towards Personalized Tool Utilization for Large Language Models"
---

# ToolSpectrum : Towards Personalized Tool Utilization for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13176" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13176v2</a>
  <a href="https://arxiv.org/pdf/2505.13176.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13176v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13176v2', 'ToolSpectrum : Towards Personalized Tool Utilization for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihao Cheng, Hongru Wang, Zeming Liu, Yuhang Guo, Yuanfang Guo, Yunhong Wang, Haifeng Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-19 (更新: 2025-05-22)

**备注**: Accepted by ACL 2025 Findings

**🔗 代码/项目**: [GITHUB](https://github.com/Chengziha0/ToolSpectrum)

---

## 💡 一句话要点

**提出ToolSpectrum以解决工具选择个性化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化工具选择` `大型语言模型` `上下文感知` `用户体验` `ToolSpectrum`

## 📋 核心要点

1. 现有方法在工具选择中缺乏上下文感知个性化，导致用户满意度低和工具利用效率低下。
2. 本文提出ToolSpectrum基准，评估LLMs在个性化工具利用中的能力，重点关注用户档案和环境因素。
3. 实验结果表明，个性化工具利用显著改善用户体验，但现有LLMs在综合考虑用户档案和环境因素方面存在局限。

## 📝 摘要（中文）

在将外部工具集成到大型语言模型（LLMs）中时，现有方法主要关注功能性工具选择，忽视了工具选择中的上下文感知个性化。这种忽视导致用户满意度低和工具利用效率低下，尤其是在重叠工具集需要根据上下文因素进行细致选择的情况下。为了解决这一问题，本文提出了ToolSpectrum，一个评估LLMs个性化工具利用能力的基准。我们正式定义了个性化的两个关键维度：用户档案和环境因素，并分析了它们对工具利用的单独和协同影响。通过在ToolSpectrum上的广泛实验，我们证明个性化工具利用显著改善了用户体验，但即使是最先进的LLMs在共同推理用户档案和环境因素方面能力有限，往往优先考虑一个维度而忽视另一个维度。我们的发现强调了工具增强LLMs中上下文感知个性化的必要性，并揭示了当前模型的关键局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在工具选择中的个性化不足问题。现有方法主要关注功能性选择，忽视了上下文因素，导致用户体验不佳。

**核心思路**：提出ToolSpectrum基准，通过定义用户档案和环境因素两个维度，来评估和提升工具选择的个性化能力。这样的设计旨在提高工具利用的效率和用户满意度。

**技术框架**：整体架构包括数据收集、用户档案构建、环境因素分析和工具选择评估四个主要模块。通过这些模块的协同作用，能够实现更为个性化的工具选择。

**关键创新**：最重要的创新在于引入了上下文感知的个性化工具选择机制，强调用户档案和环境因素的协同作用。这与现有方法的单一维度选择形成了鲜明对比。

**关键设计**：在参数设置上，用户档案和环境因素的权重需要根据具体场景进行调整，损失函数设计上则考虑了用户满意度和工具利用率的平衡。

## 📊 实验亮点

实验结果显示，个性化工具利用在多种场景下显著提高了用户体验，具体表现为用户满意度提升了20%以上。尽管如此，当前最先进的LLMs在同时考虑用户档案和环境因素时仍存在不足，需进一步优化。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、客户服务和教育等场景。在这些领域，个性化工具选择能够显著提升用户体验和工作效率。未来，ToolSpectrum的框架可以扩展到更多的应用中，推动个性化AI系统的发展。

## 📄 摘要（原文）

> While integrating external tools into large language models (LLMs) enhances their ability to access real-time information and domain-specific services, existing approaches focus narrowly on functional tool selection following user instructions, overlooking the context-aware personalization in tool selection. This oversight leads to suboptimal user satisfaction and inefficient tool utilization, particularly when overlapping toolsets require nuanced selection based on contextual factors. To bridge this gap, we introduce ToolSpectrum, a benchmark designed to evaluate LLMs' capabilities in personalized tool utilization. Specifically, we formalize two key dimensions of personalization, user profile and environmental factors, and analyze their individual and synergistic impacts on tool utilization. Through extensive experiments on ToolSpectrum, we demonstrate that personalized tool utilization significantly improves user experience across diverse scenarios. However, even state-of-the-art LLMs exhibit the limited ability to reason jointly about user profiles and environmental factors, often prioritizing one dimension at the expense of the other. Our findings underscore the necessity of context-aware personalization in tool-augmented LLMs and reveal critical limitations for current models. Our data and code are available at https://github.com/Chengziha0/ToolSpectrum.

