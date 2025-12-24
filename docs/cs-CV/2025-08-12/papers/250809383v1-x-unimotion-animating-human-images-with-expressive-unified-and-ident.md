---
layout: default
title: "X-UniMotion: Animating Human Images with Expressive, Unified and Identity-Agnostic Motion Latents"
---

# X-UniMotion: Animating Human Images with Expressive, Unified and Identity-Agnostic Motion Latents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09383" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09383v1</a>
  <a href="https://arxiv.org/pdf/2508.09383.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09383v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09383v1', 'X-UniMotion: Animating Human Images with Expressive, Unified and Identity-Agnostic Motion Latents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guoxian Song, Hongyi Xu, Xiaochen Zhao, You Xie, Tianpei Gu, Zenan Li, Chenxu Zhang, Linjie Luo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出X-UniMotion以实现高保真、身份无关的人体动画**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人体动画` `运动转移` `隐式潜在表示` `自监督学习` `虚拟现实` `增强现实` `多模态生成`

## 📋 核心要点

1. 现有运动转移方法依赖显式骨骼姿势，缺乏对多样化身份和姿势的有效处理。
2. X-UniMotion通过从单张图像中提取解耦的潜在标记，提供了一种新的运动表示方式，具有身份无关性。
3. 实验结果显示，X-UniMotion在运动表现力和身份保留方面显著优于现有方法，提升幅度明显。

## 📝 摘要（中文）

我们提出了X-UniMotion，一种统一且富有表现力的隐式潜在表示，用于整个人体运动的动画，包括面部表情、身体姿势和手势。与依赖显式骨骼姿势和启发式跨身份调整的传统运动转移方法不同，我们的方法直接从单张图像中编码多粒度运动，生成四个解耦的潜在标记，分别对应面部表情、身体姿势和每只手。这些运动潜在标记具有高度表现力和身份无关性，能够在不同身份、姿势和空间配置的主体之间实现高保真、详细的跨身份运动转移。为此，我们引入了一种自监督的端到端框架，联合学习运动编码器和潜在表示，并与基于DiT的视频生成模型一起训练，使用大规模多样的人体运动数据集。通过2D空间和颜色增强以及共享姿势下的跨身份主体对的合成3D渲染，强制执行运动与身份的解耦。此外，我们通过辅助解码器引导运动标记学习，以促进细粒度、语义对齐和深度感知的运动嵌入。大量实验表明，X-UniMotion在表现力和运动保真度方面超越了现有最先进的方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有运动转移方法在处理多样化身份和姿势时的局限性，尤其是依赖显式骨骼姿势的不足。

**核心思路**：我们提出了一种新的隐式潜在表示，能够从单张图像中直接提取多粒度运动信息，生成解耦的潜在标记，以实现高保真、身份无关的动画效果。

**技术框架**：整体架构包括运动编码器、潜在表示学习模块和基于DiT的视频生成模型。通过自监督学习，联合优化这些模块，以提高运动生成的质量和表现力。

**关键创新**：最重要的创新在于运动与身份的解耦，通过引入2D增强和合成3D渲染技术，显著提升了运动转移的灵活性和准确性。

**关键设计**：在模型设计中，我们使用了辅助解码器来促进运动标记的学习，确保生成的运动嵌入在语义上对齐且具备深度感知能力。

## 📊 实验亮点

实验结果表明，X-UniMotion在运动表现力和保真度方面超越了现有最先进的方法，具体表现为在多样化身份和姿势下的动画生成质量提升了显著的百分比，验证了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括动画制作、游戏开发、虚拟现实和增强现实等。通过实现高保真且身份无关的人体动画，X-UniMotion可以为创作者提供更灵活的工具，推动数字内容创作的创新与发展。

## 📄 摘要（原文）

> We present X-UniMotion, a unified and expressive implicit latent representation for whole-body human motion, encompassing facial expressions, body poses, and hand gestures. Unlike prior motion transfer methods that rely on explicit skeletal poses and heuristic cross-identity adjustments, our approach encodes multi-granular motion directly from a single image into a compact set of four disentangled latent tokens -- one for facial expression, one for body pose, and one for each hand. These motion latents are both highly expressive and identity-agnostic, enabling high-fidelity, detailed cross-identity motion transfer across subjects with diverse identities, poses, and spatial configurations. To achieve this, we introduce a self-supervised, end-to-end framework that jointly learns the motion encoder and latent representation alongside a DiT-based video generative model, trained on large-scale, diverse human motion datasets. Motion-identity disentanglement is enforced via 2D spatial and color augmentations, as well as synthetic 3D renderings of cross-identity subject pairs under shared poses. Furthermore, we guide motion token learning with auxiliary decoders that promote fine-grained, semantically aligned, and depth-aware motion embeddings. Extensive experiments show that X-UniMotion outperforms state-of-the-art methods, producing highly expressive animations with superior motion fidelity and identity preservation.

