---
layout: default
title: Canvas-to-Image: Compositional Image Generation with Multimodal Controls
---

# Canvas-to-Image: Compositional Image Generation with Multimodal Controls

**arXiv**: [2511.21691v1](https://arxiv.org/abs/2511.21691) | [PDF](https://arxiv.org/pdf/2511.21691.pdf)

**作者**: Yusuf Dalva, Guocheng Gordon Qian, Maya Goldenberg, Tsai-Shien Chen, Kfir Aberman, Sergey Tulyakov, Pinar Yanardag, Kuan-Chieh Jackson Wang

---

## 💡 一句话要点

**提出Canvas-to-Image框架以解决多模态控制图像生成中的忠实性问题**

**关键词**: `多模态控制` `图像生成` `扩散模型` `画布编码` `多任务训练` `忠实性评估`

## 📋 核心要点

1. 核心问题：扩散模型难以同时处理文本、参考、空间等多模态控制，导致生成图像不忠实
2. 方法要点：将异质控制编码为单一画布图像，通过多任务训练实现统一推理
3. 实验或效果：在多人组合、姿态控制等基准上，身份保持和控制依从性显著优于现有方法

## 📄 摘要（原文）

> While modern diffusion models excel at generating high-quality and diverse images, they still struggle with high-fidelity compositional and multimodal control, particularly when users simultaneously specify text prompts, subject references, spatial arrangements, pose constraints, and layout annotations. We introduce Canvas-to-Image, a unified framework that consolidates these heterogeneous controls into a single canvas interface, enabling users to generate images that faithfully reflect their intent. Our key idea is to encode diverse control signals into a single composite canvas image that the model can directly interpret for integrated visual-spatial reasoning. We further curate a suite of multi-task datasets and propose a Multi-Task Canvas Training strategy that optimizes the diffusion model to jointly understand and integrate heterogeneous controls into text-to-image generation within a unified learning paradigm. This joint training enables Canvas-to-Image to reason across multiple control modalities rather than relying on task-specific heuristics, and it generalizes well to multi-control scenarios during inference. Extensive experiments show that Canvas-to-Image significantly outperforms state-of-the-art methods in identity preservation and control adherence across challenging benchmarks, including multi-person composition, pose-controlled composition, layout-constrained generation, and multi-control generation.

