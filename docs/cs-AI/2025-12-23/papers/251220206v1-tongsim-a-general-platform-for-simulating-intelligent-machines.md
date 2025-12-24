---
layout: default
title: TongSIM: A General Platform for Simulating Intelligent Machines
---

# TongSIM: A General Platform for Simulating Intelligent Machines

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20206" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20206v1</a>
  <a href="https://arxiv.org/pdf/2512.20206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20206v1', 'TongSIM: A General Platform for Simulating Intelligent Machines')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Sun, Kunlun Wu, Chuanjian Fu, Zeming Song, Langyong Shi, Zihe Xue, Bohan Jing, Ying Yang, Xiaomeng Gao, Aijia Li, Tianyu Guo, Huiying Li, Xueyuan Yang, Rongkai Liu, Xinyi He, Yuxi Wang, Yue Li, Mingyuan Liu, Yujie Lu, Hongzhao Xie, Shiyun Zhao, Bo Dai, Wei Wang, Tao Yuan, Song-Chun Zhu, Yujia Peng, Zhenliang Zhang

**分类**: cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**TongSIM：通用智能机器模拟平台，支持具身智能体训练与评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `模拟平台` `多模态学习` `人机协作` `机器人导航`

## 📋 核心要点

1. 现有模拟平台设计狭隘，难以支持从低级导航到高级人机协作等复杂任务。
2. TongSIM 平台提供高保真、通用的模拟环境，支持具身智能体的训练和评估。
3. TongSIM 提供多样化的室内外场景、全面的评估框架和灵活的定制功能。

## 📝 摘要（中文）

随着人工智能，特别是多模态大语言模型（MLLM）的快速发展，研究重点正从单模态文本处理转向更复杂的多模态和具身人工智能领域。具身智能侧重于在逼真的模拟环境中训练智能体，利用物理交互和动作反馈，而不是传统的标注数据集。然而，现有的大多数模拟平台仍然设计狭隘，各自针对特定任务。一个能够支持从低级具身导航到高级复合活动（如多智能体社会模拟和人机协作）的通用训练环境仍然很大程度上不可用。为了弥合这一差距，我们推出了 TongSIM，这是一个高保真、通用的平台，用于训练和评估具身智能体。TongSIM 提供了实际优势，提供了 100 多个多样化的多房间室内场景以及一个开放的、交互丰富的室外城镇模拟，确保了广泛的研究适用性。其全面的评估框架和基准能够精确评估智能体的能力，如感知、认知、决策、人机协作以及空间和社会推理。凭借定制场景、任务自适应保真度、多样化的智能体类型和动态环境模拟等功能，TongSIM 为研究人员提供了灵活性和可扩展性，作为一个统一的平台，加速了通用具身智能的训练、评估和发展。

## 🔬 方法详解

**问题定义**：现有具身智能模拟平台通常针对特定任务设计，缺乏通用性和灵活性，难以支持复杂的多智能体交互、人机协作等高级任务。这限制了具身智能体的训练和评估，阻碍了通用具身智能的发展。

**核心思路**：TongSIM 的核心思路是构建一个高保真、通用的模拟平台，提供多样化的场景、灵活的配置和全面的评估框架，从而支持各种具身智能任务的训练和评估。通过提供丰富的交互环境和可定制的智能体类型，TongSIM 旨在加速通用具身智能的研究。

**技术框架**：TongSIM 平台包含以下主要模块：1) 场景生成模块，提供多样化的室内外场景，包括多房间室内环境和开放式城镇环境；2) 智能体管理模块，支持不同类型的智能体，包括机器人、人类等，并提供定制化功能；3) 物理引擎模块，模拟真实的物理交互，包括碰撞、重力等；4) 感知模块，模拟智能体的感知能力，包括视觉、听觉等；5) 评估模块，提供全面的评估指标，用于评估智能体的性能。

**关键创新**：TongSIM 的关键创新在于其通用性和灵活性。它不仅提供了多样化的场景和智能体类型，还支持任务自适应的保真度调整，允许研究人员根据任务的复杂程度选择合适的模拟精度。此外，TongSIM 还提供了全面的评估框架，可以精确评估智能体的感知、认知、决策、人机协作以及空间和社会推理能力。

**关键设计**：TongSIM 采用模块化设计，各个模块之间相互独立，易于扩展和定制。场景生成模块支持导入自定义场景，智能体管理模块支持自定义智能体类型和行为。物理引擎模块采用开源的 Bullet 物理引擎，感知模块支持多种传感器模拟，包括摄像头、麦克风、激光雷达等。评估模块提供多种评估指标，包括成功率、路径长度、时间消耗等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20206v1/tongsim/figures/teaser.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20206v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20206v1/tongsim/figures/room_freq.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TongSIM 提供了超过 100 个多样化的多房间室内场景以及一个开放的、交互丰富的室外城镇模拟。该平台还提供了一套全面的评估框架和基准，能够精确评估智能体的感知、认知、决策、人机协作以及空间和社会推理能力。具体性能数据和对比基线信息未知。

## 🎯 应用场景

TongSIM 可应用于机器人导航、人机协作、多智能体社会模拟、自动驾驶等领域。该平台能够加速具身智能体的训练和评估，推动相关技术的发展，并最终应用于智能家居、智能交通、智能制造等实际场景，提升生产效率和生活质量。

## 📄 摘要（原文）

> As artificial intelligence (AI) rapidly advances, especially in multimodal large language models (MLLMs), research focus is shifting from single-modality text processing to the more complex domains of multimodal and embodied AI. Embodied intelligence focuses on training agents within realistic simulated environments, leveraging physical interaction and action feedback rather than conventionally labeled datasets. Yet, most existing simulation platforms remain narrowly designed, each tailored to specific tasks. A versatile, general-purpose training environment that can support everything from low-level embodied navigation to high-level composite activities, such as multi-agent social simulation and human-AI collaboration, remains largely unavailable. To bridge this gap, we introduce TongSIM, a high-fidelity, general-purpose platform for training and evaluating embodied agents. TongSIM offers practical advantages by providing over 100 diverse, multi-room indoor scenarios as well as an open-ended, interaction-rich outdoor town simulation, ensuring broad applicability across research needs. Its comprehensive evaluation framework and benchmarks enable precise assessment of agent capabilities, such as perception, cognition, decision-making, human-robot cooperation, and spatial and social reasoning. With features like customized scenes, task-adaptive fidelity, diverse agent types, and dynamic environmental simulation, TongSIM delivers flexibility and scalability for researchers, serving as a unified platform that accelerates training, evaluation, and advancement toward general embodied intelligence.

