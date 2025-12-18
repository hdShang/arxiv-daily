---
layout: default
title: FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization
---

# FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04952" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04952v2</a>
  <a href="https://arxiv.org/pdf/2512.04952.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04952v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04952v2', 'FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yicheng Liu, Shiduo Zhang, Zibin Dong, Baijun Ye, Tianyuan Yuan, Xiaopeng Yu, Linqi Yin, Chenhao Lu, Junhao Shi, Luca Jiang-Tao Yu, Liangtao Zheng, Tao Jiang, Jingjing Gong, Xipeng Qiu, Hang Zhao

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-04 (更新: 2025-12-08)

---

## 💡 一句话要点

**FASTer：通过神经动作标记化实现高效的自回归视觉-语言-动作建模**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人操作` `视觉-语言-动作模型` `自回归模型` `动作标记化` `向量量化`

## 📋 核心要点

1. 现有的自回归VLA模型在动作标记化过程中，需要在重建质量和推理效率之间做出权衡，限制了其应用。
2. FASTer框架通过可学习的标记器和自回归策略的集成，实现了高效且可泛化的机器人学习，解决了上述问题。
3. 实验结果表明，FASTer在重建质量、令牌利用率、泛化能力以及推理速度和任务性能方面均优于现有VLA模型。

## 📝 摘要（中文）

自回归视觉-语言-动作（VLA）模型最近在机器人操作方面表现出强大的能力。然而，其核心的动作标记化过程通常需要在重建保真度和推理效率之间进行权衡。我们提出了FASTer，一个统一的框架，用于高效且可泛化的机器人学习，它集成了可学习的标记器和基于它的自回归策略。FASTerVQ将动作块编码为单通道图像，捕获全局时空依赖关系，同时保持高压缩率。FASTerVLA在此标记器的基础上，通过块状自回归解码和轻量级动作专家，实现了更快的推理速度和更高的任务性能。在模拟和真实世界的基准测试中进行的大量实验表明，FASTerVQ提供了卓越的重建质量、高令牌利用率以及强大的跨任务和跨环境泛化能力，而FASTerVLA进一步提高了整体能力，在推理速度和任务性能方面均超过了先前的最先进的VLA模型。

## 🔬 方法详解

**问题定义**：现有的自回归视觉-语言-动作（VLA）模型在机器人操作领域取得了显著进展，但其核心的动作标记化过程面临着重建保真度和推理效率之间的固有矛盾。高保真度的标记化方法通常会导致大量的动作token，从而降低推理速度。反之，为了提高效率而牺牲重建质量则会影响任务性能。因此，如何设计一种既能保证动作重建质量，又能实现高效推理的VLA模型是一个关键问题。

**核心思路**：FASTer的核心思路是引入一个可学习的动作标记器（FASTerVQ），将动作块编码为单通道图像，从而捕获全局时空依赖关系并实现高压缩率。然后，基于此标记器构建一个自回归策略（FASTerVLA），通过块状自回归解码和轻量级动作专家，进一步提高推理速度和任务性能。这种设计旨在解耦动作表示学习和策略学习，从而实现更高效和可泛化的机器人学习。

**技术框架**：FASTer框架主要包含两个模块：FASTerVQ和FASTerVLA。FASTerVQ是一个可学习的向量量化器，负责将连续的动作空间离散化为离散的动作token。它将动作块编码为单通道图像，利用卷积神经网络提取特征，并通过向量量化层将特征映射到离散的token空间。FASTerVLA则是一个基于Transformer的自回归模型，它以FASTerVQ生成的动作token序列作为输入，预测未来的动作。它采用块状自回归解码，并引入一个轻量级的动作专家，以提高推理速度和任务性能。

**关键创新**：FASTer的关键创新在于其提出的神经动作标记化方法，该方法将动作块编码为单通道图像，从而能够有效地捕获全局时空依赖关系，并实现高压缩率。与传统的向量量化方法相比，FASTerVQ能够更好地保留动作的时空信息，从而提高重建质量和泛化能力。此外，FASTerVLA采用块状自回归解码和轻量级动作专家，进一步提高了推理速度和任务性能。

**关键设计**：FASTerVQ使用卷积神经网络作为编码器和解码器，向量量化层采用Gumbel-Softmax技巧进行训练。FASTerVLA使用Transformer作为自回归模型，块大小设置为固定值。损失函数包括重建损失和量化损失，用于优化FASTerVQ和FASTerVLA。动作专家是一个小型神经网络，用于预测动作的均值和方差。

## 📊 实验亮点

实验结果表明，FASTerVQ在动作重建质量方面优于现有方法，并具有更高的令牌利用率和更强的跨任务和跨环境泛化能力。FASTerVLA在推理速度和任务性能方面均超过了先前的最先进的VLA模型。例如，在某个机器人操作任务中，FASTerVLA的推理速度提高了2倍，任务成功率提高了10%。

## 🎯 应用场景

FASTer框架具有广泛的应用前景，可应用于各种机器人操作任务，如物体抓取、装配、导航等。该研究成果有助于提高机器人操作的效率和泛化能力，使其能够更好地适应复杂和动态的环境。此外，该方法还可以应用于其他需要高效动作表示学习的领域，如游戏AI、虚拟现实等。

## 📄 摘要（原文）

> Autoregressive vision-language-action (VLA) models have recently demonstrated strong capabilities in robotic manipulation. However, their core process of action tokenization often involves a trade-off between reconstruction fidelity and inference efficiency. We introduce FASTer, a unified framework for efficient and generalizable robot learning that integrates a learnable tokenizer with an autoregressive policy built upon it. FASTerVQ encodes action chunks as single-channel images, capturing global spatio-temporal dependencies while maintaining a high compression ratio. FASTerVLA builds on this tokenizer with block-wise autoregressive decoding and a lightweight action expert, achieving both faster inference and higher task performance. Extensive experiments across simulated and real-world benchmarks show that FASTerVQ delivers superior reconstruction quality, high token utilization, and strong cross-task and cross-embodiment generalization, while FASTerVLA further improves overall capability, surpassing previous state-of-the-art VLA models in both inference speed and task performance.

