---
layout: default
title: Vidarc: Embodied Video Diffusion Model for Closed-loop Control
---

# Vidarc: Embodied Video Diffusion Model for Closed-loop Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17661" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17661v1</a>
  <a href="https://arxiv.org/pdf/2512.17661.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17661v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17661v1', 'Vidarc: Embodied Video Diffusion Model for Closed-loop Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu

**分类**: cs.RO, cs.LG

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**Vidarc：用于闭环控制的具身视频扩散模型，提升机器人操作性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人控制` `视频扩散模型` `具身智能` `闭环控制` `逆动力学` `自回归模型` `深度学习`

## 📋 核心要点

1. 现有基于视频的机器人控制方法在具身闭环控制方面存在高延迟和 grounding 不足的问题。
2. Vidarc 提出了一种自回归具身视频扩散模型，通过动作相关掩码和实时反馈，实现快速准确的闭环控制。
3. Vidarc 在真实机器人部署中，成功率提升至少 15%，延迟降低 91%，并展现出良好的泛化能力。

## 📝 摘要（中文）

由于复杂的具身动力学和多样的环境，数据稀缺场景下的机器人手臂操作极具挑战性。最近基于视频的方法通过在互联网规模的视频数据上进行预训练，在捕获和迁移时间和物理交互方面显示出巨大的潜力。然而，这些方法通常没有针对特定具身闭环控制进行优化，通常存在高延迟和不足的 grounding 问题。本文提出了 Vidarc（Video Diffusion for Action Reasoning and Closed-loop Control），一种新颖的自回归具身视频扩散方法，通过 masked inverse dynamics 模型进行增强。通过使用与动作相关的掩码来 grounding 视频预测，并通过缓存的自回归生成来整合实时反馈，Vidarc 实现了快速、准确的闭环控制。Vidarc 在一百万个跨具身 episodes 上进行预训练，超越了最先进的基线，在真实世界部署中实现了至少 15% 的成功率提升和 91% 的延迟降低。我们还强调了其在以前未见过的机器人平台上的鲁棒泛化和纠错能力。

## 🔬 方法详解

**问题定义**：论文旨在解决数据稀缺场景下，机器人手臂操作中现有基于视频的控制方法存在的延迟高、与环境交互不足的问题。这些方法通常难以适应特定具身机器人的动力学特性，导致控制精度和效率降低。

**核心思路**：Vidarc 的核心思路是利用视频扩散模型学习机器人操作的动态过程，并通过自回归生成的方式预测未来状态。为了提高控制精度和降低延迟，论文引入了动作相关的掩码来指导视频预测，并利用实时反馈进行纠错。

**技术框架**：Vidarc 的整体框架包含以下几个主要模块：1) 视频扩散模型：用于学习机器人操作的视频数据分布；2) Masked Inverse Dynamics 模型：用于预测给定状态和目标状态之间的动作；3) 自回归生成模块：通过缓存历史状态和动作，实现实时的闭环控制。整个流程是，首先利用视频扩散模型预测未来状态，然后利用 Masked Inverse Dynamics 模型计算所需动作，最后将动作发送给机器人执行，并根据实时反馈更新状态。

**关键创新**：Vidarc 的关键创新在于将视频扩散模型与 masked inverse dynamics 模型相结合，并采用自回归生成的方式进行闭环控制。这种方法能够有效地利用视频数据中的信息，提高控制精度和鲁棒性，并降低延迟。与现有方法相比，Vidarc 更加注重具身机器人的动力学特性，并能够更好地适应不同的环境。

**关键设计**：论文中使用了大量的视频数据进行预训练，并采用了特定的损失函数来优化视频扩散模型和 masked inverse dynamics 模型。自回归生成模块采用了缓存机制，以降低延迟。具体的网络结构和参数设置在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17661v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17661v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17661v1/figures/artifacts.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Vidarc 在真实机器人部署中取得了显著的性能提升。与最先进的基线方法相比，Vidarc 的成功率提高了至少 15%，延迟降低了 91%。此外，Vidarc 还展现出良好的泛化能力，能够在以前未见过的机器人平台上进行操作，并具有一定的纠错能力。

## 🎯 应用场景

Vidarc 的潜在应用领域包括工业自动化、家庭服务机器人、医疗机器人等。该研究成果可以提高机器人在复杂环境中的操作能力，降低开发成本，并促进机器人技术的普及。未来，Vidarc 可以进一步扩展到多模态输入、多任务学习等场景，为机器人智能化提供更强大的支持。

## 📄 摘要（原文）

> Robotic arm manipulation in data-scarce settings is a highly challenging task due to the complex embodiment dynamics and diverse contexts. Recent video-based approaches have shown great promise in capturing and transferring the temporal and physical interactions by pre-training on Internet-scale video data. However, such methods are often not optimized for the embodiment-specific closed-loop control, typically suffering from high latency and insufficient grounding. In this paper, we present Vidarc (Video Diffusion for Action Reasoning and Closed-loop Control), a novel autoregressive embodied video diffusion approach augmented by a masked inverse dynamics model. By grounding video predictions with action-relevant masks and incorporating real-time feedback through cached autoregressive generation, Vidarc achieves fast, accurate closed-loop control. Pre-trained on one million cross-embodiment episodes, Vidarc surpasses state-of-the-art baselines, achieving at least a 15% higher success rate in real-world deployment and a 91% reduction in latency. We also highlight its robust generalization and error correction capabilities across previously unseen robotic platforms.

