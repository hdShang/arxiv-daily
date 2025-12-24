---
layout: default
title: "MagicWorld: Interactive Geometry-driven Video World Exploration"
---

# MagicWorld: Interactive Geometry-driven Video World Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18886" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18886v1</a>
  <a href="https://arxiv.org/pdf/2511.18886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18886v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18886v1', 'MagicWorld: Interactive Geometry-driven Video World Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangyuan Li, Siming Zheng, Shuolin Xu, Jinwei Chen, Bo Li, Xiaobin Hu, Lei Zhao, Peng-Tao Jiang

**分类**: cs.CV

**发布日期**: 2025-11-24

---

## 💡 一句话要点

**MagicWorld：提出几何引导的交互式视频世界探索模型，提升场景稳定性和连续性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `交互式视频生成` `世界模型` `3D几何约束` `历史信息检索` `场景演化`

## 📋 核心要点

1. 现有交互式视频世界模型未能充分利用3D几何信息，导致视角变化时场景结构不稳定。
2. MagicWorld通过动作引导的3D几何模块（AG3D）和历史缓存检索（HCR）机制，显式地建模几何约束并利用历史信息。
3. 实验表明，MagicWorld在场景稳定性和连续性方面取得了显著提升，有效缓解了误差累积问题。

## 📝 摘要（中文）

本文提出了一种名为MagicWorld的交互式视频世界模型，旨在解决现有方法在交互式场景演化中存在的两个关键问题：未能充分利用指令驱动的场景运动与底层3D几何之间的对应关系，导致视角变化下的结构不稳定；以及在多步交互中容易遗忘历史信息，导致误差累积和场景语义及结构的逐渐漂移。MagicWorld从单个场景图像出发，利用用户动作驱动动态场景演化，并自回归地合成连续场景。该模型引入了动作引导的3D几何模块（AG3D），从每次交互的第一帧和相应的动作构建点云，为视角转换提供显式的几何约束，从而提高结构一致性。此外，还提出了历史缓存检索（HCR）机制，在生成过程中检索相关的历史帧并将其作为条件信号注入，帮助模型利用过去的场景信息并减轻误差累积。实验结果表明，MagicWorld在交互迭代中显著提高了场景的稳定性和连续性。

## 🔬 方法详解

**问题定义**：现有交互式视频世界模型在生成场景演化时，未能充分利用指令驱动的场景运动与底层3D几何之间的对应关系，导致在视角变化时场景结构不稳定。此外，这些模型在多步交互过程中容易遗忘历史信息，造成误差累积，使得场景语义和结构逐渐漂移。

**核心思路**：MagicWorld的核心思路是通过显式地建模3D几何信息和利用历史信息来解决上述问题。具体来说，利用动作引导的3D几何模块（AG3D）来提供几何约束，提高结构一致性；利用历史缓存检索（HCR）机制来利用过去的场景信息，减轻误差累积。

**技术框架**：MagicWorld的整体框架是一个自回归的生成模型，从单个场景图像开始，利用用户动作驱动动态场景演化，并逐步合成连续的场景。主要包含以下模块：1) 图像编码器：将输入图像编码为特征向量。2) 动作编码器：将用户动作编码为特征向量。3) 动作引导的3D几何模块（AG3D）：从第一帧图像和动作构建点云，提供几何约束。4) 历史缓存检索（HCR）：检索相关的历史帧。5) 解码器：根据图像特征、动作特征、几何约束和历史信息生成下一帧图像。

**关键创新**：MagicWorld的关键创新在于：1) 提出了动作引导的3D几何模块（AG3D），通过构建点云来显式地建模几何信息，为视角转换提供几何约束。2) 提出了历史缓存检索（HCR）机制，通过检索相关的历史帧来利用过去的场景信息，减轻误差累积。

**关键设计**：AG3D模块利用深度估计网络从第一帧图像估计深度信息，并结合相机位姿信息构建点云。HCR模块使用余弦相似度来检索与当前帧最相关的历史帧。损失函数包括图像重建损失、对抗损失和几何一致性损失。

## 📊 实验亮点

MagicWorld在交互式视频世界建模任务上取得了显著的性能提升。实验结果表明，MagicWorld在场景稳定性和连续性方面优于现有方法。具体来说，MagicWorld能够生成更稳定的场景结构，并且能够更好地保持场景的语义一致性，减少误差累积。

## 🎯 应用场景

MagicWorld可应用于虚拟现实、增强现实、游戏开发等领域，例如，可以用于创建交互式的虚拟环境，用户可以通过指令与环境进行交互，并观察环境的动态变化。该技术还可以用于机器人导航和场景理解，帮助机器人更好地理解和适应周围环境。

## 📄 摘要（原文）

> Recent interactive video world model methods generate scene evolution conditioned on user instructions. Although they achieve impressive results, two key limitations remain. First, they fail to fully exploit the correspondence between instruction-driven scene motion and the underlying 3D geometry, which results in structural instability under viewpoint changes. Second, they easily forget historical information during multi-step interaction, resulting in error accumulation and progressive drift in scene semantics and structure. To address these issues, we propose MagicWorld, an interactive video world model that integrates 3D geometric priors and historical retrieval. MagicWorld starts from a single scene image, employs user actions to drive dynamic scene evolution, and autoregressively synthesizes continuous scenes. We introduce the Action-Guided 3D Geometry Module (AG3D), which constructs a point cloud from the first frame of each interaction and the corresponding action, providing explicit geometric constraints for viewpoint transitions and thereby improving structural consistency. We further propose History Cache Retrieval (HCR) mechanism, which retrieves relevant historical frames during generation and injects them as conditioning signals, helping the model utilize past scene information and mitigate error accumulation. Experimental results demonstrate that MagicWorld achieves notable improvements in scene stability and continuity across interaction iterations.

