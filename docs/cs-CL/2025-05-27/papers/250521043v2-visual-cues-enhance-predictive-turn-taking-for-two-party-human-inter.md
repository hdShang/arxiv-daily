---
layout: default
title: Visual Cues Enhance Predictive Turn-Taking for Two-Party Human Interaction
---

# Visual Cues Enhance Predictive Turn-Taking for Two-Party Human Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21043" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21043v2</a>
  <a href="https://arxiv.org/pdf/2505.21043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21043v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21043v2', 'Visual Cues Enhance Predictive Turn-Taking for Two-Party Human Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sam O'Connor Russell, Naomi Harte

**分类**: cs.CL, cs.RO

**发布日期**: 2025-05-27 (更新: 2025-10-24)

**备注**: Accepted to ACL 2025, Findings of the Association for Computational Linguistics

**期刊**: In Findings of the Association for Computational Linguistics: ACL 2025, pages 209--221, Vienna, Austria. Association for Computational Linguistics, 10.18653/v1/2025.findings-acl.12

**DOI**: [10.18653/v1/2025.findings-acl.12](https://doi.org/10.18653/v1/2025.findings-acl.12)

---

## 💡 一句话要点

**提出MM-VAP以解决人机交互中的预测轮流问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态交互` `预测模型` `人机交互` `视觉线索` `语音处理` `面部表情` `视频会议`

## 📋 核心要点

1. 现有的预测轮流交互模型大多仅依赖语音，忽视了视觉线索的作用，导致交互的自然性不足。
2. 论文提出MM-VAP，通过结合语音与视觉信息（如面部表情和视线），提升预测轮流交互的准确性。
3. 实验结果显示，MM-VAP在视频会议中的预测准确率达到84%，显著高于音频模型的79%，并且在不同的沉默时长下均表现优异。

## 📝 摘要（中文）

轮流交互是一个丰富的多模态过程。预测轮流交互模型（PTTMs）有助于自然的人机交互，但大多数仅依赖于语音。我们提出了MM-VAP，这是一种结合语音和视觉线索（如面部表情、头部姿态和视线）的多模态PTTM。研究发现，在视频会议交互中，MM-VAP的表现优于最先进的仅音频模型（84%对79%）。与之前的研究不同，我们根据轮流之间的沉默时长进行分组，显示出视觉特征的加入使得MM-VAP在所有说话者转换的时长上均优于音频模型。详细的消融研究表明，面部表情特征对模型性能贡献最大。因此，我们的工作假设是，当交谈者能够相互看到时，视觉线索对轮流交互至关重要，必须纳入以实现准确的预测。我们还验证了自动语音对齐在PTTM训练中的适用性。此研究代表了对多模态PTTMs的首次全面分析，并公开了所有代码。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有预测轮流交互模型（PTTMs）仅依赖语音而忽视视觉信息的问题，这限制了人机交互的自然性和准确性。

**核心思路**：论文提出MM-VAP，通过结合语音和视觉线索（如面部表情、头部姿态和视线），来增强预测轮流交互的能力。这样的设计旨在利用多模态信息提升模型的表现。

**技术框架**：MM-VAP的整体架构包括语音输入模块和视觉输入模块，分别提取音频和视觉特征，然后通过融合层将两者结合，最终通过预测层输出轮流交互的预测结果。

**关键创新**：最重要的技术创新在于MM-VAP能够有效整合视觉信息，尤其是面部表情特征，显著提升了模型在不同沉默时长下的预测准确性，与传统的仅音频模型相比，表现出明显的优势。

**关键设计**：在模型设计中，采用了特定的损失函数来优化多模态特征的融合效果，并通过详细的消融实验确定了面部表情特征对模型性能的最大贡献。

## 📊 实验亮点

实验结果表明，MM-VAP在视频会议中的轮流预测准确率达到84%，相比于最先进的音频模型提升了5个百分点，且在不同沉默时长的情况下均表现优异，显示出视觉特征的重要性。

## 🎯 应用场景

该研究的潜在应用场景包括人机交互系统、虚拟助手、社交机器人等领域。通过提升预测轮流交互的准确性，能够使人机交互更加自然流畅，增强用户体验，未来可能在教育、医疗和娱乐等多个行业产生深远影响。

## 📄 摘要（原文）

> Turn-taking is richly multimodal. Predictive turn-taking models (PTTMs) facilitate naturalistic human-robot interaction, yet most rely solely on speech. We introduce MM-VAP, a multimodal PTTM which combines speech with visual cues including facial expression, head pose and gaze. We find that it outperforms the state-of-the-art audio-only in videoconferencing interactions (84% vs. 79% hold/shift prediction accuracy). Unlike prior work which aggregates all holds and shifts, we group by duration of silence between turns. This reveals that through the inclusion of visual features, MM-VAP outperforms a state-of-the-art audio-only turn-taking model across all durations of speaker transitions. We conduct a detailed ablation study, which reveals that facial expression features contribute the most to model performance. Thus, our working hypothesis is that when interlocutors can see one another, visual cues are vital for turn-taking and must therefore be included for accurate turn-taking prediction. We additionally validate the suitability of automatic speech alignment for PTTM training using telephone speech. This work represents the first comprehensive analysis of multimodal PTTMs. We discuss implications for future work and make all code publicly available.

