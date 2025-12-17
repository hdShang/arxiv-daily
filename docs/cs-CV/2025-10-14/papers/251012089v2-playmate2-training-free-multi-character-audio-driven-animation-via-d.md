---
layout: default
title: Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback
---

# Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.12089" target="_blank" class="toolbar-btn">arXiv: 2510.12089v2</a>
    <a href="https://arxiv.org/pdf/2510.12089.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.12089v2" 
            onclick="toggleFavorite(this, '2510.12089v2', 'Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xingpei Ma, Shenneng Huang, Jiaran Cai, Yuansheng Guan, Shen Zheng, Hanfeng Zhao, Qiang Zhang, Shunsi Zhang

**分类**: cs.CV

**发布日期**: 2025-10-14 (更新: 2025-11-18)

**备注**: AAAI 2026

---

## 💡 一句话要点

**Playmate2：基于扩散Transformer和奖励反馈的免训练多角色音频驱动动画**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频驱动动画` `扩散模型` `Transformer` `多角色动画` `免训练` `唇音同步` `长视频生成`

## 📋 核心要点

1. 现有音频驱动视频生成方法在唇音同步精度、长视频时间连贯性和多角色动画方面存在挑战。
2. 提出基于扩散Transformer的框架，结合LoRA训练、位置偏移推理和奖励反馈，提升视频生成质量。
3. 引入Mask-CFG免训练方法，无需额外数据或模型修改，即可实现多角色音频驱动动画。

## 📝 摘要（中文）

本文提出了一种基于扩散Transformer（DiT）的框架，用于生成任意长度的逼真说话视频，并引入了一种免训练方法用于多角色音频驱动动画。首先，采用基于LoRA的训练策略结合位置偏移推理方法，实现高效的长视频生成，同时保留基础模型的能力。其次，结合部分参数更新和奖励反馈，增强唇音同步和自然的身体运动。最后，提出了一种免训练方法，即掩码分类器自由引导（Mask-CFG），用于多角色动画，无需专门的数据集或模型修改，支持三个或更多角色的音频驱动动画。实验结果表明，该方法优于现有的最先进方法，以简单、高效和经济的方式实现了高质量、时间连贯和多角色的音频驱动视频生成。

## 🔬 方法详解

**问题定义**：现有音频驱动视频生成方法在唇音同步的准确性、长视频生成的时间连贯性以及多角色动画的实现上存在诸多痛点。尤其是在多角色场景下，需要大量特定数据集进行训练，成本高昂且泛化性差。

**核心思路**：论文的核心思路是利用扩散模型强大的生成能力，结合轻量级的LoRA训练和奖励反馈机制，提升唇音同步和动作的自然性。同时，通过Mask-CFG方法，在无需额外训练的情况下实现多角色动画，降低了对特定数据集的依赖。

**技术框架**：整体框架基于扩散Transformer（DiT），主要包含以下几个模块：1) LoRA训练模块，用于在预训练的扩散模型基础上进行微调，提升生成效率；2) 位置偏移推理模块，用于保证长视频生成的时间连贯性；3) 奖励反馈模块，通过奖励函数指导模型生成更逼真的唇音同步和身体动作；4) Mask-CFG模块，通过掩码控制不同角色的运动，实现多角色动画。

**关键创新**：最重要的技术创新点在于Mask-CFG免训练多角色动画方法。该方法无需针对多角色场景进行额外训练，而是通过在推理阶段对不同角色进行掩码，并结合分类器自由引导，实现对多个角色的独立控制。这与需要大量多角色数据进行训练的传统方法有着本质区别。

**关键设计**：LoRA训练中，只更新部分参数，降低计算成本。奖励反馈模块中，奖励函数的设计至关重要，需要综合考虑唇音同步的准确性和身体动作的自然性。Mask-CFG模块中，掩码的设计需要保证不同角色之间的独立性和协调性。位置偏移推理模块通过在时间维度上引入偏移，缓解长视频生成中的时间不一致问题。

## 📊 实验亮点

实验结果表明，Playmate2在唇音同步准确性、时间连贯性和多角色动画质量方面均优于现有方法。特别是在多角色动画方面，该方法无需额外训练即可实现，显著降低了成本。定性结果也显示，生成的视频具有更高的真实感和自然度。

## 🎯 应用场景

该研究成果可广泛应用于虚拟主播、游戏角色动画、电影制作、在线教育等领域。通过音频驱动，可以快速生成逼真且具有表现力的角色动画，降低了动画制作的成本和门槛。未来，该技术有望进一步拓展到更多领域，例如虚拟现实和增强现实等。

## 📄 摘要（原文）

> Recent advances in diffusion models have significantly improved audio-driven human video generation, surpassing traditional methods in both quality and controllability. However, existing approaches still face challenges in lip-sync accuracy, temporal coherence for long video generation, and multi-character animation. In this work, we propose a diffusion transformer (DiT)-based framework for generating lifelike talking videos of arbitrary length, and introduce a training-free method for multi-character audio-driven animation. First, we employ a LoRA-based training strategy combined with a position shift inference approach, which enables efficient long video generation while preserving the capabilities of the foundation model. Moreover, we combine partial parameter updates with reward feedback to enhance both lip synchronization and natural body motion. Finally, we propose a training-free approach, Mask Classifier-Free Guidance (Mask-CFG), for multi-character animation, which requires no specialized datasets or model modifications and supports audio-driven animation for three or more characters. Experimental results demonstrate that our method outperforms existing state-of-the-art approaches, achieving high-quality, temporally coherent, and multi-character audio-driven video generation in a simple, efficient, and cost-effective manner.

