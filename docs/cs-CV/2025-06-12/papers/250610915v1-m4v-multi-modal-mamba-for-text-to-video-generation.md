---
layout: default
title: "M4V: Multi-Modal Mamba for Text-to-Video Generation"
---

# M4V: Multi-Modal Mamba for Text-to-Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10915" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10915v1</a>
  <a href="https://arxiv.org/pdf/2506.10915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10915v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10915v1', 'M4V: Multi-Modal Mamba for Text-to-Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiancheng Huang, Gengwei Zhang, Zequn Jie, Siyu Jiao, Yinlong Qian, Ling Chen, Yunchao Wei, Lin Ma

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-06-12

**🔗 代码/项目**: [PROJECT_PAGE](https://huangjch526.github.io/M4V_project)

---

## 💡 一句话要点

**提出M4V框架以解决文本到视频生成中的计算复杂性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `文本到视频生成` `多模态融合` `时空建模` `计算复杂性` `奖励学习` `Mamba架构` `视频生成`

## 📋 核心要点

1. 现有文本到视频生成方法在处理时空建模时计算复杂度高，尤其是使用Transformer时，限制了其实际应用。
2. 本文提出M4V框架，利用多模态扩散Mamba模块实现多模态信息与时空建模的高效集成，降低计算成本。
3. 实验结果表明，M4V在生成高质量视频的同时，FLOPs减少了45%，并通过奖励学习策略提升了视觉质量。

## 📝 摘要（中文）

文本到视频生成显著丰富了内容创作，并有潜力演变为强大的世界模拟器。然而，建模广泛的时空空间在计算上仍然具有挑战性，尤其是使用Transformer时，其序列处理的平方复杂度限制了实际应用。为了解决这些问题，本文提出了M4V，一个用于文本到视频生成的多模态Mamba框架。我们提出的多模态扩散Mamba（MM-DiM）模块通过多模态令牌重组设计，实现了多模态信息与时空建模的无缝集成。实验表明，M4V在生成768×1280分辨率视频时，相较于基于注意力的方法，FLOPs减少了45%。此外，我们引入了一种奖励学习策略，以提高长上下文自回归生成过程中的每帧视觉真实感。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到视频生成中的计算复杂性问题，现有方法在处理时空建模时面临高计算成本，尤其是使用Transformer时的平方复杂度。

**核心思路**：提出M4V框架，核心在于多模态扩散Mamba（MM-DiM）模块，通过多模态令牌重组设计，实现高效的多模态信息集成与时空建模。

**技术框架**：M4V框架包含多个Mamba模块，利用MM-DiM模块进行多模态信息处理，整体流程包括文本输入、信息重组、视频生成等阶段。

**关键创新**：M4V的主要创新在于引入MM-DiM模块，显著降低了生成视频时的计算复杂度，与传统基于注意力的方法相比，FLOPs减少了45%。

**关键设计**：在设计中，采用了多模态令牌重组策略，并引入奖励学习策略以提升生成视频的视觉质量，确保每帧的真实感。

## 📊 实验亮点

实验结果显示，M4V在生成768×1280分辨率视频时，相较于传统基于注意力的方法，FLOPs减少了45%。此外，通过引入奖励学习策略，显著提升了生成视频的每帧视觉质量，展示了该方法在文本到视频生成中的有效性与优势。

## 🎯 应用场景

该研究的潜在应用领域包括影视制作、游戏开发和虚拟现实等，能够为内容创作者提供高效的工具，降低视频生成的计算成本，提升创作效率。未来，M4V框架可能推动更广泛的多模态生成技术的发展，促进人机交互的自然性与智能化。

## 📄 摘要（原文）

> Text-to-video generation has significantly enriched content creation and holds the potential to evolve into powerful world simulators. However, modeling the vast spatiotemporal space remains computationally demanding, particularly when employing Transformers, which incur quadratic complexity in sequence processing and thus limit practical applications. Recent advancements in linear-time sequence modeling, particularly the Mamba architecture, offer a more efficient alternative. Nevertheless, its plain design limits its direct applicability to multi-modal and spatiotemporal video generation tasks. To address these challenges, we introduce M4V, a Multi-Modal Mamba framework for text-to-video generation. Specifically, we propose a multi-modal diffusion Mamba (MM-DiM) block that enables seamless integration of multi-modal information and spatiotemporal modeling through a multi-modal token re-composition design. As a result, the Mamba blocks in M4V reduce FLOPs by 45% compared to the attention-based alternative when generating videos at 768$\times$1280 resolution. Additionally, to mitigate the visual quality degradation in long-context autoregressive generation processes, we introduce a reward learning strategy that further enhances per-frame visual realism. Extensive experiments on text-to-video benchmarks demonstrate M4V's ability to produce high-quality videos while significantly lowering computational costs. Code and models will be publicly available at https://huangjch526.github.io/M4V_project.

