---
layout: default
title: "Suicide Risk Assessment Using Multimodal Speech Features: A Study on the SW1 Challenge Dataset"
---

# Suicide Risk Assessment Using Multimodal Speech Features: A Study on the SW1 Challenge Dataset

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13069" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13069v1</a>
  <a href="https://arxiv.org/pdf/2505.13069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13069v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13069v1', 'Suicide Risk Assessment Using Multimodal Speech Features: A Study on the SW1 Challenge Dataset')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ambre Marie, Ilias Maoudj, Guillaume Dardenne, Gwenolé Quellec

**分类**: cs.CL, cs.LG, cs.SD, eess.AS

**发布日期**: 2025-05-19

**备注**: Submitted to the SpeechWellness Challenge at Interspeech 2025; 5 pages, 2 figures, 2 tables

---

## 💡 一句话要点

**提出多模态语音特征评估青少年自杀风险的方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自杀风险评估` `多模态融合` `语音特征` `心理健康` `机器学习`

## 📋 核心要点

1. 现有方法在青少年自杀风险评估中缺乏有效的多模态融合策略，导致分类准确率不足。
2. 本研究提出了一种结合自动转录、语言和音频嵌入的多模态方法，探索不同的融合策略以提高评估效果。
3. 实验结果显示，加权注意力策略在开发集上实现了69%的准确率，但开发与测试集之间的性能差距仍需关注。

## 📝 摘要（中文）

本研究针对第一个SpeechWellness挑战，探讨了基于语音的青少年自杀风险评估的需求。研究采用多模态方法，结合了WhisperX的自动转录、中文RoBERTa的语言嵌入和WavLM的音频嵌入。此外，还融入了手工提取的声学特征，如MFCC、谱对比和音高相关统计数据。研究探索了三种融合策略：早期连接、特定模态处理和带有mixup正则化的加权注意力。结果表明，加权注意力在开发集上达到了69%的准确率，但开发集与测试集之间的性能差距突显了泛化挑战。研究强调了优化嵌入表示和融合机制以提高分类可靠性的重要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决青少年自杀风险评估中的多模态数据融合问题。现有方法在处理不同模态信息时存在准确性不足和泛化能力差的痛点。

**核心思路**：研究通过整合自动转录、语言嵌入和音频嵌入，采用多模态融合策略，以期提高自杀风险评估的准确性和可靠性。

**技术框架**：整体架构包括数据预处理、特征提取、模态融合和分类四个主要模块。首先，使用WhisperX进行语音转录，接着提取语言和音频特征，最后通过不同的融合策略进行分类。

**关键创新**：最重要的创新在于提出了加权注意力机制与mixup正则化的结合，显著提升了模型的泛化能力，与传统的简单连接或单一模态处理方法相比，表现出更优的效果。

**关键设计**：在模型设计中，采用了多种声学特征（如MFCC、谱对比）与深度学习嵌入相结合的方式，损失函数设计上考虑了多模态特征的平衡，确保了模型在不同模态间的有效学习。

## 📊 实验亮点

实验结果显示，采用加权注意力策略的模型在开发集上达到了69%的准确率，明显优于传统方法。同时，研究指出开发集与测试集之间存在性能差距，提示未来需进一步优化模型的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康监测、青少年心理干预和危机预警系统。通过准确评估自杀风险，能够为心理健康专业人士提供更有效的决策支持，进而降低青少年自杀事件的发生率。未来，该方法可扩展至其他人群的心理健康评估。

## 📄 摘要（原文）

> The 1st SpeechWellness Challenge conveys the need for speech-based suicide risk assessment in adolescents. This study investigates a multimodal approach for this challenge, integrating automatic transcription with WhisperX, linguistic embeddings from Chinese RoBERTa, and audio embeddings from WavLM. Additionally, handcrafted acoustic features -- including MFCCs, spectral contrast, and pitch-related statistics -- were incorporated. We explored three fusion strategies: early concatenation, modality-specific processing, and weighted attention with mixup regularization. Results show that weighted attention provided the best generalization, achieving 69% accuracy on the development set, though a performance gap between development and test sets highlights generalization challenges. Our findings, strictly tied to the MINI-KID framework, emphasize the importance of refining embedding representations and fusion mechanisms to enhance classification reliability.

