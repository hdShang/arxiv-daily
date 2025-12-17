---
layout: default
title: WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation
---

# WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07313" target="_blank" class="toolbar-btn">arXiv: 2510.07313v1</a>
    <a href="https://arxiv.org/pdf/2510.07313.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07313v1" 
            onclick="toggleFavorite(this, '2510.07313v1', 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zezhong Qian, Xiaowei Chi, Yuming Li, Shizun Wang, Zhiyuan Qin, Xiaozhu Ju, Sirui Han, Shanghang Zhang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**提出WristWorld，利用4D世界模型从Anchor视角生成腕部视角视频，提升机器人操作性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `腕部视角生成` `4D世界模型` `视觉几何模型` `视频生成` `空间一致性` `视觉语言动作`

## 📋 核心要点

1. 现有VLA模型缺乏腕部视角数据，限制了其在机器人操作任务中的性能，而现有世界模型无法仅从Anchor视角生成腕部视角视频。
2. WristWorld通过扩展VGGT并引入空间投影一致性损失，实现了从Anchor视角到腕部视角的几何一致性重建，为后续视频生成奠定基础。
3. 实验表明，WristWorld在视频生成质量和空间一致性方面表现出色，并显著提升了VLA模型在机器人操作任务中的性能。

## 📝 摘要（中文）

腕部视角观测对于视觉语言动作（VLA）模型至关重要，因为它能捕捉到精细的手-物交互，从而直接提升操作性能。然而，大规模数据集很少包含此类记录，导致丰富的Anchor视角和稀缺的腕部视角之间存在巨大差距。现有的世界模型无法弥合这一差距，因为它们需要腕部视角的首帧，因此无法仅从Anchor视角生成腕部视角视频。为此，我们提出了WristWorld，这是第一个仅从Anchor视角生成腕部视角视频的4D世界模型。WristWorld分两个阶段运行：（i）重建，扩展了VGGT并结合了我们的空间投影一致性（SPC）损失，以估计几何上一致的腕部姿势和4D点云；（ii）生成，采用我们的视频生成模型从重建的视角合成时间上连贯的腕部视角视频。在Droid、Calvin和Franka Panda上的实验表明，WristWorld具有最先进的视频生成能力和卓越的空间一致性，同时还提高了VLA性能，在Calvin上平均任务完成长度提高了3.81%，并缩小了42.4%的Anchor-腕部视角差距。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作中，视觉语言动作模型（VLA）缺乏腕部视角数据的问题。现有的世界模型通常需要腕部视角的初始帧才能生成后续视频，无法直接从常见的Anchor视角生成腕部视角视频，这限制了VLA模型在实际场景中的应用。

**核心思路**：论文的核心思路是利用视觉几何模型（如VGGT）的几何和跨视角先验知识，从Anchor视角重建出腕部视角的几何信息（包括姿态和4D点云），然后基于重建的几何信息生成腕部视角的视频。这种方法避免了对腕部视角初始帧的依赖，从而能够仅从Anchor视角生成腕部视角视频。

**技术框架**：WristWorld包含两个主要阶段：重建阶段和生成阶段。在重建阶段，首先利用扩展的VGGT网络估计腕部视角的姿态，并构建4D点云。为了保证几何一致性，引入了空间投影一致性（SPC）损失。在生成阶段，利用视频生成模型，基于重建的腕部视角几何信息，生成时间上连贯的腕部视角视频。

**关键创新**：WristWorld的关键创新在于提出了一个能够仅从Anchor视角生成腕部视角视频的4D世界模型。该模型通过结合视觉几何模型和空间投影一致性损失，实现了几何一致的腕部视角重建，为后续的视频生成提供了可靠的基础。这是首个能够解决该问题的模型。

**关键设计**：空间投影一致性（SPC）损失是关键设计之一，它通过约束Anchor视角和重建的腕部视角之间的几何关系，保证了重建的腕部视角姿态和4D点云的几何一致性。具体来说，SPC损失鼓励Anchor视角中的点投影到重建的腕部视角后，仍然保持其空间位置关系。此外，对VGGT进行了扩展，使其能够更好地适应腕部视角重建任务。

## 📊 实验亮点

实验结果表明，WristWorld在Droid、Calvin和Franka Panda数据集上取得了最先进的视频生成效果，并具有卓越的空间一致性。在Calvin数据集上，WristWorld将VLA模型的平均任务完成长度提高了3.81%，并缩小了42.4%的Anchor-腕部视角差距。这些结果充分证明了WristWorld的有效性和优越性。

## 🎯 应用场景

WristWorld具有广泛的应用前景，例如可以用于增强机器人操作的模拟训练数据，提高机器人在复杂环境中的操作能力。此外，该技术还可以应用于远程操作、虚拟现实等领域，为用户提供更加沉浸式的交互体验。未来，WristWorld有望成为机器人操作领域的重要组成部分。

## 📄 摘要（原文）

> Wrist-view observations are crucial for VLA models as they capture fine-grained hand-object interactions that directly enhance manipulation performance. Yet large-scale datasets rarely include such recordings, resulting in a substantial gap between abundant anchor views and scarce wrist views. Existing world models cannot bridge this gap, as they require a wrist-view first frame and thus fail to generate wrist-view videos from anchor views alone. Amid this gap, recent visual geometry models such as VGGT emerge with geometric and cross-view priors that make it possible to address extreme viewpoint shifts. Inspired by these insights, we propose WristWorld, the first 4D world model that generates wrist-view videos solely from anchor views. WristWorld operates in two stages: (i) Reconstruction, which extends VGGT and incorporates our Spatial Projection Consistency (SPC) Loss to estimate geometrically consistent wrist-view poses and 4D point clouds; (ii) Generation, which employs our video generation model to synthesize temporally coherent wrist-view videos from the reconstructed perspective. Experiments on Droid, Calvin, and Franka Panda demonstrate state-of-the-art video generation with superior spatial consistency, while also improving VLA performance, raising the average task completion length on Calvin by 3.81% and closing 42.4% of the anchor-wrist view gap.

