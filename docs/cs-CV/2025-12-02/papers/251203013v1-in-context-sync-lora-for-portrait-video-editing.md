---
layout: default
title: In-Context Sync-LoRA for Portrait Video Editing
---

# In-Context Sync-LoRA for Portrait Video Editing

**arXiv**: [2512.03013v1](https://arxiv.org/abs/2512.03013) | [PDF](https://arxiv.org/pdf/2512.03013.pdf)

**作者**: Sagi Polaczek, Or Patashnik, Ali Mahdavi-Amiri, Daniel Cohen-Or

---

## 💡 一句话要点

**提出Sync-LoRA方法以解决肖像视频编辑中保持时序同步的挑战**

**关键词**: `肖像视频编辑` `时序同步` `扩散模型` `LoRA训练` `身份一致性` `视频生成`

## 📋 核心要点

1. 核心问题：肖像视频编辑需在修改外观时保持帧级时序同步与身份一致性
2. 方法要点：使用图像到视频扩散模型，通过训练上下文LoRA结合源视频运动与编辑首帧视觉变化
3. 实验或效果：在紧凑数据集上训练，泛化至未见身份与多样编辑，实现高视觉保真度和强时序连贯性

## 📄 摘要（原文）

> Editing portrait videos is a challenging task that requires flexible yet precise control over a wide range of modifications, such as appearance changes, expression edits, or the addition of objects. The key difficulty lies in preserving the subject's original temporal behavior, demanding that every edited frame remains precisely synchronized with the corresponding source frame. We present Sync-LoRA, a method for editing portrait videos that achieves high-quality visual modifications while maintaining frame-accurate synchronization and identity consistency. Our approach uses an image-to-video diffusion model, where the edit is defined by modifying the first frame and then propagated to the entire sequence. To enable accurate synchronization, we train an in-context LoRA using paired videos that depict identical motion trajectories but differ in appearance. These pairs are automatically generated and curated through a synchronization-based filtering process that selects only the most temporally aligned examples for training. This training setup teaches the model to combine motion cues from the source video with the visual changes introduced in the edited first frame. Trained on a compact, highly curated set of synchronized human portraits, Sync-LoRA generalizes to unseen identities and diverse edits (e.g., modifying appearance, adding objects, or changing backgrounds), robustly handling variations in pose and expression. Our results demonstrate high visual fidelity and strong temporal coherence, achieving a robust balance between edit fidelity and precise motion preservation.

