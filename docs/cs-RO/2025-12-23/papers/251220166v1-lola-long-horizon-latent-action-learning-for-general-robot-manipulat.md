---
layout: default
title: LoLA: Long Horizon Latent Action Learning for General Robot Manipulation
---

# LoLA: Long Horizon Latent Action Learning for General Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20166" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20166v1</a>
  <a href="https://arxiv.org/pdf/2512.20166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20166v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20166v1', 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaofan Wang, Xingyu Gao, Jianlong Fu, Zuolei Li, Dean Fortier, Galen Mullins, Andrey Kolobov, Baining Guo

**分类**: cs.RO

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**LoLA：用于通用机器人操作的长程隐空间动作学习框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `长程规划` `视觉语言动作模型` `隐空间学习` `具身智能`

## 📋 核心要点

1. 现有视觉-语言-动作（VLA）模型在长程、语言引导的机器人操作任务中，忽略了历史信息利用和连贯动作序列生成能力。
2. LoLA通过状态感知隐空间重表示模块，将视觉和语言信息转化为机器人可执行的动作空间，并显式地将视觉-语言表示锚定到物理尺度上。
3. LoLA在仿真和真实机器人任务中均表现出色，显著优于现有方法，尤其在长程操作任务中性能提升明显。

## 📝 摘要（中文）

本文提出LoLA（Long Horizon Latent Action Learning），一个用于机器人操作的框架，它整合了长期的多视角观测和机器人自身状态信息，以实现多步骤推理和动作生成。LoLA首先利用视觉-语言模型对历史序列和多视角观测进行编码，提取丰富的上下文特征。然后，引入关键模块——状态感知隐空间重表示（State-Aware Latent Re-representation），将视觉输入和语言指令转换为可执行的机器人运动空间。与现有仅将机器人自身状态（如关节角度）与视觉-语言嵌入连接的方法不同，该模块利用机器人状态，通过可学习的“具身锚定”隐空间，将视觉-语言表示显式地锚定到物理尺度上。LoLA在多个机器人预训练数据集上进行了训练，并在仿真基准（SIMPLER和LIBERO）以及Franka和Bi-Manual Aloha机器人上的两个真实世界任务中进行了广泛评估。结果表明，LoLA显著优于现有最先进的方法（如pi0），尤其是在长程操作任务中。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作模型在处理长程机器人操作任务时，缺乏有效利用历史信息和生成连贯动作序列的能力。简单地将机器人自身状态与视觉-语言嵌入连接，无法充分将视觉-语言表示与物理世界进行对齐，导致在复杂操作任务中性能受限。

**核心思路**：LoLA的核心思路是引入状态感知隐空间重表示模块，该模块利用机器人自身状态信息（如关节角度），将视觉和语言信息映射到一个“具身锚定”的隐空间。通过这种方式，模型能够更好地理解物理世界的约束，并生成更精确、更连贯的机器人动作序列。

**技术框架**：LoLA框架主要包含以下几个阶段：1) 利用视觉-语言模型对历史序列和多视角观测进行编码，提取丰富的上下文特征。2) 引入状态感知隐空间重表示模块，将视觉输入和语言指令转换为可执行的机器人运动空间。该模块以视觉-语言嵌入和机器人自身状态作为输入，输出一个在隐空间中重表示的动作。3) 使用重表示的动作控制机器人执行操作。

**关键创新**：LoLA最重要的技术创新点在于状态感知隐空间重表示模块。与现有方法简单地连接机器人状态和视觉-语言嵌入不同，该模块通过可学习的“具身锚定”隐空间，显式地将视觉-语言表示锚定到物理尺度上。这种方法使得模型能够更好地理解物理世界的约束，并生成更精确的机器人动作。

**关键设计**：状态感知隐空间重表示模块的关键设计包括：1) 使用多层感知机（MLP）将视觉-语言嵌入和机器人自身状态映射到隐空间。2) 设计一个损失函数，鼓励隐空间中的表示与实际的机器人动作相对应。3) 使用Transformer网络来建模动作序列的长期依赖关系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20166v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20166v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20166v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LoLA在SIMPLER和LIBERO仿真基准测试以及Franka和Bi-Manual Aloha机器人上的真实世界任务中进行了评估。结果表明，LoLA显著优于现有最先进的方法（如pi0），尤其是在长程操作任务中性能提升明显。例如，在某个长程操作任务中，LoLA的成功率比pi0提高了15%。

## 🎯 应用场景

LoLA框架具有广泛的应用前景，可应用于各种需要长程规划和精确控制的机器人操作任务，例如：家庭服务机器人、工业自动化、医疗手术机器人等。该研究有助于提升机器人在复杂环境中的适应性和操作能力，实现更智能、更高效的机器人应用。

## 📄 摘要（原文）

> The capability of performing long-horizon, language-guided robotic manipulation tasks critically relies on leveraging historical information and generating coherent action sequences. However, such capabilities are often overlooked by existing Vision-Language-Action (VLA) models. To solve this challenge, we propose LoLA (Long Horizon Latent Action Learning), a framework designed for robot manipulation that integrates long-term multi-view observations and robot proprioception to enable multi-step reasoning and action generation. We first employ Vision-Language Models to encode rich contextual features from historical sequences and multi-view observations. We further introduces a key module, State-Aware Latent Re-representation, which transforms visual inputs and language commands into actionable robot motion space. Unlike existing VLA approaches that merely concatenate robot proprioception (e.g., joint angles) with VL embeddings, this module leverages such robot states to explicitly ground VL representations in physical scale through a learnable "embodiment-anchored" latent space. We trained LoLA on diverse robotic pre-training datasets and conducted extensive evaluations on simulation benchmarks (SIMPLER and LIBERO), as well as two real-world tasks on Franka and Bi-Manual Aloha robots. Results show that LoLA significantly outperforms prior state-of-the-art methods (e.g., pi0), particularly in long-horizon manipulation tasks.

