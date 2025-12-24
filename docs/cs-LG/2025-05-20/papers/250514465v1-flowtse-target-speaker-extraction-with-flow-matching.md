---
layout: default
title: "FlowTSE: Target Speaker Extraction with Flow Matching"
---

# FlowTSE: Target Speaker Extraction with Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14465" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14465v1</a>
  <a href="https://arxiv.org/pdf/2505.14465.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14465v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14465v1', 'FlowTSE: Target Speaker Extraction with Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aviv Navon, Aviv Shamsian, Yael Segal-Feldman, Neta Glazer, Gil Hetz, Joseph Keshet

**分类**: eess.AS, cs.LG, cs.SD

**发布日期**: 2025-05-20

**备注**: InterSpeech 2025

---

## 💡 一句话要点

**提出FlowTSE以解决目标说话人提取问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `目标说话人提取` `生成模型` `条件流匹配` `梅尔谱图` `声码器` `相位重建` `语音处理`

## 📋 核心要点

1. 现有的目标说话人提取方法多为判别性，生成方法尚未得到充分探索，且通常依赖复杂的管道，导致计算开销较大。
2. 本文提出FlowTSE，采用条件流匹配的方式，简化了目标说话人提取的过程，直接处理梅尔谱图以提取目标语音。
3. 实验结果显示，FlowTSE在标准TSE基准测试中表现优异，能够与现有强基线相媲美或超越，验证了其有效性。

## 📝 摘要（中文）

目标说话人提取（TSE）旨在从混合信号中提取特定说话者的语音，通常依赖于说话者注册作为参考。尽管现有方法多为判别性，近期的生成方法在TSE中取得了良好效果，但仍未得到充分探索，且大多数方法依赖复杂的管道和预训练组件，导致计算开销较大。本文提出FlowTSE，一种基于条件流匹配的简单有效的TSE方法。该模型接收一个注册音频样本和一个混合语音信号，均以梅尔谱图表示，目标是提取目标说话者的清晰语音。此外，对于相位重建至关重要的任务，本文提出了一种新型声码器，基于混合信号的复STFT进行条件处理，从而改善相位估计。实验结果表明，FlowTSE在标准TSE基准测试中与强基线相匹配或超越。

## 🔬 方法详解

**问题定义**：本文旨在解决目标说话人提取（TSE）中的复杂性和计算开销问题。现有方法多依赖于复杂的管道和预训练组件，导致效率低下。

**核心思路**：FlowTSE通过条件流匹配的方法，简化了TSE的实现过程，直接处理梅尔谱图，旨在高效提取目标说话者的清晰语音。

**技术框架**：FlowTSE的整体架构包括两个主要输入：一个注册音频样本和一个混合语音信号。模型通过条件流匹配来实现目标语音的提取，并在需要相位重建的任务中引入新型声码器。

**关键创新**：FlowTSE的主要创新在于其使用条件流匹配的简单架构，避免了复杂的预处理和管道设计，与传统方法相比，显著降低了计算开销。

**关键设计**：在模型设计中，采用梅尔谱图作为输入，损失函数设计为适应目标说话人提取的特定需求，同时新型声码器基于混合信号的复STFT进行条件处理，以改善相位估计。

## 📊 实验亮点

实验结果表明，FlowTSE在标准TSE基准测试中表现出色，能够与现有的强基线相匹配或超越，具体性能数据未提供，但验证了其在目标说话人提取任务中的有效性和优势。

## 🎯 应用场景

该研究在语音处理、语音识别和人机交互等领域具有广泛的应用潜力。通过高效提取目标说话者的语音，FlowTSE可用于改善语音助手的性能、增强会议记录的清晰度以及提升语音翻译的准确性，未来可能在智能家居和客服系统中发挥重要作用。

## 📄 摘要（原文）

> Target speaker extraction (TSE) aims to isolate a specific speaker's speech from a mixture using speaker enrollment as a reference. While most existing approaches are discriminative, recent generative methods for TSE achieve strong results. However, generative methods for TSE remain underexplored, with most existing approaches relying on complex pipelines and pretrained components, leading to computational overhead. In this work, we present FlowTSE, a simple yet effective TSE approach based on conditional flow matching. Our model receives an enrollment audio sample and a mixed speech signal, both represented as mel-spectrograms, with the objective of extracting the target speaker's clean speech. Furthermore, for tasks where phase reconstruction is crucial, we propose a novel vocoder conditioned on the complex STFT of the mixed signal, enabling improved phase estimation. Experimental results on standard TSE benchmarks show that FlowTSE matches or outperforms strong baselines.

