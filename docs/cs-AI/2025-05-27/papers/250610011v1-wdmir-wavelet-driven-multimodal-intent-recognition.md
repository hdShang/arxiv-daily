---
layout: default
title: "WDMIR: Wavelet-Driven Multimodal Intent Recognition"
---

# WDMIR: Wavelet-Driven Multimodal Intent Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10011" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10011v1</a>
  <a href="https://arxiv.org/pdf/2506.10011.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10011v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10011v1', 'WDMIR: Wavelet-Driven Multimodal Intent Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiyin Gong, Kai Zhang, Yanghai Zhang, Qi Liu, Xinjie Sun, Junyu Lu, Linbo Zhu

**分类**: cs.MM, cs.AI, cs.CV, eess.SP

**发布日期**: 2025-05-27

**备注**: Accepted at IJCAI 2025, 9pages, 6figures

---

## 💡 一句话要点

**提出WDMIR框架以提升多模态意图识别精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态意图识别` `波浪驱动` `频域分析` `跨模态交互` `情感识别` `特征融合` `深度学习`

## 📋 核心要点

1. 现有多模态意图识别方法多侧重于文本分析，忽视了非语言线索的语义信息，导致意图理解的准确性不足。
2. 本文提出WDMIR框架，通过波浪驱动的频域分析，增强对视频和音频特征的融合，提升意图识别的精度。
3. 在MIntRec数据集上，WDMIR框架实现了1.13%的准确率提升，并在细微情感线索分析中提高了0.41%的识别准确率。

## 📝 摘要（中文）

多模态意图识别（MIR）旨在通过整合视频、音频和文本等多种信息，准确解读用户意图。现有方法往往侧重于文本分析，忽视了非语言线索中蕴含的丰富语义内容。本文提出了一种新颖的波浪驱动多模态意图识别（WDMIR）框架，通过对非语言信息的频域分析来增强意图理解。具体而言，我们提出了（1）一个波浪驱动融合模块，能够在频域中同步分解和整合视频音频特征，实现对时间动态的细粒度分析；（2）一个跨模态交互机制，促进从双模态到三模态的逐步特征增强，有效弥合语言与非语言信息之间的语义差距。在MIntRec上的大量实验表明，我们的方法在准确率上超越了之前的方法1.13%。消融研究进一步验证了波浪驱动融合模块显著提高了从非语言源提取语义信息的能力，在分析细微情感线索时准确率提升了0.41%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态意图识别方法中对非语言信息分析不足的问题，导致意图理解的准确性降低。

**核心思路**：提出波浪驱动的频域分析方法，通过对视频和音频特征的同步分解与融合，增强对非语言线索的理解，从而提升意图识别的准确性。

**技术框架**：WDMIR框架主要包括两个模块：波浪驱动融合模块和跨模态交互机制。前者负责在频域中对视频和音频特征进行分解与整合，后者则促进不同模态之间的特征增强与融合。

**关键创新**：最重要的创新在于波浪驱动融合模块，通过频域分析实现了对非语言信息的细粒度理解，显著提升了意图识别的性能。这一方法与传统的文本主导分析方法形成了鲜明对比。

**关键设计**：在模型设计中，采用了特定的波浪变换参数设置，以优化特征提取过程；损失函数设计上，结合了多模态特征的交互影响，确保了模型在训练过程中的有效性。整体网络结构则采用了模块化设计，以便于不同模态特征的灵活整合。

## 📊 实验亮点

WDMIR框架在MIntRec数据集上实现了1.13%的准确率提升，超越了现有的最优方法。此外，在分析细微情感线索时，准确率提升了0.41%，验证了波浪驱动融合模块的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、情感计算和智能助手等。通过更准确地识别用户意图，WDMIR框架能够提升用户体验，促进更自然的交流方式。未来，该技术可能在社交媒体分析、心理健康监测等领域发挥重要作用。

## 📄 摘要（原文）

> Multimodal intent recognition (MIR) seeks to accurately interpret user intentions by integrating verbal and non-verbal information across video, audio and text modalities. While existing approaches prioritize text analysis, they often overlook the rich semantic content embedded in non-verbal cues. This paper presents a novel Wavelet-Driven Multimodal Intent Recognition(WDMIR) framework that enhances intent understanding through frequency-domain analysis of non-verbal information. To be more specific, we propose: (1) a wavelet-driven fusion module that performs synchronized decomposition and integration of video-audio features in the frequency domain, enabling fine-grained analysis of temporal dynamics; (2) a cross-modal interaction mechanism that facilitates progressive feature enhancement from bimodal to trimodal integration, effectively bridging the semantic gap between verbal and non-verbal information. Extensive experiments on MIntRec demonstrate that our approach achieves state-of-the-art performance, surpassing previous methods by 1.13% on accuracy. Ablation studies further verify that the wavelet-driven fusion module significantly improves the extraction of semantic information from non-verbal sources, with a 0.41% increase in recognition accuracy when analyzing subtle emotional cues.

