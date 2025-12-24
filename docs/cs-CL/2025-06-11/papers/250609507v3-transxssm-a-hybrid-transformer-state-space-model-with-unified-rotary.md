---
layout: default
title: "TransXSSM: A Hybrid Transformer State Space Model with Unified Rotary Position Embedding"
---

# TransXSSM: A Hybrid Transformer State Space Model with Unified Rotary Position Embedding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09507" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09507v3</a>
  <a href="https://arxiv.org/pdf/2506.09507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09507v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09507v3', 'TransXSSM: A Hybrid Transformer State Space Model with Unified Rotary Position Embedding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingheng Wu, Jingze Shi, Yifan Wu, Nan Tang, Yuyu Luo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-06-18)

---

## 💡 一句话要点

**提出TransXSSM以解决Transformer与状态空间模型的编码不兼容问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长序列建模` `位置编码` `Transformer` `状态空间模型` `混合架构` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的Transformer和状态空间模型在位置编码机制上存在根本不一致，导致整合时性能不佳。
2. 本文提出统一的旋转位置嵌入（Unified RoPE），为Transformer和SSM提供一致的位置编码框架。
3. TransXSSM在训练和推理速度上分别比标准Transformer快42.3%和29.5%，并在准确性上有显著提升。

## 📝 摘要（中文）

Transformers在捕捉长距离依赖方面表现出色，而状态空间模型（SSMs）则支持线性时间序列建模。尽管这两种架构具有协同潜力，但由于其位置编码机制的根本不一致，二者的整合面临重大挑战。Transformers依赖显式的旋转位置嵌入（RoPE），而SSMs则通过卷积利用隐式位置表示。为了解决这一问题，本文提出了一种统一的旋转位置嵌入（Unified RoPE）方法，从而为自注意力和状态空间组件建立了一致的位置编码框架。基于Unified RoPE，本文引入了TransXSSM，一种在统一位置编码方案下有效整合Transformer和SSM层的混合架构。实验表明，TransXSSM在训练和推理速度上分别比标准Transformer模型快42.3%和29.5%，并在语言建模基准上超越Transformer基线超过4%。

## 🔬 方法详解

**问题定义**：本文旨在解决Transformer与状态空间模型在位置编码上的不兼容问题，现有方法在整合时常导致性能下降和不连续性。

**核心思路**：提出统一的旋转位置嵌入（Unified RoPE），使得自注意力和状态空间组件能够共享一致的位置编码，从而提高模型的整体性能。

**技术框架**：TransXSSM架构包括Transformer层和状态空间层，二者通过Unified RoPE进行连接，形成一个统一的编码框架，支持高效的长序列建模。

**关键创新**：Unified RoPE是本文的核心创新，它解决了传统Transformer和SSM在位置编码上的不一致性，使得混合模型能够更有效地捕捉长距离依赖。

**关键设计**：在模型设计中，TransXSSM的参数设置经过优化，损失函数采用标准的交叉熵损失，网络结构结合了Transformer的自注意力机制和SSM的状态空间表示，确保了高效的训练和推理。

## 📊 实验亮点

TransXSSM在训练速度上比标准Transformer快42.3%，推理速度快29.5%。在语言建模基准测试中，其准确性超越Transformer基线超过4%，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、时间序列预测和其他需要长序列建模的任务。通过提高模型的训练和推理速度，TransXSSM能够在实际应用中提供更高效的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Transformers exhibit proficiency in capturing long-range dependencies, whereas State Space Models (SSMs) facilitate linear-time sequence modeling. Notwithstanding their synergistic potential, the integration of these architectures presents a significant challenge, primarily attributable to a fundamental incongr inuity their respective positional encoding mechanisms: Transformers rely on explicit Rotary Position Embeddings (RoPE), while SSMs leverage implicit positional representations via convolutions. This divergence often precipitates discontinuities and suboptimal performance.To address this impediment, we propose a unified rotary position embedding (Unified RoPE) methodology, thereby establishing a consistent positional encoding framework for both self-attention and state-space components. Using this Unified RoPE, we introduce TransXSSM, a hybrid architecture that coherently integrates the Transformer and SSM layers under this unified positional encoding scheme. At a 4 sequenceK length, TransXSSM exhibits training and inference speeds that are 42.3% and 29.5% faster, respectively, relative to standard Transformer models. It also delivers higher accuracy: under comparable settings, it surpasses a Transformer baseline by over 4% on language modeling benchmarks.TransXSSM furthermore scales more effectively: TransXSSM-1.3B gains 7.22% in average accuracy over its 320M version (versus about 6% gains for equivalent Transformers or SSMs). Our results show that unified positional encoding resolves positional incompatibility in hybrid models, enabling efficient, high-performance long-context modeling.

