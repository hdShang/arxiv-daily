---
layout: default
title: "Reflective VLM Planning for Dual-Arm Desktop Cleaning: Bridging Open-Vocabulary Perception and Precise Manipulation"
---

# Reflective VLM Planning for Dual-Arm Desktop Cleaning: Bridging Open-Vocabulary Perception and Precise Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17328" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17328v1</a>
  <a href="https://arxiv.org/pdf/2506.17328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17328v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17328v1', 'Reflective VLM Planning for Dual-Arm Desktop Cleaning: Bridging Open-Vocabulary Perception and Precise Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yufan Liu, Yi Wu, Gweneth Ge, Haoliang Cheng, Rui Liu

**分类**: cs.RO

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出反射式视觉语言模型规划以解决双臂桌面清洁问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉语言模型` `双臂机器人` `桌面清洁` `开放词汇识别` `结构化记忆` `实时控制` `操作序列生成`

## 📋 核心要点

1. 现有方法在处理异质垃圾时，往往缺乏开放词汇识别和精确操作的能力，导致清洁效率低下。
2. 本文提出的层次化框架结合了反射式VLM规划和双臂执行，通过结构化场景表示来提升操作的灵活性和准确性。
3. 实验结果表明，系统在模拟场景中实现了87.2%的任务完成率，较静态VLM和单臂基线分别提高了28.8%和36.2%。

## 📝 摘要（中文）

桌面清洁需要对异质垃圾进行开放词汇识别和精确操作。本文提出了一种层次化框架，将反射式视觉语言模型（VLM）规划与双臂执行结合，通过结构化场景表示实现。Grounded-SAM2用于开放词汇检测，而增强记忆的VLM生成、评估和修订操作序列。这些序列被转换为五种原语的参数轨迹，由协调的Franka臂执行。在模拟场景中评估，我们的系统实现了87.2%的任务完成率，相较于静态VLM提高了28.8%，相较于单臂基线提高了36.2%。结构化记忆集成对于稳健、可泛化的操作至关重要，同时保持实时控制性能。

## 🔬 方法详解

**问题定义**：本文旨在解决桌面清洁中对异质垃圾的开放词汇识别和精确操作的挑战。现有方法在这方面表现不佳，导致清洁效率低下。

**核心思路**：通过引入反射式视觉语言模型（VLM）规划与双臂执行的结合，利用结构化场景表示来提升操作的灵活性和准确性，进而实现高效的桌面清洁。

**技术框架**：整体架构包括三个主要模块：首先，Grounded-SAM2用于开放词汇检测；其次，增强记忆的VLM负责生成、评估和修订操作序列；最后，这些序列被转换为参数轨迹，由协调的Franka臂执行。

**关键创新**：本文的主要创新在于结构化记忆的集成，使得操作更加稳健和可泛化，同时保持实时控制性能。这一设计与传统的静态VLM方法有本质区别。

**关键设计**：在技术细节上，采用了增强记忆机制以支持VLM的操作序列生成，并设计了特定的损失函数以优化轨迹生成过程，确保五种原语的高效执行。

## 📊 实验亮点

实验结果显示，系统在模拟场景中实现了87.2%的任务完成率，较静态VLM提高了28.8%，较单臂基线提高了36.2%。这一显著提升表明了结构化记忆集成在操作稳健性和实时控制中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括家庭自动化、服务机器人和工业清洁等场景。通过提升机器人在复杂环境中的操作能力，能够显著提高清洁效率和用户体验，未来可能推动智能家居和服务机器人技术的发展。

## 📄 摘要（原文）

> Desktop cleaning demands open-vocabulary recognition and precise manipulation for heterogeneous debris. We propose a hierarchical framework integrating reflective Vision-Language Model (VLM) planning with dual-arm execution via structured scene representation. Grounded-SAM2 facilitates open-vocabulary detection, while a memory-augmented VLM generates, critiques, and revises manipulation sequences. These sequences are converted into parametric trajectories for five primitives executed by coordinated Franka arms. Evaluated in simulated scenarios, our system achieving 87.2% task completion, a 28.8% improvement over static VLM and 36.2% over single-arm baselines. Structured memory integration proves crucial for robust, generalizable manipulation while maintaining real-time control performance.

