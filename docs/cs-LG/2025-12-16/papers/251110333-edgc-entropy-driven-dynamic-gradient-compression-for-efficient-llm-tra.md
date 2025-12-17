---
layout: default
title: EDGC: Entropy-driven Dynamic Gradient Compression for Efficient LLM Training
---

# EDGC: Entropy-driven Dynamic Gradient Compression for Efficient LLM Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10333" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10333</a>
  <a href="https://arxiv.org/pdf/2511.10333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10333" onclick="toggleFavorite(this, '2511.10333', 'EDGC: Entropy-driven Dynamic Gradient Compression for Efficient LLM Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingao Yi, Jiaang Duan, Hanwen Hu, Qin Hua, Haiyan Zhao, Shiyou Qian, Dingyu Yang, Jian Cao, Jinghua Tang, Yinghao Yu, Chenzhi Liao, Kangjin Wang, Liping Zhang

**分类**: cs.LG, cs.AI, cs.PF

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**EDGC：一种熵驱动的动态梯度压缩框架，用于高效的大语言模型训练。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `分布式训练` `梯度压缩` `动态压缩` `梯度熵` `通信优化` `模型训练加速`

## 📋 核心要点

1. 现有大语言模型训练方法依赖静态梯度压缩，忽略了训练过程中梯度动态变化的特性，导致性能下降。
2. EDGC框架通过梯度熵的演变趋势动态调整压缩率，兼顾压缩效率和模型误差，从而加速LLM训练。
3. 实验结果表明，EDGC在32-V100和64-H100集群上训练GPT2模型时，显著降低了通信延迟和训练时间，同时保持了模型精度。

## 📝 摘要（中文）

训练大型语言模型（LLMs）在计算资源和内存容量方面提出了重大挑战。虽然分布式训练技术有助于缓解这些问题，但它们仍然受到相当大的通信开销的影响。现有方法主要依靠静态梯度压缩来提高通信效率；然而，这些方法忽略了训练期间梯度演变的动态特性，导致性能下降。在不牺牲性能的情况下，通过压缩加速LLM训练仍然是一个挑战。本文提出了一种名为EDGC的熵驱动的动态梯度压缩框架。其核心概念是根据梯度熵的演变趋势调整LLM训练期间的压缩率，同时考虑压缩效率和误差。EDGC由三个关键部分组成：首先，它采用一种降采样方法来有效地估计梯度熵，从而降低计算开销。其次，它建立了一个将压缩率与梯度熵联系起来的理论模型，从而能够做出更明智的压缩决策。最后，一种基于窗口的调整机制动态地调整跨pipeline阶段的压缩率，从而提高通信效率并保持模型性能。我们在一个32-NVIDIA-V100集群和一个64-NVIDIA-H100集群上分别实现了EDGC来训练GPT2-2.5B和GPT2-12.1B。结果表明，EDGC在保持LLM精度的同时，显著降低了通信延迟和训练时间，分别高达46.45%和16.13%。

## 🔬 方法详解

**问题定义**：现有分布式训练方法在训练大型语言模型时面临巨大的通信开销。静态梯度压缩方法虽然能降低通信量，但忽略了训练过程中梯度分布的动态变化，导致压缩效率不高，甚至影响模型收敛和精度。因此，如何在保证模型性能的前提下，更有效地压缩梯度，降低通信开销，是本文要解决的问题。

**核心思路**：本文的核心思路是根据梯度熵的变化动态调整压缩率。梯度熵可以反映梯度分布的复杂程度，熵越高，梯度分布越分散，需要保留的信息越多，压缩率应该降低；反之，熵越低，梯度分布越集中，可以采用更高的压缩率。通过建立压缩率与梯度熵之间的理论模型，可以实现更智能的梯度压缩。

**技术框架**：EDGC框架主要包含三个模块：1) 梯度熵估计模块：采用降采样方法高效估计梯度熵，降低计算开销。2) 压缩率决策模块：建立压缩率与梯度熵之间的理论模型，根据梯度熵动态调整压缩率。3) 窗口调整模块：采用基于窗口的调整机制，在不同的pipeline stage动态调整压缩率，进一步提高通信效率。整体流程是，首先计算梯度熵，然后根据梯度熵和理论模型确定压缩率，最后利用窗口调整机制平滑压缩率的变化。

**关键创新**：EDGC的关键创新在于动态梯度压缩策略。与静态梯度压缩方法不同，EDGC能够根据梯度熵的演变趋势自适应地调整压缩率，从而在保证模型性能的同时，最大限度地降低通信开销。此外，EDGC提出的梯度熵估计方法和压缩率决策模型也具有一定的创新性。

**关键设计**：梯度熵估计模块采用降采样方法，通过采样一部分梯度来估计整体的梯度熵，降低计算复杂度。压缩率决策模块基于信息论原理，建立压缩率与梯度熵之间的理论模型，具体形式未知。窗口调整模块采用滑动窗口平均的方法，平滑压缩率的变化，避免压缩率突变对模型训练造成影响。具体窗口大小和滑动步长未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10333/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10333/figure/gpt_entropy.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10333/figure/bert_entropy.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EDGC在32-NVIDIA-V100集群上训练GPT2-2.5B模型，以及在64-NVIDIA-H100集群上训练GPT2-12.1B模型。实验结果表明，EDGC能够显著降低通信延迟和训练时间，分别高达46.45%和16.13%，同时保持了LLM的精度。这些结果验证了EDGC框架的有效性。

## 🎯 应用场景

EDGC框架可应用于各种需要分布式训练的大型语言模型，尤其是在通信带宽受限的场景下。通过降低通信开销，EDGC可以加速模型训练，降低训练成本，并支持更大规模的模型训练。该研究成果对于推动大语言模型在资源受限环境下的应用具有重要意义。

## 📄 摘要（原文）

> Training large language models (LLMs) poses significant challenges regarding computational resources and memory capacity. Although distributed training techniques help mitigate these issues, they still suffer from considerable communication overhead. Existing approaches primarily rely on static gradient compression to enhance communication efficiency; however, these methods neglect the dynamic nature of evolving gradients during training, leading to performance degradation. Accelerating LLM training via compression without sacrificing performance remains a challenge. In this paper, we propose an entropy-driven dynamic gradient compression framework called EDGC. The core concept is to adjust the compression rate during LLM training based on the evolving trends of gradient entropy, taking into account both compression efficiency and error. EDGC consists of three keythis http URL, it employs a down-sampling method to efficiently estimate gradient entropy, reducing computation overhead. Second, it establishes a theoretical model linking compression rate with gradient entropy, enabling more informed compression decisions. Lastly, a window-based adjustment mechanism dynamically adapts the compression rate across pipeline stages, improving communication efficiency and maintaining model performance. We implemented EDGC on a 32-NVIDIA-V100 cluster and a 64-NVIDIA-H100 cluster to train GPT2-2.5B and GPT2-12.1B, respectively. The results show that EDGC significantly reduces communication latency and training time by up to 46.45% and 16.13% while preserving LLM accuracy.

