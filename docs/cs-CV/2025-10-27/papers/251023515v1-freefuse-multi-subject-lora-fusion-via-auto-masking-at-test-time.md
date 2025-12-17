---
layout: default
title: FreeFuse: Multi-Subject LoRA Fusion via Auto Masking at Test Time
---

# FreeFuse: Multi-Subject LoRA Fusion via Auto Masking at Test Time

**arXiv**: [2510.23515v1](https://arxiv.org/abs/2510.23515) | [PDF](https://arxiv.org/pdf/2510.23515.pdf)

**作者**: Yaoli Liu, Yao-Xiang Ding, Kun Zhou

---

## 💡 一句话要点

**提出FreeFuse以通过自动掩码融合多主题LoRA实现免训练多主题图像生成**

**关键词**: `多主题图像生成` `LoRA融合` `免训练方法` `动态掩码` `交叉注意力` `文本到图像生成`

## 📋 核心要点

1. 核心问题：现有方法依赖预融合或复杂分割技术，难以高效生成多主题图像。
2. 方法要点：利用交叉注意力权重自动生成动态掩码，在推理时直接应用于LoRA输出。
3. 实验或效果：在生成质量和可用性上优于现有方法，无需额外训练或辅助模型。

## 📄 摘要（原文）

> This paper proposes FreeFuse, a novel training-free approach for
> multi-subject text-to-image generation through automatic fusion of multiple
> subject LoRAs. In contrast to existing methods that either focus on
> pre-inference LoRA weight merging or rely on segmentation models and complex
> techniques like noise blending to isolate LoRA outputs, our key insight is that
> context-aware dynamic subject masks can be automatically derived from
> cross-attention layer weights. Mathematical analysis shows that directly
> applying these masks to LoRA outputs during inference well approximates the
> case where the subject LoRA is integrated into the diffusion model and used
> individually for the masked region. FreeFuse demonstrates superior practicality
> and efficiency as it requires no additional training, no modification to LoRAs,
> no auxiliary models, and no user-defined prompt templates or region
> specifications. Alternatively, it only requires users to provide the LoRA
> activation words for seamless integration into standard workflows. Extensive
> experiments validate that FreeFuse outperforms existing approaches in both
> generation quality and usability under the multi-subject generation tasks. The
> project page is at https://future-item.github.io/FreeFuse/

