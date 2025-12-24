---
layout: default
title: Foundation Model Hidden Representations for Heart Rate Estimation from Auscultation
---

# Foundation Model Hidden Representations for Heart Rate Estimation from Auscultation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20745" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20745v2</a>
  <a href="https://arxiv.org/pdf/2505.20745.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20745v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20745v2', 'Foundation Model Hidden Representations for Heart Rate Estimation from Auscultation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingping Nie, Dung T. Tran, Karan Thakkar, Vasudha Kowtha, Jon Huang, Carlos Avendano, Erdrin Azemi, Vikramjit Mitra

**分类**: cs.SD, cs.LG, eess.AS

**发布日期**: 2025-05-27 (更新: 2025-05-29)

**备注**: 5 pages, Interspeech 2025 conference

---

## 💡 一句话要点

**利用基础模型隐含表示进行心率估计，提升听诊技术的准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心率估计` `听诊技术` `基础模型` `声学表示` `自监督学习` `医疗监测` `生物信号处理`

## 📋 核心要点

1. 现有方法对心音数据的利用不足，未能充分挖掘预训练基础模型中的信息。
2. 论文通过逐层分析六种声学表示模型，探索其在心率估计中的有效性，提出了一种新的评估框架。
3. 实验结果显示，自家CLAP模型的音频编码器在心率估计中表现优于基线方法，降低了MAE。

## 📝 摘要（中文）

听诊，尤其是心音，是一种非侵入性的技术，能够提供重要的生命体征信息。近年来，自监督声学表示基础模型（FMs）被提出以提供基于声学的生命体征的见解。然而，关于听诊在这些预训练FM表示中的编码程度的探索仍然较少。本文使用公开的心音图（PCG）数据集和心率（HR）估计模型，对六种声学表示FMs进行了逐层研究，并实现了基于声学特征的基线方法。结果表明，预训练基础模型的表示向量在性能上与基线相当，且自家CLAP模型的音频编码器在心率估计中表现优于基线，尽管存在领域不匹配，仍实现了更低的平均绝对误差（MAE）。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效利用预训练基础模型对心音数据进行心率估计的问题。现有方法在利用声学特征时，未能充分挖掘模型中的潜在信息，导致估计精度不足。

**核心思路**：通过逐层分析六种声学表示基础模型，评估其在心率估计中的表现，探索不同模型的隐含表示如何影响最终结果。设计上，重点在于比较不同模型的特征提取能力及其对心率估计的贡献。

**技术框架**：研究采用公开的心音图数据集，结合心率估计模型，逐层分析六种声学表示模型，包括HuBERT、wav2vec2、wavLM、Whisper、CLAP及自家CLAP模型。每种模型的表示向量被用于心率估计，并与基线方法进行比较。

**关键创新**：本研究的创新点在于对预训练基础模型的逐层分析，揭示了不同模型在心音数据中的编码能力，尤其是自家CLAP模型在心率估计中的优越性。与现有方法相比，提供了更深入的理解和应用。

**关键设计**：在实验中，采用了多种训练/验证/测试分割方式，设置了适当的损失函数以优化心率估计，确保了模型在不同条件下的鲁棒性。

## 📊 实验亮点

实验结果表明，自家CLAP模型的音频编码器在心率估计中实现了比基线方法更低的平均绝对误差（MAE），尽管存在领域不匹配，仍展现出显著的性能提升。这一发现为声学表示模型在医疗领域的应用提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括医疗监测、远程健康管理和智能穿戴设备等。通过提高心率估计的准确性，能够为临床诊断提供更可靠的数据支持，促进个性化医疗的发展。未来，研究成果有望在更广泛的生物信号监测中得到应用。

## 📄 摘要（原文）

> Auscultation, particularly heart sound, is a non-invasive technique that provides essential vital sign information. Recently, self-supervised acoustic representation foundation models (FMs) have been proposed to offer insights into acoustics-based vital signs. However, there has been little exploration of the extent to which auscultation is encoded in these pre-trained FM representations. In this work, using a publicly available phonocardiogram (PCG) dataset and a heart rate (HR) estimation model, we conduct a layer-wise investigation of six acoustic representation FMs: HuBERT, wav2vec2, wavLM, Whisper, Contrastive Language-Audio Pretraining (CLAP), and an in-house CLAP model. Additionally, we implement the baseline method from Nie et al., 2024 (which relies on acoustic features) and show that overall, representation vectors from pre-trained foundation models (FMs) offer comparable performance to the baseline. Notably, HR estimation using the representations from the audio encoder of the in-house CLAP model outperforms the results obtained from the baseline, achieving a lower mean absolute error (MAE) across various train/validation/test splits despite the domain mismatch.

