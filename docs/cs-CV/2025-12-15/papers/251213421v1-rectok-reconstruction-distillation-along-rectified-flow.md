---
layout: default
title: RecTok: Reconstruction Distillation along Rectified Flow
---

# RecTok: Reconstruction Distillation along Rectified Flow

**arXiv**: [2512.13421v1](https://arxiv.org/abs/2512.13421) | [PDF](https://arxiv.org/pdf/2512.13421.pdf)

**作者**: Qingyu Shi, Size Wu, Jinbin Bai, Kaidong Yu, Yujing Wang, Yunhai Tong, Xiangtai Li, Xuelong Li

**分类**: cs.CV

**发布日期**: 2025-12-15

**🔗 代码/项目**: [PROJECT_PAGE](https://shi-qingyu.github.io/rectok.github.io)

---

## 💡 一句话要点

**RecTok：通过校正流上的重构蒸馏，突破高维视觉Tokenizers的性能瓶颈**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视觉Tokenizers` `扩散模型` `流匹配` `语义蒸馏` `重构蒸馏` `图像生成` `高维潜在空间`

## 📋 核心要点

1. 现有视觉Tokenizers受限于维度与生成质量的权衡，高维Tokenizers性能不佳。
2. RecTok通过流语义蒸馏和重构-对齐蒸馏，丰富前向流的语义信息，提升高维Tokenizers性能。
3. 实验表明，RecTok在图像重建、生成质量和判别性能上均达到SOTA，且性能随维度增加而提升。

## 📝 摘要（中文）

视觉Tokenizers在扩散模型中起着关键作用。潜在空间的维度决定了重建保真度和潜在特征的语义表达能力。然而，维度和生成质量之间存在着根本的权衡，这限制了现有方法只能使用低维潜在空间。尽管最近的研究利用视觉基础模型来丰富视觉Tokenizers的语义并加速收敛，但高维Tokenizers的性能仍然不如低维Tokenizers。本文提出了RecTok，通过流语义蒸馏和重构-对齐蒸馏这两个关键创新，克服了高维视觉Tokenizers的局限性。我们的关键见解是使流匹配中的前向流在语义上丰富，将其作为扩散Transformer的训练空间，而不是像以前的工作那样专注于潜在空间。具体来说，我们的方法将视觉基础模型中的语义信息提炼到流匹配中的前向流轨迹中。我们进一步通过引入掩码特征重构损失来增强语义。我们的RecTok实现了卓越的图像重建、生成质量和判别性能。在有和没有无分类器指导设置下，它在gFID-50K上都取得了最先进的结果，同时保持了语义丰富的潜在空间结构。此外，随着潜在维度的增加，我们观察到持续的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决高维视觉Tokenizers在扩散模型中性能不佳的问题。现有方法受限于潜在空间维度和生成质量的权衡，导致高维Tokenizers无法充分发挥其语义表达能力。现有方法主要集中在优化潜在空间，忽略了前向流的语义信息。

**核心思路**：论文的核心思路是将视觉基础模型中的语义信息提炼到流匹配的前向流轨迹中，使前向流在语义上更加丰富。通过这种方式，扩散Transformer的训练空间不再局限于潜在空间，而是扩展到整个前向流，从而提升高维Tokenizers的性能。同时，引入重构-对齐蒸馏，进一步增强语义信息。

**技术框架**：RecTok的整体框架包括以下几个主要模块：1) 使用视觉基础模型提取图像特征；2) 使用流匹配方法构建前向流；3) 将视觉基础模型的语义信息蒸馏到前向流轨迹中；4) 引入掩码特征重构损失，增强语义信息；5) 使用扩散Transformer进行图像生成。

**关键创新**：RecTok最重要的技术创新点在于将视觉基础模型的语义信息蒸馏到流匹配的前向流轨迹中。与现有方法不同，RecTok不再仅仅关注潜在空间的优化，而是将前向流作为扩散Transformer的训练空间，从而充分利用了视觉基础模型的语义信息。此外，重构-对齐蒸馏也是一个关键创新，它通过引入掩码特征重构损失，进一步增强了语义信息。

**关键设计**：在流语义蒸馏中，使用KL散度损失来衡量前向流轨迹和视觉基础模型特征之间的差异，从而将语义信息从视觉基础模型传递到前向流。在重构-对齐蒸馏中，使用掩码特征重构损失来促使模型学习到更丰富的语义信息。具体的网络结构和参数设置需要参考论文原文。

## 📊 实验亮点

RecTok在gFID-50K指标上取得了显著的性能提升，在有和没有无分类器指导设置下都达到了SOTA水平。实验结果表明，RecTok能够有效提升图像重建、生成质量和判别性能。更重要的是，随着潜在维度的增加，RecTok的性能持续提升，这表明该方法能够充分利用高维潜在空间的优势。

## 🎯 应用场景

RecTok具有广泛的应用前景，可用于图像生成、图像编辑、图像修复等领域。通过提升高维视觉Tokenizers的性能，RecTok可以生成更高质量、更逼真的图像，并为各种视觉任务提供更强大的语义表达能力。该研究的成果有望推动扩散模型在实际应用中的发展。

## 📄 摘要（原文）

> Visual tokenizers play a crucial role in diffusion models. The dimensionality of latent space governs both reconstruction fidelity and the semantic expressiveness of the latent feature. However, a fundamental trade-off is inherent between dimensionality and generation quality, constraining existing methods to low-dimensional latent spaces. Although recent works have leveraged vision foundation models to enrich the semantics of visual tokenizers and accelerate convergence, high-dimensional tokenizers still underperform their low-dimensional counterparts. In this work, we propose RecTok, which overcomes the limitations of high-dimensional visual tokenizers through two key innovations: flow semantic distillation and reconstruction--alignment distillation. Our key insight is to make the forward flow in flow matching semantically rich, which serves as the training space of diffusion transformers, rather than focusing on the latent space as in previous works. Specifically, our method distills the semantic information in VFMs into the forward flow trajectories in flow matching. And we further enhance the semantics by introducing a masked feature reconstruction loss. Our RecTok achieves superior image reconstruction, generation quality, and discriminative performance. It achieves state-of-the-art results on the gFID-50K under both with and without classifier-free guidance settings, while maintaining a semantically rich latent space structure. Furthermore, as the latent dimensionality increases, we observe consistent improvements. Code and model are available at https://shi-qingyu.github.io/rectok.github.io.

