---
layout: default
title: "SynBrain: Enhancing Visual-to-fMRI Synthesis via Probabilistic Representation Learning"
---

# SynBrain: Enhancing Visual-to-fMRI Synthesis via Probabilistic Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10298" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10298v3</a>
  <a href="https://arxiv.org/pdf/2508.10298.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10298v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10298v3', 'SynBrain: Enhancing Visual-to-fMRI Synthesis via Probabilistic Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijian Mai, Jiamin Wu, Yu Zhu, Zhouheng Yao, Dongzhan Zhou, Andrew F. Luo, Qihao Zheng, Wanli Ouyang, Chunfeng Song

**分类**: cs.LG, cs.CV, eess.IV

**发布日期**: 2025-08-14 (更新: 2025-11-03)

**备注**: Accepted by NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/MichaelMaiii/SynBrain)

---

## 💡 一句话要点

**提出SynBrain以解决视觉刺激与脑响应映射问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉刺激` `脑响应` `概率学习` `生成模型` `神经科学` `fMRI合成` `生物可解释性`

## 📋 核心要点

1. 现有方法难以同时建模视觉刺激与脑响应之间的生物变异性和功能一致性。
2. SynBrain通过引入BrainVAE和语义到神经映射器，采用概率学习来模拟视觉到神经响应的转化。
3. 实验结果显示，SynBrain在个体特定的视觉到fMRI编码性能上显著优于现有方法，并能有效适应新个体。

## 📝 摘要（中文）

解码视觉刺激如何转化为皮层响应是计算神经科学中的一项基本挑战。视觉到神经的映射本质上是一个一对多的关系，因相同的视觉输入在不同试验、背景和个体中会引发不同的血流动力学反应。现有的确定性方法难以同时建模这种生物变异性，同时捕捉编码刺激信息的功能一致性。为了解决这些局限性，本文提出了SynBrain，一个以概率和生物可解释的方式模拟视觉语义到神经响应转化的生成框架。SynBrain引入了两个关键组件：BrainVAE通过概率学习将神经表征建模为连续概率分布，同时通过视觉语义约束保持功能一致性；语义到神经映射器作为语义传输通道，将视觉语义投影到神经响应流形，以促进高保真fMRI合成。实验结果表明，SynBrain在个体特定的视觉到fMRI编码性能上超越了现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉刺激与脑响应之间的复杂映射关系，现有方法在建模生物变异性和功能一致性方面存在不足。

**核心思路**：SynBrain通过引入概率学习和生物可解释的模型，构建了一个生成框架，能够更好地捕捉视觉语义与神经响应之间的关系。

**技术框架**：SynBrain的整体架构包括两个主要模块：BrainVAE用于建模神经表征的连续概率分布，语义到神经映射器用于将视觉语义投影到神经响应流形。

**关键创新**：最重要的创新在于将神经表征视为概率分布，并通过视觉语义约束保持功能一致性，这与传统的确定性方法形成鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数以平衡生物变异性与功能一致性，同时优化了网络结构以提高合成fMRI信号的质量。

## 📊 实验亮点

实验结果表明，SynBrain在个体特定的视觉到fMRI编码性能上超越了现有最先进的方法，具体提升幅度达到XX%（具体数据未知），并且在数据有限的情况下，能够有效提高fMRI到图像解码的性能。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在脑机接口、神经科学研究和临床诊断等领域。通过更准确地模拟视觉刺激与脑响应之间的关系，SynBrain能够帮助科学家更深入地理解大脑功能，并推动相关技术的发展。

## 📄 摘要（原文）

> Deciphering how visual stimuli are transformed into cortical responses is a fundamental challenge in computational neuroscience. This visual-to-neural mapping is inherently a one-to-many relationship, as identical visual inputs reliably evoke variable hemodynamic responses across trials, contexts, and subjects. However, existing deterministic methods struggle to simultaneously model this biological variability while capturing the underlying functional consistency that encodes stimulus information. To address these limitations, we propose SynBrain, a generative framework that simulates the transformation from visual semantics to neural responses in a probabilistic and biologically interpretable manner. SynBrain introduces two key components: (i) BrainVAE models neural representations as continuous probability distributions via probabilistic learning while maintaining functional consistency through visual semantic constraints; (ii) A Semantic-to-Neural Mapper acts as a semantic transmission pathway, projecting visual semantics into the neural response manifold to facilitate high-fidelity fMRI synthesis. Experimental results demonstrate that SynBrain surpasses state-of-the-art methods in subject-specific visual-to-fMRI encoding performance. Furthermore, SynBrain adapts efficiently to new subjects with few-shot data and synthesizes high-quality fMRI signals that are effective in improving data-limited fMRI-to-image decoding performance. Beyond that, SynBrain reveals functional consistency across trials and subjects, with synthesized signals capturing interpretable patterns shaped by biological neural variability. Our code is available at https://github.com/MichaelMaiii/SynBrain.

