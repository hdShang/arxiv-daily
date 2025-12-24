---
layout: default
title: "S-DAT: A Multilingual, GenAI-Driven Framework for Automated Divergent Thinking Assessment"
---

# S-DAT: A Multilingual, GenAI-Driven Framework for Automated Divergent Thinking Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09068" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09068v2</a>
  <a href="https://arxiv.org/pdf/2505.09068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09068v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09068v2', 'S-DAT: A Multilingual, GenAI-Driven Framework for Automated Divergent Thinking Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jennifer Haase, Paul H. P. Hanel, Sebastian Pokutta

**分类**: cs.CL, cs.HC

**发布日期**: 2025-05-14 (更新: 2025-10-23)

**DOI**: [10.1609/aies.v8i2.36622](https://doi.org/10.1609/aies.v8i2.36622)

---

## 💡 一句话要点

**提出S-DAT框架以解决传统创造力评估的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `发散思维` `创造力评估` `多语言框架` `自动化评估` `语言模型` `语义嵌入` `跨文化研究`

## 📋 核心要点

1. 传统创造力评估方法劳动密集且依赖主观评分，限制了其可扩展性和跨文化适用性。
2. S-DAT框架利用大型语言模型和多语言嵌入，计算语义距离作为发散思维的代理，具有语言无关性。
3. 在十一种语言中进行评估，S-DAT展现出稳健的评分一致性，并与其他发散思维测量具有良好的收敛效度。

## 📝 摘要（中文）

本文介绍了S-DAT（合成发散联想任务），这是一个可扩展的多语言框架，用于自动评估发散思维（DT），这是人类创造力的核心组成部分。传统的创造力评估通常劳动密集、语言特定，并依赖主观的人类评分，限制了其可扩展性和跨文化适用性。相较之下，S-DAT利用大型语言模型和先进的多语言嵌入来计算语义距离——一种与语言无关的DT代理。我们在包括英语、西班牙语、德语、俄语、印地语和日语（汉字、平假名、片假名）在内的十一种不同语言中评估S-DAT，展示了其在语言背景下的稳健和一致的评分。与之前的DAT方法不同，S-DAT与其他DT测量显示出收敛效度，并正确区分了发散思维与聚合思维的效度。这种跨语言的灵活性使得更具包容性的全球创造力研究成为可能，解决了早期方法的关键局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决传统创造力评估方法的局限性，包括劳动密集、语言特定和主观评分等痛点，这些因素限制了评估的可扩展性和跨文化适用性。

**核心思路**：S-DAT框架的核心思路是利用大型语言模型和多语言嵌入技术，计算语义距离作为发散思维的语言无关代理，从而实现自动化评估。

**技术框架**：S-DAT的整体架构包括数据预处理、语义嵌入生成、发散思维评分计算和结果分析等主要模块，确保了多语言环境下的有效性和一致性。

**关键创新**：S-DAT的关键创新在于其跨语言的灵活性和与其他发散思维测量的收敛效度，解决了以往方法的局限，使得创造力评估更加全面和公平。

**关键设计**：在技术细节方面，S-DAT采用了先进的多语言嵌入技术，设计了适应不同语言特性的损失函数，并优化了模型的参数设置，以确保在多种语言环境下的稳健性。

## 📊 实验亮点

实验结果表明，S-DAT在十一种语言中均展现出一致的评分表现，且与其他发散思维测量的收敛效度良好，显示出显著的跨语言适用性和稳健性，为创造力评估提供了新的视角。

## 🎯 应用场景

S-DAT框架的潜在应用领域包括教育、心理学和人机交互等，能够为不同文化背景下的创造力研究提供更公平和全面的评估工具。未来，S-DAT有望推动全球范围内的创造力研究，促进跨文化交流与合作。

## 📄 摘要（原文）

> This paper introduces S-DAT (Synthetic-Divergent Association Task), a scalable, multilingual framework for automated assessment of divergent thinking (DT) -a core component of human creativity. Traditional creativity assessments are often labor-intensive, language-specific, and reliant on subjective human ratings, limiting their scalability and cross-cultural applicability. In contrast, S-DAT leverages large language models and advanced multilingual embeddings to compute semantic distance -- a language-agnostic proxy for DT. We evaluate S-DAT across eleven diverse languages, including English, Spanish, German, Russian, Hindi, and Japanese (Kanji, Hiragana, Katakana), demonstrating robust and consistent scoring across linguistic contexts. Unlike prior DAT approaches, the S-DAT shows convergent validity with other DT measures and correct discriminant validity with convergent thinking. This cross-linguistic flexibility allows for more inclusive, global-scale creativity research, addressing key limitations of earlier approaches. S-DAT provides a powerful tool for fairer, more comprehensive evaluation of cognitive flexibility in diverse populations and can be freely assessed online: https://sdat.iol.zib.de/.

