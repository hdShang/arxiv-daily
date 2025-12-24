---
layout: default
title: "The Foundation Cracks: A Comprehensive Study on Bugs and Testing Practices in LLM Libraries"
---

# The Foundation Cracks: A Comprehensive Study on Bugs and Testing Practices in LLM Libraries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12320" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12320v1</a>
  <a href="https://arxiv.org/pdf/2506.12320.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12320v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12320v1', 'The Foundation Cracks: A Comprehensive Study on Bugs and Testing Practices in LLM Libraries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weipeng Jiang, Xiaoyu Zhang, Xiaofei Xie, Jiongchi Yu, Yuhan Zhi, Shiqing Ma, Chao Shen

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-14

---

## 💡 一句话要点

**提出全面研究以解决LLM库中的缺陷与测试实践问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `缺陷分析` `测试实践` `API误用` `质量保证` `HuggingFace` `vLLM`

## 📋 核心要点

1. 现有LLM库频繁出现质量问题，导致AI系统的可靠性受到威胁，尤其是API误用成为主要缺陷原因。
2. 通过对HuggingFace Transformers和vLLM库的缺陷进行分析，建立了缺陷分类体系，并评估了现有测试方法的有效性。
3. 研究发现41.73%的缺陷因测试用例不足而未被检测，提出了改进LLM库质量保证的建议。

## 📝 摘要（中文）

大型语言模型（LLM）库作为当今AI革命的基础设施，支撑着LLM的部署、推理优化、微调和生产服务。然而，这些库面临频繁的质量问题和缺陷，威胁到基于它们构建的AI系统的可靠性。为填补这一知识空白，本文首次对现代LLM库中的缺陷特征和测试实践进行了全面的实证研究。我们分析了313个修复缺陷的提交，建立了缺陷症状和根本原因的分类体系。研究发现，API误用是主要根本原因，且现有测试方法的有效性不足，导致大部分缺陷未能被检测到。基于这些发现，本文提出了一些提升LLM库质量保证的建议。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型库中的缺陷及其测试实践问题。现有方法在缺陷检测和测试有效性方面存在显著不足，导致许多缺陷未能被及时发现。

**核心思路**：通过对LLM库中缺陷的全面实证研究，建立缺陷特征的分类体系，并分析现有测试方法的有效性，以提出改进建议。

**技术框架**：研究分为两个主要模块：缺陷分析和测试有效性评估。缺陷分析包括对313个修复提交的手动分析，测试有效性评估则基于7,748个测试函数的分类。

**关键创新**：本文首次系统性地分类了LLM库中的缺陷症状和根本原因，特别是API误用的显著性，标志着从传统深度学习框架的算法缺陷向接口问题的转变。

**关键设计**：在缺陷分类中，症状分为5类，根本原因分为14类；测试方法中，定义了7种测试oracle类别，强调了预定义期望输出的使用。

## 📊 实验亮点

研究表明，API误用是LLM库中最主要的缺陷根本原因，占比高达32.17%-48.19%。此外，41.73%的缺陷因测试用例不足而未被检测，显示出现有测试方法的有效性亟待提升。

## 🎯 应用场景

该研究为大型语言模型库的开发和维护提供了重要的理论基础和实践指导，能够帮助开发者识别和修复潜在缺陷，提高LLM库的质量和可靠性。未来，随着LLM技术的不断发展，本文的发现和建议将对整个AI生态系统产生深远影响。

## 📄 摘要（原文）

> Large Language Model (LLM) libraries have emerged as the foundational infrastructure powering today's AI revolution, serving as the backbone for LLM deployment, inference optimization, fine-tuning, and production serving across diverse applications. Despite their critical role in the LLM ecosystem, these libraries face frequent quality issues and bugs that threaten the reliability of AI systems built upon them. To address this knowledge gap, we present the first comprehensive empirical investigation into bug characteristics and testing practices in modern LLM libraries. We examine 313 bug-fixing commits extracted across two widely-adopted LLM libraries: HuggingFace Transformers and vLLM.Through rigorous manual analysis, we establish comprehensive taxonomies categorizing bug symptoms into 5 types and root causes into 14 distinct categories.Our primary discovery shows that API misuse has emerged as the predominant root cause (32.17%-48.19%), representing a notable transition from algorithm-focused defects in conventional deep learning frameworks toward interface-oriented problems. Additionally, we examine 7,748 test functions to identify 7 distinct test oracle categories employed in current testing approaches, with predefined expected outputs (such as specific tensors and text strings) being the most common strategy. Our assessment of existing testing effectiveness demonstrates that the majority of bugs escape detection due to inadequate test cases (41.73%), lack of test drivers (32.37%), and weak test oracles (25.90%). Drawing from these findings, we offer some recommendations for enhancing LLM library quality assurance.

