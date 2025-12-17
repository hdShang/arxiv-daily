---
layout: default
title: X2Video: Adapting Diffusion Models for Multimodal Controllable Neural Video Rendering
---

# X2Video: Adapting Diffusion Models for Multimodal Controllable Neural Video Rendering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08530" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08530v1</a>
  <a href="https://arxiv.org/pdf/2510.08530.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08530v1" onclick="toggleFavorite(this, '2510.08530v1', 'X2Video: Adapting Diffusion Models for Multimodal Controllable Neural Video Rendering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhitong Huang, Mohan Zhang, Renhan Wang, Rui Tang, Hao Zhu, Jing Liao

**分类**: cs.GR, cs.CV

**发布日期**: 2025-10-09

**备注**: Code, model, and dataset will be released at project page soon: https://luckyhzt.github.io/x2video

**🔗 代码/项目**: [PROJECT_PAGE](https://luckyhzt.github.io/x2video)

---

## 💡 一句话要点

**提出X2Video以解决多模态视频渲染控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `扩散模型` `多模态控制` `光线真实感` `自注意力机制` `递归采样` `内在引导` `图像处理`

## 📋 核心要点

1. 现有视频生成方法在多模态控制和时间一致性方面存在不足，难以实现高质量的光线真实感视频渲染。
2. X2Video通过扩散模型结合内在引导和多模态控制，采用混合自注意力机制和掩蔽交叉注意力机制，提升视频生成的质量和灵活性。
3. 实验结果表明，X2Video能够生成长时间一致且光线真实感的视频，支持多种控制方式，显著提升了生成效果。

## 📝 摘要（中文）

我们提出了X2Video，这是第一个基于扩散模型的光线真实感视频渲染方法，能够通过内在通道（如反照率、法线、粗糙度、金属度和辐照度）进行引导，同时支持通过参考图像和文本提示进行直观的多模态控制。内在引导允许对颜色、材料、几何形状和光照进行准确操控，而参考图像和文本提示则在缺乏内在信息时提供直观调整。为实现这些功能，我们通过采用新颖高效的混合自注意力机制将内在引导图像生成模型XRGB扩展到视频生成，确保视频帧之间的时间一致性，并增强对参考图像的保真度。我们还开发了掩蔽交叉注意力机制，以有效解耦全局和局部文本提示，并将其应用于相应的区域。我们的递归采样方法结合关键帧预测和帧插值，支持长视频生成，保持长时间范围内的一致性并防止错误累积。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有视频生成方法在多模态控制和时间一致性方面的不足，尤其是在光线真实感视频渲染中，如何有效利用内在通道信息进行引导。

**核心思路**：我们提出X2Video，通过扩散模型实现视频生成，结合内在引导和多模态控制，采用混合自注意力机制确保时间一致性，同时引入掩蔽交叉注意力机制以处理全局和局部文本提示。

**技术框架**：X2Video的整体架构包括内在引导模块、混合自注意力模块、掩蔽交叉注意力模块和递归采样模块。内在引导模块负责提取和处理内在通道信息，混合自注意力模块确保帧间一致性，掩蔽交叉注意力模块处理多模态输入，递归采样模块用于长视频生成。

**关键创新**：X2Video的主要创新在于将内在引导与多模态控制相结合，采用混合自注意力机制和递归采样方法，显著提升了视频生成的质量和一致性，尤其是在长视频生成中。

**关键设计**：在设计中，我们设置了特定的损失函数以优化视频质量，采用了高效的网络结构以支持大规模视频数据的处理，并通过递归采样策略减少了错误累积，确保了长时间范围内的一致性。

## 📊 实验亮点

实验结果表明，X2Video在生成长视频时能够保持时间一致性和光线真实感，相较于基线方法，视频质量提升显著。具体而言，X2Video在多模态控制下生成的长视频在视觉效果上优于现有技术，且在参数调优方面表现出更高的灵活性和准确性。

## 🎯 应用场景

X2Video的研究成果在多个领域具有潜在应用价值，包括电影制作、游戏开发、虚拟现实和增强现实等。通过实现高质量的光线真实感视频生成，该技术能够为创作者提供更灵活的工具，提升视觉内容的创作效率和质量，未来可能在数字内容创作中发挥重要作用。

## 📄 摘要（原文）

> We present X2Video, the first diffusion model for rendering photorealistic videos guided by intrinsic channels including albedo, normal, roughness, metallicity, and irradiance, while supporting intuitive multi-modal controls with reference images and text prompts for both global and local regions. The intrinsic guidance allows accurate manipulation of color, material, geometry, and lighting, while reference images and text prompts provide intuitive adjustments in the absence of intrinsic information. To enable these functionalities, we extend the intrinsic-guided image generation model XRGB to video generation by employing a novel and efficient Hybrid Self-Attention, which ensures temporal consistency across video frames and also enhances fidelity to reference images. We further develop a Masked Cross-Attention to disentangle global and local text prompts, applying them effectively onto respective local and global regions. For generating long videos, our novel Recursive Sampling method incorporates progressive frame sampling, combining keyframe prediction and frame interpolation to maintain long-range temporal consistency while preventing error accumulation. To support the training of X2Video, we assembled a video dataset named InteriorVideo, featuring 1,154 rooms from 295 interior scenes, complete with reliable ground-truth intrinsic channel sequences and smooth camera trajectories. Both qualitative and quantitative evaluations demonstrate that X2Video can produce long, temporally consistent, and photorealistic videos guided by intrinsic conditions. Additionally, X2Video effectively accommodates multi-modal controls with reference images, global and local text prompts, and simultaneously supports editing on color, material, geometry, and lighting through parametric tuning. Project page: https://luckyhzt.github.io/x2video

