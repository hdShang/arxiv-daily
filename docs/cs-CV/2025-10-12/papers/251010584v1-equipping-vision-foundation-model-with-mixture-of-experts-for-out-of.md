---
layout: default
title: Equipping Vision Foundation Model with Mixture of Experts for Out-of-Distribution Detection
---

# Equipping Vision Foundation Model with Mixture of Experts for Out-of-Distribution Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10584" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10584v1</a>
  <a href="https://arxiv.org/pdf/2510.10584.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10584v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10584v1', 'Equipping Vision Foundation Model with Mixture of Experts for Out-of-Distribution Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shizhen Zhao, Jiahui Liu, Xin Wen, Haoru Tan, Xiaojuan Qi

**分类**: cs.CV

**发布日期**: 2025-10-12

---

## 💡 一句话要点

**提出MoFE模块和动态Mixup策略，提升视觉基础模型在OOD检测中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分布外检测` `视觉基础模型` `特征专家混合` `动态Mixup` `深度学习`

## 📋 核心要点

1. 现有方法在OOD检测中，当语义空间较大时，视觉基础模型的性能不佳，决策边界复杂导致优化困难。
2. 提出特征专家混合(MoFE)模块，将特征划分为子空间，捕获复杂数据分布并细化决策边界。
3. 引入动态-$β$ Mixup策略，自适应调整插值权重，提升困难类别的特征学习，实验结果显著优于基线。

## 📝 摘要（中文）

预训练视觉基础模型已经改变了许多计算机视觉任务。尽管它们具有学习判别性和泛化性特征的强大能力，这对于分布外(OOD)检测至关重要，但它们对这项任务的影响仍未得到充分探索。受此差距的推动，我们系统地研究了用于OOD检测的代表性视觉基础模型。我们的研究结果表明，即使没有在域内(ID)数据上进行微调，预训练的DINOv2模型自然地为OOD检测提供了高度判别性的特征空间，实现了与现有最先进方法相当的性能，而无需复杂的设计。除此之外，我们还探讨了在域内(ID)数据上微调基础模型如何增强OOD检测。然而，我们观察到，在具有较大语义空间的场景中，视觉基础模型的性能仍然不能令人满意。这是由于类别数量的增加导致决策边界的复杂性增加，这使得优化过程复杂化。为了缓解这个问题，我们提出了特征专家混合(MoFE)模块，该模块将特征划分为子空间，有效地捕获复杂的数据分布并细化决策边界。此外，我们引入了一种动态-$β$ Mixup策略，该策略从动态beta分布中采样插值权重。这适应了不同类别之间不同程度的学习难度，从而改进了更具挑战性类别的特征学习。大量的实验证明了我们方法的有效性，显著优于基线方法。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉基础模型在分布外(OOD)检测任务中，尤其是在具有较大语义空间的场景下，性能不佳的问题。现有的方法在处理复杂数据分布和优化决策边界方面存在困难，导致OOD检测的准确率下降。

**核心思路**：论文的核心思路是通过将特征空间划分为多个子空间，并利用专家混合模型(MoFE)来学习每个子空间的特征表示，从而降低决策边界的复杂性。同时，引入动态Mixup策略，根据类别的学习难度动态调整数据增强的强度，以提升模型对困难类别的识别能力。

**技术框架**：整体框架包括以下几个主要模块：1) 特征提取器：使用预训练的视觉基础模型（如DINOv2）提取图像特征。2) 特征专家混合(MoFE)模块：将提取的特征输入MoFE模块，该模块将特征划分为多个子空间，并学习每个子空间的特征表示。3) 分类器：使用学习到的特征表示进行分类，并输出OOD检测结果。4) 动态-$β$ Mixup策略：在训练过程中，使用动态Mixup策略进行数据增强，以提升模型对困难类别的识别能力。

**关键创新**：论文的关键创新在于提出了特征专家混合(MoFE)模块和动态-$β$ Mixup策略。MoFE模块通过将特征空间划分为多个子空间，降低了决策边界的复杂性，使得模型能够更好地学习复杂的数据分布。动态Mixup策略则根据类别的学习难度动态调整数据增强的强度，从而提升了模型对困难类别的识别能力。与现有方法相比，该方法能够更有效地处理具有较大语义空间的OOD检测问题。

**关键设计**：MoFE模块的关键设计包括：1) 使用多个专家网络来学习每个子空间的特征表示。2) 使用门控网络来动态地选择每个专家的权重。动态Mixup策略的关键设计包括：1) 使用动态beta分布来采样插值权重。2) 根据类别的学习难度动态调整beta分布的参数。

## 📊 实验亮点

实验结果表明，提出的MoFE模块和动态Mixup策略能够显著提升视觉基础模型在OOD检测中的性能。例如，在多个基准数据集上，该方法相比于现有方法取得了显著的性能提升，尤其是在具有较大语义空间的场景下，性能提升更为明显。具体性能数据在论文中给出。

## 🎯 应用场景

该研究成果可应用于安全监控、医疗诊断、自动驾驶等领域。例如，在安全监控中，可以检测异常事件；在医疗诊断中，可以识别罕见疾病；在自动驾驶中，可以识别未知的交通状况。该研究有助于提高人工智能系统的鲁棒性和可靠性，具有重要的实际应用价值和广阔的未来发展前景。

## 📄 摘要（原文）

> Pre-trained vision foundation models have transformed many computer vision tasks. Despite their strong ability to learn discriminative and generalizable features crucial for out-of-distribution (OOD) detection, their impact on this task remains underexplored. Motivated by this gap, we systematically investigate representative vision foundation models for OOD detection. Our findings reveal that a pre-trained DINOv2 model, even without fine-tuning on in-domain (ID) data, naturally provides a highly discriminative feature space for OOD detection, achieving performance comparable to existing state-of-the-art methods without requiring complex designs. Beyond this, we explore how fine-tuning foundation models on in-domain (ID) data can enhance OOD detection. However, we observe that the performance of vision foundation models remains unsatisfactory in scenarios with a large semantic space. This is due to the increased complexity of decision boundaries as the number of categories grows, which complicates the optimization process. To mitigate this, we propose the Mixture of Feature Experts (MoFE) module, which partitions features into subspaces, effectively capturing complex data distributions and refining decision boundaries. Further, we introduce a Dynamic-$β$ Mixup strategy, which samples interpolation weights from a dynamic beta distribution. This adapts to varying levels of learning difficulty across categories, improving feature learning for more challenging categories. Extensive experiments demonstrate the effectiveness of our approach, significantly outperforming baseline methods.

