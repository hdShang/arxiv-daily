---
layout: default
title: Video Prediction of Dynamic Physical Simulations With Pixel-Space Spatiotemporal Transformers
---

# Video Prediction of Dynamic Physical Simulations With Pixel-Space Spatiotemporal Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20807" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20807v1</a>
  <a href="https://arxiv.org/pdf/2510.20807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20807v1" onclick="toggleFavorite(this, '2510.20807v1', 'Video Prediction of Dynamic Physical Simulations With Pixel-Space Spatiotemporal Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dean L Slack, G Thomas Hudson, Thomas Winterbottom, Noura Al Moubayed

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-23

**备注**: 14 pages, 14 figures

**期刊**: IEEE Transactions on Neural Networks and Learning Systems, 36, 19106-19118, 2025

**DOI**: [10.1109/TNNLS.2025.3585949](https://doi.org/10.1109/TNNLS.2025.3585949)

---

## 💡 一句话要点

**提出基于像素空间时空Transformer的物理模拟视频预测方法**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频预测` `时空Transformer` `物理模拟` `自回归模型` `像素空间` `可解释性` `深度学习`

## 📋 核心要点

1. 现有视频生成方法在物理模拟的时空推理方面存在不足，难以进行长时间的精确预测。
2. 提出一种基于像素空间时空Transformer的自回归视频预测模型，无需复杂的训练策略或潜在特征学习。
3. 实验表明，该方法在物理精确预测的时间范围上，相比现有方法提升了高达50%，同时保持了相当的视频质量。

## 📝 摘要（中文）

本研究受自回归大型语言模型（LLM）的性能和可扩展性启发，探索了一种基于Transformer的视频预测方法，并比较了各种时空自注意力布局。该方法专注于物理模拟的因果建模，旨在解决现有视频生成方法在时空推理方面的不足，通过物理对象跟踪指标和物理模拟数据集上的无监督训练来分离时空推理。我们提出了一种简单而有效的纯Transformer模型，用于自回归视频预测，利用连续像素空间表示进行视频预测。无需复杂的训练策略或潜在特征学习组件，与现有的潜在空间方法相比，我们的方法在保持相当的视频质量指标性能的同时，将物理精确预测的时间范围显著延长了高达50%。此外，我们进行了可解释性实验，以识别网络中编码了可用于准确估计PDE模拟参数的信息的区域，并通过探测模型发现这可以推广到对超出分布的模拟参数的估计。这项工作为基于注意力的视频时空建模提供了一个简单、参数高效且可解释的平台。

## 🔬 方法详解

**问题定义**：现有视频预测方法，尤其是在处理动态物理模拟时，难以进行长时间的精确预测，并且缺乏对时空推理的有效建模。许多方法依赖于复杂的训练策略或潜在特征学习，增加了模型的复杂性和训练难度。

**核心思路**：论文的核心思路是利用Transformer模型强大的时空建模能力，直接在像素空间进行自回归视频预测。通过简化模型结构，避免复杂的潜在特征学习，从而提高模型的训练效率和预测精度。

**技术框架**：该方法采用一个纯Transformer模型，直接以连续像素空间表示作为输入和输出。模型通过自回归的方式，逐帧预测视频序列。整体流程包括：输入历史视频帧，通过Transformer模型进行时空特征提取和预测，生成下一帧的像素表示，并将预测结果作为下一步的输入，循环进行。

**关键创新**：该方法最重要的创新在于直接在像素空间进行时空建模，避免了复杂的潜在空间映射。这种方法简化了模型结构，提高了训练效率，并且能够更好地保留视频中的细节信息。此外，论文还探索了不同的时空自注意力布局，以优化模型的性能。

**关键设计**：模型采用标准的Transformer结构，包括自注意力层和前馈神经网络。关键设计包括：1）使用连续像素空间表示作为输入和输出；2）采用自回归的预测方式；3）探索不同的时空自注意力布局，例如，将空间和时间注意力分开处理，或者采用全局注意力机制。损失函数通常采用像素级别的均方误差（MSE）或类似的度量。

## 📊 实验亮点

实验结果表明，该方法在物理精确预测的时间范围上，相比现有的潜在空间方法提升了高达50%，同时保持了相当的视频质量指标性能。此外，通过可解释性实验，论文还发现网络中存在编码了可用于准确估计PDE模拟参数的信息的区域，并且这种能力可以推广到对超出分布的模拟参数的估计。

## 🎯 应用场景

该研究成果可应用于各种需要精确视频预测的领域，例如：自动驾驶中的环境预测、机器人导航中的场景理解、以及科学计算中的物理模拟可视化。通过提高视频预测的精度和时间范围，可以帮助相关系统做出更准确的决策，并提高其鲁棒性和可靠性。此外，该方法的可解释性也使其在科学研究中具有潜在的应用价值。

## 📄 摘要（原文）

> Inspired by the performance and scalability of autoregressive large language models (LLMs), transformer-based models have seen recent success in the visual domain. This study investigates a transformer adaptation for video prediction with a simple end-to-end approach, comparing various spatiotemporal self-attention layouts. Focusing on causal modeling of physical simulations over time; a common shortcoming of existing video-generative approaches, we attempt to isolate spatiotemporal reasoning via physical object tracking metrics and unsupervised training on physical simulation datasets. We introduce a simple yet effective pure transformer model for autoregressive video prediction, utilizing continuous pixel-space representations for video prediction. Without the need for complex training strategies or latent feature-learning components, our approach significantly extends the time horizon for physically accurate predictions by up to 50% when compared with existing latent-space approaches, while maintaining comparable performance on common video quality metrics. In addition, we conduct interpretability experiments to identify network regions that encode information useful to perform accurate estimations of PDE simulation parameters via probing models, and find that this generalizes to the estimation of out-of-distribution simulation parameters. This work serves as a platform for further attention-based spatiotemporal modeling of videos via a simple, parameter efficient, and interpretable approach.

