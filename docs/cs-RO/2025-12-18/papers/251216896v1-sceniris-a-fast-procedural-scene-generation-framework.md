---
layout: default
title: Sceniris: A Fast Procedural Scene Generation Framework
---

# Sceniris: A Fast Procedural Scene Generation Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16896" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16896v1</a>
  <a href="https://arxiv.org/pdf/2512.16896.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16896v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16896v1', 'Sceniris: A Fast Procedural Scene Generation Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinghuan Shang, Harsh Patel, Ran Gong, Karl Schmeckpeper

**分类**: cs.RO, cs.CV, cs.GR

**发布日期**: 2025-12-18

**备注**: Code is available at https://github.com/rai-inst/sceniris

**🔗 代码/项目**: [GITHUB](https://github.com/rai-inst/sceniris)

---

## 💡 一句话要点

**Sceniris：一种快速程序化场景生成框架，加速物理AI和生成模型开发。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `程序化场景生成` `物理AI` `机器人操作` `碰撞检测` `批量采样`

## 📋 核心要点

1. 现有程序化场景生成方法吞吐量低，严重制约了大规模数据集的构建，阻碍了物理AI和生成模型的发展。
2. Sceniris通过批量采样和更快的碰撞检测，显著提升了场景生成的效率，并扩展了对象间的空间关系。
3. 实验表明，Sceniris相比于Scene Synthesizer，在场景生成速度上实现了至少234倍的加速，效果显著。

## 📝 摘要（中文）

合成3D场景对于开发物理人工智能和生成模型至关重要。现有的程序化生成方法通常输出吞吐量较低，这在扩展数据集创建方面造成了显著的瓶颈。本文介绍Sceniris，这是一个高效的程序化场景生成框架，用于快速生成大规模、无碰撞的场景变体。Sceniris还提供可选的机器人可达性检查，为机器人任务提供可操作的场景。Sceniris旨在通过解决先前方法Scene Synthesizer的主要性能限制来实现最大效率。通过利用批量采样和cuRobo中更快的碰撞检测，Sceniris实现了至少234倍于Scene Synthesizer的速度提升。Sceniris还扩展了先前工作中可用的对象级空间关系，以支持多样化的场景需求。代码已开源。

## 🔬 方法详解

**问题定义**：论文旨在解决现有程序化场景生成方法速度慢的问题。现有方法在生成大规模数据集时效率低下，无法满足物理AI和生成模型对大量训练数据的需求。Scene Synthesizer等方法在碰撞检测和采样方面存在性能瓶颈，限制了场景生成的吞吐量。

**核心思路**：Sceniris的核心思路是通过优化采样策略和碰撞检测算法来提高场景生成的效率。具体来说，它采用批量采样来减少采样次数，并利用cuRobo中更快的碰撞检测算法来加速碰撞检测过程。此外，Sceniris还扩展了对象间的空间关系，以支持更多样化的场景生成。

**技术框架**：Sceniris的整体框架包括以下几个主要模块：1) 场景描述模块：定义场景中对象的属性和空间关系。2) 采样模块：根据场景描述生成对象的初始位置和姿态。3) 碰撞检测模块：检测对象之间是否存在碰撞。4) 优化模块：调整对象的位置和姿态，以消除碰撞并满足空间关系约束。5) 可达性检测模块（可选）：检查生成的场景是否适合机器人操作。

**关键创新**：Sceniris的关键创新在于其高效的场景生成方法。它通过批量采样和更快的碰撞检测算法，显著提高了场景生成的速度。与Scene Synthesizer相比，Sceniris在性能上有了显著的提升。此外，Sceniris还扩展了对象间的空间关系，使其能够生成更多样化的场景。

**关键设计**：Sceniris的关键设计包括：1) 批量采样策略：一次采样多个对象，减少采样次数。2) cuRobo碰撞检测算法：利用GPU加速碰撞检测，提高检测速度。3) 对象级空间关系扩展：支持更多类型的空间关系，如支撑、包含等。4) 可达性检测模块：使用机器人运动学模型检查场景的可操作性。具体参数设置和损失函数等细节未在论文中详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16896v1/assets/main_steps.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16896v1/assets/spatial_rels_cc.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16896v1/assets/main_benchmark.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Sceniris通过批量采样和cuRobo加速的碰撞检测，实现了显著的性能提升。实验结果表明，Sceniris相比于Scene Synthesizer，在场景生成速度上实现了至少234倍的加速。这一显著的性能提升使得Sceniris能够快速生成大规模的、无碰撞的场景变体，为物理AI和生成模型的发展提供了有力支持。

## 🎯 应用场景

Sceniris可广泛应用于物理AI和生成模型领域，例如机器人操作、自动驾驶、游戏开发等。它可以用于生成大规模的训练数据集，帮助训练更鲁棒、更智能的AI模型。此外，Sceniris还可以用于快速生成各种场景，用于机器人任务规划和仿真，加速机器人技术的研发和应用。未来，Sceniris有望成为物理AI和生成模型领域的重要工具。

## 📄 摘要（原文）

> Synthetic 3D scenes are essential for developing Physical AI and generative models. Existing procedural generation methods often have low output throughput, creating a significant bottleneck in scaling up dataset creation. In this work, we introduce Sceniris, a highly efficient procedural scene generation framework for rapidly generating large-scale, collision-free scene variations. Sceniris also provides an optional robot reachability check, providing manipulation-feasible scenes for robot tasks. Sceniris is designed for maximum efficiency by addressing the primary performance limitations of the prior method, Scene Synthesizer. Leveraging batch sampling and faster collision checking in cuRobo, Sceniris achieves at least 234x speed-up over Scene Synthesizer. Sceniris also expands the object-wise spatial relationships available in prior work to support diverse scene requirements. Our code is available at https://github.com/rai-inst/sceniris

