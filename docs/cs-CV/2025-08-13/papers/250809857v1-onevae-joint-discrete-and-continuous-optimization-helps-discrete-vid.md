---
layout: default
title: "OneVAE: Joint Discrete and Continuous Optimization Helps Discrete Video VAE Train Better"
---

# OneVAE: Joint Discrete and Continuous Optimization Helps Discrete Video VAE Train Better

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09857" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09857v1</a>
  <a href="https://arxiv.org/pdf/2508.09857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09857v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09857v1', 'OneVAE: Joint Discrete and Continuous Optimization Helps Discrete Video VAE Train Better')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yupeng Zhou, Zhen Li, Ziheng Ouyang, Yuming Chen, Ruoyi Du, Daquan Zhou, Bin Fu, Yihao Liu, Peng Gao, Ming-Ming Cheng, Qibin Hou

**分类**: cs.CV

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出OneVAE以解决离散视频VAE训练不稳定问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `离散视频VAE` `连续VAE` `多模态学习` `重建质量` `联合优化`

## 📋 核心要点

1. 现有的离散视频VAE在训练过程中存在不稳定性、长训练时间和重建质量下降等问题。
2. 本文提出的OneVAE通过引入连续VAE的先验知识，结合多标记量化机制和强化首帧重建，提升了离散视频VAE的训练效果。
3. 实验结果表明，OneVAE在收敛速度和重建质量上均显著优于传统的离散视频VAE，达到了更高的PSNR值。

## 📝 摘要（中文）

将视频编码为离散标记可以与文本标记对齐，从而促进简洁统一的多模态大语言模型。然而，现有的离散视频变分自编码器（VAE）在训练过程中面临不稳定、训练时间长和重建质量下降等问题。本文提出了一种名为OneVAE的方法，通过利用连续VAE的先验知识，显著加快了收敛速度并提高了性能。同时，提出了多标记量化机制和强化首帧重建的结构改进，进一步提升了重建质量。OneVAE首次在单一网络中实现了离散和连续表示的统一优化，展现出竞争力的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决离散视频变分自编码器（VAE）在训练过程中面临的稳定性差、训练时间长和重建质量低的问题。现有方法在处理视频数据时，往往无法有效利用连续表示的优势。

**核心思路**：OneVAE的核心思想是通过引入连续VAE的先验知识来增强离散视频VAE的训练效果，从而实现更快的收敛和更高的重建质量。通过重新思考离散与连续表示之间的内在联系，提出了一种联合优化方案。

**技术框架**：OneVAE的整体架构包括多个模块，首先是多标记量化机制，用于提升重建质量；其次是强化首帧重建，以便后续帧能够更好地利用首帧信息；最后是联合离散-连续优化方案，统一了两种表示方式。

**关键创新**：OneVAE的主要创新在于首次实现了离散和连续表示的统一优化，显著提高了训练效率和重建质量。与传统方法相比，OneVAE在收敛速度上快了数倍，且在性能上表现出色。

**关键设计**：在参数设置上，OneVAE采用了多标记量化机制，优化了潜在维度，并设计了特定的损失函数以强化首帧重建，确保在高压缩比下仍能保持良好的重建效果。

## 📊 实验亮点

实验结果显示，OneVAE在PSNR指标上提升了近1 dB，并且收敛速度比从头开始训练快数倍。这表明该方法在离散视频VAE的训练和重建质量上具有显著优势，能够有效解决现有方法的不足。

## 🎯 应用场景

OneVAE的研究成果在多模态学习、视频理解和生成等领域具有广泛的应用潜力。通过提高离散视频VAE的训练效率和重建质量，该方法可以为视频内容生成、视频摘要和视频检索等任务提供更强大的技术支持，推动相关领域的发展。

## 📄 摘要（原文）

> Encoding videos into discrete tokens could align with text tokens to facilitate concise and unified multi-modal LLMs, yet introducing significant spatiotemporal compression compared to continuous video representation. Previous discrete video VAEs experienced unstable training, long training time, and degraded reconstruction quality. Given the easier training and superior performance of continuous VAEs, an intuitive idea is to enhance discrete video VAEs by leveraging continuous VAEs. After rethinking the intrinsic link between discrete and continuous representations, we found that FSQ could effectively preserve pre-trained continuous VAE priors compared to other quantization methods. By leveraging continuous VAE priors, it converges several times faster than training from scratch and achieves superior performance at convergence. Meanwhile, two structural improvements are proposed. First, inspired by how continuous VAEs enhance reconstruction via enlarged latent dimensions, we introduce a multi-token quantization mechanism, which achieves nearly a 1 dB improvement in PSNR without compromising the token compression ratio. Second, to tackle reconstruction challenges in high-compression video VAEs, we strengthen first-frame reconstruction, enabling the causal VAE to leverage this information in subsequent frames and markedly improving the performance of 4 x 16 x 16 discrete VAEs. Furthermore, we propose a joint discrete-continuous optimization scheme that unifies the two paradigms and, for the first time, achieves competitive performance on both continuous and discrete representations within a single network. We name our method OneVAE to reflect this connection.

