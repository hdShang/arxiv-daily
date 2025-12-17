---
layout: default
title: DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos
---

# DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos

**arXiv**: [2512.14217v1](https://arxiv.org/abs/2512.14217) | [PDF](https://arxiv.org/pdf/2512.14217.pdf)

**作者**: Yang Bai, Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Ziyuan Liu, Gitta Kutyniok

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出DRAW2ACT框架，通过深度感知轨迹条件视频生成，提升机器人演示的可控性和一致性。**

**关键词**: `视频扩散模型` `轨迹条件生成` `深度感知` `多模态融合` `机器人演示` `时空一致性` `跨模态注意力` `具身AI`

## 📋 核心要点

1. 现有方法依赖2D轨迹或单模态条件，导致机器人演示视频的可控性和一致性受限。
2. DRAW2ACT从轨迹提取深度、语义等多模态表示，并注入扩散模型，联合生成RGB和深度视频。
3. 实验显示，DRAW2ACT在视觉保真度、一致性和操作成功率上均优于基线方法。

## 📝 摘要（中文）

视频扩散模型为具身AI提供了强大的真实世界模拟器，但在机器人操作的可控性方面仍有限制。近期基于轨迹条件的视频生成工作填补了这一空白，但通常依赖于2D轨迹或单模态条件，限制了其生成可控且一致的机器人演示的能力。我们提出了DRAW2ACT，这是一个深度感知轨迹条件视频生成框架，它从输入轨迹中提取多个正交表示，捕捉深度、语义、形状和运动，并将它们注入扩散模型。此外，我们提出联合生成空间对齐的RGB和深度视频，利用跨模态注意力机制和深度监督来增强时空一致性。最后，我们引入了一个基于生成的RGB和深度序列的多模态策略模型，以回归机器人的关节角度。在Bridge V2、Berkeley Autolab和模拟基准测试上的实验表明，与现有基线相比，DRAW2ACT实现了更优的视觉保真度和一致性，同时获得了更高的操作成功率。

## 🔬 方法详解

DRAW2ACT是一个深度感知轨迹条件视频生成框架，整体基于扩散模型。关键创新点包括：从输入轨迹提取深度、语义、形状和运动等多模态正交表示，通过跨模态注意力机制联合生成空间对齐的RGB和深度视频，并引入深度监督增强时空一致性。与现有方法的主要区别在于，它结合了深度信息，避免了仅依赖2D轨迹的局限性，从而提升了生成视频的可控性和一致性。

## 📊 实验亮点

在Bridge V2、Berkeley Autolab和模拟基准测试中，DRAW2ACT在视觉保真度和一致性方面表现优异，操作成功率显著高于现有基线，验证了其方法的有效性。

## 🎯 应用场景

该研究可应用于机器人演示视频生成、具身AI模拟训练和自动化操作任务，通过生成高质量的多模态视频，帮助机器人学习复杂操作技能，提升实际部署中的成功率和效率。

## 📄 摘要（原文）

> Video diffusion models provide powerful real-world simulators for embodied AI but remain limited in controllability for robotic manipulation. Recent works on trajectory-conditioned video generation address this gap but often rely on 2D trajectories or single modality conditioning, which restricts their ability to produce controllable and consistent robotic demonstrations. We present DRAW2ACT, a depth-aware trajectory-conditioned video generation framework that extracts multiple orthogonal representations from the input trajectory, capturing depth, semantics, shape and motion, and injects them into the diffusion model. Moreover, we propose to jointly generate spatially aligned RGB and depth videos, leveraging cross-modality attention mechanisms and depth supervision to enhance the spatio-temporal consistency. Finally, we introduce a multimodal policy model conditioned on the generated RGB and depth sequences to regress the robot's joint angles. Experiments on Bridge V2, Berkeley Autolab, and simulation benchmarks show that DRAW2ACT achieves superior visual fidelity and consistency while yielding higher manipulation success rates compared to existing baselines.

