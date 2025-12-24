---
layout: default
title: "SSLAM: Enhancing Self-Supervised Models with Audio Mixtures for Polyphonic Soundscapes"
---

# SSLAM: Enhancing Self-Supervised Models with Audio Mixtures for Polyphonic Soundscapes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12222" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12222v1</a>
  <a href="https://arxiv.org/pdf/2506.12222.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12222v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12222v1', 'SSLAM: Enhancing Self-Supervised Models with Audio Mixtures for Polyphonic Soundscapes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tony Alex, Sara Ahmed, Armin Mustafa, Muhammad Awais, Philip JB Jackson

**分类**: cs.SD, cs.AI, cs.LG, eess.AS

**发布日期**: 2025-06-13

**备注**: Accepted at ICLR 2025. Code and pre-trained models are available at \url{https://github.com/ta012/SSLAM}

---

## 💡 一句话要点

**提出SSLAM以解决多音频场景下自监督模型的性能不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自监督学习` `音频处理` `多音频场景` `模型泛化` `音频混合`

## 📋 核心要点

1. 现有自监督音频模型在多音频环境中的表现尚未得到充分验证，主要基于单音频数据集进行评估。
2. 本文提出SSLAM，通过引入音频混合学习，增强模型在多音频数据上的学习能力，同时保持单音频性能。
3. SSLAM在标准音频自监督基准上表现优异，在多音频数据集上设立新SOTA，性能提升达到9.1%（mAP）。

## 📝 摘要（中文）

自监督预训练音频网络在现实系统中得到了广泛应用，尤其是在多模态大语言模型中。然而，这些网络通常在冻结状态下使用，假设自监督预训练已足够应对复杂的多音频环境。现有音频自监督方法主要基于单音频数据集，导致其在多音频场景中的泛化能力尚未得到充分探索。为此，本文提出了自监督学习音频混合（SSLAM），旨在提升模型在多音频数据上的学习能力，同时保持在单音频数据上的强性能。通过对标准音频自监督基准数据集的评估，SSLAM在多音频数据集上设立了新的SOTA，并在AudioSet-2M上实现了高达3.9%的性能提升，mAP达到50.2。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自监督音频模型在多音频场景下的性能不足问题。现有方法主要基于单音频数据集，导致模型在复杂的多音频环境中泛化能力不足。

**核心思路**：论文提出SSLAM，通过音频混合学习的方式，增强模型对多音频数据的学习能力，同时确保在单音频数据上的性能不下降。这种设计旨在提升模型在真实世界音频场景中的适应性。

**技术框架**：SSLAM的整体架构包括音频混合生成模块和自监督学习模块。音频混合生成模块负责创建多音频混合样本，而自监督学习模块则利用这些样本进行模型训练。

**关键创新**：SSLAM的核心创新在于引入音频混合学习机制，使得模型能够在多音频环境中有效学习。这一方法与传统的单音频训练方式本质上不同，能够更好地适应复杂的音频场景。

**关键设计**：在技术细节上，SSLAM采用了特定的损失函数来平衡单音频和多音频数据的学习，同时在网络结构上进行了优化，以提高模型的学习效率和泛化能力。

## 📊 实验亮点

SSLAM在标准音频自监督基准上表现出色，尤其在AudioSet-2M上实现了3.9%的性能提升，mAP达到50.2。同时，在多音频数据集上，SSLAM在线性评估和微调阶段设立了新的SOTA，性能提升达到9.1%（mAP）。

## 🎯 应用场景

该研究的潜在应用领域包括环境声音识别、音乐分析和语音处理等。通过提升自监督模型在多音频场景下的性能，SSLAM能够为实际音频处理系统提供更强的鲁棒性和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Self-supervised pre-trained audio networks have seen widespread adoption in real-world systems, particularly in multi-modal large language models. These networks are often employed in a frozen state, under the assumption that the SSL pre-training has sufficiently equipped them to handle real-world audio. However, a critical question remains: how well do these models actually perform in real-world conditions, where audio is typically polyphonic and complex, involving multiple overlapping sound sources? Current audio SSL methods are often benchmarked on datasets predominantly featuring monophonic audio, such as environmental sounds, and speech. As a result, the ability of SSL models to generalize to polyphonic audio, a common characteristic in natural scenarios, remains underexplored. This limitation raises concerns about the practical robustness of SSL models in more realistic audio settings. To address this gap, we introduce Self-Supervised Learning from Audio Mixtures (SSLAM), a novel direction in audio SSL research, designed to improve, designed to improve the model's ability to learn from polyphonic data while maintaining strong performance on monophonic data. We thoroughly evaluate SSLAM on standard audio SSL benchmark datasets which are predominantly monophonic and conduct a comprehensive comparative analysis against SOTA methods using a range of high-quality, publicly available polyphonic datasets. SSLAM not only improves model performance on polyphonic audio, but also maintains or exceeds performance on standard audio SSL benchmarks. Notably, it achieves up to a 3.9\% improvement on the AudioSet-2M (AS-2M), reaching a mean average precision (mAP) of 50.2. For polyphonic datasets, SSLAM sets new SOTA in both linear evaluation and fine-tuning regimes with performance improvements of up to 9.1\% (mAP).

