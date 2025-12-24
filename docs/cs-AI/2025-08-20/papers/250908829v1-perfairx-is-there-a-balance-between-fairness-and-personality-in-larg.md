---
layout: default
title: "PerFairX: Is There a Balance Between Fairness and Personality in Large Language Model Recommendations?"
---

# PerFairX: Is There a Balance Between Fairness and Personality in Large Language Model Recommendations?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08829" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08829v1</a>
  <a href="https://arxiv.org/pdf/2509.08829.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08829v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08829v1', 'PerFairX: Is There a Balance Between Fairness and Personality in Large Language Model Recommendations?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chandan Kumar Sah

**分类**: cs.CY, cs.AI, cs.IR

**发布日期**: 2025-08-20

**备注**: 10 pages, 5 figures. Accepted to the Workshop on Multimodal Continual Learning (MCL) at ICCV 2025. @2025 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW), ICCV's 2025

---

## 💡 一句话要点

**提出PerFairX以解决大语言模型推荐中的公平性与个性化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推荐系统` `个性化` `公平性` `心理契合` `OCEAN模型` `用户中心AI`

## 📋 核心要点

1. 现有推荐系统在个性化与公平性之间存在矛盾，难以兼顾用户心理需求与人口统计公平性。
2. 提出PerFairX框架，通过量化个性化与公平性之间的权衡，促进LLM生成推荐的心理一致性与公平性。
3. 实验结果表明，个性化提示提高了心理契合度，但在不同人口群体间的公平性差异加剧，DeepSeek表现出更强的心理适应性。

## 📝 摘要（中文）

将大型语言模型（LLMs）整合到推荐系统中，使得通过基于提示的交互实现零-shot的个性化推荐成为可能。然而，通过OCEAN模型纳入用户个性特征时，心理一致性与人口公平性之间存在重要的张力。为此，本文提出了PerFairX，一个统一的评估框架，旨在量化LLM生成推荐中的个性化与人口公平性之间的权衡。通过使用中性和个性敏感的提示，基于多样化用户档案，我们对两个最先进的LLM（ChatGPT和DeepSeek）在电影（MovieLens 10M）和音乐（Last.fm 360K）数据集上进行了基准测试。结果显示，个性化提示显著提高了与个体特征的一致性，但可能加剧了不同人口群体之间的公平性差异。

## 🔬 方法详解

**问题定义**：本文旨在解决在大型语言模型生成推荐时，如何平衡个性化与人口公平性的问题。现有方法往往无法同时满足用户的个性化需求和不同群体之间的公平性，导致推荐结果的不均衡。

**核心思路**：论文提出的PerFairX框架通过量化个性化与公平性之间的权衡，使用个性敏感的提示来提高推荐的心理契合度，同时评估其对人口公平性的影响。

**技术框架**：PerFairX框架包括数据预处理、个性化提示生成、推荐模型评估和公平性分析四个主要模块。首先，构建多样化的用户档案，然后生成相应的个性化提示，最后对推荐结果进行心理契合度和公平性评估。

**关键创新**：最重要的创新在于提出了一个统一的评估框架，能够同时考虑个性化与公平性之间的权衡，这在现有的推荐系统研究中尚属首次。

**关键设计**：在实验中，使用OCEAN模型来评估用户个性特征，设计了中性和个性化的提示策略，并对ChatGPT和DeepSeek的输出进行了系统的比较，关注其对不同人口群体的影响。具体的损失函数和评估指标也进行了细致设计，以确保公平性和个性化的有效评估。

## 📊 实验亮点

实验结果显示，个性化提示显著提高了与用户个性特征的一致性，DeepSeek在心理契合度上表现更强，但对提示变化更敏感；而ChatGPT则提供了更稳定但个性化程度较低的输出。这些发现为未来的推荐系统设计提供了重要的参考。

## 🎯 应用场景

该研究的潜在应用领域包括个性化推荐系统、社交媒体内容推荐以及在线教育平台等。通过实现公平且个性化的推荐，PerFairX能够帮助企业提升用户满意度和忠诚度，推动用户中心的AI应用发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The integration of Large Language Models (LLMs) into recommender systems has enabled zero-shot, personality-based personalization through prompt-based interactions, offering a new paradigm for user-centric recommendations. However, incorporating user personality traits via the OCEAN model highlights a critical tension between achieving psychological alignment and ensuring demographic fairness. To address this, we propose PerFairX, a unified evaluation framework designed to quantify the trade-offs between personalization and demographic equity in LLM-generated recommendations. Using neutral and personality-sensitive prompts across diverse user profiles, we benchmark two state-of-the-art LLMs, ChatGPT and DeepSeek, on movie (MovieLens 10M) and music (Last.fm 360K) datasets. Our results reveal that personality-aware prompting significantly improves alignment with individual traits but can exacerbate fairness disparities across demographic groups. Specifically, DeepSeek achieves stronger psychological fit but exhibits higher sensitivity to prompt variations, while ChatGPT delivers stable yet less personalized outputs. PerFairX provides a principled benchmark to guide the development of LLM-based recommender systems that are both equitable and psychologically informed, contributing to the creation of inclusive, user-centric AI applications in continual learning contexts.

