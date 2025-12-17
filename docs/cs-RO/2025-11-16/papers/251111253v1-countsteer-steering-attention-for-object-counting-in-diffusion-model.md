---
layout: default
title: CountSteer: Steering Attention for Object Counting in Diffusion Models
---

# CountSteer: Steering Attention for Object Counting in Diffusion Models

**arXiv**: [2511.11253v1](https://arxiv.org/abs/2511.11253) | [PDF](https://arxiv.org/pdf/2511.11253.pdf)

**作者**: Hyemin Boo, Hyoryung Kim, Myungjin Lee, Seunghyeon Lee, Jiyoung Lee, Jang-Hwan Choi, Hyunsoo Cho

---

## 💡 一句话要点

**提出CountSteer以改进扩散模型中的对象计数准确性**

**关键词**: `扩散模型` `对象计数` `注意力引导` `文本到图像生成` `训练无关方法`

## 📋 核心要点

1. 扩散模型在文本到图像生成中难以遵循数字指令，存在语言与视觉表示差距
2. 通过引导推理时的交叉注意力隐藏状态，无需训练即可提升对象计数准确性
3. 实验显示计数准确率提高约4%，且不损害视觉质量

## 📄 摘要（原文）

> Text-to-image diffusion models generate realistic and coherent images but often fail to follow numerical instructions in text, revealing a gap between language and visual representation. Interestingly, we found that these models are not entirely blind to numbers-they are implicitly aware of their own counting accuracy, as their internal signals shift in consistent ways depending on whether the output meets the specified count. This observation suggests that the model already encodes a latent notion of numerical correctness, which can be harnessed to guide generation more precisely. Building on this intuition, we introduce CountSteer, a training-free method that improves generation of specified object counts by steering the model's cross-attention hidden states during inference. In our experiments, CountSteer improved object-count accuracy by about 4% without compromising visual quality, demonstrating a simple yet effective step toward more controllable and semantically reliable text-to-image generation.

