---
layout: default
title: Unified Diffusion Transformer for High-fidelity Text-Aware Image Restoration
---

# Unified Diffusion Transformer for High-fidelity Text-Aware Image Restoration

**arXiv**: [2512.08922v1](https://arxiv.org/abs/2512.08922) | [PDF](https://arxiv.org/pdf/2512.08922.pdf)

**作者**: Jin Hyeon Kim, Paul Hyunbin Cho, Claire Kim, Jaewon Min, Jaeeun Lee, Jihye Park, Yeji Choi, Seungryong Kim

---

## 💡 一句话要点

**提出UniT统一框架，通过集成扩散Transformer、视觉语言模型和文本定位模块，解决文本感知图像恢复中的文本幻觉问题。**

**关键词**: `文本感知图像恢复` `扩散Transformer` `视觉语言模型` `文本定位模块` `文本幻觉抑制` `高保真文本恢复`

## 📋 核心要点

1. 核心问题：扩散模型在文本感知图像恢复中因缺乏显式语言知识，常产生文本幻觉。
2. 方法要点：结合VLM提取文本指导，TSM迭代优化OCR预测，DiT利用这些线索恢复精细文本并抑制幻觉。
3. 实验或效果：在SA-Text和Real-Text基准测试中，UniT显著减少幻觉，实现最先进的端到端F1分数性能。

## 📄 摘要（原文）

> Text-Aware Image Restoration (TAIR) aims to recover high- quality images from low-quality inputs containing degraded textual content. While diffusion models provide strong gen- erative priors for general image restoration, they often pro- duce text hallucinations in text-centric tasks due to the ab- sence of explicit linguistic knowledge. To address this, we propose UniT, a unified text restoration framework that in- tegrates a Diffusion Transformer (DiT), a Vision-Language Model (VLM), and a Text Spotting Module (TSM) in an it- erative fashion for high-fidelity text restoration. In UniT, the VLM extracts textual content from degraded images to provide explicit textual guidance. Simultaneously, the TSM, trained on diffusion features, generates intermedi- ate OCR predictions at each denoising step, enabling the VLM to iteratively refine its guidance during the denoising process. Finally, the DiT backbone, leveraging its strong representational power, exploit these cues to recover fine- grained textual content while effectively suppressing text hallucinations. Experiments on the SA-Text and Real-Text benchmarks demonstrate that UniT faithfully reconstructs degraded text, substantially reduces hallucinations, and achieves state-of-the-art end-to-end F1-score performance in TAIR task.

