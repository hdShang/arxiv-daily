---
layout: default
title: Towards Explainable Quantum AI: Informing the Encoder Selection of Quantum Neural Networks via Visualization
---

# Towards Explainable Quantum AI: Informing the Encoder Selection of Quantum Neural Networks via Visualization

**arXiv**: [2512.14181v1](https://arxiv.org/abs/2512.14181) | [PDF](https://arxiv.org/pdf/2512.14181.pdf)

**作者**: Shaolun Ruan, Feng Liang, Rohan Ramakrishna, Chao Ren, Rudai Yan, Qiang Guan, Jiannan Li, Yong Wang

**分类**: quant-ph, cs.AI, cs.HC

**发布日期**: 2025-12-16

**备注**: 9 pages, 6 figures, accepted by TVCG 2026, not published yet

---

## 💡 一句话要点

**XQAI-Eyes：通过可视化辅助量子神经网络编码器选择**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)**

**关键词**: `量子神经网络` `编码器选择` `可视化工具` `可解释性AI` `量子计算`

## 📋 核心要点

1. 现有量子神经网络编码器的选择缺乏系统指导，依赖试错，难以评估编码后的量子态，也缺乏直观分析编码器区分数据特征能力的方法。
2. 论文提出XQAI-Eyes可视化工具，通过比较经典数据特征与编码后的量子态，以及检查不同类别的混合量子态，桥接经典和量子视角。
3. 实验表明XQAI-Eyes能够支持探索编码器设计与QNN有效性之间的关系，并帮助领域专家推导出量子编码器选择的关键实践。

## 📝 摘要（中文）

量子神经网络(QNNs)是量子计算和神经网络架构的有前景的融合，它提供了高速和高效的高维纠缠数据处理能力。QNNs的一个关键组成部分是编码器，它将经典输入数据映射到量子态。然而，选择合适的编码器仍然是一个重大挑战，这主要是由于缺乏系统的指导和当前方法的试错性质。由于两个关键挑战，这个过程进一步受阻：(1)在训练之前难以评估编码的量子态，以及(2)缺乏直观的方法来分析编码器有效区分数据特征的能力。为了解决这些问题，我们引入了一种新的可视化工具XQAI-Eyes，它使QNN开发人员能够比较经典数据特征及其相应的编码量子态，并检查不同类别的混合量子态。通过桥接经典和量子视角，XQAI-Eyes有助于更深入地理解编码器如何影响QNN性能。跨不同数据集和编码器设计的评估表明，XQAI-Eyes具有支持探索编码器设计与QNN有效性之间关系的潜力，从而为优化量子编码器提供了一种整体和透明的方法。此外，领域专家使用XQAI-Eyes推导出了量子编码器选择的两个关键实践，这些实践基于模式保持和特征映射的原则。

## 🔬 方法详解

**问题定义**：量子神经网络(QNNs)中的编码器选择是一个关键问题。现有的方法主要依赖于试错，缺乏系统性的指导。此外，在训练之前难以评估编码后的量子态，也缺乏直观的方法来分析编码器区分数据特征的能力。这使得选择合适的编码器变得非常困难，阻碍了QNN的性能优化。

**核心思路**：论文的核心思路是开发一个可视化工具XQAI-Eyes，通过将经典数据特征与其对应的编码量子态进行比较，并检查不同类别的混合量子态，从而帮助研究人员理解编码器如何影响QNN的性能。通过桥接经典和量子视角，XQAI-Eyes旨在提供一种更直观和系统的方法来选择合适的编码器。

**技术框架**：XQAI-Eyes工具主要包含以下几个阶段：1)经典数据输入；2)通过不同的量子编码器将经典数据编码为量子态；3)可视化编码后的量子态，包括比较经典数据特征与编码后的量子态，以及检查不同类别的混合量子态；4)基于可视化结果，分析编码器的性能，并选择合适的编码器。

**关键创新**：该论文的关键创新在于提出了XQAI-Eyes可视化工具，它提供了一种直观的方式来理解量子编码器如何影响QNN的性能。与现有方法相比，XQAI-Eyes允许研究人员在训练之前评估编码器的性能，并提供了一种系统的方法来选择合适的编码器。

**关键设计**：XQAI-Eyes的关键设计包括：1)能够可视化经典数据特征和编码后的量子态；2)能够检查不同类别的混合量子态；3)提供交互式界面，允许用户探索不同的编码器和数据集；4)基于可视化结果，提供编码器选择的建议。

## 📊 实验亮点

论文通过在多个数据集和编码器设计上进行评估，验证了XQAI-Eyes的有效性。实验结果表明，XQAI-Eyes能够帮助研究人员更好地理解编码器设计与QNN有效性之间的关系，并推导出量子编码器选择的关键实践。领域专家使用XQAI-Eyes推导出了量子编码器选择的两个关键实践，这些实践基于模式保持和特征映射的原则。

## 🎯 应用场景

该研究成果可应用于各种需要量子神经网络进行数据处理和模式识别的领域，例如量子化学、材料科学、金融建模和图像识别。XQAI-Eyes工具能够帮助研究人员更有效地设计和优化量子神经网络，从而提高相关应用的性能和效率，加速量子计算在实际问题中的应用。

## 📄 摘要（原文）

> Quantum Neural Networks (QNNs) represent a promising fusion of quantum computing and neural network architectures, offering speed-ups and efficient processing of high-dimensional, entangled data. A crucial component of QNNs is the encoder, which maps classical input data into quantum states. However, choosing suitable encoders remains a significant challenge, largely due to the lack of systematic guidance and the trial-and-error nature of current approaches. This process is further impeded by two key challenges: (1) the difficulty in evaluating encoded quantum states prior to training, and (2) the lack of intuitive methods for analyzing an encoder's ability to effectively distinguish data features. To address these issues, we introduce a novel visualization tool, XQAI-Eyes, which enables QNN developers to compare classical data features with their corresponding encoded quantum states and to examine the mixed quantum states across different classes. By bridging classical and quantum perspectives, XQAI-Eyes facilitates a deeper understanding of how encoders influence QNN performance. Evaluations across diverse datasets and encoder designs demonstrate XQAI-Eyes's potential to support the exploration of the relationship between encoder design and QNN effectiveness, offering a holistic and transparent approach to optimizing quantum encoders. Moreover, domain experts used XQAI-Eyes to derive two key practices for quantum encoder selection, grounded in the principles of pattern preservation and feature mapping.

