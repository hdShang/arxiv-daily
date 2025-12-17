---
layout: default
title: Compressed Causal Reasoning: Quantization and GraphRAG Effects on Interventional and Counterfactual Accuracy
---

# Compressed Causal Reasoning: Quantization and GraphRAG Effects on Interventional and Counterfactual Accuracy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13725" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13725</a>
  <a href="https://arxiv.org/pdf/2512.13725.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13725" onclick="toggleFavorite(this, '2512.13725', 'Compressed Causal Reasoning: Quantization and GraphRAG Effects on Interventional and Counterfactual Accuracy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Steve Nwaiwu, Nipat Jongsawat, Anucha Tungkasthan

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**研究量化和图检索增强生成对大语言模型因果推理能力的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `因果推理` `量化` `大语言模型` `图检索增强生成` `边缘计算`

## 📋 核心要点

1. 现有大语言模型在资源受限环境下进行因果推理时，量化带来的精度损失影响尚不明确。
2. 该研究系统评估了量化（INT8, NF4）对Llama 3 8B在Pearl因果阶梯三个层次推理能力的影响。
3. 实验表明，因果推理对四位量化具有鲁棒性，图检索增强生成可提升干预推理精度。

## 📝 摘要（中文）

在大型语言模型中，涵盖关联、干预和反事实推理的因果推理对于高风险环境下的可靠决策至关重要。随着部署转向边缘和资源受限环境，INT8和NF4等量化模型正成为标准。然而，精度降低对形式化因果推理的影响知之甚少。据我们所知，这是第一个系统地评估量化效应对Pearl因果阶梯所有三个层次影响的研究。使用3000个样本的分层CLadder基准测试，我们发现Llama 3 8B中的rung级别精度在量化下保持大致稳定，NF4的总体降级小于1%。第二层级的干预查询对精度损失最敏感，而第三层级的反事实推理相对稳定，但在诸如碰撞偏差和后门调整等查询类型中表现出异构弱点。在CRASS基准测试上的实验表明，不同精度之间的性能几乎相同，表明现有的常识性反事实数据集缺乏揭示量化引起的推理漂移所需的结构敏感性。我们进一步评估了使用ground truth因果图的图检索增强生成，并观察到NF4干预精度的持续提高，达到1.7%，部分抵消了压缩相关的降级。这些结果表明，因果推理对四位量化具有出乎意料的鲁棒性，图结构增强可以选择性地加强干预推理，并且当前的反事实基准测试未能捕捉到更深层次的因果脆弱性。这项工作提供了压缩因果推理的初步经验图，并为部署高效且结构支持的因果AI系统提供了实用指导。

## 🔬 方法详解

**问题定义**：论文旨在研究在资源受限的边缘计算环境中，对大语言模型进行量化（如INT8和NF4）后，其因果推理能力（包括关联、干预和反事实推理）会受到怎样的影响。现有方法缺乏对量化效应在不同因果推理层次上的系统性评估，并且现有的反事实推理数据集可能无法充分揭示量化引起的推理漂移。

**核心思路**：论文的核心思路是通过构建一个分层的因果推理基准测试（CLadder），并结合现有的常识性反事实数据集（CRASS），系统地评估不同量化级别（包括未量化、INT8和NF4）对大语言模型在不同因果推理任务上的性能影响。同时，探索图检索增强生成（Graph RAG）方法，利用ground truth因果图来增强模型的干预推理能力，以抵消量化带来的性能下降。

**技术框架**：整体框架包括以下几个主要阶段：
1. **基准测试构建**：构建一个包含3000个样本的分层CLadder基准测试，覆盖Pearl因果阶梯的三个层次（关联、干预和反事实推理）。
2. **模型量化**：对Llama 3 8B模型进行不同级别的量化（INT8和NF4）。
3. **性能评估**：在CLadder和CRASS基准测试上评估不同量化级别下模型的因果推理性能。
4. **图检索增强生成**：利用ground truth因果图，通过Graph RAG方法增强模型的干预推理能力。
5. **结果分析**：分析量化效应对不同因果推理任务的影响，以及Graph RAG方法的有效性。

**关键创新**：该研究的主要创新点在于：
1. **系统性评估**：首次系统地评估了量化效应对Pearl因果阶梯所有三个层次的因果推理能力的影响。
2. **Graph RAG增强**：探索了利用ground truth因果图的Graph RAG方法来增强模型的干预推理能力，并部分抵消了量化带来的性能下降。
3. **基准测试分析**：指出当前的反事实推理数据集可能无法充分揭示量化引起的推理漂移。

**关键设计**：
1. **CLadder基准测试**：采用分层结构，覆盖Pearl因果阶梯的三个层次，并包含3000个样本。
2. **Graph RAG**：使用ground truth因果图作为知识源，通过检索相关子图来增强模型的干预推理能力。
3. **量化方法**：采用INT8和NF4两种量化方法，以评估不同量化级别的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13725/figure_1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Llama 3 8B在量化后，因果推理能力总体保持稳定，NF4的总体降级小于1%。干预查询对精度损失最敏感，而反事实推理相对稳定。Graph RAG方法能够提高NF4干预精度1.7%，部分抵消压缩带来的性能下降。CRASS基准测试表明，现有反事实数据集可能无法充分揭示量化引起的推理漂移。

## 🎯 应用场景

该研究成果可应用于对资源敏感的边缘计算设备，例如移动机器人、自动驾驶汽车等，在这些场景下，需要在计算资源有限的情况下进行可靠的因果推理和决策。通过量化模型和图检索增强生成技术，可以在保证推理精度的前提下，降低模型的计算复杂度和存储空间，从而实现高效的因果AI系统部署。

## 📄 摘要（原文）

> Causal reasoning in Large Language Models spanning association, intervention, and counterfactual inference is essential for reliable decision making in high stakes settings. As deployment shifts toward edge and resource constrained environments, quantized models such as INT8 and NF4 are becoming standard. Yet the impact of precision reduction on formal causal reasoning is poorly understood. To our knowledge, this is the first study to systematically evaluate quantization effects across all three levels of Pearls Causal Ladder. Using a 3000 sample stratified CLadder benchmark, we find that rung level accuracy in Llama 3 8B remains broadly stable under quantization, with NF4 showing less than one percent overall degradation. Interventional queries at rung 2 are the most sensitive to precision loss, whereas counterfactual reasoning at rung 3 is comparatively stable but exhibits heterogeneous weaknesses across query types such as collider bias and backdoor adjustment. Experiments on the CRASS benchmark show near identical performance across precisions, indicating that existing commonsense counterfactual datasets lack the structural sensitivity needed to reveal quantization induced reasoning drift. We further evaluate Graph Retrieval Augmented Generation using ground truth causal graphs and observe a consistent improvement in NF4 interventional accuracy of plus 1.7 percent, partially offsetting compression related degradation. These results suggest that causal reasoning is unexpectedly robust to four bit quantization, graph structured augmentation can selectively reinforce interventional reasoning, and current counterfactual benchmarks fail to capture deeper causal brittleness. This work provides an initial empirical map of compressed causal reasoning and practical guidance for deploying efficient and structurally supported causal AI systems.

