---
layout: default
title: "Detecting Voice Phishing with Precision: Fine-Tuning Small Language Models"
---

# Detecting Voice Phishing with Precision: Fine-Tuning Small Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06180" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06180v1</a>
  <a href="https://arxiv.org/pdf/2506.06180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06180v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06180v1', 'Detecting Voice Phishing with Precision: Fine-Tuning Small Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ju Yong Sim, Seong Hwan Kim

**分类**: cs.CL

**发布日期**: 2025-06-06

**备注**: 15 pages, 4 figures, 8 tables, journal submission

---

## 💡 一句话要点

**通过微调小型语言模型提高语音钓鱼检测精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音钓鱼` `小型语言模型` `模型微调` `思维链技术` `对抗性测试` `数据集构建` `安全检测`

## 📋 核心要点

1. 现有的语音钓鱼检测方法在应对复杂场景时表现不足，缺乏有效的评估标准和鲁棒性。
2. 本文提出通过微调Llama3模型，结合VP评估标准和思维链技术，提升语音钓鱼检测的准确性。
3. 实验结果显示，微调后的Llama3-8B模型在小型语言模型中表现最佳，且与GPT-4模型的性能相当。

## 📝 摘要（中文）

本文开发了一种语音钓鱼（VP）检测器，通过微调开源小型语言模型Llama3。我们在提示中提供了精心设计的VP评估标准，并应用了思维链（CoT）技术。为了评估语言模型的鲁棒性并突出其性能差异，我们构建了一个对抗性测试数据集。此外，为了解决VP转录本的缺乏，我们参考现有或新类型的VP技术创建了转录本。实验结果表明，使用包含VP评估标准的提示微调的Llama3-8B模型在小型语言模型中表现最佳，且与基于GPT-4的VP检测器相当。这些发现表明，将人类专家知识纳入提示比在小型语言模型中使用CoT技术更为有效。

## 🔬 方法详解

**问题定义**：本文旨在解决语音钓鱼检测中的准确性和鲁棒性问题。现有方法在复杂场景下的表现不佳，且缺乏有效的评估标准和数据集。

**核心思路**：通过微调Llama3模型，结合人类专家知识和思维链技术，设计出更有效的检测提示，从而提高模型的检测性能。

**技术框架**：整体架构包括数据集构建、模型微调和性能评估三个主要模块。首先构建对抗性测试数据集，然后对Llama3进行微调，最后通过不同条件下的实验评估模型性能。

**关键创新**：最重要的创新在于将人类专家知识融入提示中，这一方法显著优于单纯依赖思维链技术的传统方法。

**关键设计**：在微调过程中，使用了特定的损失函数和参数设置，以确保模型能够有效学习VP评估标准，同时保持对抗性数据集的鲁棒性。

## 📊 实验亮点

实验结果表明，微调后的Llama3-8B模型在包含VP评估标准的提示下，表现出最佳性能，准确率显著高于其他小型语言模型，且与GPT-4模型的性能相当，展示了提升幅度的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括金融安全、网络安全和客户服务等行业，能够有效识别和防范语音钓鱼攻击，保护用户信息安全。未来，该技术可扩展至其他类型的欺诈检测，提高整体安全性。

## 📄 摘要（原文）

> We develop a voice phishing (VP) detector by fine-tuning Llama3, a representative open-source, small language model (LM). In the prompt, we provide carefully-designed VP evaluation criteria and apply the Chain-of-Thought (CoT) technique. To evaluate the robustness of LMs and highlight differences in their performance, we construct an adversarial test dataset that places the models under challenging conditions. Moreover, to address the lack of VP transcripts, we create transcripts by referencing existing or new types of VP techniques. We compare cases where evaluation criteria are included, the CoT technique is applied, or both are used together. In the experiment, our results show that the Llama3-8B model, fine-tuned with a dataset that includes a prompt with VP evaluation criteria, yields the best performance among small LMs and is comparable to that of a GPT-4-based VP detector. These findings indicate that incorporating human expert knowledge into the prompt is more effective than using the CoT technique for small LMs in VP detection.

