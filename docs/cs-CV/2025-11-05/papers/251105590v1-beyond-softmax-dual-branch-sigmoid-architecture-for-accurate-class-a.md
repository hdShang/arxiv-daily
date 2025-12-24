---
layout: default
title: "Beyond Softmax: Dual-Branch Sigmoid Architecture for Accurate Class Activation Maps"
---

# Beyond Softmax: Dual-Branch Sigmoid Architecture for Accurate Class Activation Maps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.05590" class="toolbar-btn" target="_blank">📄 arXiv: 2511.05590v1</a>
  <a href="https://arxiv.org/pdf/2511.05590.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05590v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.05590v1', 'Beyond Softmax: Dual-Branch Sigmoid Architecture for Accurate Class Activation Maps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yoojin Oh, Junhyug Noh

**分类**: cs.CV, cs.LG

**发布日期**: 2025-11-05

**备注**: Accepted at BMVC 2025

**🔗 代码/项目**: [GITHUB](https://github.com/finallyupper/beyond-softmax)

---

## 💡 一句话要点

**提出双分支Sigmoid架构，解决CAM中logit偏移和符号坍塌问题，提升定位精度。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `类激活映射` `可解释性` `弱监督定位` `双分支网络` `Sigmoid分类器`

## 📋 核心要点

1. 传统CAM方法依赖Softmax分类器，存在logit偏移和符号坍塌问题，影响定位精度。
2. 提出双分支Sigmoid架构，解耦分类和定位，利用Sigmoid分支生成更准确的类激活图。
3. 实验表明，该方法在多个数据集上提升了解释保真度和Top-1定位精度，且不损失分类性能。

## 📝 摘要（中文）

类激活映射(CAM)及其扩展已成为可视化深度网络预测依据的重要工具。然而，由于依赖最终的softmax分类器，这些方法存在两个根本性的失真：任意偏置重要性分数的加性logit偏移，以及混淆了兴奋和抑制特征的符号坍塌。我们提出了一种简单的、与架构无关的双分支sigmoid头，将定位与分类解耦。给定任何预训练模型，我们将其分类头克隆到一个以per-class sigmoid输出结束的并行分支中，冻结原始的softmax头，并仅使用类别平衡的二元监督微调sigmoid分支。在推理时，softmax保留识别精度，而类证据图从sigmoid分支生成——保留了特征贡献的大小和符号。我们的方法与大多数CAM变体无缝集成，并且开销可忽略不计。在细粒度任务(CUB-200-2011, Stanford Cars)和WSOL基准(ImageNet-1K, OpenImages30K)上的广泛评估表明，解释保真度得到改善，并且Top-1定位始终获得提升——而分类精度没有任何下降。

## 🔬 方法详解

**问题定义**：现有的类激活映射（CAM）方法依赖于Softmax分类器进行预测，这导致两个主要问题。一是Softmax的logit偏移会任意偏置重要性分数，使得生成的激活图不准确。二是Softmax将兴奋和抑制特征混淆，导致符号坍塌，无法区分正负贡献的特征。这些问题限制了CAM方法在定位和解释模型预测方面的能力。

**核心思路**：论文的核心思路是将分类和定位解耦。通过引入一个并行的Sigmoid分支，专门负责生成类激活图。Softmax分支保持原有的分类功能，而Sigmoid分支则通过二元交叉熵损失进行训练，学习每个类别的独立激活图。这样可以避免Softmax的logit偏移和符号坍塌问题，从而生成更准确的类激活图。

**技术框架**：该方法的核心是双分支架构。首先，给定一个预训练的分类模型，克隆其分类头，创建一个并行的Sigmoid分支。原始的Softmax分支保持冻结，只训练Sigmoid分支。Sigmoid分支的输出是每个类别的独立概率，使用类别平衡的二元交叉熵损失进行训练。在推理阶段，Softmax分支用于分类，而Sigmoid分支用于生成类激活图。该方法可以与大多数CAM变体无缝集成。

**关键创新**：该方法最重要的创新点在于解耦了分类和定位。通过引入独立的Sigmoid分支，避免了Softmax的固有缺陷对类激活图的影响。这种解耦的思想可以应用于其他需要解释性的深度学习模型中，提高模型的可解释性和定位精度。

**关键设计**：关键的设计包括：1) 使用类别平衡的二元交叉熵损失函数来训练Sigmoid分支，以解决类别不平衡问题。2) 冻结Softmax分支，只训练Sigmoid分支，以保持分类精度。3) Sigmoid分支的输出是每个类别的独立概率，而不是Softmax的概率分布。4) 该方法与大多数CAM变体兼容，可以方便地应用于不同的模型和任务。

## 📊 实验亮点

实验结果表明，该方法在CUB-200-2011、Stanford Cars、ImageNet-1K和OpenImages30K等数据集上，显著提升了解释保真度和Top-1定位精度，同时保持了分类精度。例如，在ImageNet-1K数据集上，Top-1定位精度提升了多个百分点。这些结果表明，该方法能够有效地解决Softmax带来的问题，生成更准确的类激活图。

## 🎯 应用场景

该研究成果可广泛应用于需要模型可解释性的领域，例如医学图像诊断、自动驾驶、安全监控等。通过提供更准确的类激活图，可以帮助用户理解模型的决策过程，提高模型的可靠性和可信度。此外，该方法还可以用于弱监督目标定位，提高定位精度。

## 📄 摘要（原文）

> Class Activation Mapping (CAM) and its extensions have become indispensable tools for visualizing the evidence behind deep network predictions. However, by relying on a final softmax classifier, these methods suffer from two fundamental distortions: additive logit shifts that arbitrarily bias importance scores, and sign collapse that conflates excitatory and inhibitory features. We propose a simple, architecture-agnostic dual-branch sigmoid head that decouples localization from classification. Given any pretrained model, we clone its classification head into a parallel branch ending in per-class sigmoid outputs, freeze the original softmax head, and fine-tune only the sigmoid branch with class-balanced binary supervision. At inference, softmax retains recognition accuracy, while class evidence maps are generated from the sigmoid branch -- preserving both magnitude and sign of feature contributions. Our method integrates seamlessly with most CAM variants and incurs negligible overhead. Extensive evaluations on fine-grained tasks (CUB-200-2011, Stanford Cars) and WSOL benchmarks (ImageNet-1K, OpenImages30K) show improved explanation fidelity and consistent Top-1 Localization gains -- without any drop in classification accuracy. Code is available at https://github.com/finallyupper/beyond-softmax.

