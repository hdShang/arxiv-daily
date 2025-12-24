---
layout: default
title: "Sceniris: A Fast Procedural Scene Generation Framework"
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

**关键词**: `程序化场景生成` `物理AI` `机器人学习` `碰撞检测` `cuRobo` `批量采样` `3D场景`

## 📋 核心要点

1. 现有程序化场景生成方法吞吐量低，严重限制了大规模数据集的创建，阻碍了物理AI和生成模型的发展。
2. Sceniris通过批量采样和更快的碰撞检测，显著提升了场景生成速度，并扩展了对象间的空间关系。
3. 实验表明，Sceniris比Scene Synthesizer至少快234倍，为机器人任务提供了更多可操作的场景。

## 📝 摘要（中文）

合成3D场景对于开发物理人工智能和生成模型至关重要。现有的程序化生成方法通常输出吞吐量较低，这在扩展数据集创建方面造成了显著的瓶颈。本文介绍Sceniris，这是一个高效的程序化场景生成框架，用于快速生成大规模、无碰撞的场景变体。Sceniris还提供可选的机器人可达性检查，为机器人任务提供可操作的场景。Sceniris通过解决先前方法Scene Synthesizer的主要性能限制来实现最大效率。通过利用批量采样和cuRobo中更快的碰撞检测，Sceniris实现了比Scene Synthesizer至少234倍的加速。Sceniris还扩展了先前工作中可用的对象级空间关系，以支持多样化的场景需求。代码已开源。

## 🔬 方法详解

**问题定义**：论文旨在解决现有程序化场景生成方法速度慢的问题。现有方法在生成大规模数据集时面临严重的性能瓶颈，限制了物理AI和生成模型的发展。Scene Synthesizer等方法虽然能够生成场景，但速度较慢，难以满足实际需求。

**核心思路**：Sceniris的核心思路是通过优化采样和碰撞检测过程来提高场景生成速度。具体来说，它采用了批量采样策略，并利用cuRobo库中更快的碰撞检测算法，从而显著减少了生成场景所需的时间。此外，Sceniris还扩展了对象间的空间关系，使其能够生成更多样化的场景。

**技术框架**：Sceniris的整体框架包括以下几个主要模块：1) 场景描述模块：定义场景中对象的类型、数量和空间关系。2) 采样模块：根据场景描述，批量采样对象的位置和姿态。3) 碰撞检测模块：使用cuRobo库快速检测对象之间是否存在碰撞。4) 可达性检查模块（可选）：检查生成的场景是否适合机器人操作。5) 场景输出模块：将生成的场景保存为3D模型文件。

**关键创新**：Sceniris最重要的技术创新点在于其高效的场景生成速度。这主要归功于以下两点：1) 批量采样：通过一次性采样多个对象的位置和姿态，减少了采样过程中的开销。2) cuRobo加速碰撞检测：利用cuRobo库中优化的碰撞检测算法，显著提高了碰撞检测的速度。与现有方法相比，Sceniris在保证场景质量的同时，显著提高了生成速度。

**关键设计**：Sceniris的关键设计包括：1) 批量采样策略：具体采样数量需要根据场景的复杂度和计算资源进行调整。2) cuRobo碰撞检测参数：需要根据对象的形状和大小设置合适的碰撞检测参数，以保证检测的准确性和效率。3) 对象空间关系定义：Sceniris扩展了对象间的空间关系，例如支持对象之间的支撑关系、包含关系等。这些关系的定义需要根据具体的应用场景进行调整。

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

Sceniris通过批量采样和cuRobo加速碰撞检测，实现了显著的性能提升。实验结果表明，Sceniris比Scene Synthesizer至少快234倍。这一显著的加速使得生成大规模数据集成为可能，为物理AI和生成模型的发展提供了有力支持。此外，Sceniris还扩展了对象间的空间关系，使其能够生成更多样化的场景。

## 🎯 应用场景

Sceniris可广泛应用于物理AI、机器人学习、计算机视觉等领域。它可以用于生成大规模的训练数据集，帮助训练更强大的AI模型。例如，可以用于训练机器人操作技能，或者用于训练视觉识别模型。此外，Sceniris还可以用于虚拟环境的创建，例如游戏开发、仿真模拟等。该研究的实际价值在于降低了数据集创建的成本，加速了AI技术的发展。未来，Sceniris可以进一步扩展，支持更多类型的对象和场景，并提供更高级的场景编辑功能。

## 📄 摘要（原文）

> Synthetic 3D scenes are essential for developing Physical AI and generative models. Existing procedural generation methods often have low output throughput, creating a significant bottleneck in scaling up dataset creation. In this work, we introduce Sceniris, a highly efficient procedural scene generation framework for rapidly generating large-scale, collision-free scene variations. Sceniris also provides an optional robot reachability check, providing manipulation-feasible scenes for robot tasks. Sceniris is designed for maximum efficiency by addressing the primary performance limitations of the prior method, Scene Synthesizer. Leveraging batch sampling and faster collision checking in cuRobo, Sceniris achieves at least 234x speed-up over Scene Synthesizer. Sceniris also expands the object-wise spatial relationships available in prior work to support diverse scene requirements. Our code is available at https://github.com/rai-inst/sceniris

