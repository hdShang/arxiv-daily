---
layout: default
title: "LUMA: Low-Dimension Unified Motion Alignment with Dual-Path Anchoring for Text-to-Motion Diffusion Model"
---

# LUMA: Low-Dimension Unified Motion Alignment with Dual-Path Anchoring for Text-to-Motion Diffusion Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25304" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25304v1</a>
  <a href="https://arxiv.org/pdf/2509.25304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25304v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25304v1', 'LUMA: Low-Dimension Unified Motion Alignment with Dual-Path Anchoring for Text-to-Motion Diffusion Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haozhe Jia, Wenshuo Chen, Yuqi Lin, Yang Yang, Lei Wang, Mang Ning, Bowen Tian, Songning Lai, Nanqian Jia, Yifan Chen, Yutao Yue

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**LUMA：基于双路锚定的低维统一运动对齐文本到动作扩散模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `文本到动作生成` `扩散模型` `运动对齐` `对比学习` `时域锚定` `频域锚定` `语义监督` `动作生成`

## 📋 核心要点

1. 现有基于扩散模型的文本到动作生成方法存在语义不对齐和运动伪影问题，主要原因是网络深层梯度衰减导致高层特征学习不足。
2. LUMA通过双路锚定增强语义对齐，一路利用MoCLIP在时域进行语义监督，另一路利用低频DCT分量在频域提供互补对齐信号。
3. 实验结果表明，LUMA在HumanML3D和KIT-ML数据集上取得了SOTA性能，FID分数分别为0.035和0.123，并且收敛速度提高了1.4倍。

## 📝 摘要（中文）

本文提出LUMA（低维统一运动对齐），一种文本到动作的扩散模型，旨在解决现有基于U-Net架构的模型在文本到动作生成任务中存在的语义不对齐和运动伪影问题。通过分析发现，网络深层的梯度衰减是导致高层特征学习不足的关键瓶颈。LUMA通过引入双路锚定来增强语义对齐。第一条路径采用轻量级的MoCLIP模型，通过对比学习进行训练，无需外部数据，从而在时间域提供语义监督。第二条路径引入频域中的互补对齐信号，该信号从以其丰富的语义内容而闻名的低频DCT分量中提取。这两个锚通过时间调制机制自适应地融合，使模型能够在整个去噪过程中从粗略对齐逐步过渡到精细的语义细化。在HumanML3D和KIT-ML上的实验结果表明，LUMA实现了最先进的性能，FID分数分别为0.035和0.123。此外，与基线相比，LUMA将收敛速度提高了1.4倍，使其成为高保真文本到动作生成的高效且可扩展的解决方案。

## 🔬 方法详解

**问题定义**：现有基于扩散模型的文本到动作生成方法，特别是基于U-Net架构的模型，在生成动作时存在语义不对齐和运动伪影的问题。这些问题源于网络深层梯度衰减，导致模型无法充分学习高层语义特征，从而影响生成动作的质量和真实性。

**核心思路**：LUMA的核心思路是通过引入双路锚定机制，从时域和频域两个角度对运动数据进行语义对齐，从而增强模型对高层语义特征的学习能力。时域锚定利用对比学习得到的MoCLIP模型提供语义监督，频域锚定则利用低频DCT分量提取语义信息。

**技术框架**：LUMA的整体框架是一个基于扩散模型的文本到动作生成流程，主要包含以下几个模块：1) 文本编码器：将输入的文本描述转换为文本特征向量。2) 运动扩散模型：基于U-Net架构，负责从噪声中逐步生成运动数据。3) 时域锚定模块：利用MoCLIP模型，在时间域对运动数据进行语义监督。4) 频域锚定模块：提取低频DCT分量，在频率域提供互补的对齐信号。5) 时间调制模块：自适应地融合时域和频域的锚定信号，实现从粗略对齐到精细语义细化的过渡。

**关键创新**：LUMA的关键创新在于双路锚定机制，它同时利用时域和频域的信息来增强语义对齐。与现有方法相比，LUMA无需依赖外部数据进行对比学习，并且能够自适应地融合不同域的对齐信号，从而实现更精确的语义控制和更高质量的动作生成。

**关键设计**：LUMA的关键设计包括：1) 轻量级的MoCLIP模型，通过对比学习在时间域提供语义监督。2) 低频DCT分量的提取，利用其丰富的语义信息在频率域提供互补的对齐信号。3) 时间调制机制，自适应地融合时域和频域的锚定信号，实现从粗略对齐到精细语义细化的过渡。4) 损失函数的设计，综合考虑了扩散模型的重建损失、对比学习损失以及对齐损失，从而优化模型的整体性能。

## 📊 实验亮点

LUMA在HumanML3D和KIT-ML数据集上取得了显著的性能提升，FID分数分别达到了0.035和0.123，超越了现有的SOTA方法。此外，LUMA还显著提高了收敛速度，与基线相比，收敛速度提高了1.4倍，这表明LUMA具有更高的训练效率和更好的可扩展性。

## 🎯 应用场景

LUMA具有广泛的应用前景，包括虚拟现实、游戏开发、动画制作、人机交互等领域。它可以根据文本描述自动生成逼真自然的动作，从而降低动作生成成本，提高创作效率。此外，LUMA还可以用于训练更智能的机器人，使其能够理解人类的指令并执行相应的动作。

## 📄 摘要（原文）

> While current diffusion-based models, typically built on U-Net architectures, have shown promising results on the text-to-motion generation task, they still suffer from semantic misalignment and kinematic artifacts. Through analysis, we identify severe gradient attenuation in the deep layers of the network as a key bottleneck, leading to insufficient learning of high-level features. To address this issue, we propose \textbf{LUMA} (\textit{\textbf{L}ow-dimension \textbf{U}nified \textbf{M}otion \textbf{A}lignment}), a text-to-motion diffusion model that incorporates dual-path anchoring to enhance semantic alignment. The first path incorporates a lightweight MoCLIP model trained via contrastive learning without relying on external data, offering semantic supervision in the temporal domain. The second path introduces complementary alignment signals in the frequency domain, extracted from low-frequency DCT components known for their rich semantic content. These two anchors are adaptively fused through a temporal modulation mechanism, allowing the model to progressively transition from coarse alignment to fine-grained semantic refinement throughout the denoising process. Experimental results on HumanML3D and KIT-ML demonstrate that LUMA achieves state-of-the-art performance, with FID scores of 0.035 and 0.123, respectively. Furthermore, LUMA accelerates convergence by 1.4$\times$ compared to the baseline, making it an efficient and scalable solution for high-fidelity text-to-motion generation.

