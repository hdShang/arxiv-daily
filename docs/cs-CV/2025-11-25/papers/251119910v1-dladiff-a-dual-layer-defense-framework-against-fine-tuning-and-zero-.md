---
layout: default
title: DLADiff: A Dual-Layer Defense Framework against Fine-Tuning and Zero-Shot Customization of Diffusion Models
---

# DLADiff: A Dual-Layer Defense Framework against Fine-Tuning and Zero-Shot Customization of Diffusion Models

**arXiv**: [2511.19910v1](https://arxiv.org/abs/2511.19910) | [PDF](https://arxiv.org/pdf/2511.19910.pdf)

**作者**: Jun Jia, Hongyi Miao, Yingjie Zhou, Linhan Cao, Yanwei Jiang, Wangqiu Zhou, Dandan Zhu, Hua Yang, Wei Sun, Xiongkuo Min, Guangtao Zhai

---

## 💡 一句话要点

**提出DLADiff框架以防御扩散模型的微调与零样本定制攻击**

**关键词**: `扩散模型防御` `面部隐私保护` `对抗训练` `零样本生成` `微调攻击`

## 📋 核心要点

1. 核心问题：扩散模型定制化技术威胁面部隐私，现有防御多忽略零样本方法
2. 方法要点：采用双层机制，结合DSUR和ADFT对抗微调，简单层防御零样本生成
3. 实验或效果：实验显示在防御微调和零样本生成上显著优于现有方法

## 📄 摘要（原文）

> With the rapid advancement of diffusion models, a variety of fine-tuning methods have been developed, enabling high-fidelity image generation with high similarity to the target content using only 3 to 5 training images. More recently, zero-shot generation methods have emerged, capable of producing highly realistic outputs from a single reference image without altering model weights. However, technological advancements have also introduced significant risks to facial privacy. Malicious actors can exploit diffusion model customization with just a few or even one image of a person to create synthetic identities nearly identical to the original identity. Although research has begun to focus on defending against diffusion model customization, most existing defense methods target fine-tuning approaches and neglect zero-shot generation defenses. To address this issue, this paper proposes Dual-Layer Anti-Diffusion (DLADiff) to defense both fine-tuning methods and zero-shot methods. DLADiff contains a dual-layer protective mechanism. The first layer provides effective protection against unauthorized fine-tuning by leveraging the proposed Dual-Surrogate Models (DSUR) mechanism and Alternating Dynamic Fine-Tuning (ADFT), which integrates adversarial training with the prior knowledge derived from pre-fine-tuned models. The second layer, though simple in design, demonstrates strong effectiveness in preventing image generation through zero-shot methods. Extensive experimental results demonstrate that our method significantly outperforms existing approaches in defending against fine-tuning of diffusion models and achieves unprecedented performance in protecting against zero-shot generation.

