---
layout: default
title: FreeMusco: Motion-Free Learning of Latent Control for Morphology-Adaptive Locomotion in Musculoskeletal Characters
---

# FreeMusco: Motion-Free Learning of Latent Control for Morphology-Adaptive Locomotion in Musculoskeletal Characters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14205" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14205v1</a>
  <a href="https://arxiv.org/pdf/2511.14205.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14205v1" onclick="toggleFavorite(this, '2511.14205v1', 'FreeMusco: Motion-Free Learning of Latent Control for Morphology-Adaptive Locomotion in Musculoskeletal Characters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minkwan Kim, Yoonsang Lee

**分类**: cs.GR

**发布日期**: 2025-11-18

**备注**: SIGGRAPH Asia 2025

---

## 💡 一句话要点

**FreeMusco：用于肌肉骨骼角色形态自适应运动的无运动数据潜在控制学习**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `肌肉骨骼模型` `运动控制` `强化学习` `无运动数据` `形态自适应` `潜在空间` `生物力学` `步态生成`

## 📋 核心要点

1. 现有方法依赖大量运动捕捉数据，限制了在数据难以获取的肌肉骨骼角色上的应用。
2. FreeMusco利用肌肉骨骼模型作为先验，通过强化学习联合学习潜在表示和控制策略，实现无运动数据的运动控制。
3. 实验表明，该方法能够生成多样且节能的运动步态，并支持目标导航和路径跟随等下游任务。

## 📝 摘要（中文）

我们提出了FreeMusco，一个无运动数据的框架，用于联合学习肌肉骨骼角色的潜在表示和控制策略。通过利用肌肉骨骼模型作为强先验，我们的方法能够使能量感知和形态自适应的运动涌现，而无需运动数据。该框架可以推广到人类、非人类和合成形态，其中自然地出现不同的节能策略——例如，类人猿的四足步态与人类的两足步态。潜在空间和相应的控制策略是从头开始构建的，无需演示，并支持下游任务，如目标导航和路径跟随——据我们所知，这是第一个提供这种能力的无运动数据方法。FreeMusco通过基于模型的强化学习学习多样且物理上合理的运动行为，该强化学习由结合了控制、平衡和生物力学项的运动目标引导。为了更好地捕捉自然步态的周期性结构，我们引入了时间平均损失公式，该公式在时间窗口内比较模拟状态和目标状态，而不是逐帧比较。我们通过在训练期间随机化目标姿势和能量水平来进一步鼓励行为多样性，从而使运动能够在运行时以形式和强度进行灵活调节。总之，这些结果表明，无需运动捕捉即可实现通用且自适应的运动控制，从而为模拟数据收集不切实际或不可能的角色运动提供了一个新方向。

## 🔬 方法详解

**问题定义**：现有肌肉骨骼角色运动控制方法通常依赖于大量的运动捕捉数据，这限制了它们在数据难以获取或不存在的场景中的应用，例如合成生物或奇特生物的运动模拟。此外，如何使角色能够根据自身形态自适应地学习运动策略也是一个挑战。

**核心思路**：FreeMusco的核心思路是利用肌肉骨骼模型作为强先验，通过强化学习直接从物理引擎中学习运动控制策略，而无需任何运动捕捉数据。通过精心设计的奖励函数和训练策略，使角色能够自发地学习能量高效且形态自适应的运动方式。

**技术框架**：FreeMusco框架包含以下主要模块：1) 肌肉骨骼模型：作为环境，提供角色状态和物理交互。2) 潜在空间：用于表示角色的运动状态和目标。3) 控制策略：一个神经网络，根据潜在空间中的状态输出控制信号。4) 强化学习算法：用于训练控制策略，使其能够实现运动目标。训练过程包括随机初始化潜在空间和控制策略，然后通过与环境交互，根据奖励函数不断优化策略。

**关键创新**：该方法最重要的创新在于实现了无运动数据的肌肉骨骼角色运动控制。通过将肌肉骨骼模型作为强先验，并结合强化学习，该方法能够生成多样且自然的运动步态，而无需任何人工干预或运动捕捉数据。此外，时间平均损失函数和随机化训练策略进一步提高了运动的稳定性和多样性。

**关键设计**：FreeMusco的关键设计包括：1) 奖励函数：结合了控制成本、平衡性和生物力学项，鼓励角色学习能量高效且稳定的运动方式。2) 时间平均损失函数：通过在时间窗口内比较模拟状态和目标状态，提高了运动的周期性和稳定性。3) 随机化训练策略：通过随机化目标姿势和能量水平，鼓励角色学习多样化的运动策略。4) 潜在空间的设计：潜在空间用于表示角色的运动状态和目标，其维度和结构对最终的运动效果有重要影响。

## 📊 实验亮点

FreeMusco在多种肌肉骨骼角色上进行了实验，包括人类、非人类和合成形态。实验结果表明，该方法能够生成多样且节能的运动步态，例如类人猿的四足步态和人类的两足步态。此外，该方法还支持目标导航和路径跟随等下游任务，展示了其强大的泛化能力。

## 🎯 应用场景

FreeMusco具有广泛的应用前景，包括游戏、电影、虚拟现实等领域。它可以用于创建逼真且自然的肌肉骨骼角色动画，而无需昂贵的运动捕捉设备和人工干预。此外，该方法还可以用于研究生物运动的机理，以及设计新型的机器人运动控制系统。

## 📄 摘要（原文）

> We propose FreeMusco, a motion-free framework that jointly learns latent representations and control policies for musculoskeletal characters. By leveraging the musculoskeletal model as a strong prior, our method enables energy-aware and morphology-adaptive locomotion to emerge without motion data. The framework generalizes across human, non-human, and synthetic morphologies, where distinct energy-efficient strategies naturally appear--for example, quadrupedal gaits in Chimanoid versus bipedal gaits in Humanoid. The latent space and corresponding control policy are constructed from scratch, without demonstration, and enable downstream tasks such as goal navigation and path following--representing, to our knowledge, the first motion-free method to provide such capabilities. FreeMusco learns diverse and physically plausible locomotion behaviors through model-based reinforcement learning, guided by the locomotion objective that combines control, balancing, and biomechanical terms. To better capture the periodic structure of natural gait, we introduce the temporally averaged loss formulation, which compares simulated and target states over a time window rather than on a per-frame basis. We further encourage behavioral diversity by randomizing target poses and energy levels during training, enabling locomotion to be flexibly modulated in both form and intensity at runtime. Together, these results demonstrate that versatile and adaptive locomotion control can emerge without motion capture, offering a new direction for simulating movement in characters where data collection is impractical or impossible.

