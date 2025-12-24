---
layout: default
title: "KoopMotion: Learning Almost Divergence Free Koopman Flow Fields for Motion Planning"
---

# KoopMotion: Learning Almost Divergence Free Koopman Flow Fields for Motion Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09074" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09074v2</a>
  <a href="https://arxiv.org/pdf/2509.09074.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09074v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09074v2', 'KoopMotion: Learning Almost Divergence Free Koopman Flow Fields for Motion Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alice Kate Li, Thales C Silva, Victoria Edwards, Vijay Kumar, M. Ani Hsieh

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-09-11 (更新: 2025-11-12)

**备注**: Revised with link to code. Accepted to CoRL 2025 (Conference on Robot Learning). 15 pages 11 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://alicekl.github.io/koop-motion/) | [PROJECT_PAGE](https://alicekl.github.io/koop-motion)

---

## 💡 一句话要点

**KoopMotion：学习近似无散度的Koopman流场用于运动规划，实现轨迹收敛与跟踪。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `运动规划` `Koopman算子` `流场` `轨迹收敛` `从演示学习` `机器人控制` `动力系统` `无散度`

## 📋 核心要点

1. 现有基于Koopman算子的运动规划方法缺乏对轨迹收敛性和目标点的内在约束，限制了其在从演示学习中的应用。
2. KoopMotion将运动流场建模为Koopman算子参数化的动力系统，并利用流场的散度特性，保证轨迹收敛到期望的参考轨迹。
3. 实验表明，KoopMotion在LASA数据集和3D机械臂轨迹数据集上表现出色，且在真实机器人实验中验证了其有效性，仅需少量样本即可生成密集运动规划。

## 📝 摘要（中文）

本文提出了一种基于流场的运动规划新方法，该方法驱动机器人从任意初始状态到达期望的参考轨迹，并收敛到轨迹的终点。尽管Koopman算子理论在动力系统建模中表现出有效性，但它本身并不能保证收敛到期望的轨迹或指定的目标——这是从演示中学习（LfD）的要求。我们提出了KoopMotion，它将运动流场表示为由Koopman算子参数化的动力系统，以模仿期望的轨迹，并利用学习到的流场的散度特性来获得平滑的运动场，当机器人偏离期望轨迹时，该运动场会收敛到期望的参考轨迹，并跟踪该轨迹直到终点。为了证明我们方法的有效性，我们展示了KoopMotion在LASA人类笔迹数据集和3D机械臂末端执行器轨迹数据集上的评估，包括频谱分析。我们还在物理机器人上进行了实验，验证了KoopMotion在非静态流体环境中运行的微型自主水面舰艇上的性能。我们的方法在空间和时间上都具有很高的样本效率，仅需LASA数据集的3%即可生成密集的运动规划。此外，在比较衡量空间和时间动力学建模效果的指标时，KoopMotion比基线方法有了显著的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决运动规划问题，特别是如何使机器人能够从任意初始状态平滑且稳定地收敛到期望的参考轨迹，并最终到达轨迹终点。现有方法，尤其是基于Koopman算子的方法，虽然能建模动力系统，但缺乏内在机制来保证轨迹的收敛性和目标点的可达性，这限制了它们在从演示学习等场景中的应用。

**核心思路**：论文的核心思路是将运动规划问题转化为学习一个近似无散度的Koopman流场。通过将运动流场表示为由Koopman算子参数化的动力系统，并利用流场的散度特性，可以引导机器人向期望轨迹收敛。近似无散度保证了流场的平滑性，避免了突变和不稳定的运动。

**技术框架**：KoopMotion的整体框架包括以下几个主要步骤：1) 从演示数据中学习Koopman算子，该算子能够近似地描述期望的运动轨迹。2) 构建基于Koopman算子的运动流场，该流场将机器人的状态映射到控制输入。3) 通过优化目标函数，使得学习到的流场近似无散度，从而保证运动的平滑性和稳定性。4) 利用学习到的流场进行运动规划，引导机器人从任意初始状态到达并跟踪期望的轨迹。

**关键创新**：该论文的关键创新在于将Koopman算子与流场的散度特性相结合，提出了一种新的运动规划方法。与传统的基于Koopman算子的方法相比，KoopMotion能够显式地控制轨迹的收敛性和目标点的可达性。此外，通过优化流场的散度，可以获得更加平滑和稳定的运动轨迹。

**关键设计**：论文中一个关键的设计是优化目标函数，该目标函数包含两部分：一部分是使得学习到的Koopman算子能够准确地描述期望的运动轨迹，另一部分是使得学习到的流场近似无散度。具体来说，可以通过添加一个正则化项到损失函数中来实现对流场散度的约束。此外，论文还可能涉及到对Koopman算子的基函数进行选择，以及对优化算法进行调整等技术细节。

## 📊 实验亮点

KoopMotion在LASA人类笔迹数据集上仅使用3%的数据即可生成密集的运动规划，显示出极高的样本效率。与基线方法相比，KoopMotion在空间和时间动力学建模方面均有显著提升。在真实机器人实验中，KoopMotion成功控制微型自主水面舰艇在非静态流体环境中运行，验证了其在复杂环境中的适用性。

## 🎯 应用场景

KoopMotion具有广泛的应用前景，例如机器人导航、自主车辆控制、人机协作等领域。它可以用于生成平滑、稳定的运动轨迹，提高机器人的运动效率和安全性。此外，KoopMotion还可以应用于从演示学习，使得机器人能够模仿人类的运动技能，从而实现更加自然和高效的人机交互。该方法在非静态流体环境中的应用也表明其具有一定的鲁棒性。

## 📄 摘要（原文）

> In this work, we propose a novel flow field-based motion planning method that drives a robot from any initial state to a desired reference trajectory such that it converges to the trajectory's end point. Despite demonstrated efficacy in using Koopman operator theory for modeling dynamical systems, Koopman does not inherently enforce convergence to desired trajectories nor to specified goals - a requirement when learning from demonstrations (LfD). We present KoopMotion which represents motion flow fields as dynamical systems, parameterized by Koopman Operators to mimic desired trajectories, and leverages the divergence properties of the learnt flow fields to obtain smooth motion fields that converge to a desired reference trajectory when a robot is placed away from the desired trajectory, and tracks the trajectory until the end point. To demonstrate the effectiveness of our approach, we show evaluations of KoopMotion on the LASA human handwriting dataset and a 3D manipulator end-effector trajectory dataset, including spectral analysis. We also perform experiments on a physical robot, verifying KoopMotion on a miniature autonomous surface vehicle operating in a non-static fluid flow environment. Our approach is highly sample efficient in both space and time, requiring only 3\% of the LASA dataset to generate dense motion plans. Additionally, KoopMotion provides a significant improvement over baselines when comparing metrics that measure spatial and temporal dynamics modeling efficacy. Code at: \href{https://alicekl.github.io/koop-motion/}{\color{blue}{https://alicekl.github.io/koop-motion}}.

