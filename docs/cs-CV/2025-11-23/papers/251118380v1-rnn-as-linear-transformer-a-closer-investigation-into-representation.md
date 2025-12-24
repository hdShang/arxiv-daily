---
layout: default
title: "RNN as Linear Transformer: A Closer Investigation into Representational Potentials of Visual Mamba Models"
---

# RNN as Linear Transformer: A Closer Investigation into Representational Potentials of Visual Mamba Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18380" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18380v1</a>
  <a href="https://arxiv.org/pdf/2511.18380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18380v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18380v1', 'RNN as Linear Transformer: A Closer Investigation into Representational Potentials of Visual Mamba Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timing Yang, Guoyizhe Wei, Alan Yuille, Feng Wang

**分类**: cs.CV

**发布日期**: 2025-11-23

---

## 💡 一句话要点

**分析Mamba视觉模型表征能力，揭示其与线性Transformer的关联**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉Mamba` `状态空间模型` `线性注意力` `低秩近似` `激活图评估` `自监督学习` `模型可解释性`

## 📋 核心要点

1. 现有视觉Mamba模型的内部机制尚不明确，阻碍了对其表征能力的深入理解。
2. 论文通过理论分析和实验验证，揭示了Mamba与Softmax和线性注意力之间的联系。
3. 实验表明，Mamba在长程依赖建模和可解释性方面具有潜力，并在ImageNet上取得了优异的线性探测精度。

## 📝 摘要（中文）

Mamba最近作为视觉任务的有效骨干网络受到了广泛关注。然而，其在视觉领域中的潜在机制仍然知之甚少。本文系统地研究了Mamba的表征特性，并做出了三个主要贡献。首先，我们从理论上分析了Mamba与Softmax和线性注意力之间的关系，证实它可以被视为Softmax注意力的低秩近似，从而弥合了Softmax和线性形式之间的表征差距。其次，我们引入了一种新的二元分割指标用于激活图评估，将定性评估扩展到定量测量，证明了Mamba建模长程依赖关系的能力。第三，通过利用DINO进行自监督预训练，我们获得了比标准监督方法产生的更清晰的激活图，突出了Mamba的可解释性潜力。值得注意的是，我们的模型在ImageNet上实现了78.5%的线性探测精度，突显了其强大的性能。我们希望这项工作能够为未来基于Mamba的视觉架构的研究提供有价值的见解。

## 🔬 方法详解

**问题定义**：现有视觉Transformer模型计算复杂度高，难以处理长序列。Mamba作为一种新型序列模型，在视觉领域展现出潜力，但其内部机制和表征能力尚不明确，限制了其进一步发展和应用。现有方法缺乏对Mamba表征能力的深入分析和有效评估手段。

**核心思路**：论文的核心思路是将Mamba与Softmax和线性注意力机制联系起来，通过理论分析证明Mamba可以视为Softmax注意力的低秩近似。同时，引入新的二元分割指标对Mamba的激活图进行定量评估，并利用自监督预训练提升Mamba的可解释性。

**技术框架**：论文主要包含三个部分：1) 理论分析Mamba与Softmax和线性注意力的关系；2) 提出新的二元分割指标评估Mamba的激活图；3) 利用DINO进行自监督预训练，提升Mamba的可解释性。整体流程是先通过理论分析建立联系，然后通过实验验证和评估Mamba的表征能力，最后通过自监督预训练提升其性能和可解释性。

**关键创新**：论文的关键创新在于：1) 从理论上证明了Mamba可以视为Softmax注意力的低秩近似，弥合了Softmax和线性形式之间的表征差距；2) 提出了新的二元分割指标，将激活图的评估从定性分析扩展到定量分析。

**关键设计**：论文的关键设计包括：1) 使用状态空间模型（SSM）作为Mamba的基础架构；2) 利用选择机制动态调整SSM的参数；3) 引入新的二元分割指标，该指标基于激活图的阈值分割，评估分割结果与ground truth的相似度；4) 使用DINO进行自监督预训练，学习更鲁棒的特征表示。

## 📊 实验亮点

论文通过实验验证了Mamba在视觉任务中的有效性。特别是在ImageNet线性探测任务中，模型取得了78.5%的精度，证明了其强大的表征能力。此外，通过DINO自监督预训练，Mamba获得了更清晰的激活图，提升了模型的可解释性。

## 🎯 应用场景

该研究成果可应用于各种视觉任务，如图像分类、目标检测、语义分割等。通过深入理解Mamba的表征能力，可以设计更高效、更可解释的视觉模型。此外，该研究提出的二元分割指标可以作为评估其他视觉模型激活图的通用工具，促进模型可解释性研究。

## 📄 摘要（原文）

> Mamba has recently garnered attention as an effective backbone for vision tasks. However, its underlying mechanism in visual domains remains poorly understood. In this work, we systematically investigate Mamba's representational properties and make three primary contributions. First, we theoretically analyze Mamba's relationship to Softmax and Linear Attention, confirming that it can be viewed as a low-rank approximation of Softmax Attention and thereby bridging the representational gap between Softmax and Linear forms. Second, we introduce a novel binary segmentation metric for activation map evaluation, extending qualitative assessments to a quantitative measure that demonstrates Mamba's capacity to model long-range dependencies. Third, by leveraging DINO for self-supervised pretraining, we obtain clearer activation maps than those produced by standard supervised approaches, highlighting Mamba's potential for interpretability. Notably, our model also achieves a 78.5 percent linear probing accuracy on ImageNet, underscoring its strong performance. We hope this work can provide valuable insights for future investigations of Mamba-based vision architectures.

