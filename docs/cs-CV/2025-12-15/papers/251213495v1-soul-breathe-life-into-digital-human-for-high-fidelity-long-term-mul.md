---
layout: default
title: Soul: Breathe Life into Digital Human for High-fidelity Long-term Multimodal Animation
---

# Soul: Breathe Life into Digital Human for High-fidelity Long-term Multimodal Animation

**arXiv**: [2512.13495v1](https://arxiv.org/abs/2512.13495) | [PDF](https://arxiv.org/pdf/2512.13495.pdf)

**作者**: Jiangning Zhang, Junwei Zhu, Zhenye Gan, Donghao Luo, Chuming Lin, Feifan Xu, Xu Peng, Jianlong Hu, Yuansen Liu, Yijia Hong, Weijian Cao, Han Feng, Xu Chen, Chencan Fu, Keke He, Xiaobin Hu, Chengjie Wang

---

## 💡 一句话要点

**提出Soul框架，通过多模态输入生成高保真长时数字人动画，应用于虚拟主播和影视制作。**

**关键词**: `数字人动画` `多模态生成` `长时一致性` `唇同步` `蒸馏训练` `数据集构建`

## 📋 核心要点

1. 核心问题：数字人动画面临数据稀缺、长期生成一致性差和推理效率低等挑战。
2. 方法要点：基于Wan2.2-5B骨干，集成音频注入层、阈值感知码本替换和蒸馏策略，优化生成质量与速度。
3. 实验或效果：构建Soul-1M数据集和Soul-Bench基准，在视频质量、唇同步和身份保持上显著超越现有模型。

## 📄 摘要（原文）

> We propose a multimodal-driven framework for high-fidelity long-term digital human animation termed $\textbf{Soul}$, which generates semantically coherent videos from a single-frame portrait image, text prompts, and audio, achieving precise lip synchronization, vivid facial expressions, and robust identity preservation. We construct Soul-1M, containing 1 million finely annotated samples with a precise automated annotation pipeline (covering portrait, upper-body, full-body, and multi-person scenes) to mitigate data scarcity, and we carefully curate Soul-Bench for comprehensive and fair evaluation of audio-/text-guided animation methods. The model is built on the Wan2.2-5B backbone, integrating audio-injection layers and multiple training strategies together with threshold-aware codebook replacement to ensure long-term generation consistency. Meanwhile, step/CFG distillation and a lightweight VAE are used to optimize inference efficiency, achieving an 11.4$\times$ speedup with negligible quality loss. Extensive experiments show that Soul significantly outperforms current leading open-source and commercial models on video quality, video-text alignment, identity preservation, and lip-synchronization accuracy, demonstrating broad applicability in real-world scenarios such as virtual anchors and film production. Project page at https://zhangzjn.github.io/projects/Soul/

