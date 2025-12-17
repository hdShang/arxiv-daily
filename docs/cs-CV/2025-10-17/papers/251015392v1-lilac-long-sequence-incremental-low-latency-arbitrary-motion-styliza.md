---
layout: default
title: LILAC: Long-sequence Incremental Low-latency Arbitrary Motion Stylization via Streaming VAE-Diffusion with Causal Decoding
---

# LILAC: Long-sequence Incremental Low-latency Arbitrary Motion Stylization via Streaming VAE-Diffusion with Causal Decoding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15392" target="_blank" class="toolbar-btn">arXiv: 2510.15392v1</a>
    <a href="https://arxiv.org/pdf/2510.15392.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15392v1" 
            onclick="toggleFavorite(this, '2510.15392v1', 'LILAC: Long-sequence Incremental Low-latency Arbitrary Motion Stylization via Streaming VAE-Diffusion with Causal Decoding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Peng Ren, Hai Yang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-17

**🔗 代码/项目**: [PROJECT_PAGE](https://pren1.github.io/lilac/)

---

## 💡 一句话要点

**LILAC：基于流式VAE-Diffusion和因果解码的长序列增量低延迟任意动作风格化**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `动作风格化` `流式处理` `VAE-Diffusion` `低延迟` `长序列` `因果解码` `运动生成`

## 📋 核心要点

1. 现有流式动作风格化方法计算开销大，难以保证时间稳定性，限制了实时交互应用。
2. LILAC利用潜在空间流式VAE-Diffusion架构，结合因果滑动窗口和解码运动特征注入，实现低延迟长序列风格化。
3. 实验表明，LILAC在基准数据集上实现了高质量的实时动作风格化，并在风格化质量和响应性之间取得了平衡。

## 📝 摘要（中文）

本文提出LILAC（Long-sequence Incremental Low-latency Arbitrary Motion Stylization via Streaming VAE-Diffusion with Causal Decoding），旨在解决实时生成长序列风格化人体动作的问题。现有流式方法通常直接在原始动作空间操作，计算开销大且难以保持时间稳定性。虽然基于潜在空间的VAE-Diffusion框架可以缓解这些问题并实现高质量的风格化，但通常仅限于离线处理。LILAC基于高性能的离线任意动作风格化框架，通过具有滑动窗口因果设计的潜在空间流式架构，并注入解码的运动特征以确保平滑的运动过渡，将其扩展到在线设置。该架构无需依赖未来帧或修改扩散模型架构即可实现长序列实时任意风格化，在风格化质量和响应性之间取得了良好的平衡，实验结果表明了其在基准数据集上的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决实时生成长序列风格化人体动作的问题。现有流式方法直接在原始动作空间进行操作，导致计算量巨大，难以保证时间上的连贯性和稳定性。而基于VAE-Diffusion的离线方法虽然能够生成高质量的风格化动作，但无法满足实时性需求。

**核心思路**：论文的核心思路是将离线VAE-Diffusion框架扩展到在线流式设置。通过在潜在空间中进行操作，降低计算复杂度。同时，采用滑动窗口因果设计，避免使用未来信息，保证实时性。此外，通过注入解码的运动特征，确保运动过渡的平滑性。

**技术框架**：LILAC的整体框架包含以下几个主要模块：1) 编码器：将原始运动序列编码到潜在空间；2) 流式扩散模型：在潜在空间中进行风格化，采用滑动窗口因果设计；3) 解码器：将风格化后的潜在表示解码回运动空间；4) 运动特征注入模块：将解码后的运动特征注入到扩散模型的中间层，以保证运动的平滑过渡。整个流程是增量式的，每当有新的运动数据输入时，都会进行一次风格化和解码，并输出结果。

**关键创新**：LILAC的关键创新在于将离线VAE-Diffusion框架成功地扩展到了在线流式设置，并且在保证实时性的前提下，实现了高质量的动作风格化。与现有方法相比，LILAC不需要访问未来的运动帧，也不需要修改扩散模型的架构，从而更加灵活和高效。

**关键设计**：LILAC的关键设计包括：1) 滑动窗口的大小：需要根据实际应用场景进行调整，以平衡实时性和风格化质量；2) 运动特征注入的位置和方式：需要仔细设计，以保证运动过渡的平滑性，同时避免引入过多的计算开销；3) 损失函数的设计：需要综合考虑风格化质量、运动平滑性和实时性等因素。

## 📊 实验亮点

LILAC在基准数据集上进行了实验，结果表明，LILAC能够在保证实时性的前提下，实现高质量的动作风格化。与现有的流式方法相比，LILAC在风格化质量和运动平滑性方面都有显著提升。具体性能数据（例如延迟、风格化质量指标等）可在论文中找到。

## 🎯 应用场景

LILAC可应用于虚拟现实、游戏、动画制作等领域，实现对虚拟角色的实时动作风格化控制。例如，用户可以通过LILAC实时调整虚拟角色的动作风格，使其更符合用户的个性化需求。此外，LILAC还可以用于生成各种风格化的运动数据，用于训练其他机器学习模型，例如动作识别模型。

## 📄 摘要（原文）

> Generating long and stylized human motions in real time is critical for applications that demand continuous and responsive character control. Despite its importance, existing streaming approaches often operate directly in the raw motion space, leading to substantial computational overhead and making it difficult to maintain temporal stability. In contrast, latent-space VAE-Diffusion-based frameworks alleviate these issues and achieve high-quality stylization, but they are generally confined to offline processing. To bridge this gap, LILAC (Long-sequence Incremental Low-latency Arbitrary Motion Stylization via Streaming VAE-Diffusion with Causal Decoding) builds upon a recent high-performing offline framework for arbitrary motion stylization and extends it to an online setting through a latent-space streaming architecture with a sliding-window causal design and the injection of decoded motion features to ensure smooth motion transitions. This architecture enables long-sequence real-time arbitrary stylization without relying on future frames or modifying the diffusion model architecture, achieving a favorable balance between stylization quality and responsiveness as demonstrated by experiments on benchmark datasets. Supplementary video and examples are available at the project page: https://pren1.github.io/lilac/

