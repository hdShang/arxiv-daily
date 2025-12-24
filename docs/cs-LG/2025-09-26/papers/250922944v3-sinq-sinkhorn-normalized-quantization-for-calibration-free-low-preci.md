---
layout: default
title: "SINQ: Sinkhorn-Normalized Quantization for Calibration-Free Low-Precision LLM Weights"
---

# SINQ: Sinkhorn-Normalized Quantization for Calibration-Free Low-Precision LLM Weights

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22944" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22944v3</a>
  <a href="https://arxiv.org/pdf/2509.22944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22944v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22944v3', 'SINQ: Sinkhorn-Normalized Quantization for Calibration-Free Low-Precision LLM Weights')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lorenz K. Müller, Philippe Bich, Jiawei Zhuang, Ahmet Çelik, Luca Benfenati, Lukas Cavigelli

**分类**: cs.LG

**发布日期**: 2025-09-26 (更新: 2025-10-09)

**🔗 代码/项目**: [GITHUB](https://github.com/huawei-csl/SINQ)

---

## 💡 一句话要点

**SINQ：用于免校准低精度LLM权重 Sinkhorn 归一化量化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低精度量化` `大型语言模型` `后训练量化` `Sinkhorn归一化` `矩阵平衡` `免校准量化` `模型压缩` `深度学习`

## 📋 核心要点

1. 现有低精度量化方法在4比特及以下位宽时，由于异常值影响，导致困惑度下降。
2. SINQ通过Sinkhorn归一化，寻找每行每列的缩放因子，最小化矩阵不平衡，提升量化精度。
3. 在Qwen3和DeepSeek-V2.5上的实验表明，SINQ显著优于未校准的均匀量化基线。

## 📝 摘要（中文）

后训练量化已成为以低精度部署大型语言模型的最广泛使用的策略。然而，当前的方法在小于等于4比特的位宽下表现出困惑度下降，部分原因是表示异常值导致与这些异常值共享相同尺度的参数出现精度问题。对于免校准的均匀量化方法，这个问题尤其突出。我们引入SINQ，通过额外的第二轴比例因子和快速Sinkhorn-Knopp风格的算法来增强现有的后训练量化器，该算法寻找比例来归一化每行和每列的方差，从而最小化量化的每个矩阵代理目标：矩阵不平衡。我们的方法在层之间没有交互，可以很容易地应用于新的架构来量化任何线性层。我们在Qwen3模型系列和DeepSeek-V2.5上评估了我们的方法。SINQ显著提高了WikiText2和C4的困惑度，优于未校准的均匀量化基线，并且可以通过将其与校准和非均匀量化级别相结合来进一步增强。重现这项工作结果并使用SINQ轻松量化模型的代码可在https://github.com/huawei-csl/SINQ获得。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在低精度量化时，尤其是使用免校准的均匀量化方法时，由于权重矩阵中异常值的存在而导致的性能下降问题。现有方法无法有效处理这些异常值，导致共享相同缩放因子的参数精度降低，最终影响模型的困惑度。

**核心思路**：论文的核心思路是通过引入Sinkhorn归一化，对权重矩阵的行和列分别进行缩放，从而平衡矩阵的元素分布，减少异常值的影响。这种方法旨在最小化一个新定义的“矩阵不平衡”指标，该指标作为量化的代理目标。通过平衡矩阵，可以提高量化后的权重精度，从而提升模型的整体性能。

**技术框架**：SINQ方法可以被视为现有后训练量化器的增强模块。它主要包含以下几个步骤：1. 对权重矩阵进行预处理，计算每行和每列的方差。2. 使用Sinkhorn-Knopp算法，迭代地寻找行和列的缩放因子，以归一化方差。3. 将缩放后的权重矩阵进行量化。4. 在推理时，将量化后的权重反量化，并应用相应的缩放因子。该方法不依赖于特定层，可以应用于任何线性层。

**关键创新**：SINQ的关键创新在于：1. 提出了“矩阵不平衡”的概念，并将其作为量化的代理目标。2. 利用Sinkhorn-Knopp算法，高效地寻找行和列的缩放因子，实现矩阵的归一化。3. 该方法是免校准的，不需要额外的校准数据，降低了量化的复杂度。与现有方法的本质区别在于，SINQ关注于平衡权重矩阵的元素分布，而不是简单地对权重进行量化。

**关键设计**：SINQ的关键设计包括：1. Sinkhorn-Knopp算法的迭代次数：需要根据实际情况进行调整，以达到最佳的归一化效果。2. 矩阵不平衡的定义：论文中使用了特定的矩阵不平衡度量，其他度量方式也可能适用。3. 与现有量化器的集成方式：SINQ可以作为现有量化器的预处理步骤，也可以与校准和非均匀量化方法结合使用。

## 📊 实验亮点

实验结果表明，SINQ在Qwen3模型系列和DeepSeek-V2.5上显著提高了WikiText2和C4数据集的困惑度，优于未校准的均匀量化基线。具体而言，SINQ在保持或降低模型大小的同时，有效提升了模型的性能。此外，SINQ还可以与校准和非均匀量化方法相结合，进一步提高量化效果。

## 🎯 应用场景

SINQ方法可广泛应用于大型语言模型的低精度部署，尤其是在资源受限的边缘设备上。通过降低模型的大小和计算复杂度，SINQ能够使LLM在移动设备、嵌入式系统等平台上高效运行。此外，该方法还可以应用于其他类型的神经网络，以提高其在低精度下的性能。未来，SINQ有望成为LLM量化的标准方法之一，推动AI技术在各个领域的普及。

## 📄 摘要（原文）

> Post-training quantization has emerged as the most widely used strategy for deploying large language models at low precision. Still, current methods show perplexity degradation at bit-widths less than or equal to 4, partly because representing outliers causes precision issues in parameters that share the same scales as these outliers. This problem is especially pronounced for calibration-free, uniform quantization methods. We introduce SINQ to augment existing post-training quantizers with an additional second-axis scale factor and a fast Sinkhorn-Knopp-style algorithm that finds scales to normalize per-row and per-column variances, thereby minimizing a novel per-matrix proxy target for quantization: the matrix imbalance. Our method has no interactions between layers and can be trivially applied to new architectures to quantize any linear layers. We evaluate our method on the Qwen3 model family and DeepSeek-V2.5. SINQ improves WikiText2 and C4 perplexity significantly against uncalibrated uniform quantization baselines and can be further enhanced by combining it with calibration and non-uniform quantization levels. Code to reproduce the results of this work and to easily quantize models using SINQ is available at https://github.com/huawei-csl/SINQ.

