---
layout: default
title: Towards High-Consistency Embodied World Model with Multi-View Trajectory Videos
---

# Towards High-Consistency Embodied World Model with Multi-View Trajectory Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12882" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12882v2</a>
  <a href="https://arxiv.org/pdf/2511.12882.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12882v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.12882v2', 'Towards High-Consistency Embodied World Model with Multi-View Trajectory Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taiyi Su, Jian Zhu, Yaxuan Li, Chong Ma, Zitai Huang, Hanli Wang, Yi Xu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-17 (更新: 2025-11-19)

**备注**: 15 pages, 23 figures

---

## 💡 一句话要点

**提出MTV-World，利用多视角轨迹视频实现高一致性的具身世界模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `具身世界模型` `多视角学习` `轨迹视频` `视觉运动预测` `机器人控制` `物理交互` `自动评估`

## 📋 核心要点

1. 现有具身世界模型在将低级动作转化为精确机器人运动时存在困难，导致预测与真实物理交互不一致。
2. MTV-World利用多视角轨迹视频作为控制信号，补偿空间信息损失，实现更精确的视觉运动预测。
3. 论文提出自动评估流程，并使用Jaccard指数评估空间一致性，实验证明模型在双臂场景中表现出色。

## 📝 摘要（中文）

具身世界模型旨在通过视觉观察和动作来预测物理世界并与之交互。然而，现有模型难以将低级动作（例如，关节位置）准确地转化为预测帧中精确的机器人运动，导致与真实物理交互的不一致。为了解决这些限制，我们提出了MTV-World，一种具身世界模型，它引入了多视角轨迹视频控制，以实现精确的视觉运动预测。具体来说，我们没有直接使用低级动作进行控制，而是采用通过相机内参和外参以及笛卡尔空间变换获得的轨迹视频作为控制信号。然而，将3D原始动作投影到2D图像上不可避免地会导致空间信息的丢失，使得单视角不足以进行精确的交互建模。为了克服这个问题，我们引入了一个多视角框架，该框架补偿了空间信息的丢失，并确保与物理世界的高度一致性。MTV-World基于多视角轨迹视频作为输入，并以每个视角的初始帧为条件来预测未来帧。此外，为了系统地评估机器人运动精度和物体交互准确性，我们开发了一个自动评估流程，利用多模态大型模型和参考视频对象分割模型。为了衡量空间一致性，我们将其定义为一个物体位置匹配问题，并采用Jaccard指数作为评估指标。大量的实验表明，MTV-World在复杂的双臂场景中实现了精确的控制执行和准确的物理交互建模。

## 🔬 方法详解

**问题定义**：现有具身世界模型难以准确地将低级动作指令（如关节位置）转化为预测视频帧中精确的机器人运动，导致预测的物理交互与真实世界不一致。这种不一致性限制了模型在复杂机器人任务中的应用，例如双臂协同操作。

**核心思路**：论文的核心思路是使用多视角轨迹视频作为控制信号，替代直接使用低级动作。轨迹视频包含了更丰富的空间信息，能够更准确地描述机器人的运动轨迹。多视角的设计弥补了单视角投影造成的空间信息损失，从而提高预测的准确性和一致性。

**技术框架**：MTV-World的整体框架包括以下几个主要模块：1) 多视角轨迹视频生成模块：利用相机参数和笛卡尔空间变换将机器人动作转化为多视角轨迹视频。2) 视频预测模块：基于多视角轨迹视频和初始帧，预测未来的视频帧。3) 自动评估模块：利用多模态大型模型和参考视频对象分割模型，自动评估机器人运动精度和物体交互准确性。

**关键创新**：该论文的关键创新在于：1) 使用多视角轨迹视频作为控制信号，提高了视觉运动预测的精度和一致性。2) 提出了一个自动评估流程，能够系统地评估机器人运动精度和物体交互准确性。3) 将空间一致性定义为一个物体位置匹配问题，并采用Jaccard指数作为评估指标。

**关键设计**：轨迹视频的生成依赖于精确的相机标定和坐标系转换。视频预测模块可能采用Transformer或RNN等序列模型。自动评估模块需要选择合适的视觉分割模型和多模态大模型。Jaccard指数用于衡量预测物体位置与真实物体位置的重叠程度。

## 📊 实验亮点

实验结果表明，MTV-World在复杂的双臂场景中实现了精确的控制执行和准确的物理交互建模。论文提出的自动评估流程能够有效地评估模型的性能，并为未来的研究提供参考。具体性能数据未知，但论文强调了在空间一致性方面的显著提升。

## 🎯 应用场景

该研究成果可应用于各种需要精确控制和物理交互的机器人任务，例如：工业自动化、医疗手术机器人、家庭服务机器人等。通过提高机器人对环境的理解和预测能力，可以实现更安全、更高效的人机协作，并拓展机器人的应用范围。

## 📄 摘要（原文）

> Embodied world models aim to predict and interact with the physical world through visual observations and actions. However, existing models struggle to accurately translate low-level actions (e.g., joint positions) into precise robotic movements in predicted frames, leading to inconsistencies with real-world physical interactions. To address these limitations, we propose MTV-World, an embodied world model that introduces Multi-view Trajectory-Video control for precise visuomotor prediction. Specifically, instead of directly using low-level actions for control, we employ trajectory videos obtained through camera intrinsic and extrinsic parameters and Cartesian-space transformation as control signals. However, projecting 3D raw actions onto 2D images inevitably causes a loss of spatial information, making a single view insufficient for accurate interaction modeling. To overcome this, we introduce a multi-view framework that compensates for spatial information loss and ensures high-consistency with physical world. MTV-World forecasts future frames based on multi-view trajectory videos as input and conditioning on an initial frame per view. Furthermore, to systematically evaluate both robotic motion precision and object interaction accuracy, we develop an auto-evaluation pipeline leveraging multimodal large models and referring video object segmentation models. To measure spatial consistency, we formulate it as an object location matching problem and adopt the Jaccard Index as the evaluation metric. Extensive experiments demonstrate that MTV-World achieves precise control execution and accurate physical interaction modeling in complex dual-arm scenarios.

