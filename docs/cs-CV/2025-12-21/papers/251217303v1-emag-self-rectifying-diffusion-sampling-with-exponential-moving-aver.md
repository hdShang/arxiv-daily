---
layout: default
title: "EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance"
---

# EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17303" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17303v1</a>
  <a href="https://arxiv.org/pdf/2512.17303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17303v1', 'EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ankit Yadav, Ta Duc Huy, Lingqiao Liu

**分类**: cs.CV

**发布日期**: 2025-12-19

**备注**: 26 pages

---

## 💡 一句话要点

**提出EMAG：一种基于指数移动平均指导的自校正扩散采样方法，提升生成质量。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `扩散模型` `生成模型` `注意力机制` `指数移动平均` `自适应指导`

## 📋 核心要点

1. 现有扩散模型指导方法缺乏对负样本粒度和难度的有效控制，且目标层选择固定，限制了生成质量的进一步提升。
2. EMAG通过指数移动平均自适应地选择注意力层，生成更难且语义忠实的负样本，从而暴露并纠正生成过程中的细微错误。
3. 实验表明，EMAG显著提升了生成质量和人类偏好得分，并且可以与现有高级指导技术结合，进一步提高性能。

## 📝 摘要（中文）

在扩散和流匹配生成模型中，指导技术被广泛用于提高样本质量和一致性。无分类器指导（CFG）是现代系统中的常用选择，它通过对比条件和无条件样本来实现这一点。最近的研究探索了在推理时使用较弱模型对比负样本，通过强/弱模型对、基于注意力的掩码、随机块丢弃或扰动自注意力能量景观等方式。虽然这些策略改进了生成质量，但它们仍然缺乏对负样本粒度或难度的可靠控制，并且目标层选择通常是固定的。我们提出了一种名为指数移动平均指导（EMAG）的免训练机制，该机制在扩散Transformer中修改推理时的注意力，并采用基于统计的自适应层选择规则。与先前的方法不同，EMAG产生更难的、语义上忠实的负样本（细粒度退化），揭示了困难的失败模式，使去噪器能够改进细微的伪影，从而提高质量和人类偏好得分（HPS），相比CFG提升了+0.46。我们进一步证明，EMAG自然地与高级指导技术（如APG和CADS）结合，从而进一步提高HPS。

## 🔬 方法详解

**问题定义**：现有扩散模型，特别是基于Transformer的扩散模型，在生成高质量图像时依赖于指导技术，如无分类器指导（CFG）。然而，现有方法在生成负样本时，难以控制负样本的难度和粒度，并且通常采用固定的层选择策略，这限制了模型纠正细微错误的能力，阻碍了生成质量的进一步提升。

**核心思路**：EMAG的核心思想是利用指数移动平均（EMA）来构建一个“弱”模型，并使用该弱模型生成更难、更细粒度的负样本。通过对比原始模型和EMA模型在注意力机制上的差异，自适应地选择需要进行负样本生成的层，从而使模型能够专注于纠正那些最容易出错的区域。这种方法旨在暴露并纠正生成过程中的细微伪影，提升整体生成质量。

**技术框架**：EMAG主要在扩散Transformer的推理阶段进行操作，无需额外的训练。其流程如下：1) 使用原始模型进行前向传播，计算每一层的注意力权重。2) 使用指数移动平均（EMA）更新注意力权重，得到一个“弱”模型的注意力权重。3) 基于原始模型和EMA模型的注意力权重差异，自适应地选择需要进行负样本生成的层。4) 在选定的层上，使用EMA模型生成负样本。5) 将原始模型和负样本结合，进行最终的图像生成。

**关键创新**：EMAG的关键创新在于其自适应层选择规则和基于EMA的负样本生成方法。与现有方法相比，EMAG能够生成更难、更细粒度的负样本，并且能够根据模型的实际表现，自适应地选择需要进行负样本生成的层。这种方法使得模型能够专注于纠正那些最容易出错的区域，从而提升整体生成质量。此外，EMAG是一种免训练的方法，可以直接应用于现有的扩散模型，无需额外的训练成本。

**关键设计**：EMAG的关键设计包括：1) 指数移动平均的衰减率：控制EMA模型的更新速度，影响负样本的难度。2) 自适应层选择规则：基于原始模型和EMA模型的注意力权重差异，选择需要进行负样本生成的层。可以使用不同的统计指标来衡量注意力权重的差异，例如KL散度或余弦相似度。3) 负样本生成方式：可以使用不同的方法来生成负样本，例如直接使用EMA模型的输出，或者对EMA模型的输出进行一定的扰动。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17303v1/resources/Slide2.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17303v1/resources/negative_sample_grid.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17303v1/resources/Negative_example_degradation_control.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EMAG在图像生成质量上优于传统的无分类器指导（CFG）方法，人类偏好得分（HPS）提升了+0.46。此外，EMAG可以与高级指导技术（如APG和CADS）结合，进一步提高HPS。这些结果表明，EMAG能够有效地提升生成图像的质量和细节，并且具有良好的通用性和可扩展性。

## 🎯 应用场景

EMAG可广泛应用于各种基于扩散模型的图像生成任务，例如文本到图像生成、图像修复、图像超分辨率等。该方法能够提升生成图像的质量和细节，尤其是在需要高保真度和精细控制的应用场景中具有重要价值。未来，EMAG有望与其他先进的生成模型和指导技术结合，进一步推动图像生成领域的发展。

## 📄 摘要（原文）

> In diffusion and flow-matching generative models, guidance techniques are widely used to improve sample quality and consistency. Classifier-free guidance (CFG) is the de facto choice in modern systems and achieves this by contrasting conditional and unconditional samples. Recent work explores contrasting negative samples at inference using a weaker model, via strong/weak model pairs, attention-based masking, stochastic block dropping, or perturbations to the self-attention energy landscape. While these strategies refine the generation quality, they still lack reliable control over the granularity or difficulty of the negative samples, and target-layer selection is often fixed. We propose Exponential Moving Average Guidance (EMAG), a training-free mechanism that modifies attention at inference time in diffusion transformers, with a statistics-based, adaptive layer-selection rule. Unlike prior methods, EMAG produces harder, semantically faithful negatives (fine-grained degradations), surfacing difficult failure modes, enabling the denoiser to refine subtle artifacts, boosting the quality and human preference score (HPS) by +0.46 over CFG. We further demonstrate that EMAG naturally composes with advanced guidance techniques, such as APG and CADS, further improving HPS.

