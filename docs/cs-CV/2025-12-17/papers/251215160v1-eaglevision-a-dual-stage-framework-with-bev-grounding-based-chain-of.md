---
layout: default
title: EagleVision: A Dual-Stage Framework with BEV-grounding-based Chain-of-Thought for Spatial Intelligence
---

# EagleVision: A Dual-Stage Framework with BEV-grounding-based Chain-of-Thought for Spatial Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15160" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15160v1</a>
  <a href="https://arxiv.org/pdf/2512.15160.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15160v1" onclick="toggleFavorite(this, '2512.15160v1', 'EagleVision: A Dual-Stage Framework with BEV-grounding-based Chain-of-Thought for Spatial Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaxu Wan, Xu Wang, Mengwei Xie, Hang Zhang, Mu Xu, Yang Han, Hong Zhang, Ding Yuan, Yifan Yang

**分类**: cs.CV

**发布日期**: 2025-12-17

**备注**: 13 pages, 7 figures, 6 tables

---

## 💡 一句话要点

**EagleVision：基于BEV的链式思考双阶段框架，提升空间智能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间智能` `链式思考` `BEV感知` `强化学习` `长视频理解`

## 📋 核心要点

1. 现有方法在空间一致性、视角多样性和证据追溯方面存在不足，无法有效进行空间推理。
2. EagleVision通过双阶段框架，利用宏观感知选择关键帧，微观验证进行姿态查询，实现空间链式思考。
3. EagleVision在VSI-Bench上取得了领先性能，证明了其在空间理解方面的有效性和泛化能力。

## 📝 摘要（中文）

现有的空间智能方法通常将3D线索附加到2D推理流程中，或将MLLM与黑盒重建模块耦合，导致空间一致性弱、视角多样性有限，且证据链无法追溯到支持视图。类似于“图像思考”的框架虽然展示了通过假设形成与主动获取视觉证据交错实现逐步多模态推理的可能性，但未解决空间链式思考（CoT）中的三个关键挑战：在严格的token预算下构建全局空间感知，将3D假设与视频帧显式关联以进行验证，以及设计用于强化学习的空间对齐奖励。为了解决这些问题，我们提出了EagleVision，一个通过宏观感知和微观验证进行渐进式空间认知的双阶段框架。在宏观感知阶段，EagleVision采用语义-视角融合行列式点过程（SPF-DPP），在固定token预算下从长视频中选择一组紧凑的、具有几何和语义信息的关键帧。在微观验证阶段，我们将空间CoT形式化为基于BEV的姿态查询：智能体迭代地预测BEV平面上的姿态，检索最近的真实帧，并通过强化学习进行训练，其空间对齐奖励用于评估预测姿态与观察到的视图之间的一致性。在VSI-Bench上，EagleVision在开源视觉语言模型中实现了最先进的性能，展示了强大且可泛化的空间理解能力。

## 🔬 方法详解

**问题定义**：现有空间智能方法依赖于2D推理或黑盒3D重建，导致空间信息利用不足，推理过程缺乏透明度和可解释性。尤其是在长视频场景下，如何高效地利用有限的计算资源进行全局空间感知是一个挑战。

**核心思路**：EagleVision的核心在于将空间推理分解为宏观感知和微观验证两个阶段。宏观感知负责从长视频中提取关键信息，构建全局空间表征；微观验证则通过基于BEV的姿态查询，将3D假设与实际图像帧关联，进行精细化的空间推理。这种分阶段的方法既能有效利用计算资源，又能提高空间推理的准确性和可解释性。

**技术框架**：EagleVision框架包含两个主要阶段：宏观感知和微观验证。宏观感知阶段使用语义-视角融合行列式点过程（SPF-DPP）从长视频中选择关键帧，该过程考虑了帧的几何和语义信息，以确保选择的帧具有代表性。微观验证阶段将空间CoT形式化为基于BEV的姿态查询，智能体迭代地预测BEV平面上的姿态，并检索最近的真实帧。通过强化学习，智能体学习预测准确的姿态，从而实现空间推理。

**关键创新**：EagleVision的关键创新在于其双阶段框架和基于BEV的姿态查询方法。双阶段框架有效地将全局空间感知和局部精细推理分离，提高了效率和准确性。基于BEV的姿态查询方法将3D空间信息显式地融入到推理过程中，增强了空间一致性。此外，使用空间对齐奖励进行强化学习，使得智能体能够学习到与真实世界对齐的空间表征。

**关键设计**：SPF-DPP的关键在于其行列式点过程，用于选择具有代表性的关键帧。BEV-grounded pose querying的关键在于如何设计奖励函数，论文中使用空间对齐奖励，鼓励预测的姿态与观察到的视图保持一致。强化学习算法的选择也至关重要，需要选择适合连续动作空间的算法。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15160v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15160v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15160v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EagleVision在VSI-Bench数据集上取得了state-of-the-art的性能，超越了现有的开源视觉语言模型。实验结果表明，EagleVision在空间理解方面具有显著优势，能够有效地处理长视频场景下的空间推理任务。具体的性能数据需要在论文中查找。

## 🎯 应用场景

EagleVision在机器人导航、自动驾驶、视频监控等领域具有广泛的应用前景。它可以帮助机器人更好地理解周围环境，进行更精确的定位和导航。在自动驾驶领域，可以提高车辆对复杂交通场景的感知能力。在视频监控领域，可以实现更智能的事件检测和行为分析。

## 📄 摘要（原文）

> Recent spatial intelligence approaches typically attach 3D cues to 2D reasoning pipelines or couple MLLMs with black-box reconstruction modules, leading to weak spatial consistency, limited viewpoint diversity, and evidence chains that cannot be traced back to supporting views. Frameworks for "thinking with images" (e.g., ChatGPT-o3 and DeepEyes) show that stepwise multimodal reasoning can emerge by interleaving hypothesis formation with active acquisition of visual evidence, but they do not address three key challenges in spatial Chain-of-Thought (CoT): building global space perception under strict token budgets, explicitly associating 3D hypotheses with video frames for verification, and designing spatially grounded rewards for reinforcement learning. To address these issues, we present EagleVision, a dual-stage framework for progressive spatial cognition through macro perception and micro verification. In the macro perception stage, EagleVision employs a semantics-perspective-fusion determinantal point process (SPF-DPP) to select a compact set of geometry- and semantics-aware keyframes from long videos under a fixed token budget. In the micro verification stage, we formalize spatial CoT as BEV-grounded pose querying: the agent iteratively predicts poses on a BEV plane, retrieves the nearest real frames, and is trained purely by reinforcement learning with a spatial grounding reward that scores the consistency between predicted poses and observed views. On VSI-Bench, EagleVision achieves state-of-the-art performance among open-source vision-language models, demonstrating strong and generalizable spatial understanding.

