---
layout: default
title: MIDUS: Memory-Infused Depth Up-Scaling
---

# MIDUS: Memory-Infused Depth Up-Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13751" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13751</a>
  <a href="https://arxiv.org/pdf/2512.13751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13751" onclick="toggleFavorite(this, '2512.13751', 'MIDUS: Memory-Infused Depth Up-Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taero Kim, Hoyoon Byun, Youngjun Choi, Sungrae Park, Kyungwoo Song

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**MIDUS：通过注入记忆的深度扩展方法，提升大语言模型效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度扩展` `大型语言模型` `注意力机制` `记忆网络` `持续预训练`

## 📋 核心要点

1. 现有深度扩展方法依赖前馈网络，效率受限，难以在扩展模型容量的同时控制参数增长和推理成本。
2. MIDUS用头注意力记忆层替换前馈网络，为每个注意力头分配独立记忆库，实现头注意力检索和信息注入。
3. 实验表明，MIDUS在持续预训练中表现出优于现有深度扩展基线的性能，同时保持高效的参数利用率。

## 📝 摘要（中文）

扩展大型语言模型(LLMs)需要增加模型容量，同时避免参数过度增长或推理成本过高。深度扩展(DUS)通过复制层并应用持续预训练(CPT)成为一种有前景的策略，但其对前馈网络(FFN)的依赖限制了效率和可获得的收益。我们引入了记忆注入深度扩展(MIDUS)，它用头注意力记忆(HML)层替换复制块中的FFN。基于注意力头在层间和层内具有不同作用的观察，MIDUS为每个头分配一个独立的记忆库，从而实现头注意力检索并将信息注入到后续层，同时保持头注意力功能结构。这种设计将稀疏记忆访问与头注意力表示相结合，并结合了高效的每头注意力值分解模块，从而缓解了通常的效率-性能权衡。在我们的CPT实验中，MIDUS相对于强大的DUS基线表现出强大的性能改进，同时保持了高效的参数占用。我们的研究结果表明，通过利用其头注意力记忆设计，MIDUS是一种引人注目的、资源高效的深度扩展替代传统FFN复制的方法。

## 🔬 方法详解

**问题定义**：现有的大语言模型深度扩展方法，如DUS，过度依赖前馈神经网络（FFN），导致模型扩展时参数量迅速增加，推理效率降低。如何在不显著增加参数量和推理成本的前提下，有效扩展模型深度，提升模型性能，是本文要解决的核心问题。

**核心思路**：MIDUS的核心思路是用头注意力记忆（Head-wise Memory，HML）层替换复制块中的FFN。作者观察到不同的注意力头在模型中扮演着不同的角色，因此为每个头分配独立的记忆库，允许模型根据每个头的特定需求检索和注入信息。这种方法旨在利用注意力机制的优势，在保持模型性能的同时，减少参数冗余。

**技术框架**：MIDUS的整体架构基于深度扩展（DUS）框架，主要包含以下几个阶段：1) 复制模型层：复制原始模型的若干层，形成扩展的深度；2) 替换FFN：将复制层中的前馈神经网络（FFN）替换为头注意力记忆（HML）层；3) 持续预训练（CPT）：在扩展后的模型上进行持续预训练，使模型适应新的深度和结构。HML层是关键模块，负责存储和检索与每个注意力头相关的信息。

**关键创新**：MIDUS的关键创新在于头注意力记忆（HML）层的设计。与传统的共享记忆方法不同，HML为每个注意力头分配独立的记忆库，允许模型根据每个头的特定需求进行信息检索和注入。此外，MIDUS还引入了每头注意力值分解模块，进一步提高了模型的效率。这种头注意力级别的记忆管理方式，能够更精细地控制信息的流动和利用，从而在保持模型性能的同时，降低参数量和计算复杂度。

**关键设计**：HML层的关键设计包括：1) 独立的记忆库：每个注意力头对应一个独立的记忆库，存储与该头相关的信息；2) 注意力检索机制：使用注意力机制从记忆库中检索信息，检索权重由当前层的注意力头计算得到；3) 信息注入机制：将检索到的信息注入到后续层，影响后续层的计算；4) 每头注意力值分解：对每个注意力头的值向量进行分解，减少参数量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13751/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13751/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13751/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MIDUS在持续预训练任务中，相较于DUS基线，在参数量相近的情况下，取得了显著的性能提升。具体数据（原文未提供，未知）。MIDUS通过头注意力记忆的设计，实现了高效的深度扩展，为大语言模型的优化提供了一种新的思路。

## 🎯 应用场景

MIDUS具有广泛的应用前景，可用于提升各种大型语言模型的性能，尤其是在资源受限的环境下。例如，可以应用于移动设备上的轻量级模型部署，或在计算资源有限的服务器上进行高效推理。此外，MIDUS的设计思想也可以推广到其他类型的深度学习模型中，例如视觉Transformer等。

## 📄 摘要（原文）

> Scaling large language models (LLMs) demands approaches that increase capacity without incurring excessive parameter growth or inference cost. Depth Up-Scaling (DUS) has emerged as a promising strategy by duplicating layers and applying Continual Pre-training (CPT), but its reliance on feed-forward networks (FFNs) limits efficiency and attainable gains. We introduce Memory-Infused Depth Up-Scaling (MIDUS), which replaces FFNs in duplicated blocks with a head-wise memory (HML) layer. Motivated by observations that attention heads have distinct roles both across and within layers, MIDUS assigns an independent memory bank to each head, enabling head-wise retrieval and injecting information into subsequent layers while preserving head-wise functional structure. This design combines sparse memory access with head-wise representations and incorporates an efficient per-head value factorization module, thereby relaxing the usual efficiency-performance trade-off. Across our CPT experiments, MIDUS exhibits robust performance improvements over strong DUS baselines while maintaining a highly efficient parameter footprint. Our findings establish MIDUS as a compelling and resource-efficient alternative to conventional FFN replication for depth up-scaling by leveraging its head-wise memory design.

