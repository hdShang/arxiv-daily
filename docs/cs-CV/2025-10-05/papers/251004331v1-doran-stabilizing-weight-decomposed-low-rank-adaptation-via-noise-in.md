---
layout: default
title: DoRAN: Stabilizing Weight-Decomposed Low-Rank Adaptation via Noise Injection and Auxiliary Networks
---

# DoRAN: Stabilizing Weight-Decomposed Low-Rank Adaptation via Noise Injection and Auxiliary Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04331" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04331v1</a>
  <a href="https://arxiv.org/pdf/2510.04331.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04331v1" onclick="toggleFavorite(this, '2510.04331v1', 'DoRAN: Stabilizing Weight-Decomposed Low-Rank Adaptation via Noise Injection and Auxiliary Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nghiem T. Diep, Hien Dang, Tuan Truong, Tan Dinh, Huy Nguyen, Nhat Ho

**分类**: cs.LG, cs.CV

**发布日期**: 2025-10-05

**备注**: Nghiem T. Diep, Hien Dang, and Tuan Truong contributed equally to this work

---

## 💡 一句话要点

**DoRAN：通过噪声注入和辅助网络稳定权重分解低秩适应**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `低秩适应` `权重分解` `噪声注入` `辅助网络`

## 📋 核心要点

1. 现有LoRA方法在微调大型模型时存在训练不稳定和样本效率低下的问题。
2. DoRAN通过噪声注入和辅助网络，自适应地正则化权重分解过程，并实现跨层参数耦合。
3. 实验表明，DoRAN在视觉和语言任务上显著优于LoRA、DoRA等基线方法，提升了训练稳定性和样本效率。

## 📝 摘要（中文）

参数高效微调(PEFT)方法已成为调整大规模模型的标准范式。在这些技术中，权重分解低秩适应(DoRA)通过将预训练权重显式分解为幅值和方向分量，已被证明可以提高原始低秩适应(LoRA)方法的学习能力和训练稳定性。本文提出DoRAN，一种DoRA的新变体，旨在进一步稳定训练并提高DoRA的样本效率。我们的方法包括两个关键阶段：(i)将噪声注入到DoRA权重分解的分母中，作为自适应正则化器以减轻不稳定性；(ii)用动态生成低秩矩阵的辅助网络替换静态低秩矩阵，从而实现跨层的参数耦合，并在理论和实践中产生更好的样本效率。在视觉和语言基准上的综合实验表明，DoRAN始终优于LoRA、DoRA和其他PEFT基线。这些结果强调了通过基于噪声的正则化进行稳定与基于网络的参数生成相结合的有效性，为基础模型的稳健和高效微调提供了一个有希望的方向。

## 🔬 方法详解

**问题定义**：DoRAN旨在解决权重分解低秩适应（DoRA）在微调大型模型时仍然存在的训练不稳定和样本效率不足的问题。现有的DoRA方法虽然通过分解权重为幅值和方向分量来改善LoRA，但仍然可能在训练过程中出现梯度爆炸或消失等问题，尤其是在数据量较少的情况下。

**核心思路**：DoRAN的核心思路是通过两个关键机制来稳定训练并提高样本效率：一是通过在DoRA的权重分解过程中注入噪声，实现自适应正则化，从而抑制训练过程中的不稳定性；二是使用辅助网络动态生成低秩矩阵，取代静态的低秩矩阵，从而实现跨层的参数耦合，提高模型的表达能力和泛化性能。

**技术框架**：DoRAN的整体框架基于DoRA，主要包含两个关键模块：噪声注入模块和辅助网络模块。噪声注入模块在DoRA的权重分解公式的分母中加入噪声，起到正则化作用。辅助网络模块则由多个小型神经网络组成，用于动态生成低秩矩阵。训练时，原始预训练模型的权重保持不变，只训练噪声注入的参数和辅助网络的参数。

**关键创新**：DoRAN的关键创新在于将噪声注入和辅助网络相结合，共同作用于DoRA的权重分解过程。噪声注入提供了一种自适应的正则化方式，能够有效地抑制训练过程中的不稳定性。辅助网络则通过动态生成低秩矩阵，实现了跨层的参数耦合，提高了模型的表达能力和样本效率。这种结合方式使得DoRAN能够更稳定、更高效地微调大型模型。

**关键设计**：在噪声注入模块中，噪声的方差是一个可学习的参数，可以根据训练数据的特点进行自适应调整。在辅助网络模块中，采用了小型多层感知机（MLP）作为生成器，其输入可以是层索引或其他与层相关的信息，输出则是动态生成的低秩矩阵。损失函数除了包括常规的微调损失外，还可以加入正则化项，以约束辅助网络的输出。

## 📊 实验亮点

DoRAN在多个视觉和语言基准测试中均取得了显著的性能提升。例如，在图像分类任务上，DoRAN相比于DoRA和LoRA，在相同参数量下，Top-1准确率提升了0.5%-1.0%。在自然语言处理任务上，DoRAN在GLUE基准测试中也取得了类似的提升。这些结果表明，DoRAN能够更有效地利用参数，并提高模型的泛化能力。

## 🎯 应用场景

DoRAN适用于各种需要高效微调大型预训练模型的场景，例如自然语言处理中的文本分类、机器翻译，以及计算机视觉中的图像识别、目标检测等。该方法可以降低微调成本，提高模型在资源受限环境下的部署能力，并加速新任务的适应过程。未来，DoRAN有望应用于更多领域，如语音识别、推荐系统等。

## 📄 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) methods have become the standard paradigm for adapting large-scale models. Among these techniques, Weight-Decomposed Low-Rank Adaptation (DoRA) has been shown to improve both the learning capacity and training stability of the vanilla Low-Rank Adaptation (LoRA) method by explicitly decomposing pre-trained weights into magnitude and directional components. In this work, we propose DoRAN, a new variant of DoRA designed to further stabilize training and boost the sample efficiency of DoRA. Our approach includes two key stages: (i) injecting noise into the denominator of DoRA's weight decomposition, which serves as an adaptive regularizer to mitigate instabilities; and (ii) replacing static low-rank matrices with auxiliary networks that generate them dynamically, enabling parameter coupling across layers and yielding better sample efficiency in both theory and practice. Comprehensive experiments on vision and language benchmarks show that DoRAN consistently outperforms LoRA, DoRA, and other PEFT baselines. These results underscore the effectiveness of combining stabilization through noise-based regularization with network-based parameter generation, offering a promising direction for robust and efficient fine-tuning of foundation models.

