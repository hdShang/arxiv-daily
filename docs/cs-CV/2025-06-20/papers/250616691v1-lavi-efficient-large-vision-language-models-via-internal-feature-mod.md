---
layout: default
title: "LaVi: Efficient Large Vision-Language Models via Internal Feature Modulation"
---

# LaVi: Efficient Large Vision-Language Models via Internal Feature Modulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16691" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16691v1</a>
  <a href="https://arxiv.org/pdf/2506.16691.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16691v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16691v1', 'LaVi: Efficient Large Vision-Language Models via Internal Feature Modulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tongtian Yue, Longteng Guo, Yepeng Tang, Zijia Zhao, Xinxin Zhu, Hua Huang, Jing Liu

**分类**: cs.CV

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出LaVi以解决视觉语言模型效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型视觉语言模型` `多模态融合` `特征调制` `计算效率` `实时推理` `视觉语言对齐` `深度学习`

## 📋 核心要点

1. 现有大型视觉语言模型在视觉语言集成方面效率低下，限制了其可扩展性和应用。
2. LaVi通过内部特征调制实现视觉语言融合，避免了长上下文计算负担，提升了效率。
3. LaVi在多个基准测试中表现优异，相比LLaVA-OV-7B，FLOPs减少94.0%，推理速度提升3.1倍，内存使用减半。

## 📝 摘要（中文）

尽管大型视觉语言模型（LVLMs）取得了显著进展，但现有方法在视觉语言集成方面存在根本瓶颈：效率低下。当前方法要么破坏模型的固有结构，要么引入严重的长上下文计算负担，限制了可扩展性和效率。本文重新思考多模态集成，提出LaVi，一种新型LVLM，通过在大型语言模型（LLMs）内部特征调制实现无缝高效的视觉语言融合。与依赖视觉标记连接的主流LVLM不同，LaVi通过引入轻量级自适应变换，避免了长上下文扩展，确保视觉输入与语言隐藏状态的精确对齐，同时显著降低计算成本。广泛评估显示，LaVi在15个图像和视频基准上不仅实现了最先进的多模态性能，还大幅提升了效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型视觉语言模型在视觉语言集成中效率低下的问题。现有方法往往破坏模型结构或引入长上下文计算负担，限制了其可扩展性和效率。

**核心思路**：LaVi的核心思路是通过内部特征调制实现视觉语言的高效融合。该方法通过注入视觉条件的增量到层归一化的仿射参数中，直接调制语言隐藏状态，从而确保视觉与语言的精确对齐，同时保留语言模型的语言先验。

**技术框架**：LaVi的整体架构包括输入视觉信息和语言信息，通过轻量级自适应变换模块进行特征调制，最终输出融合后的多模态表示。该框架有效避免了长上下文扩展的问题。

**关键创新**：LaVi的主要创新在于其内部特征调制机制，与传统方法依赖视觉标记连接的方式本质不同。该机制通过视觉输入直接调制语言隐藏状态，显著提高了效率。

**关键设计**：LaVi采用轻量级的变换模块，具体设计包括视觉条件增量的注入方式和层归一化的仿射参数调整，确保了模型在保持性能的同时大幅降低计算成本。

## 📊 实验亮点

LaVi在15个图像和视频基准测试中表现优异，相比于LLaVA-OV-7B，FLOPs减少了94.0%，推理速度提升了3.1倍，内存使用减半。这些结果表明LaVi在多模态性能和效率上均达到了新的高度。

## 🎯 应用场景

LaVi的研究成果在多个领域具有广泛的应用潜力，包括实时多模态推理、图像与文本的交互理解、以及视频内容分析等。其高效的特征调制机制使得在资源受限的环境中也能实现高性能的视觉语言任务，推动了智能助手、自动驾驶等技术的发展。

## 📄 摘要（原文）

> Despite the impressive advancements of Large Vision-Language Models (LVLMs), existing approaches suffer from a fundamental bottleneck: inefficient visual-language integration. Current methods either disrupt the model's inherent structure or introduce severe long-context computational burden, severely limiting scalability and efficiency. In this paper, we rethink multimodal integration and present LaVi, a novel LVLM that enables seamless and efficient vision-language fusion through internal feature modulation within the Large Language Models (LLMs). Unlike dominant LVLMs that rely on visual token concatenation, LaVi bypasses long-context expansion by introducing a lightweight and adaptive transformation, which incorporates visual context by injecting token-wise vision-conditioned deltas into the affine parameters of layer normalization. This mechanism directly modulates linguistic hidden states based on visual input, ensuring precise vision-language alignment while preserving the LLM's linguistic priors and drastically reducing computational costs. Extensive evaluations across 15 image and video benchmarks demonstrate that LaVi not only achieves state-of-the-art multimodal performance but also dramatically enhances efficiency. Compared to LLaVA-OV-7B, LaVi reduces FLOPs by 94.0%, improves inference speed by 3.1 times, and cuts memory usage in half - establishing LaVi as a scalable and practical solution for real-time multimodal reasoning. The code and models will be released soon.

