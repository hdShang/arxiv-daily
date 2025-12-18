---
layout: default
title: AdaPerceiver: Transformers with Adaptive Width, Depth, and Tokens
---

# AdaPerceiver: Transformers with Adaptive Width, Depth, and Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18105" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18105v1</a>
  <a href="https://arxiv.org/pdf/2511.18105.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18105v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18105v1', 'AdaPerceiver: Transformers with Adaptive Width, Depth, and Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Purvish Jajal, Nick John Eliopoulos, Benjamin Shiue-Hal Chou, George K. Thiruvathukal, Yung-Hsiang Lu, James C. Davis

**分类**: cs.CV, cs.LG

**发布日期**: 2025-11-22

---

## 💡 一句话要点

**AdaPerceiver：提出首个在深度、宽度和tokens上自适应的Transformer架构。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自适应Transformer` `动态计算` `深度自适应` `宽度自适应` `Token选择` `图像分类` `语义分割`

## 📋 核心要点

1. 现有Transformer模型在推理时计算资源分配固定，难以适应不同硬件和延迟约束。
2. AdaPerceiver提出一种新的Transformer架构，可在深度、宽度和tokens三个维度上进行自适应调整。
3. 实验表明，AdaPerceiver在图像分类、语义分割和深度估计任务上均取得了显著的性能提升。

## 📝 摘要（中文）

现代Transformer架构在各种任务和领域中表现出色，但在推理时如何分配计算资源方面仍然僵化。实际部署通常需要模型适应不同的硬件和延迟约束，但大多数动态计算方法都集中在单个轴上，例如减少tokens的数量。本文提出了一种新的能力：AdaPerceiver，这是第一个在单个模型中统一实现深度、宽度和tokens自适应的Transformer架构。论文提出了一个支持沿这些轴进行自适应的架构，并将其与有效的联合训练方案相结合，以确保模型在其各种配置中保持性能。在图像分类、语义分割和深度估计任务上评估了AdaPerceiver。在图像分类上，AdaPerceiver扩展了精度-吞吐量Pareto前沿，实现了85.4%的准确率，同时比FlexiViT-L产生高36%的吞吐量。在密集预测方面，AdaPerceiver在语义分割和深度估计上与ViT-H/14相匹配，同时具有约26倍更少的编码器FLOPs（浮点运算）。最后，论文展示了配备策略的AdaPerceiver如何在保持ImageNet1K准确率（±0.1个百分点）的同时，将FLOPs降低24-33%。

## 🔬 方法详解

**问题定义**：现有Transformer模型在推理时计算资源分配策略是静态的，无法根据实际的硬件环境和延迟要求进行动态调整。这导致模型在资源受限的场景下难以达到最佳性能，或者在资源充足的场景下造成计算资源的浪费。现有的动态计算方法通常只关注单个维度的自适应，例如减少token数量，而忽略了模型深度和宽度的重要性。

**核心思路**：AdaPerceiver的核心思路是设计一种可以在深度、宽度和tokens三个维度上进行自适应调整的Transformer架构。通过在训练过程中学习不同配置下的模型参数，AdaPerceiver可以在推理时根据实际需求选择合适的配置，从而在精度和效率之间取得平衡。这种统一的自适应能力使得AdaPerceiver能够更好地适应不同的硬件环境和延迟约束。

**技术框架**：AdaPerceiver的整体架构基于Transformer，但引入了自适应模块来实现深度、宽度和tokens的动态调整。具体来说，模型包含多个Transformer层，每一层都可以选择是否被激活。同时，每一层的宽度（即隐藏层维度）也可以动态调整。此外，模型还采用了一种token选择机制，可以根据输入图像的内容选择保留哪些tokens。在训练过程中，模型通过联合训练的方式学习不同配置下的参数，并使用一种特殊的损失函数来鼓励模型在不同配置下保持一致的性能。

**关键创新**：AdaPerceiver最重要的技术创新点在于其统一的自适应能力。与现有方法相比，AdaPerceiver可以同时在深度、宽度和tokens三个维度上进行动态调整，从而更加灵活地适应不同的硬件环境和延迟约束。此外，AdaPerceiver还提出了一种有效的联合训练方案，可以确保模型在不同配置下保持一致的性能。

**关键设计**：AdaPerceiver的关键设计包括：1) 可跳过的Transformer层，允许模型动态调整深度；2) 可变宽度的隐藏层，允许模型动态调整宽度；3) 基于注意力的token选择机制，允许模型动态调整tokens数量；4) 一种特殊的损失函数，用于鼓励模型在不同配置下保持一致的性能。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

AdaPerceiver在图像分类任务上，实现了85.4%的准确率，同时比FlexiViT-L提高了36%的吞吐量。在密集预测任务上，AdaPerceiver在语义分割和深度估计上与ViT-H/14的性能相当，但编码器的FLOPs减少了约26倍。此外，配备策略的AdaPerceiver可以在保持ImageNet1K准确率不变的情况下，将FLOPs降低24-33%。这些实验结果表明，AdaPerceiver在精度和效率之间取得了良好的平衡。

## 🎯 应用场景

AdaPerceiver具有广泛的应用前景，尤其适用于资源受限的边缘设备和需要实时响应的场景。例如，它可以应用于移动端的图像识别、自动驾驶中的目标检测、以及视频监控中的异常行为检测等。通过动态调整模型的深度、宽度和tokens数量，AdaPerceiver可以在保证精度的前提下，显著降低计算成本和延迟，从而实现更高效的部署和应用。

## 📄 摘要（原文）

> Modern transformer architectures achieve remarkable performance across tasks and domains but remain rigid in how they allocate computation at inference time. Real-world deployment often requires models to adapt to diverse hardware and latency constraints, yet most approaches to dynamic computation focus on a single axis -- such as reducing the number of tokens. We present a novel capability: AdaPerceiver, the first transformer architecture with unified adaptivity across depth, width, and tokens within a single model. We propose an architecture that supports adaptivity along these axes. We couple this with an efficient joint training regime that ensures the model maintains performance across its various configurations. We evaluate AdaPerceiver on image classification, semantic segmentation, and depth estimation tasks. On image classification, AdaPerceiver expands the accuracy-throughput Pareto front. It achieves 85.4% accuracy while yielding 36% higher throughput than FlexiViT-L. On dense prediction, AdaPerceiver matches ViT-H/14 while having $\sim$26x fewer encoder FLOPs (floating-point operations) on semantic segmentation and depth estimation. Finally, we show how AdaPerceiver equipped with a policy can maintain ImageNet1K accuracy ($\pm0.1$ percentage points) while reducing FLOPs by $24-33$%.

