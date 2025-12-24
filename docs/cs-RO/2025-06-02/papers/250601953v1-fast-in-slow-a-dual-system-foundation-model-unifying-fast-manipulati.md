---
layout: default
title: "Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning"
---

# Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01953" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01953v1</a>
  <a href="https://arxiv.org/pdf/2506.01953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01953v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01953v1', 'Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Chen, Jiaming Liu, Chenyang Gu, Zhuoyang Liu, Renrui Zhang, Xiaoqi Li, Xiao He, Yandong Guo, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng

**分类**: cs.RO

**发布日期**: 2025-06-02

---

## 💡 一句话要点

**提出Fast-in-Slow模型以解决机器人操控中的执行频率与推理效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操控` `视觉-语言模型` `双系统模型` `高频执行` `推理效率` `动作生成` `异质模态输入`

## 📋 核心要点

1. 现有的机器人操控方法在执行频率和推理效率上存在显著不足，导致操作的实时性和准确性受限。
2. 本文提出的Fast-in-Slow模型通过将系统1的执行模块嵌入到系统2中，部分共享参数，从而实现高频执行与推理的协调。
3. 实验结果表明，FiS-VLA在模拟和现实任务中分别提高了8%和11%的成功率，控制频率达到117.7 Hz，显著优于现有方法。

## 📝 摘要（中文）

机器人操控中的政策泛化和执行效率是两大关键挑战。尽管近期的基础政策受益于互联网规模的预训练视觉-语言模型（VLM）的常识推理能力，但其执行频率往往较低。为了解决这一困境，基于卡尼曼理论的双系统方法被提出，利用VLM为基础的系统2模型进行高层推理，同时使用独立的系统1动作模型实现实时控制。然而，现有设计将两个系统保持为独立模型，限制了系统1充分利用系统2的预训练知识。本文提出了Fast-in-Slow（FiS），一个统一的双系统视觉-语言-动作（VLA）模型，通过部分共享参数将系统1嵌入VLM为基础的系统2中。这一创新范式不仅实现了系统1的高频执行，还促进了推理与执行组件之间的协调。FiS-VLA在模拟和现实任务中分别比之前的最先进方法提高了8%和11%的平均成功率，同时以117.7 Hz的控制频率实现了动作分块为八。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操控中政策泛化与执行效率的矛盾，现有方法由于系统1与系统2的独立性，无法充分利用预训练知识，导致执行频率低下。

**核心思路**：提出的Fast-in-Slow模型通过将系统1的执行模块嵌入到VLM为基础的系统2中，部分共享参数，实现高频执行与推理的有效协调。

**技术框架**：FiS-VLA模型包括两个主要模块：系统1负责快速动作生成，系统2负责高层次的推理。两个系统通过异步操作频率和异质模态输入进行协同工作。

**关键创新**：FiS模型的核心创新在于将两个系统整合为一个统一的模型，使得系统1能够利用系统2的丰富知识，从而提高执行频率和推理效率。

**关键设计**：模型设计中采用了双重意识共同训练策略，确保系统1具备动作生成能力，同时保留系统2的上下文推理表示。

## 📊 实验亮点

FiS-VLA模型在实验中表现出色，模拟任务中平均成功率提高了8%，现实任务中提高了11%。此外，模型实现了117.7 Hz的控制频率，动作分块设置为八，展现了优越的实时控制能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化生产线和服务机器人等，能够显著提升机器人在复杂环境中的操作能力和效率。未来，该模型有望推动更高效的机器人系统开发，促进人机协作的智能化进程。

## 📄 摘要（原文）

> Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation. While recent foundation policies benefit from the common-sense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency. To mitigate this dilemma, dual-system approaches, inspired by Kahneman's theory, have been proposed to leverage a VLM-based System 2 model handling high-level reasoning and a separate System 1 action model ensuring real-time control. However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2. In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing parameters. This innovative paradigm not only enables high-frequency execution in System 1 but also facilitates coordination between the reasoning and execution components within a single foundation model of System 2. Given their fundamentally distinct roles within FiS-VLA, we design the two systems to incorporate heterogeneous modality inputs alongside asynchronous operating frequencies, enabling both fast and precise manipulation. To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's contextual reasoning representation. For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in real-world tasks in terms of average success rate, while achieving a 117.7 Hz control frequency with action chunk set to eight. Project web page: fast-in-slow.github.io.

