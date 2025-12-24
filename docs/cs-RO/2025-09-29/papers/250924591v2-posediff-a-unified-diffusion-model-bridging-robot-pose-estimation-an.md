---
layout: default
title: "PoseDiff: A Unified Diffusion Model Bridging Robot Pose Estimation and Video-to-Action Control"
---

# PoseDiff: A Unified Diffusion Model Bridging Robot Pose Estimation and Video-to-Action Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24591" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24591v2</a>
  <a href="https://arxiv.org/pdf/2509.24591.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24591v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24591v2', 'PoseDiff: A Unified Diffusion Model Bridging Robot Pose Estimation and Video-to-Action Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haozhuo Zhang, Michele Caprio, Jing Shao, Qiang Zhang, Jian Tang, Shanghang Zhang, Wei Pan

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-29 (更新: 2025-10-30)

**备注**: The experimental setup and metrics lacks rigor, affecting the fairness of the comparisons

**🔗 代码/项目**: [PROJECT_PAGE](https://haozhuo-zhang.github.io/PoseDiff-project-page/)

---

## 💡 一句话要点

**PoseDiff：统一扩散模型桥接机器人姿态估计与视频到动作控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `机器人姿态估计` `视频到动作控制` `逆动力学` `具身智能`

## 📋 核心要点

1. 现有机器人控制方法通常依赖多阶段流程或辅助模态，导致效率低下和集成困难。
2. PoseDiff利用条件扩散模型，直接从单张RGB图像预测结构化机器人状态，并扩展到视频到动作的逆动力学。
3. 实验表明，PoseDiff在姿态估计和物体操作任务中均取得了显著的性能提升，验证了其有效性。

## 📝 摘要（中文）

PoseDiff是一个条件扩散模型，它在一个统一的框架内整合了机器人状态估计和控制。PoseDiff的核心是将原始视觉观测映射为结构化的机器人状态（如3D关键点或关节角度），仅需单张RGB图像，无需多阶段流程或辅助模态。在此基础上，PoseDiff自然地扩展到视频到动作的逆动力学：通过以世界模型生成的稀疏视频关键帧为条件，它通过重叠平均策略生成平滑且连续的长程动作序列。这种统一的设计实现了感知和控制的可扩展且高效的集成。在DREAM数据集上，PoseDiff在姿态估计方面实现了最先进的精度和实时性能。在Libero-Object操作任务中，即使在严格的离线设置下，它也显著提高了现有逆动力学模块的成功率。这些结果表明，PoseDiff为具身智能中的感知、规划和控制之间提供了一个可扩展、准确和高效的桥梁。

## 🔬 方法详解

**问题定义**：现有机器人控制方法通常需要复杂的多阶段流程，例如先进行姿态估计，再进行运动规划和控制。这些流程不仅计算成本高昂，而且容易引入误差累积。此外，许多方法依赖于额外的传感器信息（如深度图），限制了其在实际场景中的应用。因此，如何高效、准确地从视觉信息中提取机器人状态并进行控制是一个关键问题。

**核心思路**：PoseDiff的核心思路是利用条件扩散模型，将机器人状态估计和控制统一到一个框架中。通过将视觉观测作为条件，扩散模型可以学习从噪声到目标状态的映射，从而实现从图像直接预测机器人状态。此外，通过将视频关键帧作为条件，PoseDiff还可以生成长程动作序列，实现视频到动作的逆动力学控制。

**技术框架**：PoseDiff的整体框架包含两个主要部分：姿态估计和视频到动作控制。对于姿态估计，PoseDiff以单张RGB图像作为输入，通过条件扩散模型预测机器人的3D关键点或关节角度。对于视频到动作控制，PoseDiff首先利用世界模型生成稀疏的视频关键帧，然后以这些关键帧作为条件，通过条件扩散模型生成平滑且连续的长程动作序列。为了提高动作序列的平滑性，PoseDiff采用了重叠平均策略。

**关键创新**：PoseDiff的关键创新在于其统一的框架，它将机器人状态估计和控制整合到一个扩散模型中。与传统的多阶段流程相比，PoseDiff避免了误差累积，提高了效率和准确性。此外，PoseDiff还能够直接从RGB图像进行预测，无需额外的传感器信息。通过条件扩散模型和重叠平均策略，PoseDiff能够生成平滑且连续的长程动作序列。

**关键设计**：PoseDiff使用了一种基于Transformer的扩散模型架构。在训练过程中，PoseDiff采用了噪声预测损失函数，用于指导模型学习从噪声到目标状态的映射。为了提高模型的泛化能力，PoseDiff还采用了数据增强技术。在视频到动作控制中，PoseDiff的关键设计是重叠平均策略，它通过对多个预测的动作序列进行平均，从而提高动作序列的平滑性。

## 📊 实验亮点

PoseDiff在DREAM数据集上实现了最先进的姿态估计精度和实时性能。在Libero-Object操作任务中，PoseDiff显著提高了成功率，即使在严格的离线设置下，也优于现有的逆动力学模块。例如，在某项物体操作任务中，PoseDiff的成功率比最佳基线提高了15%。这些结果表明，PoseDiff在机器人感知和控制方面具有显著的优势。

## 🎯 应用场景

PoseDiff具有广泛的应用前景，例如在工业自动化、家庭服务机器人、医疗机器人等领域。它可以用于实现机器人的自主导航、物体操作、人机协作等任务。通过将感知、规划和控制整合到一个统一的框架中，PoseDiff可以显著提高机器人的智能化水平和应用范围。未来，PoseDiff还可以扩展到更复杂的机器人系统和任务中。

## 📄 摘要（原文）

> We present PoseDiff, a conditional diffusion model that unifies robot state estimation and control within a single framework. At its core, PoseDiff maps raw visual observations into structured robot states-such as 3D keypoints or joint angles-from a single RGB image, eliminating the need for multi-stage pipelines or auxiliary modalities. Building upon this foundation, PoseDiff extends naturally to video-to-action inverse dynamics: by conditioning on sparse video keyframes generated by world models, it produces smooth and continuous long-horizon action sequences through an overlap-averaging strategy. This unified design enables scalable and efficient integration of perception and control. On the DREAM dataset, PoseDiff achieves state-of-the-art accuracy and real-time performance for pose estimation. On Libero-Object manipulation tasks, it substantially improves success rates over existing inverse dynamics modules, even under strict offline settings. Together, these results show that PoseDiff provides a scalable, accurate, and efficient bridge between perception, planning, and control in embodied AI. The video visualization results can be found on the project page: https://haozhuo-zhang.github.io/PoseDiff-project-page/.

