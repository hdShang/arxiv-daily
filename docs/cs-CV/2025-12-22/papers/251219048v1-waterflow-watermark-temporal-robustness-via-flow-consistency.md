---
layout: default
title: "WaTeRFlow: Watermark Temporal Robustness via Flow Consistency"
---

# WaTeRFlow: Watermark Temporal Robustness via Flow Consistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19048" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19048v1</a>
  <a href="https://arxiv.org/pdf/2512.19048.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19048v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19048v1', 'WaTeRFlow: Watermark Temporal Robustness via Flow Consistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Utae Jeong, Sumin In, Hyunju Ryu, Jaewan Choi, Feng Yang, Jongheon Jeong, Seungryong Kim, Sangpil Kim

**分类**: cs.CV

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出WaTeRFlow框架，增强水印在图像转视频中的时间鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `图像水印` `视频水印` `时间鲁棒性` `图像转视频` `光流` `深度学习` `版权保护` `内容溯源`

## 📋 核心要点

1. 现有水印方案在图像转视频后，因每帧独立检测导致鲁棒性下降，无法满足跨模态应用需求。
2. WaTeRFlow框架通过FUSE引入真实失真，利用光流和时间一致性损失稳定预测，并保持语义信息。
3. 实验表明，WaTeRFlow显著提升了水印在I2V场景下的鲁棒性，提高了首帧和每帧的比特准确率。

## 📝 摘要（中文）

图像水印技术用于验证图像的真实性和来源，但现有方案容易受到各种失真和生成式编辑的攻击。基于深度学习的水印技术提高了对扩散模型图像编辑的鲁棒性，但当水印图像通过图像转视频（I2V）转换为视频时，每帧水印检测的性能会下降。I2V技术已从短而抖动的片段迅速发展到多秒、时间连贯的场景，不仅用于内容创作，还用于世界建模和模拟工作流程，使得跨模态水印恢复至关重要。本文提出了WaTeRFlow框架，专门用于增强I2V下的鲁棒性。它包含：（i）FUSE（Flow-guided Unified Synthesis Engine），通过指令驱动的编辑和快速视频扩散代理，在训练期间使编码器-解码器暴露于真实的失真；（ii）光流扭曲和时间一致性损失（TCL），用于稳定每帧预测；（iii）语义保持损失，用于维护条件信号。在代表性的I2V模型上的实验表明，从帧中可以准确恢复水印，并且在视频生成前后应用各种失真时，首帧和每帧的比特准确率更高，鲁棒性更强。

## 🔬 方法详解

**问题定义**：现有图像水印技术在图像转视频（I2V）场景下表现不佳。主要痛点在于，I2V过程引入了时间上的不一致性，导致每帧独立的水印检测结果不稳定，整体鲁棒性下降。此外，现有的深度学习水印方法主要关注图像域的攻击，缺乏对视频生成过程中的各种失真和编辑的适应性。

**核心思路**：WaTeRFlow的核心思路是利用光流信息来增强水印检测的时间一致性。通过在训练过程中模拟I2V过程中的各种失真，并引入时间一致性损失，使得水印检测器能够更好地适应视频帧之间的变化，从而提高整体的鲁棒性。此外，还通过语义保持损失来确保水印的嵌入不会影响视频内容的语义信息。

**技术框架**：WaTeRFlow框架主要包含三个核心模块：FUSE（Flow-guided Unified Synthesis Engine）、光流扭曲与时间一致性损失（TCL）以及语义保持损失。FUSE模块负责生成带有各种失真的训练数据，模拟真实的I2V场景。光流扭曲与TCL模块利用光流信息来对齐相邻帧的水印检测结果，并引入时间一致性损失来约束检测结果的稳定性。语义保持损失则用于确保水印的嵌入不会影响视频内容的语义信息。

**关键创新**：WaTeRFlow的关键创新在于其针对I2V场景的时间鲁棒性设计。与现有的图像水印方法不同，WaTeRFlow显式地考虑了视频帧之间的时间关系，并利用光流信息来增强水印检测的时间一致性。此外，FUSE模块能够生成更加真实的训练数据，使得水印检测器能够更好地适应各种I2V过程中的失真。

**关键设计**：FUSE模块通过指令驱动的编辑和快速视频扩散代理来生成带有各种失真的训练数据。时间一致性损失（TCL）基于光流计算相邻帧之间的对应关系，并约束对应位置的水印检测结果尽可能一致。语义保持损失通常采用感知损失或对抗损失，以确保水印的嵌入不会影响视频内容的语义信息。具体的网络结构和参数设置取决于所使用的I2V模型和水印检测器。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19048v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19048v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19048v1/figure/figure3_05.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，WaTeRFlow在各种I2V模型上均能实现准确的水印恢复，并且在视频生成前后应用各种失真时，首帧和每帧的比特准确率均显著提高。与现有方法相比，WaTeRFlow在I2V场景下具有更强的鲁棒性和更高的准确率，能够有效抵抗各种攻击。

## 🎯 应用场景

WaTeRFlow技术可应用于视频版权保护、内容溯源、深度伪造检测等领域。通过在视频中嵌入鲁棒的水印，可以有效防止未经授权的复制和传播，并为内容创作者提供法律保护。此外，该技术还可以用于检测深度伪造视频，维护网络安全和信息安全。

## 📄 摘要（原文）

> Image watermarking supports authenticity and provenance, yet many schemes are still easy to bypass with various distortions and powerful generative edits. Deep learning-based watermarking has improved robustness to diffusion-based image editing, but a gap remains when a watermarked image is converted to video by image-to-video (I2V), in which per-frame watermark detection weakens. I2V has quickly advanced from short, jittery clips to multi-second, temporally coherent scenes, and it now serves not only content creation but also world-modeling and simulation workflows, making cross-modal watermark recovery crucial. We present WaTeRFlow, a framework tailored for robustness under I2V. It consists of (i) FUSE (Flow-guided Unified Synthesis Engine), which exposes the encoder-decoder to realistic distortions via instruction-driven edits and a fast video diffusion proxy during training, (ii) optical-flow warping with a Temporal Consistency Loss (TCL) that stabilizes per-frame predictions, and (iii) a semantic preservation loss that maintains the conditioning signal. Experiments across representative I2V models show accurate watermark recovery from frames, with higher first-frame and per-frame bit accuracy and resilience when various distortions are applied before or after video generation.

