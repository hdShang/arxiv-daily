---
layout: default
title: Video-LMM Post-Training: A Deep Dive into Video Reasoning with Large Multimodal Models
---

# Video-LMM Post-Training: A Deep Dive into Video Reasoning with Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05034" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05034v6</a>
  <a href="https://arxiv.org/pdf/2510.05034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05034v6" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05034v6', 'Video-LMM Post-Training: A Deep Dive into Video Reasoning with Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yolo Y. Tang, Jing Bi, Pinxin Liu, Zhenyu Pan, Zhangyun Tan, Qianxiang Shen, Jiani Liu, Hang Hua, Junjia Guo, Yunzhong Xiao, Chao Huang, Zhiyuan Wang, Susan Liang, Xinyi Liu, Yizhi Song, Junhua Huang, Jia-Xing Zhong, Bozheng Li, Daiqing Qi, Ziyun Zeng, Ali Vosoughi, Luchuan Song, Zeliang Zhang, Daiki Shimada, Han Liu, Jiebo Luo, Chenliang Xu

**分类**: cs.CV

**发布日期**: 2025-10-06 (更新: 2025-11-25)

**备注**: Version v1.1

**🔗 代码/项目**: [GITHUB](https://github.com/yunlong10/Awesome-Video-LMM-Post-Training)

---

## 💡 一句话要点

**全面剖析视频大模型后训练方法，提升视频推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频大模型` `后训练` `监督微调` `强化学习` `测试时缩放` `视频理解` `多模态学习`

## 📋 核心要点

1. 现有视频大模型后训练方法分散，缺乏系统性研究，阻碍了模型推理能力的提升。
2. 本文全面考察了视频大模型的后训练方法，包括监督微调、强化学习和测试时缩放三大支柱。
3. 通过系统分析，总结了关键设计原则和评估协议，并指出了奖励设计、可扩展性等方面的挑战。

## 📝 摘要（中文）

视频理解是计算机视觉领域最具挑战性的前沿方向，它要求模型能够推理复杂的时空关系、长期依赖和多模态证据。近年来，涌现出的视频大模型（Video-LMMs）通过将视觉编码器与强大的基于解码器的语言模型相结合，在视频理解任务中展现了卓越的能力。然而，将这些模型从基本的感知系统转变为复杂的推理引擎的关键阶段——后训练，在文献中仍然分散。本综述首次全面考察了Video-LMMs的后训练方法，包括三个基本支柱：带有思维链的监督微调（SFT）、基于可验证目标的强化学习（RL）以及通过增强推理计算实现的测试时缩放（TTS）。我们提出了一个结构化的分类法，阐明了这些技术的作用、相互联系和特定于视频的调整，解决了诸如时间定位、时空 grounding、长视频效率和多模态证据整合等独特挑战。通过对代表性方法的系统分析，我们综合了关键的设计原则、见解和评估协议，同时识别了奖励设计、可扩展性和成本-性能优化方面的关键开放挑战。我们进一步整理了必要的基准、数据集和指标，以促进对后训练有效性的严格评估。本综述旨在为研究人员和从业人员提供一个统一的框架，以提升Video-LMM的能力。

## 🔬 方法详解

**问题定义**：视频理解任务需要模型具备复杂的时空推理能力，处理长期依赖关系和多模态信息。现有的Video-LMMs虽然在视频理解方面取得了进展，但后训练方法分散，缺乏系统性的研究，难以充分挖掘模型的推理潜力。现有方法在时间定位、时空 grounding、长视频效率和多模态证据整合等方面存在挑战。

**核心思路**：本文的核心思路是对Video-LMMs的后训练方法进行系统性的梳理和分析，将其归纳为三个基本支柱：监督微调（SFT）、强化学习（RL）和测试时缩放（TTS）。通过对这三个支柱的深入研究，旨在为研究人员和从业人员提供一个统一的框架，以提升Video-LMM的能力。

**技术框架**：本文构建了一个结构化的分类法，用于阐明SFT、RL和TTS这三种后训练技术在Video-LMMs中的作用、相互联系和特定于视频的调整。该框架涵盖了时间定位、时空 grounding、长视频效率和多模态证据整合等关键方面。通过对代表性方法的分析，总结了关键的设计原则、见解和评估协议。

**关键创新**：本文的主要创新在于对Video-LMMs后训练方法的系统性研究和分类。首次全面考察了SFT、RL和TTS这三个基本支柱，并提出了一个结构化的分类法，阐明了这些技术在视频理解任务中的作用和相互关系。此外，本文还识别了奖励设计、可扩展性和成本-性能优化等关键开放挑战。

**关键设计**：本文对SFT、RL和TTS这三种后训练方法进行了深入分析，并总结了关键的设计原则。例如，在SFT中，强调使用思维链（chain-of-thought）来提高模型的推理能力；在RL中，强调设计可验证的目标来指导模型的学习；在TTS中，强调通过增强推理计算来提高模型的性能。此外，本文还整理了必要的基准、数据集和指标，以促进对后训练有效性的严格评估。

## 📊 实验亮点

本文对Video-LMMs的后训练方法进行了全面的综述，并提出了一个结构化的分类法。通过对代表性方法的分析，总结了关键的设计原则、见解和评估协议。此外，本文还识别了奖励设计、可扩展性和成本-性能优化等关键开放挑战，为未来的研究方向提供了指导。

## 🎯 应用场景

该研究成果可应用于智能监控、自动驾驶、视频搜索、智能客服等领域。通过提升视频大模型的推理能力，可以实现更精准的事件检测、行为识别、场景理解等功能，从而提高相关应用的智能化水平和用户体验。

## 📄 摘要（原文）

> Video understanding represents the most challenging frontier in computer vision, requiring models to reason about complex spatiotemporal relationships, long-term dependencies, and multimodal evidence. The recent emergence of Video-Large Multimodal Models (Video-LMMs), which integrate visual encoders with powerful decoder-based language models, has demonstrated remarkable capabilities in video understanding tasks. However, the critical phase that transforms these models from basic perception systems into sophisticated reasoning engines, post-training, remains fragmented across the literature. This survey provides the first comprehensive examination of post-training methodologies for Video-LMMs, encompassing three fundamental pillars: supervised fine-tuning (SFT) with chain-of-thought, reinforcement learning (RL) from verifiable objectives, and test-time scaling (TTS) through enhanced inference computation. We present a structured taxonomy that clarifies the roles, interconnections, and video-specific adaptations of these techniques, addressing unique challenges such as temporal localization, spatiotemporal grounding, long video efficiency, and multimodal evidence integration. Through systematic analysis of representative methods, we synthesize key design principles, insights, and evaluation protocols while identifying critical open challenges in reward design, scalability, and cost-performance optimization. We further curate essential benchmarks, datasets, and metrics to facilitate rigorous assessment of post-training effectiveness. This survey aims to provide researchers and practitioners with a unified framework for advancing Video-LMM capabilities. Additional resources and updates are maintained at: https://github.com/yunlong10/Awesome-Video-LMM-Post-Training

