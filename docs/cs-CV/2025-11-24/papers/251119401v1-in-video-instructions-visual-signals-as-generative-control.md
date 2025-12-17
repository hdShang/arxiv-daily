---
layout: default
title: In-Video Instructions: Visual Signals as Generative Control
---

# In-Video Instructions: Visual Signals as Generative Control

**arXiv**: [2511.19401v1](https://arxiv.org/abs/2511.19401) | [PDF](https://arxiv.org/pdf/2511.19401.pdf)

**作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang

---

## 💡 一句话要点

**提出视频内指令方法，利用视觉信号实现可控图像到视频生成。**

**关键词**: `可控视频生成` `视觉指令` `图像到视频` `多对象场景` `空间感知控制`

## 📋 核心要点

1. 核心问题：如何实现细粒度可控的图像到视频生成，避免文本提示的全局性和模糊性。
2. 方法要点：在视频帧中嵌入视觉元素如文本、箭头作为指令，实现空间感知的物体动作对应。
3. 实验效果：在多个先进生成器上验证，模型能可靠解析并执行复杂多对象场景的视觉指令。

## 📄 摘要（原文）

> Large-scale video generative models have recently demonstrated strong visual capabilities, enabling the prediction of future frames that adhere to the logical and physical cues in the current observation. In this work, we investigate whether such capabilities can be harnessed for controllable image-to-video generation by interpreting visual signals embedded within the frames as instructions, a paradigm we term In-Video Instruction. In contrast to prompt-based control, which provides textual descriptions that are inherently global and coarse, In-Video Instruction encodes user guidance directly into the visual domain through elements such as overlaid text, arrows, or trajectories. This enables explicit, spatial-aware, and unambiguous correspondences between visual subjects and their intended actions by assigning distinct instructions to different objects. Extensive experiments on three state-of-the-art generators, including Veo 3.1, Kling 2.5, and Wan 2.2, show that video models can reliably interpret and execute such visually embedded instructions, particularly in complex multi-object scenarios.

