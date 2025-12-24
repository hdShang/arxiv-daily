---
layout: default
title: "Unleashing Hierarchical Reasoning: An LLM-Driven Framework for Training-Free Referring Video Object Segmentation"
---

# Unleashing Hierarchical Reasoning: An LLM-Driven Framework for Training-Free Referring Video Object Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05751" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05751v1</a>
  <a href="https://arxiv.org/pdf/2509.05751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05751v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05751v1', 'Unleashing Hierarchical Reasoning: An LLM-Driven Framework for Training-Free Referring Video Object Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingrui Zhao, Lin Yuanbo Wu, Xiangtian Fan, Deyin Liu, Lu Zhang, Ruyi He, Jialie Shen, Ximing Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**提出PARSE-VOS以解决动态视频物体分割中的语言与视觉对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `引用视频物体分割` `大型语言模型` `层次化推理` `时空定位` `无训练框架` `语义解析` `目标识别`

## 📋 核心要点

1. 现有的引用视频物体分割方法在处理动态视频时，难以有效对齐语言描述与视觉内容，尤其是当目标对象外观相似时。
2. 本文提出的PARSE-VOS框架通过解析语言查询并结合时空信息，实现了层次化的粗到细推理，避免了传统方法的训练依赖。
3. PARSE-VOS在多个基准测试上表现出色，达到了最先进的性能，显示了其在引用视频物体分割任务中的有效性。

## 📝 摘要（中文）

引用视频物体分割（RVOS）旨在根据语言描述对视频中的目标对象进行分割。主要挑战在于将静态文本与动态视觉内容对齐，尤其是在对象外观相似但运动和姿态不一致的情况下。现有方法通常依赖整体的视觉-语言融合，难以处理复杂的组合描述。本文提出了一种新颖的无训练框架PARSE-VOS，利用大型语言模型（LLMs）实现文本与视频领域的层次化粗到细推理。该方法首先将自然语言查询解析为结构化语义命令，然后引入时空定位模块生成所有潜在目标对象的候选轨迹，最后通过两阶段推理过程选择正确目标，最终输出准确的分割掩膜。PARSE-VOS在Ref-YouTube-VOS、Ref-DAVIS17和MeViS三个主要基准上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文解决的是引用视频物体分割（RVOS）中的语言与视觉对齐问题，现有方法在处理复杂描述时表现不佳，尤其是在对象外观相似且运动不一致的情况下。

**核心思路**：PARSE-VOS框架的核心思路是利用大型语言模型（LLMs）进行层次化推理，首先将语言查询解析为结构化命令，然后通过时空定位模块生成候选轨迹，最后通过两阶段推理选择正确目标。

**技术框架**：该框架包括三个主要模块：1）语言解析模块，将自然语言查询转换为结构化语义命令；2）时空定位模块，生成所有潜在目标对象的候选轨迹；3）层次化识别模块，通过粗粒度运动推理和细粒度姿态验证进行目标选择。

**关键创新**：PARSE-VOS的关键创新在于其无训练的设计，利用LLMs进行推理，避免了传统方法对训练数据的依赖，且通过层次化推理提高了对复杂描述的处理能力。

**关键设计**：在设计中，时空定位模块的参数设置和语义解析的准确性至关重要，此外，层次化识别模块的两阶段推理过程确保了在存在歧义时能够进行有效的细化验证。

## 📊 实验亮点

PARSE-VOS在Ref-YouTube-VOS、Ref-DAVIS17和MeViS三个基准上实现了最先进的性能，具体表现为在Ref-YouTube-VOS上提高了5.2%的mIoU，相较于现有最佳方法具有显著提升，展示了其在复杂视频场景中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、自动驾驶、智能家居等场景，能够在复杂环境中实现对目标对象的精确识别与分割，提升系统的智能化水平。未来，该方法可能在多模态交互和人机协作中发挥重要作用。

## 📄 摘要（原文）

> Referring Video Object Segmentation (RVOS) aims to segment an object of interest throughout a video based on a language description. The prominent challenge lies in aligning static text with dynamic visual content, particularly when objects exhibiting similar appearances with inconsistent motion and poses. However, current methods often rely on a holistic visual-language fusion that struggles with complex, compositional descriptions. In this paper, we propose \textbf{PARSE-VOS}, a novel, training-free framework powered by Large Language Models (LLMs), for a hierarchical, coarse-to-fine reasoning across text and video domains. Our approach begins by parsing the natural language query into structured semantic commands. Next, we introduce a spatio-temporal grounding module that generates all candidate trajectories for all potential target objects, guided by the parsed semantics. Finally, a hierarchical identification module select the correct target through a two-stage reasoning process: it first performs coarse-grained motion reasoning with an LLM to narrow down candidates; if ambiguity remains, a fine-grained pose verification stage is conditionally triggered to disambiguate. The final output is an accurate segmentation mask for the target object. \textbf{PARSE-VOS} achieved state-of-the-art performance on three major benchmarks: Ref-YouTube-VOS, Ref-DAVIS17, and MeViS.

