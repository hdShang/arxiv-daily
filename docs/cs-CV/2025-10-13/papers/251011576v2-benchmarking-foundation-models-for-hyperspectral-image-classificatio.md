---
layout: default
title: Benchmarking foundation models for hyperspectral image classification: Application to cereal crop type mapping
---

# Benchmarking foundation models for hyperspectral image classification: Application to cereal crop type mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11576" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11576v2</a>
  <a href="https://arxiv.org/pdf/2510.11576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11576v2" onclick="toggleFavorite(this, '2510.11576v2', 'Benchmarking foundation models for hyperspectral image classification: Application to cereal crop type mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Walid Elbarz, Mohamed Bourriz, Hicham Hajji, Hamd Ait Abdelali, François Bourzeix

**分类**: cs.CV

**发布日期**: 2025-10-13 (更新: 2025-10-14)

**备注**: currently being reviewed for WHISPERS conference ( Workshop on Hyperspectral Image and Signal Processing: Evolution in Remote Sensing )

---

## 💡 一句话要点

**评估基础模型在 hyperspectral 图像分类中的性能，应用于谷类作物类型识别。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `hyperspectral 图像分类` `基础模型` `Vision Transformers` `作物类型识别` `SpectralEarth 数据集`

## 📋 核心要点

1. 现有方法在 hyperspectral 作物类型识别中泛化能力不足，难以适应不同地理区域和传感器平台。
2. 本研究通过微调在大型 hyperspectral 数据集上预训练的基础模型，提升模型在特定任务上的性能。
3. 实验表明，在 SpectralEarth 数据集上预训练的 Vision Transformers 在作物类型识别中表现最佳，OA 达到 93.5%。

## 📝 摘要（中文）

本研究评估了基础模型在 hyperspectral 作物类型识别中的潜力。具体地，研究对比了三个基础模型：HyperSigma、DOFA 和在 SpectralEarth 数据集（一个大型多时相 hyperspectral 档案）上预训练的 Vision Transformers。这些模型在人工标注的训练区域数据上进行微调，并在独立的测试区域进行评估。性能指标包括总体精度（OA）、平均精度（AA）和 F1 分数。HyperSigma 的 OA 为 34.5% (+/- 1.8%)，DOFA 为 62.6% (+/- 3.5%)，SpectralEarth 模型为 93.5% (+/- 0.8%)。从头开始训练的紧凑型 SpectralEarth 变体达到了 91% 的 OA，突出了模型架构对于跨地理区域和传感器平台的泛化能力的重要性。这些结果为 hyperspectral 作物类型识别的基础模型提供了一个系统的评估，并为未来的模型开发指明了方向。

## 🔬 方法详解

**问题定义**：论文旨在解决 hyperspectral 图像分类在谷类作物类型识别中的应用问题。现有方法在跨区域、跨传感器平台上的泛化能力较弱，需要大量标注数据进行训练，成本较高。

**核心思路**：论文的核心思路是利用在大规模 hyperspectral 数据集上预训练的基础模型，通过微调的方式，使其适应特定的作物类型识别任务。预训练模型能够学习到通用的光谱特征表示，从而减少对特定任务标注数据的依赖，提高模型的泛化能力。

**技术框架**：整体流程包括：1) 选择三个基础模型（HyperSigma, DOFA, SpectralEarth 预训练的 Vision Transformers）；2) 使用人工标注的训练数据对模型进行微调；3) 在独立的测试区域评估模型的性能，使用总体精度（OA）、平均精度（AA）和 F1 分数作为评价指标。

**关键创新**：最重要的创新点在于系统性地评估了不同类型的基础模型在 hyperspectral 图像分类中的性能，并验证了在大规模 hyperspectral 数据集上预训练的模型在作物类型识别任务中的有效性。此外，研究还发现模型架构对于跨区域泛化能力至关重要。

**关键设计**：研究中使用了 Vision Transformers 作为基础模型之一，并在 SpectralEarth 数据集上进行了预训练。SpectralEarth 数据集是一个大型多时相 hyperspectral 档案，包含了丰富的光谱信息。模型的微调过程使用了交叉熵损失函数，并采用了 Adam 优化器。具体的参数设置（如学习率、batch size 等）未知。

## 📊 实验亮点

实验结果表明，在 SpectralEarth 数据集上预训练的 Vision Transformers 模型在谷类作物类型识别中表现最佳，总体精度（OA）达到 93.5% (+/- 0.8%)。即使是从头开始训练的紧凑型 SpectralEarth 变体，也能达到 91% 的 OA，这突出了模型架构的重要性。相比之下，HyperSigma 和 DOFA 的性能明显较差，OA 分别为 34.5% 和 62.6%。

## 🎯 应用场景

该研究成果可应用于精准农业领域，实现对农作物类型的自动识别和面积估算，为农业生产管理提供决策支持。此外，该方法还可以推广到其他地物类型的识别，例如森林类型、土地利用类型等，具有广泛的应用前景。未来，结合无人机或卫星遥感数据，可以实现大范围、高精度的地物类型识别。

## 📄 摘要（原文）

> Foundation models are transforming Earth observation, but their potential for hyperspectral crop mapping remains underexplored. This study benchmarks three foundation models for cereal crop mapping using hyperspectral imagery: HyperSigma, DOFA, and Vision Transformers pre-trained on the SpectralEarth dataset (a large multitemporal hyperspectral archive). Models were fine-tuned on manually labeled data from a training region and evaluated on an independent test region. Performance was measured with overall accuracy (OA), average accuracy (AA), and F1-score. HyperSigma achieved an OA of 34.5% (+/- 1.8%), DOFA reached 62.6% (+/- 3.5%), and the SpectralEarth model achieved an OA of 93.5% (+/- 0.8%). A compact SpectralEarth variant trained from scratch achieved 91%, highlighting the importance of model architecture for strong generalization across geographic regions and sensor platforms. These results provide a systematic evaluation of foundation models for operational hyperspectral crop mapping and outline directions for future model development.

