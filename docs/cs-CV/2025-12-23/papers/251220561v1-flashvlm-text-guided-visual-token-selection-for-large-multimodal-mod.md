---
layout: default
title: FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models
---

# FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20561" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20561v1</a>
  <a href="https://arxiv.org/pdf/2512.20561.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20561v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20561v1', 'FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaitong Cai, Jusheng Zhang, Jing Yang, Yijia Fan, Pengtao Xie, Jian Wang, Keze Wang

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: Under submission

---

## 💡 一句话要点

**FlashVLM：文本引导的视觉Token选择，提升大模型多模态效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `Token选择` `跨模态相似性` `视觉显著性` `模型压缩` `效率优化` `文本引导`

## 📋 核心要点

1. 现有VLMs处理大量视觉tokens导致计算冗余，且token缩减方法易忽略文本信息或依赖不稳定的注意力图。
2. FlashVLM通过计算图像tokens与文本嵌入的跨模态相似性，并结合视觉显著性，实现文本引导的动态token选择。
3. 实验表明，FlashVLM在大幅压缩视觉tokens的同时，性能超越未剪枝基线，并在多个基准测试中表现出强大的鲁棒性。

## 📝 摘要（中文）

大型视觉语言模型(VLMs)通常处理每个图像或视频帧的数百甚至数千个视觉token，导致二次方级别的注意力计算成本和显著的冗余。现有的token缩减方法通常忽略文本查询或依赖于深度注意力图，而深度注意力图在激进剪枝下不稳定，导致语义对齐性能下降。我们提出了FlashVLM，一个文本引导的视觉token选择框架，可以动态地调整视觉输入以适应查询。FlashVLM不依赖于噪声大的注意力权重，而是计算投影图像token和语言模型空间中归一化文本嵌入之间的显式跨模态相似性。这种外在相关性与内在视觉显著性融合，使用对数域加权和温度控制锐化。此外，多样性保持分区保留了一个最小但具有代表性的背景token集合，以维持全局上下文。在相同的token预算和评估协议下，FlashVLM实现了超越无损的压缩，在LLaVA 1.5上剪枝高达77.8%的视觉token的同时，略微超过了未剪枝的基线，并且在压缩94.4%的情况下，仍保持92.8%的准确率。在14个图像和视频基准上的大量实验表明，FlashVLM在保持主流VLMs的强大鲁棒性和泛化能力的同时，提供了最先进的效率-性能权衡。

## 🔬 方法详解

**问题定义**：现有的大型视觉语言模型（VLMs）在处理图像和视频时，需要处理大量的视觉tokens，这导致了巨大的计算开销，特别是注意力机制的二次方复杂度。现有的token缩减方法要么忽略了文本查询的信息，要么依赖于深度学习模型中的注意力图。然而，这些注意力图在进行激进的token剪枝时往往不稳定，导致视觉和文本之间的语义对齐效果下降，最终影响模型的性能。

**核心思路**：FlashVLM的核心思路是利用文本信息来引导视觉token的选择，从而动态地调整视觉输入以适应特定的文本查询。它不依赖于不稳定的注意力权重，而是通过计算图像tokens和文本嵌入之间的跨模态相似性来确定哪些视觉tokens与文本查询最相关。同时，为了保持全局上下文，FlashVLM还保留了一部分具有代表性的背景tokens。

**技术框架**：FlashVLM的整体框架包括以下几个主要步骤：1) 将图像分割成tokens，并使用视觉编码器提取每个token的特征；2) 使用语言模型对文本查询进行编码，得到文本嵌入；3) 计算图像tokens的特征和文本嵌入之间的跨模态相似性，得到每个视觉token与文本查询的相关性得分；4) 结合视觉显著性信息，对相关性得分进行加权和锐化；5) 使用多样性保持分区算法选择一部分与文本最相关的视觉tokens，并保留一部分具有代表性的背景tokens；6) 将选择的视觉tokens和文本嵌入输入到视觉语言模型中进行后续处理。

**关键创新**：FlashVLM的关键创新在于它使用显式的跨模态相似性来指导视觉token的选择，而不是依赖于不稳定的注意力权重。这种方法能够更准确地选择与文本查询相关的视觉tokens，从而提高模型的性能。此外，FlashVLM还引入了多样性保持分区算法，以确保选择的tokens能够覆盖图像的全局上下文。

**关键设计**：FlashVLM的关键设计包括：1) 使用对数域加权和温度控制锐化来融合跨模态相似性和视觉显著性；2) 使用余弦相似度来计算图像tokens和文本嵌入之间的相似性；3) 使用k-means聚类算法来实现多样性保持分区，选择具有代表性的背景tokens。温度参数控制锐化程度，影响选择token的集中度。多样性保持分区确保全局信息不丢失。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20561v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20561v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20561v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FlashVLM在LLaVA 1.5上实现了显著的性能提升。在剪枝高达77.8%的视觉tokens的情况下，FlashVLM的性能略微超过了未剪枝的基线。更令人印象深刻的是，即使在压缩94.4%的视觉tokens的情况下，FlashVLM仍然保持了92.8%的准确率。在14个图像和视频基准上的实验表明，FlashVLM在效率和性能之间取得了最佳的平衡。

## 🎯 应用场景

FlashVLM具有广泛的应用前景，例如在图像/视频检索、视觉问答、图像描述生成等领域。通过减少视觉tokens的数量，FlashVLM可以显著降低计算成本，提高模型的效率，使其更适用于资源受限的设备或需要实时响应的应用场景。此外，FlashVLM还可以用于提高模型的鲁棒性和泛化能力，使其能够更好地适应不同的图像和视频数据。

## 📄 摘要（原文）

> Large vision-language models (VLMs) typically process hundreds or thousands of visual tokens per image or video frame, incurring quadratic attention cost and substantial redundancy. Existing token reduction methods often ignore the textual query or rely on deep attention maps, whose instability under aggressive pruning leads to degraded semantic alignment.
>   We propose FlashVLM, a text guided visual token selection framework that dynamically adapts visual inputs to the query. Instead of relying on noisy attention weights, FlashVLM computes an explicit cross modal similarity between projected image tokens and normalized text embeddings in the language model space. This extrinsic relevance is fused with intrinsic visual saliency using log domain weighting and temperature controlled sharpening. In addition, a diversity preserving partition retains a minimal yet representative set of background tokens to maintain global context.
>   Under identical token budgets and evaluation protocols, FlashVLM achieves beyond lossless compression, slightly surpassing the unpruned baseline while pruning up to 77.8 percent of visual tokens on LLaVA 1.5, and maintaining 92.8 percent accuracy even under 94.4 percent compression. Extensive experiments on 14 image and video benchmarks demonstrate that FlashVLM delivers state of the art efficiency performance trade offs while maintaining strong robustness and generalization across mainstream VLMs.

