---
layout: default
title: Explaining the Reasoning of Large Language Models Using Attribution Graphs
---

# Explaining the Reasoning of Large Language Models Using Attribution Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15663" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15663v1</a>
  <a href="https://arxiv.org/pdf/2512.15663.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15663v1" onclick="toggleFavorite(this, '2512.15663v1', 'Explaining the Reasoning of Large Language Models Using Attribution Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chase Walker, Rickard Ewetz

**分类**: cs.AI, cs.CL

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出CAGE框架，利用归因图解释大型语言模型推理过程，提升归因忠实度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可解释性` `上下文归因` `归因图` `因果关系`

## 📋 核心要点

1. 现有上下文归因方法忽略了LLM生成过程中的代际影响，导致解释不完整。
2. CAGE框架构建归因图，量化prompt和先前生成对当前生成的影响，保留因果性和行随机性。
3. 实验表明，CAGE在多个模型和数据集上显著提高了上下文归因的忠实度，平均提升高达40%。

## 📝 摘要（中文）

大型语言模型(LLMs)展现了卓越的能力，但其推理过程仍然不透明，引发了安全和信任问题。归因方法已被证明在解释计算机视觉模型的决策方面有效，它将信用分配给输入特征。其中，上下文归因已成为解释自回归LLM行为的一种有前景的方法。然而，当前的上下文归因通过直接将生成的token与prompt关联，忽略了代际间的影响，从而产生不完整的解释。为了克服这些缺点，我们引入了基于图解释的上下文归因(CAGE)框架。CAGE引入了一个归因图：一个有向图，量化了每个生成如何受到prompt和所有先前生成的影响。构建该图是为了保持两个属性——因果性和行随机性。归因图允许通过边缘化图中路径上的中间贡献来计算上下文归因。在多个模型、数据集、指标和方法中，CAGE提高了上下文归因的忠实度，平均增益高达40%。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLMs）推理过程如同黑盒，缺乏透明度，这给安全性和可信度带来了挑战。现有的上下文归因方法试图解释LLM的生成过程，但它们通常直接将生成的token归因于原始prompt，忽略了生成过程中先前token的影响，即代际影响。这种简化导致了不完整的解释，无法准确反映LLM的真实推理过程。

**核心思路**：CAGE框架的核心思路是构建一个归因图，该图能够捕捉LLM生成过程中prompt和所有先前生成token对当前生成token的影响。通过这个图，可以追踪信息在生成过程中的传递和转换，从而更全面、准确地解释LLM的推理过程。该方法旨在解决现有上下文归因方法忽略代际影响的问题，提供更细粒度、更忠实的解释。

**技术框架**：CAGE框架包含以下主要步骤：1) 构建归因图：该图是一个有向图，节点代表prompt中的token和生成的token，边代表token之间的影响关系。边的权重表示影响的强度。2) 保持因果性：图的构建保证了因果关系，即当前token只能受到先前token的影响。3) 保持行随机性：每个节点的输出边的权重之和为1，保证了归因的完整性。4) 计算上下文归因：通过在归因图上进行边缘化操作，可以计算每个生成token对prompt中token的归因，从而解释LLM的生成过程。

**关键创新**：CAGE框架的关键创新在于引入了归因图来显式地建模LLM生成过程中的代际影响。与现有方法直接将生成token归因于prompt不同，CAGE通过归因图捕捉了token之间的传递关系，从而提供了更全面、更细粒度的解释。这种基于图的归因方法能够更准确地反映LLM的真实推理过程。

**关键设计**：归因图的构建是CAGE框架的关键。具体来说，边的权重可以通过多种方法来估计，例如基于注意力机制的权重或者基于梯度的方法。此外，为了保证因果性和行随机性，需要对边的权重进行归一化处理。边缘化操作可以通过标准的图算法来实现，例如最短路径算法或者随机游走算法。具体的参数设置和算法选择会影响最终的归因结果，需要根据具体的应用场景进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15663v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15663v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15663v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CAGE框架在多个模型（包括GPT-2、GPT-Neo等）和数据集上显著提高了上下文归因的忠实度，平均增益高达40%。CAGE在各种指标和方法上均表现出优越性，证明了其有效性和通用性。这些结果表明，CAGE能够提供更准确、更可靠的LLM推理过程解释。

## 🎯 应用场景

CAGE框架可应用于提高LLM的透明度和可信度，例如在医疗诊断、金融风控等高风险领域，解释LLM的决策过程，辅助人工审核和决策。此外，CAGE还可以用于调试和优化LLM，发现模型中的潜在问题，提升模型的性能和鲁棒性。该研究有助于推动LLM在更多领域的应用。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit remarkable capabilities, yet their reasoning remains opaque, raising safety and trust concerns. Attribution methods, which assign credit to input features, have proven effective for explaining the decision making of computer vision models. From these, context attributions have emerged as a promising approach for explaining the behavior of autoregressive LLMs. However, current context attributions produce incomplete explanations by directly relating generated tokens to the prompt, discarding inter-generational influence in the process. To overcome these shortcomings, we introduce the Context Attribution via Graph Explanations (CAGE) framework. CAGE introduces an attribution graph: a directed graph that quantifies how each generation is influenced by both the prompt and all prior generations. The graph is constructed to preserve two properties-causality and row stochasticity. The attribution graph allows context attributions to be computed by marginalizing intermediate contributions along paths in the graph. Across multiple models, datasets, metrics, and methods, CAGE improves context attribution faithfulness, achieving average gains of up to 40%.

