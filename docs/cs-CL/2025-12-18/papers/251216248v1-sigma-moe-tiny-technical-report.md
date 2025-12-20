---
layout: default
title: Sigma-Moe-Tiny Technical Report
---

# Sigma-Moe-Tiny Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16248" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16248v1</a>
  <a href="https://arxiv.org/pdf/2512.16248.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16248v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16248v1', 'Sigma-Moe-Tiny Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingguo Hu, Zhenghao Lin, Ziyue Yang, Yucheng Ding, Xiao Liu, Yuting Jiang, Ruizhe Wang, Tianyu Chen, Zhongxin Guo, Yifan Xiong, Rui Gao, Lei Qu, Jinsong Su, Peng Cheng, Yeyun Gong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/microsoft/ltp-megatron-lm) | [PROJECT_PAGE](https://qghuxmu.github.io/Sigma-MoE-Tiny)

---

## 💡 一句话要点

**Sigma-MoE-Tiny：提出一种高稀疏MoE语言模型，解决专家负载均衡难题，实现高效扩展。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `MoE` `稀疏模型` `负载均衡` `渐进式稀疏化` `语言模型` `深度学习`

## 📋 核心要点

1. 现有MoE模型在极端稀疏性下，专家负载均衡面临挑战，传统负载均衡损失在底层失效。
2. 提出渐进式稀疏化策略，旨在平衡专家利用率和训练稳定性，解决高稀疏性下的负载均衡问题。
3. Sigma-MoE-Tiny仅激活0.5B参数，但在同等或更大规模模型中表现出色，训练过程稳定。

## 📝 摘要（中文）

本文介绍了Sigma-MoE-Tiny，一种混合专家（MoE）语言模型，它实现了现有开源模型中最高的稀疏性。Sigma-MoE-Tiny采用细粒度的专家分割，每层最多96个专家，但每个token仅激活一个专家，从而在200亿总参数下仅激活0.5B参数。这种极端稀疏性带来的主要挑战是专家负载均衡。研究发现，在这种设置下，广泛使用的负载均衡损失在较低层中往往失效。为了解决这个问题，提出了一种渐进式稀疏化策略，旨在平衡专家利用率和训练稳定性。Sigma-MoE-Tiny在一个多样化和高质量的语料库上进行预训练，然后进行后训练以进一步释放其能力。整个训练过程保持了显著的稳定性，没有出现不可恢复的损失峰值。综合评估表明，尽管仅激活0.5B参数，Sigma-MoE-Tiny在同等或更大规模的同类模型中实现了顶级的性能。此外，还深入讨论了高稀疏MoE模型中的负载均衡问题，为未来MoE架构中提高稀疏性提供了见解。

## 🔬 方法详解

**问题定义**：论文旨在解决MoE模型中，在极高稀疏度下专家负载不均衡的问题。现有的负载均衡损失函数在高稀疏度下，尤其是在模型的底层，效果不佳，导致部分专家过度使用，而另一些专家利用率不足，影响模型整体性能。

**核心思路**：论文的核心思路是通过渐进式稀疏化策略来解决专家负载均衡问题。该策略并非一开始就采用最高的稀疏度，而是逐步增加稀疏度，从而在训练初期保证专家能够得到充分的训练和利用，避免一开始就出现严重的负载不均衡。

**技术框架**：Sigma-MoE-Tiny模型基于Transformer架构，并引入了MoE层。整体流程包括：首先，在高质量语料库上进行预训练，使用渐进式稀疏化策略进行专家选择和负载均衡；然后，进行后训练，进一步提升模型性能。模型包含多个MoE层，每个MoE层包含多个专家，每个token只路由到一个专家。

**关键创新**：关键创新在于提出的渐进式稀疏化策略。与传统的固定稀疏度MoE模型不同，Sigma-MoE-Tiny在训练过程中动态调整稀疏度，从而更好地平衡专家利用率和训练稳定性。这种方法能够有效避免因高稀疏度导致的早期训练不稳定和专家负载不均衡问题。

**关键设计**：渐进式稀疏化策略的具体实现包括：在训练初期，使用较低的稀疏度，允许更多的token路由到不同的专家，确保每个专家都能得到充分的训练。随着训练的进行，逐步增加稀疏度，最终达到目标稀疏度。论文中可能还涉及了对路由策略的优化，例如使用Top-K路由或可学习的路由函数，以及对负载均衡损失函数的改进，以更好地适应高稀疏度场景。具体的参数设置和损失函数细节需要在论文原文中查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16248v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16248v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16248v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Sigma-MoE-Tiny在仅激活0.5B参数的情况下，实现了与参数规模更大模型相当甚至更优越的性能。实验结果表明，该模型在多个NLP任务上取得了领先水平，证明了其在高稀疏度下的有效性。此外，训练过程的稳定性也表明了渐进式稀疏化策略的优越性。

## 🎯 应用场景

Sigma-MoE-Tiny的研究成果可应用于各种需要高效扩展的大规模语言模型场景，例如自然语言处理、机器翻译、文本生成等。其高稀疏性使得模型在资源受限的环境下也能运行，具有很高的实际应用价值。未来，该研究可以推动MoE模型在移动设备和边缘计算等领域的应用。

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) has emerged as a promising paradigm for foundation models due to its efficient and powerful scalability. In this work, we present Sigma-MoE-Tiny, an MoE language model that achieves the highest sparsity compared to existing open-source models. Sigma-MoE-Tiny employs fine-grained expert segmentation with up to 96 experts per layer, while activating only one expert for each token, resulting in 20B total parameters with just 0.5B activated. The major challenge introduced by such extreme sparsity lies in expert load balancing. We find that the widely-used load balancing loss tends to become ineffective in the lower layers under this setting. To address this issue, we propose a progressive sparsification schedule aiming to balance expert utilization and training stability. Sigma-MoE-Tiny is pre-trained on a diverse and high-quality corpus, followed by post-training to further unlock its capabilities. The entire training process remains remarkably stable, with no occurrence of irrecoverable loss spikes. Comprehensive evaluations reveal that, despite activating only 0.5B parameters, Sigma-MoE-Tiny achieves top-tier performance among counterparts of comparable or significantly larger scale. In addition, we provide an in-depth discussion of load balancing in highly sparse MoE models, offering insights for advancing sparsity in future MoE architectures.
>   Project page: https://qghuxmu.github.io/Sigma-MoE-Tiny
>   Code: https://github.com/microsoft/ltp-megatron-lm

