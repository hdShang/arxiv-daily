---
layout: default
title: Visual Generation Tuning
---

# Visual Generation Tuning

**arXiv**: [2511.23469v1](https://arxiv.org/abs/2511.23469) | [PDF](https://arxiv.org/pdf/2511.23469.pdf)

**作者**: Jiahao Guo, Sinan Du, Jingfeng Yao, Wenyu Liu, Bo Li, Haoxiang Cao, Kun Gai, Chun Yuan, Kai Wu, Xinggang Wang

---

## 💡 一句话要点

**提出视觉生成调优（VGT）以激发视觉语言模型的视觉生成潜力，降低对齐成本并加速收敛。**

**关键词**: `视觉生成调优` `视觉语言模型` `自回归建模` `语义对齐` `图像重建` `统一多模态模型`

## 📋 核心要点

1. 核心问题：视觉语言模型在视觉生成任务中的潜力未充分探索，现有方法对齐成本高。
2. 方法要点：通过语义编码器与像素解码器对齐，构建VGT-AE，实现高效视觉生成调优。
3. 实验或效果：在图像重建和生成任务中取得优异性能，如26.67 PSNR和0.77 GenEval分数，并展示扩展潜力。

## 📄 摘要（原文）

> Large Vision Language Models (VLMs) effectively bridge the modality gap through extensive pretraining, acquiring sophisticated visual representations aligned with language. However, it remains underexplored whether these representations, optimized for multimodal understanding tasks, harbor an inherent potential for visual generation. In this paper, we propose VGT, Visual Generation Tuning, a novel paradigm designed to stimulate the underlying capabilities of visual generation within any vision language models. By performing efficient visual generation tuning on well-pretrained VLMs, we significantly mitigate the alignment costs and accelerate the convergence of autoregressive modeling in the continuous space (20x speedup). Specifically, we dismiss the entangled pixel-level VAEs designed for diffusion transformers and formulate VGT-AE through aligning the semantic encoders from pretrained VLMs with the latent representations of pixel decoders. In image reconstruction tasks, we achieve 26.67 PSNR and 0.50 rFID at a 28x compression ratio, outperforming specialized VAEs; in visual generation tasks, we achieve state-of-the-art outcomes among autoregressive models, 0.77 on GenEval and 78.73 on DPG-Bench. Furthermore, our proposed VGT showcases significant scaling promise and is versatile for endowing any VLMs trained for multimodal understanding with the capabilities of visual generation, which paves the new avenue to explore next-generation unified multimodal foundation models. Models and codes are available at https://github.com/hustvl/VGT.

