---
layout: default
title: SneakPeek: Future-Guided Instructional Streaming Video Generation
---

# SneakPeek: Future-Guided Instructional Streaming Video Generation

**arXiv**: [2512.13019v1](https://arxiv.org/abs/2512.13019) | [PDF](https://arxiv.org/pdf/2512.13019.pdf)

**作者**: Cheeun Hong, German Barquero, Fadime Sener, Markos Georgopoulos, Edgar Schönfeld, Stefan Popov, Yuming Du, Oscar Mañas, Albert Pumarola

---

## 💡 一句话要点

**提出SneakPeek框架，通过未来引导的流式生成解决教学视频中长序列动作的时序一致性和可控性问题。**

**关键词**: `教学视频生成` `时序一致性` `扩散模型` `流式生成` `多步骤控制` `未来预测`

## 📋 核心要点

1. 核心问题：现有视频扩散模型在生成多步骤教学视频时，难以保持时序一致性和可控性。
2. 方法要点：引入预测因果适应、未来引导自强制和多提示条件化，以增强一致性和交互控制。
3. 实验或效果：实验表明，该方法能生成时序连贯、语义忠实且准确遵循复杂多步骤描述的教学视频。

## 📄 摘要（原文）

> Instructional video generation is an emerging task that aims to synthesize coherent demonstrations of procedural activities from textual descriptions. Such capability has broad implications for content creation, education, and human-AI interaction, yet existing video diffusion models struggle to maintain temporal consistency and controllability across long sequences of multiple action steps. We introduce a pipeline for future-driven streaming instructional video generation, dubbed SneakPeek, a diffusion-based autoregressive framework designed to generate precise, stepwise instructional videos conditioned on an initial image and structured textual prompts. Our approach introduces three key innovations to enhance consistency and controllability: (1) predictive causal adaptation, where a causal model learns to perform next-frame prediction and anticipate future keyframes; (2) future-guided self-forcing with a dual-region KV caching scheme to address the exposure bias issue at inference time; (3) multi-prompt conditioning, which provides fine-grained and procedural control over multi-step instructions. Together, these components mitigate temporal drift, preserve motion consistency, and enable interactive video generation where future prompt updates dynamically influence ongoing streaming video generation. Experimental results demonstrate that our method produces temporally coherent and semantically faithful instructional videos that accurately follow complex, multi-step task descriptions.

