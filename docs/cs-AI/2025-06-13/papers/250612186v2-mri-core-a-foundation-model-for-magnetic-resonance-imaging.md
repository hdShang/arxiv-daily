---
layout: default
title: "MRI-CORE: A Foundation Model for Magnetic Resonance Imaging"
---

# MRI-CORE: A Foundation Model for Magnetic Resonance Imaging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12186" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12186v2</a>
  <a href="https://arxiv.org/pdf/2506.12186.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12186v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12186v2', 'MRI-CORE: A Foundation Model for Magnetic Resonance Imaging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Dong, Yuwen Chen, Hanxue Gu, Nicholas Konz, Yaqian Chen, Qihang Li, Maciej A. Mazurowski

**分类**: eess.IV, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-06-13 (更新: 2025-07-22)

**备注**: 36 pages, under review

---

## 💡 一句话要点

**提出MRI-CORE以解决MRI数据标注不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `磁共振成像` `深度学习` `基础模型` `迁移学习` `数据效率` `医学影像分析` `自动化诊断`

## 📋 核心要点

1. 现有的MRI模型训练需要大量标注数据，且高精度注释成本高，数据隐私问题严重。
2. MRI-CORE通过使用超过600万切片的MRI数据进行训练，旨在提高模型的性能和数据利用效率。
3. 实验结果显示，MRI-CORE在多项任务中超越了现有最先进的方法，尤其是在数据受限的分割任务中表现突出。

## 📝 摘要（中文）

磁共振成像（MRI）在深度学习的广泛应用中展现出自动化诊断和预后工具的潜力。然而，训练新模型需要大量标注数据，这在高精度注释和数据隐私方面面临挑战。为了解决这一问题，本文提出了MRI-CORE，一个基于视觉的基础模型，使用来自18个身体部位的超过110,000个MRI体积的600万切片进行训练。实验结果表明，在13个数据受限的分割任务中，MRI-CORE在性能上显著优于现有方法，并在图像分类和零样本分割中也表现出色，显示出其在数据高效开发人工智能模型方面的强大潜力。我们还提供了关于哪些策略能产生最有用的基础模型的数据，以及一个新颖的分析，探讨了预训练数据与下游任务数据之间的相似性与迁移学习性能的关系。我们的模型已公开发布，采用宽松许可。

## 🔬 方法详解

**问题定义**：本文旨在解决MRI模型训练中对大量标注数据的依赖，现有方法在数据获取和标注方面面临高成本和隐私问题的挑战。

**核心思路**：MRI-CORE通过利用大规模的未标注MRI数据进行预训练，结合迁移学习策略，旨在提高模型在下游任务中的表现，减少对标注数据的需求。

**技术框架**：该模型的整体架构包括数据预处理、模型预训练、迁移学习和下游任务评估四个主要阶段。预训练阶段使用了来自不同身体部位的MRI切片，确保模型的广泛适应性。

**关键创新**：MRI-CORE的主要创新在于其大规模的预训练数据集和针对特定任务的迁移学习策略，这与传统方法依赖小规模标注数据的方式有本质区别。

**关键设计**：在模型设计中，采用了特定的损失函数以优化分割和分类任务的性能，同时在网络结构上进行了调整，以适应不同类型的MRI图像特征。

## 📊 实验亮点

在实验中，MRI-CORE在13个数据受限的分割任务中表现出显著提升，超越了现有最先进的方法，具体性能提升幅度未知。此外，在图像分类和零样本分割任务中也展现出强大的潜力，证明了其在数据高效开发中的应用价值。

## 🎯 应用场景

MRI-CORE的研究成果可广泛应用于医学影像分析、自动化诊断系统以及临床决策支持工具等领域。其高效的数据利用能力将推动AI在医疗领域的进一步发展，降低对大量标注数据的依赖，提升诊断效率和准确性。

## 📄 摘要（原文）

> The widespread use of Magnetic Resonance Imaging (MRI) in combination with deep learning shows promise for many high-impact automated diagnostic and prognostic tools. However, training new models requires large amounts of labeled data, a challenge due to high cost of precise annotations and data privacy. To address this issue, we introduce the MRI-CORE, a vision foundation model trained using more than 6 million slices from over 110 thousand MRI volumes across 18 body locations. Our experiments show notable improvements in performance over state-of-the-art methods in 13 data-restricted segmentation tasks, as well as in image classification, and zero-shot segmentation, showing the strong potential of MRI-CORE to enable data-efficient development of artificial intelligence models. We also present data on which strategies yield most useful foundation models and a novel analysis relating similarity between pre-training and downstream task data with transfer learning performance. Our model is publicly available with a permissive license.

