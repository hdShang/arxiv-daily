---
layout: default
title: "Matrix-game 2.0: An open-source real-time and streaming interactive world model"
---

# Matrix-game 2.0: An open-source real-time and streaming interactive world model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13009" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13009v3</a>
  <a href="https://arxiv.org/pdf/2508.13009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13009v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13009v3', 'Matrix-game 2.0: An open-source real-time and streaming interactive world model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianglong He, Chunli Peng, Zexiang Liu, Boyang Wang, Yifan Zhang, Qi Cui, Fei Kang, Biao Jiang, Mengyin An, Yangyang Ren, Baixin Xu, Hao-Xiang Guo, Kaixiong Gong, Size Wu, Wei Li, Xuchen Song, Yang Liu, Yangguang Li, Yahui Zhou

**分类**: cs.CV

**发布日期**: 2025-08-18 (更新: 2025-12-10)

**备注**: Project Page: https://matrix-game-v2.github.io

---

## 💡 一句话要点

**提出Matrix-Game 2.0以解决实时交互世界建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `交互视频生成` `扩散模型` `实时性能` `自回归生成` `虚拟现实` `数据生产管道` `动作注入` `蒸馏技术`

## 📋 核心要点

1. 现有的交互世界模型依赖于复杂的双向注意力机制和长时间的推理步骤，导致实时性能不足。
2. Matrix-Game 2.0通过少步自回归扩散生成长视频，结合数据生产管道、动作注入模块和蒸馏技术，实现实时交互。
3. 该模型在多种场景下以25 FPS的速度生成高质量视频，显著提升了生成效率和交互体验。

## 📝 摘要（中文）

近年来，交互视频生成的进展表明扩散模型在捕捉复杂物理动态和交互行为方面的潜力。然而，现有的交互世界模型依赖于双向注意力和冗长的推理步骤，严重限制了实时性能。为此，本文提出Matrix-Game 2.0，一个通过少步自回归扩散实时生成长视频的交互世界模型。该框架包括三个关键组件：可扩展的数据生产管道、动作注入模块和基于因果架构的少步蒸馏。Matrix-Game 2.0能够以25 FPS的超快速度生成高质量的分钟级视频，并开源了模型权重和代码库，以推动交互世界建模的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有交互世界模型在实时性能上的不足，尤其是在复杂动态场景中的即时反应能力。现有方法的双向注意力和冗长推理步骤使得实时生成变得困难。

**核心思路**：Matrix-Game 2.0的核心思路是通过少步自回归扩散来生成视频，减少推理时间并提高生成速度，从而实现实时交互。

**技术框架**：该框架包含三个主要模块：首先是一个可扩展的数据生产管道，能够在Unreal Engine和GTA5环境中生成大量视频数据；其次是动作注入模块，允许用户通过鼠标和键盘输入进行交互；最后是基于因果架构的少步蒸馏技术，确保生成过程的高效性。

**关键创新**：最重要的技术创新在于引入了少步自回归扩散生成机制，这一机制显著提升了生成速度和实时交互能力，与传统方法相比，能够更好地模拟真实世界的动态变化。

**关键设计**：在设计中，模型采用了优化的损失函数和网络结构，以确保生成视频的质量和交互的流畅性。具体参数设置和网络架构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，Matrix-Game 2.0能够以25 FPS的速度生成高质量的分钟级视频，相较于现有方法在生成速度上有显著提升，能够满足实时交互的需求。具体性能数据和对比基线在论文中进行了详细分析。

## 🎯 应用场景

Matrix-Game 2.0的研究成果在多个领域具有潜在应用价值，包括游戏开发、虚拟现实、教育培训等。通过实时生成高质量的交互视频，该模型能够为用户提供更加沉浸式的体验，推动相关行业的发展和创新。

## 📄 摘要（原文）

> Recent advances in interactive video generations have demonstrated diffusion model's potential as world models by capturing complex physical dynamics and interactive behaviors. However, existing interactive world models depend on bidirectional attention and lengthy inference steps, severely limiting real-time performance. Consequently, they are hard to simulate real-world dynamics, where outcomes must update instantaneously based on historical context and current actions. To address this, we present Matrix-Game 2.0, an interactive world model generates long videos on-the-fly via few-step auto-regressive diffusion. Our framework consists of three key components: (1) A scalable data production pipeline for Unreal Engine and GTA5 environments to effectively produce massive amounts (about 1200 hours) of video data with diverse interaction annotations; (2) An action injection module that enables frame-level mouse and keyboard inputs as interactive conditions; (3) A few-step distillation based on the casual architecture for real-time and streaming video generation. Matrix Game 2.0 can generate high-quality minute-level videos across diverse scenes at an ultra-fast speed of 25 FPS. We open-source our model weights and codebase to advance research in interactive world modeling.

