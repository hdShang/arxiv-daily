---
layout: default
title: "Mamba2 Meets Silence: Robust Vocal Source Separation for Sparse Regions"
---

# Mamba2 Meets Silence: Robust Vocal Source Separation for Sparse Regions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14556" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14556v1</a>
  <a href="https://arxiv.org/pdf/2508.14556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14556v1', 'Mamba2 Meets Silence: Robust Vocal Source Separation for Sparse Regions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Euiyeon Kim, Yong-Hoon Choi

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出Mamba2模型以解决稀疏区域的声源分离问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `声源分离` `音频处理` `Mamba2模型` `长时间序列` `音乐技术` `深度学习` `状态空间模型`

## 📋 核心要点

1. 现有的声源分离方法，尤其是基于Transformer的模型，常常无法有效捕捉间歇性出现的声乐，导致分离效果不佳。
2. 本文提出了一种基于Mamba2的模型，通过结合带分割策略和双路径架构，能够更好地处理长时间序列的声乐分离问题。
3. 实验结果显示，该模型在cSDR上达到了11.03 dB，超越了当前最先进的模型，并在不同输入条件下表现出稳定性和一致性。

## 📝 摘要（中文）

本文介绍了一种新型音乐源分离模型，旨在实现准确的声乐隔离。与基于Transformer的方法不同，该模型利用Mamba2这一最新的状态空间模型，更好地捕捉长时间的时间依赖性。为高效处理长输入序列，本文结合了带分割策略与双路径架构。实验结果表明，该方法在cSDR上达到了11.03 dB，超越了现有的最先进模型，并在uSDR上也取得了显著提升。此外，该模型在不同输入长度和声乐出现模式下表现稳定一致，展示了基于Mamba的模型在高分辨率音频处理中的有效性，并为音频研究的更广泛应用开辟了新方向。

## 🔬 方法详解

**问题定义**：本文旨在解决声源分离中的声乐隔离问题，现有方法在处理间歇性声乐时表现不佳，导致分离效果不理想。

**核心思路**：论文提出的核心思路是利用Mamba2模型的优势，结合带分割策略和双路径架构，以更好地捕捉长时间的时间依赖性，从而提高声乐分离的准确性。

**技术框架**：整体架构包括输入音频的带分割处理，随后通过双路径网络进行特征提取和声源分离，最后输出分离后的声乐和伴奏。

**关键创新**：最重要的技术创新在于采用Mamba2模型，这一状态空间模型在处理长序列时表现优越，显著改善了声乐的分离效果，与传统的Transformer方法形成鲜明对比。

**关键设计**：模型设计中，采用了特定的损失函数以优化声乐与伴奏的分离效果，同时在网络结构上进行了优化，以适应长输入序列的处理需求。具体参数设置和网络层数在实验中经过调优，以达到最佳性能。

## 📊 实验亮点

实验结果表明，提出的模型在cSDR上达到了11.03 dB，超越了现有的最先进模型，并在uSDR上也取得了显著提升。这一性能提升展示了Mamba2模型在高分辨率音频处理中的有效性，尤其是在处理不同输入长度和声乐出现模式时表现出稳定性。

## 🎯 应用场景

该研究的潜在应用领域包括音乐制作、音频后期处理以及语音识别等。通过提高声乐分离的准确性，该模型能够为音乐创作和音频分析提供更高质量的音频素材，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> We introduce a new music source separation model tailored for accurate vocal isolation. Unlike Transformer-based approaches, which often fail to capture intermittently occurring vocals, our model leverages Mamba2, a recent state space model, to better capture long-range temporal dependencies. To handle long input sequences efficiently, we combine a band-splitting strategy with a dual-path architecture. Experiments show that our approach outperforms recent state-of-the-art models, achieving a cSDR of 11.03 dB-the best reported to date-and delivering substantial gains in uSDR. Moreover, the model exhibits stable and consistent performance across varying input lengths and vocal occurrence patterns. These results demonstrate the effectiveness of Mamba-based models for high-resolution audio processing and open up new directions for broader applications in audio research.

