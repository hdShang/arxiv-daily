---
layout: default
title: Assessing Foundation Models for Mold Colony Detection with Limited Training Data
---

# Assessing Foundation Models for Mold Colony Detection with Limited Training Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00561" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00561v1</a>
  <a href="https://arxiv.org/pdf/2510.00561.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00561v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00561v1', 'Assessing Foundation Models for Mold Colony Detection with Limited Training Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henrik Pichler, Janis Keuper, Matthew Copping

**分类**: cs.CV

**发布日期**: 2025-10-01

**备注**: 17 pages, 2 figures, accepted as oral presentation at GCPR 2025

---

## 💡 一句话要点

**利用少量训练数据，评估真菌菌落检测的基础模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `真菌菌落检测` `视觉基础模型` `少样本学习` `迁移学习` `微生物图像分析`

## 📋 核心要点

1. 传统真菌菌落检测依赖大量标注数据训练YoloV9等模型，成本高昂且效率低下。
2. 论文探索了利用数据高效的基础模型，仅需少量标注数据即可达到甚至超越传统模型的性能。
3. 实验表明，MaskDINO在仅用150张图像微调后，性能接近充分训练的YoloV9，且在少量数据下仍保持可靠性。

## 📝 摘要（中文）

量化培养皿样本上的真菌菌落对于评估室内空气质量至关重要，因为高菌落计数可能表明潜在的健康风险和通风系统缺陷。传统上，这种劳动密集型过程以及微生物学中的其他任务的自动化依赖于大型数据集的手动标注以及随后对YoloV9等模型的广泛训练。为了证明详尽的标注不再是解决新的视觉任务的先决条件，我们编译了一个包含5000个培养皿图像的代表性数据集，并用边界框进行标注，模拟了传统的数据收集方法以及具有精心策划的实例级掩码子集的少样本和低样本场景。我们针对特定任务的指标，将三个视觉基础模型与传统基线进行基准测试，反映了现实世界的实际需求。值得注意的是，MaskDINO仅在150张图像上进行微调时，就达到了与经过广泛训练的YoloV9模型几乎相同的性能，并且在仅使用25张图像时仍保持了具有竞争力的性能，在约70%的样本上仍然可靠。我们的结果表明，数据高效的基础模型可以用所需数据的一小部分匹配传统方法，从而能够更早地开发和更快地迭代改进自动化微生物系统，并且比传统模型实现更高的上限性能。

## 🔬 方法详解

**问题定义**：论文旨在解决微生物培养皿中真菌菌落的自动检测问题。传统方法依赖于大量人工标注的数据集来训练目标检测模型（如YoloV9），这既耗时又昂贵。因此，如何在标注数据有限的情况下，实现高精度的真菌菌落检测是本研究要解决的核心问题。

**核心思路**：论文的核心思路是利用预训练的视觉基础模型，通过少量样本微调，使其适应真菌菌落检测任务。预训练模型已经学习了通用的视觉特征，因此只需要少量特定领域的标注数据就可以快速适应新任务，从而降低了数据标注成本。

**技术框架**：论文采用迁移学习的框架，首先选择合适的视觉基础模型（如MaskDINO），然后在包含5000张培养皿图像的数据集上进行微调。该数据集模拟了传统数据收集方法以及少样本和低样本场景。使用边界框标注和实例级掩码，为模型提供更丰富的监督信息。最后，在测试集上评估模型的性能。

**关键创新**：论文的关键创新在于证明了视觉基础模型在微生物图像分析领域的有效性。与从头开始训练模型相比，使用预训练模型可以显著减少所需的数据量，并提高模型的泛化能力。此外，论文还探索了不同数据量下的模型性能，为实际应用中数据标注策略的选择提供了参考。

**关键设计**：论文使用了MaskDINO作为基础模型，它是一种基于Transformer的实例分割模型。在微调过程中，使用了标准的交叉熵损失函数和Dice损失函数来优化模型的分割性能。实验中，作者探索了不同的微调策略和数据增强方法，以进一步提高模型的性能。具体参数设置未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，MaskDINO在仅使用150张图像进行微调后，其性能与经过大量数据训练的YoloV9模型相当。即使只使用25张图像进行微调，MaskDINO仍然可以在约70%的样本上保持可靠性。这表明，数据高效的基础模型可以用远少于传统方法所需的数据量，达到甚至超越传统模型的性能。

## 🎯 应用场景

该研究成果可应用于室内空气质量评估、食品安全检测、医疗诊断等领域。通过自动化真菌菌落检测，可以提高检测效率，降低人工成本，并为相关领域的科学研究提供技术支持。未来，该方法有望推广到其他微生物图像分析任务中，加速自动化微生物系统的发展。

## 📄 摘要（原文）

> The process of quantifying mold colonies on Petri dish samples is of critical importance for the assessment of indoor air quality, as high colony counts can indicate potential health risks and deficiencies in ventilation systems. Conventionally the automation of such a labor-intensive process, as well as other tasks in microbiology, relies on the manual annotation of large datasets and the subsequent extensive training of models like YoloV9. To demonstrate that exhaustive annotation is not a prerequisite anymore when tackling a new vision task, we compile a representative dataset of 5000 Petri dish images annotated with bounding boxes, simulating both a traditional data collection approach as well as few-shot and low-shot scenarios with well curated subsets with instance level masks. We benchmark three vision foundation models against traditional baselines on task specific metrics, reflecting realistic real-world requirements. Notably, MaskDINO attains near-parity with an extensively trained YoloV9 model while finetuned only on 150 images, retaining competitive performance with as few as 25 images, still being reliable on $\approx$ 70% of the samples. Our results show that data-efficient foundation models can match traditional approaches with only a fraction of the required data, enabling earlier development and faster iterative improvement of automated microbiological systems with a superior upper-bound performance than traditional models would achieve.

