---
layout: default
title: "D2Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning"
---

# D2Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19443" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19443v1</a>
  <a href="https://arxiv.org/pdf/2512.19443.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19443v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19443v1', 'D2Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Evelyn Zhang, Fufu Yu, Aoqi Wu, Zichen Wen, Ke Yan, Shouhong Ding, Biqing Qi, Linfeng Zhang

**分类**: cs.CV

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**D2Pruner：通过解偏重要性和结构多样性实现MLLM Token剪枝**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `Token剪枝` `解偏` `结构多样性` `最大独立集` `细粒度定位` `计算效率`

## 📋 核心要点

1. 现有MLLM的token剪枝方法在细粒度定位任务中表现不佳，主要原因是重要性偏置和结构盲视。
2. D2Pruner通过结合解偏重要性和结构剪枝机制，选择重要且多样的token子集，从而提升性能。
3. 实验表明，D2Pruner在通用理解和细粒度定位任务中均能显著减少计算量并保持甚至提升性能。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)处理长视觉token序列时面临巨大的计算负担。Token剪枝为加速提供了一条途径，但我们发现当前方法虽然在通用理解方面足够，但在细粒度定位任务上却 катастрофически 失败。我们将这种失败归因于两种主流策略的固有缺陷：基于重要性的方法存在强烈的 positional bias，这是一种固有的模型伪像，会分散对语义内容的注意力；而基于多样性的方法表现出结构盲视，忽略了用户的提示和空间冗余。为了解决这个问题，我们引入了D2Pruner，一个通过独特地结合解偏重要性和结构剪枝机制来纠正这些问题的框架。我们的方法首先基于解偏的注意力分数，将最关键的token集合作为枢轴来保护。然后，对剩余的token执行最大独立集(MIS)选择，这些token在混合图上建模，其中边表示空间邻近性和语义相似性。这个过程迭代地保留最重要和可用的token，同时删除其邻居，确保选择补充token以最大化重要性和多样性。大量的实验表明，D2Pruner具有卓越的效率和保真度。应用于LLaVA-1.5-7B进行通用理解任务时，它减少了74.2%的FLOPs，同时保留了99.2%的原始性能。此外，在具有InternVL-2.5-8B的具有挑战性的定位基准测试中，它在90%的token减少率下保持了85.7%的性能，这是一个显著的进步，比现有方法提高了高达63.53%。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）中视觉token序列过长导致的计算负担问题。现有的token剪枝方法在通用理解任务上表现尚可，但在细粒度定位任务上会严重失效。主要痛点在于：基于重要性的方法受位置偏见影响，而基于多样性的方法忽略了用户提示和空间冗余。

**核心思路**：D2Pruner的核心思路是结合解偏的重要性评估和结构多样性剪枝，从而选择既重要又具有代表性的token子集。通过解偏重要性，消除模型固有的位置偏见，关注语义内容。利用结构多样性剪枝，确保选取的token在空间和语义上具有代表性，避免冗余。

**技术框架**：D2Pruner框架包含两个主要阶段：1) **解偏重要性评估**：计算每个token的解偏注意力分数，选择最重要的token作为枢轴（pivots）。2) **结构多样性剪枝**：对剩余token构建混合图，图中边表示空间邻近性和语义相似性，然后使用最大独立集（MIS）算法，迭代地选择重要且与已选token不相邻的token。

**关键创新**：D2Pruner的关键创新在于同时考虑了token的重要性（解偏后的）和结构多样性。与现有方法相比，D2Pruner能够更好地平衡计算效率和性能，尤其是在细粒度定位任务中，避免了因位置偏见或结构盲视导致的性能下降。

**关键设计**：在解偏重要性评估中，具体如何消除位置偏见，论文中未详细说明，属于未知细节。混合图的构建方式，空间邻近性和语义相似性的具体度量方法，以及MIS算法的具体实现，都属于关键设计细节，但论文中未提供足够信息。这些细节对最终性能有重要影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19443v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19443v1/image/img_motivation.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19443v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

D2Pruner在LLaVA-1.5-7B上进行通用理解任务时，减少了74.2%的FLOPs，同时保留了99.2%的原始性能。在InternVL-2.5-8B上进行细粒度定位任务时，在90%的token减少率下保持了85.7%的性能，比现有方法提高了高达63.53%。这些结果表明D2Pruner在效率和精度方面均优于现有方法。

## 🎯 应用场景

D2Pruner可应用于各种需要处理长视觉token序列的多模态大型语言模型，例如图像/视频理解、视觉问答、目标检测和图像分割等。该方法能够有效降低计算成本，提高模型推理速度，使其更易于部署在资源受限的设备上，并促进MLLM在实际场景中的应用。

## 📄 摘要（原文）

> Processing long visual token sequences poses a significant computational burden on Multimodal Large Language Models (MLLMs). While token pruning offers a path to acceleration, we find that current methods, while adequate for general understanding, catastrophically fail on fine-grained localization tasks. We attribute this failure to the inherent flaws of the two prevailing strategies: importance-based methods suffer from a strong positional bias, an inherent model artifact that distracts from semantic content, while diversity-based methods exhibit structural blindness, disregarding the user's prompt and spatial redundancy. To address this, we introduce D2Pruner, a framework that rectifies these issues by uniquely combining debiased importance with a structural pruning mechanism. Our method first secures a core set of the most critical tokens as pivots based on a debiased attention score. It then performs a Maximal Independent Set (MIS) selection on the remaining tokens, which are modeled on a hybrid graph where edges signify spatial proximity and semantic similarity. This process iteratively preserves the most important and available token while removing its neighbors, ensuring that the supplementary tokens are chosen to maximize importance and diversity. Extensive experiments demonstrate that D2Pruner has exceptional efficiency and fidelity. Applied to LLaVA-1.5-7B for general understanding tasks, it reduces FLOPs by 74.2\% while retaining 99.2\% of its original performance. Furthermore, in challenging localization benchmarks with InternVL-2.5-8B, it maintains 85.7\% performance at a 90\% token reduction rate, marking a significant advancement with up to 63. 53\% improvement over existing methods.

