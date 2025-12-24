---
layout: default
title: "Inv-Entropy: A Fully Probabilistic Framework for Uncertainty Quantification in Language Models"
---

# Inv-Entropy: A Fully Probabilistic Framework for Uncertainty Quantification in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09684" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09684v2</a>
  <a href="https://arxiv.org/pdf/2506.09684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09684v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09684v2', 'Inv-Entropy: A Fully Probabilistic Framework for Uncertainty Quantification in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyi Song, Ruihan Ji, Naichen Shi, Fan Lai, Raed Al Kontar

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-11-05)

**期刊**: NeurIPS, 2025

**🔗 代码/项目**: [GITHUB](https://github.com/UMDataScienceLab/Uncertainty-Quantification-for-LLMs)

---

## 💡 一句话要点

**提出Inv-Entropy框架以量化语言模型的不确定性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `不确定性量化` `大型语言模型` `概率框架` `逆模型` `遗传算法` `语义相似性` `扰动策略`

## 📋 核心要点

1. 现有的不确定性量化方法多为启发式，缺乏系统的概率解释，限制了大型语言模型的可靠应用。
2. 本文提出了一种基于逆模型的完全概率框架，通过扰动输入空间来量化不确定性，定义了新的不确定性度量Inv-Entropy。
3. 实验结果显示，Inv-Entropy在不确定性量化方面优于现有的语义UQ方法，验证了其有效性和灵活性。

## 📝 摘要（中文）

大型语言模型（LLMs）已在自然语言处理领域引发变革，但其可靠部署需要有效的不确定性量化（UQ）。现有UQ方法往往是启发式的，缺乏概率解释。本文首先提供了扰动在LLMs不确定性量化中的理论依据，随后引入双随机游走视角，将输入-输出对建模为两个马尔可夫链，并通过语义相似性定义转移概率。基于此，我们提出了一种基于逆模型的完全概率框架，通过系统性扰动评估给定输出条件下输入空间的多样性来量化不确定性。我们定义了一种新的不确定性度量Inv-Entropy，并提出了一种基于遗传算法的扰动算法GAAP，以增强采样输入的多样性。实验表明，Inv-Entropy在性能上优于现有的语义UQ方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型的不确定性量化问题，现有方法往往缺乏系统性和概率解释，导致不可靠的结果。

**核心思路**：提出了一种基于逆模型的完全概率框架，通过系统性扰动输入空间来量化不确定性，利用双随机游走视角建模输入-输出对。

**技术框架**：整体框架包括两个主要模块：首先是基于语义相似性的马尔可夫链建模输入-输出对，其次是通过定义的Inv-Entropy度量不确定性，并结合遗传算法GAAP增强输入多样性。

**关键创新**：最重要的创新在于提出了Inv-Entropy作为新的不确定性度量，并通过双随机游走视角提供了新的建模思路，显著区别于现有的启发式方法。

**关键设计**：在设计中，采用了多种不确定性度量、嵌入方式和扰动策略，GAAP算法通过遗传算法优化输入扰动，提升了采样的多样性。损失函数和网络结构的具体细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，Inv-Entropy在不确定性量化方面的表现优于现有的语义UQ方法，具体性能提升幅度达到了XX%（具体数据待补充），验证了其有效性和灵活性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本生成、对话系统和信息检索等。通过有效的不确定性量化，能够提升模型在实际应用中的可靠性和安全性，未来可能推动更广泛的智能系统部署。

## 📄 摘要（原文）

> Large language models (LLMs) have transformed natural language processing, but their reliable deployment requires effective uncertainty quantification (UQ). Existing UQ methods are often heuristic and lack a probabilistic interpretation. This paper begins by providing a theoretical justification for the role of perturbations in UQ for LLMs. We then introduce a dual random walk perspective, modeling input-output pairs as two Markov chains with transition probabilities defined by semantic similarity. Building on this, we propose a fully probabilistic framework based on an inverse model, which quantifies uncertainty by evaluating the diversity of the input space conditioned on a given output through systematic perturbations. Within this framework, we define a new uncertainty measure, Inv-Entropy. A key strength of our framework is its flexibility: it supports various definitions of uncertainty measures, embeddings, perturbation strategies, and similarity metrics. We also propose GAAP, a perturbation algorithm based on genetic algorithms, which enhances the diversity of sampled inputs. In addition, we introduce a new evaluation metric, Temperature Sensitivity of Uncertainty (TSU), which directly assesses uncertainty without relying on correctness as a proxy. Extensive experiments demonstrate that Inv-Entropy outperforms existing semantic UQ methods. The code to reproduce the results can be found at https://github.com/UMDataScienceLab/Uncertainty-Quantification-for-LLMs.

