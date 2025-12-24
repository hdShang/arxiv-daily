---
layout: default
title: "LLMs vs. Chinese Anime Enthusiasts: A Comparative Study on Emotionally Supportive Role-Playing"
---

# LLMs vs. Chinese Anime Enthusiasts: A Comparative Study on Emotionally Supportive Role-Playing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06388" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06388v1</a>
  <a href="https://arxiv.org/pdf/2508.06388.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06388v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06388v1', 'LLMs vs. Chinese Anime Enthusiasts: A Comparative Study on Emotionally Supportive Role-Playing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lanlan Qiu, Xiao Pu, Yeqi Feng, Tianxing He

**分类**: cs.CL

**发布日期**: 2025-08-08

**备注**: 21 pages, 17 figures, 3 tables

**🔗 代码/项目**: [GITHUB](https://github.com/LanlanQiu/ChatAnime)

---

## 💡 一句话要点

**提出ChatAnime数据集以解决LLMs情感支持角色扮演的研究空白**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `情感支持` `角色扮演` `动漫角色` `数据集构建` `用户体验评估` `对话系统`

## 📋 核心要点

1. 现有方法在结合角色扮演与情感支持方面存在显著研究空白，缺乏有效的评估机制。
2. 论文提出了ChatAnime数据集，专注于动漫角色的情感支持角色扮演，设计了系统化的评估框架。
3. 实验结果表明，顶级LLMs在角色扮演和情感支持方面超越人类，但在响应多样性上仍需改进。

## 📝 摘要（中文）

大型语言模型（LLMs）在角色扮演对话和提供情感支持方面展现了显著能力。然而，结合这两种能力以实现与虚拟角色的情感支持互动仍存在重要研究空白。为此，本文以动漫角色为案例，提出了首个情感支持角色扮演（ESRP）数据集ChatAnime。我们选择了20个顶级动漫角色，并设计了60个情感中心的现实场景问题，随后收集了来自10个LLMs和40名中国动漫爱好者的对话数据。通过9个细化指标评估LLMs的ESRP表现，实验结果显示，表现最佳的LLMs在角色扮演和情感支持方面超越了人类粉丝，但在响应多样性上仍落后于人类。希望本研究为未来优化LLMs在ESRP中的应用提供有价值的资源和见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在情感支持角色扮演中的应用不足，现有方法未能有效结合角色特性与情感支持。

**核心思路**：通过构建ChatAnime数据集，选择具有鲜明个性的动漫角色，设计情感中心的问题，以评估LLMs在情感支持中的表现。

**技术框架**：研究分为数据集构建、对话数据收集和用户体验评估三个主要阶段，涵盖角色选择、场景设计和对话生成。

**关键创新**：首次提出情感支持角色扮演（ESRP）数据集，结合动漫角色的个性与情感支持，填补了现有研究空白。

**关键设计**：数据集包含2400个人工回答和24000个LLM生成的回答，采用9个细化指标评估LLMs的表现，确保评估的全面性与准确性。

## 📊 实验亮点

实验结果显示，表现最佳的LLMs在角色扮演和情感支持方面的得分超过了人类粉丝，具体数据表明LLMs在这两个维度的表现提升显著。然而，在响应多样性方面，人类仍然领先，表明LLMs在这一领域仍有改进空间。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟助手、游戏角色对话系统以及心理健康支持等。通过优化LLMs在情感支持角色扮演中的表现，可以提升用户体验，促进人机交互的自然性和有效性，未来可能对相关行业产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated impressive capabilities in role-playing conversations and providing emotional support as separate research directions. However, there remains a significant research gap in combining these capabilities to enable emotionally supportive interactions with virtual characters. To address this research gap, we focus on anime characters as a case study because of their well-defined personalities and large fan bases. This choice enables us to effectively evaluate how well LLMs can provide emotional support while maintaining specific character traits. We introduce ChatAnime, the first Emotionally Supportive Role-Playing (ESRP) dataset. We first thoughtfully select 20 top-tier characters from popular anime communities and design 60 emotion-centric real-world scenario questions. Then, we execute a nationwide selection process to identify 40 Chinese anime enthusiasts with profound knowledge of specific characters and extensive experience in role-playing. Next, we systematically collect two rounds of dialogue data from 10 LLMs and these 40 Chinese anime enthusiasts. To evaluate the ESRP performance of LLMs, we design a user experience-oriented evaluation system featuring 9 fine-grained metrics across three dimensions: basic dialogue, role-playing and emotional support, along with an overall metric for response diversity. In total, the dataset comprises 2,400 human-written and 24,000 LLM-generated answers, supported by over 132,000 human annotations. Experimental results show that top-performing LLMs surpass human fans in role-playing and emotional support, while humans still lead in response diversity. We hope this work can provide valuable resources and insights for future research on optimizing LLMs in ESRP. Our datasets are available at https://github.com/LanlanQiu/ChatAnime.

