---
layout: default
title: Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in
---

# Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in

**arXiv**: [2512.14273v1](https://arxiv.org/abs/2512.14273) | [PDF](https://arxiv.org/pdf/2512.14273.pdf)

**作者**: Xiaoqian Shen, Min-Hung Chen, Yu-Chiang Frank Wang, Mohamed Elhoseiny, Ryo Hachiuma

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://xiaoqian-shen.github.io/Zoom-Zero/

---

## 💡 一句话要点

**提出Zoom-Zero框架，通过粗到细的时序放大机制解决视频问答中的时序定位不准确问题。**

**关键词**: `视频问答` `时序定位` `粗到细框架` `强化学习` `多模态融合` `长视频理解` `视觉验证` `令牌信用分配`

## 📋 核心要点

1. 现有大型视频语言模型在时序感知方面有限，基于GRPO的方法仍难以忠实定位视频证据，导致时序错位和幻觉。
2. 提出Zoom-Zero框架，采用粗到细的时序放大机制，结合放大精度奖励和令牌选择性信用分配，提升时序定位和视觉验证。
3. 在NExT-GQA和ReXTime数据集上时序定位精度分别提升5.2%和4.6%，答案准确率提高2.4%，长视频理解平均提升6.4%。

## 📝 摘要（中文）

基于视频的问答任务旨在定位视频中的相关时序片段并生成准确答案，但现有大型视频语言模型在时序感知方面存在局限。虽然基于组相对策略优化的方法试图改进时序定位，但仍难以忠实将答案基于相关视频证据，导致时序错位和幻觉。本文提出Zoom-Zero，一种粗到细的框架，首先定位查询相关片段，然后时序放大到最显著帧进行细粒度视觉验证。该方法通过两个关键创新解决GVQA任务中GRPO的局限：(i) 放大精度奖励，验证时序定位预测的保真度并促进对定位帧的细粒度视觉验证；(ii) 令牌选择性信用分配，将奖励归因于负责时序定位或答案生成的令牌，缓解GRPO在处理多方面奖励信号时的问题。所提方法推进了基于视频的问答，在NExT-GQA和ReXTime数据集上分别将时序定位精度提升5.2%和4.6%，同时将平均答案准确率提高2.4%。此外，推理过程中的粗到细放大通过保留关键视觉细节而不损害全局上下文，进一步有益于长视频理解，在长视频基准上平均提升6.4%。

## 🔬 方法详解

Zoom-Zero是一个粗到细的框架，整体流程包括两个阶段：首先，通过粗粒度定位模块识别查询相关的视频时序片段；然后，时序放大到这些片段中最显著的帧进行细粒度视觉验证，以生成准确答案。关键技术创新点包括：(i) 放大精度奖励机制，用于评估时序定位预测的保真度并促进对定位帧的细粒度验证；(ii) 令牌选择性信用分配，将强化学习奖励精确分配给负责时序定位或答案生成的令牌，优化多任务学习。与现有基于GRPO的方法相比，该方法更有效地处理多方面奖励信号，减少了时序错位和幻觉问题。

## 📊 实验亮点

在NExT-GQA数据集上时序定位精度提升5.2%，在ReXTime数据集上提升4.6%；平均答案准确率提高2.4%；长视频理解基准上平均性能提升6.4%，显著优于现有方法。

## 🎯 应用场景

该研究可应用于智能视频分析、教育辅助、安防监控和内容检索等领域，通过提升视频问答的时序定位精度，增强对长视频的理解能力，为多模态人工智能系统提供更可靠的视频证据支持。

## 📄 摘要（原文）

> Grounded video question answering (GVQA) aims to localize relevant temporal segments in videos and generate accurate answers to a given question; however, large video-language models (LVLMs) exhibit limited temporal awareness. Although existing approaches based on Group Relative Policy Optimization (GRPO) attempt to improve temporal grounding, they still struggle to faithfully ground their answers in the relevant video evidence, leading to temporal mislocalization and hallucinations. In this work, we present Zoom-Zero, a coarse-to-fine framework that first localizes query-relevant segments and then temporally zooms into the most salient frames for finer-grained visual verification. Our method addresses the limits of GRPO for the GVQA task with two key innovations: (i) a zoom-in accuracy reward that validates the fidelity of temporal grounding prediction and facilitates fine-grained visual verification on grounded frames; (ii) token-selective credit assignment, which attributes rewards to the tokens responsible for temporal localization or answer generation, mitigating GRPO's issue in handling multi-faceted reward signals. Our proposed method advances grounded video question answering, improving temporal grounding by 5.2\% on NExT-GQA and 4.6\% on ReXTime, while also enhancing average answer accuracy by 2.4\%. Additionally, the coarse-to-fine zoom-in during inference further benefits long-form video understanding by preserving critical visual details without compromising global context, yielding an average improvement of 6.4\% on long-video benchmarks.

