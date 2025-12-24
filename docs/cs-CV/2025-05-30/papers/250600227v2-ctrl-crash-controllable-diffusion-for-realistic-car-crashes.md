---
layout: default
title: Ctrl-Crash: Controllable Diffusion for Realistic Car Crashes
---

# Ctrl-Crash: Controllable Diffusion for Realistic Car Crashes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00227" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00227v2</a>
  <a href="https://arxiv.org/pdf/2506.00227.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00227v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00227v2', 'Ctrl-Crash: Controllable Diffusion for Realistic Car Crashes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anthony Gosselin, Ge Ya Luo, Luis Lara, Florian Golemo, Derek Nowrouzezahrai, Liam Paull, Alexia Jolicoeur-Martineau, Christopher Pal

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-05-30 (更新: 2025-12-13)

**备注**: Under review at Pattern Recognition Letters

---

## 💡 一句话要点

**提出Ctrl-Crash以解决真实汽车碰撞模拟问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `汽车碰撞模拟` `视频扩散` `可控生成` `反事实生成` `交通安全`

## 📋 核心要点

1. 现有视频扩散技术在生成真实汽车碰撞图像时面临数据稀缺的挑战，限制了交通安全的提升。
2. Ctrl-Crash模型通过条件信号如边界框和碰撞类型，实现了对汽车碰撞视频的可控生成，支持反事实场景的生成。
3. 实验结果显示，Ctrl-Crash在视频质量评估指标上超越了现有扩散方法，展现出更高的物理真实感和视频质量。

## 📝 摘要（中文）

近年来，视频扩散技术取得了显著进展，但由于大多数驾驶数据集中事故事件的稀缺，生成真实的汽车碰撞图像仍然存在困难。为提高交通安全，本文提出了Ctrl-Crash，一个可控的汽车碰撞视频生成模型，能够根据边界框、碰撞类型和初始图像帧等信号进行条件生成。该方法支持反事实场景生成，输入的微小变化可以导致截然不同的碰撞结果。通过无分类器引导技术，我们实现了对每个条件信号独立可调的精细控制。实验结果表明，Ctrl-Crash在视频质量的定量指标（如FVD和JEDi）和基于人类评估的物理真实感和视频质量方面均达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频扩散技术在生成真实汽车碰撞图像时因数据稀缺而导致的困难，影响了交通安全的提升。

**核心思路**：Ctrl-Crash模型通过条件信号（如边界框和碰撞类型）进行控制，允许生成不同的碰撞场景，支持反事实生成，满足对事故模拟的需求。

**技术框架**：该模型的整体架构包括输入条件信号、生成网络和后处理模块。输入信号用于指导生成过程，生成网络负责创建视频帧，后处理模块则优化视频质量。

**关键创新**：Ctrl-Crash的主要创新在于引入了无分类器引导技术，允许对每个条件信号进行独立调节，从而实现更精细的控制和多样化的生成结果。

**关键设计**：模型设计中采用了可调节的引导尺度，损失函数结合了视频质量和物理真实感的评估，网络结构则基于最新的扩散模型架构进行优化。

## 📊 实验亮点

实验结果表明，Ctrl-Crash在视频质量评估上达到了最先进的性能，FVD和JEDi指标均优于现有的扩散方法，且在物理真实感和视频质量的人工评估中表现突出，显示出显著的提升幅度。

## 🎯 应用场景

Ctrl-Crash的研究成果在交通安全领域具有重要应用潜力，可以用于事故模拟、驾驶培训和自动驾驶系统的安全性评估。通过生成真实的碰撞场景，能够帮助研究人员和工程师更好地理解事故发生的机制，从而制定更有效的安全措施。未来，该技术还可以扩展到其他类型的动态场景生成中。

## 📄 摘要（原文）

> Video diffusion techniques have advanced significantly in recent years; however, they struggle to generate realistic imagery of car crashes due to the scarcity of accident events in most driving datasets. Improving traffic safety requires realistic and controllable accident simulations. To tackle the problem, we propose Ctrl-Crash, a controllable car crash video generation model that conditions on signals such as bounding boxes, crash types, and an initial image frame. Our approach enables counterfactual scenario generation where minor variations in input can lead to dramatically different crash outcomes. To support fine-grained control at inference time, we leverage classifier-free guidance with independently tunable scales for each conditioning signal. Ctrl-Crash achieves state-of-the-art performance across quantitative video quality metrics (e.g., FVD and JEDi) and qualitative measurements based on a human-evaluation of physical realism and video quality compared to prior diffusion-based methods.

