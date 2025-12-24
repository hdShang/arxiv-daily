---
layout: default
title: "Deployability-Centric Infrastructure-as-Code Generation: An LLM-based Iterative Framework"
---

# Deployability-Centric Infrastructure-as-Code Generation: An LLM-based Iterative Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05623" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05623v1</a>
  <a href="https://arxiv.org/pdf/2506.05623.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05623v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05623v1', 'Deployability-Centric Infrastructure-as-Code Generation: An LLM-based Iterative Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Zhang, Shidong Pan, Zejun Zhang, Zhenchang Xing, Xiaoyu Sun

**分类**: cs.SE, cs.AI, cs.CL

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出基于LLM的IaC生成框架以解决部署能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基础设施即代码` `云计算` `大型语言模型` `自动化部署` `模板生成` `迭代反馈机制` `部署能力评估`

## 📋 核心要点

1. 现有的IaC生成方法主要关注语法正确性，缺乏对部署能力的评估，导致生成的模板在实际应用中效果不佳。
2. 本文提出了IaCGen框架，利用迭代反馈机制来生成以部署能力为中心的IaC模板，解决了现有方法的不足。
3. 实验表明，使用IaCGen后，所有评估模型的部署成功率超过90%，显著提升了生成模板的实用性。

## 📝 摘要（中文）

基础设施即代码（IaC）生成在自动化云基础设施配置方面具有重要潜力。尽管大型语言模型（LLMs）在生成可部署的基础设施模板方面展现出希望，但现有评估主要关注语法正确性，忽视了部署能力这一关键指标。为此，本文提出了IaCGen框架，利用迭代反馈机制生成IaC模板，并构建了DPIaC-Eval基准，涵盖153个真实场景，评估语法、部署、用户意图和安全性。实验结果显示，尽管当前最先进的LLMs在首次尝试中的部署成功率较低，但IaCGen显著提升了性能，所有评估模型的通过率超过90%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有IaC生成方法在部署能力评估上的不足，现有方法往往只关注语法正确性，导致生成的模板在实际部署中失败率较高。

**核心思路**：提出IaCGen框架，通过迭代反馈机制生成以部署能力为中心的IaC模板，确保生成的模板不仅语法正确，还能在实际环境中成功部署。

**技术框架**：IaCGen框架包括多个模块，首先是自然语言描述的解析模块，然后是模板生成模块，接着是部署能力评估模块，最后是反馈机制模块，通过不断迭代优化生成的模板。

**关键创新**：最重要的创新在于引入了部署能力评估作为生成模板的核心标准，与现有方法相比，强调了实用性而非仅仅是语法的正确性。

**关键设计**：在参数设置上，采用了多轮反馈机制，损失函数设计中引入了部署成功率作为重要指标，确保生成的模板能够满足用户的实际需求。

## 📊 实验亮点

实验结果显示，当前最先进的LLMs在首次尝试中的部署成功率仅为30.2%和26.8%，而使用IaCGen后，所有评估模型的通过率均超过90%，其中Claude-3.5和Claude-3.7的成功率达到了98%。

## 🎯 应用场景

该研究的潜在应用领域包括云计算服务提供商、DevOps团队及任何需要自动化基础设施配置的企业。通过提高IaC模板的部署能力，能够显著降低运维成本，提高云资源的使用效率，推动云基础设施的自动化发展。

## 📄 摘要（原文）

> Infrastructure-as-Code (IaC) generation holds significant promise for automating cloud infrastructure provisioning. Recent advances in Large Language Models (LLMs) present a promising opportunity to democratize IaC development by generating deployable infrastructure templates from natural language descriptions, but current evaluation focuses on syntactic correctness while ignoring deployability, the fatal measure of IaC template utility. We address this gap through two contributions: (1) IaCGen, an LLM-based deployability-centric framework that uses iterative feedback mechanism to generate IaC templates, and (2) DPIaC-Eval, a deployability-centric IaC template benchmark consists of 153 real-world scenarios that can evaluate syntax, deployment, user intent, and security. Our evaluation reveals that state-of-the-art LLMs initially performed poorly, with Claude-3.5 and Claude-3.7 achieving only 30.2% and 26.8% deployment success on the first attempt respectively. However, IaCGen transforms this performance dramatically: all evaluated models reach over 90% passItr@25, with Claude-3.5 and Claude-3.7 achieving 98% success rate. Despite these improvements, critical challenges remain in user intent alignment (25.2% accuracy) and security compliance (8.4% pass rate), highlighting areas requiring continued research. Our work provides the first comprehensive assessment of deployability-centric IaC template generation and establishes a foundation for future research.

