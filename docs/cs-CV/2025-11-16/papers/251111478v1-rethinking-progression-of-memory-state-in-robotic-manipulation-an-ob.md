---
layout: default
title: Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective
---

# Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective

**arXiv**: [2511.11478v1](https://arxiv.org/abs/2511.11478) | [PDF](https://arxiv.org/pdf/2511.11478.pdf)

**作者**: Nhat Chung, Taisei Hanyu, Toan Nguyen, Huy Le, Frederick Bumgarner, Duy Minh Ho Nguyen, Khoa Vo, Kashu Yamazaki, Chase Rainwater, Tung Kieu, Anh Nguyen, Ngan Le

---

## 💡 一句话要点

**提出Embodied-SlotSSM框架以解决机器人操作中非马尔可夫推理的可扩展性问题**

**关键词**: `机器人操作` `非马尔可夫推理` `对象中心视觉` `槽位状态空间模型` `视觉语言动作模型` `长序列任务`

## 📋 核心要点

1. 核心问题：机器人操作中对象级部分可观测性导致视觉语言动作模型在长序列中推理困难
2. 方法要点：使用槽位状态空间建模和关系编码器实现时空一致的槽位身份与动作预测
3. 实验或效果：在LIBERO-Mem任务套件上验证了框架的基准性能和可扩展性

## 📄 摘要（原文）

> As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

