---
layout: default
title: "microCLIP: Unsupervised CLIP Adaptation via Coarse-Fine Token Fusion for Fine-Grained Image Classification"
---

# microCLIP: Unsupervised CLIP Adaptation via Coarse-Fine Token Fusion for Fine-Grained Image Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02270" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02270v1</a>
  <a href="https://arxiv.org/pdf/2510.02270.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02270v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02270v1', 'microCLIP: Unsupervised CLIP Adaptation via Coarse-Fine Token Fusion for Fine-Grained Image Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sathira Silva, Eman Ali, Chetan Arora, Muhammad Haris Khan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-02

**🔗 代码/项目**: [GITHUB](https://github.com/sathiiii/microCLIP)

---

## 💡 一句话要点

**microCLIP：通过粗细粒度Token融合实现无监督CLIP微调，提升细粒度图像分类性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细粒度图像分类` `CLIP` `无监督微调` `Token融合` `自训练`

## 📋 核心要点

1. CLIP在细粒度图像分类中依赖粗糙的全局特征，限制了其性能，现有方法忽略了空间精度。
2. microCLIP通过显著性导向的TokenFusion模块，融合全局和局部特征，并利用自训练框架优化CLIP的视觉和文本表示。
3. 实验结果表明，microCLIP在13个细粒度基准测试中平均精度提升2.90%，证明了其有效性。

## 📝 摘要（中文）

本文提出microCLIP，一个自训练框架，用于利用细粒度线索联合优化CLIP的视觉和文本表示，以实现基于CLIP的视觉-语言模型(VLM)的无监督微调，用于细粒度图像分类。该方法的核心是轻量级的TokenFusion模块中的显著性导向注意力池化(SOAP)，它从patch嵌入构建一个显著性引导的[FG]token，并将其与全局[CLS]token融合，以实现粗细粒度的对齐。为了稳定微调，引入了一个双头LLM派生的分类器：一个冻结的分类器，通过多视角对齐，为伪标签提供稳定的基于文本的先验；以及一个可学习的分类器，从LLM描述初始化，并使用TokenFusion进行微调。此外，还开发了动态知识聚合，它凸组合固定的LLM/CLIP先验与TokenFusion不断演变的logits，以迭代地优化伪标签。这些组件共同揭示了CLIP中潜在的细粒度信号，在13个细粒度基准测试中实现了平均2.90%的精度提升，同时只需要轻量级的微调。

## 🔬 方法详解

**问题定义**：细粒度图像分类任务需要模型对图像中微小的局部线索具有高度的敏感性。CLIP虽然具有强大的零样本迁移能力，但其依赖于粗糙的全局特征，导致其在细粒度分类任务上的表现受限。现有方法尝试将大型语言模型(LLM)的描述与CLIP的[CLS]token对齐，以注入细粒度知识，但忽略了空间精度，无法充分利用图像的局部信息。

**核心思路**：microCLIP的核心思路是通过融合CLIP的全局特征和从图像局部区域提取的细粒度特征，来提升模型对细粒度信息的感知能力。该方法利用显著性导向的注意力机制，从图像patch嵌入中提取重要的局部特征，并将其与全局特征融合，从而实现粗细粒度的对齐。此外，通过自训练的方式，不断优化CLIP的视觉和文本表示，进一步提升模型的性能。

**技术框架**：microCLIP的整体框架包括以下几个主要模块：1) TokenFusion模块：该模块利用显著性导向注意力池化(SOAP)从图像patch嵌入中提取显著性区域的特征，并生成一个[FG]token，然后将[FG]token与CLIP的[CLS]token融合，得到融合后的特征表示。2) 双头LLM派生分类器：该分类器包含一个冻结的分类器和一个可学习的分类器。冻结的分类器利用多视角对齐提供稳定的文本先验，用于伪标签生成；可学习的分类器从LLM描述初始化，并使用TokenFusion的输出进行微调。3) 动态知识聚合：该模块将固定的LLM/CLIP先验与TokenFusion的输出进行凸组合，以迭代地优化伪标签。

**关键创新**：microCLIP的关键创新在于以下几个方面：1) 提出了Saliency-Oriented Attention Pooling (SOAP)机制，能够有效地从图像patch嵌入中提取显著性区域的特征。2) 设计了TokenFusion模块，将全局特征和局部特征进行融合，从而提升模型对细粒度信息的感知能力。3) 引入了双头LLM派生分类器和动态知识聚合机制，能够稳定自训练过程，并提升伪标签的质量。

**关键设计**：TokenFusion模块中的SOAP机制利用注意力权重来选择重要的patch嵌入，并将它们加权平均，从而生成[FG]token。双头LLM派生分类器中的冻结分类器使用CLIP的文本编码器对LLM生成的文本描述进行编码，并将其作为文本先验。可学习的分类器使用交叉熵损失函数进行训练，目标是最小化预测标签与伪标签之间的差异。动态知识聚合使用一个可学习的参数来控制LLM/CLIP先验和TokenFusion输出之间的权重。

## 📊 实验亮点

microCLIP在13个细粒度图像分类基准测试中取得了显著的性能提升，平均精度提升了2.90%。例如，在CUB-200-2011数据集上，microCLIP的精度达到了87.5%，超过了现有的无监督微调方法。实验结果表明，microCLIP能够有效地利用细粒度信息，提升模型的分类性能。

## 🎯 应用场景

microCLIP在细粒度图像分类领域具有广泛的应用前景，例如鸟类识别、植物分类、车型识别等。该方法可以应用于智能安防、自动驾驶、生物多样性保护等领域，具有重要的实际价值。未来，可以进一步研究如何将microCLIP应用于其他视觉任务，例如目标检测、图像分割等，并探索更有效的特征融合和知识迁移方法。

## 📄 摘要（原文）

> Unsupervised adaptation of CLIP-based vision-language models (VLMs) for fine-grained image classification requires sensitivity to microscopic local cues. While CLIP exhibits strong zero-shot transfer, its reliance on coarse global features restricts its performance on fine-grained classification tasks. Prior efforts inject fine-grained knowledge by aligning large language model (LLM) descriptions with the CLIP $\texttt{[CLS]}$ token; however, this approach overlooks spatial precision. We propose $\textbf{microCLIP}$, a self-training framework that jointly refines CLIP's visual and textual representations using fine-grained cues. At its core is Saliency-Oriented Attention Pooling (SOAP) within a lightweight TokenFusion module, which builds a saliency-guided $\texttt{[FG]}$ token from patch embeddings and fuses it with the global $\texttt{[CLS]}$ token for coarse-fine alignment. To stabilize adaptation, we introduce a two-headed LLM-derived classifier: a frozen classifier that, via multi-view alignment, provides a stable text-based prior for pseudo-labeling, and a learnable classifier initialized from LLM descriptions and fine-tuned with TokenFusion. We further develop Dynamic Knowledge Aggregation, which convexly combines fixed LLM/CLIP priors with TokenFusion's evolving logits to iteratively refine pseudo-labels. Together, these components uncover latent fine-grained signals in CLIP, yielding a consistent $2.90\%$ average accuracy gain across 13 fine-grained benchmarks while requiring only light adaptation. Our code is available at https://github.com/sathiiii/microCLIP.

