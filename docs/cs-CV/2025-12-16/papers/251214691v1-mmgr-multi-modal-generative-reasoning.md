---
layout: default
title: MMGR: Multi-Modal Generative Reasoning
---

# MMGR: Multi-Modal Generative Reasoning

**arXiv**: [2512.14691v1](https://arxiv.org/abs/2512.14691) | [PDF](https://arxiv.org/pdf/2512.14691.pdf)

**作者**: Zefan Cai, Haoyi Qiu, Tianyi Ma, Haozhe Zhao, Gengze Zhou, Kung-Hsiang Huang, Parisa Kordjamshidi, Minjia Zhang, Xiao Wen, Jiuxiang Gu, Nanyun Peng, Junjie Hu

**分类**: cs.CL, cs.CV

**发布日期**: 2025-12-16

**备注**: work in progress

---

## 💡 一句话要点

**提出MMGR多模态生成推理评估框架，以解决现有视频基础模型在物理、逻辑和空间约束方面缺乏可靠评估的问题。**

**关键词**: `多模态推理评估` `视频基础模型` `生成世界模型` `物理常识推理` `具身导航` `抽象推理` `基准测试` `因果推理`

## 📋 核心要点

1. 现有视频基础模型评估指标（如FVD）过于关注感知质量，忽视了物理、逻辑和空间推理失败，导致模型作为世界模拟器的可靠性不足。
2. 论文提出MMGR框架，基于五种推理能力（物理、逻辑、3D空间、2D空间、时序）构建原则性评估，覆盖抽象推理、具身导航和物理常识三大领域。
3. 基准测试显示，主流模型在物理常识任务上表现中等，但在抽象推理（如ARC-AGI准确率低于10%）和长时程空间规划上表现不佳，揭示了关键局限性。

## 📝 摘要（中文）

视频基础模型能够生成视觉逼真且时序连贯的内容，但其作为世界模拟器的可靠性取决于是否捕捉了物理、逻辑和空间约束。现有指标如弗雷歇视频距离（FVD）强调感知质量，却忽视了推理失败，包括违反因果关系、物理规律和全局一致性。我们引入了MMGR（多模态生成推理评估与基准），这是一个基于五种推理能力的原则性评估框架：物理推理、逻辑推理、3D空间推理、2D空间推理和时序推理。MMGR在三个领域评估生成推理：抽象推理（ARC-AGI、数独）、具身导航（真实世界3D导航与定位）和物理常识（运动和组合交互）。MMGR应用细粒度指标，要求视频和图像生成在整体上正确。我们对领先的视频模型（Veo-3、Sora-2、Wan-2.2）和图像模型（Nano-banana、Nano-banana Pro、GPT-4o-image、Qwen-image）进行了基准测试，揭示了跨领域的显著性能差距。模型在物理常识任务上表现中等，但在抽象推理上表现不佳（ARC-AGI准确率低于10%），并在具身设置中的长时程空间规划上遇到困难。我们的分析突出了当前模型的关键局限性，包括过度依赖感知数据、全局状态一致性弱，以及目标函数奖励视觉合理性而非因果正确性。MMGR提供了一个统一的诊断基准，并为推理感知的生成世界模型指明了路径。

## 🔬 方法详解

MMGR是一个多模态生成推理评估框架，整体框架基于五种核心推理能力（物理、逻辑、3D空间、2D空间、时序），设计细粒度评估指标，要求视频和图像生成在整体上正确。关键技术创新点在于将推理能力系统化分类，并应用于三个具体领域（抽象推理、具身导航、物理常识），通过统一基准进行跨模型比较。与现有方法的主要区别在于，现有方法如FVD侧重于感知质量评估，而MMGR强调推理正确性，能够诊断模型在因果关系、物理约束和全局一致性方面的失败，从而提供更全面的评估视角。

## 📊 实验亮点

实验结果显示，主流视频和图像模型在物理常识任务上表现中等，但在抽象推理任务（如ARC-AGI）上准确率低于10%，且在具身导航的长时程空间规划中表现不佳，揭示了模型在全局状态一致性和因果推理方面的显著缺陷。

## 🎯 应用场景

该研究可应用于视频生成模型的质量评估与优化、具身智能系统的导航与规划、以及物理模拟和游戏开发中的世界建模。它为开发更可靠的生成世界模型提供了诊断工具，有助于提升AI在复杂环境中的推理能力。

## 📄 摘要（原文）

> Video foundation models generate visually realistic and temporally coherent content, but their reliability as world simulators depends on whether they capture physical, logical, and spatial constraints. Existing metrics such as Frechet Video Distance (FVD) emphasize perceptual quality and overlook reasoning failures, including violations of causality, physics, and global consistency. We introduce MMGR (Multi-Modal Generative Reasoning Evaluation and Benchmark), a principled evaluation framework based on five reasoning abilities: Physical, Logical, 3D Spatial, 2D Spatial, and Temporal. MMGR evaluates generative reasoning across three domains: Abstract Reasoning (ARC-AGI, Sudoku), Embodied Navigation (real-world 3D navigation and localization), and Physical Commonsense (sports and compositional interactions). MMGR applies fine-grained metrics that require holistic correctness across both video and image generation. We benchmark leading video models (Veo-3, Sora-2, Wan-2.2) and image models (Nano-banana, Nano-banana Pro, GPT-4o-image, Qwen-image), revealing strong performance gaps across domains. Models show moderate success on Physical Commonsense tasks but perform poorly on Abstract Reasoning (below 10 percent accuracy on ARC-AGI) and struggle with long-horizon spatial planning in embodied settings. Our analysis highlights key limitations in current models, including overreliance on perceptual data, weak global state consistency, and objectives that reward visual plausibility over causal correctness. MMGR offers a unified diagnostic benchmark and a path toward reasoning-aware generative world models.

