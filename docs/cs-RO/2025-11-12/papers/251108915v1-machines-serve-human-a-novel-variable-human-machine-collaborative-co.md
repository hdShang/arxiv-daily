---
layout: default
title: Machines Serve Human: A Novel Variable Human-machine Collaborative Compression Framework
---

# Machines Serve Human: A Novel Variable Human-machine Collaborative Compression Framework

**arXiv**: [2511.08915v1](https://arxiv.org/abs/2511.08915) | [PDF](https://arxiv.org/pdf/2511.08915.pdf)

**作者**: Zifu Zhang, Shengxi Li, Xiancheng Sun, Mai Xu, Zhengyuan Liu, Jingyuan Xia

---

## 💡 一句话要点

**提出Diff-FCHM框架，基于机器视觉压缩实现人机协作压缩，提升性能。**

**关键词**: `人机协作压缩` `机器视觉压缩` `扩散先验` `特征压缩` `可变比特率策略`

## 📋 核心要点

1. 现有方法基于人视觉压缩，导致复杂度和比特率问题。
2. 新方法以机器视觉压缩为基础，聚合语义并利用扩散先验恢复细节。
3. 实验显示在机器和人类视觉压缩上均取得显著性能提升。

## 📄 摘要（原文）

> Human-machine collaborative compression has been receiving increasing research efforts for reducing image/video data, serving as the basis for both human perception and machine intelligence. Existing collaborative methods are dominantly built upon the de facto human-vision compression pipeline, witnessing deficiency on complexity and bit-rates when aggregating the machine-vision compression. Indeed, machine vision solely focuses on the core regions within the image/video, requiring much less information compared with the compressed information for human vision. In this paper, we thus set out the first successful attempt by a novel collaborative compression method based on the machine-vision-oriented compression, instead of human-vision pipeline. In other words, machine vision serves as the basis for human vision within collaborative compression. A plug-and-play variable bit-rate strategy is also developed for machine vision tasks. Then, we propose to progressively aggregate the semantics from the machine-vision compression, whilst seamlessly tailing the diffusion prior to restore high-fidelity details for human vision, thus named as diffusion-prior based feature compression for human and machine visions (Diff-FCHM). Experimental results verify the consistently superior performances of our Diff-FCHM, on both machine-vision and human-vision compression with remarkable margins. Our code will be released upon acceptance.

