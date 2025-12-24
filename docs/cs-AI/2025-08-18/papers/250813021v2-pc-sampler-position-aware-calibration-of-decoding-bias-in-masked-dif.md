---
layout: default
title: "PC-Sampler: Position-Aware Calibration of Decoding Bias in Masked Diffusion Models"
---

# PC-Sampler: Position-Aware Calibration of Decoding Bias in Masked Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13021" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13021v2</a>
  <a href="https://arxiv.org/pdf/2508.13021.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13021v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13021v2', 'PC-Sampler: Position-Aware Calibration of Decoding Bias in Masked Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengcheng Huang, Shuhao Liu, Zhenghao Liu, Yukun Yan, Shuo Wang, Zulong Chen, Tong Xiao

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-18 (更新: 2025-08-19)

**备注**: 17 pages,13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/NEUIR/PC-Sampler)

---

## 💡 一句话要点

**提出PC-Sampler以解决MDMs解码策略的局限性**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `掩蔽扩散模型` `序列生成` `解码策略` `位置感知` `置信度校准` `信息最大化` `自然语言处理`

## 📋 核心要点

1. 现有的掩蔽扩散模型在解码策略上存在局限，导致生成质量不稳定，尤其是在早期阶段容易选择平凡标记。
2. 本文提出PC-Sampler，通过位置感知加权和置信度校准，优化解码路径并提高生成内容的相关性。
3. 实验结果显示，PC-Sampler在多个基准任务中表现优异，平均提升超过10%，接近自回归模型的性能水平。

## 📝 摘要（中文）

近年来，掩蔽扩散模型（MDMs）作为序列生成的强大非自回归替代方案取得了显著进展。然而，初步实验表明，MDMs的生成质量对解码策略的选择高度敏感。特别是，广泛采用的不确定性基础采样器存在两个主要局限：缺乏全局轨迹控制和在解码早期阶段对平凡标记的明显偏向。为此，本文提出了位置感知置信度校准采样（PC-Sampler），一种将全局轨迹规划与内容感知信息最大化相结合的新解码策略。PC-Sampler引入位置感知加权机制来调节解码路径，并使用校准置信度分数来抑制平凡标记的过早选择。在三个先进的MDMs上进行的广泛实验表明，PC-Sampler在七个具有挑战性的基准测试中平均超越现有MDMs解码策略超过10%，显著缩小了与最先进自回归模型的性能差距。

## 🔬 方法详解

**问题定义**：本文旨在解决掩蔽扩散模型在解码过程中存在的全局轨迹控制不足和早期选择平凡标记的偏向问题。这些问题限制了模型的生成质量和潜力。

**核心思路**：PC-Sampler的核心思想是结合全局轨迹规划与内容感知的信息最大化，通过位置感知加权机制和置信度校准来优化解码过程，确保生成内容的多样性和相关性。

**技术框架**：PC-Sampler的整体架构包括两个主要模块：位置感知加权模块和置信度校准模块。前者用于调节解码路径，后者则用于抑制平凡标记的选择。整个流程通过不断迭代优化生成结果。

**关键创新**：PC-Sampler的主要创新在于引入了位置感知的加权机制和校准的置信度评分，这与现有的不确定性基础采样器形成了鲜明对比，后者往往缺乏全局控制能力。

**关键设计**：在设计中，PC-Sampler采用了特定的权重参数设置，以确保在解码过程中对重要标记的优先选择，同时使用了特定的损失函数来优化置信度校准，确保生成结果的质量。

## 📊 实验亮点

实验结果表明，PC-Sampler在三个先进的掩蔽扩散模型上进行的七个基准测试中，平均性能提升超过10%，显著缩小了与最先进自回归模型的性能差距，展示了其在解码策略上的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和自动文本生成等。通过提高掩蔽扩散模型的生成质量，PC-Sampler能够在实际应用中提供更为准确和相关的内容生成，推动智能对话和自动化内容创作的发展。

## 📄 摘要（原文）

> Recent advances in masked diffusion models (MDMs) have established them as powerful non-autoregressive alternatives for sequence generation. Nevertheless, our preliminary experiments reveal that the generation quality of MDMs is still highly sensitive to the choice of decoding strategy. In particular, widely adopted uncertainty-based samplers suffer from two key limitations: a lack of global trajectory control and a pronounced bias toward trivial tokens in the early stages of decoding. These shortcomings restrict the full potential of MDMs. In this work, we introduce Position-Aware Confidence-Calibrated Sampling (PC-Sampler), a novel decoding strategy that unifies global trajectory planning with content-aware informativeness maximization. PC-Sampler incorporates a position-aware weighting mechanism to regulate the decoding path and a calibrated confidence score to suppress the premature selection of trivial tokens. Extensive experiments on three advanced MDMs across seven challenging benchmarks-including logical reasoning and planning tasks-demonstrate that PC-Sampler consistently outperforms existing MDM decoding strategies by more than 10% on average, significantly narrowing the performance gap with state-of-the-art autoregressive models. All codes are available at https://github.com/NEUIR/PC-Sampler.

