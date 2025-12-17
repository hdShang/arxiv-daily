---
layout: default
title: Coherent Audio-Visual Editing via Conditional Audio Generation Following Video Edits
---

# Coherent Audio-Visual Editing via Conditional Audio Generation Following Video Edits

**arXiv**: [2512.07209v1](https://arxiv.org/abs/2512.07209) | [PDF](https://arxiv.org/pdf/2512.07209.pdf)

**作者**: Masato Ishii, Akio Hayakawa, Takashi Shibuya, Yuki Mitsufuji

---

## 💡 一句话要点

**提出基于视频编辑的音频生成模型以增强音视频编辑一致性**

**关键词**: `音视频编辑` `条件音频生成` `视频到音频模型` `数据增强` `动态音频调整`

## 📋 核心要点

1. 核心问题：视频编辑后音频与视觉变化不协调，影响音视频一致性。
2. 方法要点：构建视频到音频生成模型，结合源音频、目标视频和文本提示进行条件生成。
3. 实验或效果：实验显示方法在音视频对齐和内容完整性上优于现有方法。

## 📄 摘要（原文）

> We introduce a novel pipeline for joint audio-visual editing that enhances the coherence between edited video and its accompanying audio. Our approach first applies state-of-the-art video editing techniques to produce the target video, then performs audio editing to align with the visual changes. To achieve this, we present a new video-to-audio generation model that conditions on the source audio, target video, and a text prompt. We extend the model architecture to incorporate conditional audio input and propose a data augmentation strategy that improves training efficiency. Furthermore, our model dynamically adjusts the influence of the source audio based on the complexity of the edits, preserving the original audio structure where possible. Experimental results demonstrate that our method outperforms existing approaches in maintaining audio-visual alignment and content integrity.

