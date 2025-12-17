---
layout: default
title: Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting
---

# Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting

**arXiv**: [2512.14115v1](https://arxiv.org/abs/2512.14115) | [PDF](https://arxiv.org/pdf/2512.14115.pdf)

**作者**: Ramesh Gundluru, Shubham Gupta, Sri Rama Murty K

**分类**: cs.SD, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出联合多模态对比学习框架，以解决声学词嵌入在语音检索任务中的局限性，提升口语词检测和关键词识别的鲁棒性。**

**关键词**: `声学词嵌入` `多模态对比学习` `口语词检测` `关键词识别` `音频-文本对齐` `语音检索` `联合优化` `共享嵌入空间`

## 📋 核心要点

1. 现有声学词嵌入方法依赖单模态监督，音频-音频和音频-文本对齐优化分离，导致模型泛化能力受限。
2. 提出联合多模态对比学习框架，统一音频-文本和音频-音频监督，在共享嵌入空间中进行端到端优化。
3. 在词判别任务上超越基线，同时支持口语词检测和关键词识别，展示了方法的鲁棒性和灵活性。

## 📝 摘要（中文）

声学词嵌入（AWEs）提高了语音检索任务（如口语词检测和关键词识别）的效率。然而，现有方法存在局限性，包括单模态监督、音频-音频和音频-文本对齐的分离优化，以及需要任务特定模型。为解决这些不足，我们提出了一个联合多模态对比学习框架，在共享嵌入空间中统一了声学和跨模态监督。我们的方法同时优化：（i）音频-文本对比学习，受CLAP损失启发，以对齐音频和文本表示；（ii）音频-音频对比学习，通过深度词判别损失，以增强类内紧凑性和类间分离性。所提方法在词判别任务上优于现有AWE基线，同时灵活支持口语词检测和关键词识别。据我们所知，这是首个此类综合方法。

## 🔬 方法详解

论文提出一个联合多模态对比学习框架，整体架构包括音频编码器和文本编码器，生成共享嵌入空间中的表示。关键技术创新点在于同时应用音频-文本对比学习（基于CLAP损失）和音频-音频对比学习（基于深度词判别损失），以统一优化跨模态对齐和声学判别性。与现有方法的主要区别在于避免了分离优化，通过端到端训练整合多模态监督，从而提升模型在语音检索任务中的性能和泛化能力。

## 📊 实验亮点

在词判别任务上，所提方法优于现有声学词嵌入基线，同时灵活支持口语词检测和关键词识别，展示了多模态联合优化的有效性。

## 🎯 应用场景

该研究可应用于语音检索系统，如口语词检测和关键词识别，适用于智能助手、语音搜索和音频内容分析等领域，提高检索效率和准确性。

## 📄 摘要（原文）

> Acoustic Word Embeddings (AWEs) improve the efficiency of speech retrieval tasks such as Spoken Term Detection (STD) and Keyword Spotting (KWS). However, existing approaches suffer from limitations, including unimodal supervision, disjoint optimization of audio-audio and audio-text alignment, and the need for task-specific models. To address these shortcomings, we propose a joint multimodal contrastive learning framework that unifies both acoustic and cross-modal supervision in a shared embedding space. Our approach simultaneously optimizes: (i) audio-text contrastive learning, inspired by the CLAP loss, to align audio and text representations and (ii) audio-audio contrastive learning, via Deep Word Discrimination (DWD) loss, to enhance intra-class compactness and inter-class separation. The proposed method outperforms existing AWE baselines on word discrimination task while flexibly supporting both STD and KWS. To our knowledge, this is the first comprehensive approach of its kind.

