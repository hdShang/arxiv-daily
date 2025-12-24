---
layout: default
title: TrackVLA: Embodied Visual Tracking in the Wild
---

# TrackVLA: Embodied Visual Tracking in the Wild

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23189" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23189v1</a>
  <a href="https://arxiv.org/pdf/2505.23189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23189v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23189v1', 'TrackVLA: Embodied Visual Tracking in the Wild')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoan Wang, Jiazhao Zhang, Minghan Li, Jiahang Liu, Anqi Li, Kui Wu, Fangwei Zhong, Junzhi Yu, Zhizheng Zhang, He Wang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-05-29

**🔗 代码/项目**: [PROJECT_PAGE](https://pku-epic.github.io/TrackVLA-web)

---

## 💡 一句话要点

**提出TrackVLA以解决动态环境中的视觉跟踪问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身视觉跟踪` `视觉-语言-动作` `动态环境` `目标识别` `轨迹规划` `深度学习` `机器人导航`

## 📋 核心要点

1. 现有方法通常将目标识别与轨迹规划模块化，导致在动态环境中处理复杂场景时的性能不足。
2. TrackVLA通过共享的语言模型骨干，结合语言建模头进行识别和基于锚点的扩散模型进行轨迹规划，提升了两者的协同效果。
3. 在多个公共基准测试中，TrackVLA以零样本方式显著超越现有方法，且在真实场景中以10 FPS的速度保持鲁棒性。

## 📝 摘要（中文）

具身视觉跟踪是具身人工智能中的一项基础技能，使得智能体能够在动态环境中仅依靠自我中心视觉跟随特定目标。该任务具有挑战性，因为它需要在严重遮挡和高场景动态条件下进行准确的目标识别和有效的轨迹规划。现有方法通常通过将识别与规划模块化分开来解决这一挑战。本文提出了TrackVLA，一个视觉-语言-动作（VLA）模型，学习物体识别与轨迹规划之间的协同作用。通过构建具身视觉跟踪基准（EVT-Bench）并收集多样化的识别样本，TrackVLA在合成和真实环境中进行了广泛实验，展示了最先进的性能和强大的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决具身视觉跟踪中的目标识别与轨迹规划的协同问题。现有方法在动态环境中面临严重遮挡和高场景动态时的性能不足。

**核心思路**：TrackVLA通过整合视觉、语言和动作的模型，利用共享的语言模型骨干，增强目标识别与轨迹规划的协同作用，从而提高整体性能。

**技术框架**：TrackVLA的整体架构包括两个主要模块：一个用于目标识别的语言建模头和一个用于轨迹规划的基于锚点的扩散模型。这种设计使得模型能够在处理复杂场景时更为高效。

**关键创新**：TrackVLA的核心创新在于将目标识别与轨迹规划的过程进行深度融合，而不是简单的模块化分开。这种方法使得模型在动态环境中表现出更强的适应性和鲁棒性。

**关键设计**：在训练过程中，TrackVLA使用了构建的具身视觉跟踪基准（EVT-Bench），包含170万样本，采用了特定的损失函数和网络结构，以确保模型在多样化场景中的有效性。通过这些设计，模型在真实世界的应用中表现出色。

## 📊 实验亮点

TrackVLA在多个公共基准测试中表现出色，尤其是在零样本条件下，其性能显著超越现有方法。实验结果显示，TrackVLA在真实场景中以10 FPS的速度处理高动态和遮挡情况，展现出强大的鲁棒性和泛化能力。

## 🎯 应用场景

TrackVLA的研究成果在多个领域具有潜在应用价值，包括机器人导航、智能监控和增强现实等。通过提高动态环境中的目标跟踪能力，能够为智能体提供更为精准的决策支持，推动具身人工智能的发展。未来，TrackVLA可能在自主驾驶和人机交互等领域发挥重要作用。

## 📄 摘要（原文）

> Embodied visual tracking is a fundamental skill in Embodied AI, enabling an agent to follow a specific target in dynamic environments using only egocentric vision. This task is inherently challenging as it requires both accurate target recognition and effective trajectory planning under conditions of severe occlusion and high scene dynamics. Existing approaches typically address this challenge through a modular separation of recognition and planning. In this work, we propose TrackVLA, a Vision-Language-Action (VLA) model that learns the synergy between object recognition and trajectory planning. Leveraging a shared LLM backbone, we employ a language modeling head for recognition and an anchor-based diffusion model for trajectory planning. To train TrackVLA, we construct an Embodied Visual Tracking Benchmark (EVT-Bench) and collect diverse difficulty levels of recognition samples, resulting in a dataset of 1.7 million samples. Through extensive experiments in both synthetic and real-world environments, TrackVLA demonstrates SOTA performance and strong generalizability. It significantly outperforms existing methods on public benchmarks in a zero-shot manner while remaining robust to high dynamics and occlusion in real-world scenarios at 10 FPS inference speed. Our project page is: https://pku-epic.github.io/TrackVLA-web.

