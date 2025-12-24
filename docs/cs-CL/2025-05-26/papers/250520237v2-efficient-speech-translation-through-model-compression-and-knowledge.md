---
layout: default
title: Efficient Speech Translation through Model Compression and Knowledge Distillation
---

# Efficient Speech Translation through Model Compression and Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20237" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20237v2</a>
  <a href="https://arxiv.org/pdf/2505.20237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20237v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20237v2', 'Efficient Speech Translation through Model Compression and Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yasmin Moslem

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-05-26 (更新: 2025-06-02)

**备注**: IWSLT 2025

**期刊**: Proceedings of the 22nd International Conference on Spoken Language Translation (IWSLT 2025)

**DOI**: [10.18653/v1/2025.iwslt-1.40](https://doi.org/10.18653/v1/2025.iwslt-1.40)

---

## 💡 一句话要点

**通过模型压缩与知识蒸馏提高语音翻译效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模型压缩` `知识蒸馏` `语音翻译` `低秩适应` `量化技术`

## 📋 核心要点

1. 现有的大规模音频语言模型在语音翻译中计算需求高，导致部署困难。
2. 本文提出结合层修剪、低秩适应和知识蒸馏的方法，以降低模型复杂度。
3. 实验结果表明，修剪后的模型在参数和存储上减少50%，翻译质量几乎不变。

## 📝 摘要（中文）

大规模音频语言模型在语音翻译中的高效部署面临显著的计算需求挑战。本文通过在国际口语语言翻译会议（IWSLT 2025）“模型压缩”赛道的系统提交，提出了一种解决方案。我们结合了基于层重要性评估的迭代层修剪、4位量化的低秩适应（QLoRA）和知识蒸馏等方法。在实验中，我们使用Qwen2-Audio-7B-Instruct进行德语和中文的语音翻译。经过修剪的模型在参数和存储占用上减少了50%，同时保持了教师模型97-100%的翻译质量。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模音频语言模型在语音翻译中的高计算需求问题。现有方法在部署时面临参数量大、存储需求高等痛点，限制了其实际应用。

**核心思路**：通过模型压缩和知识蒸馏的结合，降低模型的复杂度，同时保持翻译质量。采用层修剪和低秩适应技术，以提高模型的效率。

**技术框架**：整体架构包括三个主要模块：首先进行层重要性评估，选择性修剪不重要的层；其次应用QLoRA进行低秩适应和量化；最后通过知识蒸馏将教师模型的知识转移到学生模型中。

**关键创新**：最重要的创新在于结合了层修剪、低秩适应和知识蒸馏三种技术，显著提高了模型的压缩效率，并保持了翻译质量。与传统方法相比，本文方法在模型参数和存储占用上实现了大幅度减少。

**关键设计**：在层修剪过程中，采用了基于层重要性评估的迭代方法；QLoRA使用4位量化技术以减少存储需求；知识蒸馏则通过设计合适的损失函数，确保学生模型能够有效学习教师模型的知识。

## 📊 实验亮点

实验结果显示，经过修剪的学生模型在参数和存储占用上减少了50%，而翻译质量保持在97-100%之间，几乎与教师模型无差异。这一成果表明，模型压缩与知识蒸馏的结合能够有效提升语音翻译系统的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括实时语音翻译、跨语言沟通工具以及多语言教育平台。通过提高语音翻译模型的效率，能够在资源受限的设备上实现更广泛的应用，推动全球化交流与合作。未来，该技术有望在更多语言和场景中得到应用，提升用户体验。

## 📄 摘要（原文）

> Efficient deployment of large audio-language models for speech translation remains challenging due to their significant computational requirements. In this paper, we address this challenge through our system submissions to the "Model Compression" track at the International Conference on Spoken Language Translation (IWSLT 2025). We experiment with a combination of approaches including iterative layer pruning based on layer importance evaluation, low-rank adaptation with 4-bit quantization (QLoRA), and knowledge distillation. In our experiments, we use Qwen2-Audio-7B-Instruct for speech translation into German and Chinese. Our pruned (student) models achieve up to a 50% reduction in both model parameters and storage footprint, while retaining 97-100% of the translation quality of the in-domain (teacher) models.

