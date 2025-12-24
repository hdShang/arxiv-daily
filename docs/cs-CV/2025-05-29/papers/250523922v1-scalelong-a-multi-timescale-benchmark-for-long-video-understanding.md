---
layout: default
title: ScaleLong: A Multi-Timescale Benchmark for Long Video Understanding
---

# ScaleLong: A Multi-Timescale Benchmark for Long Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23922" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23922v1</a>
  <a href="https://arxiv.org/pdf/2505.23922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23922v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23922v1', 'ScaleLong: A Multi-Timescale Benchmark for Long Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Ma, Huaqing Yuan, Xingjian Wang, Qianbo Zang, Tianci Liu, Xinyang He, Yanbin Wei, Jiawei Guo, Ni Jiahui, Zhenzhu Yang, Meng Cao, Shanghaoran Quan, Yizhi Li, Wangchunshu Zhou, Jiaheng Liu, Wenhao Huang, Ge Zhang, Shiwen Ni, Xiaojie Jin

**分类**: cs.CV, cs.CL

**发布日期**: 2025-05-29

**🔗 代码/项目**: [GITHUB](https://github.com/multimodal-art-projection/ScaleLong)

---

## 💡 一句话要点

**提出ScaleLong基准以解决长视频理解中的多时间尺度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `多时间尺度` `基准测试` `多模态大语言模型` `视频分析` `内容推荐` `智能摘要`

## 📋 核心要点

1. 现有长视频理解方法往往忽视多时间尺度设计，导致无法在相同视频内容上进行有效的模型性能比较。
2. 本文提出ScaleLong基准，通过在同一视频中嵌入针对不同时间尺度的问题，解决了多尺度比较的挑战。
3. 实验结果显示，23个多模态大语言模型的性能呈U型曲线，视觉标记容量的增加显著提升了推理能力。

## 📝 摘要（中文）

长视频理解要求模型捕捉层次化的时间信息，包括剪辑（秒）、镜头（十秒）、事件（分钟）和故事（小时）。现有基准忽视了这种多尺度设计，导致无法在相同内容上直接比较模型性能。为此，本文提出ScaleLong，这是第一个通过在同一视频内容中嵌入针对四个层次时间尺度的问题来解决这一问题的基准。ScaleLong包含269个长视频，平均时长86分钟，涵盖5个主要类别和36个子类别，每个视频设计4到8个问题，确保每个时间尺度至少有一个问题。对23个多模态大语言模型的评估显示出U型性能曲线，短时间尺度和长时间尺度的准确率较高，而中间水平则有所下降。此外，消融研究表明，增加视觉标记容量能持续提升各时间尺度的推理能力。ScaleLong为提升长视频理解中的多模态大语言模型能力提供了细粒度的多时间尺度基准。

## 🔬 方法详解

**问题定义**：本文旨在解决长视频理解中缺乏有效多时间尺度比较的问题。现有方法往往将尺度特定的问题分散在不同视频中，无法直接比较模型在相同内容上的表现。

**核心思路**：ScaleLong基准通过在同一视频内容中设计针对四个层次时间尺度（剪辑、镜头、事件和故事）的问题，提供了一个统一的评估框架，使得不同模型在相同视频上的性能可以直接比较。

**技术框架**：ScaleLong包含269个长视频，平均时长86分钟，覆盖5个主要类别和36个子类别。每个视频设计4到8个问题，确保每个时间尺度至少有一个问题。评估过程中，使用23个多模态大语言模型进行性能测试。

**关键创新**：ScaleLong的主要创新在于其多时间尺度的问题设计，使得模型在相同视频内容上的表现可以被直接比较。这一设计突破了现有基准的局限性，提供了更为细致的评估标准。

**关键设计**：在实验中，增加视觉标记的容量被证明能够持续提升模型在各时间尺度上的推理能力，且评估结果呈现出U型性能曲线，短时间尺度和长时间尺度的准确率较高，而中间时间尺度的表现相对较低。实验还表明，设计问题时的细致考虑对模型性能有显著影响。

## 📊 实验亮点

在对23个多模态大语言模型的评估中，ScaleLong展现出U型性能曲线，短时间尺度和长时间尺度的准确率显著高于中间时间尺度。此外，增加视觉标记容量的实验结果表明，推理能力在所有时间尺度上均得到了提升，验证了该基准的有效性和实用性。

## 🎯 应用场景

ScaleLong基准的提出为长视频理解领域提供了新的评估标准，具有广泛的应用潜力。它可以用于多模态大语言模型的训练与评估，推动智能视频分析、内容推荐及自动摘要等领域的发展。未来，随着长视频内容的日益增加，该基准将对相关研究和应用产生深远影响。

## 📄 摘要（原文）

> Although long-video understanding demands that models capture hierarchical temporal information -- from clip (seconds) and shot (tens of seconds) to event (minutes) and story (hours) -- existing benchmarks either neglect this multi-scale design or scatter scale-specific questions across different videos, preventing direct comparison of model performance across timescales on the same content. To address this, we introduce ScaleLong, the first benchmark to disentangle these factors by embedding questions targeting four hierarchical timescales -- clip (seconds), shot (tens of seconds), event (minutes), and story (hours) -- all within the same video content. This within-content multi-timescale questioning design enables direct comparison of model performance across timescales on identical videos. ScaleLong features 269 long videos (avg.\ 86\,min) from 5 main categories and 36 sub-categories, with 4--8 carefully designed questions, including at least one question for each timescale. Evaluating 23 MLLMs reveals a U-shaped performance curve, with higher accuracy at the shortest and longest timescales and a dip at intermediate levels. Furthermore, ablation studies show that increased visual token capacity consistently enhances reasoning across all timescales. ScaleLong offers a fine-grained, multi-timescale benchmark for advancing MLLM capabilities in long-video understanding. The code and dataset are available https://github.com/multimodal-art-projection/ScaleLong.

