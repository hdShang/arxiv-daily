---
layout: default
title: IKMo: Image-Keyframed Motion Generation with Trajectory-Pose Conditioned Motion Diffusion Model
---

# IKMo: Image-Keyframed Motion Generation with Trajectory-Pose Conditioned Motion Diffusion Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21146" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21146v1</a>
  <a href="https://arxiv.org/pdf/2505.21146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21146v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21146v1', 'IKMo: Image-Keyframed Motion Generation with Trajectory-Pose Conditioned Motion Diffusion Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Zhao, Yan Zhang, Xubo Yang

**分类**: cs.GR, cs.CV

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出IKMo以解决现有人体动作生成的局限性**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人体动作生成` `扩散模型` `多模态融合` `轨迹解耦` `姿态编码` `用户研究` `动画制作` `虚拟现实`

## 📋 核心要点

1. 现有方法在处理轨迹和姿态输入时，通常采用全局处理，导致生成的动作质量不高。
2. IKMo通过解耦轨迹和姿态输入，采用两阶段条件框架，提升了动作生成的精度和可控性。
3. 实验结果显示，IKMo在多个指标上超越了现有最先进的方法，且用户研究表明生成结果更符合用户期望。

## 📝 摘要（中文）

现有的人体动作生成方法在处理轨迹和姿态输入时，通常对两种模态进行全局处理，导致输出效果不佳。本文提出IKMo，一种基于扩散模型的图像关键帧动作生成方法，通过解耦轨迹和姿态输入，采用两阶段条件框架进行处理。实验结果表明，IKMo在HumanML3D和KIT-ML数据集上，在所有指标下均优于现有最先进的方法。此外，基于MLLM的代理被实现用于预处理模型输入，用户提供文本和关键帧图像后，代理提取运动描述、关键帧姿态和轨迹，作为优化输入。用户研究显示，MLLM代理的预处理使生成的动作更符合用户期望。我们相信，该方法提高了基于扩散模型的动作生成的保真度和可控性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有的人体动作生成方法在轨迹和姿态输入处理上的局限性，尤其是全局处理导致的输出质量不佳的问题。

**核心思路**：IKMo通过解耦轨迹和姿态输入，采用两阶段条件框架，分别优化和编码这两种输入，以提高生成动作的空间和语义保真度。

**技术框架**：整体架构分为两个阶段：第一阶段使用专门的优化模块对输入进行精细化处理；第二阶段则通过轨迹编码器和姿态编码器并行编码轨迹和姿态数据，最终由运动控制网络处理融合后的数据生成动作。

**关键创新**：IKMo的主要创新在于将轨迹和姿态输入解耦，并通过两阶段的条件框架进行处理，这与现有方法的全局处理方式形成了本质区别。

**关键设计**：在设计上，IKMo引入了专门的优化模块和两个独立的编码器，确保轨迹和姿态信息的独立性和有效性，同时使用运动控制网络来指导生成过程，提升了生成动作的质量。

## 📊 实验亮点

实验结果显示，IKMo在HumanML3D和KIT-ML数据集上，在所有评估指标上均超越了现有最先进的方法，具体提升幅度未知。此外，用户研究表明，使用MLLM代理进行预处理后，生成的动作更符合用户的期望，进一步验证了该方法的有效性。

## 🎯 应用场景

该研究在动画制作、虚拟现实和游戏开发等领域具有广泛的应用潜力。通过提高动作生成的保真度和可控性，IKMo可以帮助开发者更高效地创建自然流畅的人物动作，提升用户体验。此外，未来可能在机器人控制和人机交互等领域也能发挥重要作用。

## 📄 摘要（原文）

> Existing human motion generation methods with trajectory and pose inputs operate global processing on both modalities, leading to suboptimal outputs. In this paper, we propose IKMo, an image-keyframed motion generation method based on the diffusion model with trajectory and pose being decoupled. The trajectory and pose inputs go through a two-stage conditioning framework. In the first stage, the dedicated optimization module is applied to refine inputs. In the second stage, trajectory and pose are encoded via a Trajectory Encoder and a Pose Encoder in parallel. Then, motion with high spatial and semantic fidelity is guided by a motion ControlNet, which processes the fused trajectory and pose data. Experiment results based on HumanML3D and KIT-ML datasets demonstrate that the proposed method outperforms state-of-the-art on all metrics under trajectory-keyframe constraints. In addition, MLLM-based agents are implemented to pre-process model inputs. Given texts and keyframe images from users, the agents extract motion descriptions, keyframe poses, and trajectories as the optimized inputs into the motion generation model. We conducts a user study with 10 participants. The experiment results prove that the MLLM-based agents pre-processing makes generated motion more in line with users' expectation. We believe that the proposed method improves both the fidelity and controllability of motion generation by the diffusion model.

