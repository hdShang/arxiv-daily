---
layout: default
title: "ButterflyQuant: Ultra-low-bit LLM Quantization through Learnable Orthogonal Butterfly Transforms"
---

# ButterflyQuant: Ultra-low-bit LLM Quantization through Learnable Orthogonal Butterfly Transforms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09679" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09679v2</a>
  <a href="https://arxiv.org/pdf/2509.09679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09679v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09679v2', 'ButterflyQuant: Ultra-low-bit LLM Quantization through Learnable Orthogonal Butterfly Transforms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingxin Xu, Zhen Dong, Oussama Elachqar, Yuzhang Shang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-11 (更新: 2025-09-25)

**备注**: Replace discrete Hadamard transforms with continuous Butterfly transforms to facilitate the learning of rotation matrices in LLM quantization

**🔗 代码/项目**: [GITHUB](https://github.com/42Shawn/Butterflyquant-llm)

---

## 💡 一句话要点

**提出ButterflyQuant以解决大语言模型量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `深度学习` `蝴蝶变换` `异常值抑制` `模型优化` `Givens旋转` `资源受限设备`

## 📋 核心要点

1. 现有的量化方法在极端2位量化时，因激活值中的异常值导致性能严重下降，限制了大语言模型的应用。
2. ButterflyQuant通过可学习的蝴蝶变换替代固定的Hadamard变换，采用连续参数化以适应不同层的权重分布。
3. 在LLaMA-2-7B模型上进行2位量化时，ButterflyQuant的困惑度为15.4，显著优于基线方法QuIP的37.3。

## 📝 摘要（中文）

大型语言模型需要巨大的内存占用，这限制了其在消费硬件上的部署。量化通过降低数值精度来减少内存，但极端的2位量化会因激活值中的异常值而导致性能严重下降。现有的基于旋转的方法如QuIP和QuaRot使用固定的Hadamard变换来消除异常值，但无法适应特定的权重分布。本文提出ButterflyQuant，采用可学习的蝴蝶变换替代Hadamard旋转，利用连续的Givens旋转角度进行参数化，确保正交性并实现平滑优化。实验结果表明，ButterflyQuant在LLaMA-2-7B模型的2位量化中，困惑度为15.4，相较于QuIP的37.3有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在极端2位量化时因激活值异常值导致的性能下降问题。现有方法如QuIP和QuaRot使用固定的Hadamard变换，无法适应不同层的权重分布，造成性能损失。

**核心思路**：论文提出ButterflyQuant，通过可学习的蝴蝶变换替代Hadamard旋转，利用连续的Givens旋转角度进行参数化。这种设计允许模型在训练过程中自适应地调整变换，从而更有效地抑制异常值。

**技术框架**：ButterflyQuant的整体架构包括数据预处理、可学习的蝴蝶变换模块和量化模块。首先对输入数据进行预处理，然后通过蝴蝶变换模块进行激活值的变换，最后进行量化处理。

**关键创新**：最重要的技术创新在于引入了可学习的蝴蝶变换，替代了传统的固定Hadamard变换。这一创新使得变换能够根据不同层的特征进行自适应调整，显著提高了量化后的模型性能。

**关键设计**：在设计中，蝴蝶变换的参数通过连续的Givens旋转角度进行优化，确保了正交性。此外，论文还引入了均匀性正则化，以促进变换后激活值的平滑分布，便于后续的量化处理。

## 📊 实验亮点

在实验中，ButterflyQuant在LLaMA-2-7B模型的2位量化中，困惑度达到了15.4，相较于基线方法QuIP的37.3，表现出显著的性能提升。这一结果表明，ButterflyQuant在处理异常值方面具有优越性，能够有效提高量化模型的性能。

## 🎯 应用场景

ButterflyQuant的研究成果具有广泛的应用潜力，尤其是在资源受限的设备上部署大型语言模型时。通过有效的量化方法，能够在保持模型性能的同时，显著降低内存占用，为智能手机、边缘计算设备等提供更好的支持。未来，该方法还可以扩展到其他深度学习模型的量化和优化中。

## 📄 摘要（原文）

> Large language models require massive memory footprints, severely limiting deployment on consumer hardware. Quantization reduces memory through lower numerical precision, but extreme 2-bit quantization suffers from catastrophic performance loss due to outliers in activations. Rotation-based methods such as QuIP and QuaRot apply orthogonal transforms to eliminate outliers before quantization, using computational invariance: $\mathbf{y} = \mathbf{Wx} = (\mathbf{WQ}^T)(\mathbf{Qx})$ for orthogonal $\mathbf{Q}$. However, these methods use fixed transforms--Hadamard matrices achieving optimal worst-case coherence $μ= 1/\sqrt{n}$--that cannot adapt to specific weight distributions. We identify that different transformer layers exhibit distinct outlier patterns, motivating layer-adaptive rotations rather than one-size-fits-all approaches. In this work, we propose ButterflyQuant, which replaces Hadamard rotations with learnable butterfly transforms parameterized by continuous Givens rotation angles. Unlike Hadamard's discrete $\{+1, -1\}$ entries that are non-differentiable and thus prohibit gradient-based learning, butterfly transforms' continuous parameterization enables smooth optimization while guaranteeing orthogonality by construction. This orthogonal constraint ensures theoretical guarantees in outlier suppression while achieving $O(n \log n)$ computational complexity with only $\frac{n \log n}{2}$ learnable parameters. We further introduce a uniformity regularization on post-transformation activations to promote smoother distributions amenable to quantization. Learning requires only 128 calibration samples and converges in minutes on a single GPU--a negligible one-time cost. For LLaMA-2-7B with 2-bit quantization, ButterflyQuant achieves 15.4 perplexity versus 37.3 for QuIP. \href{https://github.com/42Shawn/Butterflyquant-llm}{Codes} are available.

