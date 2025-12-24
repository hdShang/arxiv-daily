---
layout: default
title: "SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting"
---

# SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14742" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14742v1</a>
  <a href="https://arxiv.org/pdf/2506.14742.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14742v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14742v1', 'SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan

**分类**: cs.CV

**发布日期**: 2025-06-17

**🔗 代码/项目**: [PROJECT_PAGE](https://ziqiaopeng.github.io/synctalk)

---

## 💡 一句话要点

**提出SyncTalk++以解决高保真同步人头合成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `说话头合成` `高保真渲染` `同步控制` `面部表情生成` `动态肖像渲染`

## 📋 核心要点

1. 现有方法在合成说话头视频时，常常面临同步性不足的问题，导致生成结果不够真实。
2. SyncTalk++通过动态肖像渲染器和面部同步控制器，确保主体身份一致性和唇部动作与语音的精确对齐。
3. 实验表明，SyncTalk++在同步性和真实感方面显著优于现有技术，渲染速度达到每秒101帧。

## 📝 摘要（中文）

在合成真实感语音驱动的说话头视频时，实现高同步性是一个重大挑战。真实的说话头需要在主体身份、唇部动作、面部表情和头部姿态之间进行同步协调。为了解决这一关键问题，本文提出了SyncTalk++，其核心是动态肖像渲染器和面部同步控制器，确保主体身份的一致性和唇部动作与语音的对齐。此外，论文还引入了头部同步稳定器以优化头部姿态，增强自然性。SyncTalk++在渲染速度和质量上显著提升，达到每秒101帧，实验结果表明其在同步性和真实感方面优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在合成真实感说话头视频时，主体身份、唇部动作、面部表情和头部姿态之间的同步问题。现有方法在这些方面的协调性不足，导致生成结果不够自然和真实。

**核心思路**：SyncTalk++的核心思路是通过引入动态肖像渲染器和面部同步控制器，确保在合成过程中各个元素之间的高效同步。同时，利用3D面部混合形状模型重建准确的面部表情，以提升真实感。

**技术框架**：SyncTalk++的整体架构包括多个模块：动态肖像渲染器、面部同步控制器、头部同步稳定器、表情生成器和躯干恢复器。动态肖像渲染器负责保持主体身份一致性，面部同步控制器则确保唇部动作与语音的对齐。头部同步稳定器优化头部姿态，表情生成器和躯干恢复器则处理面部表情和躯干区域的生成。

**关键创新**：SyncTalk++的主要创新在于其动态肖像渲染器和面部同步控制器的结合使用，这一设计使得生成的说话头在同步性和真实感上有了显著提升。与现有方法相比，SyncTalk++在处理复杂音频时表现出更强的鲁棒性。

**关键设计**：在技术细节上，SyncTalk++采用了特定的损失函数来优化唇部动作与语音的对齐，同时在网络结构上引入了3D面部混合形状模型，以提高面部表情的准确性和自然性。

## 📊 实验亮点

实验结果显示，SyncTalk++在同步性和真实感方面显著优于现有最先进的方法，渲染速度达到每秒101帧，提升幅度明显。用户研究表明，参与者对生成视频的自然性和真实感给予了高度评价，验证了该方法的有效性。

## 🎯 应用场景

SyncTalk++在虚拟现实、游戏开发、在线教育和影视制作等领域具有广泛的应用潜力。其高保真度和高效率的合成能力，可以为用户提供更为真实的交互体验，推动相关行业的发展。未来，该技术有望在个性化虚拟助手和社交媒体内容创作中发挥重要作用。

## 📄 摘要（原文）

> Achieving high synchronization in the synthesis of realistic, speech-driven talking head videos presents a significant challenge. A lifelike talking head requires synchronized coordination of subject identity, lip movements, facial expressions, and head poses. The absence of these synchronizations is a fundamental flaw, leading to unrealistic results. To address the critical issue of synchronization, identified as the ''devil'' in creating realistic talking heads, we introduce SyncTalk++, which features a Dynamic Portrait Renderer with Gaussian Splatting to ensure consistent subject identity preservation and a Face-Sync Controller that aligns lip movements with speech while innovatively using a 3D facial blendshape model to reconstruct accurate facial expressions. To ensure natural head movements, we propose a Head-Sync Stabilizer, which optimizes head poses for greater stability. Additionally, SyncTalk++ enhances robustness to out-of-distribution (OOD) audio by incorporating an Expression Generator and a Torso Restorer, which generate speech-matched facial expressions and seamless torso regions. Our approach maintains consistency and continuity in visual details across frames and significantly improves rendering speed and quality, achieving up to 101 frames per second. Extensive experiments and user studies demonstrate that SyncTalk++ outperforms state-of-the-art methods in synchronization and realism. We recommend watching the supplementary video: https://ziqiaopeng.github.io/synctalk++.

