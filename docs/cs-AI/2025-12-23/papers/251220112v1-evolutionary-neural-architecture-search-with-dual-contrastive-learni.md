---
layout: default
title: Evolutionary Neural Architecture Search with Dual Contrastive Learning
---

# Evolutionary Neural Architecture Search with Dual Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20112" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20112v1</a>
  <a href="https://arxiv.org/pdf/2512.20112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20112v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20112v1', 'Evolutionary Neural Architecture Search with Dual Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xian-Rong Zhang, Yue-Jiao Gong, Wei-Neng Chen, Jun Zhang

**分类**: cs.NE, cs.AI

**发布日期**: 2025-12-23

**备注**: 26 pages

---

## 💡 一句话要点

**提出DCL-ENAS，利用双重对比学习提升进化神经架构搜索的效率和精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `神经架构搜索` `进化算法` `对比学习` `自监督学习` `神经网络` `模型优化`

## 📋 核心要点

1. ENAS依赖神经预测器指导搜索，但获取带标签的架构训练数据成本高昂，限制了预测器的精度。
2. DCL-ENAS通过双重对比学习，先无监督学习架构表示，再有监督微调相对性能预测，降低了对标注数据的需求。
3. 实验表明，DCL-ENAS在多个NASBench数据集和真实心电图分类任务上均取得了显著的性能提升。

## 📝 摘要（中文）

本文提出了一种基于双重对比学习的进化神经架构搜索方法（DCL-ENAS），旨在解决ENAS中训练数据获取成本高昂的问题。DCL-ENAS分两个阶段训练神经预测器：第一阶段，使用对比自监督学习从神经架构中学习有意义的表示，无需标签；第二阶段，通过对比学习进行微调，准确预测不同架构的相对性能，从而指导进化搜索。在NASBench-101和NASBench-201上的实验表明，DCL-ENAS取得了最高的验证精度，超越了已发表的最强基线0.05% (ImageNet16-120)到0.39% (NASBench-101)。在真实世界的心电图心律失常分类任务中，DCL-ENAS的性能比通过随机搜索获得的手动设计的非NAS模型提高了约2.5个百分点，且仅需7.7 GPU-days。

## 🔬 方法详解

**问题定义**：进化神经架构搜索（ENAS）依赖于神经预测器来指导架构搜索过程。然而，训练这些预测器需要大量的已训练架构及其性能标签，这导致了巨大的计算成本。尤其是在计算资源有限的情况下，如何利用有限的架构-标签对来训练一个高精度的预测器，是ENAS面临的关键挑战。现有方法通常直接预测架构的绝对性能，这需要大量的训练数据才能达到理想的精度。

**核心思路**：DCL-ENAS的核心思路是利用对比学习来降低对绝对性能预测的需求。它不是直接预测架构的绝对性能，而是预测不同架构之间的相对性能差异。这种相对性能预测对噪声和偏差具有更强的鲁棒性，并且可以使用更少的训练数据来实现更高的精度。通过对比学习，模型可以学习到架构之间的相似性和差异性，从而更好地进行排序和选择。

**技术框架**：DCL-ENAS包含两个主要的对比学习阶段。第一阶段是对比自监督学习，该阶段利用大量的未标记架构数据，通过对比学习的方式学习架构的表示。具体来说，对于每个架构，通过数据增强等方式生成多个变体，然后通过对比学习的目标函数，使得同一个架构的不同变体在表示空间中尽可能接近，而不同架构的变体则尽可能远离。第二阶段是对比微调，该阶段利用少量的已标记架构数据，通过对比学习的方式微调第一阶段学习到的架构表示。具体来说，对于每个架构对，根据它们的性能差异构建正负样本对，然后通过对比学习的目标函数，使得性能相似的架构对在表示空间中尽可能接近，而性能差异大的架构对则尽可能远离。

**关键创新**：DCL-ENAS的关键创新在于其双重对比学习框架。第一阶段的对比自监督学习能够有效地利用大量的未标记架构数据，学习到有意义的架构表示，从而为第二阶段的对比微调提供了一个良好的初始化。第二阶段的对比微调则能够有效地利用少量的已标记架构数据，学习到架构之间的相对性能差异，从而提高预测器的精度。这种双重对比学习框架能够显著降低对标注数据的需求，提高ENAS的效率和精度。

**关键设计**：在对比自监督学习阶段，使用了数据增强技术来生成架构变体，例如随机裁剪、旋转等。对比损失函数采用了InfoNCE损失函数，该损失函数能够有效地将相似的样本拉近，将不相似的样本推远。在对比微调阶段，使用了margin ranking loss作为对比损失函数，该损失函数能够有效地学习架构之间的相对性能差异。此外，还使用了warm-up策略来逐步增加对比损失的权重，以避免训练初期出现梯度爆炸等问题。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20112v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20112v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20112v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DCL-ENAS在NASBench-101和NASBench-201上取得了显著的性能提升，超越了已发表的最强基线0.05% (ImageNet16-120)到0.39% (NASBench-101)。在真实世界的心电图心律失常分类任务中，DCL-ENAS的性能比通过随机搜索获得的手动设计的非NAS模型提高了约2.5个百分点，且仅需7.7 GPU-days，表明了其在实际应用中的有效性和效率。

## 🎯 应用场景

DCL-ENAS具有广泛的应用前景，可应用于各种需要自动设计神经网络架构的场景，例如图像分类、目标检测、自然语言处理等。尤其是在计算资源有限或标注数据稀缺的情况下，DCL-ENAS能够显著提高神经架构搜索的效率和精度，降低模型开发的成本。该方法还可以应用于特定领域的模型定制，例如医疗诊断、金融风控等，通过自动搜索针对特定任务优化的神经网络架构，提高模型的性能和泛化能力。

## 📄 摘要（原文）

> Evolutionary Neural Architecture Search (ENAS) has gained attention for automatically designing neural network architectures. Recent studies use a neural predictor to guide the process, but the high computational costs of gathering training data -- since each label requires fully training an architecture -- make achieving a high-precision predictor with { limited compute budget (i.e., a capped number of fully trained architecture-label pairs)} crucial for ENAS success. This paper introduces ENAS with Dual Contrastive Learning (DCL-ENAS), a novel method that employs two stages of contrastive learning to train the neural predictor. In the first stage, contrastive self-supervised learning is used to learn meaningful representations from neural architectures without requiring labels. In the second stage, fine-tuning with contrastive learning is performed to accurately predict the relative performance of different architectures rather than their absolute performance, which is sufficient to guide the evolutionary search. Across NASBench-101 and NASBench-201, DCL-ENAS achieves the highest validation accuracy, surpassing the strongest published baselines by 0.05\% (ImageNet16-120) to 0.39\% (NASBench-101). On a real-world ECG arrhythmia classification task, DCL-ENAS improves performance by approximately 2.5 percentage points over a manually designed, non-NAS model obtained via random search, while requiring only 7.7 GPU-days.

