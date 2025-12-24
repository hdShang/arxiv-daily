---
layout: default
title: "T2S: High-resolution Time Series Generation with Text-to-Series Diffusion Models"
---

# T2S: High-resolution Time Series Generation with Text-to-Series Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02417" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02417v2</a>
  <a href="https://arxiv.org/pdf/2505.02417.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02417v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02417v2', 'T2S: High-resolution Time Series Generation with Text-to-Series Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunfeng Ge, Jiawei Li, Yiji Zhao, Haomin Wen, Zhao Li, Meikang Qiu, Hongyan Li, Ming Jin, Shirui Pan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-05 (更新: 2025-05-08)

**备注**: Accepted by the 34th International Joint Conference on Artificial Intelligence (IJCAI 2025)

---

## 💡 一句话要点

**提出T2S框架以解决时间序列生成中的数据稀疏与不平衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列生成` `扩散模型` `变分自编码器` `多模态数据` `流匹配` `文本对齐` `数据稀疏` `生成模型`

## 📋 核心要点

1. 现有时间序列生成方法面临数据稀疏和不平衡等挑战，且缺乏对通用时间序列描述的系统探索。
2. 论文提出了T2S框架，通过长度自适应变分自编码器和扩散变换器有效连接文本与时间序列。
3. T2S在13个数据集上实现了最先进的性能，展示了其在生成任意长度时间序列方面的能力。

## 📝 摘要（中文）

文本到时间序列生成在解决数据稀疏、不平衡和多模态时间序列数据集有限性方面具有重要潜力。尽管扩散模型在文本到其他类型数据生成中取得了显著成功，但在时间序列生成中的应用仍处于初步阶段。现有方法面临两个主要限制：一是缺乏对通用时间序列描述的系统探索，二是无法生成任意长度的时间序列，限制了其在实际场景中的应用。本文首先将时间序列描述分为点级、片段级和实例级，并引入一个包含超过60万个高分辨率时间序列-文本对的新数据集。其次，提出了T2S框架，以领域无关的方式连接自然语言与时间序列，采用长度自适应变分自编码器编码不同长度的时间序列，并通过流匹配和扩散变换器对齐文本表示与潜在嵌入。经过广泛评估，T2S在12个领域的13个数据集上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决时间序列生成中的数据稀疏和不平衡问题，现有方法无法生成任意长度的时间序列，限制了其应用场景。

**核心思路**：提出T2S框架，通过长度自适应变分自编码器将不同长度的时间序列编码为一致的潜在嵌入，并利用流匹配对齐文本表示与潜在嵌入。

**技术框架**：T2S框架包括三个主要模块：时间序列编码模块、文本表示对齐模块和生成模块，支持生成任意长度的时间序列。

**关键创新**：T2S的核心创新在于其领域无关的生成方式和长度自适应的编码能力，与现有方法相比，能够更好地处理多样化的时间序列生成任务。

**关键设计**：采用变分自编码器进行潜在空间的学习，设计了流匹配算法以增强文本与时间序列的对齐效果，同时在损失函数中引入了多任务学习策略以提升生成质量。

## 📊 实验亮点

T2S在13个数据集上实现了最先进的性能，展示了其在生成任意长度时间序列方面的能力，显著提升了生成质量，相较于基线方法有明显的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场分析、医疗监测、气象预测等，能够为数据稀疏和不平衡问题提供有效解决方案。未来，T2S框架有望推动多模态数据生成的研究进展，促进各领域的智能化应用。

## 📄 摘要（原文）

> Text-to-Time Series generation holds significant potential to address challenges such as data sparsity, imbalance, and limited availability of multimodal time series datasets across domains. While diffusion models have achieved remarkable success in Text-to-X (e.g., vision and audio data) generation, their use in time series generation remains in its nascent stages. Existing approaches face two critical limitations: (1) the lack of systematic exploration of general-proposed time series captions, which are often domain-specific and struggle with generalization; and (2) the inability to generate time series of arbitrary lengths, limiting their applicability to real-world scenarios. In this work, we first categorize time series captions into three levels: point-level, fragment-level, and instance-level. Additionally, we introduce a new fragment-level dataset containing over 600,000 high-resolution time series-text pairs. Second, we propose Text-to-Series (T2S), a diffusion-based framework that bridges the gap between natural language and time series in a domain-agnostic manner. T2S employs a length-adaptive variational autoencoder to encode time series of varying lengths into consistent latent embeddings. On top of that, T2S effectively aligns textual representations with latent embeddings by utilizing Flow Matching and employing Diffusion Transformer as the denoiser. We train T2S in an interleaved paradigm across multiple lengths, allowing it to generate sequences of any desired length. Extensive evaluations demonstrate that T2S achieves state-of-the-art performance across 13 datasets spanning 12 domains.

